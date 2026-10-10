# Oxygen diffusion and consumption: student packet

Revision O2-TEACHING-1.0.1-EN. This packet is a companion to Chapter 8, not a replacement chapter. Read the revised chapter accepted for the pilot and Appendix B. Work with the documented Modeling Scientist release identified in the module provenance file. The model inputs and the fitting dataset are synthetic teaching material. The chapter figure is schematic. Neither is a measured oxygen profile.

## A question to carry through the module

Oxygen can enter sediment from the water above and disappear into reactions below. If a profile declines with depth, what could you calculate about that exchange, and what further observation would you need before attributing it to a particular process?

You will interpret a profile, construct its balance, inspect a simulation, predict parameter effects, compare with synthetic data, and critique a field inference. Submit your predictions before computing so that an incorrect first prediction can become useful evidence of how your reasoning changed.

## Before you start

You need concentration-unit conversion, basic derivatives and integrals, a first-order rate law, and either spreadsheet formulas or the ability to run a documented Python script. You do not need to write a transport solver. Complete this ungraded diagnostic: (1) convert 200 micromol/L to mol/m3; (2) calculate the gradient from C = 0.20 mol/m3 at x = 0 to C = 0.10 mol/m3 at x = 0.002 m; (3) sketch inward and outward arrows for a slab when oxygen decreases downward; (4) find bulk concentration at C = 0.20 mol/m3 and phi = 0.8. If two or more items are uncertain, use the instructor's units and balance bridge before E02.

Prework is approximately 45 minutes. The lesson is planned for 180 minutes with a 10-minute break and about 90 minutes of follow-up work. The optional 20-minute prerequisite bridge is additional to that budget. Actual timing will be measured in a future learner pilot.

## The accepted teaching model

Depth x increases downward from the sediment-water interface. C is dissolved oxygen per unit volume of porewater, in mol m^-3 water. Porosity phi is dimensionless. D_s is the tortuosity-corrected sediment diffusivity in m2/s; its definition does not include an additional porosity multiplier. F is flux per unit sediment area, positive downward. q = kC is oxygen consumption per unit porewater volume. R = -phi q is the bulk oxygen source, negative for consumption.

Equation O2-Q01, bulk balance:

$$\frac{\partial(\phi C)}{\partial t}=-\frac{\partial F}{\partial x}-\phi kC,\qquad F=-\phi D_s\frac{\partial C}{\partial x}.$$

For constant phi > 0, D_s and k, no advection and no explicit biological adaptation, Equation O2-Q02 is

$$\frac{\partial C}{\partial t}=D_s\frac{\partial^2 C}{\partial x^2}-kC.$$

The domain is 0 < x < L. Conditions: C(0,t) = C_0 for t > 0; dC/dx(L,t) = 0; C(x,0) = 0 in the interior. The top boundary is switched on at t = 0. The resulting discontinuity at that boundary is intentional. The lower condition closes the modeled domain; it is not an assertion that every sediment has a sealed bottom.

The first-order sink is an aggregate oxygen demand. It does not distinguish aerobic organic-carbon respiration from oxidation of reduced chemical species. The baseline omits a thermodynamic factor, donor dynamics, sulfate/methane coupling, variable porosity, advection, irrigation and multidimensional geometry.

Equation O2-Q03, reference steady solution (k > 0):

$$C_{ss}(x)=C_0\frac{\cosh((L-x)/\ell)}{\cosh(L/\ell)},\qquad \ell=\sqrt{D_s/k}.$$

This solution stays positive for positive C_0. An operational detection depth is a threshold crossing, not an exact oxygen-free front. Use finite-domain formulas for quantitative answers. The exponential C_0 exp(-x/ell) is only a deep-domain near-surface approximation.

All inputs below are illustrative choices, not field measurements or values calibrated from literature.

