#!/usr/bin/env python3
"""Illustrative O2 model, Python standard library only. No measured calibration.

Run: python3 oxygen_model.py --out my-run
Choose a new or empty output directory.
C: mol/m3 porewater; Ds: m2/s, excludes phi; k: 1/s; x: m downward.
Cell-centred finite volumes, backward Euler, fixed surface C, sealed bottom.
"""
import argparse
import csv
import json
import math
import platform
import random
from pathlib import Path

DEFAULT = dict(L=0.03, D=1e-9, k=1e-5, phi=0.8, C0=0.2)


def analytic(x, L, D, k, C0):
    if k == 0:
        return C0
    ell = math.sqrt(D / k)
    return C0 * (math.exp(-x / ell) + math.exp(-(2 * L - x) / ell)) / (1 + math.exp(-2 * L / ell))


def tridiagonal(lower, diag, upper, rhs):
    """Thomas elimination for the strictly diagonally dominant model matrices."""
    b, y = diag[:], rhs[:]
    for i in range(1, len(b)):
        factor = lower[i - 1] / b[i - 1]
        b[i] -= factor * upper[i - 1]
        y[i] -= factor * y[i - 1]
    y[-1] /= b[-1]
    for i in range(len(b) - 2, -1, -1):
        y[i] = (y[i] - upper[i] * y[i + 1]) / b[i]
    return y


def operator(n, L, D, k, C0):
    if not isinstance(n, int) or n < 2 or not all(math.isfinite(v) for v in (L, D, k, C0)):
        raise ValueError('Require integer n >= 2 and finite parameters')
    if L <= 0 or D < 0 or k < 0 or C0 < 0:
        raise ValueError('Require L > 0 and D,k,C0 >= 0')
    h = L / n
    a = D / h**2
    diag = [2 * a + k] * n
    diag[0], diag[-1] = 3 * a + k, a + k
    return h, [-a] * (n - 1), diag, [-a] * (n - 1), [2 * a * C0] + [0.0] * (n - 1)


def steady(n=80, **p):
    if p['D'] <= 0:
        raise ValueError('Steady analytic comparison requires D > 0')
    h, lo, diag, up, b = operator(n, p['L'], p['D'], p['k'], p['C0'])
    return h, tridiagonal(lo, diag, up, b)


def transient(n=80, dt=1000, duration=1e6, initial=None, **p):
    if not all(math.isfinite(v) for v in (dt, duration, p['phi'])) or dt <= 0 or duration <= 0 or not 0 < p['phi'] <= 1:
        raise ValueError('Require dt,duration > 0 and 0 < phi <= 1')
    h, lo, diag, up, b = operator(n, p['L'], p['D'], p['k'], p['C0'])
    c = [0.0] * n if initial is None else list(initial)
    if len(c) != n or any(not math.isfinite(v) or v < 0 for v in c):
        raise ValueError('Initial concentrations must be finite, nonnegative, length n')
    t, worst_balance, min_c, inflow, consumed = 0.0, 0.0, min(c), 0.0, 0.0
    initial_mass = p['phi'] * h * sum(c)
    max_c = max(c)
    while t < duration:
        step = min(dt, duration - t)
        old_mass = p['phi'] * h * sum(c)
        c = tridiagonal([step * v for v in lo], [1 + step * v for v in diag],
                        [step * v for v in up], [v + step * s for v, s in zip(c, b)])
        mass = p['phi'] * h * sum(c)
        flux = 2 * p['phi'] * p['D'] * (p['C0'] - c[0]) / h
        sink = p['phi'] * p['k'] * h * sum(c)
        # Balance uses the same implicit-time face flux and reaction as the solve.
        residual = (mass - old_mass) / step - flux + sink
        worst_balance = max(worst_balance, abs(residual))
        inflow += step * flux
        consumed += step * sink
        min_c, max_c = min(min_c, min(c)), max(max_c, max(c))
        if min(c) < 0:
            raise ArithmeticError('Negative concentration: no clipping is permitted')
        t += step
    return c, dict(max_balance_residual_mol_m2_s=worst_balance,
                   cumulative_balance_residual_mol_m2=mass - initial_mass - inflow + consumed,
                   min_concentration_mol_m3=min_c, max_concentration_mol_m3=max_c,
                   final_inventory_mol_m2=mass, inflow_mol_m2=inflow, consumption_mol_m2=consumed)


