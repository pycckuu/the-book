"""Reconstruct exported arithmetic without importing/running the solver.

Run: python3 check_saved_csv.py OUTPUT_DIRECTORY
Uses Decimal and saved interval/rate/state values. No trajectory solve.
"""
import csv
from decimal import Decimal, getcontext
import hashlib
import json
import math
from pathlib import Path
import sys

getcontext().prec = 50
D = Decimal


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("coverage: duplicate case/manifest key " + key)
        result[key] = value
    return result


def declared_ledgers(manifest):
    # Fixed accepted support is declared by adjacent portable controls, not CSV counts.
    here = Path(__file__).resolve().parent
    plan = json.loads((here / "pre-run-plan.json").read_text())
    saved = json.loads((here / "saved-results-manifest.json").read_text())
    values = plan["values"]
    k, capacity, volume = (values[n] for n in ("K_mol_m3", "qmax_mol_m3_s", "V_liquid_m3"))
    tau = k / capacity
    default = saved["default_dt_s"]
    ratios = dict(zip(("low", "transition", "high"), values["ratios_S0_over_K"]))
    if len(values["ratios_S0_over_K"]) != 3 or set(manifest["cases"]) != set(ratios):
        raise ValueError("coverage: case-manifest.json case set differs from declared low/transition/high")
    for field, expected in (("K_mol_m3", k), ("qmax_mol_m3_s", capacity),
                            ("V_liquid_m3", volume), ("tau_s", tau),
                            ("default_candidate_dt_s", default)):
        if manifest[field] != expected:
            raise ValueError("coverage: case-manifest.json " + field + " differs from declared support")
    specs = {}
    for case, ratio in ratios.items():
        s0 = k * ratio
        # These are the frozen observation-window formulae, not a trajectory solve.
        end = (s0 * (1 - 0.01) + k * math.log(1 / 0.01)) / capacity
        event_end = end + max(0.02 * end, 4000)
        info = manifest["cases"][case]
        for field, expected in (("S0_mol_m3", s0), ("S0_over_K", ratio),
                                ("trajectory_end_s", end), ("event_end_s", event_end)):
            if info[field] != expected:
                raise ValueError("coverage: case-manifest.json " + case + ":" + field + " differs from declared support")
        specs[case + "-step-ledger.csv"] = (s0, default, end, event_end)
        specs[case + "-large-step-ledger.csv"] = (s0, 10 * tau, end, event_end)
    # The zero-branch dt100/T250 contract has no event extension.
    specs["zero-substrate-ledger.csv"] = (0, 100, 250, 250)
    specs["zero-capacity-ledger.csv"] = (k, 100, 250, 250)
    return specs


def complete_history(path, rows, spec):
    s0, dt, end, event_end = spec
    if not rows:
        raise ValueError("coverage: " + path.name + " missing start/terminal intervals (empty history)")
    if D(rows[0]["S_previous_mol_m3"]) != D(str(s0)):
        raise ValueError("coverage: " + path.name + " record1 initial state differs from declared case")
    index = 0
    left = 0.0
    steps = set()
    for boundary, phase in ((end, "trajectory"), (event_end, "event_extension")):
        while left < boundary:
            right = min(left + dt, boundary)
            index += 1
            if index > len(rows):
                raise ValueError("coverage: " + path.name + " missing interval " + str(index) + " in " + phase + " to " + str(boundary))
            row = rows[index - 1]
            context = "coverage: " + path.name + " record" + str(index) + ": "
            if row["step"] in steps:
                raise ValueError(context + "duplicate step logical key " + row["step"])
            steps.add(row["step"])
            if row["step"] != str(index):
                raise ValueError(context + "step sequence differs from declared intervals")
            if row["phase"] != phase:
                raise ValueError(context + "phase differs from declared " + phase)
            for field, expected in (("t_left_s", left), ("t_right_s", right), ("dt_s", right - left)):
                value = D(row[field])
                if not value.is_finite() or value != D(str(expected)):
                    raise ValueError(context + field + " differs from declared interval " + str(expected))
            left = right
    if index != len(rows):
        raise ValueError("coverage: " + path.name + " unexpected extra/duplicate interval after declared endpoint")


