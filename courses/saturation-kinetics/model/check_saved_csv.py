"""Reconstruct exported arithmetic without importing/running the solver.

Run: python3 check_saved_csv.py OUTPUT_DIRECTORY
Uses Decimal and saved interval/rate/state values. No trajectory solve.
"""
import csv
from decimal import Decimal, getcontext
import hashlib
import json
from pathlib import Path
import sys

getcontext().prec = 50
D = Decimal


def check(root):
    manifest = json.loads((root / "case-manifest.json").read_text())
    v, k, capacity = (D(str(manifest[n])) for n in ("V_liquid_m3", "K_mol_m3", "qmax_mol_m3_s"))
    evidence = []
    failures = []
    files = sorted(root.glob("*-ledger.csv"))
    for path in files:
        rows = list(csv.DictReader(path.open()))
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
    assert len(files) == 8, "expected3default,3large-step,2zero ledgers"
    report = {"revision": "SAT-SAVED-CSV-READBACK-1", "method": "50-digit Decimal arithmetic over saved CSV, no solver import",
              "ledger_files": evidence, "rows_checked": sum(x["rows"] for x in evidence),
              "failures": failures, "pass": not failures,
              "scope": "update and independent interval sums, rate algebra, state/time continuity, exported balances; not an independent physical validation"}
    (root / "saved-csv-readback.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"pass": not failures, "rows_checked": report["rows_checked"], "failures": failures[:5]}))
    if failures:
        raise ArithmeticError("saved CSV reconstruction failed")


if __name__ == "__main__":
    check(Path(sys.argv[1]))
