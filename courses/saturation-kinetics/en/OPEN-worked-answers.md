---
title: "Saturation kinetics: OPEN worked answers"
lang: en
---

These answers are openly available for self-study. [Attempt the student tasks first](student-packet.md), retain that attempt and record consultations/revisions. The component rubric rewards justified reasoning; a critique can have several correct responses. Self-marking after consultation is not evidence of unaided mastery.

All displayed numerical values below come from the unchanged SAT-NUMERICS-1 exports accepted by the Editor. Display rounding is for reading, not a new verification tolerance. Raw tables retain full precision. Numerical acceptance covers a synthetic constant-capacity reduced equation, not mechanism-reduction accuracy, natural validation or learner outcomes. The [file guide](README.md) explains the shared model and companion ZIP.

## SK-E01 / SK-LO01

An enzyme interpretation concerns a reaction/depletion rate, typically amount per liquid volume per time, and needs a declared enzyme mechanism, constant active enzyme and an applicable reduction/observation map. Free substrate differs from enzyme-bound substrate; an assay of total free-plus-bound substrate needs its own observation map. The present synthetic cases have no microscopic enzyme states and do not test reduction accuracy.

Monod uses a biomass-specific growth response $\mu$ in $\mathrm{s^{-1}}$, with a substrate concentration scale $K_s$. Substrate consumption requires biomass and yield accounting before it can be related to growth. An empirical Monod shape does not identify an enzyme $K_m$.

Our $q$ is substrate depletion per liquid volume per time, with constant $q_{\max}$. It has no changing biomass, maintenance, feed or transport. Matching algebraic shape does not demonstrate either a microscopic mechanism or growth.

Rubric: correct three observables and units 6; evidence/assumption distinction 6; constant-capacity scope 3.

## SK-E02 / SK-LO02

$q(0)=0$, $q(K)=q_{\max}/2$ and $q$ tends to $q_{\max}$ at high $S/K$. The low-substrate limit is $q\simeq(q_{\max}/K)S$; the high-substrate limit is $q\simeq q_{\max}$. $K$ has concentration units, $q_{\max}$ volumetric-rate units and $V_\ell$ volume units.

At $S=K=0.1\,\mathrm{mol\,m^{-3}}$, the supplied rate is $5\times10^{-6}\,\mathrm{mol\,m^{-3}\,s^{-1}}$ and the amount rate is $V_\ell q=5\times10^{-9}\,\mathrm{mol\,s^{-1}}$. Multiplying by liquid volume converts basis; inserting porosity would change the declared batch.

For positive $S$, the linear rate's relative excess over the saturation law is $S/K$; the constant rate's excess is $K/S$. Five-percent rate criteria therefore require $S/K\leq0.05$ or $S/K\geq20$, respectively. At zero substrate relative rate error is undefined, represented by a blank, although $q=0$ is defined. These are instantaneous-rate comparisons; integrating an approximate rate does not inherit the same trajectory-error guarantee.

For the stated single-enzyme mechanism, $K_m=(k_{-1}+k_{\mathrm{cat}})/k_1$ differs from the binding dissociation constant $K_d=k_{-1}/k_1$. Their approximation to each other needs additional rapid-equilibrium assumptions. The phenomenological $K$ here is not an independently observed binding constant.

Rubric: curve 5; limits/rate domains 6; units/conversion 6; conditional parameter meaning 3.

## SK-E03 / SK-LO03

The fixed-volume balance gives

$$
\dot M=-V_\ell q,\qquad \dot B=V_\ell q,\qquad
M+B=M_0,
$$

with $M_0=10^{-6}\,\mathrm{mol}$ for low and $10^{-2}\,\mathrm{mol}$ for high. $B$ records substrate equivalents; it does not identify products or prove elemental conservation.

Separating the scalar law gives

$$
\int_{S}^{S_0}\left(1+\frac{K}{s}\right)\,ds=q_{\max}t,
\qquad S_0-S+K\ln(S_0/S)=q_{\max}t.
$$

For $0<f<1$,

$$
t_f=\frac{S_0(1-f)+K\ln(1/f)}{q_{\max}}.
$$

The logarithm diverges as positive $S$ approaches zero, so there is no exact finite exhaustion. Zero-substrate/zero-capacity controls have undefined fractional events, represented by null with reasons, not computed zero times.