| Input | Value | Meaning |
|---|---:|---|
| L | 0.03 m | Domain depth |
| D_s (code `D`) | 1e-9 m2/s | Diffusivity, excluding the porosity prefactor |
| k | 1e-5 s^-1 | Aggregate first-order sink coefficient |
| phi | 0.8 | Water-filled porosity |
| C_0 | 0.2 mol/m3 water (200 micromol/L) | Interface concentration |
| N, dt | 80 cells, 1000 s | Baseline transient settings |

Use code `D` for mathematical D_s. For the E04 domain comparison the fixed evaluation depth is x = ell_baseline = 0.01 m, and the short domain is L = 0.01 m. The remaining cases use the original L unless specified.

## What to submit

Use one response document with headings O2-E01 through O2-E07, plus your output files or spreadsheet. Each calculation must state the equation, inputs, units and which boundary conditions it assumes. Label every figure or table as schematic, simulated, synthetic fitting data, or independently measured. Keep original predictions visible beside revised reasoning. Your total is 100 points. A total of 70 or more requires two scientific gates as well: consistent flux sign and volume basis; no claim that synthetic/schematic agreement validates a real sediment. The instructor will ask for targeted correction if either gate fails.

## O2-E01: profile detective (10 points)

Reading: chapter opening and "The porewater profile, explained". Dependency: units and gradient signs. Outcome: O2-LO1.

The canonical chapter figure generator used oxygen f(z) = exp(-z/1.4), where z is depth in cm and f is dimensionless relative concentration. Sulfate and methane were drawn from separate illustrative functions on relative scales, not from a coupled simulation or measurements.

1. Make a three-row table of f at z = 0, 1.4 and 2.8 cm. State which axis increases downward.
2. Infer oxygen's diffusive flux direction. Explain what a change in slope with depth can tell you under a steady diffusion-only assumption, and what a profile alone cannot identify about the sink.
3. Write a corrected two-sentence caption that states provenance and avoids calling the sulfate/methane graphical crossing a measured transition.
4. Name two measurements you would need to turn this sketch into a testable field balance. Do not estimate an actual field respiration rate from the relative axes.

## O2-E02: make the bookkeeping explicit (15 points)

Reading: "Conservation: the only law you need", "What moves: transport", Appendix B "The diagenetic equation". Dependency: E01 and diagnostic. Outcome: O2-LO2.

1. Draw a slab of unit sediment area between x and x + dx. Define stored oxygen, upper/lower fluxes and total consumption. Derive O2-Q01 by dividing by dx and taking the limit. State units and volume basis for C, phi C, F, q and R.
2. Show why constant porosity cancels from O2-Q02, and identify two reported quantities from which it must not disappear.
3. Explain the sign of F when oxygen decreases downward, and of R when oxygen is consumed. Translate the three initial/boundary conditions into words.
4. Differentiate O2-Q03 to verify its steady equation and both boundary conditions. State what happens as k tends to zero and why setting C(L)=0 would define a different problem.

## O2-E03: reproduce and verify a simulation (20 points)

Reading: chapter "Start with one species", model README and verification report. Dependency: E02. Outcome: O2-LO3.

The supplied `model/oxygen_model.py` is a byte-identical copy of the verified model code, not a course-written solver. It requires Python 3 and the standard library. From the student bundle directory run:

```bash
python3 --version
python3 model/oxygen_model.py --out my-run
```

Choose a fresh output directory so prior evidence stays intact. The command runs the checks and saves `verification.json`, `profiles.csv` and `synthetic-profile.csv`. The profile columns are `t_s`, `x_m`, `C_simulated_mol_m3_porewater`, `C_analytic_steady_mol_m3_porewater`. Positions are cell centres. Profiles are exported at t = 10000, 100000 and 1000000 s. The verification report has separate `grid`, `grid_orders`, `time_dt_s`, `time_max_errors` and `time_orders` fields. Read the supplied `verification-methods.md` before interpreting them.

