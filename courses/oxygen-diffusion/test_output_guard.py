"""Guard-order regression only; no original numerical function is executed.

python3 test_output_guard.py --out fresh-guard-controls [--before-root OLD_COURSE]
Tripwires run at the actual __main__ entrypoint, with real argparse/filesystem.
"""
import argparse
import hashlib
import json
from pathlib import Path
import runpy
import stat
import subprocess
import sys
import tempfile


class NumericalTripwire(RuntimeError):
    pass


def probe(source, destination, default=False):
    calls = []
    mkdir_calls = []
    main_called = []
    original_mkdir = Path.mkdir

    def observed_mkdir(path, *args, **kwargs):
        mkdir_calls.append(str(path))
        return original_mkdir(path, *args, **kwargs)

    def trace(frame, event, arg):
        if event == 'call' and frame.f_code.co_name == 'main' and frame.f_code.co_filename == str(source):
            main_called.append(True)
            for name in ['verify', 'synthetic_fit', 'transient']:
                def tripwire(*args, label=name, **kwargs):
                    calls.append(label)
                    raise NumericalTripwire(label)
                frame.f_globals[name] = tripwire
        return trace

    sys.argv = [str(source)] + ([] if default else ['--out', str(destination)])
    status = 0
    Path.mkdir = observed_mkdir
    sys.settrace(trace)
    try:
        runpy.run_path(str(source), run_name='__main__')
    except NumericalTripwire as error:
        print('NUMERICAL_TRIPWIRE:' + str(error), file=sys.stderr)
        status = 86
    except SystemExit as error:
        status = error.code
    finally:
        sys.settrace(None)
        Path.mkdir = original_mkdir
    print(json.dumps({'main_called': len(main_called), 'numerical_tripwires': calls,
                      'original_numerical_executions': 0, 'mkdir_calls': mkdir_calls,
                      'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest()}))
    raise SystemExit(status)


def tree(root):
    result = {}
    for path in [root] + sorted(root.rglob('*')):
        info = path.lstat()
        record = {'mode': info.st_mode, 'mtime_ns': info.st_mtime_ns}
        if stat.S_ISLNK(info.st_mode):
            record['link'] = str(path.readlink())
        elif path.is_file():
            record['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
        result[str(path.relative_to(root))] = record
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--before-root', type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    course = Path(__file__).resolve().parent
    controls = []
    for language in ['en', 'ru']:
        modes = ['expected_files_and_nested', 'nested_only', 'empty_child_directory',
                 'default_occupied', 'symlink_to_occupied', 'existing_file',
                 'fresh', 'existing_empty', 'fresh_nested_parents']
        if args.before_root:
            modes = ['before_nonempty'] + modes
        for mode in modes:
            with tempfile.TemporaryDirectory(dir=args.out) as td:
                root = Path(td)
                default = mode == 'default_occupied'
                dest = root / ('results' if default else 'output')
                positive = mode in ['fresh', 'existing_empty', 'fresh_nested_parents']
                before = mode == 'before_nonempty'
                if mode == 'fresh_nested_parents':
                    dest = root / 'new-parent' / 'nested' / 'output'
                elif mode == 'existing_empty':
                    dest.mkdir()
                elif mode == 'existing_file':
                    dest.write_bytes(b'RETAIN existing file\x00\xff')
                elif mode == 'symlink_to_occupied':
                    target = root / 'target';target.mkdir()
                    (target / 'verification.json').write_bytes(b'RETAIN target')
                    dest.symlink_to(target, target_is_directory=True)
                elif not positive:
                    (dest / 'nested' / 'deeper').mkdir(parents=True)
                    if mode != 'empty_child_directory':
                        (dest / 'nested' / 'deeper' / 'sentinel.bin').write_bytes(b'RETAIN nested sentinel\x00\xff')
                    if mode not in ['nested_only', 'empty_child_directory']:
                        for name in ['profiles.csv', 'verification.json', 'synthetic-profile.csv']:
                            (dest / name).write_bytes(b'RETAIN original ' + name.encode() + b'\x00\xff')
                snapshot = tree(root)
                source = ((args.before_root if before else course) / language / 'model' / 'oxygen_model.py').resolve()
                command = [sys.executable, '-B', str(Path(__file__).resolve()), '--probe', str(source), str(dest)]
                if default:
                    command.append('--default')
                result = subprocess.run(command, cwd=root, capture_output=True, text=True)
                after = tree(root)
                record = json.loads(result.stdout.strip())
                assert record['main_called'] == 1
                assert record['original_numerical_executions'] == 0
                if positive or before:
                    assert result.returncode == 86 and record['numerical_tripwires'] == ['verify'], (mode, result.stderr)
                    assert record['mkdir_calls'], mode
                    if positive:
                        assert dest.is_dir() and not any(dest.iterdir()), mode
                    else:
                        assert snapshot == after, mode
                else:
                    assert result.returncode == 2, (mode, result.stderr)
                    assert 'Output directory must be new or empty; existing contents will not be overwritten.' in result.stderr
                    assert not record['numerical_tripwires'] and not record['mkdir_calls'], mode
                    assert snapshot == after, mode
                label = language + '-' + mode
                (args.out / (label + '.stdout.txt')).write_text(result.stdout)
                (args.out / (label + '.stderr.txt')).write_text(result.stderr)
                controls.append({'control': label, 'command': command, 'exit_code': result.returncode,
                                 'probe': record, 'expected_outcome_observed': True,
                                 'meaning': 'before implementation permits occupied output into computation' if before else 'guard permits empty/fresh path before numerical tripwire' if positive else 'rejects occupied output before computation or mutation',
                                 'before_tree': snapshot, 'after_tree': after,
                                 'tree_and_file_bytes_unchanged': snapshot == after,
                                 'stdout_file': label + '.stdout.txt', 'stderr_file': label + '.stderr.txt'})
    report = {'status': 'PASS', 'test_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'candidate_source_pins': {language: hashlib.sha256((course / language / 'model/oxygen_model.py').read_bytes()).hexdigest() for language in ['en','ru']},
              'controls': controls, 'solver_executions': 0, 'builds': 0,
              'method': 'Actual __main__ branch via runpy, actual argparse and filesystem; numerical entrypoints are fail-if-called tripwires. Path.mkdir is observed, not mocked to return success.',
              'limit': 'Exit86 is intentionally a numerical tripwire, not model or numerical success. No concurrency guarantee or programmatic synthetic_fit API guard is claimed.'}
    (args.out / 'regression-results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status':'PASS', 'controls':len(controls),'original_numerical_executions':0}))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--probe':
        probe(Path(sys.argv[2]), Path(sys.argv[3]), '--default' in sys.argv[4:])
    main()
