"""CSV-only completeness controls through the actual standalone checker command.

python3 test_check_saved_csv.py --archive saved-results.zip --out fresh-controls
Optional --before ORIGINAL_CHECKER records the genuine prefix false PASS.
No model/solver imports. Fixed fixture assertions are independent of checker helpers.
"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--before', type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    here = Path(__file__).resolve().parent
    checker = here / 'check_saved_csv.py'
    with zipfile.ZipFile(args.archive) as archive:
        payload = {Path(name).name: archive.read(name) for name in archive.namelist() if not name.endswith('/')}
    ledgers = sorted(name for name in payload if name.endswith('-ledger.csv'))
    assert ledgers == ['high-large-step-ledger.csv', 'high-step-ledger.csv',
                       'low-large-step-ledger.csv', 'low-step-ledger.csv',
                       'transition-large-step-ledger.csv', 'transition-step-ledger.csv',
                       'zero-capacity-ledger.csv', 'zero-substrate-ledger.csv']
    decoded = {name: list(csv.DictReader(io.StringIO(payload[name].decode()))) for name in ledgers}
    assert sum(len(rows) for rows in decoded.values()) == 11693
    for name in ['zero-capacity-ledger.csv', 'zero-substrate-ledger.csv']:
        assert len(decoded[name]) == 3 and decoded[name][-1]['dt_s'] == '50.0'
        assert all(row['delta_B_mol'] == '0.0' for row in decoded[name])
    historical = json.loads(payload['saved-csv-readback.json'])
    outcomes = []

    def rewrite(root, name, transform):
        path = root / name
        with path.open(newline='') as stream:
            reader = csv.DictReader(stream)
            fields = reader.fieldnames
            rows = list(reader)
        transform(rows)
        with path.open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def manifest_change(root, transform):
        path = root / 'case-manifest.json'
        data = json.loads(path.read_text())
        transform(data)
        path.write_text(json.dumps(data) + '\n')

    def run(label, mutate, diagnostic='', before=False):
        with tempfile.TemporaryDirectory(dir=args.out) as directory:
            root = Path(directory)
            for name, data in payload.items():
                (root / name).write_bytes(data)
            mutate(root)
            command = [sys.executable, '-B', str(args.before if before else checker), str(root)]
            result = subprocess.run(command, capture_output=True, text=True)
            (args.out / (label + '.stdout.txt')).write_text(result.stdout)
            (args.out / (label + '.stderr.txt')).write_text(result.stderr)
            expected = 0 if not diagnostic else 1
            if result.returncode != expected:
                raise AssertionError(label + ': unexpected exit ' + str(result.returncode) + ': ' + result.stderr)
            if diagnostic:
                # Match the exception message, not traceback source-code snippets.
                last = result.stderr.strip().splitlines()[-1]
                assert last.startswith('ValueError: coverage: '), (label, last)
                assert diagnostic in last, (label, last)
            else:
                report = json.loads((root / 'saved-csv-readback.json').read_text())
                assert report['pass'] and not report['failures']
                if not before:
                    for key in ['ledger_files', 'rows_checked', 'failures']:
                        assert report[key] == historical[key], (label, key)
            outcomes.append({'control': label, 'checker': 'before' if before else 'candidate',
                             'exit_code': result.returncode, 'expected_diagnostic': diagnostic,
                             'actual_diagnostic': result.stderr.strip().splitlines()[-1] if result.stderr else '',
                             'expected_outcome_observed': True,
                             'stdout_file': label + '.stdout.txt', 'stderr_file': label + '.stderr.txt'})

    def prefixes(root):
        for name in ledgers:
            rewrite(root, name, lambda rows: rows.__delitem__(slice(1, None)))

    if args.before:
        run('before_eight_single_record_false_PASS', prefixes, before=True)
    run('complete_archive', lambda root: None)
    run('fresh_before_readback', lambda root: (root / 'saved-csv-readback.json').unlink())
    run('eight_single_record_prefixes', prefixes, 'high-large-step-ledger.csv missing interval')
    run('headers_only', lambda root: [rewrite(root, name, lambda rows: rows.clear()) for name in ledgers], 'empty history')
    run('missing_case_ledger', lambda root: (root / 'low-step-ledger.csv').unlink(), 'missing=')
    run('renamed_case_ledger', lambda root: (root / 'low-step-ledger.csv').rename(root / 'other-step-ledger.csv'), 'unexpected=')
    run('duplicate_case_group', lambda root: shutil.copyfile(root / 'low-step-ledger.csv', root / 'low-copy-ledger.csv'), 'unexpected=')
    run('missing_terminal_interval', lambda root: rewrite(root, 'low-step-ledger.csv', lambda rows: rows.pop()), 'low-step-ledger.csv missing interval')
    run('missing_middle_interval', lambda root: rewrite(root, 'low-step-ledger.csv', lambda rows: rows.pop(3)), 'step sequence')
    run('duplicate_step_key', lambda root: rewrite(root, 'low-step-ledger.csv', lambda rows: rows.insert(1, rows[0].copy())), 'duplicate step logical key')
    run('wrong_trajectory_endpoint', lambda root: rewrite(root, 'low-step-ledger.csv', lambda rows: next(row for row in rows if row['step'] == '462').update(t_right_s='46151')), 't_right_s differs')
    run('wrong_extension_endpoint', lambda root: rewrite(root, 'low-step-ledger.csv', lambda rows: rows[-1].update(t_right_s='50151')), 't_right_s differs')
    run('wrong_initial_time', lambda root: rewrite(root, 'low-step-ledger.csv', lambda rows: rows[0].update(t_left_s='1')), 't_left_s differs')
    run('wrong_interval_width', lambda root: rewrite(root, 'low-step-ledger.csv', lambda rows: rows[0].update(dt_s='99')), 'dt_s differs')
    run('wrong_phase_label', lambda root: rewrite(root, 'low-step-ledger.csv', lambda rows: rows[0].update(phase='event_extension')), 'phase differs')
    run('missing_extension_phase', lambda root: rewrite(root, 'low-step-ledger.csv', lambda rows: rows.__setitem__(slice(None), [row for row in rows if row['phase'] == 'trajectory'])), 'missing interval')
    run('extension_as_trajectory', lambda root: rewrite(root, 'low-step-ledger.csv', lambda rows: next(row for row in rows if row['phase'] == 'event_extension').update(phase='trajectory')), 'phase differs')
    run('wrong_zero_terminal', lambda root: rewrite(root, 'zero-capacity-ledger.csv', lambda rows: rows[-1].update(t_right_s='300')), 't_right_s differs')
    run('wrong_large_step_start', lambda root: rewrite(root, 'high-large-step-ledger.csv', lambda rows: rows[0].update(S_previous_mol_m3='0.001')), 'initial state differs')
    run('missing_manifest_case', lambda root: manifest_change(root, lambda data: data['cases'].pop('low')), 'case set differs')
    run('renamed_manifest_case', lambda root: manifest_change(root, lambda data: data['cases'].__setitem__('other', data['cases'].pop('low'))), 'case set differs')
    def duplicate_key(root):
        path = root / 'case-manifest.json'
        path.write_text(path.read_text().replace('"low": {', '"low": {}, "low": {', 1))
    run('duplicate_manifest_case', duplicate_key, 'duplicate case/manifest key low')
    run('manifest_trajectory_window', lambda root: manifest_change(root, lambda data: data['cases']['low'].update(trajectory_end_s=45000)), 'low:trajectory_end_s differs')
    run('manifest_extension_window', lambda root: manifest_change(root, lambda data: data['cases']['low'].update(event_end_s=50000)), 'low:event_end_s differs')
    run('wrong_default_declared_step', lambda root: manifest_change(root, lambda data: data.update(default_candidate_dt_s=200)), 'default_candidate_dt_s differs')
    report = {'status': 'PASS', 'checker_sha256': digest(checker), 'test_sha256': digest(Path(__file__)),
              'archive_sha256': digest(args.archive), 'original_CSV_pins': {name: hashlib.sha256(payload[name]).hexdigest() for name in ledgers},
              'declaration_pins': {name: digest(here / name) for name in ['pre-run-plan.json', 'saved-results-manifest.json']},
              'controls': outcomes, 'solver_executions': 0,
              'scope': 'Complete declared eight native ledgers only; no snapshot/reference/model or empirical revalidation.'}
    (args.out / 'regression-results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'controls': len(outcomes), 'candidate_positive': 2,
                      'candidate_negative': len(outcomes) - 2 - bool(args.before), 'solver_executions': 0}))


if __name__ == '__main__':
    main()