Low begins at $S_0/K=0.01$, inside the five-percent proportional-rate domain, and remains there. High begins at 100, near the plateau, but ends analytically at $S=0.1\,\mathrm{mol\,m^{-3}}=K$ in its one-percent trajectory window. It leaves near saturation and never reaches $S/K\leq0.05$ in that window. It is a high-start case, not evidence for its eventual proportional tail. Low supplies that interpretation; transition remains owner support.

The low/high starting rates are $9.900990099\times10^{-8}$ and $9.900990099\times10^{-6}\,\mathrm{mol\,m^{-3}\,s^{-1}}$. The initial absolute high rate is much greater, but initial amount is also much greater; a faster absolute rate need not give faster fractional depletion. Plot relative substrate on declared time axes. A normalized $t/T$ axis permits a shape comparison without implying equal elapsed time.

The following threshold times are in $\mathrm{s}$, displayed to six decimal places. Each row compares the same fraction; all six numerical events are reached within their separate fixed event horizons.

| Case | Fraction remaining | Analytical time | Numerical time |
| --- | --- | ---: | ---: |
| low | $0.5$ | $6981.471806$ | $7015.891276$ |
| low | $0.1$ | $23115.850930$ | $23230.450403$ |
| low | $0.01$ | $46150.701860$ | $46380.068748$ |
| high | $0.5$ | $506931.471806$ | $506931.964486$ |
| high | $0.1$ | $923025.850930$ | $923030.120451$ |
| high | $0.01$ | $1036051.701860$ | $1036085.873868$ |

Full precision, brackets and separate horizons are in [thresholds.csv](../model/results/thresholds.csv). Low trajectory ends at $46150.701860\,\mathrm{s}$; high at $1036051.701860\,\mathrm{s}$. The numerical one-percent events occur after those trajectory ends and use the explicitly labeled event extension. They do not change the physical support of trajectory norms.

Rubric: signs/equation 9; accounting/units 6; controlled prediction/time interpretation 7; balance limits 3.

## SK-E04 / SK-LO04

Backward Euler solves

$$
S_{n+1}+h q_{\max}\frac{S_{n+1}}{K+S_{n+1}}=S_n.
$$

The endpoint rate $q(S_{n+1})$ is used by the numerical update; it is not a measured interval-average rate. Set $\Delta Z=hq(S_{n+1})$, $\Delta B=V_\ell\Delta Z$ and independently sum these increments. This preserves the method's accounting. A trapezoidal integral of diagnostic snapshot rates would be a different calculation.

The [OPEN worked-step CSV](worksheets/OPEN-worked-step-values.csv) is byte-identical to the owner's selected-row table. For the two assigned low rows:

| Quantity | Step 1 | Step 2 |
| --- | ---: | ---: |
| $S_{n+1}$ ($\mathrm{mol\,m^{-3}}$) | $0.000990195135927848$ | $0.0009804854828384393$ |
| $\Delta Z$ ($\mathrm{mol\,m^{-3}}$) | $9.804864072151698\times10^{-6}$ | $9.709653089408767\times10^{-6}$ |
| $\Delta B$ ($\mathrm{mol}$) | $9.804864072151698\times10^{-9}$ | $9.709653089408767\times10^{-9}$ |
| Cumulative $B$ ($\mathrm{mol}$) | $9.804864072151698\times10^{-9}$ | $1.9514517161560465\times10^{-8}$ |
| Remaining $M$ ($\mathrm{mol}$) | $9.90195135927848\times10^{-7}$ | $9.804854828384392\times10^{-7}$ |

The saved cumulative amount residual is $-2.117582368135751\times10^{-22}\,\mathrm{mol}$ at both rows. The first saved step residual has that value; the second is zero. The low amount tolerance is $10^{-17}\,\mathrm{mol}$. Saved floating arithmetic and a spreadsheet's evaluation order may produce slightly different last digits; retain signed residuals and judge against the declared tolerance, not exact textual equality. No concentration-update calculation is required beyond reconstructing the saved increment.

The independent analytical reference solves the integrated relation by log-root bisection rather than the production quadratic. Numerical snapshots are linearly interpolated onto 401 fixed trajectory times; reference concentrations use those same times. Reference quality itself is checked by its residual and bracket, not presumed exact by its name.

The following low-case snapshot errors are **percent of initial $S_0$**, with a $0.5\%$ trajectory limit. Event errors have a separate $1\%$ limit; refinement includes both concentration and threshold comparisons.

