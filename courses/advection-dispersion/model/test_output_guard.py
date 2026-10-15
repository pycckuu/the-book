"""Real AD CLI/direct-run output guard controls, stopped before computation.

python3 -B test_output_guard.py --out fresh-controls [--model-root MODEL] [--before-root ORIGINAL_MODEL]
No numerical body or Export body is executed; tripwire exit86 is ordering only.
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


class ComputationTripwire(BaseException):
    pass


def tree(root):
    records={}
    for p in [root]+sorted(root.rglob('*')):
        info=p.lstat();row={'mode':info.st_mode,'mtime_ns':info.st_mtime_ns}
        if stat.S_ISLNK(info.st_mode):row['link']=str(p.readlink())
        elif p.is_file():row['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
        records[str(p.relative_to(root))]=row
    return records


def probe(model,surface,out):
    model=model.resolve();out=out.resolve() if not out.is_symlink() else out
    model_file=model/'advection_model.py';verify_file=model/'verify_advection.py'
    numeric={'pulse','steady','factor','solve','coefficients','linear_residual','steady_coefficients',
             'exp_average','steady_average','steady_point','feed_average','face_fluxes',
             'spatial_metrics','outlet_metrics','periodic','closed_ode_error','comparison','interval_observation'}
    calls=[];entries=[];mkdir=[];writes=[]
    old_mkdir=Path.mkdir;old_open=Path.open
    def observed_mkdir(path,*args,**kwargs):
        mkdir.append(str(path));return old_mkdir(path,*args,**kwargs)
    def observed_open(path,mode='r',*args,**kwargs):
        if any(x in mode for x in ['w','a','x','+']):writes.append(str(path))
        return old_open(path,mode,*args,**kwargs)
    def trace(frame,event,arg):
        if event=='call' and frame.f_code.co_filename in [str(model_file),str(verify_file)]:
            name=frame.f_code.co_name
            if name in ['main','run']:entries.append(name)
            export=name=='__init__' and frame.f_locals.get('self').__class__.__name__=='Export'
            if name in numeric or export:
                calls.append('Export.__init__' if export else name)
                raise ComputationTripwire(calls[-1])
        return trace
    sys.path.insert(0,str(model));sys.argv=[str(model_file if surface=='custom' else verify_file),'--out',str(out)]
    status=0;reason=''
    Path.mkdir=observed_mkdir;Path.open=observed_open;sys.settrace(trace)
    try:
        if surface=='direct':
            ns=runpy.run_path(str(verify_file),run_name='_guard_probe')
            ns['run'](out)
        else:runpy.run_path(sys.argv[0],run_name='__main__')
    except ComputationTripwire as error:
        status=86;reason=str(error)
    except SystemExit as error:status=error.code
    except ValueError as error:
        status=1;reason=str(error)
        print(reason,file=sys.stderr)
    finally:
        sys.settrace(None);Path.mkdir=old_mkdir;Path.open=old_open
    print(json.dumps({'surface':surface,'entries':entries,'computation_tripwires':calls,
                      'mkdir_calls':mkdir,'write_open_calls':writes,'reason':reason,
                      'original_numerical_bodies_executed':0,'original_export_bodies_executed':0}))
    raise SystemExit(status)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--model-root',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--before-root',type=Path)
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    rows=[]
    for surface in ['custom','verify','direct']:
        modes=['occupied_files','nested_only','empty_child','existing_file','symlink_occupied',
               'fresh','empty','fresh_parents','symlink_empty']
        if args.before_root:modes=['before_occupied']+modes
        for mode in modes:
            with tempfile.TemporaryDirectory(prefix='path with spaces ',dir=args.out) as td:
                root=Path(td).resolve();dest=root/'output with spaces'
                positive=mode in ['fresh','empty','fresh_parents','symlink_empty']
                before=mode=='before_occupied'
                if mode=='existing_file':dest.write_bytes(b'KEEP file\x00\xff')
                elif mode.startswith('symlink_'):
                    target=root/'target';target.mkdir();dest.symlink_to(target,target_is_directory=True)
                    if mode=='symlink_occupied':(target/'verification.json').write_bytes(b'KEEP target\x00\xff')
                elif mode=='fresh_parents':dest=root/'new parent'/'child'/'output'
                elif mode=='empty':dest.mkdir()
                elif not positive:
                    (dest/'nested'/'child').mkdir(parents=True)
                    if mode!='empty_child':(dest/'nested'/'child'/'sentinel.bin').write_bytes(b'KEEP nested\x00\xff')
                    if mode in ['occupied_files','before_occupied']:
                        for name in ['verification.json','custom-profiles.csv','custom-report.json']:
                            (dest/name).write_bytes(b'KEEP '+name.encode()+b'\x00\xff')
                if not positive and not before:
                    history=dest.parent/'run-history';history.mkdir()
                    (history/'old.json').write_bytes(b'KEEP history\x00\xff')
                snapshot=tree(root)
                source=(args.before_root if before else args.model_root).resolve()
                command=[sys.executable,'-B',str(Path(__file__).resolve()),'--probe',str(source),surface,str(dest)]
                result=subprocess.run(command,cwd=root,capture_output=True,text=True)
                after=tree(root);row=json.loads(result.stdout)
                assert row['entries'] and row['original_numerical_bodies_executed']==0
                assert not row['write_open_calls'],(surface,mode,row)
                if positive or before:
                    assert result.returncode==86,(surface,mode,result.stderr)
                    assert row['mkdir_calls'] and row['computation_tripwires'],(surface,mode,row)
                    assert row['computation_tripwires']==(['Export.__init__'] if surface=='custom' else ['pulse'])
                    if positive:assert dest.is_dir() and not any(dest.iterdir())
                    if before and surface=='verify':assert (dest.parent/'run-history').is_dir()
                else:
                    assert result.returncode==(1 if surface=='direct' else 2),(surface,mode,result.stderr)
                    assert 'Output directory must be new or empty; existing contents will not be overwritten.' in result.stderr
                    assert not row['mkdir_calls'] and not row['computation_tripwires']
                    assert snapshot==after,(surface,mode)
                    if surface=='verify':assert 'run' not in row['entries']
                label=surface+'-'+mode
                (args.out/(label+'.stdout.txt')).write_text(result.stdout)
                (args.out/(label+'.stderr.txt')).write_text(result.stderr)
                rows.append({'control':label,'command':command,'exit_code':result.returncode,'probe':row,
                             'before_tree':snapshot,'after_tree':after,'tree_bytes_modes_mtime_unchanged':snapshot==after,
                             'expected_outcome_observed':True,'meaning':'original occupied route reaches mutation/computation boundary' if before else 'fresh/empty route permits pre-computation boundary' if positive else 'occupied route rejects before writes/computation/history',
                             'stdout_file':label+'.stdout.txt','stderr_file':label+'.stderr.txt'})
    report={'status':'PASS_GUARD_ORDER_ONLY','test_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'candidate_source_pins':{p:hashlib.sha256((args.model_root/p).read_bytes()).hexdigest() for p in ['advection_model.py','verify_advection.py']},
            'controls':rows,'numeric_executions':0,'export_body_executions':0,'builds':0,
            'method':'Actual CLI/runpy, argparse and direct run(Path). Source-level call trace raises BaseException before numerical/Export bodies, outside verification ERROR catch; real mkdir/open wrappers only observe.',
            'limits':'Exit86 is ordering, not successful numerical execution. Single-process preflight; direct Export and concurrent writers outside scope. Required --out means no default destination; default custom parameters are exercised.'}
    (args.out/'regression-results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'controls':len(rows),'numeric_executions':0}))


if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='--probe':probe(Path(sys.argv[2]),sys.argv[3],Path(sys.argv[4]))
    main()
