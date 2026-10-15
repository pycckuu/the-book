"""CSV-only integrity regression. Never imports model.py or executes run.py.

python3 test_check_saved.py --archive saved-results.zip --out NEW_DIRECTORY --suite final-selfcheck
The archive is the unchanged accepted 100 s fixture, not a generated trajectory.
"""
import argparse
import csv
import hashlib
import io
import json
import platform
from collections import Counter
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import zipfile

ROOT = Path(__file__).resolve().parent
FILES = ('case-settings.csv', 'step-ledger.csv', 'comparison.csv', 'verification.csv')
CASES = {'forward', 'reverse', 'equilibrium', 'A_only', 'B_only', 'empty', 'partial_final_step'}

# Exact accepted case identities and literal independent diagnostic oracles.
SELECTED_RETAINED = ('complete_frozen', 'runner_before_saved_metrics', 'headers_only', 'missing_case', 'missing_run', 'missing_quantity_group', 'missing_comparison_time', 'missing_terminal_interval', 'missing_verification_metric', 'partial_saved_metric_group', 'duplicate_verification.csv', 'NaN_case-settings.csv', 'NaN_step-ledger.csv', 'NaN_comparison.csv', 'NaN_verification.csv', 'positive_infinity_verification.csv', 'negative_infinity_verification.csv', 'forbidden_blank_verification.csv', 'nonfinite_threshold', 'illegal_initial_zero_for_null', 'wrong_null_reason', 'nonfinite_reduction', 'blank_normalizer')
EXPECTED_IDS = ('complete_frozen', 'runner_before_saved_metrics', 'headers_only', 'missing_case', 'missing_run', 'missing_quantity_group', 'missing_comparison_time', 'missing_terminal_interval', 'missing_verification_metric', 'partial_saved_metric_group', 'duplicate_verification.csv', 'NaN_case-settings.csv', 'NaN_step-ledger.csv', 'NaN_comparison.csv', 'NaN_verification.csv', 'positive_infinity_verification.csv', 'negative_infinity_verification.csv', 'forbidden_blank_verification.csv', 'nonfinite_threshold', 'illegal_initial_zero_for_null', 'wrong_null_reason', 'nonfinite_reduction', 'blank_normalizer', 'C2_genuine_FAIL_relabelled_PASS', 'missing_final_group', 'final_not_preappend', 'C1_saved_FAIL', 'forged_value_PASS', 'rescaled_normalizer', 'altered_threshold', 'altered_normalized_value', 'altered_status', 'altered_unit', 'altered_criterion', 'unknown_saved_metric', 'duplicate_saved_metric', 'C2_final_count_forged')
POSITIVE_ALIASES = {'valid_final_default': 'complete_frozen', 'valid_preappend_explicit': 'runner_before_saved_metrics'}
DIAGNOSTICS = {'headers_only': "ValueError: case-settings.csv case IDs: declared coverage mismatch; missing 'A_only'; unexpected None", 'missing_case': "ValueError: case-settings.csv case IDs: declared coverage mismatch; missing 'forward'; unexpected None", 'missing_run': "ValueError: step-ledger.csv run groups: declared coverage mismatch; missing ('forward', 'forward:50s'); unexpected None", 'missing_quantity_group': "ValueError: comparison.csv groups: declared coverage mismatch; missing ('reverse', 'reverse:400s', 'snapshots-401', 'Xi_minus'); unexpected None", 'missing_comparison_time': "ValueError: comparison.csv times ('forward', 'forward:400s', 'snapshots-401', 'c_A'): declared coverage mismatch; missing 0.0; unexpected None", 'missing_terminal_interval': "ValueError: step-ledger.csv times ('forward', 'forward:100s'): declared coverage mismatch; missing 80000.0; unexpected None", 'missing_verification_metric': "ValueError: verification.csv metric IDs: declared coverage mismatch; missing ('B01', 'all', 'global', 'algebra', 'invalid_inputs_rejected'); unexpected None", 'partial_saved_metric_group': 'ValueError: verification.csv saved-CSV group field metric: final phase requires exactly 11 declared metrics', 'duplicate_verification.csv': "ValueError: verification.csv record 2 ('all', 'global', 'B01', 'invalid_inputs_rejected'): duplicate verification logical key", 'NaN_case-settings.csv': "ValueError: case-settings.csv record 1 ('forward',): nonfinite numeric field T_K", 'NaN_step-ledger.csv': "ValueError: step-ledger.csv record 1 ('forward', 'forward:100s', '0'): nonfinite numeric field n_A", 'NaN_comparison.csv': "ValueError: comparison.csv record 1 ('forward', 'forward:400s', '0'): nonfinite numeric field reference_value", 'NaN_verification.csv': "ValueError: verification.csv record 1 ('all', 'global', 'B01', 'invalid_inputs_rejected'): nonfinite numeric field value", 'positive_infinity_verification.csv': "ValueError: verification.csv record 1 ('all', 'global', 'B01', 'invalid_inputs_rejected'): nonfinite numeric field value", 'negative_infinity_verification.csv': "ValueError: verification.csv record 1 ('all', 'global', 'B01', 'invalid_inputs_rejected'): nonfinite numeric field value", 'forbidden_blank_verification.csv': "ValueError: verification.csv record 1 ('all', 'global', 'B01', 'invalid_inputs_rejected'): forbidden blank/value in value", 'nonfinite_threshold': "ValueError: verification.csv record 1 ('all', 'global', 'B01', 'invalid_inputs_rejected'): nonfinite numeric field threshold_upper", 'illegal_initial_zero_for_null': "ValueError: step-ledger.csv record 1 ('forward', 'forward:100s', '0'): forbidden blank/value in actual_h_s", 'wrong_null_reason': "ValueError: step-ledger.csv record 1 ('forward', 'forward:100s', '0'): incorrect null_reason", 'nonfinite_reduction': "ValueError: step-ledger.csv record 1 ('forward', 'forward:100s', '0'): nonfinite reconstruction residual saved_amount", 'blank_normalizer': "ValueError: verification.csv record 1 ('all', 'global', 'B01', 'invalid_inputs_rejected'): forbidden blank/value in normalizer", 'missing_final_group': 'ValueError: verification.csv saved-CSV group field metric: final phase requires exactly 11 declared metrics', 'final_not_preappend': 'ValueError: verification.csv saved-CSV group field metric: pre-append phase requires group absent', 'C1_saved_FAIL': 'ValueError: verification.csv saved-CSV metric saved_amount field value: recorded/reconstructed mismatch', 'forged_value_PASS': 'ValueError: verification.csv saved-CSV metric saved_amount field value: recorded/reconstructed mismatch', 'rescaled_normalizer': 'ValueError: verification.csv saved-CSV metric saved_amount field normalizer: recorded/reconstructed mismatch', 'altered_threshold': 'ValueError: verification.csv saved-CSV metric saved_amount field threshold_upper: recorded/reconstructed mismatch', 'altered_normalized_value': 'ValueError: verification.csv saved-CSV metric saved_amount field normalized_value: recorded/reconstructed mismatch', 'altered_status': 'ValueError: verification.csv saved-CSV metric saved_amount field status: recorded/reconstructed mismatch', 'altered_unit': 'ValueError: verification.csv saved-CSV metric saved_amount field unit: recorded/reconstructed mismatch', 'altered_criterion': 'ValueError: verification.csv saved-CSV metric saved_amount field criterion: recorded/reconstructed mismatch', 'unknown_saved_metric': 'ValueError: verification.csv saved-CSV metric unknown_saved_metric field metric: undeclared metric', 'duplicate_saved_metric': 'ValueError: verification.csv saved-CSV metric saved_amount field metric: duplicate logical key', 'C2_final_count_forged': 'ValueError: verification.csv saved-CSV metric saved_schema_ID_support_null_status_mismatch_count field value: recorded/reconstructed mismatch'}
ARCHIVE_SHA256 = 'bc32f1bf7ba77339c3fec2e9780e73a56219ccfa90bf4430b87dda858bc6c0df'
C1_SHA256 = 'c2d07f618d715e46c543f43b5f9626cdff6f08c092abb4cdf675ea8d35c4727c'
C2_SHA256 = 'f804e08da9317465f7bc3b528c7353958a6e3168a27f5b536c081953baa30d0c'


