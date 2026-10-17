#!/usr/bin/env python3
"""Q04 entry-boundary regression, one outer driver and 27 pre-numerical probes.

Run once against an untouched Git-object baseline, with a fresh external --out.
A: ordinary candidate admission. B: optimized baseline reachability.
R: optimized candidate refusal. No numerical/teaching/comparison body is run.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import runpy
import shutil
import stat
import subprocess
import sys
import traceback

MESSAGE = 'Verification requires normal Python; remove -O/-OO and unset PYTHONOPTIMIZE.'
SNAPSHOT = 'aadefa8e9a051c64b75602944b7ea5b9fc732d921f183e2ef1d4f957ec6b2ce9'
WORKBOOKS = (
    ('Beck.Oxygen.Data.xlsx', '47b66bc3243e7b188c2b04e6599d92f1ee2da3479f06f838573e5e28709b6af4', '3aa0ff04a92467b2ebcbeba730d47d09'),
    ('latest-Beck.Oxygen.Data.xlsx', 'c5f82518fe5739c99fe7242932ea7118137fc97e9985e05d002fd02548f2cb61', '80aeb327b8ebecd9d359c1c1b5ba0e00'),
)
# Each entry owns a distinct shipped command/callable boundary.
TARGETS = {
    'OEM': ('oxygen-diffusion/en/model/oxygen_model.py', 'main', 'verify', '-O'),
    'OEV': ('oxygen-diffusion/en/model/oxygen_model.py', 'verify', 'steady', '-OO'),
    'ORM': ('oxygen-diffusion/ru/model/oxygen_model.py', 'main', 'verify', 'env1'),
    'ORV': ('oxygen-diffusion/ru/model/oxygen_model.py', 'verify', 'steady', '-O'),
    'AD': ('advection-dispersion/model/readback_exports.py', 'main', 'read', '-O'),
    'SAT': ('saturation-kinetics/model/saturation.py', 'main', 'threshold', '-OO'),
    'ENERGY': ('energy-constraints/model/run.py', 'execute', 'parameters', 'env2'),
    'TEACH': ('oxygen-diffusion/en/check_teaching.py', '<module>', 'teaching_model_load', '-O'),
    'COMP': ('oxygen-diffusion/optional-observed-data/compare_measured.py', 'main', 'read_summary', 'env2'),
}
IDS = [p + '-' + t for p in 'ABR' for t in list(TARGETS)[:7]] + [p + '-' + t for t in ('TEACH', 'COMP') for p in 'ABR']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False) + '\n')


def inventory(root, times=False, source=False):
    result = {}
    def visit(path):
        key = path.relative_to(root).as_posix()
        info = path.lstat()
        row = {'mode': stat.S_IMODE(info.st_mode)}
        if times:
            row['mtime_ns'] = info.st_mtime_ns
        if path.is_symlink():
            row.update(type='symlink', target=os.readlink(path))
        elif path.is_dir():
            row['type'] = 'directory'
        elif path.is_file():
            row.update(type='file', size=info.st_size, sha256=digest(path))
        else:
            raise RuntimeError('unsupported inventory member: ' + str(path))
        result[key] = row
        if row['type'] == 'directory':
            for child in sorted(path.iterdir()):
                if source and child.name in ('.git', '.context'):
                    continue
                visit(child)
    visit(root)
    return result


def stage_case(root, sandbox, target):
    source = root / 'courses' / TARGETS[target][0]
    members = [source]
    if target == 'TEACH':
        members.append(source.parent / 'model-snapshot/oxygen_model.py')
    elif target == 'COMP':
        members.extend(source.parent / 'data' / w[0] for w in WORKBOOKS)
    staged = []
    if target in ('TEACH', 'COMP'):
        for member in members:
            destination = sandbox / 'staged' / member.relative_to(root)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(member, destination)
            source_mode = stat.S_IMODE(member.stat().st_mode)
            if digest(destination) != digest(member) or stat.S_IMODE(destination.stat().st_mode) != source_mode or destination.stat().st_ino == member.stat().st_ino:
                raise RuntimeError('staged source/dependency bytes, mode or independence mismatch')
            staged.append({'source': str(member), 'staged': str(destination), 'sha256': digest(member), 'staged_sha256': digest(destination), 'mode': source_mode, 'staged_mode': stat.S_IMODE(destination.stat().st_mode)})
        source = sandbox / 'staged' / source.relative_to(root)
        if target == 'TEACH':
            snapshot = source.parent / 'model-snapshot/oxygen_model.py'
            if digest(snapshot) != SNAPSHOT or stat.S_IMODE(snapshot.stat().st_mode) != 0o644:
                raise RuntimeError('wrong independently pinned teaching snapshot')
        else:
            for name, sha, md5 in WORKBOOKS:
                workbook = source.parent / 'data' / name
                if digest(workbook) != sha or hashlib.md5(workbook.read_bytes()).hexdigest() != md5 or stat.S_IMODE(workbook.stat().st_mode) != 0o644:
                    raise RuntimeError('wrong independently pinned workbook: ' + name)
    for directory in (sandbox / 'existing/nested', sandbox / 'results/nested'):
        directory.mkdir(parents=True)
        (directory / 'RETAIN.bin').write_bytes(b'RETAIN\x00\xff')
    if target in ('TEACH', 'COMP'):
        directory = source.parent / ('teaching-checks' if target == 'TEACH' else 'results')
        (directory / 'nested').mkdir(parents=True)
        (directory / 'nested/RETAIN.bin').write_bytes(b'RETAIN\x00\xff')
    if target == 'AD':
        dump(sandbox / 'results/verification.json', {'status': 'PASS', 'code_sha256': digest(root / 'courses/advection-dispersion/model/advection_model.py'), 'verification_code_sha256': digest(root / 'courses/advection-dispersion/model/verify_advection.py')})
        dump(sandbox / 'results/case-manifest.json', [{'case_id': 'q04_fixture', 'parameters': {}}])
    return source, staged


def probe(args):
    phase, target = args.probe.split('-', 1)
    relative, entry, tripwire, mode = TARGETS[target]
    root, sandbox, report = args.source_root.resolve(), args.sandbox.resolve(), args.report.resolve()
    canonical = root / 'courses' / relative
    source = sandbox / 'staged' / 'courses' / relative if target in ('TEACH', 'COMP') else canonical
    source = source.resolve()
    state = {'id': args.probe, 'source': str(source), 'canonical_source': str(canonical), 'source_sha256': digest(source),
             'mode': {'optimize': sys.flags.optimize, 'debug': __debug__, 'ignore_environment': sys.flags.ignore_environment, 'isolated': sys.flags.isolated, 'PYTHONOPTIMIZE': os.environ.get('PYTHONOPTIMIZE')},
             'probe_argv': sys.argv[:], 'cwd': str(Path.cwd().resolve()), 'entry_events': [], 'tripwire_events': [],
             'write_attempts': [], 'snapshot_load_requests': [], 'prevented_unexpected_calls': [], 'original_numerical_bodies': 0,
             'original_snapshot_loader_calls': 0, 'original_read_summary_bodies': 0}
    if args.probe == 'A-AD':
        state['permitted_sha_calls'] = []
    active = [False]
    def audit(event, values):
        if not active[0]:
            return
        write = event in ('os.mkdir', 'os.remove', 'os.rmdir', 'os.rename')
        if event == 'open':
            flags = values[2]
            write = bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
        if write:
            state['write_attempts'].append({'event': event, 'args': [str(v) for v in values]})
    sys.addaudithook(audit)

    class Tripwire(BaseException):
        pass

    def stop(*unused, **kwargs):
        if args.probe == 'A-AD' and (len(state['permitted_sha_calls']) != 2 or
                                       any(row.get('returned_sha256') != row['expected_sha256'] for row in state['permitted_sha_calls'])):
            raise RuntimeError('AD source-pin helper sequence incomplete before read tripwire')
        state['tripwire_events'].append(tripwire)
        raise Tripwire()

    model_path = root / 'courses/energy-constraints/model/model.py'
    def trace(frame, event, arg):
        filename = frame.f_code.co_filename
        name = frame.f_code.co_name
        if event == 'call' and filename == str(source) and name == entry:
            state['entry_events'].append({'file': str(filename), 'entry': name, 'sha256': digest(source)})
            if target != 'TEACH':
                frame.f_globals[tripwire] = stop
        elif event in ('call', 'return') and args.probe == 'A-AD' and filename == str(source) and name == 'sha':
            expected_paths = [source.with_name('advection_model.py'), source.with_name('verify_advection.py')]
            caller = frame.f_back
            if (not __debug__ or sys.flags.optimize != 0 or
                    digest(source) != '8adb2ea0474b19a9ecb230acd76bc5a8d8f078623511b6a246562cff9db7da98' or
                    frame.f_code is not frame.f_globals['sha'].__code__ or
                    caller is None or caller.f_code is not frame.f_globals['main'].__code__ or
                    caller.f_code.co_filename != str(source) or len(state['entry_events']) != 1 or state['tripwire_events']):
                raise RuntimeError('Unexpected AD source-pin helper identity or phase')
            calls = state['permitted_sha_calls']
            index = len(calls) if event == 'call' else len(calls) - 1
            if index not in (0, 1) or Path(frame.f_locals['p']).resolve() != expected_paths[index]:
                raise RuntimeError('Unexpected AD source-pin helper argument or order')
            if event == 'call':
                calls.append({'source': str(source), 'source_sha256': digest(source),
                              'argument': str(expected_paths[index]), 'expected_sha256': digest(expected_paths[index])})
            elif 'returned_sha256' in calls[index] or arg != calls[index]['expected_sha256']:
                raise RuntimeError('Unexpected AD source-pin helper return')
            else:
                calls[index]['returned_sha256'] = arg
        elif event == 'call' and (filename == str(source) or (target == 'ENERGY' and filename == str(model_path))) and name not in ('<module>', '<dictcomp>', '<listcomp>', '<genexpr>'):
            state['prevented_unexpected_calls'].append({'file': str(filename), 'function': name})
            raise RuntimeError('Unexpected original function before tripwire: ' + name)
        return trace

    original_spec = importlib.util.spec_from_file_location
    def guarded_spec(name, location, *positional, **kwargs):
        location = Path(location).resolve()
        if name == 'verified_oxygen' or location.is_relative_to(sandbox / 'staged'):
            state['snapshot_load_requests'].append({'name': name, 'path': str(location), 'sha256': digest(location)})
            if name != 'verified_oxygen' or location != source.parent / 'model-snapshot/oxygen_model.py' or digest(location) != SNAPSHOT:
                raise RuntimeError('Unexpected teaching course-load target')
            stop()
        return original_spec(name, location, *positional, **kwargs)

    out = sandbox / 'new-parent/out'
    extra = {'OEM': ['--out', str(out)], 'ORM': ['--out', str(out)], 'AD': ['--results', str(sandbox / 'results')], 'SAT': [str(out)], 'ENERGY': ['--output', str(out)]}.get(target, [])
    sys.argv = [str(source)] + extra
    state['target_argv'] = sys.argv[:]
    sys.path.insert(0, str(source.parent))
    code = 1
    try:
        active[0] = True
        sys.settrace(trace)
        if target == 'TEACH':
            importlib.util.spec_from_file_location = guarded_spec
        if entry == 'verify':
            namespace = runpy.run_path(str(source), run_name='q04_callable')
            namespace['verify']()
        else:
            runpy.run_path(str(source), run_name='__main__')
    except Tripwire:
        code = 86
        print('NUMERICAL_TRIPWIRE:' + tripwire, file=sys.stderr)
    except BaseException as error:
        state['exception'] = {'type': type(error).__name__, 'message': str(error)}
        traceback.print_exc()
    finally:
        sys.settrace(None)
        active[0] = False
        importlib.util.spec_from_file_location = original_spec
        if target == 'ENERGY':
            imported = sys.modules.get('model')
            if imported is not None and getattr(imported, '__file__', None):
                actual = Path(imported.__file__).resolve()
                state['model_import'] = {'path': str(actual), 'sha256': digest(actual), 'expected_path': str(model_path)}
        state['exit'] = code
        dump(report, state)
    return code


def destination_errors(before, after, exact):
    if exact:
        return [] if before == after else ['whole destination snapshot differs']
    errors = []
    for name, row in before.items():
        actual = after.get(name)
        if row['type'] == 'directory' and actual is not None:
            row, actual = dict(row), dict(actual)
            row.pop('mtime_ns', None)
            actual.pop('mtime_ns', None)
        if row != actual:
            errors.append('existing destination changed: ' + name)
    for name in after.keys() - before.keys():
        if name not in ('new-parent', 'new-parent/out') or after[name]['type'] != 'directory':
            errors.append('unexpected destination addition: ' + name)
    return errors


def run_suite(args):
    candidate = Path(__file__).resolve().parents[1]
    baseline, receipt = args.baseline_root.resolve(), args.out.resolve()
    if receipt == candidate or receipt.is_relative_to(candidate) or receipt == baseline or receipt.is_relative_to(baseline):
        raise ValueError('receipt must be outside candidate and baseline roots')
    receipt.mkdir(parents=True, exist_ok=False)
    before_roots = {'candidate': inventory(candidate, source=True), 'baseline': inventory(baseline, source=True)}
    dump(receipt / 'source-roots.before.json', before_roots)
    results = []
    for identity in IDS:
        phase, target = identity.split('-', 1)
        source_root = baseline if phase == 'B' else candidate
        sandbox = receipt / 'sandboxes' / identity
        sandbox.mkdir(parents=True)
        errors = []
        result = {'id': identity, 'phase': phase, 'errors': errors, 'matched': False}
        try:
            source, staged = stage_case(source_root, sandbox, target)
            before = inventory(sandbox, times=True)
            dump(receipt / (identity + '.before.json'), before)
            dump(receipt / (identity + '.inputs.json'), {'source_root': str(source_root), 'source': str(source), 'source_sha256': digest(source), 'staged': staged, 'destination': before})
            expected_mode = 0 if phase == 'A' else (2 if TARGETS[target][3] in ('-OO', 'env2') else 1)
            mode = None if phase == 'A' else TARGETS[target][3]
            argv = [sys.executable, '-B'] + ([mode] if mode in ('-O', '-OO') else []) + [str(Path(__file__).resolve()), '--probe', identity, '--source-root', str(source_root), '--sandbox', str(sandbox), '--report', str(receipt / (identity + '.probe.json'))]
            result.update(argv=argv, cwd=str(sandbox), source_sha256=digest(source), expected_optimize=expected_mode, env_argument='omitted', temporary_parent_PYTHONOPTIMIZE=mode[-1] if mode in ('env1', 'env2') else None)
            dump(receipt / (identity + '.launch.json'), result)
            old = os.environ.get('PYTHONOPTIMIZE')
            try:
                if mode in ('env1', 'env2'):
                    os.environ['PYTHONOPTIMIZE'] = mode[-1]
                else:
                    os.environ.pop('PYTHONOPTIMIZE', None)
                with subprocess.Popen(argv, cwd=sandbox, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
                    result['pid'] = process.pid
                    stdout, stderr = process.communicate()
                    child = subprocess.CompletedProcess(argv, process.returncode, stdout, stderr)
            finally:
                if old is None:
                    os.environ.pop('PYTHONOPTIMIZE', None)
                else:
                    os.environ['PYTHONOPTIMIZE'] = old
            result['exit'] = child.returncode
            for channel, raw in [('stdout', child.stdout), ('stderr', child.stderr)]:
                (receipt / (identity + '.' + channel + '.bin')).write_bytes(raw)
                result[channel + '_sha256'] = hashlib.sha256(raw).hexdigest()
                try:
                    raw.decode('utf-8', errors='strict')
                except UnicodeDecodeError as error:
                    errors.append(channel + ' decode error: ' + str(error))
            expected_exit = 1 if phase == 'R' else 86
            expected_line = 'RuntimeError: ' + MESSAGE if phase == 'R' else 'NUMERICAL_TRIPWIRE:' + TARGETS[target][2]
            if child.returncode != expected_exit or child.stdout != b'' or not child.stderr.splitlines() or child.stderr.splitlines()[-1] != expected_line.encode('utf-8'):
                errors.append('exit/channel/last-line oracle mismatch')
            state = json.loads((receipt / (identity + '.probe.json')).read_text())
            if phase == 'R' and state.get('exception') != {'type': 'RuntimeError', 'message': MESSAGE}:
                errors.append('intended RuntimeError identity mismatch')
            mode_state = state['mode']
            if mode_state['optimize'] != expected_mode or mode_state['debug'] != (expected_mode == 0) or mode_state['isolated'] != 0 or mode_state['ignore_environment'] != 0 or mode_state['PYTHONOPTIMIZE'] != result['temporary_parent_PYTHONOPTIMIZE']:
                errors.append('actual optimization environment mismatch')
            if len(state['entry_events']) != 1 or state['source_sha256'] != digest(source) or state['source'] != str(source.resolve()):
                errors.append('entry/source mismatch')
            if state['tripwire_events'] != ([] if phase == 'R' else [TARGETS[target][2]]) or state['prevented_unexpected_calls'] or state['original_numerical_bodies'] != 0:
                errors.append('tripwire/original-body mismatch')
            if phase == 'R' or target in ('TEACH', 'COMP'):
                if state['write_attempts']:
                    errors.append('unexpected destination mkdir/write attempts')
            if target == 'TEACH' and (len(state['snapshot_load_requests']) != (0 if phase == 'R' else 1) or state['original_snapshot_loader_calls'] != 0):
                errors.append('teaching course-load mismatch')
            if target == 'COMP' and state['original_read_summary_bodies'] != 0:
                errors.append('original comparator body ran')
            if target == 'ENERGY':
                imported = state.get('model_import', {})
                model = source_root / 'courses/energy-constraints/model/model.py'
                if imported.get('path') != str(model) or imported.get('sha256') != digest(model):
                    errors.append('source-local ENERGY model import mismatch')
            after = inventory(sandbox, times=True)
            dump(receipt / (identity + '.after.json'), after)
            errors.extend(destination_errors(before, after, phase == 'R' or target in ('TEACH', 'COMP')))
            result['probe_sha256'] = digest(receipt / (identity + '.probe.json'))
        except Exception as error:
            errors.append(type(error).__name__ + ': ' + str(error))
        result['matched'] = not errors
        results.append(result)
        dump(receipt / (identity + '.result.json'), result)
    after_roots = {'candidate': inventory(candidate, source=True), 'baseline': inventory(baseline, source=True)}
    dump(receipt / 'source-roots.after.json', after_roots)
    root_errors = [] if before_roots == after_roots else ['source-root inventory changed']
    counts = {label: sum(row['type'] == 'file' for row in rows.values()) for label, rows in before_roots.items()}
    if counts != {'candidate': 430, 'baseline': 429}:
        root_errors.append('expected complete430/429 source file counts')
    passed = all(row['matched'] for row in results) and not root_errors
    final = {'status': 'PASS' if passed else 'FAIL', 'target_calls': sum('pid' in row for row in results), 'relay_parent_calls': 0, 'outer_driver_commands': 1, 'original_numerical_bodies': 0, 'source_file_counts': counts, 'source_errors': root_errors, 'results': results,
             'limits': 'Instrumented source-entry admission only. No solver, snapshot loader, original comparator/teaching computation or numerical/empirical/learner validation; no bare-command cache guarantee.'}
    dump(receipt / 'optimization-gates-results.json', final)
    print(json.dumps({'status': final['status'], 'target_calls': sum('pid' in row for row in results), 'matched': sum(row['matched'] for row in results), 'source_errors': root_errors}))
    return 0 if passed else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-root', type=Path)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--probe', choices=IDS)
    parser.add_argument('--source-root', type=Path)
    parser.add_argument('--sandbox', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    if args.probe:
        if not all((args.source_root, args.sandbox, args.report)):
            parser.error('probe requires source-root, sandbox and external report')
        return probe(args)
    if not all((args.baseline_root, args.out)):
        parser.error('suite requires baseline-root and fresh external out')
    return run_suite(args)


if __name__ == '__main__':
    sys.exit(main())
