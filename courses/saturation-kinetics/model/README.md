# Saturation kinetics numerical packet

All model data are synthetic. The verified default is 100 s for this constant-capacity depletion equation. Python standard library only, no install step. Numerical verification does not establish enzyme-mechanism accuracy, microbial growth or field validity.

The compact [saved-results.zip](saved-results.zip) companion contains all 19 exact output files, including complete interval ledgers, snapshots, verification metrics and failed coarse controls. Extract it in this directory to create `results/`. The five small worksheets and summary CSVs are also available directly in [results/](results/). Large generated tables are kept in the ZIP so source review stays focused on the algorithm.

From this directory, generate outputs in a new empty directory:

```sh
python3 saturation.py new-results
python3 check_saved_csv.py new-results
```

The first command executes the bounded model and SAT-B01 through SAT-B08 checks. The second reads saved exports and independently recomputes interval arithmetic. It does not run/import the solver. Existing nonempty output directories are rejected. The portable pre-run plan preserves the original inputs and criteria while replacing private path labels with stable evidence labels. The saved manifest records the original plan hash; re-execution updates only that manifest field, with all numerical outputs unchanged. Numerical/default results and raw failed coarse controls are preserved in results/. The portable execution reproduces all numerical exports; only the manifest plan hash reflects the portable metadata copy.

The saved-data checker requires the declared low/transition/high default and large-step ledgers plus both zero-branch ledgers. It verifies each start, native interval, step key, trajectory boundary and event-extension boundary against the adjacent fixed-input plan and accepted-default declaration. All actual partial intervals remain valid. A truncated prefix cannot represent a complete saved history. This checks the eight ledgers, not every snapshot, threshold or verification result.

The [checker provenance](checker-provenance.json) distinguishes the current checker from the checker used during the original solve. The current portable plan pins the hardened checker; its timestamp and original pre-run identity remain historical. The original solver identity, numerical controls and archived results remain historical and unchanged. The archive's embedded plan/report identities are not replaced by the current metadata. The current `saturation.py` and matched `pre-run-plan.json` add an optimized-verification refusal; the executed source and original plan identities remain historical. Use normal Python without `-O`/`-OO` and with `PYTHONOPTIMIZE` unset. To run the saved-data controls without solving, use a fresh directory:

```sh
python3 test_check_saved_csv.py --archive saved-results.zip --out new-csv-controls
```

## Files and observation support

- case-manifest.json: units, inputs, fixed physical windows, volume basis and proposed default.
- low/transition/high-step-ledger.csv: all actual update intervals, including separately labeled event extension, full-precision numeric exports.
- low/transition/high-snapshots.csv: 401 fixed physical times per trajectory, numerical states and independent reference, reference brackets and errors. Numerical state and cumulative Z are linearly interpolated from step endpoints. Instantaneous snapshot rate is not a budget increment.
- thresholds.csv: analytical and numerical threshold times, first enclosing endpoint bracket, declared trajectory/event windows. Blank numeric cells mean null, never zero. A nonreached event is censored.
- rate-curve.csv: one saturation law, limiting rate comparisons and amount-rate conversion. Relative rate errors at zero substrate are undefined/blank.
- time-refinement.csv: separate endpoint/snapshot errors, order, common-support half-step comparisons, threshold metrics and actual gates for every step size. Blank half-step/order entries mean unavailable for the edge of the series, not a measured pass.
- verification.json: individual benchmarks, minima/counts, reference maxima, all actual coarse failures, default attempt and auxiliary checks.
- large-step and zero ledgers: bounded owner checks. The nominal large step is shortened by fixed boundaries, as documented in auxiliary-interval-readback.json.
- blank-step-worksheet.csv and OPEN-worked-step-values.csv: selected first two, final trajectory and final event rows for each core case. Answers are openly supplied. Rows with gaps are selections from complete ledgers and must not be cumulatively summed as if consecutive.
- saved-csv-readback.json: independent exported-arithmetic readback of all eight complete ledgers.

Every concentration uses modeled liquid volume (mol/m3), rate uses mol/m3/s, interval time uses seconds, volume uses m3 and amount uses mol of substrate equivalents. Cumulative disappearance is not a product or biomass observation. The three cases have distinct initial amounts and distinct analytical trajectory windows. Compare rates or relative depletion on explicitly declared support, not an unannounced common-duration experiment.

## No-Python route

Open a complete CASE-step-ledger.csv in a spreadsheet. Decimal point is '.', comma is the separator and the first row contains column names. Keep all saved digits. Inspect snapshots, rate and refinement tables directly. Blank values follow the null rules above.

For an independent interval reconstruction, retain the supplied columns A through Q and set cell AA1 to liquid volume 0.001, AA2 to K=0.1 and AA3 to capacity=0.00001. For a zero-capacity ledger only, AA3 is zero. Add the following helper columns and copy formulas from row2 through the final row:

| Column | Formula in row2 | Meaning |
| --- | --- | --- |
| R | `=E2*H2` | Interval depleted equivalents per liquid volume |
| S | `=$AA$1*R2` | Interval depleted amount |
| T | `=SUM($S$2:S2)` | Independent cumulative depleted amount |
| U | `=$AA$1*G2` | Remaining amount |
| V | `=U2+S2-$AA$1*F2` | Step amount residual |
| W | `=U2+T2-N2` | Cumulative amount residual |
| X | `=G2+R2-F2` | Nonlinear update residual |
| Y | `=SUM($R$2:R2)` | Independent cumulative concentration equivalents |
| Z | `=$AA$3*G2/($AA$2+G2)-H2` | Rate-algebra residual |

Compare R/S/T/U/Y to exported I/L/M/K/J, respectively. Do not compute cumulative disappearance solely as initial minus remaining, or integrate snapshot rates with a trapezoid. Both would change the independent ledger exercise. The amount tolerance is MAX(1e-12*M0,volume*1e-14), in mol. The nonlinear tolerance is MAX(1e-12*MAX(S_previous,K),1e-14), in concentration units. Signed residuals stay visible.

Fill the blank worksheet using these calculations on the complete ledger, then read the separate OPEN worked values. The selected worksheet includes nonconsecutive final rows: cumulative values require all intervening complete-ledger increments. Snapshot interpolation never introduces extra budget rows.

Positive K has a nonzero analytical tail at every finite time. Report fraction/time thresholds, not a first clipped zero. The high-start case does not reach the five-percent linear-rate domain within its trajectory window. No optional three-K comparison, parameter optimizer, field data, growing Monod culture, full enzyme mechanism or old transport rerun is included.
