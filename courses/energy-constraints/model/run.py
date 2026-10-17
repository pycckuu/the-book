"""Execute the frozen ENERGY plan and write its four declared CSV families."""
import argparse
import csv
import hashlib
import html
import json
import math
from pathlib import Path

from model import parameters, validate, solve, sample, reference, gibbs

ROOT = Path(__file__).resolve().parent
QUANTITIES = ('c_A', 'c_B', 'G_ex', 'xi_net', 'Xi_plus', 'Xi_minus')


def dump(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False) + '\n')


def cell(value):
    if value is None:
        return ''
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ArithmeticError('nonfinite CSV value')
        return format(value, '.17g')
    return value


def write_csv(path, columns, records):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore')
        writer.writeheader()
        for record in records:
            writer.writerow({k: cell(record.get(k)) for k in columns})


def execute(out):
    if not __debug__:
        raise RuntimeError("Verification requires normal Python; remove -O/-OO and unset PYTHONOPTIMIZE.")
    settings = json.loads((ROOT / 'inputs/proposed-settings.json').read_text())
    schema = json.loads((ROOT / 'inputs/export-schema.json').read_text())
    clarifications = json.loads((ROOT / 'inputs/clarifications.json').read_text())
    manifest = json.loads((ROOT / 'execution-manifest.json').read_text())
    for name, digest in manifest['file_pins'].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    out.mkdir(parents=True, exist_ok=False)
    columns = {f['path']: f['columns'] for f in schema['files'] if f['path'].endswith('.csv')}
    units = schema['unit_dictionary']
    cases = settings['core_cases'] + settings['auxiliary_cases']
    pmap = {c['id']: parameters(settings['common'], c) for c in cases}
    core = [c['id'] for c in settings['core_cases']]
    end = settings['core_support']['window_s'][1]
    snapshots = [j * end / 400 for j in range(401)]
    metrics, histories, runs = [], [], {}
    attempt = 0

    def record(bid, metric, value, norm=1.0, lower=None, upper=None,
               case='all', run='global', support='algebra', unit='1', reason=''):
        normalized = value / norm if value is not None and norm is not None else None
        if normalized is None:
            status = 'UNRESOLVED'
        else:
            if not math.isfinite(normalized):
                raise ArithmeticError('nonfinite verification metric: ' + metric)
            status = 'PASS' if (lower is None or normalized >= lower) and (upper is None or normalized <= upper) else 'FAIL'
        row = dict(attempt_index=attempt, case_id=case, run_id=run, benchmark_id=bid,
                   metric=metric, support_id=support, value=value, normalizer=norm,
                   normalized_value=normalized, unit=unit, criterion='; '.join(
                       s for s in ((f'normalized >= {lower}' if lower is not None else ''),
                                   (f'normalized <= {upper}' if upper is not None else '')) if s),
                   threshold_lower=lower, threshold_upper=upper, status=status,
                   null_reason=reason, synthetic=True)
        metrics.append(row)
        return status

    def check(bid, name, condition, **kw):
        return record(bid, name, 0.0 if condition else 1.0, upper=0.0, **kw)

    # B01 is a domain/algebra check, not an added numerical case family.
    base = pmap['forward']
    invalids = []
    for key in ('T', 'V', 'cs', 'R', 'K', 'lam', 'p'):
        for value in (0.0, -1.0, math.inf, math.nan):
            trial = dict(base, **{key: value})
            try:
                validate(trial)
            except ValueError:
                invalids.append({'field': key, 'input': repr(value), 'rejected': True})
            else:
                invalids.append({'field': key, 'input': repr(value), 'rejected': False})
    for key in ('A0', 'B0', 'C'):
        for value in (-1.0, math.inf, math.nan):
            try:
                validate(dict(base, **{key: value}))
            except ValueError:
                invalids.append({'field': key, 'input': repr(value), 'rejected': True})
            else:
                invalids.append({'field': key, 'input': repr(value), 'rejected': False})
    check('B01', 'invalid_inputs_rejected', all(v['rejected'] for v in invalids))
    record('B01', 'detailed_balance', abs(base['kf'] / base['kr'] / base['K'] - 1), upper=1e-12)
    record('B01', 'standard_relation', abs((-base['RT'] * math.log(base['K'])) / base['RT'] + math.log(base['K'])), upper=1e-12)
    state = reference(base, 1000.0)
    record('B01', 'm2_written_basis_power', abs((-base['V'] * (state['r_net'] / 2) * (2 * state['delta_rG'])) - state['P_diss']),
           norm=base['RT'] * base['N'] / base['tau'], upper=1e-12, unit='W')
    doubled = dict(base, cs=2 * base['cs'])
    record('B01', 'common_standard_cancels_reaction_G', abs(reference(doubled, 1000)['delta_rG'] - state['delta_rG']),
           norm=base['RT'], upper=1e-12, unit='J mol^-1 written A->B')
    check('B01', 'declared_units_and_chemical_basis', units['n_A'] == 'mol equivalent' and units['delta_rG'] == 'J mol^-1 written A->B')

    # B02 reference substitution, gross accounting and independent binary Gibbs.
    for name, p in pmap.items():
        ns = max(p['N'], 1e-15)
        gs = p['RT'] * p['N'] if p['C'] else 1.0
        reference_times = [0.0, 1e-6 * p['tau']] + snapshots
        refs = [reference(p, t) for t in reference_times]
        kw = dict(case=name, support='reference-401-plus-small-z')
        record('B02', 'initial_reference', max(abs(refs[0]['c_A'] - p['A0']), abs(refs[0]['c_B'] - p['B0'])),
               norm=p['C'] or 1.0, upper=1e-12, unit='mol m^-3', **kw)
        record('B02', 'reference_extent_identity', max(max(abs(r['A_extent_residual']), abs(r['B_extent_residual'])) for r in refs),
               norm=ns, upper=1e-12, unit='mol', **kw)
        check('B02', 'zero_time_gross_and_positive_reference', refs[0]['Xi_plus'] == refs[0]['Xi_minus'] == 0 and
              all(t == 0 or (r['c_A'] > 0 and r['c_B'] > 0) for t, r in zip(reference_times, refs)) if p['C'] else all(r['G_ex'] == 0 for r in refs), **kw)
        if p['C']:
            xe = p['Beq'] / p['C']
            differences = []
            for r in refs:
                x = r['c_B'] / p['C']
                binary = p['RT'] * p['N'] * math.fsum((x * math.log(x / xe) if x else 0,
                    (1 - x) * math.log((1 - x) / (1 - xe)) if x != 1 else 0))
                differences.append(abs(binary - r['G_ex']))
            record('B02', 'direct_binary_reference_G', max(differences), norm=gs, upper=1e-12, unit='J', **kw)
            derivative_errors = [abs(p['lam'] * (p['Beq'] - p['B0']) * math.exp(-p['lam'] * t) - reference(p, t)['r_net']) for t in snapshots]
            record('B02', 'analytical_ODE_substitution', max(derivative_errors), norm=p['lam'] * p['C'], upper=1e-12,
                   unit='mol m^-3 s^-1', **kw)

    def inspect(name, h, rows, auxiliary=False):
        p = pmap[name]
        rid = name + ':' + format(h, 'g') + 's'
        kw = dict(case=name, run=rid, support='native')
        ns, gs = max(p['N'], 1e-15), p['RT'] * p['N'] if p['C'] else 1.0
        check('B03', 'nonnegative_and_strict_positive_time', all(r['c_A'] >= 0 and r['c_B'] >= 0 and
              (not p['C'] or r['time_s'] == 0 or (r['c_A'] > 0 and r['c_B'] > 0)) for r in rows), **kw)
        check('B03', 'gross_nonnegative_monotone', all(r['Xi_plus'] >= 0 and r['Xi_minus'] >= 0 for r in rows) and
              all(new['Xi_plus'] >= old['Xi_plus'] and new['Xi_minus'] >= old['Xi_minus'] for old, new in zip(rows, rows[1:])), **kw)
        for key in ('total_residual', 'A_extent_residual', 'B_extent_residual'):
            record('B03', key, max(abs(r[key]) for r in rows), norm=ns, upper=1e-11, unit='mol', **kw)
        overshoot = max(max(0.0, min(p['B0'], p['Beq']) - r['c_B'], r['c_B'] - max(p['B0'], p['Beq']),
                            min(p['A0'], p['Aeq']) - r['c_A'], r['c_A'] - max(p['A0'], p['Aeq'])) for r in rows)
        record('B03', 'overshoot', overshoot, norm=p['C'] or 1.0, upper=1e-12, unit='mol m^-3', **kw)
        if not p['C']:
            check('B03', 'empty_exact_zero', all(all(r[k] == 0 for k in ('c_A', 'c_B', 'n_A', 'n_B', 'Xi_plus', 'Xi_minus', 'xi_net', 'G_ex', 'D_state')) for r in rows), **kw)
        finite = [r for r in rows if r['delta_rG'] is not None]
        if finite:
            record('B04', 'flux_force', max(abs(math.log(r['r_plus'] / r['r_minus']) + r['delta_rG'] / p['RT']) for r in finite), upper=1e-12, **kw)
        if name == 'equilibrium':
            for key, norm, unit in [('r_net', p['lam'] * p['C'], 'mol m^-3 s^-1'), ('delta_rG', p['RT'], 'J mol^-1'), ('G_ex', gs, 'J')]:
                record('B04', 'equilibrium_' + key, max(abs(r[key]) for r in rows), norm=norm, upper=1e-12, unit=unit, **kw)
            check('B04', 'equilibrium_gross_positive', all(r['r_plus'] > 0 and r['r_minus'] > 0 for r in rows), **kw)
            record('B04', 'equilibrium_net_extent', max(abs(r['xi_net']) for r in rows), norm=ns, upper=1e-12, unit='mol', **kw)
        elif name in ('forward', 'reverse'):
            sign = 1 if name == 'forward' else -1
            record('B04', 'net_direction', min(sign * r['r_net'] for r in rows), norm=p['lam'] * p['C'], lower=-1e-12, **kw)
        record('B05', 'min_G_ex', min(r['G_ex'] for r in rows), norm=gs, lower=-1e-12, unit='J', **kw)
        record('B05', 'min_state_drop', min(r['delta_D_state'] for r in rows[1:]), norm=gs, lower=-1e-12, unit='J', **kw)
        if finite:
            record('B05', 'min_power_times_tau', min(r['P_diss'] * p['tau'] for r in finite), norm=gs, lower=-1e-12, unit='J', **kw)
            record('B05', 'min_gap', min(r['dissipation_gap'] for r in rows[1:]), norm=gs, lower=-1e-12, unit='J', **kw)
        record('B05', 'telescoping_residual', abs(math.fsum(r['delta_D_state'] for r in rows[1:]) - rows[-1]['D_state']), norm=gs, upper=1e-11, unit='J', **kw)
        initial = rows[0]
        expected_reason = 'empty_batch' if not p['C'] else ('zero_A_activity' if p['A0'] == 0 else ('zero_B_activity' if p['B0'] == 0 else ''))
        valid_nulls = initial['null_reason'] == expected_reason and initial['actual_h_s'] is None and initial['endpoint_power_energy'] is None
        if expected_reason:
            valid_nulls &= initial['delta_rG'] is None and initial['P_diss'] is None
            valid_nulls &= initial['Q'] == 0 if expected_reason == 'zero_B_activity' else initial['Q'] is None
        valid_nulls &= all((r['P_diss'] is None and r['Q'] is None and r['null_reason'] == 'empty_batch') if not p['C'] else
                          (r['P_diss'] is not None and r['null_reason'] == '') for r in rows[1:])
        check('B05', 'exact_null_domains', valid_nulls, **kw)
        if not auxiliary:
            accuracy(name, h, rows)
        return rid

    def errors(name, rows, times):
        p = pmap[name]
        native_times = [r['time_s'] for r in rows]
        values = {q: 0.0 for q in QUANTITIES}
        for t in times:
            actual, _ = sample(p, rows, t, native_times)
            ref = reference(p, t)
            for q in QUANTITIES:
                values[q] = max(values[q], abs(actual[q] - ref[q]))
        return values

    def scaled_metrics(bid, name, rid, support, values, threshold):
        p = pmap[name]
        for q in QUANTITIES:
            normalizers = [(p['C'] if q.startswith('c_') else (p['RT'] * p['N'] if q == 'G_ex' else p['N']), 'absolute')]
            if q.startswith('c_'):
                normalizers.append((abs(p['B0'] - p['Beq']), 'amplitude'))
            if q == 'G_ex':
                normalizers.append((p['G0'], 'initial_energy'))
            for norm, label in normalizers:
                unavailable = name == 'equilibrium' and label != 'absolute'
                record(bid, q + '_' + label, None if unavailable else values[q], norm=None if unavailable else norm,
                       upper=threshold, case=name, run=rid, support=support, unit=units[q],
                       reason=('zero_initial_deviation' if label == 'amplitude' else 'zero_initial_free_energy') if unavailable else '')

    def accuracy(name, h, rows):
        rid = name + ':' + format(h, 'g') + 's'
        for label, times in [('native', [r['time_s'] for r in rows]), ('snapshots-401', snapshots)]:
            values = errors(name, rows, times)
            scaled_metrics('B06', name, rid, label, values, 1e-12 if name == 'equilibrium' else .005)

    def refinement(candidate):
        union = sorted(set(snapshots + [r['time_s'] for r in runs[('forward', candidate)]] +
                           [r['time_s'] for r in runs[('forward', candidate / 2)]]))
        sizes = [candidate, candidate / 2, candidate / 4]
        order_union = sorted(set(snapshots + [r['time_s'] for size in sizes for r in runs[('forward', size)]]))
        for name in core:
            p = pmap[name]
            rid = name + ':' + format(candidate, 'g') + 's'
            large, small = runs[(name, candidate)], runs[(name, candidate / 2)]
            lt, st = [r['time_s'] for r in large], [r['time_s'] for r in small]
            values = {q: 0.0 for q in QUANTITIES}
            for t in union:
                a, _ = sample(p, large, t, lt)
                b, _ = sample(p, small, t, st)
                for q in QUANTITIES:
                    values[q] = max(values[q], abs(a[q] - b[q]))
            scaled_metrics('B07', name, rid, 'halfstep-union:' + format(candidate, 'g'), values, 1e-12 if name == 'equilibrium' else .0025)
            for support, times in [('snapshots-401', snapshots), ('last-three-union:' + format(candidate, 'g'), order_union)]:
                errs = [errors(name, runs[(name, size)], times) for size in sizes]
                for q in ('c_A', 'c_B'):
                    for i in (0, 1):
                        e1, e2 = errs[i][q] / p['C'], errs[i + 1][q] / p['C']
                        informative = name != 'equilibrium' and min(e1, e2) > 1e-12
                        record('B07', q + '_order_' + format(sizes[i], 'g'), math.log2(e1 / e2) if informative else None,
                               lower=.8, upper=1.2, case=name, run=rid, support=support,
                               reason='' if informative else ('zero_initial_deviation' if name == 'equilibrium' else 'below_metric_floor'))
        return union, order_union

    def attempt_size(h):
        nonlocal attempt
        attempt += 1
        start = len(metrics)
        for name in core:
            rows = solve(pmap[name], end, h)
            runs[(name, h)] = rows
            inspect(name, h, rows)
        tested = metrics[start:]
        histories.append({'attempt_index': attempt, 'step_s': h,
                          'direct_run_gate_status': 'FAIL' if any(r['status'] == 'FAIL' for r in tested) else 'PASS',
                          'failed_metrics': [{k: r[k] for k in ('case_id', 'benchmark_id', 'metric', 'support_id', 'normalized_value', 'threshold_upper')}
                                             for r in tested if r['status'] == 'FAIL']})

    for h in settings['core_support']['ordered_refinement_steps_s']:
        attempt_size(float(h))
    for case in settings['auxiliary_cases']:
        name = case['id']
        p = pmap[name]
        terminal = 8 / p['lam'] + 1 / (3 * p['lam']) if name == 'partial_final_step' else case['window_s'][1]
        h = case['nominal_step_s']
        rows = solve(p, terminal, h)
        runs[(name, h)] = rows
        rid = inspect(name, h, rows, auxiliary=True)
        if name != 'partial_final_step':
            check('B08', 'two_full_10tau_steps', len(rows) == 3 and all(r['actual_h_over_tau'] == 10 for r in rows[1:]), case=name, run=rid, support='native')
        else:
            check('B08', 'exact_partial_terminal', rows[-1]['time_s'] == terminal and 0 < rows[-1]['actual_h_s'] < h, case=name, run=rid, support='native')

    default, candidate_decisions = None, []
    for candidate in (100.0, 50.0, 25.0, 12.5, 6.25, 3.125):
        for h in (candidate, candidate / 2, candidate / 4):
            if ('forward', h) not in runs:
                # The finest 1.5625 s partner has no additional order requirement;
                # order uses the last three allowed sizes, never a tenth mesh.
                if h < 1.5625:
                    continue
                attempt_size(h)
        if candidate == 3.125:
            # Use the last three allowed sizes for order and this candidate's pair.
            order_candidate = 6.25
        else:
            order_candidate = candidate
        start = len(metrics)
        pair_union, order_union = refinement(order_candidate)
        if order_candidate != candidate:
            # The 6.25/3.125 comparison is stricter evidence, and also explicitly
            # record the final 3.125/1.5625 pair on its own frozen common support.
            final_union = sorted(set(snapshots + [r['time_s'] for h in (candidate, candidate / 2) for r in runs[('forward', h)]]))
            for name in core:
                p = pmap[name]; values = {q: 0.0 for q in QUANTITIES}
                rows1, rows2 = runs[(name, candidate)], runs[(name, candidate / 2)]
                ts1, ts2 = [r['time_s'] for r in rows1], [r['time_s'] for r in rows2]
                for t in final_union:
                    a, _ = sample(p, rows1, t, ts1); b, _ = sample(p, rows2, t, ts2)
                    for q in QUANTITIES: values[q] = max(values[q], abs(a[q] - b[q]))
                scaled_metrics('B07', name, name + ':' + format(candidate, 'g') + 's', 'halfstep-union:' + format(candidate, 'g'), values, 1e-12 if name == 'equilibrium' else .0025)
            pair_union = final_union
        selected_runs = {name + ':' + format(h, 'g') + 's' for name in core for h in (candidate, candidate / 2, order_candidate / 4)}
        relevant = [r for r in metrics if r['benchmark_id'] in ('B01', 'B02', 'B08') or
                    (r['benchmark_id'] in ('B03', 'B04', 'B05') and (r['run_id'] in selected_runs or r['case_id'] not in core)) or
                    (r['benchmark_id'] == 'B06' and r['run_id'] in selected_runs)] + metrics[start:]
        informative_unresolved = [r for r in relevant if r['status'] == 'UNRESOLVED' and r['case_id'] != 'equilibrium']
        ok = not any(r['status'] == 'FAIL' for r in relevant) and not informative_unresolved
        candidate_decisions.append({'candidate_s': candidate, 'status': 'PASS' if ok else 'FAIL',
                                    'policy': 'fixed100s_then_declared_halving_not_coarsest_passing',
                                    'failed_metrics': [r for r in relevant if r['status'] == 'FAIL'],
                                    'unresolved_informative_metrics': informative_unresolved})
        if ok:
            default = candidate
            break
    if default is None:
        dump(out / 'failure-history.json', {'attempts': histories, 'candidate_decisions': candidate_decisions})
        raise ArithmeticError('no allowed default candidate passed; contract reconciliation required')

    case_records = []
    for case in cases:
        name, p = case['id'], pmap[case['id']]
        is_core = name in core
        terminal = end if is_core else runs[(name, case['nominal_step_s'])][-1]['time_s']
        case_records.append(dict(case_id=name, role='core' if is_core else 'auxiliary', synthetic=True,
            parameter_source='fictional illustrative assumption, not fitted/measured', T_K=p['T'], p_Pa=p['p'],
            V_liquid_m3=p['V'], c_standard_mol_m3=p['cs'], R_J_mol_K=p['R'], C0_mol_m3=p['C'],
            c_A0_mol_m3=p['A0'], c_B0_mol_m3=p['B0'], K_eq=p['K'], lambda_s_inv=p['lam'],
            k_f_s_inv=p['kf'], k_r_s_inv=p['kr'], delta_rG_standard_J_mol=-p['RT'] * math.log(p['K']),
            window_end_s=terminal, nominal_h_s=default if is_core else case['nominal_step_s'],
            reference_equilibrium_fraction_B=p['K'] / (1 + p['K'])))
    write_csv(out / 'case-settings.csv', columns['case-settings.csv'], case_records)
    ledger = []
    for (name, h), rows in runs.items():
        if name in core and h not in (default, default / 2):
            continue
        for r in rows:
            reason = r['null_reason']
            if r['time_s'] == 0:
                reason = ';'.join(filter(None, (reason, 'not_applicable_initial_step')))
            ledger.append(dict(r, case_id=name, run_id=name + ':' + format(h, 'g') + 's',
                               sample_kind='native_BE_endpoint', nominal_h_s=h, synthetic=True, null_reason=reason))
    write_csv(out / 'step-ledger.csv', columns['step-ledger.csv'], ledger)
    support_defs = {'snapshots-401': snapshots, 'halfstep-union:' + format(default, 'g'): pair_union,
                    'last-three-union:' + format(order_candidate, 'g'): order_union}
    def comparison_records():
        for name in core:
            p = pmap[name]
            support_sizes = [('snapshots-401', [h['step_s'] for h in histories]),
                             ('halfstep-union:' + format(default, 'g'), [default, default / 2]),
                             ('last-three-union:' + format(order_candidate, 'g'), [order_candidate, order_candidate / 2, order_candidate / 4])]
            for support, sizes in support_sizes:
                for h in sizes:
                    rows = runs[(name, h)]; ts = [r['time_s'] for r in rows]
                    for t in support_defs[support]:
                        actual, interpolated = sample(p, rows, t, ts)
                        ref = reference(p, t)
                        for q in QUANTITIES:
                            yield dict(case_id=name, run_id=name + ':' + format(h, 'g') + 's', support_id=support,
                                       time_s=t, quantity=q, unit=units[q], synthetic=True, value=actual[q],
                                       reference_value=ref[q], signed_error=actual[q] - ref[q], candidate_interpolated=interpolated,
                                       reference_method='independent_exponential_integrated_throughput', null_reason='')
    write_csv(out / 'comparison.csv', columns['comparison.csv'], comparison_records())
    write_csv(out / 'verification.csv', columns['verification.csv'], metrics)
    # Separate module reads serialized CSVs and does not import the solver/model.
    from check_saved import check_saved
    saved = check_saved(out, phase='pre-append')
    dump(out / 'saved-table-readback.json', saved)
    for metric in saved['metrics']:
        record('B08', metric['metric'], metric['value'], norm=metric['normalizer'],
               upper=metric['threshold'], support='saved-CSV', unit=metric['unit'])
    if any(r['benchmark_id'] == 'B08' and r['status'] == 'FAIL' for r in metrics):
        raise ArithmeticError('B08 saved-table reconstruction failed')
    write_csv(out / 'verification.csv', columns['verification.csv'], metrics)
    summary = dict(packet_id='ENERGY-NUMERICS-1', status='NUMERICAL_VERIFICATION_PASS',
                   proposed_default_s=default, accepted_default_s=None, synthetic=True,
                   empirical_validation=False, learner_validation=False,
                   prospective_plan_sha256=hashlib.sha256((ROOT / 'prospective-plan.json').read_bytes()).hexdigest(),
                   execution_manifest_sha256=hashlib.sha256((ROOT / 'execution-manifest.json').read_bytes()).hexdigest(),
                   actual_attempts=histories, candidate_decisions=candidate_decisions,
                   global_and_selected_gate_failures=[],
                   supports={k: dict(count=len(v), first_s=v[0], last_s=v[-1],
                         generation='sorted union of prescribed native grids and snapshots' if k != 'snapshots-401' else 'j*80000/400 j=0..400',
                         time_array_sha256=hashlib.sha256(json.dumps(v, separators=(',', ':')).encode()).hexdigest()) for k, v in support_defs.items()},
                   run_metadata=[dict(case_id=name, run_id=name + ':' + format(h, 'g') + 's', nominal_h_s=h,
                                      steps=len(rows) - 1, window_end_s=rows[-1]['time_s'], last_actual_h_s=rows[-1]['actual_h_s'],
                                      last_actual_h_over_tau=rows[-1]['actual_h_over_tau']) for (name, h), rows in runs.items()],
                   invalid_input_evidence=invalids, saved_table_readback=saved,
                   required_carry_forwards=clarifications,
                   nulls='Equilibrium relative-amplitude/initial-energy/order metrics are UNRESOLVED with declared nonapplicability reason; informative non-equilibrium order remains compulsory.',
                   formula_readback='Reference derivative: dcB/dt=lambda*(cBeq-cB0)*exp(-lambda*t)=kf*cA-kr*cB. dXi+/dt=V*kf*cA, dXi-/dt=V*kr*cB. Gibbs curvature RTN/[x(1-x)]>0; dG_ex/dt=V*r*delta_rG<=0. BE unit column sums and convexity give delta_D_state>=actual_h*P_new>=0.',
                   limits='Numerical verification of a fictional ideal constant-volume fixed-T,p batch closure only. No ATP/growth/heat-capture/speciation/transport/tracer data or parameter fitting.100s follows a fixed policy, not coarsest-passing selection.')
    dump(out / 'verification.json', summary)
    worksheet(out, ledger, case_records[0])
    print(json.dumps({'status': summary['status'], 'proposed_default_s': default,
                      'attempts': [(v['step_s'], v['direct_run_gate_status']) for v in histories],
                      'verification_records': len(metrics), 'saved_table_status': saved['status']}))


