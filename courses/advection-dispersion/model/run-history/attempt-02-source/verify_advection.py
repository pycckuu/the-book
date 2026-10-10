#!/usr/bin/env python3
"""Reproduce B01-B08, independently refined teaching outputs and synthetic tasks.

All external data are absent: parameters and observations are illustrative.
python3 verify_advection.py --out results
Failures are retained in run-history. Returns nonzero if acceptance targets fail.
"""
import argparse
import csv
import datetime
import hashlib
import json
import math
import platform
import sys
import traceback
from pathlib import Path
import advection_model as m

ROOT=Path(__file__).resolve().parent
CONTRACT_SHA='d890ac5b46c239a9b64bfadf1cf4a1af5bdb2ec7e97a56f34deb3333166df75e'
METRIC_SHA=hashlib.sha256((ROOT/'metric-definitions.json').read_bytes()).hexdigest()


def csv_write(path,rows):
    if not rows: raise ValueError('No rows to export')
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def orders(errors):
    return [math.log(a/b,2) if a>0 and b>0 else None for a,b in zip(errors,errors[1:])]


def periodic(p,n,dt,T,Cb=1.,amp=.25):
    """Auxiliary cyclic upwind/BE matrix solved by rank-one Thomas correction."""
    m.validate(p,n,dt,T)
    if n<3: raise ValueError('Periodic auxiliary requires N>=3')
    h=p['L']/n; beta=2*math.pi/p['L']
    a,b=p['u']/h,p['D']/h**2
    sinc=math.sin(beta*h/2)/(beta*h/2)
    c=[Cb+amp*sinc*math.cos(beta*(i+.5)*h) for i in range(n)]
    cache={}; t=0.; min_C=min(c)
    while t<T:
        step=min(dt,T-t)
        if step not in cache:
            lo=[-step*(a+b)]*(n-1); up=[-step*b]*(n-1)
            diag=[1+step*(a+2*b+p['k'])]*n
            # u*v^T corners: row(last),col(0)=alpha; row(0),col(last)=beta.
            alpha,beta_corner=-step*b,-step*(a+b)
            gamma=-diag[0]
            diag[0]-=gamma; diag[-1]-=alpha*beta_corner/gamma
            fac=m.factor(lo,diag,up)
            z=m.solve(fac,[gamma]+[0.]*(n-2)+[alpha])
            cache[step]=(fac,z,beta_corner/gamma)
        fac,z,ratio=cache[step]
        old=c; x=m.solve(fac,old)
        corr=(x[0]+ratio*x[-1])/(1+z[0]+ratio*z[-1])
        c=[v-corr*w for v,w in zip(x,z)]
        min_C=min(min_C,min(c)); t+=step
    theta=beta*h
    lam=complex(-p['k']-4*p['D']*math.sin(theta/2)**2/h**2-p['u']*(1-math.cos(theta))/h,
                -p['u']*math.sin(theta)/h)
    semi=[Cb*math.exp(-p['k']*T)+amp*sinc*math.exp(lam.real*T)*math.cos(beta*(i+.5)*h+lam.imag*T) for i in range(n)]
    continuum=[Cb*math.exp(-p['k']*T)+amp*sinc*math.exp(-(p['k']+p['D']*beta**2)*T)*math.cos(beta*((i+.5)*h-p['u']*T)) for i in range(n)]
    mean=math.fsum(c)/n
    coscoef=2*math.fsum((v-mean)*math.cos(beta*(i+.5)*h) for i,v in enumerate(c))/n
    sincoef=2*math.fsum((v-mean)*math.sin(beta*(i+.5)*h) for i,v in enumerate(c))/n
    amplitude=math.hypot(coscoef,sincoef)
    phase=math.atan2(-sincoef,coscoef)
    deff=-math.log(amplitude/(amp*sinc))/(beta*beta*T)-p['k']/(beta*beta)
    residual=max(abs((1+step*(a+2*b+p['k']))*v-step*(a+b)*c[(i-1)%n]-step*b*c[(i+1)%n]-old[i]) for i,v in enumerate(c))
    return dict(N=n,dt_s=dt,T_s=T,error_semidiscrete=max(abs(v-w) for v,w in zip(c,semi)),
                error_continuum=max(abs(v-w) for v,w in zip(c,continuum)),min_C=min_C,
                measured_mean=mean,expected_mean=Cb*math.exp(-p['k']*T),amplitude=amplitude,
                phase_rad=phase,expected_phase_rad=-p['u']*beta*T,
                D_effective_m2_s=deff,D_num_leading_m2_s=p['u']*h/2+p['u']**2*dt/2,
                final_linear_residual=residual)