The main script also reports a synthetic fit used as a benchmark in E05. Credit requires its objective, residuals and identifiability reasoning, not simply copying its fitted number.

Without Python, use the archived `model/results/profiles.csv` and `model/results/verification.json` in a spreadsheet for E03, with `model/verification-report.md` and `verification-methods.md` as interpretation guides. Record that you analysed supplied outputs, not a run of your own. Record the archived command, inputs and Python version from the report, then compute profile errors and inspect spatial/time checks. Use `data/synthetic-profile.csv` and spreadsheet formulas for E05. The exported verification JSON includes the same fit benchmark that the code reports, but contains no completed E04 sensitivity or E05 residual answer tables. The numerical-source `model/README.md` describes a wider snapshot; only its oxygen-model command is part of this core student bundle. The optional measured-data handout is supplied separately.

1. Save the exact inputs, command and software version. Explain the origin of the synthetic inputs. Plot numerical and analytic steady concentrations at the same positions, with units. Record the maximum error and its normalization.
2. Inspect the direct discrete-steady spatial study at N = 20, 40, 80 and 160. It solves the discrete steady equations without a finite final time. Separately compare the startup outputs with the steady reference, then inspect the smooth-eigenmode time-step study, whose initial condition differs from the zero-interior startup. Report the actual sequence of errors and the tolerances used by the scientist, without asserting that stability implies accuracy.
3. At steady state integrate consumption over the domain and compare it with upper flux minus lower flux. During startup explain how accumulation changes that equality. Use bulk units and distinguish instantaneous from integrated-in-time balances.
4. Inspect the k = 0 and positivity checks. Explain why these checks can reveal implementation errors but cannot establish that first-order demand is an adequate field mechanism.

If you cannot run Python, use the frozen exported profiles and check report plus a spreadsheet for the analytic solution and budget. Clearly state that you inspected supplied results rather than independently running the solver. Both routes require calculations and interpretation; only the execution claim differs.

## O2-E04: predict, perturb and test the domain (15 points)

Reading: "Start with one species" and "What we sacrificed". Dependency: E03. Outcome: O2-LO4.

Write predictions before evaluating O2-Q03. Change one baseline input at a time: double k; double D_s; double C_0; set phi = 0.6 holding D_s fixed. For each, report ell, C(L)/C_0, the downward upper flux F(0) in mol/m2/s and mmol/m2/day, and the direction of the change. Do not assume porosity changes leave real tortuosity unchanged: this is a controlled mathematical experiment.

Then change only L to ell_baseline = 0.01 m, and separately to 2L_baseline = 0.06 m. Compare C at the fixed depth x = ell_baseline and F(0) to baseline. Explain why a shallower no-flux boundary can alter a near-surface interpretation.

Finally, find the first depth where C/C_0 falls to 0.05, if it exists in each domain. Give your method, and state explicitly when the threshold is not reached. Contrast this relative threshold with a fixed instrument concentration threshold if C_0 changes. No case has an exact zero-concentration front under the accepted first-order steady model.

## O2-E05: recover only what the data can identify (20 points)

Reading: model synthetic-data provenance, chapter "Start with one species" and "Effective rate constants". Dependency: E04. Outcome: O2-LO5.

Use `data/synthetic-profile.csv`, or the byte-identical CSV generated in E03. Ten positions x = 0.003, 0.006, ..., 0.030 m were generated from O2-Q03 with alpha_true = 10000 m^-2, C_0 = 0.2 mol/m3 and L = 0.03 m, then perturbed using independent Gaussian draws with sigma = 0.002 mol/m3 and seed 20261010. The known seed and generating value make this a transparent recovery experiment.

The code's `synthetic_fit` uses a one-parameter least-squares search over alpha in [100, 1e6] m^-2 and reports a 200-replicate parametric bootstrap. The function evaluates the formula with D = 1 and k = alpha as an algebraic ratio parameterization; these are not new physical diffusivity or rate inputs. If you use the reported conditional percentile interval, state its model/noise assumptions. You may instead show point-recovery error and a controlled perturbation/refit.

