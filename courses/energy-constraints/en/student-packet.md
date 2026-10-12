---
title: "Energy constraints: student packet"
lang: en
---

A reaction can be favorable without being fast. Balanced conversion can continue without net progress. A closed batch can conserve matter while losing available Gibbs work. Use one reversible example to separate those statements.

There are five exercises, worth 100 points, with a planned workload of 195 minutes and an optional 15-minute prerequisite refresher. Save a first attempt before consulting the separate [OPEN worked answers](OPEN-worked-answers.md), then record what you consulted and revised. Both readings remain openly accessible. Python is not required. The [curriculum](curriculum.md) gives the component rubric and reading sequence.

## Model reminder and supplied inputs

The fictional conversion is $A\rightleftharpoons B$, with one convertible equivalent per molecule-state. The batch is well mixed and closed to matter at fixed temperature and pressure with a thermal reservoir. Constant modeled liquid volume is an incompressible-solvent/equal-solute-volume approximation. This is not a rigid fixed-$T,V$ model or an isolated energy-conserving vessel. It contains no work-extraction device, ATP, biomass or natural redox calibration.

The accepted numerical step is $100\,\mathrm{s}$ for this declared case set and support. All values are synthetic model outputs and illustrative assumptions, not observations. Use the common inputs

$$
\begin{gathered}
T=298.15\,\mathrm{K},\quad p=10^5\,\mathrm{Pa},\quad V_\ell=10^{-3}\,\mathrm{m^3},\\
c^\circ=1000\,\mathrm{mol\,m^{-3}},\quad C_0=1\,\mathrm{mol\,m^{-3}},\quad K_{\mathrm{eq}}=4,\\
\lambda=10^{-4}\,\mathrm{s^{-1}},\quad k_f=8\times10^{-5}\,\mathrm{s^{-1}},\quad
k_r=2\times10^{-5}\,\mathrm{s^{-1}}.
\end{gathered}
$$

The gas constant is $R=8.31446261815324\,\mathrm{J\,mol^{-1}\,K^{-1}}$. Declared inputs above use readable decimal notation; the calculation worksheet and CSVs retain full precision. Printed calculated results below use about three significant figures; use the full-precision inputs to check small residuals and numerical gates. Concentrations are per modeled liquid volume; $n_i=V_\ell c_i$ and $N=V_\ell C_0$. There is no porosity multiplier.

For positive states, activities $a_i=c_i/c^\circ$ and $Q=a_B/a_A$ are dimensionless. Chemical, unprimed quantities for the written $A\to B$ reaction obey

$$
\Delta_rG^\circ=-RT\ln K_{\mathrm{eq}},\qquad
\Delta_rG=RT\ln(Q/K_{\mathrm{eq}}).
$$

A transformed $\Delta_rG^{\circ\prime}$ needs the matched $Q'$ and reservoir convention; relabeling or mixing chemical and transformed quantities is invalid. For this one-to-one reaction with a common concentration standard, $c^\circ$ cancels from $Q$ and the reaction Gibbs quantities. Individual activities depend on it. The example does not show standard-state dependence of $K_{\mathrm{eq}}$ or $\Delta_rG^\circ$.

The chosen reversible law is

$$
\begin{gathered}
r_+=k_f c_A,\quad r_-=k_r c_B,\quad r=r_+-r_-,\\
\dot c_A=-r,\quad \dot c_B=r,\quad k_f/k_r=K_{\mathrm{eq}},\quad \lambda=k_f+k_r.
\end{gathered}
$$

Each $r$ has units $\mathrm{mol\,m^{-3}\,s^{-1}}$. This closure is distinct from Michaelis-Menten enzyme reduction and empirical Monod growth. The sign of Gibbs energy alone does not identify a rate law or its magnitude.

The independent reference is

$$
\begin{gathered}
c_{B,\mathrm{eq}}=C_0\frac{K_{\mathrm{eq}}}{1+K_{\mathrm{eq}}},\quad
c_{A,\mathrm{eq}}=\frac{C_0}{1+K_{\mathrm{eq}}},\\
c_B(t)=c_{B,\mathrm{eq}}-(c_{B,\mathrm{eq}}-c_{B0})e^{-\lambda t},\quad
c_A(t)=C_0-c_B(t).
\end{gathered}
$$

It evaluates the analytical solution at a requested time and does not iterate the candidate backward-Euler method. Finite-time relaxation approaches equilibrium rather than reaching exact equilibrium from a non-equilibrium start.

## ENERGY-E01 {#energy-e01}

**Reaction basis, activities and direction. 15 points.** Use the initial core states below, in $\mathrm{mol\,m^{-3}}$ of modeled liquid. Form the forward-case activities and $Q$. Determine the direction of net thermodynamic tendency in each case. State the concentration-to-amount conversion and the units of $\Delta_rG$ for the written reaction.

| Case | Initial $c_A$ | Initial $c_B$ |
| --- | --- | --- |
| forward | 0.800 | 0.200 |
| reverse | 0.0500 | 0.950 |
| equilibrium | 0.200 | 0.800 |


