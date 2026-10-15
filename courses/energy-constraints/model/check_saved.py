"""Independent saved-CSV arithmetic/reference readback. No solver/model import."""
import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path


def read(path):
    with path.open(newline='') as f:
        for index, row in enumerate(csv.DictReader(f), 1):
            row['_where'] = f'{path.name} record {index} ' + repr(tuple(row.get(k) for k in ('case_id', 'run_id', 'time_s', 'benchmark_id', 'metric') if k in row))
            if None in row or any(v is None for v in row.values()):
                raise ValueError(row['_where'] + ': malformed CSV record')
            yield row


def number(row, key):
    raw = row[key]
    if raw == '':
        return None
    try:
        value = float(raw)
    except ValueError as error:
        raise ValueError(row['_where'] + ': invalid numeric field ' + key) from error
    if not math.isfinite(value):
        raise ValueError(row['_where'] + ': nonfinite numeric field ' + key)
    return value


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


def grid(end, step):
    return {min(i * step, end) for i in range(math.ceil(end / step) + 1)}


def declarations(settings, default, quantities):
    """Coverage from trusted course declarations, never from observed CSV groups."""
    core = [c['id'] for c in settings['core_cases']]
    end = settings['core_support']['window_s'][1]
    steps = [float(h) for h in settings['core_support']['ordered_refinement_steps_s']]
    # The bounded halving policy ends at 3.125 s, with a 1.5625 s partner.
    candidates = [settings['core_support']['candidate_step_s'] / 2**i for i in range(6)]
    if default not in candidates:
        raise ValueError('case-settings.csv nominal_h_s: default outside declared halving policy')
    candidates = candidates[:candidates.index(default) + 1]
    for candidate in candidates:
        steps += [h for h in (candidate, candidate / 2, candidate / 4) if h >= 1.5625]
    steps = sorted(set(steps), reverse=True)
    n = settings['core_support']['snapshot_count']
    snapshots = {j * end / (n - 1) for j in range(n)}
    order = default if default != 3.125 else 6.25
    support = {'snapshots-401': snapshots,
               'halfstep-union:' + format(default, 'g'): snapshots | grid(end, default) | grid(end, default / 2),
               'last-three-union:' + format(order, 'g'): snapshots | grid(end, order) | grid(end, order / 2) | grid(end, order / 4)}
    ledger = {(name, name + ':' + format(h, 'g') + 's'): grid(end, h)
              for name in core for h in (default, default / 2)}
    lam = settings['common']['lambda_s_inv']
    for case in settings['auxiliary_cases']:
        name, h = case['id'], case['nominal_step_s']
        terminal = 8 / lam + 1 / (3 * lam) if name == 'partial_final_step' else case['window_s'][1]
        ledger[(name, name + ':' + format(h, 'g') + 's')] = grid(terminal, h)
    comparison = {}
    for name in core:
        for label, sizes in [('snapshots-401', steps),
                             ('halfstep-union:' + format(default, 'g'), [default, default / 2]),
                             ('last-three-union:' + format(order, 'g'), [order, order / 2, order / 4])]:
            for h in sizes:
                for q in quantities:
                    comparison[(name, name + ':' + format(h, 'g') + 's', label, q)] = support[label]
    return core, steps, candidates, ledger, comparison


