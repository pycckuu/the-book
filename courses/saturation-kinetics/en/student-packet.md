---
title: "Saturation kinetics: student packet"
lang: en
---

This module studies a synthetic dissolved substrate in a closed, well-mixed liquid of constant volume. It uses a **constant-capacity substrate-depletion closure**. An enzyme mechanism and empirical Monod growth can share its hyperbolic shape while describing different observables.

There are five tasks, worth 100 points. The planned workload is 210 minutes plus an optional 15-minute prerequisite refresher, not measured completion time. Read the [curriculum](curriculum.md) for prerequisites and the [file guide](README.md) before opening data. [OPEN worked answers](OPEN-worked-answers.md) are public. Attempt first, save your prediction, then record any consultation or substantive hint and your revision. Revised self-marking does not establish unaided mastery.

## Model and accepted teaching inputs

$S$ is substrate concentration per modeled liquid volume; $K$ is the positive half-saturation concentration. $q_{\max}$ is fixed volumetric depletion capacity. $V_\ell$ is liquid volume, a different quantity. The synthetic input values accepted for this bounded numerical example are

$$
\begin{gathered}
K=0.1\,\mathrm{mol\,m^{-3}},\qquad q_{\max}=10^{-5}\,\mathrm{mol\,m^{-3}\,s^{-1}},\\
V_\ell=10^{-3}\,\mathrm{m^3},\qquad \Delta t=100\,\mathrm{s}.
\end{gathered}
$$

All concentration/rate units refer to liquid volume. No porosity factor, spatial flux, growth, maintenance or energy correction is added. The equations are

$$
\begin{gathered}
q(S)=q_{\max}\frac{S}{K+S},\qquad \dot S=-q(S),\\
\dot Z=q(S),\qquad Z(0)=0.
\end{gathered}
$$

$Z$ accumulates depleted substrate equivalents per liquid volume. $M=V_\ell S$ is remaining amount and $B=V_\ell Z$ is depleted amount, both in $\mathrm{mol}$. $B$ is not measured product or biomass.

Only low/high are compulsory comparisons: $S_0=0.001$ and $10\,\mathrm{mol\,m^{-3}}$, respectively. Capacity, $K$ and volume stay fixed. The transition case is owner verification support. Each case's trajectory ends at its own analytical one-percent-remaining time, not a common-duration experiment. A separate fixed event horizon permits numerical threshold bracketing. Read [case metadata](../model/saved-results.zip) and the [support guide](README.md); archive-only JSON and snapshot tables must be extracted first; see the file guide for exact member names.

## Use supplied outputs with or without Python

The no-Python route is complete: open the directly supplied CSVs in a spreadsheet, extract the immutable [numerical companion ZIP](../model/saved-results.zip) for complete interval ledgers, and fill the two assigned worksheet rows. CSVs use comma separators, decimal point and a header row. Keep saved precision; preserve blank cells as null, not zero. Report **analysed supplied outputs**, not an independent solver run. The full owner checking suite and auxiliary cases are not compulsory work.

For the Python route, from `courses/saturation-kinetics/en/`, use the owner's canonical command with a fresh empty output directory:

```sh
cd ../model
python3 saturation.py new-results
```

This runs the unchanged new model and its owner checks, producing all owner cases. Interpret only the assigned tasks below. Optional owner saved-file reconstruction is `python3 check_saved_csv.py new-results`; it reads exported arithmetic and does not execute the solver. For `saturation.py`, use normal Python without `-O`/`-OO` and with `PYTHONOPTIMIZE` unset. Keep its matched bundled `pre-run-plan.json`; the original executed source and plan identities remain historical.

## SK-E01 / SK-LO01: same shape, different meanings (15 points)

Classify these three descriptions: (a) a reduced single-enzyme rate experiment, (b) an empirical response of biomass-specific growth to substrate, (c) the present constant-capacity substrate-depletion closure. Name the measured response and units for each, state one assumption needed for its interpretation, and explain why a fitted hyperbola does not establish the other two descriptions. You need no biomass equation or microscopic constants.

Use **The First City**, “The speed limit of life: why enzymes matter” and “What we sacrificed”; use the contextual growth expression in **Model Toolkit**, “Growth, yield, and decay”. Read [Saturation without growth](scientific-reading.md) for the distinct enzyme, growth and depletion observables; see [reading dependencies](DEPENDENCIES.md).

Rubric: response/observable 6; mechanism versus empirical claim 6; fixed-capacity scope 3.

## SK-E02 / SK-LO02: curve, limits and units (20 points)

