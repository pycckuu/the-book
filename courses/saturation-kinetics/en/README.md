# Saturation kinetics: English file guide

Read [Saturation without growth](scientific-reading.md), then the [student packet](student-packet.md). Consult the separate [OPEN worked answers](OPEN-worked-answers.md) after your first attempt. [Curriculum](curriculum.md), [outcome map](exercise-outcome-map.json) and the unexecuted [pilot protocol](pilot-protocol.md) describe the five tasks, 100 points and 210 planned minutes, plus an optional 15-minute refresher. These are planned, not measured, learning outcomes.

## Supplied files

The [model README](../model/README.md) and [saved-results ZIP](../model/saved-results.zip) accompany every course delivery. Extract the ZIP into a new empty folder. It has a `results/` prefix: case metadata is `results/case-manifest.json`, low/high snapshots are `results/low-snapshots.csv` and `results/high-snapshots.csv`, and complete update ledgers are `results/low-step-ledger.csv` and `results/high-step-ledger.csv`. Links to those archive-only inputs open the ZIP; they do not open loose CSV files. Snapshot tables contain 401 fixed times per case. Transition and auxiliary tables support owner verification; they add no learner tasks.

Direct compact files are [rate curve](../model/results/rate-curve.csv), [thresholds](../model/results/thresholds.csv) and [time refinement](../model/results/time-refinement.csv). Local [blank worksheet](worksheets/blank-step-worksheet.csv) and [OPEN worked values](worksheets/OPEN-worked-step-values.csv) preserve the supplied bytes. Only the low case steps 1 and 2 are compulsory worksheet rows. Read [book dependencies](DEPENDENCIES.md) for the contextual passages. All model data are synthetic.

## Supplied-output spreadsheet route

Import comma-delimited UTF-8 CSV, retaining headers and numeric precision. Blank cells mean null/undefined/unavailable as described by the owner, never zero. The low worksheet's first two data rows contain $S_n$, $S_{n+1}$, $q_{n+1}$ and actual $h$; reconstruct

$$
\Delta Z=hq_{n+1},\quad \Delta B=V_\ell\Delta Z,\quad
B_n=\sum_{i=1}^n\Delta B_i,\quad M_n=V_\ell S_n.
$$

Keep $V_\ell=0.001\,\mathrm{m^3}$. In this owner worksheet, set cell `T1` to `0.001`. For row 2, use `J2=F2*I2`, `K2=SUM($J$2:J2)`, `L2=$T$1*H2`, `M2=$T$1*J2`, `N2=SUM($M$2:M2)`, `P2=L2+M2-$T$1*G2`, `Q2=L2+N2-O2`, `R2=H2+J2-G2`. Copy only into row 3 for the second assigned low step. These column letters apply to the local **blank worksheet with a case column**, not the complete ledger's different layout. The model README supplies a different full-ledger helper layout. Do not mix the two layouts.

Do not copy cumulative `SUM` formulas across the worksheet's later nonconsecutive rows/case changes. Those cumulative values require all intervening increments from the corresponding complete ledger, not a sum of selected rows. For the full low ledger, use the owner's documented helper columns in its [unchanged README](../model/README.md). Snapshot interpolation adds no budget steps. Report analysed supplied outputs.

## Canonical Python route

From `courses/saturation-kinetics/en/`:

```sh
cd ../model
python3 saturation.py new-results
```

Use a fresh empty output directory. Python standard library only; `saturation.py` requires its unchanged adjacent `pre-run-plan.json`. Optional `python3 check_saved_csv.py new-results` reconstructs exported arithmetic without importing/running the solver. Running all owner cases does not add transition/auxiliary learner tasks. The teaching readings use the supplied verified outputs.
