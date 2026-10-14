# Reversible batch and Gibbs availability

This synthetic ideal A ⇌ B batch uses a verified 100 s default under a fixed policy. The actual 400 s run failed accuracy checks; 200 s passed. The selected default is not claimed to be the coarsest passing step. Numerical verification does not establish natural kinetics, biological energy capture or learner outcomes.

Python 3 and its standard library are sufficient. From this directory, write to a fresh output directory:

```sh
python3 run.py --output new-results
python3 check_saved.py new-results
```

The runner checks its source/input pins, evaluates seven cases and eight benchmark groups, and retains the actual coarse/refined outcomes. The second command reconstructs saved arithmetic, independent exponential/integrated references, geometric backward-Euler values and common-support metrics without importing the solver. Existing output directories are rejected. No older course model runs as part of these commands.

The saved-data checker requires the complete declared case/run/quantity groups and physical-time supports, including the final native intervals. Expected coverage comes from the accompanying settings/schema and bounded refinement policy; a CSV cannot define away its own missing rows. It rejects nonfinite numbers and forbidden blanks with a file, row key and field diagnostic. True boundary/empty nulls and equilibrium nonapplicability remain distinct from numerical zero. The check also accepts the runner's intermediate verification table before its own saved-CSV metrics are appended; a partially appended group is rejected.

For the separate CSV-only corruption regression, use a new directory:

```sh
python3 test_check_saved.py --archive saved-results.zip --out checker-regression
```

This uses disposable copies of the unchanged accepted 100 s archive and records complete/negative controls and CLI exit statuses. It runs no solver and establishes no empirical or learner validity. Original numerical CSV identities and execution provenance remain separate from later checker revisions.

The [execution manifest](execution-manifest.json) pins the current code and input presentation copies for the reproduction command. [Provenance](presentation-only-input-mapping.json) retains the original executed checker and original owner manifest, as well as the prior portable manifest. The hardened checker did not exist at the original solve; changing these current pins does not regenerate or validate the saved numerical data.

The declared final 3.125 s fallback remains an unexecuted compatibility limitation: if every preceding candidate fails, the unchanged runner can repeat the 6.25 s verification IDs. The hardened checker then rejects duplicates. The accepted fixed-input fixture selects 100 s and does not reach that branch. This candidate does not fix the fallback.

## Saved data and spreadsheet route

Extract [saved-results.zip](saved-results.zip) with an ordinary archive manager to obtain `results-r2/`. Its four CSV families are pinned in [saved-results-manifest.json](saved-results-manifest.json):

- `case-settings.csv`: seven synthetic input sets, units and derived constants.
- `step-ledger.csv`: both evolved inventories and independently accumulated forward/reverse increments; 7425 rows.
- `comparison.csv`: paired analytical references on the same physical times, labeled state interpolation and refinement support; 266580 rows.
- `verification.csv`: raw metrics, normalizers, criteria, genuine failures and explicit unavailable values.

Open these files in a spreadsheet using comma separators and dot decimals. The two consecutive forward steps have a [blank worksheet](results/blank-worksheet.html) and separate [OPEN worked values](results/OPEN-worksheet.html). Attempt the blank view first. The complete numerical tables stay in the archive so the source diff focuses on the model.

For each native endpoint, derive each gross increment as `V_liquid * actual_h * k * current_concentration`. Accumulate the forward and reverse columns separately, take their signed difference, and compare against both inventories. Use the actual shortened step at the final partial endpoint. Interpolated snapshots are not extra budget increments.

## Physical meaning and finite domains

The model is closed to matter, well mixed and held at fixed temperature and pressure by reservoirs. Constant liquid volume is a dilute incompressible-solvent approximation. Concentrations use mol/m3 of modeled liquid; inventories and throughputs use mol of convertible equivalents. This accounting does not prove unspecified elemental, charge or electron balances.

Activities are dimensionless. Reaction Gibbs energy is chemical and unprimed, in J/mol of the written A → B reaction. The common standard concentration cancels in this equal-stoichiometry reaction quotient. Equilibrium ratios constrain `K_eq` under this closure; equilibrium concentrations alone do not identify the relaxation rate or gross exchange. Measuring exchange would require independent tracer or exchange observations.

`G_ex` uses the direct compensated two-species expression and equilibrium concentrations derived once from the initial total. It is Gibbs availability in J, not a heat inventory. The unforced batch extracts no work or ATP. The binary Gibbs expression is a reference check at exactly conserved analytical states, not a replacement based on a drifting numerical total.

The two state updates and gross increments are independent. Signed net extent can be negative; gross throughput remains nonnegative. Balanced exchange at equilibrium provides no net available work.

At a true zero activity, logarithmic force and power are blank with an explicit reason. With B=0 and A>0, `Q=0` remains valid while its logarithm is nonfinite. With A=0, the ratio is undefined. Empty batches retain exact-zero inventories/Gibbs energy and undefined ratio, force and power. No epsilon, clipping or mass repair is used. The finite boundary Gibbs limit does not define a finite initial power.

The first endpoint-power proxy uses `actual_h * current_positive_time_power`, never the preceding null boundary power. The Gibbs state drop is at least this endpoint proxy in exact arithmetic; their gap is a numerical diagnostic. Telescoping state drops do not independently demonstrate energy accuracy or a calorimetric heat balance.

The core window is 0 to 80000 s, with 401 common snapshots, candidate/half-step endpoint unions and a fixed last-three union. Nonlinear Gibbs energy is recomputed from interpolated states. Energy-tail errors use the stated absolute scales, without a relative guarantee as availability vanishes. Boundary auxiliary runs have two full 10-tau steps; their positivity/accounting checks do not assert production accuracy. The partial-final-step case retains its actual 133.33333333332848 s last interval.

The original first execution rejected valid boundary starts because a positive-time predicate also included a repeated zero-time snapshot. That predicate was corrected; equations, cases, supports and tolerances were unchanged. The genuine failed history is preserved separately. The portable copy removes coordination metadata; re-execution changes provenance hashes and status labels while preserving numerical tables, criteria and outcomes.

This companion does not implement growth, maintenance, ATP coupling, species speciation, empirical fitting or transport. Scientific readings, teaching packets and Russian delivery are separate module components.