| Step ($\mathrm{s}$) | Snapshot error (% of $S_0$) | Trajectory pass | Event / refinement pass |
| --- | ---: | --- | --- |
| $400.0$ | $0.723460$ | False | False / False |
| $200.0$ | $0.362901$ | True | True / True |
| $100.0$ | $0.181822$ | True | True / True |
| $50.0$ | $0.090969$ | True | True / True |
| $25.0$ | $0.045509$ | True | True /  |

At $100\,\mathrm{s}$, low endpoint error is $0.181373\%$ of $S_0$, snapshot error $0.181822\%$, and the half-step concentration difference $0.090951\%$ against its $0.25\%$ limit. Maximum fractional-time error is $0.496995\%$ against $1\%$. The first default candidate passed. The low $400\,\mathrm{s}$ run failed trajectory, event and refinement gates; positivity/accounting still passed. Transition coarse failures are owner evidence, not an extra calculation. The last two low snapshot orders are approximately $0.999077$ and $0.999211$, consistent with first order. Missing edge-of-series comparisons remain null, not passes.

Maximum reported pointwise relative error for low reference values at least one percent of $S_0$ is $2.305926\%$. This uses a different denominator. At the final low trajectory snapshot, $S_{\mathrm{ref}}=9.999999999999349\times10^{-6}$ and $S_{\mathrm{num}}=1.023072369985967\times10^{-5}\,\mathrm{mol\,m^{-3}}$; its pointwise relative error is approximately $2.307237\%$. The slight distinction comes from the reported diagnostic's inclusion cutoff at reference $0.01S_0$, and both support definitions must remain explicit. Neither result is a small-tail accuracy guarantee.

The trajectory ends analytically at $46150.701860\,\mathrm{s}$; the low numerical one-percent event is $46380.068748\,\mathrm{s}$ in the bracket $[46350.701860,46450.701860]\,\mathrm{s}$. The later crossing is separately recorded, not forced onto the trajectory endpoint. Half-step comparisons use the union of endpoint grids plus the fixed snapshots, restricted to the trajectory window, with labeled interpolation. Positivity and a small ledger residual remain separate from these accuracy checks.

Owner auxiliary runs request nominal $h/\tau=10$ but boundaries shorten actual intervals: low maximum is about $4.615$, transition about $5.595$, and only high includes ten full nominal steps. They establish the reported positivity/update/accounting checks, not default trajectory accuracy. No full large step for low/transition or auxiliary accuracy is claimed.

Rubric: reconstructed increments/cumulative ledger 8; reference/support distinction 7; correct failures/norms/refinement 6; positivity and honest scope 4.

## SK-E05 / SK-LO05

One full-credit response is:

> A saturating substrate-depletion curve identifies a useful closure only on its declared liquid-volume and observation basis. It does not demonstrate growth, because no biomass or yield balance was observed, and it does not identify an enzyme mechanism, because different processes can give a similar shape. Here capacity is held constant; changing active enzyme or biomass could invalidate that assumption. At low substrate, the rate mainly informs the ratio $q_{\max}/K$; at high substrate, the plateau mainly informs capacity and weakly constrains $K$. These are practical information limits, not proof of exact nonidentifiability of an ideal full hyperbola. Measuring biomass change alongside uptake could test a growth interpretation; measuring active enzyme and free versus bound substrate could test an enzyme interpretation. Independent observations on the claimed natural setting are needed to assess applicability. Numerical verification establishes agreement with the reduced equation, not either mechanism or transfer to a mat.

The conditional logarithmic sensitivities are

$$
\frac{\partial\ln q}{\partial\ln q_{\max}}=1,\qquad
\frac{\partial\ln q}{\partial\ln K}=-\frac{K}{K+S}.
$$

These support the limiting reasoning without fitting a three-$K$ table. Other measurements earn credit if they discriminate the stated claim. No uncertainty estimate follows without actual observations and an observation/error model.

Rubric: mechanism/growth 5; information limits 5; relevant measurement 3; natural validity 2.

## Overall assessment

Total 100 points, with proposed threshold 70 and all three gates from the [curriculum](curriculum.md). Preserve component feedback and first/revised scores. Do not repeatedly penalize downstream propagation of one disclosed arithmetic error. Use the [pilot protocol](pilot-protocol.md) only for a later authorized pilot; no participant data or outcomes currently exist.
