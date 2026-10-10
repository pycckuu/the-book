"""Independent saved-CSV arithmetic/reference readback. No solver/model import."""
import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path


def read(path):
    with path.open(newline='') as f:
        yield from csv.DictReader(f)


def number(row, key):
    return float(row[key]) if row[key] else None


def direct_g(p, a, b):
    if p['C'] == 0:
        return 0.0
    # Direct compensated form, independently evaluated without model.phi.
    return p['RT'] * p['V'] * math.fsum(
        (c * math.log(c / eq) if c else 0.0) - c + eq
        for c, eq in ((a, p['Aeq']), (b, p['Beq'])))


def exact_reference(p, t):
    decay_loss = -math.expm1(-p['lam'] * t)
    a = p['A0'] + (p['Aeq'] - p['A0']) * decay_loss
    b = p['B0'] + (p['Beq'] - p['B0']) * decay_loss
    plus = p['V'] * p['kf'] * (p['Aeq'] * t + (p['A0'] - p['Aeq']) * decay_loss / p['lam'])
    minus = p['V'] * p['kr'] * (p['Beq'] * t + (p['B0'] - p['Beq']) * decay_loss / p['lam'])
    return dict(c_A=a, c_B=b, Xi_plus=plus, Xi_minus=minus, xi_net=plus - minus, G_ex=direct_g(p, a, b))