def closed_ode_error(p,n,dt,T):
    c=.7; r=m.pulse(dict(p,u=0.,D=0.,k=1e-5),n,dt,T,initial=[c]*n,snapshot_times=(0.,T))
    return dict(dt_s=dt,error=max(abs(v-c*math.exp(-1e-5*T)) for v in r['c']),
                BE_closed_form_error=max(abs(v-c/(1+dt*1e-5)**round(T/dt)) for v in r['c']),report=r['report'])


def check_budget(result):
    r=result['report']
    return (r['max_linear_residual_scaled']<=1e-12 and
            (r['max_step_residual_scaled']<=1e-10 if r['nonzero_amount_scale'] else r['max_step_residual']<=1e-14) and
            (r['max_cumulative_residual_scaled']<=1e-10 if r['nonzero_amount_scale'] else r['max_cumulative_residual']<=1e-14) and
            r['min_C']>=-1e-12 and r['max_C']<=1+1e-12)


def comparison(p,base,refined,axis):
    a,b=m.outlet_metrics(base),m.outlet_metrics(refined)
    fields=['peak_C','peak_time_s','t10_s','t50_s','t90_s','mean_time_s','width_time_s']
    details=[]
    for key in fields:
        floor=.01*p['C_ref'] if key=='peak_C' else .01*p['L']/p['u']
        error=abs(a[key]-b[key]); tol=.02*max(abs(b[key]),floor)
        details.append(dict(axis=axis,metric=key,base=a[key],refined=b[key],absolute_change=error,tolerance=tol,pass_target=error<=tol))
    for key in ('export_fraction','loss_fraction','storage_fraction'):
        error=abs(a[key]-b[key])
        details.append(dict(axis=axis,metric=key,base=a[key],refined=b[key],absolute_change=error,tolerance=.005,pass_target=error<=.005))
    worst=0.; scale=0.
    for t,c in base['snapshots'].items():
        if t not in refined['snapshots']: continue
        d=refined['snapshots'][t]
        if len(d)==2*len(c): d=[(d[2*i]+d[2*i+1])/2 for i in range(len(c))]
        if len(d)!=len(c): raise ValueError('Profile refinement grids incompatible')
        worst=max(worst,max(abs(v-w) for v,w in zip(c,d))); scale=max(scale,max(d))
    tol=.02*max(scale,.01*p['C_ref'])
    details.append(dict(axis=axis,metric='profile_cell_average_max_difference',base=None,refined=None,absolute_change=worst,tolerance=tol,pass_target=worst<=tol))
    return details


def interval_observation(result,left,right,p):
    amount=math.fsum(r['F_out_right_endpoint']*max(0.,min(right,r['t_right_s'])-max(left,r['t_left_s'])) for r in result['rows'])
    return amount/(p['phi']*p['u']*(right-left))


