---
title: "OPEN worked answers: energy constraints"
lang: en
---

These worked answers are openly accessible. Save a first attempt, then compare the reasoning and record consultations, hints and changes. There is no access gate. First and revised scores remain separate; supported self-marking does not establish unaided mastery. The [student packet](student-packet.md) contains the prompts and the [curriculum](curriculum.md#rubric) the component rubric.

Numerical keys below use the accepted synthetic ENERGY-NUMERICS-1 inputs. They are modeled results, not measurements, and do not establish a natural mechanism, biological capture or learner benefit. Printed calculated results are rounded to about three significant figures; the frozen CSVs and calculation worksheets retain full precision. Analytical explanations reuse the accepted contract. The [data guide](README.md) identifies members, units and supports.

## ENERGY-E01 {#energy-answer-e01}

For the written $A\to B$ direction, one mole of reaction progress converts one mole of declared equivalent. Concentrations use $\mathrm{mol\,m^{-3}}$ of modeled liquid, so $n_i=V_\ell c_i$ is in $\mathrm{mol}$. $\Delta_rG$ is $\mathrm{J\,mol^{-1}}$ of the written reaction. In the forward initial state the activities are approximately $8\times10^{-4}$ and $2\times10^{-4}$, dimensionless, giving $Q=0.25<K_{\mathrm{eq}}=4$ and negative $\Delta_rG$. The rounded quotients and reaction energies are:

| Case | $Q$ | $\Delta_rG\ (\mathrm{J\,mol^{-1}})$ | Interpretation |
| --- | --- | --- | --- |
| forward | 0.25 | -6870 | Forward tendency |
| reverse | 19.0 | 3860 | Reverse tendency |
| equilibrium | 4.00 | 5.5e-13 | Equilibrium within reported roundoff |


The reverse case has $Q>K_{\mathrm{eq}}$, making the written forward direction unfavorable and the reverse direction favorable. The equilibrium residual is at floating-point roundoff: the exact model state has $Q=K_{\mathrm{eq}}$ and $\Delta_rG=0$. Do not clip the stored residual or assign it a new mechanism.

For $mA\rightleftharpoons mB$, with $m=2$,

$$
Q_m=Q^m,\quad K_m=K_{\mathrm{eq}}^m,\quad
\Delta_rG_m=m\Delta_rG,\quad r_m=r/m,
$$

so $-V_\ell r_m\Delta_rG_m=-V_\ell r\Delta_rG$. The physical power is invariant. The same process has been counted in a different reaction unit; its mass-action mechanism has not become second order.

Chemical standard energy pairs with chemical activities and $Q$. Transformed standard energy at declared buffered conditions pairs with transformed totals and $Q'$, with its reservoir already accounted for. Mixing the two conventions, or adding the proton reservoir again inside a transformed quotient, is invalid. No transformed calculation is implemented here. Because $\Delta\nu=0$ for this one-to-one conversion and the common concentration standard cancels, this example does not show a change of $K_{\mathrm{eq}}$ or standard reaction energy when that standard is changed consistently.

Credit components: written basis/units 4; quotient/sign 4; invariance 4; chemical/transformed pairing 3. A correct sign with a dimensional logarithm does not earn full quotient credit.

## ENERGY-E02 {#energy-answer-e02}

$r_+$ and $r_-$ are nonnegative modeled one-way volumetric rates. Their difference $r$ is signed. Forward initial $r$ is approximately $6\times10^{-5}\,\mathrm{mol\,m^{-3}\,s^{-1}}$; reverse initial $r$ is approximately $-1.5\times10^{-5}\,\mathrm{mol\,m^{-3}\,s^{-1}}$. Forward net extent is positive, with $n_B$ rising and $n_A$ falling; reverse net extent is negative, with the opposite changes. Both cumulative gross throughputs are nonnegative in either case:

$$
\Xi_+=V_\ell\int r_+dt,\quad \Xi_-=V_\ell\int r_-dt,\quad
\xi=\Xi_+-\Xi_-,\quad n_A=n_{A0}-\xi,\quad n_B=n_{B0}+\xi.
$$

At equilibrium the one-way rates are equal and positive, approximately $1.6\times10^{-5}\,\mathrm{mol\,m^{-3}\,s^{-1}}$ each. Net progress, force and dissipation vanish in the exact model. Gross exchange does not continually replenish available work. The stored tiny equilibrium values are preserved roundoff evidence.

The equilibrium state depends on $C_0$ and $K_{\mathrm{eq}}$, while the deviation decays as $e^{-\lambda t}$. Scaling $\lambda$ at fixed $K_{\mathrm{eq}}$ changes relaxation time $\tau=1/\lambda$ and one-way rates, not the equilibrium concentrations or initial state availability. Stationary equilibrium concentrations alone cannot identify $\lambda$ or measure gross exchange. A tracer or exchange observation would add information; none is supplied here.

Credit: gross/net rates 5; extents/signs 5; equilibrium work distinction 5; timing/observation limits 5. Calling zero net rate “no conversion in either direction” misses the modeled detailed balance.

## ENERGY-E03 {#energy-answer-e03}

| Quantity | Meaning | Unit |
| --- | --- | --- |
| $\Delta_rG$ | Energy change per written reaction progress | $\mathrm{J\,mol^{-1}}$ |
| $G_{\mathrm{ex}}$ | Remaining Gibbs availability relative to the declared equilibrium | $\mathrm{J}$ |
| $D$ | State-function decrease during relaxation | $\mathrm{J}$ |
| $P_{\mathrm{diss}}$ | Instantaneous free-energy dissipation rate | $\mathrm{W}=\mathrm{J\,s^{-1}}$ |

The initial forward availability is $2.06\,\mathrm{J}$. At $200\,\mathrm{s}$ the stored Gibbs availability is $1.98\,\mathrm{J}$ and the stored decrease is $0.0802\,\mathrm{J}$. Remaining availability, its cumulative decrease and instantaneous power are different quantities. Under this unforced fixed-$T,p$ relaxation, $\dot G_{\mathrm{ex}}=V_\ell r\Delta_rG\leq0$. The state has a finite availability relative to the reaction-constrained equilibrium.

$G_{\mathrm{ex}}(t)$ bounds nonexpansion work for ideal reversible extraction to that equilibrium. No device extracts work in this model; the batch instead dissipates its availability. Neither $D$ nor $P_{\mathrm{diss}}$ gives calorimetric heat, enthalpy change, ATP capture or biomass yield. Closed matter does not make the batch thermally isolated: the declared reservoir fixes temperature, and pressure is controlled.

Numerical availability uses

$$
G_{\mathrm{ex}}=RTV_\ell\sum_i[c_i\ln(c_i/c_{i,\mathrm{eq}})-c_i+c_{i,\mathrm{eq}}],
$$

with $c_{i,\mathrm{eq}}$ pinned to initial $C_0$. Keeping the direct linear terms exposes a drifting numerical inventory; recalculating equilibrium from that drift would hide it. The independent binary expression is compared only at exact analytical reference states with conserved total. A zero $c\ln c$ continuous limit does not define $\ln0$ as finite. Balanced gross exchange at equilibrium creates neither new availability nor net work.

Credit: quantity/units 6; finite availability/decrease 6; reservoir/work/heat limits 5; equilibrium interpretation 3. A work bound is not measured extracted work.

## ENERGY-E04 {#energy-answer-e04}

The [OPEN worksheet](worksheets/OPEN-worksheet.html) gives every exact source field and the same layout/formulas as the [blank worksheet](worksheets/blank-worksheet.html). Use independently supplied states for both amounts and independently accumulated gross increments for extent; do not derive the gross ledger from inventory differences.

| Field, amount in $\mathrm{mol}$ | Step 1 | Step 2 |
| --- | --- | --- |
| n_A | 0.000794 | 0.000788 |
| n_B | 0.000206 | 0.000212 |
| delta_Xi_plus | 6.35e-6 | 6.31e-6 |
| delta_Xi_minus | 4.12e-7 | 4.24e-7 |
| Xi_plus | 6.35e-6 | 1.27e-5 |
| Xi_minus | 4.12e-7 | 8.36e-7 |
| xi_net | 5.94e-6 | 1.18e-5 |
| total_residual | 0 | 0 |
| A_extent_residual | 0 | 0 |
| B_extent_residual | 0 | -2.71e-20 |


All amounts, increments, extents and matter residuals above use $\mathrm{mol}$ of declared equivalent. Tiny nonzero residuals are retained, not repaired. The B03/B08 normalized amount criterion is $10^{-11}$ with the stated amount normalizer; worksheet spreadsheet differences are compared at retained precision, not by requiring byte-identical floating-point evaluation.

| Field | Step 1 | Step 2 |
| --- | --- | --- |
| G_ex | 2.02 | 1.98 |
| delta_D_state | 0.0406 | 0.0396 |
| P_diss | 0.000403 | 0.000394 |
| endpoint_power_energy | 0.0403 | 0.0394 |
| dissipation_gap | 0.000269 | 0.000259 |


`G_ex`, `delta_D_state`, `endpoint_power_energy` and `dissipation_gap` are in $\mathrm{J}$; `P_diss` is in $\mathrm{W}$. For step 1,

$$
\begin{gathered}
\Delta D_{\mathrm{state}}=G_{\mathrm{ex}}(0)-G_{\mathrm{ex}}(100\,\mathrm{s}),\\
W_{\mathrm{end}}=(100\,\mathrm{s})P_{\mathrm{diss}}(100\,\mathrm{s}).
\end{gathered}
$$

The positive gap reflects the difference between a state drop and right-endpoint power quadrature. It is not additional biological energy or heat. State-drop sums telescope by construction; accuracy needs the independent reference and refinement. B05 retains raw roundoff and permits a normalized step-drop/gap minimum of $-10^{-12}$ with scale $RTN$, without clipping.

At the matched $200\,\mathrm{s}$ snapshot, halving the step brings both $c_B$ and $G_{\mathrm{ex}}$ closer to the independent reference. The signed concentration errors are $-5.84\times10^{-5}$ and $-2.93\times10^{-5}\,\mathrm{mol\,m^{-3}}$ for the $100$ and $50\,\mathrm{s}$ runs. The corresponding Gibbs errors are $0.000391$ and $0.000196\,\mathrm{J}$. This is a local comparison, not a whole-support maximum.

The student table separately supplies the actual `B06/c_B_amplitude` maximum over 401 shared snapshots. Its $400\,\mathrm{s}$ normalized error $0.00731$ exceeds $0.005$; $200\,\mathrm{s}$ gives $0.00365$ and passes. $100\,\mathrm{s}$ gives $0.00183$ and passes. $50\,\mathrm{s}$ gives $0.000918$ and passes. Each normalizer is the initial forward amplitude $0.600\,\mathrm{mol\,m^{-3}}$.

The accepted numerical verification binds the full gates and corrected $400$ FAIL, $200/100/50/25$ PASS history. The default is $100\,\mathrm{s}$ by the predeclared fixed policy with its $50\,\mathrm{s}$ comparison, not because $200\,\mathrm{s}$ failed. The analytical exponential/integrated-throughput reference does not iterate the candidate recurrence. Same-support refinement checks differ from conservation checks; both remain numerical evidence rather than natural validation.

401 snapshots are generated on $[0,80000\,\mathrm{s}]$. The candidate/half-step union has 1601 times, and the fixed last-three order union has 3201. Native versus snapshot metrics are separately labeled. State/cumulative-throughput interpolation is explicit; nonlinear Gibbs energy is recomputed from interpolated states using initial-$C_0$ equilibrium. No nearly vanishing-energy relative-accuracy guarantee follows from these fixed-scale norms.

Auxiliary $A$-only/$B$-only cases use two actual full $100000\,\mathrm{s}$ steps ($h/\tau=10$). The partial-endpoint control has nominal $400\,\mathrm{s}$ but actual final $133\,\mathrm{s}$ at $83300\,\mathrm{s}$. These demonstrate accounting/domain behavior, not production accuracy, and require no extra student arithmetic.

The preserved first execution had a repeated-zero support predicate bug and genuine failed outcomes. The owner corrected exactly two runner statements concerning the time list/positive-time predicate before the corrected run. Historical very-fine equilibrium roundoff failures remain preserved, not relabeled as final passing outcomes. This chronology is distinct from the genuine corrected $400\,\mathrm{s}$ accuracy failure.

Credit: independent two-step ledger 10; energy drop/proxy/gap 8; matched reference/refinement support 8; default/history/limits 4. One disclosed arithmetic error is not penalized repeatedly for its propagation.

## ENERGY-E05 {#energy-answer-e05}

| Case/time | $Q$ | $\Delta_rG\ (\mathrm{J\,mol^{-1}})$ | $P\ (\mathrm{W})$ | $W_{\mathrm{end}}\ (\mathrm{J})$ |
| --- | --- | --- | --- | --- |
| A_only/0 | 0 | null | null | null |
| A_only/100000 | 2.67 | -1010 | 7.31e-6 | 0.731 |
| B_only/0 | null | null | null | null |
| B_only/100000 | 4.5 | 292 | 5.31e-7 | 0.0531 |
| empty/0 | null | null | null | null |


`A_only` has valid $Q=0$ at the initial boundary, but $\ln Q$, force and power have no finite numerical value. `B_only` has an undefined quotient from a zero denominator, with nonfinite force/power. Initial Gibbs availability is finite through the continuous state-function limit, as shown in the student table. At both nonempty positive endpoints the states, force and power are finite. The first interval proxy uses current endpoint power; preceding null power is neither replaced by zero nor used in quadrature.

The empty state has zero concentrations, amounts, one-way/net rates, throughputs, Gibbs availability and $D$. Its quotient, force and power remain null with `empty_batch`; an empty batch is not a measured equilibrium ratio. Its endpoint proxy/gap remain null. At $t=0$ every case also has null step size/increments/drop/proxy/gap because there is no preceding step, even when the initial thermodynamic power is finite. Mathematical initial cumulative throughputs are numeric zero.

A possible critique (other justified wording earns credit):

> The equilibrium concentrations determine the equilibrium ratio only under the declared ideal, homogeneous closed-batch closure. They do not identify the relaxation scale or measure one-way exchange. Equal forward and reverse rates are model quantities, and nonzero gross exchange does not supply net work at equilibrium. An independent tracer or exchange observation could constrain that exchange, but none is provided. The batch's Gibbs availability is a reversible work bound relative to its specified equilibrium, while unforced relaxation dissipates it. It is not measured heat, extracted work or an ATP yield. Verification against analytical references and matched-time refinements checks this reduced equation and its numerical implementation. It does not validate a natural redox process, biological capture, growth or maintenance. Zero-activity starts also need explicit null force/power values and finite state-function limits; replacing them with an arbitrary epsilon would change the modeled domain.

Credit: boundary/empty semantics 6; observability/additional evidence 5; natural/coupling limits 4. Proposal of a measurement is conceptual critique, not an instruction to collect data or perform a fit.

## Feedback and evidence

Use the first attempt to identify a misconception, then revise only the affected component with explicit reasoning. Mastery criteria in the curriculum are proposed, not measured learner outcomes. Keep first/revised scores and consultation records separate. No pilot has been executed and no improvement, completion rate or unaided mastery has been established.