Rewrite the same physical process as $2A\rightleftharpoons2B$. Show how the quotient, equilibrium constant, energy per written reaction and progress rate transform, and why physical power is unchanged. This is a change of reaction basis, not a new second-order mechanism. Explain why chemical and transformed quotients/standard energies must remain paired.

## ENERGY-E02 {#energy-e02}

**Gross conversion, signed net progress and equilibrium. 20 points.** Interpret these initial modeled rates, all in $\mathrm{mol\,m^{-3}\,s^{-1}}$. Tiny equilibrium residuals are retained floating-point values, not a second equilibrium mechanism.

| Case, $t=0$ | $r_+$ | $r_-$ | $r$ |
| --- | --- | --- | --- |
| forward | 6.4e-5 | 4e-6 | 6e-5 |
| reverse | 4e-6 | 1.9e-5 | -1.5e-5 |
| equilibrium | 1.6e-5 | 1.6e-5 | -3.39e-21 |


Distinguish the nonnegative gross throughputs $\Xi_+=V_\ell\int r_+dt$ and $\Xi_-=V_\ell\int r_-dt$ from signed net extent $\xi=\Xi_+-\Xi_-$. Describe their signs and the changes in both inventories for forward and reverse relaxation. Explain why equilibrium can have ongoing gross exchange with zero net conversion and no continuing net available work.

Use the reference above to explain, symbolically, what changing $\lambda$ at fixed $K_{\mathrm{eq}}$ changes and what it leaves unchanged. State what stationary equilibrium concentration data cannot establish. No second run or additional case is required.

## ENERGY-E03 {#energy-e03}

**Finite availability, dissipation and power. 20 points.** Classify $\Delta_rG$, $G_{\mathrm{ex}}$, $D$ and $P_{\mathrm{diss}}$ by meaning and units. The direct state diagnostic is

$$
G_{\mathrm{ex}}=RTV_\ell\sum_{i=A,B}
\left[c_i\ln(c_i/c_{i,\mathrm{eq}})-c_i+c_{i,\mathrm{eq}}\right].
$$

Equilibrium concentrations in the numerical diagnostic are derived once from initial $C_0$. They are not recomputed from a drifting numerical total. The separate binary relative-entropy form checks exact analytical reference states and does not replace this numerical diagnostic. The continuous limit of the $c_i\ln c_i$ term at zero is zero; this does not make a separate zero-activity logarithm finite.

$$
D(t)=G_{\mathrm{ex}}(0)-G_{\mathrm{ex}}(t),\qquad
P_{\mathrm{diss}}=-V_\ell r\Delta_rG.
$$

Interpret the forward values below. Explain why $G_{\mathrm{ex}}(t)$ bounds remaining nonexpansion work for ideal reversible extraction to the specified equilibrium, why this unforced batch extracts none, and why neither $D$ nor $P_{\mathrm{diss}}$ is a calorimetric heat measurement or ATP yield. Explain the finite total availability despite possible continuing balanced gross exchange.

| $t\ (\mathrm{s})$ | $c_A$ | $c_B$ | $G_{\mathrm{ex}}\ (\mathrm{J})$ | $P_{\mathrm{diss}}\ (\mathrm{W})$ |
| --- | --- | --- | --- | --- |
| 0 | 0.800 | 0.200 | 2.06 | 0.000412 |
| 100 | 0.794 | 0.206 | 2.02 | 0.000403 |
| 200 | 0.788 | 0.212 | 1.98 | 0.000394 |


Concentrations in this table have units $\mathrm{mol\,m^{-3}}$. Values come from native `forward:100s` endpoints at the listed times. Use the supplied stable Gibbs and power values for E04 differences; implementing their stable evaluation is not an assigned task.

## ENERGY-E04 {#energy-e04}

**Two-step ledger and independent numerical evidence. 30 points.** Complete only the two consecutive forward steps at $100$ and $200\,\mathrm{s}$ in the [blank worksheet](worksheets/blank-worksheet.html). The initial row is supplied and is not a third arithmetic step. The separate [OPEN worksheet](worksheets/OPEN-worksheet.html) remains accessible for later comparison.

For each actual step $h$, form independent gross amount increments from current endpoint states:

$$
\begin{gathered}
\Delta\Xi_+=V_\ell h k_f c_{A,\mathrm{new}},\quad
\Delta\Xi_-=V_\ell h k_r c_{B,\mathrm{new}},\\
\Xi_\pm=\sum\Delta\Xi_\pm,\quad \xi=\Xi_+-\Xi_-,\\
n_A-n_{A0}+\xi,\quad n_B-n_{B0}-\xi,\quad n_A+n_B-N.
\end{gathered}
$$

Use the supplied concentration states to obtain both amounts independently. Do not set one amount to the total minus the other to manufacture a successful check. Sum each gross column from step 1 within the same case/run, without skipped steps or mixed histories.

Then calculate