def run(out):
    out.mkdir(parents=True,exist_ok=True)
    evidence={'revision':'AD-NUMERICS-1','contract_sha256':CONTRACT_SHA,'metrics_sha256':METRIC_SHA,
              'code_sha256':hashlib.sha256((ROOT/'advection_model.py').read_bytes()).hexdigest(),
              'verification_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python':platform.python_version(),'synthetic_only':True,'empirical_validation':False,'benchmarks':{},'failures':[]}
    def record(name,data,passed):
        evidence['benchmarks'][name]={'pass':bool(passed),'evidence':data}
        if not passed: evidence['failures'].append(name)
        print(name,'PASS' if passed else 'FAIL',flush=True)
    p=m.DEFAULT.copy()
    invalid=[]
    for key,value in [('L',0.),('phi',0.),('phi',1.1),('u',-1.),('D',-1.),('k',-1.),('C_ref',-1.),('Tp',0.),('D',float('nan'))]:
        try: m.pulse(dict(p,**{key:value}),8,1000.,1000.); invalid.append(False)
        except ValueError: invalid.append(True)
    for n,dt,T in [(1,1000.,1000.),(2.5,1000.,1000.),(8,0.,1000.),(8,1000.,float('inf'))]:
        try: m.pulse(p,n,dt,T); invalid.append(False)
        except ValueError: invalid.append(True)
    try: m.pulse(p,8,1000.,1000.,initial=[-1.]*8); invalid.append(False)
    except ValueError: invalid.append(True)
    zero=m.pulse(dict(p,C_ref=0.,k=1e-5),10,7000.,21000.,snapshot_times=(0.,21000.))
    record('B01',dict(invalid_inputs_rejected=invalid,zero=zero['report']),all(invalid) and all(v==0 for v in zero['c']) and check_budget(zero))
    constant=[]
    for n in (50,100,200,400):
        c,lin=m.steady(p,n)
        constant.append(dict(N=n,max_error=max(abs(v-p['C_ref']) for v in c),linear_residual_scaled=lin,
                             flux_difference=p['phi']*p['u']*(p['C_ref']-c[-1]),min_C=min(c)))
    record('B02',constant,max(r['max_error'] for r in constant)<1e-10 and max(r['linear_residual_scaled'] for r in constant)<1e-12)
    reactive=dict(p,k=1e-5); grid=[]
    for n in (50,100,200,400):
        c,lin=m.steady(reactive,n); h=p['L']/n
        exact=[m.steady_average(reactive,i*h,(i+1)*h) for i in range(n)]
        grid.append(dict(N=n,dt_s=None,error=max(abs(v-w) for v,w in zip(c,exact)),linear_residual_scaled=lin,
                         min_C=min(c),flux_in=p['phi']*p['u']*p['C_ref'],flux_out=p['phi']*p['u']*c[-1],
                         sink=p['phi']*h*reactive['k']*math.fsum(c)))
    spatial_orders=orders([r['error'] for r in grid])
    analytic_budget=p['phi']*p['u']*(p['C_ref']-m.steady_point(reactive,p['L']))-p['phi']*reactive['k']*p['L']*m.steady_average(reactive,0.,p['L'])
    record('B03',dict(grid=grid,orders=spatial_orders,continuum_budget_residual=analytic_budget),
           all(.8<v<1.2 for v in spatial_orders[-2:]) and abs(analytic_budget)<1e-15 and all(r['min_C']>=0 and abs(r['flux_in']-r['flux_out']-r['sink'])<1e-15 and r['linear_residual_scaled']<1e-12 for r in grid))
    time=[]
    for k in (0.,1e-5):
        tests=[periodic(dict(p,k=k),64,dt,20000.) for dt in (1000.,500.,250.,125.)]
        o=orders([r['error_semidiscrete'] for r in tests]); fine=periodic(dict(p,k=k),64,5.,20000.)
        time.append(dict(k=k,tests=tests,orders=o,small_dt_continuum_plateau=fine))
    diffusion=[periodic(dict(p,u=0.,k=0.),n,1.,10000.) for n in (16,32,64,128)]
    diff_orders=orders([r['error_continuum'] for r in diffusion])
    record('B04',dict(time=time,isolated_diffusion_space=diffusion,diffusion_orders=diff_orders),
           all(all(.8<v<1.2 for v in r['orders']) and all(t['min_C']>=0 and t['final_linear_residual']<1e-12 for t in r['tests']) for r in time) and all(1.8<v<2.2 for v in diff_orders[-2:]))
    overlap=m.pulse(p,20,7000.,42000.,snapshot_times=(0.,42000.))
    # Core step crossing Tp is 14000..21000: only 6000 seconds belong to feed.
    overlap_row=next(r for r in overlap['rows'] if r['t_left_s']<p['Tp']<r['t_right_s'])
    record('B05_overlap',dict(report=overlap['report'],endpoint_interval=overlap_row),
           abs(overlap['report']['input']-p['phi']*p['u']*p['C_ref']*p['Tp'])<1e-15 and check_budget(overlap))
    space_pure=[periodic(dict(p,D=0.,k=0.),n,10.,10000.) for n in (40,80,160,320)]
    time_pure=[periodic(dict(p,D=0.,k=0.),160,dt,20000.) for dt in (1000.,500.,250.,125.)]
    hyper=[]
    for n in (50,100,200,400):
        hp=dict(p,D=0.,k=0.); dt=100000./n/10
        r=m.pulse(hp,n,dt,200000.,snapshot_times=(0.,50000.,100000.,150000.,200000.))
        pulse_error=0.; h=p['L']/n
        for t,c in r['snapshots'].items():
            front=min(p['L'],p['u']*t); back=max(0.,p['u']*(t-p['Tp']))
            exact=[p['C_ref']*max(0.,min((i+1)*h,front)-max(i*h,back))/h for i in range(n)]
            pulse_error=max(pulse_error,h*math.fsum(abs(v-w) for v,w in zip(c,exact)))
        mm=m.outlet_metrics(r)
        hyper.append(dict(N=n,dt_s=dt,max_profile_L1_mol_m2_water=pulse_error,
                          t50_s=mm['t50_s'],width_time_s=mm['width_time_s'],export_fraction=mm['export_fraction'],
                          auxiliary_exact_arrival_s=p['L']/p['u'],auxiliary_exact_t50_s=p['L']/p['u']+p['Tp']/2,
                          auxiliary_exact_width_s=p['Tp']/math.sqrt(12),report=r['report']))
    hp_loss=dict(p,D=0.,k=1e-5)
    loss_limit=m.pulse(hp_loss,400,100.,400000.,snapshot_times=(0.,400000.))
    fraction=m.outlet_metrics(loss_limit)['export_fraction']; reference=math.exp(-p['L']*hp_loss['k']/p['u'])
    record('B06',dict(space_pure=space_pure,time_pure=time_pure,hyperbolic=hyper,
                     characteristic_loss_export_fraction=fraction,characteristic_loss_exact=reference),
           all(a['D_effective_m2_s']>b['D_effective_m2_s'] for a,b in zip(space_pure,space_pure[1:])) and
           all(a['D_effective_m2_s']>b['D_effective_m2_s'] for a,b in zip(time_pure,time_pure[1:])) and
           all(a['max_profile_L1_mol_m2_water']>b['max_profile_L1_mol_m2_water'] for a,b in zip(hyper,hyper[1:])) and
           abs(fraction-reference)<.01 and all(check_budget_result(h['report']) for h in hyper) and
           all(r['final_linear_residual']<1e-12 and abs(r['measured_mean']-r['expected_mean'])<1e-10 for r in space_pure+time_pure))
    short=m.pulse(reactive,200,250.,50000.,snapshot_times=(0.,50000.))
    longp=dict(reactive,L=2.)
    long=m.pulse(longp,400,250.,50000.,snapshot_times=(0.,50000.))
    difference=max(abs(a-b) for a,b in zip(short['c'],long['c'][:200]))
    shared_steady=max(abs(m.steady_average(reactive,i/200,(i+1)/200)-m.steady_average(longp,i/200,(i+1)/200)) for i in range(200))
    record('B07',dict(physical_Tp_s=p['Tp'],same_h_m=.005,pulse_shared_profile_max_difference=difference,
                     constant_feed_shared_continuum_profile_max_difference=shared_steady,
                     short_report=short['report'],long_report=long['report'],interpretation='Quantified boundary/domain sensitivity, not a zero-error target or universal exit irrelevance.'),check_budget(short) and check_budget(long) and short['report']['input']==long['report']['input'])
    a=m.pulse(p,80,500.,100000.,snapshot_times=(0.,100000.))
    phi_p=dict(p,phi=.60); b=m.pulse(phi_p,80,500.,100000.,snapshot_times=(0.,100000.))
    fixed_darcy=m.pulse(dict(phi_p,u=p['phi']*p['u']/phi_p['phi']),80,500.,100000.,snapshot_times=(0.,100000.))
    small_loss=m.pulse(dict(p,k=1e-12),80,500.,100000.,snapshot_times=(0.,100000.))
    closed=m.pulse(dict(p,u=0.,k=1e-5),30,500.,20000.,initial=[.7]*30,snapshot_times=(0.,20000.))
    decays=[closed_ode_error(p,10,dt,20000.) for dt in (1000.,500.,250.,125.)]
    decay_orders=orders([r['error'] for r in decays])
    record('B08',dict(fixed_u_max_C_difference=max(abs(v-w) for v,w in zip(a['c'],b['c'])),
                     phi_inventory_ratio=b['report']['final_inventory']/a['report']['final_inventory'],
                     phi_export_ratio=b['report']['export']/a['report']['export'],
                     fixed_Darcy_C_difference=max(abs(v-w) for v,w in zip(a['c'],fixed_darcy['c'])),
                     k_to_zero_C_difference=max(abs(v-w) for v,w in zip(a['c'],small_loss['c'])),
                     closed_diffusion_decay_report=closed['report'],decay=decays,decay_orders=decay_orders),
           a['c']==b['c'] and abs(b['report']['final_inventory']/a['report']['final_inventory']-2)<1e-12 and
           max(abs(v-w) for v,w in zip(a['c'],small_loss['c']))<1e-6 and
           max(abs(v-w) for v,w in zip(a['c'],fixed_darcy['c']))>1e-3 and
           closed['report']['input']==closed['report']['export']==0 and
           all(.8<v<1.2 for v in decay_orders) and all(r['BE_closed_form_error']<1e-12 for r in decays) and check_budget(closed))
    # Default-resolution gate uses the definitions file pinned above before run.
    cases={'conservative':p,'reactive':reactive,'faster-flow':dict(p,u=2*p['u']),
           'more-dispersion':dict(p,D=2*p['D'])}
    controls={}; refinements=[]; summaries={}; results={}
    for case,params in cases.items():
        writer=m.Export(out,case,params)
        try: result=m.pulse(params,400,100.,600000.,writer=writer)
        finally: writer.close()
        results[case]=result; mm=m.outlet_metrics(result); summaries[case]=mm
        grid_ref=m.pulse(params,800,100.,600000.)
        time_ref=m.pulse(params,400,50.,600000.)
        details=comparison(params,result,grid_ref,'grid_only')+comparison(params,result,time_ref,'time_only')
        refinements += [dict(case_id=case,**row) for row in details]
        heuristic=(params['u']*params['L']/400/2+params['u']**2*100/2)/params['D']
        controls[case]=dict(parameters=params,base_report=result['report'],grid_refined_report=grid_ref['report'],
                            time_refined_report=time_ref['report'],D_num_over_D_heuristic=heuristic,
                            independent_refinement_pass=all(row['pass_target'] for row in details),metrics=mm)
        record('B05_'+case,result['report'],check_budget(result) and abs(result['report']['input']-params['phi']*params['u']*params['C_ref']*params['Tp'])<1e-14)
        print('REFINEMENT',case,'PASS' if controls[case]['independent_refinement_pass'] else 'FAIL',flush=True)
    record('DEFAULT_RESOLUTION',controls,all(r['independent_refinement_pass'] and r['D_num_over_D_heuristic']<=.05 and
                                           check_budget_result(r['grid_refined_report']) and check_budget_result(r['time_refined_report']) for r in controls.values()))
    windows=[]
    for case in cases:
        extended=m.pulse(cases[case],400,100.,800000.,snapshot_times=(0.,20000.,50000.,100000.,150000.,200000.,400000.,600000.,800000.))
        details=comparison(cases[case],results[case],extended,'window_extension')
        windows.append(dict(case_id=case,metrics_extended=m.outlet_metrics(extended),extended_report=extended['report'],changes=details))
    record('OBSERVATION_WINDOW',windows,all(summaries[r['case_id']]['storage_fraction']<=.001 and all(d['pass_target'] for d in r['changes']) for r in windows))
    csv_write(out/'independent-refinement.csv',refinements)
    csv_write(out/'scenario-summary.csv',[dict(case_id=case,**row) for case,row in summaries.items()])
    # Raw observations and completed answers kept in distinct files, both open.
    intervals=[(left,left+10000.) for left in (30000.,50000.,70000.,90000.,110000.,140000.,180000.,240000.)]
    truth=m.pulse(reactive,800,50.,600000.)
    obs=[]
    for i,(left,right) in enumerate(intervals):
        obs.append(dict(observation_id='S'+str(i+1),synthetic_truth_case_id='reactive-refined',t_left_s=left,t_right_s=right,
                        observable='outlet interval-mean flux-normalized concentration',y=interval_observation(truth,left,right,reactive),
                        units='mol m^-3 porewater',synthetic_flag=True,noise_definition='none; deterministic FV/BE reference',sigma=''))
    csv_write(out/'observations-synthetic.csv',obs)
    candidates={'k0':results['conservative'],'k1':results['reactive'],'k2':m.pulse(dict(p,k=2e-5),400,100.,600000.)}
    residuals=[]; scores=[]
    for name,result in candidates.items():
        for row in obs:
            prediction=interval_observation(result,row['t_left_s'],row['t_right_s'],p)
            residuals.append(dict(observation_id=row['observation_id'],candidate_case_id=name,prediction_same_support=prediction,
                                  observed_y=row['y'],residual_prediction_minus_observation=prediction-row['y'],units=row['units']))
        residual_values=[r['residual_prediction_minus_observation'] for r in residuals if r['candidate_case_id']==name]
        scores.append(dict(candidate_case_id=name,k_s_inv={'k0':0.,'k1':1e-5,'k2':2e-5}[name],
                           RMSE_mol_m3_water=math.sqrt(math.fsum(r*r for r in residual_values)/len(residual_values)),
                           known_inputs='same L,phi,u,D_L,C_ref,Tp,window,grid,dt; only k differs',interpretation='Synthetic consistency; no empirical calibration or interval'))
    csv_write(out/'candidate-residuals-open-answers.csv',residuals); csv_write(out/'candidate-scores-open-answers.csv',scores)
    record('SYNTHETIC_INFERENCE',dict(observation_count=len(obs),candidate_scores=scores,truth_case='reactive-refined',truth_grid_N=800,truth_dt_s=50.,noise='none',truth_report=truth['report'],
                                    independent_data=False),scores[1]['RMSE_mol_m3_water']<min(scores[0]['RMSE_mol_m3_water'],scores[2]['RMSE_mol_m3_water']) and check_budget(truth) and all(check_budget(r) for r in candidates.values()))
    # Synthetic truth/prediction time series allow independent spreadsheet aggregation.
    for name,result in dict(candidates,truth_refined=truth).items():
        csv_write(out/(name+'-synthetic-source-series.csv'),[dict(t_left_s=r['t_left_s'],t_right_s=r['t_right_s'],C_out_right_endpoint=r['C_out_right_endpoint'],delta_O=r['delta_O']) for r in result['rows']])
    # Tables for selected instructor/no-Python reference and refinement calculations.
    csv_write(out/'steady-spatial.csv',grid)
    csv_write(out/'periodic-time.csv',[dict(k=q['k'],**t) for q in time for t in q['tests']])
    csv_write(out/'periodic-spreading.csv',[dict(axis='grid_only',**r) for r in space_pure]+[dict(axis='time_only',**r) for r in time_pure])
    csv_write(out/'hyperbolic-limit.csv',[{k:v for k,v in row.items() if k!='report'} for row in hyper])
    evidence['case_manifest']=[dict(case_id=case,parameters=params,volume_basis='C porewater; flux/inventory/loss per bulk area',
                                  synthetic=True,reference_type='core finite pulse',IC='zero cell averages',
                                  inlet='known total mass flux; exact rectangular feed overlap',outlet='zero dispersive gradient; advective export',
                                  N=400,dt_s=100.,end_s=600000.,code_sha256=evidence['code_sha256'],
                                  snapshot_times_s=list(results[case]['snapshots']),
                                  input_mol_m2=results[case]['report']['input']) for case,params in cases.items()]
    evidence['default_resolution']={'N':400,'dt_s':100.,'end_s':600000.,'provisional_until_editor_acceptance':True,
                                    'metrics_declared_before_testing':True,'all_core_scenarios_checked':True}
    evidence['status']='PASS' if not evidence['failures'] else 'FAIL'
    (out/'case-manifest.json').write_text(json.dumps(evidence['case_manifest'],indent=2)+'\n')
    return evidence


def check_budget_result(report):
    return check_budget({'report':report})


def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=True)
    history=args.out.parent/'run-history'; history.mkdir(exist_ok=True)
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    try: evidence=run(args.out)
    except Exception:
        evidence={'status':'ERROR','traceback':traceback.format_exc(),
                  'code_sha256':hashlib.sha256((ROOT/'advection_model.py').read_bytes()).hexdigest(),
                  'verification_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    text=json.dumps(evidence,indent=2,allow_nan=False)+'\n'
    (args.out/'verification.json').write_text(text); (history/(stamp+'.json')).write_text(text)
    print('FINAL',evidence['status'],flush=True)
    if evidence['status']=='ERROR': print(evidence['traceback'],flush=True)
    return 0 if evidence['status']=='PASS' else 1


if __name__=='__main__': sys.exit(main())
