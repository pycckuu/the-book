"""Constant-capacity synthetic batch. Python standard library only.

Run: python3 saturation.py OUTPUT_DIRECTORY
OUTPUT_DIRECTORY must be empty. This generates verification and CSV exports.
Reference bisection and production quadratic are separate calculations.
"""
import bisect
import csv
import hashlib
import json
import math
from pathlib import Path
import sys

K = 0.1
Q = 1e-5
V = 1e-3
TAU = K / Q
RATIOS = {"low": 0.01, "transition": 1.0, "high": 100.0}
FRACTIONS = (0.5, 0.1, 0.01)


def validate(s, k, q, v, dt):
    if not all(math.isfinite(x) for x in (s, k, q, v, dt)):
        raise ValueError("nonfinite input")
    if not (1e-6 <= k <= 10 and 1e-6 <= v <= 1 and dt > 0):
        raise ValueError("K, volume or step outside declared support")
    if not (0 <= s / k <= 100 and (q == 0 or 1e-10 <= q <= 1e-2)):
        raise ValueError("substrate or capacity outside declared support")


def rate(s, k=K, q=Q):
    return q * (s / (k + s))


def step(s, dt, k=K, q=Q):
    if s == 0 or q == 0:
        return s
    # Scale by K, then use the cancellation-safe positive-root branch.
    x = s / k
    b = 1 + dt * q / k - x
    root = math.hypot(b, 2 * math.sqrt(x))
    result = k * ((root - b) / 2 if b < 0 else 2 * x / (root + b))
    if not math.isfinite(result):
        raise ArithmeticError("nonfinite update")
    return result


def threshold(s0, f, k=K, q=Q):
    return (s0 * (1 - f) + k * math.log(1 / f)) / q


def reference(s0, t, k=K, q=Q):
    if t == 0 or q == 0 or s0 == 0:
        return s0, 0.0, 0.0, 0, 0.0, 0.0
    lo, hi = -q * t / k, 0.0
    scale = max(s0, k)
    for iteration in range(1, 201):
        y = (lo + hi) / 2
        g = s0 * math.expm1(y) + k * y + q * t
        if g <= 0:
            lo = y
        else:
            hi = y
        y = (lo + hi) / 2
        residual = abs(s0 * math.expm1(y) + k * y + q * t) / scale
        if hi - lo <= 1e-12 and residual <= 1e-12:
            s = s0 * math.exp(y)
            if s == 0 or not math.isfinite(s):
                raise ArithmeticError("reference underflow/nonfinite")
            return s, residual, hi - lo, iteration, lo, hi
    raise ArithmeticError("reference bracket/residual unresolved")


def simulate(s0, dt, end, event_end, k=K, q=Q, v=V):
    validate(s0, k, q, v, dt)
    t, s, z, total_b = 0.0, s0, 0.0, 0.0
    rows = []
    times, states, zs = [0.0], [s0], [0.0]
    for boundary, phase in ((end, "trajectory"), (event_end, "event_extension")):
        while t < boundary:
            right = min(t + dt, boundary)
            h = right - t
            if h <= 0:
                raise ArithmeticError("time cannot advance")
            nxt = step(s, h, k, q)
            qnext = rate(nxt, k, q)
            dz = h * qnext
            db = v * dz
            z += dz
            total_b += db
            nonlinear = nxt + dz - s
            rows.append({
                "step": len(rows) + 1, "phase": phase,
                "t_left_s": t, "t_right_s": right, "dt_s": h,
                "S_previous_mol_m3": s, "S_next_mol_m3": nxt,
                "q_next_mol_m3_s": qnext, "delta_Z_mol_m3": dz,
                "Z_cumulative_mol_m3": z, "M_remaining_mol": v * nxt,
                "delta_B_mol": db, "B_cumulative_mol": total_b,
                "M0_mol": v * s0,
                "step_balance_residual_mol": v * nxt + db - v * s,
                "cumulative_balance_residual_mol": v * nxt + total_b - v * s0,
                "nonlinear_residual_mol_m3": nonlinear})
            t, s = right, nxt
            times.append(t)
            states.append(s)
            zs.append(z)
    return {"rows": rows, "t": times, "s": states, "z": zs}


def interpolate(run, t, key="s"):
    if t < run["t"][0] or t > run["t"][-1]:
        raise ValueError("no extrapolation")
    i = bisect.bisect_right(run["t"], t) - 1
    if run["t"][i] == t:
        return run[key][i]
    a = (t - run["t"][i]) / (run["t"][i + 1] - run["t"][i])
    return run[key][i] + a * (run[key][i + 1] - run[key][i])


