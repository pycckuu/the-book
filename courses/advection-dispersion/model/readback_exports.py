#!/usr/bin/env python3
"""Independently reassemble saved CSV budgets/profiles/observations, no solver run.

python3 readback_exports.py --results results
Also writes student-readable metadata and spatial metrics from saved profiles.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    with p.open() as f: return list(csv.DictReader(f))


def write(p,rows):
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def main():
    if not __debug__:
        raise RuntimeError("Verification requires normal Python; remove -O/-OO and unset PYTHONOPTIMIZE.")
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('--results',type=Path,required=True)
    out=parser.parse_args().results; root=Path(__file__).resolve().parent
    verification=json.loads((out/'verification.json').read_text())
    assert verification['status']=='PASS', 'Numerical checks have not passed'
    assert verification['code_sha256']==sha(root/'advection_model.py')
    assert verification['verification_code_sha256']==sha(root/'verify_advection.py')
    manifests=json.loads((out/'case-manifest.json').read_text())
    checks=[]; spatial=[]; metadata=[]
    for case in manifests:
        name=case['case_id']; p=case['parameters']
        rows=read(out/(name+'-pulse-budget.csv')); profiles=read(out/(name+'-profiles.csv'))
        faces=read(out/(name+'-face-fluxes.csv')); snapshots={}
        for row in profiles: snapshots.setdefault(float(row['t_s']),[]).append(row)
        states={float(row['t_right_s']):float(row['M_next']) for row in rows}; states[0.]=float(rows[0]['M_previous'])
        dI=math.fsum(float(r['delta_I']) for r in rows)
        dO=math.fsum(float(r['delta_O']) for r in rows)
        dB=math.fsum(float(r['delta_B']) for r in rows)
        step=max(abs(float(r['M_next'])-float(r['M_previous'])-float(r['delta_I'])+float(r['delta_O'])+float(r['delta_B'])) for r in rows)
        cumulative=states[case['end_s']]-states[0.]-dI+dO+dB
        input_error=abs(dI-p['phi']*p['u']*p['C_ref']*p['Tp'])
        increment_error=max(max(abs(float(r['delta_I'])-(float(r['t_right_s'])-float(r['t_left_s']))*float(r['F_in_interval_average'])),
                                 abs(float(r['delta_O'])-(float(r['t_right_s'])-float(r['t_left_s']))*float(r['F_out_right_endpoint'])),
                                 abs(float(r['delta_B'])-(float(r['t_right_s'])-float(r['t_left_s']))*p['k']*float(r['M_next']))) for r in rows)
        component_error=max(abs(float(r['F_total_mol_m2_s'])-float(r['F_adv_mol_m2_s'])-float(r['F_disp_mol_m2_s'])) for r in faces)
        profile_mass_error=0.
        for t,sample in snapshots.items():
            weights=[p['phi']*(float(r['x_right_m'])-float(r['x_left_m']))*float(r['C_cell_average_mol_m3_water']) for r in sample]
            mass=math.fsum(weights); profile_mass_error=max(profile_mass_error,abs(mass-states[t]))
            if mass:
                centres=[(float(r['x_left_m'])+float(r['x_right_m']))/2 for r in sample]
                mean=math.fsum(w*x for w,x in zip(weights,centres))/mass
                variance=math.fsum(w*((x-mean)**2+(float(r['x_right_m'])-float(r['x_left_m']))**2/12) for w,x,r in zip(weights,centres,sample))/mass
                width=math.sqrt(variance)
            else: mean=width=None
            spatial.append(dict(case_id=name,t_s=t,M_mol_m2_bulk_area=mass,centroid_m=mean,width_m=width,
                                support='resident inventory remaining in finite column; piecewise-constant cells',undefined=mass==0))
        summary=dict(case_id=name,step_budget_abs_mol_m2=step,cumulative_budget_reassembled_mol_m2=cumulative,
                     expected_input_error_mol_m2=input_error,increment_reassembly_max_error_mol_m2=increment_error,
                     face_component_sum_max_error_mol_m2_s=component_error,profile_storage_max_error_mol_m2=profile_mass_error)
        assert max(step,abs(cumulative),input_error,increment_error,profile_mass_error)<1e-10
        assert component_error<1e-15
        checks.append(summary)
        coefficients={'L_m':p['L'],'phi_dimensionless':p['phi'],'u_m_s_porewater':p['u'],'v_D_m_s_bulk_area':p['phi']*p['u'],
                      'D_L_m2_s_excluding_phi':p['D'],'k_s_inv':p['k'],'C_ref_mol_m3_water':p['C_ref'],'T_p_s':p['Tp']}
        metadata.append(dict(case_id=name,coefficients=coefficients,coefficient_record_sha256=hashlib.sha256(json.dumps(coefficients,sort_keys=True).encode()).hexdigest(),
                             N=case['N'],h_m=p['L']/case['N'],dt_s=case['dt_s'],end_s=case['end_s'],
                             IC=case['IC'],inlet=case['inlet'],outlet=case['outlet'],synthetic=True,
                             code_sha256=verification['code_sha256'],contract_sha256=verification['contract_sha256'],
                             metric_definitions_sha256=verification['metrics_sha256'],
                             output_sha256={f.name:sha(f) for f in sorted(out.glob(name+'-*.csv'))}))
    observations=read(out/'observations-synthetic.csv'); residuals=read(out/'candidate-residuals-open-answers.csv')
    observation_by_id={r['observation_id']:r for r in observations}; raw_checks=[]
    for source_name in ('truth_refined','k0','k1','k2'):
        source=read(out/(source_name+'-synthetic-source-series.csv')); max_error=0.
        for obs in observations:
            left,right=float(obs['t_left_s']),float(obs['t_right_s'])
            prediction=math.fsum(float(r['C_out_right_endpoint'])*max(0.,min(right,float(r['t_right_s']))-max(left,float(r['t_left_s']))) for r in source)/(right-left)
            expected=float(obs['y']) if source_name=='truth_refined' else float(next(r['prediction_same_support'] for r in residuals if r['candidate_case_id']==source_name and r['observation_id']==obs['observation_id']))
            max_error=max(max_error,abs(prediction-expected))
        assert max_error<1e-12
        raw_checks.append(dict(source=source_name,interval_prediction_reassembly_max_error_mol_m3=max_error))
    scores=read(out/'candidate-scores-open-answers.csv'); score_checks=[]
    for score in scores:
        residual_values=[float(r['prediction_same_support'])-float(observation_by_id[r['observation_id']]['y']) for r in residuals if r['candidate_case_id']==score['candidate_case_id']]
        rmse=math.sqrt(math.fsum(v*v for v in residual_values)/len(residual_values))
        error=abs(rmse-float(score['RMSE_mol_m3_water'])); assert error<1e-12
        score_checks.append(dict(candidate=score['candidate_case_id'],RMSE_reassembled=rmse,error=error))
    write(out/'spatial-metrics.csv',spatial)
    (out/'case-metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
    truth=dict(metadata[1]); truth.update(case_id='reactive-refined',N=800,h_m=1/800,dt_s=50.)
    truth.pop('output_sha256')
    provenance=dict(revision='AD-SYNTHETIC-1',synthetic_only=True,truth=truth,noise='none',random_seed=None,
                    observation_support='eight exact-declared 10000-second interval averages of right-endpoint flux-normalized exit reconstruction',
                    candidate_k_s_inv={'k0':0.,'k1':1e-5,'k2':2e-5},candidate_grid_N=400,candidate_dt_s=100.,
                    uncertainty='No measured noise, sigma or confidence interval; same physical model at different resolutions. Not independent natural data.',
                    files_sha256={f.name:sha(f) for f in sorted(out.glob('*synthetic*.csv'))})
    (out/'synthetic-provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    report=dict(status='PASS',scope='Independent saved-table readback, not independent solver or field validation',
                readback_code_sha256=sha(Path(__file__)),core_cases=checks,synthetic_intervals=raw_checks,scores=score_checks)
    (out/'export-readback.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__': main()
