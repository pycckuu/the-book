"""CSV-only integrity regression. Never imports model.py or executes run.py.

python3 test_check_saved.py --archive saved-results.zip --out NEW_DIRECTORY
The archive is the unchanged accepted 100 s fixture, not a generated trajectory.
"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import zipfile

ROOT = Path(__file__).resolve().parent
FILES = ('case-settings.csv', 'step-ledger.csv', 'comparison.csv', 'verification.csv')
CASES = {'forward', 'reverse', 'equilibrium', 'A_only', 'B_only', 'empty', 'partial_final_step'}


def run_tests(archive, out):
    out.mkdir(parents=True, exist_ok=False)
    with zipfile.ZipFile(archive) as z:
        original = {name: z.read('results-r2/' + name) for name in FILES}
    tables = {}
    headers = {}
    for name, data in original.items():
        reader = csv.DictReader(io.StringIO(data.decode()))
        headers[name], tables[name] = reader.fieldnames, list(reader)
    # Independent fixed-fixture assertions, not calls to checker coverage helpers.
    if [len(tables[f]) for f in FILES] != [7, 7425, 266580, 655]:
        raise ValueError('Regression requires the accepted complete 100 s archive')
    if {r['case_id'] for r in tables['case-settings.csv']} != CASES:
        raise ValueError('Fixture case IDs changed')
    if len({(r['case_id'], r['run_id']) for r in tables['step-ledger.csv']}) != 10:
        raise ValueError('Fixture must have six core and four auxiliary ledgers')
    if len({(r['case_id'], r['run_id'], r['support_id'], r['quantity']) for r in tables['comparison.csv']}) != 180:
        raise ValueError('Fixture comparison groups changed')
    if sum(r['status'] == 'FAIL' for r in tables['verification.csv']) != 14:
        raise ValueError('Genuine coarse FAIL history missing')
    controls = [('complete_frozen', None, None, True),
                ('runner_before_saved_metrics', 'verification.csv', lambda rows: [r for r in rows if r['support_id'] != 'saved-CSV'], True),
                ('headers_only', 'all', None, False),
                ('missing_case', 'case-settings.csv', lambda rows: rows[1:], False),
                ('missing_run', 'step-ledger.csv', lambda rows: [r for r in rows if r['run_id'] != 'forward:50s'], False),
                ('missing_quantity_group', 'comparison.csv', lambda rows: [r for r in rows if not (r['case_id']=='reverse' and r['run_id']=='reverse:400s' and r['support_id']=='snapshots-401' and r['quantity']=='Xi_minus')], False),
                ('missing_comparison_time', 'comparison.csv', lambda rows: rows[1:], False),
                ('missing_terminal_interval', 'step-ledger.csv', lambda rows: [r for r in rows if not (r['run_id']=='forward:100s' and r['time_s']=='80000')], False),
                ('missing_verification_metric', 'verification.csv', lambda rows: rows[1:], False),
                ('partial_saved_metric_group', 'verification.csv', lambda rows: [r for r in rows if not (r['support_id']=='saved-CSV' and r['metric']=='saved_BE_inverse')], False)]
    for name in FILES:
        controls.append(('duplicate_' + name, name, lambda rows: [rows[0]] + rows, False))
    fields = {'case-settings.csv':'T_K', 'step-ledger.csv':'n_A', 'comparison.csv':'reference_value', 'verification.csv':'value'}
    def replacement(field, value):
        def mutate(rows):
            first = dict(rows[0]); first[field] = value
            return [first] + rows[1:]
        return mutate
    for name, field in fields.items():
        for tag, value in [('NaN','nan'), ('positive_infinity','inf'), ('negative_infinity','-inf'), ('forbidden_blank','')]:
            controls.append((tag + '_' + name, name, replacement(field, value), False))
    controls += [('nonfinite_threshold', 'verification.csv', replacement('threshold_upper','nan'), False),
                 ('finite_settings_conflict', 'case-settings.csv', replacement('T_K','300'), False),
                 ('inconsistent_default', 'case-settings.csv', replacement('nominal_h_s','50'), False),
                 ('illegal_initial_zero_for_null', 'step-ledger.csv', replacement('actual_h_s','0'), False),
                 ('wrong_null_reason', 'step-ledger.csv', replacement('null_reason','empty_batch'), False),
                 ('nonfinite_reduction', 'step-ledger.csv', replacement('n_A','1e308'), False),
                 ('blank_normalizer', 'verification.csv', replacement('normalizer',''), False)]
    results = []
    start = time.monotonic()
    with tempfile.TemporaryDirectory(prefix='csv-regression-', dir=out) as tmp:
        work = Path(tmp)
        for index, (label, target, mutate, expected_pass) in enumerate(controls):
            folder = work / str(index); folder.mkdir()
            for name, data in original.items():
                path = folder / name
                if target == 'all':
                    path.write_bytes(data.splitlines(keepends=True)[0])
                elif target == name:
                    with path.open('w', newline='') as f:
                        writer = csv.DictWriter(f, fieldnames=headers[name]); writer.writeheader(); writer.writerows(mutate(tables[name]))
                else:
                    path.write_bytes(data)
            command = [sys.executable, '-B', str(ROOT/'check_saved.py'), str(folder)]
            proc = subprocess.run(command, capture_output=True, text=True)
            (out/(label+'.stdout.txt')).write_text(proc.stdout)
            (out/(label+'.stderr.txt')).write_text(proc.stderr)
            result = json.loads(proc.stdout) if proc.returncode == 0 else None
            observed_pass = proc.returncode == 0 and result['status'] == 'PASS'
            matched = observed_pass if expected_pass else proc.returncode != 0
            if expected_pass:
                if result['row_counts']['ledger_rows'] != 7425 or result['row_counts']['comparison_rows'] != 266580:
                    matched = False
            elif not any(token in proc.stderr for token in ['case-settings.csv','step-ledger.csv','comparison.csv','verification.csv']):
                matched = False  # A negative control must identify the input family.
            if label.startswith(('NaN_', 'positive_infinity_', 'negative_infinity_', 'forbidden_blank_')):
                matched = matched and target in proc.stderr and fields[target] in proc.stderr
            results.append({'control':label,'expected':'PASS' if expected_pass else 'FAIL','exit_code':proc.returncode,
                'observed_status':result['status'] if result else 'REJECTED', 'expected_outcome_observed':matched,
                'stdout_path':label+'.stdout.txt','stderr_path':label+'.stderr.txt',
                'diagnostic':proc.stderr.strip().splitlines()[-1] if proc.stderr.strip() else '',
                'row_counts':result['row_counts'] if result else None})
            print(label, 'OK' if matched else 'UNEXPECTED', 'exit', proc.returncode, flush=True)
            # Keep logs, not disposable full-size copied tables.
            for p in folder.iterdir(): p.unlink()
            folder.rmdir()
    summary = {'status':'PASS' if all(r['expected_outcome_observed'] for r in results) else 'FAIL',
        'checker_sha256':hashlib.sha256((ROOT/'check_saved.py').read_bytes()).hexdigest(),
        'regression_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
        'original_CSV_pins':{f:hashlib.sha256(data).hexdigest() for f,data in original.items()},
        'python':sys.version,'solver_executions':0,'controls':results,'duration_s':time.monotonic()-start,
        'scope':'Complete frozen fixture and the runner pre-saved-metric phase; no fresh solver, alternate selected default or empirical validation.'}
    (out/'regression-results.json').write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n')
    if summary['status'] != 'PASS':
        raise RuntimeError('Integrity regressions failed; inspect saved stdout/stderr')


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, default=ROOT/'saved-results.zip')
    parser.add_argument('--out', type=Path, required=True)
    args=parser.parse_args()
    run_tests(args.archive, args.out)