1. Plot the supplied synthetic concentrations at their documented positions, using the documented units. State how the values were generated and what the known perturbations mean. Do not present them as instrument readings.
2. Estimate only alpha = k/D_s (m^-2) with C_0 and L fixed as documented. Use the verified model's fitting command or a transparent one-parameter spreadsheet search. Write the objective and report the fitted value with concentration residuals. Compare its loss with the documented generating value, if the dataset identifies it.
3. Construct another pair (D_s,k) by multiplying both by two. Demonstrate why the normalized steady profiles coincide. Identify what changes in the physical flux or transient behavior despite the same steady profile shape.
4. Explain which uncertainties the synthetic exercise includes and which it does not. If a noise scale is provided, evaluate one sensible perturbation/refit or report the release's recovery error. Do not call a numerical search grid or a noise-free fit a statistical confidence interval.
5. Propose an independent transport or transient measurement that could separate D_s and k. Explain how it adds information and which nuisance quantities (phi, surface C_0, geometry, boundary layer) would still matter.

## O2-E06: critique an inference from a field study (15 points)

Reading: chapter "What we sacrificed"; inspected publisher abstract of Gundersen and Jorgensen (1990), *Nature* 345, 604-607.[^gundersen]

Dependency: E05. Outcome: O2-LO6.

The inspected abstract describes in situ microelectrode and surface/DBL mapping at a Danish coastal sediment. In that particular geometry, their three-dimensional diffusive-flux estimate was about 2.5 times the simple one-dimensional estimate. This statement comes from the abstract; the full methods have not been inspected for this task.

1. Identify which baseline assumption this finding challenges. State why multiplying every oxygen uptake estimate by 2.5 would not be justified.
2. Design one additional observation that could test the one-dimensional approximation at your study site. Say what outcome would support retaining it, and what outcome would require revising the geometry or transport closure.
3. Evaluate the claim "Our code matches the analytic profile and fitted synthetic data, so the model validates aerobic microbial respiration in this sediment." Separate code verification, fitting, field validation and sink attribution. Name a field datum reserved from fitting and a comparison that would test an actual prediction.
4. Give one plausible failure of the fixed-surface-C_0 condition when a diffusive boundary layer is present. Propose how to test it without immediately adding a more complex model.

[^gundersen]: Jens K. Gundersen and Bo Barker Jorgensen, "Microstructure of diffusive boundary layers and the oxygen uptake of the sea floor," *Nature* 345 (1990): 604-607, https://doi.org/10.1038/345604a0. Publisher abstract inspected 10 October 2026: https://www.nature.com/articles/345604a0 . This reference is included in the book bibliography. [@GundersenJorgensen1990]

Optional E06 extension (ungraded, approximately 20 to 30 additional minutes, not part of the nominal module budget): inspect the separate handout `optional-observed-data/data-comparison-task.md` in the companion source bundle for Beck and Maiti's archived measured station summaries. This is a separate observational-provenance task, not a replacement for the synthetic concentration-profile fit. The summaries contain flux and penetration-depth values, not raw profiles. Use the pinned versioned DOIs and preserve missing values. The instructor controls this additional handout and keeps its answers separate. No extension is required to earn the core 100 points.

## O2-E07: an independent transfer memo (5 points)

Dependency: E01 through E06. Outcome: O2-LO7. Complete without the instructor solution packet.

At time t*, surface oxygen halves while D_s, k, phi and L remain unchanged. In at most 150 words, predict (a) the eventual concentration profile and upper flux relative to the old steady values, (b) what you can say about the response before the new steady state, (c) whether a relative 5% detection depth and a fixed absolute detection threshold behave the same way, and (d) one observation that would expose a failed assumption. State which of your claims is exact in the accepted linear model and which is conditional about the field system. No simulation result for this event is supplied.