def worksheet(out, ledger, settings):
    rows = [r for r in ledger if r['run_id'] == 'forward:' + format(settings['nominal_h_s'], 'g') + 's'][:3]
    fields = ['c_A', 'c_B', 'n_A', 'n_B', 'delta_Xi_plus', 'delta_Xi_minus', 'Xi_plus', 'Xi_minus', 'xi_net',
              'G_ex', 'delta_D_state', 'P_diss', 'endpoint_power_energy', 'dissipation_gap']
    for opened in (False, True):
        title = 'OPEN worked values' if opened else 'Blank worksheet'
        body = ['<!doctype html><html lang="en"><meta charset="utf-8"><title>' + title + '</title>',
                '<style>body{font:16px system-ui;max-width:1100px;margin:32px auto;padding:12px}table{border-collapse:collapse;width:100%}td,th{border:1px solid #aaa;padding:7px;text-align:right}th:first-child,td:first-child{text-align:left}small{display:block;margin:15px 0}</style>',
                '<h1>' + title + '</h1><p>Synthetic illustrative A ⇌ B. Two consecutive forward steps only. Verified 100 s numerical policy; all data are synthetic.</p>',
                '<p>V_liquid=' + str(settings['V_liquid_m3']) + ' m³; C0=' + str(settings['C0_mol_m3']) +
                ' mol/m³; T=' + str(settings['T_K']) + ' K; k_f=' + str(settings['k_f_s_inv']) +
                ' s⁻¹; k_r=' + str(settings['k_r_s_inv']) + ' s⁻¹; K_eq=' + str(settings['K_eq']) +
                '; R=' + str(settings['R_J_mol_K']) + ' J mol⁻¹ K⁻¹; h=' + str(settings['nominal_h_s']) + ' s.</p>',
                '<p>Use n=Vc; ΔΞ+=Vhk_f c_A,new; ΔΞ−=Vhk_r c_B,new; ξ=Ξ+−Ξ−. Independently compare n_A=n_A0−ξ and n_B=n_B0+ξ. Compute the direct initial-C G_ex, its state drop, P=−VrΔ_rG and W_end=hP_new. Read the column units and true-zero/null branches in README.</p>',
                '<table><tr><th>Existing field</th><th>Initial, t=0 s</th><th>Step1, t=' + str(rows[1]['time_s']) +
                ' s</th><th>Step2, t=' + str(rows[2]['time_s']) + ' s</th></tr>']
        for field in fields:
            values = [html.escape(str(cell(r[field]))) if opened or i == 0 or field in ('c_A', 'c_B') else '' for i, r in enumerate(rows)]
            for i, r in enumerate(rows):
                if r[field] is None:
                    values[i] = 'null (no preceding step)'
            body.append('<tr><td>' + field + '</td>' + ''.join('<td>' + v + '</td>' for v in values) + '</tr>')
        body.append('</table><small>Values use case-settings.csv and the native step-ledger.csv. Attempt the blank view before consulting the separate OPEN values. Full errors, references and candidate history are in the saved exports. Numerical verification does not establish empirical or learner validity.</small></html>')
        (out / ('OPEN-worksheet.html' if opened else 'blank-worksheet.html')).write_text('\n'.join(body) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True, help='New output directory; existing directories are never overwritten')
    execute(parser.parse_args().output.resolve())