def run_tests(archive, out):
    out.mkdir(parents=True, exist_ok=False)
    if hashlib.sha256(archive.read_bytes()).hexdigest() != ARCHIVE_SHA256:
        raise ValueError('Accepted archive SHA256 changed')
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
    # Existing 37 definitions above remain unchanged; omitted cases are not executed.
    controls = [c for c in controls if c[0] in SELECTED_RETAINED]
    def saved_change(rows, changes):
        return [dict(r, **changes) if r['support_id'] == 'saved-CSV' and r['metric'] == 'saved_amount' else r for r in rows]
    def c2(rows):
        return [dict(r, status='PASS') if (r['attempt_index'], r['benchmark_id'], r['case_id'], r['run_id'], r['support_id'], r['metric']) ==
                ('1', 'B06', 'forward', 'forward:400s', 'native', 'c_A_amplitude') else r for r in rows]
    def without_saved(rows):
        return [r for r in rows if r['support_id'] != 'saved-CSV']
    def extra_saved(rows, unknown):
        row = dict(next(r for r in rows if r['support_id'] == 'saved-CSV' and r['metric'] == 'saved_amount'))
        if unknown:
            row['metric'] = 'unknown_saved_metric'
        return rows + [row]
    controls += [
        ('C2_genuine_FAIL_relabelled_PASS', 'verification.csv', lambda rows: without_saved(c2(rows)), False),
        ('missing_final_group', 'verification.csv', without_saved, False),
        ('final_not_preappend', None, None, False),
        ('C1_saved_FAIL', 'verification.csv', lambda rows: saved_change(rows, dict(value='0.5', normalized_value='0.5', status='FAIL')), False),
        ('forged_value_PASS', 'verification.csv', lambda rows: saved_change(rows, dict(value='0', normalized_value='0')), False),
        ('rescaled_normalizer', 'verification.csv', lambda rows: saved_change(rows, dict(normalizer='2', normalized_value=format(float(next(r['value'] for r in rows if r['support_id']=='saved-CSV' and r['metric']=='saved_amount')) / 2, '.17g'))), False),
        ('altered_threshold', 'verification.csv', lambda rows: saved_change(rows, dict(threshold_upper='1', criterion='normalized <= 1')), False),
        ('altered_normalized_value', 'verification.csv', lambda rows: saved_change(rows, dict(normalized_value='0')), False),
        ('altered_status', 'verification.csv', lambda rows: saved_change(rows, dict(status='FAIL')), False),
        ('altered_unit', 'verification.csv', lambda rows: saved_change(rows, dict(unit='count')), False),
        ('altered_criterion', 'verification.csv', lambda rows: saved_change(rows, dict(criterion='FORGED')), False),
        ('unknown_saved_metric', 'verification.csv', lambda rows: extra_saved(rows, True), False),
        ('duplicate_saved_metric', 'verification.csv', lambda rows: extra_saved(rows, False), False),
        ('C2_final_count_forged', 'verification.csv', c2, False)]
    ids = [c[0] for c in controls]
    if tuple(ids) != EXPECTED_IDS or len(set(ids)) != 37 or POSITIVE_ALIASES != {
            'valid_final_default': 'complete_frozen', 'valid_preappend_explicit': 'runner_before_saved_metrics'}:
        raise ValueError('Exact accepted case/alias set changed')
    def serialize(rows):
        stream = io.StringIO(newline='')
        writer = csv.DictWriter(stream, fieldnames=headers['verification.csv'])
        writer.writeheader(); writer.writerows(rows)
        return stream.getvalue().encode()
    # Validate full historical mutation bytes before any checker invocation.
    c1_rows = saved_change(tables['verification.csv'], dict(value='0.5', normalized_value='0.5', status='FAIL'))
    if hashlib.sha256(serialize(c1_rows)).hexdigest() != C1_SHA256 or hashlib.sha256(serialize(c2(tables['verification.csv']))).hexdigest() != C2_SHA256:
        raise ValueError('C1/C2 historical verification.csv bytes changed')
    expected_metrics = [dict(metric=r['metric'], value=float(r['value']), normalizer=float(r['normalizer']),
                             unit=r['unit'], threshold=float(r['threshold_upper']))
                        for r in tables['verification.csv'] if r['support_id'] == 'saved-CSV']
    if len(expected_metrics) != 11:
        raise ValueError('Accepted archived self metrics changed')
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
            input_hashes = {name: hashlib.sha256((folder/name).read_bytes()).hexdigest() for name in FILES}
            phase = 'pre-append' if label in ('runner_before_saved_metrics', 'final_not_preappend', 'C2_genuine_FAIL_relabelled_PASS') else 'final'
            command = [sys.executable, '-B', str(ROOT/'check_saved.py'), str(folder)]
            if phase == 'pre-append':
                command += ['--phase', phase]
            proc = subprocess.run(command, capture_output=True)
            stdout_path, stderr_path = label+'.stdout.txt', label+'.stderr.txt'
            (out/stdout_path).write_bytes(proc.stdout); (out/stderr_path).write_bytes(proc.stderr)
            decoded, decode_errors = [], {}
            for channel, data in (('stdout', proc.stdout), ('stderr', proc.stderr)):
                try:
                    decoded.append(data.decode())
                except UnicodeDecodeError as error:
                    decoded.append(data.decode(errors='replace'))
                    decode_errors[channel] = str(error)
            stdout, stderr = decoded
            lines = [line for line in stderr.splitlines() if line.strip()]
            diagnostic = lines[-1] if lines else ''  # Do not strip the selected line.
            expected_class = 'PASS' if expected_pass else ('ARITHMETIC_FAIL' if label == 'C2_genuine_FAIL_relabelled_PASS' else 'REJECTED')
            result, parse_error = None, None
            try:
                result = json.loads(stdout)
            except (ValueError, TypeError) as error:
                parse_error = str(error)
            observed_class = ('PASS' if result['status'] == 'PASS' else 'ARITHMETIC_FAIL') if isinstance(result, dict) and result.get('status') in ('PASS', 'FAIL') else 'REJECTED'
            if expected_class == 'REJECTED':
                matched = proc.returncode == 1 and proc.stdout == b'' and diagnostic == DIAGNOSTICS[label]
            else:
                arithmetic_fail = expected_class == 'ARITHMETIC_FAIL'
                wanted_metrics = [dict(m) for m in expected_metrics]
                if arithmetic_fail:
                    wanted_metrics[-1]['value'] = 1
                matched = (proc.returncode == (1 if arithmetic_fail else 0) and proc.stderr == b'' and isinstance(result, dict)
                    and result.get('status') == ('FAIL' if arithmetic_fail else 'PASS') and result.get('phase') == phase
                    and result.get('metrics') == wanted_metrics
                    and result.get('mismatches') == (['metric status:c_A_amplitude'] if arithmetic_fail else [])
                    and result.get('row_counts') == {'ledger_rows':7425, 'comparison_rows':266580, 'verification_numeric_rows':603 if phase == 'pre-append' else 614})
            matched = matched and not decode_errors
            results.append({'control':label, 'expected_class':expected_class, 'observed_class':observed_class,
                'exit_code':proc.returncode, 'phase':phase, 'argv':command, 'expected_outcome_observed':matched,
                'stdout_path':stdout_path, 'stderr_path':stderr_path,
                'stdout_sha256':hashlib.sha256(proc.stdout).hexdigest(), 'stderr_sha256':hashlib.sha256(proc.stderr).hexdigest(),
                'diagnostic':diagnostic, 'expected_diagnostic':DIAGNOSTICS.get(label), 'JSON_parse_error':parse_error,
                'UTF8_decode_errors':decode_errors,
                'input_CSV_hashes':input_hashes, 'row_counts':result.get('row_counts') if isinstance(result,dict) else None})
            print(label, 'OK' if matched else 'UNEXPECTED', 'exit', proc.returncode, flush=True)
            for p in folder.iterdir(): p.unlink()
            folder.rmdir()
    expected_counts = {'PASS':2, 'REJECTED':34, 'ARITHMETIC_FAIL':1}
    observed_counts = dict(Counter(r['observed_class'] for r in results))
    summary = {'status':'PASS' if all(r['expected_outcome_observed'] for r in results) and observed_counts == expected_counts else 'FAIL',
        'suite':'final-selfcheck', 'case_IDs':ids, 'positive_aliases':POSITIVE_ALIASES,
        'expected_classes':expected_counts, 'observed_classes':observed_counts, 'actual_checker_invocations':len(results),
        'checker_sha256':hashlib.sha256((ROOT/'check_saved.py').read_bytes()).hexdigest(),
        'regression_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
        'source_input_pins':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'inputs').glob('*.json'))},
        'original_CSV_pins':{f:hashlib.sha256(data).hexdigest() for f,data in original.items()},
        'python':sys.version, 'executable':sys.executable, 'platform':platform.platform(),
        'solver_executions':0, 'controls':results, 'duration_s':time.monotonic()-start,
        'scope':'One CSV-only selected regression and final selfcheck suite. Historical37 remain old-code evidence, no solver or empirical/learner validation.'}
    (out/'final-selfcheck-results.json').write_text(json.dumps(summary,indent=2,allow_nan=False)+'\n')
    if summary['status'] != 'PASS':
        raise RuntimeError('Final selfcheck regressions failed; retain evidence, no rerun')


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path, default=ROOT/'saved-results.zip')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--suite', choices=('final-selfcheck',), required=True)
    args=parser.parse_args()
    run_tests(args.archive, args.out)
