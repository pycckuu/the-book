---
title: "Energy constraints: curriculum and component rubric"
lang: en
---

The module follows **Saturation without growth** and precedes growth, yield and maintenance. It uses a fixed-$T,p$ synthetic reversible batch with one conserved A/B equivalent. Use the supplied [scientific reading](scientific-reading.md), verified model and data. The [source guide](DEPENDENCIES.md) identifies the prerequisite readings and boundaries of this module. No learner outcomes have been measured.

## Prerequisite map

Concentration versus amount, signed balances, rate versus cumulative amount, elementary logarithms/exponentials and spreadsheet arithmetic are required. Python is optional. Prior conservation/verification work can refresh the entry skills; no full prior solver replay is required.

Prework diagnostic (5 planned minutes): convert a liquid concentration to amount using the supplied volume, state how a rate differs from its integral, and identify why a logarithm cannot take a dimensional or zero argument. Two uncertain answers suggest a separately timed 15-minute refresher. This is entry preparation, not a sixth exercise. Diagnostic responses are used for feedback, not added to the 100-point assessment.

Prerequisites $\rightarrow$ ENERGY-E01 $\rightarrow$ ENERGY-E02 $\rightarrow$ ENERGY-E03 $\rightarrow$ ENERGY-E04 $\rightarrow$ ENERGY-E05. Each exercise maps to the correspondingly numbered ENERGY-LO outcome in the [English outcome map](exercise-outcome-map.json).

| Selected reading | Purpose |
| ------------------------------------------- | --------------------------------------------------------- |
| **The Budget of the Universe**, “The budget: Gibbs free energy”, “Real conditions, not standard ones”, “Why favorable reactions still stall” | Use accepted corrected chemical/transformed, work-bound and favorability/rate distinctions. |
| **Modeling the Invisible**, “Conservation: the only law you need”, “What reacts: rate expressions” | Signed rates and volume basis; coupled remaining drive is not simply uncoupled chemical equilibrium. |
| **Model Toolkit**, “Thermodynamic factor” | Qualified context only; no ATP calculation or rate-law transfer. |
| **Saturation without growth**, “One shape, distinct observables”, “Declare the liquid and the ledger”, “A synthetic calculation, with a separate reference” | Distinguish closure, observable, balance and verification. |
| **Energy, rates, and a reversible batch** (scientific-reading.md) | Isolates reaction basis, gross/net accounting, Gibbs availability and finite-domain meanings. The student reminder uses the same closure; this is no additional task. |

Only selected passages are preparation. The source guide links the corrected prerequisite versions, which may be on separate book branches.

## Exercise and outcome sequence

| Exercise / outcome | Bounded student prompt and assessable evidence | Points / session minutes |
| --------------- | ----------------------------------------------------------------------------- | ---------- |
| ENERGY-E01 / ENERGY-LO01 | Write the $A\to B$ reaction basis and liquid/equivalent units. Form dimensionless activities and $Q$ for a positive supplied state. Determine the sign of $\Delta_rG=RT\ln(Q/K_{\mathrm{eq}})$. Show symbolically that rewriting the same process as $2A\rightleftharpoons2B$ doubles energy per written reaction and halves its progress rate, preserving power. Explain why chemical and transformed quantities cannot be mixed. | 15 / 20 |
| ENERGY-E02 / ENERGY-LO02 | Using supplied forward, reverse and equilibrium core rows, distinguish $r_+$, $r_-$ and their signed difference, and distinguish $\Xi_+$, $\Xi_-$ and $\xi$. Explain nonzero balanced exchange with zero net rate at equilibrium. Use the analytical exponential form to explain why changing $\lambda$ at fixed $K_{\mathrm{eq}}$ changes timing but not equilibrium, without running a second case. State what equilibrium concentrations alone cannot identify. | 20 / 20 |
| ENERGY-E03 / ENERGY-LO03 | Classify $\Delta_rG$ (energy per reaction), $G_{\mathrm{ex}}$ and $D$ (energy), and $P_{\mathrm{diss}}$ (power), with units. Explain $G_{\mathrm{ex}}(t)$ as remaining nonexpansion-work availability relative to the specified equilibrium, and $D=G_{\mathrm{ex}}(0)-G_{\mathrm{ex}}(t)$ as the finite decrease during unforced relaxation. Distinguish dissipation, extracted work and heat. Explain why balanced gross conversion cannot provide ongoing net work. | 20 / 25 |
| ENERGY-E04 / ENERGY-LO04 | Reconstruct only the first two consecutive forward-case steps in a supplied blank worksheet. Sum independent forward/reverse amount increments, compare their net difference with both state changes, and calculate the state drop, right-endpoint power energy and gap. Use one same-time forward reference/refinement excerpt and the preserved candidate-history summary to judge numerical evidence. State why a telescoping state-drop sum alone cannot verify energy accuracy. | 30 / 35 |
| ENERGY-E05 / ENERGY-LO05 | Annotate supplied initial/first-positive-time boundary rows and an empty initial row with the correct finite, zero or null meanings. In a 120 to 180 word critique, explain why equilibrium concentrations do not measure gross exchange or identify $\lambda$, name a tracer or exchange observation as additional evidence, and distinguish numerical verification from a natural, ATP or growth claim. No experiment, fit or new case is assigned. | 15 / 20 |