$$
\Delta D_{\mathrm{state}}=G_{\mathrm{ex,old}}-G_{\mathrm{ex,new}},\quad
W_{\mathrm{end}}=hP_{\mathrm{diss,new}},\quad
g=\Delta D_{\mathrm{state}}-W_{\mathrm{end}}.
$$

Interpret $\Delta D_{\mathrm{state}}\geq W_{\mathrm{end}}\geq0$ with the supplied roundoff limits. The endpoint proxy is not asserted equal to the continuous dissipation integral. A telescoping sum of state drops is not independent energy-accuracy evidence.

Read this matched excerpt from `comparison.csv`. Both runs are synthetic, `support_id=snapshots-401`, $t=200\,\mathrm{s}$, `candidate_interpolated=false`. Concentration has units $\mathrm{mol\,m^{-3}}$ and Gibbs availability has units $\mathrm{J}$.

| Run | Quantity | Candidate | Reference | Signed error |
| --- | --- | --- | --- | --- |
| forward:100s | c_B | 0.212 | 0.212 | -5.84e-5 |
| forward:100s | G_ex | 1.98 | 1.98 | 0.000391 |
| forward:50s | c_B | 0.212 | 0.212 | -2.93e-5 |
| forward:50s | G_ex | 1.98 | 1.98 | 0.000196 |


Which run is closer at this time? Why does that local observation need the separate whole-support evidence below? These `B06/c_B_amplitude` rows share the 401 snapshots from $0$ to $80000\,\mathrm{s}$. Raw max errors and normalizers both have concentration units; the normalized maximum is dimensionless, with criterion $\leq0.005$.

| Step $h\ (\mathrm{s})$ | Raw max error | Normalizer | Normalized max | Status |
| --- | --- | --- | --- | --- |
| 400 | 0.00438 | 0.600 | 0.00731 | FAIL |
| 200 | 0.00219 | 0.600 | 0.00365 | PASS |
| 100 | 0.00110 | 0.600 | 0.00183 | PASS |
| 50 | 0.000551 | 0.600 | 0.000918 | PASS |
| 25 | 0.000276 | 0.600 | 0.000459 | PASS |


The corrected direct-run history is $400\,\mathrm{s}$ FAIL and $200,100,50,25\,\mathrm{s}$ PASS. The accepted $100\,\mathrm{s}$ choice follows the fixed predeclared policy, not selection of the coarsest passing step. Explain that distinction and what the independent analytical reference/refinement adds to the matter ledger. No full-array maximum or observed-order calculation is required.

## ENERGY-E05 {#energy-e05}

**Zero domains and bounded inference. 15 points.** Annotate the following supplied auxiliary rows: for each initial boundary identify whether $Q$, $\Delta_rG$, power and Gibbs availability are finite, zero or undefined/nonfinite. Describe the first positive endpoint without replacing an initial null by zero. For the empty branch also describe inventories and $D$.

| Case | $t\ (\mathrm{s})$ | $c_A$ | $c_B$ | $G_{\mathrm{ex}}\ (\mathrm{J})$ |
| --- | --- | --- | --- | --- |
| A_only | 0 | 1 | 0 | 3.99 |
| A_only | 100000 | 0.273 | 0.727 | 0.0379 |
| B_only | 0 | 0 | 1 | 0.553 |
| B_only | 100000 | 0.182 | 0.818 | 0.00262 |
| empty | 0 | 0 | 0 | 0 |


Concentrations are in $\mathrm{mol\,m^{-3}}$. Boundary positive-time rows are coarse auxiliary native endpoints, not production-accuracy evidence. Their first interval is $100000\,\mathrm{s}$; two full intervals span $200000\,\mathrm{s}$. Initial step quantities have no preceding interval. No epsilon concentration, clipping or numeric infinity is permitted.

In 120 to 180 words, critique a claim that “equilibrium concentrations measure gross exchange, prove the rate scale, and show a biologically usable energy yield.” Name a tracer or exchange observation as additional evidence, distinguish verification from natural validation, and state the limits of this uncoupled model. Naming the measurement does not assign an experiment or fit.

## Supplied-output route and submission

Open the worksheet in a browser and copy its field table to spreadsheet cells A1:D19; instructions and helper inputs appear below it. Use dot decimals and retain the full strings. Only columns C and D represent assigned steps. Calculating from supplied states/outputs is a complete route for these exercises; it is not an independent solver reproduction.

The [course README](README.md) gives the exact data ZIP extraction members, support/units and an optional canonical Python command. The four CSV families remain unchanged. Core native steps, 401 snapshots, the $100/50\,\mathrm{s}$ union and the $100/50/25\,\mathrm{s}$ order union are distinct supports. Nonlinear Gibbs values on interpolated samples are recomputed from states with initial-$C_0$ equilibrium, not interpolated as energy.

Keep the forward worksheet, written interpretations and critique, first/revised attempts, and answer/hint consultation notes. Use the [component rubric](curriculum.md#rubric) for feedback. A revised self-mark after consulting OPEN answers is supported learning and does not establish unaided mastery. No learner outcomes have yet been measured.
