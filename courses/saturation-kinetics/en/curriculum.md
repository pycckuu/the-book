---
title: "Saturation kinetics: curriculum and assessment"
lang: en
---

This curriculum uses the independently verified synthetic constant-capacity depletion companion. The workload and mastery criteria are planned; no learner outcomes are claimed.

## Prerequisites and reading sequence

Require concentration versus amount, depletion sign/rate units, elementary derivatives/exponential decay and spreadsheet arithmetic/plotting. Prior oxygen O2-LO1/2/3 or advection AD-LO2/3 can refresh accounting/verification; neither full module nor its solver is required. A five-minute prework diagnostic asks for a volumetric depletion-rate unit, conversion from concentration to amount, and a signed depletion source. Two uncertain answers suggest the optional 15-minute refresher, separately timed.

Use actual rendered titles and headings; source-file chapter numbers are not reader references. These are selected passages, not whole chapters:

| Reading | Purpose |
| --- | --- |
| **The First City**, “The speed limit of life: why enzymes matter”; “What we sacrificed” | Saturation intuition and limits of isolated-enzyme interpretation. |
| **Modeling the Invisible**, “Conservation: the only law you need”; “What reacts: rate expressions”; “What we sacrificed” | Sign, rate/volume basis and effective-parameter interpretation. |
| **Energy Toolkit**, “Linearizing the Michaelis-Menten curve: Lineweaver-Burk” | Algebraic context only; no reciprocal fit/error-model endorsement or energy calculation. |
| **Model Toolkit**, “Reaction rate expressions”, including “Hydrolysis (effective saturation closure)”; displayed Monod law under “Growth, yield, and decay” | Contrast observables/units, without importing POM parameters or solving growth. |

Read [Saturation without growth](scientific-reading.md) and the contextual book passages listed in [DEPENDENCIES.md](DEPENDENCIES.md). The course derives the declared closed dissolved-substrate model; particulate hydrolysis, dual-substrate independence and full enzyme accuracy are not inferred from it.

## Dependency and outcome map

Entry knowledge $\rightarrow$ SK-E01 $\rightarrow$ SK-E02 $\rightarrow$ SK-E03 $\rightarrow$ SK-E04 $\rightarrow$ SK-E05. There are no additional compulsory cases or tasks. Canonical machine-readable outcome IDs use two digits, as in the accepted [E/LO map](exercise-outcome-map.json).

| Exercise / outcome | Measurable submission | Points |
| --- | --- | ---: |
| SK-E01 / SK-LO01 | Correctly distinguish response/observable, evidence and assumptions for enzyme, Monod and fixed-capacity closure. | 15 |
| SK-E02 / SK-LO02 | Sketch/interpret half-saturation and limits; convert basis and distinguish concentration-scale meaning. | 20 |
| SK-E03 / SK-LO03 | Derive signed inventory, substrate-equivalent ledger and analytical fraction-time relation; interpret low/high supplied histories. | 25 |
| SK-E04 / SK-LO04 | Reconstruct two low-case rows; assess same-support reference/refinement, error norms, positivity and preserved failure evidence. | 25 |
| SK-E05 / SK-LO05 | Critique mechanism/parameter-information/natural-transfer claims and propose a discriminating measurement. | 15 |

## Analytic rubric and feedback

| Exercise | Components, in points | Total |
| --- | --- | ---: |
| E01 | Observable 6; mechanism/empirical claim 6; fixed-capacity scope 3. | 15 |
| E02 | Curve 5; limits 6; units/basis 6; parameter meaning 3. | 20 |
| E03 | Signed inventory 9; cumulative accounting 6; controlled predictions 7; ledger limits 3. | 25 |
| E04 | Saved ledger 8; analytical comparison 7; refinement 6; positivity/failures 4. | 25 |
| E05 | Mechanism/growth 5; information limits 5; independent measurement 3; natural validity 2. | 15 |

Award full component points for correct, justified work; partial points for a correct method with a disclosed omission/arithmetic error; zero where the component is absent or conceptually wrong. Do not repeatedly penalize propagation of one disclosed error. Give targeted component feedback. Critique answers need not match the worked wording.

Proposed mastery is at least 70/100 **and** three gates: (1) correct liquid-volume basis, concentration/amount conversion and depletion sign; (2) shared hyperbola distinguished from enzyme mechanism, empirical Monod and fixed capacity; (3) reduced-equation verification not called natural validation. Gate failures require targeted revision even at a high total. Keep first-attempt and revised scores, answer consultation and substantive hints separate. A revised score after OPEN answers is supported learning, not unaided mastery.

## Planned workload

| Stage | Planned minutes | Tasks |
| --- | ---: | --- |
| Prework | 25 | Diagnostic 5; selected readings 20. |
| Session | 125 | E01 20; E02 25; E03 25; break 10; E04 30; E05 15. |
| Follow-up | 60 | E03 15; E04 25; E05 10; OPEN-answer correction and feedback 10. |

Total 210 minutes, an unmeasured estimate. Optional prerequisite refresh adds 15. The E04 blank worksheet contains owner reference rows beyond its two assigned low steps; completing those, transition plots or the full owner suite is not extra compulsory work. Extracting the companion ZIP is part of the supplied-output route, not a solver implementation. Use recorded pilot time to revise the estimate later.

## Delivery and exclusions

[Student prompts](student-packet.md) and separate [OPEN answers](OPEN-worked-answers.md) are both public. The [file guide](README.md) supports Python and no-Python routes on the same inputs. No biomass dynamics, maintenance, thermodynamic gate, transport, full mass-action comparison, optimizer, static three-$K$ table or parameter confidence interval is added. Translation follows accepted integrated English source. The [pilot protocol](pilot-protocol.md) is a later proposal, not learner evidence or recruitment authority.