def metric_keys(settings, steps, candidates, quantities):
    """Declared metric IDs, independently enumerated from the unchanged runner contract."""
    keys = set()
    def add(bid, case, run, support, names):
        keys.update((bid, case, run, support, name) for name in names)
    add('B01', 'all', 'global', 'algebra', ['invalid_inputs_rejected', 'detailed_balance', 'standard_relation',
        'm2_written_basis_power', 'common_standard_cancels_reaction_G', 'declared_units_and_chemical_basis'])
    cases = settings['core_cases'] + settings['auxiliary_cases']
    for c in cases:
        names = ['initial_reference', 'reference_extent_identity', 'zero_time_gross_and_positive_reference']
        if c['id'] != 'empty':
            names += ['direct_binary_reference_G', 'analytical_ODE_substitution']
        add('B02', c['id'], 'global', 'reference-401-plus-small-z', names)
    scaled = [q + '_absolute' for q in quantities] + ['c_A_amplitude', 'c_B_amplitude', 'G_ex_initial_energy']
    for case in cases:
        name = case['id']; core = name in [c['id'] for c in settings['core_cases']]
        for h in steps if core else [case['nominal_step_s']]:
            run = name + ':' + format(h, 'g') + 's'
            add('B03', name, run, 'native', ['nonnegative_and_strict_positive_time', 'gross_nonnegative_monotone',
                'total_residual', 'A_extent_residual', 'B_extent_residual', 'overshoot'] + (['empty_exact_zero'] if name == 'empty' else []))
            if name != 'empty':
                add('B04', name, run, 'native', ['flux_force'])
            if name == 'equilibrium':
                add('B04', name, run, 'native', ['equilibrium_r_net', 'equilibrium_delta_rG', 'equilibrium_G_ex',
                    'equilibrium_gross_positive', 'equilibrium_net_extent'])
            elif name in ('forward', 'reverse'):
                add('B04', name, run, 'native', ['net_direction'])
            add('B05', name, run, 'native', ['min_G_ex', 'min_state_drop', 'telescoping_residual', 'exact_null_domains'] +
                (['min_power_times_tau', 'min_gap'] if name != 'empty' else []))
            if core:
                for support in ('native', 'snapshots-401'):
                    add('B06', name, run, support, scaled)
    for candidate in candidates:
        order = candidate if candidate != 3.125 else 6.25
        for c in settings['core_cases']:
            name = c['id']; run = name + ':' + format(order, 'g') + 's'
            add('B07', name, run, 'halfstep-union:' + format(order, 'g'), scaled)
            for support in ('snapshots-401', 'last-three-union:' + format(order, 'g')):
                add('B07', name, run, support, [q + '_order_' + format(h, 'g') for q in ('c_A', 'c_B') for h in (order, order / 2)])
            if candidate != order:
                add('B07', name, name + ':' + format(candidate, 'g') + 's', 'halfstep-union:' + format(candidate, 'g'), scaled)
    for c in settings['auxiliary_cases']:
        name = c['id']; run = name + ':' + format(c['nominal_step_s'], 'g') + 's'
        add('B08', name, run, 'native', ['exact_partial_terminal' if name == 'partial_final_step' else 'two_full_10tau_steps'])
    return keys