Only the two consecutive forward native steps require ledger arithmetic. Reverse/equilibrium and boundary/empty excerpts are interpretation. Full auxiliary/partial-step/refinement histories remain owner support. No extra case, fit, tracer experiment, export family or assessed task is added.

## Rubric {#rubric}

| Exercise | Components in points | Total |
| ------------ | ----------------------------------------------------------------------------- | -------- |
| E01 | Written basis and liquid units 4; dimensionless quotient and sign 4; basis/power invariance 4; chemical/transformed distinction 3. | 15 |
| E02 | Gross/net rates 5; cumulative extents and signs 5; equilibrium exchange/work distinction 5; time scale and observation limits 5. | 20 |
| E03 | Quantity/units distinction 6; finite availability and decrease 6; reservoir/work/heat limits 5; equilibrium interpretation 3. | 20 |
| E04 | Independent two-step matter ledger 10; state drop/right-endpoint proxy/gap 8; matched reference and refinement support 8; actual default/failure policy and limits 4. | 30 |
| E05 | Boundary/empty null meanings 6; observability and additional evidence 5; natural/coupling limits 4. | 15 |

Full component credit requires justified correct work. Partial credit recognizes a sound method with a disclosed omission or arithmetic error; an absent or conceptually incorrect component receives zero. Do not repeatedly penalize propagation of one disclosed arithmetic error. Critique responses may use different justified wording.

Proposed mastery: at least 70/100 plus three conceptual gates: (1) consistent reaction/volume/activity basis and zero-log handling; (2) gross versus net conversion and work versus heat/power; (3) independent numerical evidence distinguished from natural validation. Gate failure needs targeted revision despite a high total. Record first-attempt and revised component scores, answer consultations and substantive hints separately. Supported revision is not evidence of unaided mastery. These are proposed criteria, not observed outcomes.



The five component totals are 15, 20, 20, 30 and 15. The subtotal is 100; optional preparation does not change the rubric. Numerical keys in the separate [OPEN worked answers](OPEN-worked-answers.md) now use exact accepted outputs. Symbolic reasoning, units, support and justified critique matter; numerical agreement alone is insufficient.

## Attempt-first delivery and routes

Student prompts and OPEN answers are separate readings, both publicly accessible. Save the first attempt before consultation, then document answer access/hints and revisions. There is no withholding of answers. First/revised scores remain separate. A supplied-output spreadsheet route is complete for the assigned exercises and is distinguished from independent numerical reproduction.

The [blank worksheet](worksheets/blank-worksheet.html) and [OPEN view](worksheets/OPEN-worksheet.html) share the exact two source rows. Stable Gibbs and power fields are supplied inputs; the blank amount/increment/drop/proxy/gap/residual cells are reconstruction targets. All four scientific families remain unchanged in the [model data companion](../model/saved-results.zip).

## Planned workload

| Stage | Planned minutes | Contents |
| ---------------- | -------------------- | ------------------------------------------------------------ |
| Prework | 20 | Diagnostic 5; selected passages 15. |
| Session | 130 | E01 20; E02 20; E03 25; break 10; E04 35; E05 20. |
| Follow-up | 45 | E03 10; E04 20; E05 revision and OPEN-answer feedback 15. |

Total 195 planned minutes, plus 15 optional prerequisite minutes. Time estimates are unmeasured. No completion rate or learner benefit is claimed. The [pilot protocol](pilot-protocol.md) proposes future evidence collection for one complete existing module and is unexecuted.
