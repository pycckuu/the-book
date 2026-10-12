"""Illustrative ideal A <-> B, fixed T,p and modeled liquid volume. Stdlib only."""
import bisect
import math


def parameters(common, case):
    c = case.get('total_concentration_mol_m3', common['total_concentration_mol_m3'])
    k = common['K_eq_dimensionless']
    lam = common['lambda_s_inv']
    x = case['initial_x_B']
    x = k / (1 + k) if isinstance(x, str) else (0 if x is None else x)
    p = dict(T=common['temperature_K'], V=common['liquid_volume_m3'],
             p=common['pressure_Pa'], cs=common['standard_concentration_mol_m3'],
             R=common['gas_constant_J_mol_K'], K=k, lam=lam,
             A0=c * (1 - x), B0=c * x, C=c)
    validate(p)
    p.update(kf=lam * k / (1 + k), kr=lam / (1 + k),
             Aeq=c / (1 + k), Beq=c * k / (1 + k), N=p['V'] * c,
             RT=p['R'] * p['T'], tau=1 / lam)
    p['G0'] = gibbs(p, p['A0'], p['B0'])
    return p


def validate(p):
    for key in ('T', 'V', 'cs', 'R', 'K', 'lam', 'p'):
        if not math.isfinite(p[key]) or p[key] <= 0:
            raise ValueError('positive finite input required: ' + key)
    for key in ('A0', 'B0', 'C'):
        if not math.isfinite(p[key]) or p[key] < 0:
            raise ValueError('nonnegative finite input required: ' + key)


def phi(y):
    """(1+y)log(1+y)-y, continuous at -1; stable near zero."""
    if y == -1:
        return 1.0
    if abs(y) < 1e-3:
        return math.fsum((-1)**n * y**n / (n * (n - 1)) for n in range(2, 13))
    return (1 + y) * math.log1p(y) - y


def gibbs(p, a, b):
    if p['C'] == 0:
        return 0.0
    terms = [eq if c == 0 else eq * phi((c - eq) / eq)
             for c, eq in ((a, p['Aeq']), (b, p['Beq']))]
    return p['RT'] * p['V'] * math.fsum(terms)


def observe(p, a, b, plus, minus):
    if a < 0 or b < 0 or not all(math.isfinite(v) for v in (a, b, plus, minus)):
        raise ArithmeticError('negative or nonfinite state/throughput')
    rp, rm = p['kf'] * a, p['kr'] * b
    r = rp - rm
    g = gibbs(p, a, b)
    reason = 'empty_batch' if p['C'] == 0 else ('zero_A_activity' if a == 0 else ('zero_B_activity' if b == 0 else ''))
    q = b / a if a > 0 else None
    dg = p['RT'] * (math.log(b) - math.log(a) - math.log(p['K'])) if not reason else None
    power = -p['V'] * r * dg if dg is not None else None
    xi = plus - minus
    return dict(c_A=a, c_B=b, n_A=p['V'] * a, n_B=p['V'] * b,
                a_A=a / p['cs'], a_B=b / p['cs'], Q=q, delta_rG=dg,
                r_plus=rp, r_minus=rm, r_net=r, Xi_plus=plus, Xi_minus=minus,
                xi_net=xi, G_ex=g, D_state=p['G0'] - g, P_diss=power,
                total_residual=p['V'] * (a + b) - p['N'],
                A_extent_residual=p['V'] * a - (p['V'] * p['A0'] - xi),
                B_extent_residual=p['V'] * b - (p['V'] * p['B0'] + xi),
                thermo_status='empty' if p['C'] == 0 else ('zero_boundary' if reason else 'finite'),
                null_reason=reason)


def reference(p, t):
    """Exponential/integral reference; never calls the BE method."""
    if t == 0:
        return observe(p, p['A0'], p['B0'], 0.0, 0.0)
    z = p['lam'] * t
    u = -math.expm1(-z) / p['lam']
    v = (math.fsum((-1)**n * z**n / math.factorial(n) for n in range(2, 16)) / p['lam']
         if abs(z) < 1e-3 else t - u)
    decay = math.exp(-z)
    a = p['Aeq'] + (p['A0'] - p['Aeq']) * decay
    b = p['Beq'] + (p['B0'] - p['Beq']) * decay
    plus = p['V'] * p['kf'] * math.fsum((p['A0'] * u, p['Aeq'] * v))
    minus = p['V'] * p['kr'] * math.fsum((p['B0'] * u, p['Beq'] * v))
    return observe(p, a, b, plus, minus)


def solve(p, end, nominal):
    """Positive two-state BE map; both states evolved, no complement repair."""
    if not (math.isfinite(end) and end > 0 and math.isfinite(nominal) and nominal > 0):
        raise ValueError('positive finite end and nominal step required')
    a, b, plus, minus = p['A0'], p['B0'], 0.0, 0.0
    rows = [dict(time_s=0.0, actual_h_s=None, actual_h_over_tau=None,
                 delta_Xi_plus=None, delta_Xi_minus=None, delta_D_state=None,
                 endpoint_power_energy=None, dissipation_gap=None,
                 **observe(p, a, b, plus, minus))]
    for i in range(1, math.ceil(end / nominal) + 1):
        t = min(i * nominal, end)
        h = t - rows[-1]['time_s']
        denominator = 1 + h * p['lam']
        anew = ((1 + h * p['kr']) * a + h * p['kr'] * b) / denominator
        bnew = (h * p['kf'] * a + (1 + h * p['kf']) * b) / denominator
        if p['C'] > 0 and (anew <= 0 or bnew <= 0):
            raise ArithmeticError('positive-time nonempty state lost positivity')
        dp, dm = p['V'] * h * p['kf'] * anew, p['V'] * h * p['kr'] * bnew
        plus, minus = math.fsum((plus, dp)), math.fsum((minus, dm))
        obs = observe(p, anew, bnew, plus, minus)
        drop = rows[-1]['G_ex'] - obs['G_ex']
        w = h * obs['P_diss'] if obs['P_diss'] is not None else None
        rows.append(dict(time_s=t, actual_h_s=h, actual_h_over_tau=h * p['lam'],
                         delta_Xi_plus=dp, delta_Xi_minus=dm, delta_D_state=drop,
                         endpoint_power_energy=w, dissipation_gap=drop - w if w is not None else None,
                         **obs))
        a, b = anew, bnew
    return rows


def sample(p, rows, t, times=None):
    times = times if times is not None else [r['time_s'] for r in rows]
    i = bisect.bisect_left(times, t)
    if i < len(rows) and times[i] == t:
        return rows[i], False
    left, right = rows[i - 1], rows[i]
    weight = (t - left['time_s']) / (right['time_s'] - left['time_s'])
    vals = [left[k] + weight * (right[k] - left[k]) for k in ('c_A', 'c_B', 'Xi_plus', 'Xi_minus')]
    return observe(p, *vals), True