def events(run, s0, end, event_end):
    result = []
    for f in FRACTIONS:
        row = {"fraction_remaining": f, "t_analytic_s": threshold(s0, f),
               "trajectory_window_end_s": end, "event_extension_end_s": event_end}
        for i in range(1, len(run["t"])):
            if run["s"][i] <= f * s0 <= run["s"][i - 1]:
                a = (run["s"][i - 1] - f * s0) / (run["s"][i - 1] - run["s"][i])
                tn = run["t"][i - 1] + a * (run["t"][i] - run["t"][i - 1])
                row.update(t_numerical_s_or_null=tn, bracket_left_s=run["t"][i - 1],
                           bracket_right_s=run["t"][i], event_status="reached",
                           relative_time_error_or_null=abs(tn - row["t_analytic_s"]) / row["t_analytic_s"])
                break
        else:
            row.update(t_numerical_s_or_null=None, bracket_left_s=None, bracket_right_s=None,
                       event_status="censored", relative_time_error_or_null=None)
        result.append(row)
    return result


def health(run, s0, k=K, v=V):
    amount_tol = max(1e-12 * v * s0, v * 1e-14)
    nonlinear_ratios = [abs(r["nonlinear_residual_mol_m3"]) /
                        max(1e-12 * max(r["S_previous_mol_m3"], k), 1e-14) for r in run["rows"]]
    step_error = max(abs(r["step_balance_residual_mol"]) for r in run["rows"])
    cumulative_error = max(abs(r["cumulative_balance_residual_mol"]) for r in run["rows"])
    increases = [b - a for a, b in zip(run["s"], run["s"][1:])]
    result = {"minimum_S_mol_m3": min(run["s"]),
              "negative_count": sum(s < 0 for s in run["s"]),
              "above_initial_count": sum(s > s0 for s in run["s"]),
              "positive_increase_count": sum(x > 0 for x in increases),
              "largest_signed_increase_mol_m3": max(increases),
              "max_step_balance_residual_mol": step_error,
              "max_cumulative_balance_residual_mol": cumulative_error,
              "amount_tolerance_mol": amount_tol,
              "max_update_residual_over_tolerance": max(nonlinear_ratios),
              "steps": len(run["rows"])}
    result["positive_monotone_pass"] = not any((result["negative_count"], result["above_initial_count"], result["positive_increase_count"]))
    result["accounting_pass"] = max(step_error, cumulative_error) <= amount_tol
    result["update_pass"] = max(nonlinear_ratios) <= 1
    return result


def write_csv(path, rows):
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2, allow_nan=False) + "\n")


