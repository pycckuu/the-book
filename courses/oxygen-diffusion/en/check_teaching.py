#!/usr/bin/env python3
"""Check teaching answers with the pinned scientist model, no new solver.
Run from bundle root: python3 check_teaching.py
"""
import csv
import hashlib
import importlib.util
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODEL = ROOT / 'model-snapshot' / 'oxygen_model.py'
spec = importlib.util.spec_from_file_location('verified_oxygen', MODEL)
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)
p = model.DEFAULT.copy()
out = ROOT / 'teaching-checks'
out.mkdir(exist_ok=True)

# Independently evaluate the stated cosh reference, then compare the scientist's
# algebraically equivalent exponential implementation and integrate the sink.
ell0 = math.sqrt(p['D'] / p['k'])
flux0 = p['phi'] * p['D'] * p['C0'] / ell0 * math.tanh(p['L'] / ell0)
for x in (0., .003, .01, .02, .03):
    ref = p['C0'] * math.cosh((p['L'] - x) / ell0) / math.cosh(p['L'] / ell0)
    assert abs(ref - model.analytic(x, p['L'], p['D'], p['k'], p['C0'])) < 1e-15
n = 1000
h = p['L'] / n
cs = [model.analytic(i*h, p['L'], p['D'], p['k'], p['C0']) for i in range(n+1)]
integral = h/3 * (cs[0] + cs[-1] + 4*sum(cs[1:-1:2]) + 2*sum(cs[2:-1:2]))
sink = p['phi'] * p['k'] * integral
assert abs(sink-flux0) / flux0 < 1e-10

cases = [('baseline', p), ('double_k', dict(p, k=2*p['k'])),
         ('double_Ds', dict(p, D=2*p['D'])), ('double_C0', dict(p, C0=2*p['C0'])),
         ('phi_0.6_Ds_fixed', dict(p, phi=.6)), ('L_equals_ell0', dict(p, L=ell0)),
         ('double_L', dict(p, L=2*p['L']))]
rows = []
for name, v in cases:
    ell = math.sqrt(v['D'] / v['k'])
    a = v['L'] / ell
    bottom_fraction = 1 / math.cosh(a)
    threshold = None if .05 < bottom_fraction else v['L'] - ell * math.acosh(.05 * math.cosh(a))
    flux = v['phi'] * v['D'] * v['C0'] / ell * math.tanh(a)
    rows.append(dict(case=name, ell_m=ell, bottom_fraction=bottom_fraction,
                     surface_flux_mol_m2_s=flux, surface_flux_mmol_m2_day=flux*86400*1000,
                     C_at_x_ell0_mol_m3=model.analytic(ell0,v['L'],v['D'],v['k'],v['C0']),
                     relative_5pct_depth_m=threshold))
assert rows[0]['relative_5pct_depth_m'] is None
assert rows[1]['relative_5pct_depth_m'] is not None
assert rows[-1]['relative_5pct_depth_m'] is not None
assert abs(rows[3]['surface_flux_mol_m2_s']/flux0-2) < 1e-14
assert abs(rows[4]['surface_flux_mol_m2_s']/flux0-.75) < 1e-14

report = json.loads((ROOT/'model-snapshot/results/verification.json').read_text())
data = list(csv.DictReader((ROOT/'model-snapshot/results/synthetic-profile.csv').open()))
alpha = report['calibration']['alpha_fit_m_minus2']
residuals = []
for d in data:
    x, y = float(d['x_m']), float(d['C_synthetic_mol_m3_porewater'])
    fitted = model.analytic(x,p['L'],1.,alpha,p['C0'])
    residuals.append(dict(x_m=x, C_synthetic_mol_m3=y, C_fitted_mol_m3=fitted,
                          residual_model_minus_synthetic_mol_m3=fitted-y))
objective = lambda a: sum((model.analytic(float(d['x_m']),p['L'],1.,a,p['C0'])-float(d['C_synthetic_mol_m3_porewater']))**2 for d in data)
assert objective(alpha) <= objective(1e4)
assert max(abs(model.analytic(float(d['x_m']),p['L'],p['D'],p['k'],p['C0']) -
               model.analytic(float(d['x_m']),p['L'],2*p['D'],2*p['k'],p['C0'])) for d in data) < 1e-15
profiles = list(csv.DictReader((ROOT/'model-snapshot/results/profiles.csv').open()))
startup_errors = {}
for t in sorted({float(d['t_s']) for d in profiles}):
    selected = [d for d in profiles if float(d['t_s']) == t]
    error = max(abs(float(d['C_simulated_mol_m3_porewater'])-float(d['C_analytic_steady_mol_m3_porewater'])) for d in selected)
    startup_errors[str(int(t))] = dict(max_error_vs_steady_mol_m3=error, max_error_divided_by_C0=error/p['C0'])

for filename, values in [('sensitivity.csv', rows), ('fit-residuals.csv', residuals)]:
    with (out/filename).open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(values[0])); writer.writeheader(); writer.writerows(values)
checks = dict(model_sha256=hashlib.sha256(MODEL.read_bytes()).hexdigest(), parameters=p,
              baseline_simpson_sink_mol_m2_s=sink, baseline_analytic_flux_mol_m2_s=flux0,
              simpson_relative_budget_error=abs(sink-flux0)/flux0,
              sensitivity=rows, alpha_fit_m_minus2=alpha,
              alpha_fit_relative_error=(alpha-1e4)/1e4,
              objective_fit_mol2_m_minus6=objective(alpha), objective_true_mol2_m_minus6=objective(1e4),
              fit_RMSE_mol_m3=math.sqrt(objective(alpha)/len(data)), fit_residuals=residuals,
              startup_errors=startup_errors, status='checks passed; no field validation')
(out/'teaching-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