def golden_minimum(fun, lo, hi):
    for _ in range(100):
        a = lo + (hi - lo) * 0.3819660112501051
        b = lo + (hi - lo) * 0.6180339887498949
        if fun(a) < fun(b):
            hi = b
        else:
            lo = a
    return (lo + hi) / 2


def synthetic_fit(out):
    rng = random.Random(20261010)
    L, C0, sigma, alpha_true = DEFAULT['L'], DEFAULT['C0'], 0.002, 1e4
    xs = [0.003 * i for i in range(1, 11)]
    ys = [analytic(x, L, 1.0, alpha_true, C0) + rng.gauss(0, sigma) for x in xs]
    def fit(observations):
        objective = lambda log_a: sum((analytic(x, L, 1.0, math.exp(log_a), C0) - y)**2 for x, y in zip(xs, observations))
        return math.exp(golden_minimum(objective, math.log(100), math.log(1e6)))
    alpha = fit(ys)
    bootstrap = sorted(fit([analytic(x, L, 1.0, alpha, C0) + rng.gauss(0, sigma) for x in xs]) for _ in range(200))
    with (out / 'synthetic-profile.csv').open('w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['x_m', 'C_synthetic_mol_m3_porewater', 'sigma_mol_m3', 'provenance'])
        w.writerows((x, y, sigma, 'analytic first-order profile + seeded Gaussian noise; no field data') for x, y in zip(xs, ys))
    derivatives = [(analytic(x, L, 1., alpha * math.exp(1e-4), C0) - analytic(x, L, 1., alpha * math.exp(-1e-4), C0)) / 2e-4 for x in xs]
    return dict(alpha_true_m_minus2=alpha_true, alpha_fit_m_minus2=alpha,
                bootstrap_95_percentile_interval_m_minus2=[bootstrap[4], bootstrap[194]],
                bootstrap_replicates=200, noise_sigma_mol_m3=sigma, seed=20261010,
                conditional_k_s_minus1=alpha * DEFAULT['D'],
                conditional_log_alpha_standard_error=sigma / math.sqrt(sum(d*d for d in derivatives)),
                caveat='Synthetic recovery only; interval conditions on known C0,L,sigma and exact model. No empirical validation.')


def verify():
    if not __debug__:
        raise RuntimeError("Verification requires normal Python; remove -O/-OO and unset PYTHONOPTIMIZE.")
    p = DEFAULT.copy()
    grid = []
    for n in (20, 40, 80, 160):
        h, c = steady(n=n, **p)
        errors = [v - analytic((i + 0.5)*h, p['L'], p['D'], p['k'], p['C0']) for i, v in enumerate(c)]
        flux = 2 * p['phi'] * p['D'] * (p['C0'] - c[0]) / h
        sink = p['phi'] * p['k'] * h * sum(c)
        grid.append(dict(n=n, max_absolute_error=max(map(abs, errors)), flux=flux, integrated_sink=sink, balance_residual=flux-sink))
    orders = [math.log(grid[i]['max_absolute_error']/grid[i+1]['max_absolute_error'], 2) for i in range(3)]
    assert all(1.8 < v < 2.2 for v in orders), orders
    assert max(abs(r['balance_residual']) for r in grid) < 1e-17
    _, c0 = steady(n=20, **dict(p, k=0.0))
    assert max(abs(v-p['C0']) for v in c0) < 1e-12
    # Exact semi-discrete eigenmode isolates time error from spatial error.
    n, amplitude, T = 100, 0.02, 20000
    h, base = steady(n=n, **p)
    mu = math.pi / (2*p['L'])
    mode = [math.sin(mu*(i+.5)*h) for i in range(n)]
    initial = [v + amplitude*s for v, s in zip(base, mode)]
    lambda_h = 4*p['D']/h**2 * math.sin(mu*h/2)**2 + p['k']
    time_errors = []
    continuum_errors = []
    for dt in (1000, 500, 250, 125):
        c, bal = transient(n=n, dt=dt, duration=T, initial=initial, **p)
        exact = [v+amplitude*s*math.exp(-lambda_h*T) for v,s in zip(base,mode)]
        time_errors.append(max(abs(v-w) for v,w in zip(c,exact)))
        assert bal['max_balance_residual_mol_m2_s'] < 1e-17
        # Independent continuum smooth solution, including spatial error.
        exact_cont = [analytic((i+.5)*h,p['L'],p['D'],p['k'],p['C0'])+amplitude*mode[i]*math.exp(-(p['D']*mu**2+p['k'])*T) for i in range(n)]
        continuum_errors.append(max(abs(v-w) for v,w in zip(c,exact_cont)))
    time_orders = [math.log(time_errors[i]/time_errors[i+1],2) for i in range(3)]
    assert all(.95 < v < 1.05 for v in time_orders), time_orders
    # Zero transport: pure first-order decay, BE closed form and time refinement.
    decay, decay_error = [], []
    for dt in (1000,500,250):
        c, _ = transient(n=10, dt=dt, duration=T, initial=[p['C0']]*10, **dict(p,D=0.0))
        exact_be = p['C0']/(1+p['k']*dt)**round(T/dt)
        assert max(abs(v-exact_be) for v in c) < 1e-14
        decay.append(c[0]); decay_error.append(abs(c[0]-p['C0']*math.exp(-p['k']*T)))
    assert decay_error[0] > decay_error[1] > decay_error[2]
    small_k = analytic(0.01,p['L'],p['D'],1e-14,p['C0'])
    assert abs(small_k-p['C0']) < 1e-8
    semi = analytic(.01,1.0,p['D'],p['k'],p['C0'])
    assert abs(semi-p['C0']*math.exp(-1)) < 1e-14
    # Structural non-identifiability: scaling D,k together changes no steady profile.
    assert max(abs(analytic(x,p['L'],p['D'],p['k'],p['C0'])-analytic(x,p['L'],4*p['D'],4*p['k'],p['C0'])) for x in (.0,.01,.02,.03)) < 1e-15
    # Surface concentration scales both steady concentration and flux linearly.
    assert abs(analytic(.01,p['L'],p['D'],p['k'],2*p['C0'])-2*analytic(.01,p['L'],p['D'],p['k'],p['C0'])) < 1e-15
    for bad in (dict(k=-1.),dict(phi=0.),dict(D=float('nan'))):
        try:
            transient(duration=10,**dict(p,**bad))
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid parameter accepted')
    return dict(grid=grid, grid_orders=orders, time_dt_s=[1000,500,250,125],
                time_max_errors=time_errors, time_orders=time_orders,
                smooth_continuum_max_errors=continuum_errors,
                pure_decay_concentrations=decay, pure_decay_continuum_errors=decay_error,
                analytic_limits=['k=0 uniform steady', 'D=0 pure decay', 'k approaches zero',
                                 'deep-domain exponential', 'surface scaling', 'D,k common-scaling invariance'])


def main():
    if not __debug__:
        raise RuntimeError("Verification requires normal Python; remove -O/-OO and unset PYTHONOPTIMIZE.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, default=Path('results'))
    args = parser.parse_args()
    if args.out.exists() and (not args.out.is_dir() or any(args.out.iterdir())):
        parser.error('Output directory must be new or empty; existing contents will not be overwritten.')
    args.out.mkdir(parents=True, exist_ok=True)
    p = DEFAULT.copy()
    report = dict(parameters=p, parameter_status='all illustrative, not literature estimates',
                  python=platform.python_version(), verification=verify(), calibration=synthetic_fit(args.out))
    rows = []
    for T in (10000,100000,1000000):
        c, balance = transient(duration=T, **p)
        assert balance['max_balance_residual_mol_m2_s'] < 1e-17
        assert abs(balance['cumulative_balance_residual_mol_m2']) < 1e-13
        assert balance['max_concentration_mol_m3'] <= p['C0'] + 1e-14
        report['step_run_'+str(T)] = balance
        h = p['L']/len(c)
        rows.extend((T,(i+.5)*h,v,analytic((i+.5)*h,p['L'],p['D'],p['k'],p['C0'])) for i,v in enumerate(c))
    ell = math.sqrt(p['D']/p['k'])
    report['analytic_steady'] = dict(ell_m=ell, Damkohler=p['k']*p['L']**2/p['D'],
         inventory_mol_m2=p['phi']*p['C0']*ell*math.tanh(p['L']/ell),
         surface_flux_mol_m2_s=p['phi']*p['D']*p['C0']/ell*math.tanh(p['L']/ell),
         bottom_C_mol_m3=analytic(p['L'],p['L'],p['D'],p['k'],p['C0']))
    with (args.out/'profiles.csv').open('w',newline='') as f:
        w=csv.writer(f); w.writerow(['t_s','x_m','C_simulated_mol_m3_porewater','C_analytic_steady_mol_m3_porewater']); w.writerows(rows)
    (args.out/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