def check_saved(folder, *, phase='final'):
    if phase not in ('final', 'pre-append'):
        raise ValueError('Unknown saved-CSV phase: ' + str(phase))
    root = Path(__file__).resolve().parent
    schema = json.loads((root / 'inputs/export-schema.json').read_text())
    settings = json.loads((root / 'inputs/proposed-settings.json').read_text())
    expected = {v['path']: v['columns'] for v in schema['files'] if v['path'].endswith('.csv')}
    mismatches = []
    for name, fields in expected.items():
        with (folder / name).open(newline='') as f:
            if next(csv.reader(f)) != fields:
                raise ValueError(name + ': schema header mismatch')
    quantities = next(f['quantities'] for f in schema['files'] if f['path'] == 'comparison.csv')
    numeric = {'case-settings.csv': set(expected['case-settings.csv']) - {'case_id', 'role', 'synthetic', 'parameter_source'},
               'step-ledger.csv': set(schema['unit_dictionary']) | {'time_s', 'actual_h_s', 'actual_h_over_tau', 'nominal_h_s'},
               'comparison.csv': {'time_s', 'value', 'reference_value', 'signed_error'},
               'verification.csv': {'attempt_index', 'value', 'normalizer', 'normalized_value', 'threshold_lower', 'threshold_upper'}}
    def rows(name):
        for row in read(folder / name):
            values = {k: number(row, k) for k in numeric[name]}
            nulls = set()
            if name == 'step-ledger.csv':
                if values['time_s'] == 0:
                    nulls |= {'actual_h_s', 'actual_h_over_tau', 'delta_Xi_plus', 'delta_Xi_minus', 'delta_D_state', 'endpoint_power_energy', 'dissipation_gap'}
                if values['c_A'] == 0 or values['c_B'] == 0:
                    nulls |= {'delta_rG', 'P_diss'}
                if values['c_A'] == 0:
                    nulls.add('Q')
                if values['c_A'] == values['c_B'] == 0:
                    nulls |= {'endpoint_power_energy', 'dissipation_gap'}
                reason = 'empty_batch' if values['c_A'] == values['c_B'] == 0 else ('zero_A_activity' if values['c_A'] == 0 else ('zero_B_activity' if values['c_B'] == 0 else ''))
                reasons = {reason} if reason else set()
                if values['time_s'] == 0:
                    reasons.add('not_applicable_initial_step')
                if set(filter(None, row['null_reason'].split(';'))) != reasons:
                    raise ValueError(row['_where'] + ': incorrect null_reason')
                status = 'empty' if reason == 'empty_batch' else ('zero_boundary' if reason else 'finite')
                if row['thermo_status'] != status:
                    raise ValueError(row['_where'] + ': incorrect thermo_status')
            elif name == 'verification.csv':
                # Missing bounds are legitimate one-sided criteria, not numeric zeros.
                nulls |= {k for k in ('threshold_lower', 'threshold_upper') if values[k] is None}
                if row['status'] == 'UNRESOLVED':
                    relative = row['case_id'] == 'equilibrium' and row['metric'].endswith(('_amplitude', '_initial_energy'))
                    order = '_order_' in row['metric'] and row['null_reason'] == ('zero_initial_deviation' if row['case_id'] == 'equilibrium' else 'below_metric_floor')
                    if not (relative or order):
                        raise ValueError(row['_where'] + ': forbidden unresolved metric')
                    nulls |= {'value', 'normalized_value'}
                    if relative:
                        reason = 'zero_initial_deviation' if row['metric'].endswith('_amplitude') else 'zero_initial_free_energy'
                        if row['null_reason'] != reason:
                            raise ValueError(row['_where'] + ': incorrect relative-metric null_reason')
                        nulls.add('normalizer')
                if values['threshold_lower'] is None and values['threshold_upper'] is None:
                    raise ValueError(row['_where'] + ': missing threshold_lower/threshold_upper')
                if values['normalizer'] is not None and values['normalizer'] <= 0:
                    raise ValueError(row['_where'] + ': nonpositive normalizer')
                if values['attempt_index'] is None or values['attempt_index'] < 0 or not values['attempt_index'].is_integer():
                    raise ValueError(row['_where'] + ': invalid attempt_index')
            for key, value in values.items():
                if (value is None) != (key in nulls):
                    raise ValueError(row['_where'] + ': forbidden blank/value in ' + key)
            if row['synthetic'] != 'true':
                raise ValueError(row['_where'] + ': missing synthetic label')
            yield row
    def complete(label, actual, wanted):
        if actual != wanted:
            raise ValueError(label + ': declared coverage mismatch; missing ' + repr(min(wanted - actual, default=None)) +
                             '; unexpected ' + repr(min(actual - wanted, default=None)))
    pmap = {}
    declared_cases = {c['id']: c for c in settings['core_cases'] + settings['auxiliary_cases']}
    defaults = set()
    for row in rows('case-settings.csv'):
        name = row['case_id']
        if name not in declared_cases or name in pmap:
            raise ValueError(row['_where'] + ': unknown/duplicate case')
        case, common = declared_cases[name], settings['common']
        c = case.get('total_concentration_mol_m3', common['total_concentration_mol_m3'])
        k, lam = common['K_eq_dimensionless'], common['lambda_s_inv']
        x = case['initial_x_B']; x = k / (1 + k) if isinstance(x, str) else (0 if x is None else x)
        is_core = name in [c['id'] for c in settings['core_cases']]
        terminal = settings['core_support']['window_s'][1] if is_core else (8 / lam + 1 / (3 * lam) if name == 'partial_final_step' else case['window_s'][1])
        declared = dict(T_K=common['temperature_K'], p_Pa=common['pressure_Pa'], V_liquid_m3=common['liquid_volume_m3'],
            c_standard_mol_m3=common['standard_concentration_mol_m3'], R_J_mol_K=common['gas_constant_J_mol_K'], C0_mol_m3=c,
            c_A0_mol_m3=c * (1 - x), c_B0_mol_m3=c * x, K_eq=k, lambda_s_inv=lam, k_f_s_inv=lam * k / (1 + k),
            k_r_s_inv=lam / (1 + k), delta_rG_standard_J_mol=-common['gas_constant_J_mol_K'] * common['temperature_K'] * math.log(k),
            window_end_s=terminal, reference_equilibrium_fraction_B=k / (1 + k))
        if not is_core:
            declared['nominal_h_s'] = case['nominal_step_s']
        for key, value in declared.items():
            if not math.isclose(number(row, key), value, rel_tol=1e-12, abs_tol=0):
                raise ValueError(row['_where'] + ': settings declaration mismatch in ' + key)
        if row['role'] != ('core' if is_core else 'auxiliary'):
            raise ValueError(row['_where'] + ': role mismatch')
        if is_core:
            defaults.add(number(row, 'nominal_h_s'))
        p = {k: float(row[col]) for k, col in [('A0', 'c_A0_mol_m3'), ('B0', 'c_B0_mol_m3'), ('C', 'C0_mol_m3'),
            ('V', 'V_liquid_m3'), ('cs', 'c_standard_mol_m3'), ('K', 'K_eq'), ('lam', 'lambda_s_inv'),
            ('kf', 'k_f_s_inv'), ('kr', 'k_r_s_inv')]}
        p['RT'] = float(row['T_K']) * float(row['R_J_mol_K'])
        p.update(Aeq=p['C'] / (1 + p['K']), Beq=p['C'] * p['K'] / (1 + p['K']), N=p['V'] * p['C'])
        p['G0'] = direct_g(p, p['A0'], p['B0'])
        pmap[row['case_id']] = p
    complete('case-settings.csv case IDs', set(pmap), set(declared_cases))
    if len(defaults) != 1:
        raise ValueError('case-settings.csv: inconsistent core default steps')
    core, steps, candidates, wanted_ledger, wanted_comparison = declarations(settings, defaults.pop(), quantities)
    wanted_metrics = metric_keys(settings, steps, candidates, quantities)
    ledger_end = {key: max(times) for key, times in wanted_ledger.items()}
    ledger_times = defaultdict(set)
    metric_ids = set()
    maxima = defaultdict(float)
    counts = defaultdict(int)
    previous, cumulative, aux_info = {}, {}, []
    def residual(metric, value):
        if not math.isfinite(value):
            raise ValueError(where + ': nonfinite reconstruction residual ' + metric)
        maxima[metric] = max(maxima[metric], abs(value))

    where = 'saved CSV reduction'
    for row in rows('step-ledger.csv'):
        where = row['_where']
        name, run = row['case_id'], row['run_id']
        if name not in pmap:
            raise ValueError(where + ': undeclared ledger case_id')
        p = pmap[name]; ns = max(p['N'], 1e-15); gs = p['RT'] * p['N'] if p['C'] else 1.0
        a, b, t = number(row, 'c_A'), number(row, 'c_B'), number(row, 'time_s')
        values = {key: number(row, key) for key in schema['unit_dictionary']}
        key = (name, run)
        if key not in wanted_ledger or t not in wanted_ledger[key] or t in ledger_times[key]:
            raise ValueError(where + ': unknown/duplicate ledger logical key or time')
        ledger_times[key].add(t)
        if row['sample_kind'] != 'native_BE_endpoint' or number(row, 'nominal_h_s') != float(run.split(':')[1][:-1]):
            raise ValueError(where + ': native support/nominal step mismatch')
        if t and (run not in previous or t <= number(previous[run], 'time_s')):
            raise ValueError(where + ': missing start or nonascending ledger time')
        if t and t - number(previous[run], 'time_s') != min(number(row, 'nominal_h_s'), ledger_end[key] - number(previous[run], 'time_s')):
            raise ValueError(where + ': missing or wrong native interval')
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
    complete('step-ledger.csv run groups', set(ledger_times), set(wanted_ledger))
    for key, times in ledger_times.items():
        complete('step-ledger.csv times ' + repr(key), times, wanted_ledger[key])
    errors = defaultdict(float)
    pair_values = defaultdict(lambda: defaultdict(dict))
    times_by_group = defaultdict(set)
    support_cache = {group[2]: times for group, times in wanted_comparison.items()}
    for row in rows('comparison.csv'):
        where = row['_where']
        name, run, support, q = row['case_id'], row['run_id'], row['support_id'], row['quantity']
        group = (name, run, support, q)
        if group not in wanted_comparison:
            raise ValueError(where + ': unknown comparison group')
        p = pmap[name]; t = number(row, 'time_s'); h = float(run.split(':')[1][:-1])
        if t not in wanted_comparison[group] or t in times_by_group[group]:
            raise ValueError(where + ': unknown/duplicate comparison logical key or time')
        if row['unit'] != schema['unit_dictionary'][q] or row['reference_method'] != 'independent_exponential_integrated_throughput' or row['null_reason']:
            raise ValueError(where + ': comparison unit/reference/null provenance mismatch')
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
        interpolated = t % h != 0
        if row['candidate_interpolated'] != str(interpolated).lower():
            mismatches.append('interpolation label:' + run)
        if row['synthetic'] != 'true':
            mismatches.append('missing synthetic label')
        if support.startswith('halfstep'):
            pair_values[(name, support, q)][run][t] = actual
        counts['comparison_rows'] += 1
    complete('comparison.csv groups', set(times_by_group), set(wanted_comparison))
    for group, times in times_by_group.items():
        complete('comparison.csv times ' + repr(group), times, wanted_comparison[group])
    saved_rows = []
    for row in rows('verification.csv'):
        where = row['_where']
        key = tuple(row[k] for k in ('benchmark_id', 'case_id', 'run_id', 'support_id', 'metric'))
        if key[:4] == ('B08', 'all', 'global', 'saved-CSV'):
            saved_rows.append(row)
            counts['verification_numeric_rows'] += 1  # Reporting only, excluded from reductions.
            continue
        if key not in wanted_metrics:
            raise ValueError(where + ': undeclared verification metric ID')
        if key in metric_ids:
            raise ValueError(where + ': duplicate verification logical key')
        metric_ids.add(key)
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
    complete('verification.csv metric IDs', metric_ids, wanted_metrics)
    # Reconcile only after independent ordinary reductions, never recursively.
    if phase == 'pre-append':
        if saved_rows:
            raise ValueError('verification.csv saved-CSV group field metric: pre-append phase requires group absent')
    else:
        expected_saved = {m['metric']: m for m in result_metrics}
        recorded = {}
        for row in saved_rows:
            metric = row['metric']
            if metric not in expected_saved:
                raise ValueError('verification.csv saved-CSV metric ' + metric + ' field metric: undeclared metric')
            if metric in recorded:
                raise ValueError('verification.csv saved-CSV metric ' + metric + ' field metric: duplicate logical key')
            recorded[metric] = row
        if set(recorded) != set(expected_saved):
            raise ValueError('verification.csv saved-CSV group field metric: final phase requires exactly 11 declared metrics')
        expected_rows = {}
        for metric, m in expected_saved.items():
            expected_rows[metric] = dict(value=m['value'], normalizer=m['normalizer'],
                normalized_value=m['value'] / m['normalizer'], threshold_lower=None,
                threshold_upper=m['threshold'], unit=m['unit'],
                criterion=f"normalized <= {m['threshold']}",
                status='PASS' if m['value'] <= m['threshold'] else 'FAIL',
                null_reason='', synthetic='true', benchmark_id='B08',
                case_id='all', run_id='global', support_id='saved-CSV', metric=metric)
        numeric_fields = {'value', 'normalizer', 'normalized_value', 'threshold_lower', 'threshold_upper'}
        # Field-major precedence binds diagnostics independently of CSV row order.
        for field in ('value', 'normalizer', 'normalized_value', 'threshold_lower', 'threshold_upper',
                      'unit', 'criterion', 'status', 'null_reason', 'synthetic',
                      'benchmark_id', 'case_id', 'run_id', 'support_id', 'metric'):
            for metric in expected_saved:
                row = recorded[metric]
                actual = number(row, field) if field in numeric_fields else row[field]
                if actual != expected_rows[metric][field]:
                    raise ValueError('verification.csv saved-CSV metric ' + metric + ' field ' + field + ': recorded/reconstructed mismatch')
    passed = all(m['value'] <= m['threshold'] for m in result_metrics)
    return {'status': 'PASS' if passed else 'FAIL', 'phase': phase, 'method': 'Independent CSV-only amount/energy/null/support/status reconstruction, independent exponential/integral reference and fixed-step geometric BE check; no model/solver import.',
            'metrics': result_metrics, 'row_counts': dict(counts), 'mismatches': mismatches,
            'auxiliary_reference_information': aux_info,
            'limits': 'Arithmetic/numerical verification only. Auxiliary accuracy is reported for information without production accuracy gates.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder', type=Path)
    parser.add_argument('--phase', choices=('final', 'pre-append'), default='final')
    args = parser.parse_args()
    result = check_saved(args.folder, phase=args.phase)
    print(json.dumps(result, indent=2, allow_nan=False))
    raise SystemExit(0 if result['status'] == 'PASS' else 1)