def main(out):
    if not __debug__:
        raise RuntimeError("Verification requires normal Python; remove -O/-OO and unset PYTHONOPTIMIZE.")
    out.mkdir(parents=True, exist_ok=True)
    if any(out.iterdir()):
        raise ValueError("output directory must be empty")
    plan = json.loads(Path(__file__).with_name("pre-run-plan.json").read_text())
    assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest() == plan["code_sha256"]
    metrics, runs, refs, case_info = {}, {}, {}, {}
    reference_summary = {"max_normalized_residual": 0, "max_log_bracket_width": 0,
                         "max_iterations": 0, "calls": 0, "failures": 0}

    def exact(case, t):
        key = (case, t)
        if key not in refs:
            result = reference(case_info[case]["S0_mol_m3"], t)
            refs[key] = result
            reference_summary["max_normalized_residual"] = max(reference_summary["max_normalized_residual"], result[1])
            reference_summary["max_log_bracket_width"] = max(reference_summary["max_log_bracket_width"], result[2])
            reference_summary["max_iterations"] = max(reference_summary["max_iterations"], result[3])
            reference_summary["calls"] += 1
        return refs[key][0]

    for case, ratio in RATIOS.items():
        s0 = K * ratio
        end = threshold(s0, 0.01)
        event_end = end + max(0.02 * end, 4000)
        case_info[case] = {"S0_mol_m3": s0, "S0_over_K": ratio,
                           "trajectory_end_s": end, "event_end_s": event_end}

    def evaluate(case, dt):
        if (case, dt) in metrics:
            return
        info = case_info[case]
        s0, end = info["S0_mol_m3"], info["trajectory_end_s"]
        run = simulate(s0, dt, end, info["event_end_s"])
        runs[case, dt] = run
        snap = [end * i / 400 for i in range(401)]
        endpoints = [t for t in run["t"] if t <= end]
        def error(t):
            return abs(interpolate(run, t) - exact(case, t))
        esnap = max(error(t) for t in snap)
        eend = max(error(t) for t in endpoints)
        support = set(endpoints + snap)
        relative = [error(t) / exact(case, t) for t in support if exact(case, t) >= 0.01 * s0]
        bound_violation = 0.0
        for t in support:
            lower = max(s0 - Q * t, s0 * math.exp(-Q * t / K))
            upper = s0 * math.exp(-Q * t / (K + s0))
            bound_violation = max(bound_violation, lower - exact(case, t), exact(case, t) - upper)
        evt = events(run, s0, end, info["event_end_s"])
        event_pass = all(e["event_status"] == "reached" and e["relative_time_error_or_null"] <= 0.01 for e in evt)
        row = dict(case=case, dt_s=dt, dt_over_tau=dt / TAU,
                   max_endpoint_error_over_S0=eend / s0,
                   max_snapshot_error_over_S0=esnap / s0,
                   max_pointwise_relative_error_above_1_percent_remaining=max(relative),
                   max_bound_violation_mol_m3=bound_violation,
                   bounds_pass=bound_violation <= 1e-12 * max(s0, K),
                   trajectory_pass=max(esnap, eend) <= 0.005 * s0,
                   event_pass=event_pass, events=evt, **health(run, s0))
        metrics[case, dt] = row

    series = [400.0, 200.0, 100.0, 50.0, 25.0]
    for dt in series:
        for case in RATIOS:
            evaluate(case, dt)

    def refinement(case, dt):
        evaluate(case, dt / 2)
        a, b = runs[case, dt], runs[case, dt / 2]
        end = case_info[case]["trajectory_end_s"]
        s0 = case_info[case]["S0_mol_m3"]
        support = sorted(set([end * i / 400 for i in range(401)] +
                             [t for t in a["t"] if t <= end] + [t for t in b["t"] if t <= end]))
        diff = max(abs(interpolate(a, t) - interpolate(b, t)) for t in support) / s0
        event_diff = []
        for x, y in zip(metrics[case, dt]["events"], metrics[case, dt / 2]["events"]):
            event_diff.append(None if x["event_status"] != "reached" or y["event_status"] != "reached"
                              else abs(x["t_numerical_s_or_null"] - y["t_numerical_s_or_null"]) / x["t_analytic_s"])
        metrics[case, dt].update(candidate_to_halfstep_max_difference_over_S0=diff,
                                candidate_to_halfstep_support_count=len(support),
                                threshold_halfstep_differences=event_diff,
                                refinement_pass=diff <= 0.0025 and all(x is not None and x <= 0.005 for x in event_diff))

    for dt in series[:-1]:
        for case in RATIOS:
            refinement(case, dt)

    def orders():
        for case in RATIOS:
            ordered = sorted((h for c, h in metrics if c == case), reverse=True)
            for previous, h in zip(ordered, ordered[1:]):
                a, b = metrics[case, previous], metrics[case, h]
                if previous != 2 * h:
                    continue
                ea, eb = a["max_snapshot_error_over_S0"], b["max_snapshot_error_over_S0"]
                b["observed_order_fixed_snapshots"] = math.log(ea / eb, 2) if ea > 1e-10 and eb > 1e-10 else None
            last = [metrics[case, h].get("observed_order_fixed_snapshots") for h in ordered[-2:]]
            case_info[case]["last_two_orders"] = last
            case_info[case]["order_pass"] = all(p is not None and 0.8 <= p <= 1.2 for p in last)

    history = []
    candidate = 100.0
    for attempt in range(10):
        for case in RATIOS:
            evaluate(case, candidate)
            refinement(case, candidate)
        orders()
        failures = []
        for case in RATIOS:
            r = metrics[case, candidate]
            for gate in ("trajectory_pass", "event_pass", "positive_monotone_pass", "accounting_pass", "update_pass", "bounds_pass", "refinement_pass"):
                if not r[gate]:
                    failures.append(case + ":" + gate)
            if not case_info[case]["order_pass"]:
                failures.append(case + ":order_pass")
        history.append({"candidate_dt_s": candidate, "pass": not failures, "failures": failures})
        if not failures:
            break
        candidate /= 2
    else:
        raise ArithmeticError("default unresolved after 10 halvings")

    auxiliary = []
    for case in RATIOS:
        info = case_info[case]
        run = simulate(info["S0_mol_m3"], 10 * TAU, info["trajectory_end_s"], info["event_end_s"])
        auxiliary.append({"case": case, "dt_over_tau": 10, "accuracy_claim": False,
                          **health(run, info["S0_mol_m3"])})
        write_csv(out / (case + "-large-step-ledger.csv"), run["rows"])
    for name, s0, q in (("zero-substrate", 0.0, Q), ("zero-capacity", K, 0.0)):
        run = simulate(s0, 100, 250, 250, q=q)
        auxiliary.append({"case": name, "state_identity_pass": all(s == s0 for s in run["s"]),
                          "zero_increment_pass": all(r["delta_B_mol"] == 0 for r in run["rows"]),
                          "fractional_event": None, "event_reason": name,
                          **health(run, s0)})
        write_csv(out / (name + "-ledger.csv"), run["rows"])
    invalid = []
    good = [K, K, Q, V, 100]
    for index, bad in ((0, -1), (0, 101 * K), (1, 0), (1, -1), (1, 1e-7), (2, -1),
                       (2, 1e-11), (3, 0), (3, 2), (4, 0), (4, -1)):
        args = good.copy()
        args[index] = bad
        try:
            validate(*args)
        except ValueError:
            invalid.append({"parameter_index": index, "value": bad, "rejected": True})
        else:
            invalid.append({"parameter_index": index, "value": bad, "rejected": False})
    for index in range(5):
        for label, bad in (("NaN", float("nan")), ("infinity", float("inf"))):
            args = good.copy()
            args[index] = bad
            try:
                validate(*args)
            except ValueError:
                invalid.append({"parameter_index": index, "value": label, "rejected": True})
            else:
                invalid.append({"parameter_index": index, "value": label, "rejected": False})

    thresholds, worked = [], []
    for case in RATIOS:
        info = case_info[case]
        run = runs[case, candidate]
        write_csv(out / (case + "-step-ledger.csv"), run["rows"])
        snapshots = []
        for i in range(401):
            t = info["trajectory_end_s"] * i / 400
            sn, sr = interpolate(run, t), exact(case, t)
            z = interpolate(run, t, "z")
            root = refs[case, t]
            snapshots.append(dict(time_s=t, support="piecewise-linear-step-state",
                                  S_numerical_mol_m3=sn, S_reference_mol_m3=sr,
                                  rate_at_snapshot_mol_m3_s=rate(sn), Z_interpolated_mol_m3=z,
                                  absolute_S_error_mol_m3=abs(sn - sr), relative_S_error=abs(sn - sr) / sr,
                                  error_scale_S0_mol_m3=info["S0_mol_m3"],
                                  M_remaining_mol=V * sn, B_depleted_equivalents_mol=V * z,
                                  reference_normalized_residual=root[1], reference_log_bracket_width=root[2],
                                  reference_iterations=root[3], reference_log_bracket_left=root[4],
                                  reference_log_bracket_right=root[5]))
        write_csv(out / (case + "-snapshots.csv"), snapshots)
        thresholds += [dict(case=case, **r) for r in metrics[case, candidate]["events"]]
        for row in (run["rows"][0], run["rows"][1], next(r for r in run["rows"] if r["t_right_s"] == info["trajectory_end_s"]), run["rows"][-1]):
            worked.append(dict(case=case, **row))
    write_csv(out / "thresholds.csv", thresholds)
    write_csv(out / "OPEN-worked-step-values.csv", worked)
    blanks = [{key: (value if key in ("case", "step", "phase", "t_left_s", "t_right_s", "dt_s", "S_previous_mol_m3", "S_next_mol_m3", "q_next_mol_m3_s", "M0_mol") else None)
               for key, value in row.items()} for row in worked]
    write_csv(out / "blank-step-worksheet.csv", blanks)
    curve = []
    for ratio in (0, 0.01, 0.05, 0.1, 0.5, 1, 2, 10, 20, 100):
        s = K * ratio
        qr = rate(s)
        curve.append(dict(S_mol_m3=s, S_over_K=ratio, q_saturation_mol_m3_s=qr,
                          q_over_qmax=qr / Q, q_linear_mol_m3_s=Q * ratio, q_zero_order_mol_m3_s=Q,
                          linear_relative_rate_excess_or_null=None if s == 0 else ratio,
                          zero_order_relative_rate_excess_or_null=None if s == 0 else 1 / ratio,
                          amount_rate_mol_s=V * qr))
    write_csv(out / "rate-curve.csv", curve)
    rows = []
    for (case, h), row in sorted(metrics.items(), key=lambda x: (x[0][0], -x[0][1])):
        flat = {k: v for k, v in row.items() if k not in ("events", "threshold_halfstep_differences")}
        for i, f in enumerate(FRACTIONS):
            flat["fraction_" + str(f) + "_time_relative_error"] = row["events"][i]["relative_time_error_or_null"]
            flat["fraction_" + str(f) + "_halfstep_time_relative_difference"] = row.get("threshold_halfstep_differences", [None] * 3)[i]
        rows.append(flat)
    all_fields = list(dict.fromkeys(k for r in rows for k in r))
    write_csv(out / "time-refinement.csv", [{k: r.get(k) for k in all_fields} for r in rows])
    rate_checks = rate(0) == 0 and rate(K) == Q / 2
    for r in curve[1:]:
        qr = r["q_saturation_mol_m3_s"]
        rate_checks &= math.isclose(r["q_linear_mol_m3_s"] / qr - 1, r["S_over_K"], rel_tol=1e-12, abs_tol=1e-12)
        rate_checks &= math.isclose(Q / qr - 1, 1 / r["S_over_K"], rel_tol=1e-12, abs_tol=1e-12)
    selected = [metrics[case, candidate] for case in RATIOS]
    partial_pass = all(any(r["dt_s"] < candidate for r in runs[case, candidate]["rows"]) for case in RATIOS)
    gates = {
        "SAT-B01": {"pass": rate_checks, "evidence": "rate-curve.csv; units/limits are also analytical contract checks"},
        "SAT-B02": {"pass": all(r["trajectory_pass"] for r in selected), "evidence": "independent log-root endpoint and401 snapshot maxima"},
        "SAT-B03": {"pass": all(r["event_pass"] for r in selected), "evidence": "thresholds.csv; positive K has no finite exact zero by analytical contract"},
        "SAT-B04": {"pass": all(r["accounting_pass"] and r["update_pass"] for r in selected + auxiliary), "evidence": "independently accumulated BE increments including auxiliary rows; separate saved-CSV reconstruction required"},
        "SAT-B05": {"pass": all(r["refinement_pass"] for r in selected) and all(x["order_pass"] for x in case_info.values()), "evidence": "time-refinement.csv; common union support and fixed-snapshot order"},
        "SAT-B06": {"pass": all(r["positive_monotone_pass"] for r in selected + auxiliary), "evidence": "actual minima/counts, no clipping; auxiliary dt/tau10 for all3 cases"},
        "SAT-B07": {"pass": rate_checks and all(r["bounds_pass"] for r in selected), "evidence": "rate excesses and independent-reference trajectory bounds"},
        "SAT-B08": {"pass": partial_pass and all(r["rejected"] for r in invalid) and all(r.get("state_identity_pass", True) and r.get("zero_increment_pass", True) for r in auxiliary), "evidence": "zero/invalid branches and exact partial-step windows"}}
    info = {"revision": "SAT-NUMERICS-1", "synthetic": True, "K_mol_m3": K, "qmax_mol_m3_s": Q,
            "V_liquid_m3": V, "tau_s": TAU, "default_candidate_dt_s": candidate,
            "default_status": "OWNER_VERIFIED_PENDING_EDITOR_ACCEPTANCE", "cases": case_info,
            "volume_basis": "modeled liquid", "amount_basis": "substrate equivalents, not products or biomass",
            "code_sha256": plan["code_sha256"], "plan_sha256": hashlib.sha256(Path(__file__).with_name("pre-run-plan.json").read_bytes()).hexdigest(),
            "reference": "independent log-root bisection", "snapshot_support": "401 uniform times, linear interpolation of BE states",
            "halfstep_support": "union of both endpoint grids plus401 snapshots inside trajectory window only",
            "input_range": plan["input_range"], "optional_static_comparison": "omitted by Editor Q03"}
    dump(out / "case-manifest.json", info)
    dump(out / "verification.json", {"revision": "SAT-NUMERICS-1", "gates": gates,
                                     "all_owner_gates_pass": all(r["pass"] for r in gates.values()),
                                     "reference": reference_summary, "selected_case_metrics": selected,
                                     "default_attempt_history": history, "all_run_metrics": list(metrics.values()),
                                     "auxiliary": auxiliary, "invalid_inputs": invalid,
                                     "final_partial_steps_pass": partial_pass,
                                     "clipping": False, "numerical_failures_retained": True,
                                     "empirical_validation": False, "Editor_acceptance": False})
    if not all(r["pass"] for r in gates.values()):
        raise ArithmeticError("one or more owner gates failed")
    print(json.dumps({"default_dt_s": candidate, "owner_gates_pass": True, "default_attempts": history,
                      "files": len(list(out.iterdir()))}))


if __name__ == "__main__":
    main(Path(sys.argv[1]))
