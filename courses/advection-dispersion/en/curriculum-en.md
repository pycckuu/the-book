---
title: "Flowing water, spreading and loss: curriculum and assessment"
lang: en
---

This module bridges the book readings “Modeling the Invisible” and “The Water Planet”. It carries oxygen-pilot reasoning forward rather than repeating that module. [Exercises](student-packet-en.qmd) and [OPEN worked answers](worked-answers-en.qmd) are separate readings, both openly available. Numerical defaults and teaching inputs are accepted; The English scientific and teaching sources are integrated; format review and Russian alignment remain separate gates. The [pilot protocol](pilot-protocol-en.md) has not been executed.

## Entry knowledge and prerequisite map

Required mathematics: derivatives, definite integrals, exponential decay and units; numerical analysis at the level of finite-volume cells, time steps and refinement. Both routes require basic tabular arithmetic, plotting and signed residuals. Running Python is optional for the supplied-output route.

Use the existing five-minute diagnostic within prework: distinguish resident $C$ from bulk inventory $\phi C$; explain the sign of diffusive flux; state the units of first-order $k$; distinguish numerical verification from natural validity. If two items are uncertain, use the optional 20-minute oxygen bridge and record that extra time separately. No new scored exercise is added. Darcy versus porewater velocity and known-total-flux inlet are new content.

Prerequisite chain: oxygen inventory/flux (O2-LO1/2) then AD-E01 then AD-E02; oxygen verification (O2-LO3) plus those balances then AD-E03; oxygen controlled comparisons (O2-LO4) then AD-E04 after E02/03; oxygen residuals (O2-LO5) then AD-E05 after E03/04; oxygen evidence appraisal (O2-LO6/7) plus the preceding work then AD-E06. The machine-readable [E/LO map](exercise-outcome-map.json) records exact dependencies.

## Outcomes, readings and evidence

| Outcome and exercise | Measurable evidence | Reading connection |
| --- | --- | --- |
| AD-LO1 / AD-E01 | Define both velocities with units and predict a transport-only pulse before viewing output; distinguish the two porosity controls. | “Modeling the Invisible”, “What moves: transport”; appendix “Advection” and “Externally impressed flow (Darcy)”. |
| AD-LO2 / AD-E02 | Derive consistent storage, total flux and bulk loss; specify IC/inlet/outlet and retain finite-time storage. | “Modeling the Invisible”, “Conservation: the only law you need”; accepted model interface. |
| AD-LO3 / AD-E03 | Reconstruct one step/cumulative ledger, identify the correct references and explain selected grid/time orders and artificial spreading. | “Modeling the Invisible”, “What we sacrificed”; accepted verification/export definitions. |
| AD-LO4 / AD-E04 | Compare the four fixed-duration cases using own-dose fractions, outlet median and temporal width; explain retained storage and parent loss. | “Let the water move” and appendix “Advection, dispersion and parent loss”; pinned scenario inputs. |
| AD-LO5 / AD-E05 | Calculate eight compatible residuals and three equal-weight RMSE scores; state known controls and the steady scaling ambiguity. | “The Water Planet”, “The modeling challenge”; synthetic observation support. |
| AD-LO6 / AD-E06 | Write a supported 150-word closure critique with a section locator and a discriminating observation, retaining numerical-evidence limits. | “The Water Planet”, “The modeling challenge”; P02 Gouze2021Dispersion methods 2.1 to 2.3 and conclusion 4. |

These are intended observable performances, not achieved student outcomes. Students need the integrated book readings alongside this packet. Broader book claims are not newly verified by this course.

## Module syllabus and planned time

| Stage | Planned minutes | Work |
| --- | ---: | --- |
| Prework | 30 | Diagnostic 5; oxygen refresh 10; focused reading 15. |
| Session, transport and balance | 45 | E01 15; E02 30. |
| Session, numerical reasoning | 50 | E03 40; break 10. |
| Session, comparisons and critique | 85 | E04 35; E05 30; E06 20. |
| Follow-up | 60 | E03 20; E05 25; E06 15. |

The plan totals 270 minutes (30 prework, 180 session including the break, 60 follow-up). The optional prerequisite bridge adds 20 minutes. These durations are estimates, not measured learner load. No optimizer, pore-scale simulation, compulsory full benchmark rerun or additional exercise is required.

For either route, record predictions first and then use exports. The canonical single-case Python command is in the exercise packet; the no-Python route calculates from the same supplied interval/cell data in a spreadsheet. A spreadsheet analysis is not an independent solver execution. Open answers remain available for self-study; learners record what changed after consultation.

## Analytic rubric, 100 points

| Exercise | Rubric components | Maximum |
| --- | --- | ---: |
| AD-E01 | Velocity basis/units 3; transport sketch 4; reasoned prediction 3. | 10 |
| AD-E02 | Slab/terms 8; volume basis/units 5; boundaries/initial state 4; assumptions 3. | 20 |
| AD-E03 | Budget 7; reference checks 6; spreading/refinement 8; positivity/limits 4. | 25 |
| AD-E04 | Prior predictions 6; quantified comparisons 8; loss/inventory 4; limits 2. | 20 |
| AD-E05 | Observable/provenance 3; residuals 5; inference/conditions 5; independent observation 2. | 15 |
| AD-E06 | Supported critique 4; independent test 3; prediction/limit 3. | 10 |

For each component, full credit requires the stated evidence and a justified conclusion. Partial credit follows the correct portion of the method; absent or contrary reasoning earns no credit for that component. Keep original work and corrections distinguishable. Do not penalize the same disclosed arithmetic error repeatedly when its propagation is otherwise consistent. Use unrounded files as the numerical reference, but grade support, units and interpretation rather than exact final displayed digits. A saved-output arithmetic check is not a PDE accuracy tolerance.

Proposed mastery requires at least 70/100 and all three conceptual gates: (1) consistent velocity, volume and total-flux accounting in E01/02; (2) physical versus numerical spreading in E03; (3) no inference from numerical verification or synthetic agreement to natural validity in E05/06. An unsupported “missing mass equals reaction” statement also fails gate 1 because it drops storage. Gate failures require targeted revision even if the point total is high. Report first-attempt and revised scores separately, including answer-consultation status; revised self-study success cannot be reported as unaided mastery.

## Scientific and teaching limits

The constant-area saturated single-mobile-species model tracks resident concentration, advective/dispersive transport and aggregate parent disappearance. It supplies no product, elemental or microbial mechanism balance. All observations are noiseless synthetic interval means. Fixed transport/feed/geometry condition the three-$k$ comparison; it is not a simultaneous multi-parameter estimate. Timing diagnostics condition on finite-window exported mass, and resident spatial width is a different statistic. Generated-medium pore-scale numerical evidence in P02 constrains closure interpretation without validating this teaching column against nature. There are no actual learner attempts or measured learning gains yet.