def closed_BE(p, h, t):
    """Independent fixed-step geometric formula, not a time-step recurrence."""
    n = int(t // h)
    loss = -math.expm1(-n * math.log1p(h * p['lam']))
    a = p['A0'] + (p['Aeq'] - p['A0']) * loss
    b = p['B0'] + (p['Beq'] - p['B0']) * loss
    plus = p['V'] * p['kf'] * (p['Aeq'] * n * h + (p['A0'] - p['Aeq']) * loss / p['lam'])
    minus = p['V'] * p['kr'] * (p['Beq'] * n * h + (p['B0'] - p['Beq']) * loss / p['lam'])
    weight = (t - n * h) / h
    if weight:
        anew = p['Aeq'] + (a - p['Aeq']) / (1 + h * p['lam'])
        bnew = p['Beq'] + (b - p['Beq']) / (1 + h * p['lam'])
        plus += weight * p['V'] * h * p['kf'] * anew
        minus += weight * p['V'] * h * p['kr'] * bnew
        a += weight * (anew - a)
        b += weight * (bnew - b)
    return dict(c_A=a, c_B=b, Xi_plus=plus, Xi_minus=minus, xi_net=plus - minus, G_ex=direct_g(p, a, b))


def check_saved(folder):
    schema = json.loads((Path(__file__).resolve().parent / 'inputs/export-schema.json').read_text())
    expected = {v['path']: v['columns'] for v in schema['files'] if v['path'].endswith('.csv')}
    mismatches = []
    for name, fields in expected.items():
        with (folder / name).open(newline='') as f:
            if next(csv.reader(f)) != fields:
                mismatches.append(name)
    pmap = {}
    for row in read(folder / 'case-settings.csv'):
        p = {k: float(row[col]) for k, col in [('A0', 'c_A0_mol_m3'), ('B0', 'c_B0_mol_m3'), ('C', 'C0_mol_m3'),
            ('V', 'V_liquid_m3'), ('cs', 'c_standard_mol_m3'), ('K', 'K_eq'), ('lam', 'lambda_s_inv'),
            ('kf', 'k_f_s_inv'), ('kr', 'k_r_s_inv')]}
        p['RT'] = float(row['T_K']) * float(row['R_J_mol_K'])
        p.update(Aeq=p['C'] / (1 + p['K']), Beq=p['C'] * p['K'] / (1 + p['K']), N=p['V'] * p['C'])
        p['G0'] = direct_g(p, p['A0'], p['B0'])
        pmap[row['case_id']] = p
    maxima = defaultdict(float)
    counts = defaultdict(int)
    previous, cumulative, aux_info = {}, {}, []
    def residual(metric, value):
        maxima[metric] = max(maxima[metric], abs(value))

    for row in read(folder / 'step-ledger.csv'):
        name, run = row['case_id'], row['run_id']
        p = pmap[name]; ns = max(p['N'], 1e-15); gs = p['RT'] * p['N'] if p['C'] else 1.0
        a, b, t = number(row, 'c_A'), number(row, 'c_B'), number(row, 'time_s')
        values = {key: number(row, key) for key in schema['unit_dictionary']}
        counts['ledger_rows'] += 1
        residual('saved_amount', (values['n_A'] - p['V'] * a) / ns)
        residual('saved_amount', (values['n_B'] - p['V'] * b) / ns)
        residual('saved_amount', (values['n_A'] + values['n_B'] - p['N']) / ns)
        g = direct_g(p, a, b)
        residual('saved_energy', (g - values['G_ex']) / gs)
        residual('saved_energy', (p['G0'] - g - values['D_state']) / gs)
        if t == 0:
            cumulative[run] = [0.0, 0.0]
            if any(values[k] != 0 for k in ('Xi_plus', 'Xi_minus', 'xi_net')) or number(row, 'actual_h_s') is not None:
                mismatches.append('initial ledger:' + run)
        else:
            old = previous[run]
            h = t - number(old, 'time_s')
            residual('saved_step_support', h - number(row, 'actual_h_s'))
            for i, (inc, col, rate, c) in enumerate([('delta_Xi_plus', 'Xi_plus', p['kf'], a), ('delta_Xi_minus', 'Xi_minus', p['kr'], b)]):
                reconstructed = p['V'] * h * rate * c
                residual('saved_amount', (reconstructed - values[inc]) / ns)
                cumulative[run][i] += reconstructed
                residual('saved_amount', (cumulative[run][i] - values[col]) / ns)
            for key, eq in (('c_A', p['Aeq']), ('c_B', p['Beq'])):
                scalar_new = eq + (number(old, key) - eq) / (1 + h * p['lam'])
                residual('saved_BE_inverse', (scalar_new - values[key]) / (p['C'] or 1.0))
            drop = direct_g(p, number(old, 'c_A'), number(old, 'c_B')) - g
            residual('saved_energy', (drop - values['delta_D_state']) / gs)
        xi = cumulative[run][0] - cumulative[run][1]
        residual('saved_amount', (xi - values['xi_net']) / ns)
        residual('saved_amount', (values['n_A'] - (p['V'] * p['A0'] - xi)) / ns)
        residual('saved_amount', (values['n_B'] - (p['V'] * p['B0'] + xi)) / ns)
        reason = 'empty_batch' if not p['C'] else ('zero_A_activity' if a == 0 else ('zero_B_activity' if b == 0 else ''))
        if reason:
            if values['delta_rG'] is not None or values['P_diss'] is not None or reason not in row['null_reason']:
                mismatches.append('null force/power:' + run)
            if values['Q'] != (0.0 if reason == 'zero_B_activity' else None):
                mismatches.append('null/zero Q:' + run)
        else:
            dg = p['RT'] * math.log((b / a) / p['K'])
            power = -p['V'] * (p['kf'] * a - p['kr'] * b) * dg
            residual('saved_force', (dg - values['delta_rG']) / p['RT'])
            residual('saved_energy', (power - values['P_diss']) / (gs * p['lam']))
            if t:
                w = number(row, 'actual_h_s') * power
                residual('saved_energy', (w - values['endpoint_power_energy']) / gs)
                residual('saved_energy', (values['delta_D_state'] - w - values['dissipation_gap']) / gs)
        if name not in ('forward', 'reverse', 'equilibrium'):
            ref = exact_reference(p, t)
            aux_info.append({'case_id': name, 'time_s': t, 'c_B': b, 'reference_c_B': ref['c_B'],
                             'G_ex': values['G_ex'], 'reference_G_ex': ref['G_ex'], 'accuracy_gate': 'not_applicable_auxiliary'})
        previous[run] = row
    errors = defaultdict(float)
    pair_values = defaultdict(lambda: defaultdict(dict))
    times_by_group = defaultdict(set)
    snapshots = [j * 80000 / 400 for j in range(401)]
    support_cache = {'snapshots-401': set(snapshots)}
    for row in read(folder / 'comparison.csv'):
        name, run, support, q = row['case_id'], row['run_id'], row['support_id'], row['quantity']
        p = pmap[name]; t = float(row['time_s']); h = float(run.split(':')[1][:-1])
        norm = p['C'] if q.startswith('c_') else (p['RT'] * p['N'] if q == 'G_ex' else p['N'])
        actual, ref = float(row['value']), float(row['reference_value'])
        residual('saved_reference', (exact_reference(p, t)[q] - ref) / norm)
        residual('saved_geometric_BE', (closed_BE(p, h, t)[q] - actual) / norm)
        residual('saved_error_column', (actual - ref - float(row['signed_error'])) / norm)
        errors[(name, run, support, q)] = max(errors[(name, run, support, q)], abs(actual - ref))
        group = (name, run, support, q)
        if t in times_by_group[group]:
            mismatches.append('duplicate comparison logical row')
        times_by_group[group].add(t)
        if support not in support_cache:
            top = float(support.split(':')[1]); sizes = [top, top / 2]
            if support.startswith('last-three'):
                sizes.append(top / 4)
            support_cache[support] = set(snapshots + [i * size for size in sizes for i in range(int(80000 / size) + 1)])
        interpolated = t % h != 0
        if row['candidate_interpolated'] != str(interpolated).lower():
            mismatches.append('interpolation label:' + run)
        if row['synthetic'] != 'true':
            mismatches.append('missing synthetic label')
        if support.startswith('halfstep'):
            pair_values[(name, support, q)][run][t] = actual
        counts['comparison_rows'] += 1
    for group, times in times_by_group.items():
        if times != support_cache[group[2]]:
            mismatches.append('support mismatch:' + repr(group))
    for row in read(folder / 'verification.csv'):
        value, norm, normalized = number(row, 'value'), number(row, 'normalizer'), number(row, 'normalized_value')
        if value is None:
            if row['status'] != 'UNRESOLVED' or not row['null_reason']:
                mismatches.append('unexplained null metric')
            continue
        residual('saved_metric_arithmetic', normalized - value / norm)
        low, high = number(row, 'threshold_lower'), number(row, 'threshold_upper')
        status = 'PASS' if (low is None or normalized >= low) and (high is None or normalized <= high) else 'FAIL'
        if status != row['status']:
            mismatches.append('metric status:' + row['metric'])
        name, run, support, metric = row['case_id'], row['run_id'], row['support_id'], row['metric']
        if row['benchmark_id'] == 'B06' and support == 'snapshots-401':
            q = next(q for q in ('Xi_plus', 'Xi_minus', 'xi_net', 'G_ex', 'c_A', 'c_B') if metric.startswith(q + '_'))
            residual('saved_refinement_metrics', (errors[(name, run, support, q)] - value) / norm)
        if row['benchmark_id'] == 'B07' and '_order_' in metric:
            q, step = metric.split('_order_'); h = float(step)
            e1 = errors[(name, name + ':' + format(h, 'g') + 's', support, q)]
            e2 = errors[(name, name + ':' + format(h / 2, 'g') + 's', support, q)]
            residual('saved_refinement_metrics', math.log2(e1 / e2) - value)
        if row['benchmark_id'] == 'B07' and support.startswith('halfstep'):
            q = next(q for q in ('Xi_plus', 'Xi_minus', 'xi_net', 'G_ex', 'c_A', 'c_B') if metric.startswith(q + '_'))
            pair = list(pair_values[(name, support, q)].values())
            reconstructed = max(abs(pair[0][t] - pair[1][t]) for t in support_cache[support])
            residual('saved_refinement_metrics', (reconstructed - value) / norm)
        counts['verification_numeric_rows'] += 1
    result_metrics = [{'metric': key, 'value': value, 'normalizer': 1.0,
                       'unit': '1 (maximum normalized reconstruction residual)', 'threshold': 1e-11}
                      for key, value in sorted(maxima.items())]
    result_metrics.append({'metric': 'saved_schema_ID_support_null_status_mismatch_count', 'value': len(mismatches),
                           'normalizer': 1.0, 'unit': 'count', 'threshold': 0.0})
    passed = all(m['value'] <= m['threshold'] for m in result_metrics)
    return {'status': 'PASS' if passed else 'FAIL', 'method': 'Independent CSV-only amount/energy/null/support/status reconstruction, independent exponential/integral reference and fixed-step geometric BE check; no model/solver import.',
            'metrics': result_metrics, 'row_counts': dict(counts), 'mismatches': mismatches,
            'auxiliary_reference_information': aux_info,
            'limits': 'Arithmetic/numerical verification only. Auxiliary accuracy is reported for information without production accuracy gates.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path)
    result = check_saved(parser.parse_args().folder)
    print(json.dumps(result, indent=2, allow_nan=False))
    raise SystemExit(0 if result['status'] == 'PASS' else 1)
