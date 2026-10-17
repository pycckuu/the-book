---
title: "Energy constraints: data and course guide"
lang: en
---

Start with the [student packet](student-packet.md). The [OPEN answers](OPEN-worked-answers.md) and [OPEN worksheet](worksheets/OPEN-worksheet.html) are public; save a first attempt before consulting them and keep first/revised records separate. Use the [blank worksheet](worksheets/blank-worksheet.html) for only the two forward arithmetic steps. The [curriculum](curriculum.md) and [unexecuted pilot proposal](pilot-protocol.md) serve instructors.

## Verified numerical inputs

The fixed $100\,\mathrm{s}$ policy is accepted for this bounded synthetic model. The actual $400\,\mathrm{s}$ accuracy failure and $200\,\mathrm{s}$ pass are preserved; the default is not claimed to be the coarsest passing step. Read [Energy, rates, and a reversible batch](scientific-reading.md) and the [model guide](../model/README.md) for physical meaning, finite domains and verification limits. Archived manifest status fields retain their original preacceptance values; current teaching status does not rewrite them.

## Complete supplied-data route without Python

The model [saved-results.zip](../model/saved-results.zip) is the exact frozen data companion, SHA256 `bc32f1bf7ba77339c3fec2e9780e73a56219ccfa90bf4430b87dda858bc6c0df`. Download and extract it into a directory of your choice, preserving these exact members:

| Family/member | Use |
| --- | --- |
| `results-r2/case-settings.csv` | Seven declared cases, liquid/energy/rate settings and initial values. Also available [directly](data/case-settings.csv). |
| `results-r2/step-ledger.csv` | Initial row and all native endpoints, two independent gross ledgers, amounts/Gibbs/power/nulls. Large table: open the ZIP, then this member. |
| `results-r2/comparison.csv` | Same-time analytical references, 401 snapshots and labeled union supports; large table: open the ZIP, then this member. |
| `results-r2/verification.csv` | Raw norms, normalizers, exact criteria and true attempt statuses. Also available [directly](data/verification.csv). |
| `DATA-MANIFEST.json` | Exact four-family hashes, sizes, units/schema identity and row counts. A [saved-family manifest](../model/saved-results-manifest.json) is also provided. |

CSV uses UTF-8, comma separators, dot decimals and 17 significant digits; blank cells mean null where the explicit reason says so. All outputs are `synthetic=true`. No measured observations are supplied. Native ledger identity is `(case_id,run_id,time_s)` and comparison identity is `(case_id,run_id,support_id,time_s,quantity)`. Do not compare unequal times or merge case/run sums.

For E04, local HTML views use exact `forward:100s` fields at $t=0,100,200\,\mathrm{s}$. Copy the field table to spreadsheet A1:D19. Follow its helper-cell/formula instructions for columns C and D only. Stable Gibbs and power values are supplied, not an assigned nonlinear implementation. The complete table archive remains available for provenance; full arrays/extra auxiliary reconstruction are not compulsory.

## Units, supports and nulls

$c_i$ is $\mathrm{mol\,m^{-3}}$ liquid, $n_i=V_\ell c_i$ is $\mathrm{mol}$ equivalent; $r_i$ is $\mathrm{mol\,m^{-3}\,s^{-1}}$. Activities and $Q,K_{\mathrm{eq}}$ are dimensionless. $\Delta_rG$ is $\mathrm{J\,mol^{-1}}$ of written $A\to B$; $G_{\mathrm{ex}},D,\Delta D,W_{\mathrm{end}}$ and gap are $\mathrm{J}$; power is $\mathrm{W}$. All numerical Gibbs values use the direct initial-$C_0$ equilibrium form. Gibbs decrease is not heat/captured ATP.

Initial rows have no preceding interval, hence null step size/increments/drop/proxy/gap; initial cumulative gross quantities are zero. For $A>0,B=0$, $Q=0$ is valid but force/power are null. For $A=0,B>0$, quotient/force/power are null. Nonempty positive-time endpoints have finite force/power, and their first proxy uses the finite current-endpoint power. Empty has exact zero matter/Gibbs/decrease but null quotient/force/power/proxy/gap. The [unit/schema dictionary](../model/inputs/export-schema.json) lists exact reason strings. Never invent epsilon activities or treat null as numeric zero.

Core window is $[0,80000\,\mathrm{s}]$. The 401 snapshots are $t_j=200j\,\mathrm{s}$ for $j=0,\ldots,400$. Native endpoints, 1601-time candidate/half-step union and 3201-time order union remain separately labeled in the saved verification CSV and [declared benchmark plan](../model/inputs/benchmark-plan.json). Nonlinear Gibbs values are recomputed from interpolated states; the independent analytical reference is evaluated at the same time. Accuracy gates use fixed stated scales, not a nearly zero energy tail denominator.

The seven cases are forward, reverse, equilibrium, A_only, B_only, empty and partial_final_step. Boundary auxiliaries keep two full actual $100000\,\mathrm{s}$ steps ($h/\tau=10$). Partial-final control has nominal $400\,\mathrm{s}$ but actual shortened last step $133.33333333332848\,\mathrm{s}$. Auxiliaries provide domain/accounting evidence, not production accuracy or extra exercises. Gross exchange is modeled, not measured from equilibrium concentrations.

## Canonical optional Python route

Python 3 with the standard library is sufficient; this course does not require it. From `courses/energy-constraints/en/`, the frozen owner's reproduction command is: The `run.py` command requires normal Python without `-O`/`-OO` and with `PYTHONOPTIMIZE` unset; `check_saved.py` retains its existing contract.

```sh
cd ../model
python3 run.py --output fresh-results
```

Use a new output directory. Read [prospective-plan.json](../model/prospective-plan.json) and the exact [execution manifest](../model/execution-manifest.json) before any voluntary reproduction; do not alter settings/gates. The optional owner's saved-output readback command is `python3 check_saved.py fresh-results` from that model directory; its default final phase requires and reconciles all eleven self-check metrics, while the internal runner explicitly uses pre-append before adding them. Neither command was run while preparing this teaching candidate. Supplied-output analysis is distinguished from this independent execution route.

The [model guide](../model/README.md) records the repeated-zero predicate correction and execution chronology. The corrected $400\,\mathrm{s}$ accuracy FAIL, $200\,\mathrm{s}$ PASS and fixed-policy $100\,\mathrm{s}$ acceptance are not replaced by expectations. Saved numerical verification does not claim field or learner validation.