def check(root):
    manifest = json.loads((root / "case-manifest.json").read_text(), object_pairs_hook=unique_object)
    specs = declared_ledgers(manifest)
    v, k, capacity = (D(str(manifest[n])) for n in ("V_liquid_m3", "K_mol_m3", "qmax_mol_m3_s"))
    evidence = []
    failures = []
    files = sorted(root.glob("*-ledger.csv"))
    actual = {path.name for path in files}
    if actual != set(specs):
        raise ValueError("coverage: ledger file set; missing=" + str(sorted(set(specs) - actual)) + "; unexpected=" + str(sorted(actual - set(specs))))
    for path in files:
        with path.open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        complete_history(path, rows, specs[path.name])
        z = D(0)
        b = D(0)
        q = D(0) if path.name.startswith("zero-capacity") else capacity
        m0 = D(rows[0]["M0_mol"])
        tol = max(D("1e-12") * m0, v * D("1e-14"))
        maximum_balance = D(0)
        max_increment_difference = D(0)
        previous_s = D(rows[0]["S_previous_mol_m3"])
        previous_t = D(0)
        for row in rows:
            value = lambda key: D(row[key])
            sn, nxt, h, qnext = (value(n) for n in ("S_previous_mol_m3", "S_next_mol_m3", "dt_s", "q_next_mol_m3_s"))
            dz = h * qnext
            db = v * dz
            z += dz
            b += db
            update_tol = max(D("1e-12") * max(sn, k), D("1e-14"))
            calculated = {
                "q_next_mol_m3_s": q * nxt / (k + nxt),
                "delta_Z_mol_m3": dz, "delta_B_mol": db,
                "Z_cumulative_mol_m3": z, "B_cumulative_mol": b,
                "M_remaining_mol": v * nxt,
                "step_balance_residual_mol": v * nxt + db - v * sn,
                "cumulative_balance_residual_mol": v * nxt + b - m0,
                "nonlinear_residual_mol_m3": nxt + dz - sn}
            if sn != previous_s or value("t_left_s") != previous_t or not D(0) <= nxt <= sn:
                failures.append([path.name, row["step"], "state/time continuity or positivity"])
            for key, expected in calculated.items():
                tolerance = tol if key.endswith("_mol") else update_tol
                if key == "q_next_mol_m3_s":
                    tolerance = max(abs(q) * D("1e-12"), D("1e-20"))
                difference = abs(expected - value(key))
                max_increment_difference = max(max_increment_difference, abs(db - value("delta_B_mol")))
                if difference > tolerance:
                    failures.append([path.name, row["step"], key, str(difference), str(tolerance)])
            step_balance = abs(v * nxt + db - v * sn)
            cumulative_balance = abs(v * nxt + b - m0)
            maximum_balance = max(maximum_balance, step_balance, cumulative_balance)
            if max(step_balance, cumulative_balance) > tol or abs(nxt + dz - sn) > update_tol:
                failures.append([path.name, row["step"], "reconstructed balance/update"])
            if abs(value("t_right_s") - value("t_left_s") - h) > D("1e-9"):
                failures.append([path.name, row["step"], "interval width"])
            previous_s, previous_t = nxt, value("t_right_s")
        evidence.append({"file": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                         "rows": len(rows), "recomputed_B_final_mol": str(b),
                         "final_remaining_mol": str(v * previous_s),
                         "max_balance_residual_mol": str(maximum_balance),
                         "amount_tolerance_mol": str(tol),
                         "max_increment_export_difference_mol": str(max_increment_difference)})
    report = {"revision": "SAT-SAVED-CSV-READBACK-1", "method": "50-digit Decimal arithmetic over saved CSV, no solver import",
              "ledger_files": evidence, "rows_checked": sum(x["rows"] for x in evidence),
              "failures": failures, "pass": not failures,
              "scope": "update and independent interval sums, rate algebra, state/time continuity, exported balances; complete declared ledger filenames, phases and native intervals; not an independent physical validation"}
    (root / "saved-csv-readback.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"pass": not failures, "rows_checked": report["rows_checked"], "failures": failures[:5]}))
    if failures:
        raise ArithmeticError("saved CSV reconstruction failed")


if __name__ == "__main__":
    check(Path(sys.argv[1]))