Before opening [rate-curve.csv](../model/results/rate-curve.csv), sketch $q$ against $S$. Identify half-saturation and low/high limits; state the dimensions of $K$, $q_{\max}$ and $V_\ell$. Convert the rate at $S=K$ to amount per second. Use the table to check which substrate ratios allow the linear or constant-rate approximation within five percent in **instantaneous rate**. Explain why these criteria alone do not bound trajectory error, and why $K$ is not automatically a binding-affinity measurement.

Read **Modeling the Invisible**, “What reacts: rate expressions”, and **Model Toolkit**, “Reaction rate expressions”. The reciprocal identity in **Energy Toolkit** is context only; no reciprocal regression is assigned.

Rubric: curve/half-saturation 5; limits 6; units/basis 6; parameter meaning 3.

## SK-E03 / SK-LO03: depletion and its ledger (25 points)

Draw the closed inventory and derive $\dot M$, $\dot B$ and $M+B=M_0$. State the scope of this identity. Predict the low/high rate and relative-depletion histories before consulting the [low snapshots](../model/saved-results.zip) and [high snapshots](../model/saved-results.zip). Plot $S/S_0$ on each case's declared physical time axis, or label a comparison axis $t/T$ with each case's own $T$; do not call that normalized axis common elapsed time. Interpret the change in $q/q_{\max}$ using the supplied rate law. One plot may have two panels; no transition plot is required.

Separate variables to obtain an implicit concentration-time relation. Use it to interpret the half-remaining and one-percent times in [thresholds.csv](../model/results/thresholds.csv), including fraction, units and analytical versus numerical support. Explain why positive $K$ gives no exact finite-time exhaustion. Explain whether high-start reaches the five-percent linear-rate regime within its trajectory window. Retain remaining substrate; do not invent product, biomass or elemental balances.

Read **Modeling the Invisible**, “Conservation: the only law you need”.

Rubric: signed inventory 9; cumulative accounting 6; controlled predictions 7; ledger limits 3.

## SK-E04 / SK-LO04: assess supplied computation (25 points)

Fill **only the low case steps 1 and 2** in the [blank worksheet](worksheets/blank-step-worksheet.csv). The unchanged owner worksheet also contains selected nonconsecutive final rows and other cases; those are reference support, not additional tasks. Reconstruct $\Delta Z=\Delta t\,q(S_{n+1})$, $\Delta B=V_\ell\Delta Z$, their sums through step 2, remaining $M$, and signed step/cumulative residuals. Use the actual interval width. Do not derive accumulated $B$ solely as $M_0-M$.

From [time-refinement.csv](../model/results/time-refinement.csv), assess the **low-case** series at $400,200,100,50,25\,\mathrm{s}$. Report which accepted default checks pass and which coarse checks fail. Compare numerical snapshots with the independently computed reference at the same times. Distinguish initial-concentration-normalized error, shrinking-tail relative error, threshold-time error, positivity and ledger closure. Explain why a closing ledger and a positive state do not prove time accuracy; do not repair a failure by clipping or changing physical parameters.

Use the last low trajectory snapshot and the first numerical one-percent threshold to explain why the trajectory end differs from the threshold crossing. Snapshot concentrations are piecewise-linear interpolants; their instantaneous rates are not extra budget updates. Event-extension intervals are labeled separately and excluded from trajectory-error norms.

Rubric: saved update/ledger 8; analytical comparison 7; refinement 6; positivity/failures 4.

## SK-E05 / SK-LO05: inference and natural applicability (15 points)

In about 150 words critique: “A fitted saturating depletion curve proves Monod growth, identifies an enzyme mechanism and transfers to a natural mat.” Identify the observable and fixed-capacity assumptions. Explain what low-substrate-only rate information mainly constrains and why a plateau gives weak information about $K$. Propose one independent measurement that would distinguish the claimed mechanism or applicability. Verification of this reduced equation is not natural validation.

Use E02's limiting algebra. No static three-$K$ table, residual fit, optimizer, confidence interval, extra case or research-paper reproduction is assigned.

Rubric: mechanism/growth 5; parameter information 5; discriminating measurement 3; natural validity 2.

## Submit and revise

Retain your first attempt, score by component, answer/hint consultation, revised reasoning and elapsed times by stage. Total 100 points. Proposed mastery is at least 70 plus all three conceptual gates: correct volume/rate basis and depletion sign; mechanism/empirical/fixed-capacity distinction; verification versus natural validity. A failed gate requires a targeted revision despite a high score. First-attempt and revised scores stay separate. No learner performance or workload has yet been measured.
