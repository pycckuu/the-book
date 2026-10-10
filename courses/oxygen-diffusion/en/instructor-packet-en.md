# Oxygen: worked answers and rubric

Revision O2-TEACHING-1.0.1-EN. These worked answers are openly included in the book. Try the exercises before consulting them. Solutions below refer to the same accepted model and synthetic inputs as the student packet. This packet supplies the answer key and point allocation; it does not report any learner attempt or outcome.

## Scoring and scientific gates

Score 100 points: E01 10; E02 15; E03 20; E04 15; E05 20; E06 15; E07 5. Proposed mastery is at least 70/100 plus both gates: consistent flux sign and reaction-volume basis; no synthetic/schematic-to-field validation claim. Give partial credit for a coherent derivation carried through with a stated arithmetic error. Do not deduct the same upstream error again if later reasoning is internally consistent. Gates require targeted correction regardless of total. Log first independent answers and assistance separately. A correct number without units, setup or provenance cannot earn full computation credit.

## Entry diagnostic and bridge

Expected: 200 micromol/L = 0.200 mol/m3; gradient = (0.10 - 0.20)/0.002 = -50 mol m^-4 water; diffusive oxygen flux is positive downward (a negative gradient enters F = -phi D_s C_x); bulk concentration is 0.8 * 0.20 = 0.16 mol/m3 sediment. A slab can receive flux from above and transmit a smaller flux below while consuming the difference. "There is no outflow because oxygen is falling" is not justified by the gradient alone.

If two or more are uncertain, offer the 20-minute bridge: 5 minutes on one litre and one cubic metre; 5 on C versus phi C using a one-cubic-metre sediment box; 5 on two-face flux arrows and signs; 5 on one corrected diagnostic. Require students to explain the corrected volume basis before E02. Record bridge support in the pilot.

## O2-E01 expected response (10 points)

At z = 0, 1.4, 2.8 cm, f = 1, exp(-1) = 0.367879, exp(-2) = 0.135335. Concentration is horizontal and relative; depth is vertical and increases downward. This calculation describes the generator's schematic, not the accepted model or a sediment measurement.

A negative C_x gives positive downward F for positive phi and D_s. Under steady, constant-coefficient diffusion-only assumptions, curvature C_xx = kC/D_s is positive for the first-order sink: the negative concentration slope relaxes with depth as downward flux is consumed. A declining profile by itself does not identify the species of microbe, a unique organic-carbon respiration rate, or the appropriateness of that rate law. Changing D_s, other transport or transient accumulation can change the inference.

Acceptable caption: "Schematic relative oxygen, sulfate and methane profiles illustrate possible transport and reaction patterns. The curves are drawn from separate functions; their crossing is not a measured sulfate-methane transition or a coupled-model prediction."

Accept measurements of an oxygen microprofile with absolute concentrations and positions, interface oxygen, porosity/tortuosity or D_s, repeated profiles in time, boundary-layer gradients, independent flux, or reduced-species fluxes. Require at least one measurement that gives physical concentration/length units and another that tests transport/sink assumptions.

Rubric: values/axes 2; flux and bounded inference 3; corrected provenance caption 3; measurements 2. Misconception prompt: "What would multiply the dimensionless curve into oxygen per volume?"

## O2-E02 expected response (15 points)

For unit sediment area, stored moles in a thin slab are phi C dx. Its rate of change is F(x) - F(x + dx) - phi kC dx (using local smooth values). Dividing by dx and taking its limit gives O2-Q01. With constant phi and D_s, substitute F = -phi D_s C_x and divide by phi to obtain C_t = D_s C_xx - kC. A porewater consumption rate q = kC must be multiplied by phi before insertion into the bulk balance. If demand instead were defined per sediment volume, its definition and cancellation would be different.

Units: C mol m^-3 water; phi C mol m^-3 sediment; F mol m^-2 sediment s^-1; q mol m^-3 water s^-1; R = -phi q mol m^-3 sediment s^-1; k s^-1; D_s m2/s; gradient C_x mol m^-4 water. Porosity remains in inventory M = integral_0^L phi C dx (mol m^-2 sediment) and physical flux F. Under the controlled baseline it does not alter the porewater profile.

The upper boundary prescribes interface concentration after a step. The bottom excludes diffusive flux across the chosen lower face. The interior starts without oxygen. There is no continuous initial corner at x = 0 and t = 0, which the numerical formulation must treat as a boundary step, not "fix" by pretending an initial steady profile.

Let a = L/ell. Differentiate O2-Q03:

$$C_x=-\frac{C_0}{\ell}\frac{\sinh((L-x)/\ell)}{\cosh a},\quad C_{xx}=\frac{C}{\ell^2}.$$

Because D_s/ell2 = k, D_s C_xx - kC = 0; C(0)=C_0 and C_x(L)=0. As k tends to zero, ell tends to infinity, both cosh terms tend to 1, and C tends to C_0. Finite-domain C(L)=C_0/cosh(a) is positive for finite positive inputs. C(L)=0 is a Dirichlet boundary and a different problem.

Rubric: slab derivation 4; units/volume basis 4; porosity and sign/conditions 3; analytic check and limit 4. Scientific gate: a positive consumptive bulk R or q inserted without phi in the bulk balance requires correction. Prompt: "Are the reaction units per water volume or total sediment volume?"

## O2-E03 expected response (20 points)

Checked run: Python 3.9.6, model code SHA256 is recorded in `provenance.json`. The model was independently rerun in an isolated output directory. All model assertions passed. The course checker independently compares the cosh formula to the verified model's exponential form, integrates the analytic sink by Simpson quadrature, and evaluates the sensitivity/fit tables. Full machine-readable evidence and runnable checker are in the instructor bundle.

Baseline ell = 0.010 m, Da = 9, diffusion scale L2/D_s = 900000 s (10.4167 days) and reaction scale 1/k = 100000 s (1.15741 days). Exact bottom C = 0.01986558548 mol/m3 water; M_ss = 0.001592087606 mol/m2; F(0) = 1.592087606e-8 mol/m2/s = 1.375563691 mmol/m2/day. Quadrature sink = 1.592087605899486e-8 mol/m2/s, relative difference from analytic flux 4.5014e-13.

Spatial study (direct discrete steady, no final-time error):

| N | Max absolute C error (mol/m3 water) | Error / C_0 | Order to next N |
|---:|---:|---:|---:|
| 20 | 0.0005065490592 | 0.002532745296 | 1.922799 |
| 40 | 0.0001335984115 | 0.0006679920576 | 1.962616 |
| 80 | 3.427638673e-05 | 0.0001713819337 | 1.981614 |
| 160 | 8.678999273e-06 | 4.339499637e-05 |  |

The steady flux-minus-sink maximum is 4.9565e-21 mol/m2/s. The script's acceptance bounds are 1.8 < observed spatial order < 2.2 and absolute steady budget residual < 1e-17 mol/m2/s.

Time study: N = 100, t = 20000 s, initial discrete steady state plus 0.02 sin(pi x/(2L)). This deliberately smooth initial state isolates time accuracy; it is not the startup condition. The exact semi-discrete eigenmode reference uses lambda_h = k + 4D_s/h2 sin2(pi h/(4L)).

| dt (s) | Max time error (mol/m3 water) | Order to next dt |
|---:|---:|---:|
| 1000 | 2.497275664e-05 | 0.994499 |
| 500 | 1.253407739e-05 | 0.997239 |
| 250 | 6.279042141e-06 | 0.998617 |
| 125 | 3.142531848e-06 |  |

The accepted time-order range is 0.95 to 1.05. The continuum reference at the fixed spatial grid plateaus near 2.20e-5 mol/m3, so a continuum comparison alone does not isolate time error.

Zero-interior startup at N = 80, dt = 1000 s:

| Final t (s) | Max error against analytic steady C (mol/m3 water) | Error / C_0 |
|---:|---:|---:|
| 10000 | 0.07864734208 | 0.3932367104 |
| 100000 | 0.01351627898 | 0.06758139489 |
| 1000000 | 3.427809325e-05 | 0.0001713904663 |

These are errors against a steady target, combining equilibration and grid/time effects, not standalone time-accuracy estimates. At the longest startup run, maximum instantaneous balance residual is 2.9977e-21 mol/m2/s; cumulative residual is 3.8164e-16 mol/m2. Code tolerances are < 1e-17 for instantaneous and < 1e-13 for cumulative balance, with nonnegative concentrations and maximum <= C_0 + 1e-14. The global reported minimum zero includes the initial state. The k = 0 uniform-steady check uses absolute concentration tolerance < 1e-12 mol/m3. For course hand calculations, allow 0.5% relative rounding error for nonzero reference values; qualitative claims, signs, units and absent crossings still need to be exact.

The exact steady upper flux and inventory are

$$F(0)=\phi D_s(C_0/\ell)\tanh(L/\ell),\quad F(L)=0,$$

$$M_{ss}=\phi C_0\ell\tanh(L/\ell).$$

The integrated consumption is S = integral_0^L phi kC dx = k M_ss = F(0). In startup the correct instantaneous identity is dM/dt = F(0,t) - F(L,t) - S(t). The cumulative identity integrates all three rates over elapsed time. A small cumulative mass residual demonstrates discrete bookkeeping, not temporal accuracy or mechanism validity. Units for M are mol/m2, for F and S mol/m2/s.

Accept numerical/reference comparisons at identical cell locations, with the reported normalization. A cell-centred FV concentration must not be mislabeled as a boundary sample at x = 0. Require spatial refinement with the same physical final time and control of temporal/equilibration error; require a separate time-step comparison to an appropriate transient reference. Backward Euler can be stable with a time step that is too large for accurate dynamics.

A k = 0 check should tend to uniform C_0 with this fixed-top, no-flux-bottom configuration. Positivity is expected for nonnegative inputs and these conditions. Finite k generates a smooth positive tail, not an exact anoxic front. Explain that analytic-limit and convergence checks verify the solver; independent field observations address model validity.

Rubric: reproducibility/provenance 3; matched-position profile/error 4; spatial and temporal study interpretation 5; units/conservation 5; limit/positivity vs field validity 3. Exported-results route can earn full reasoning credit, but must explicitly state no independent solver execution. Prompt: "Could your small steady error coexist with a wrong response time?"

## O2-E04 expected response (15 points)

Checked by `check_teaching.py` using the accepted finite-domain solution. Fluxes and profiles refer to each case's own physical inputs, with phi held independent of D_s for the stated controlled test. A blank threshold means "not reached in the domain", not zero.

Concentration comparison. The columns use ell in mm and C(10 mm) in mol/m3.

| Case | ell | C(L)/C_0 | C(10 mm) |
|---|---:|---:|---:|
| baseline | 10.000000 | 0.099327927 | 0.074738220 |
| double_k | 7.071068 | 0.028733259 | 0.048783139 |
| double_Ds | 14.142136 | 0.236350243 | 0.102962842 |
| double_C0 | 10.000000 | 0.099327927 | 0.149476440 |
| phi_0.6_Ds_fixed | 10.000000 | 0.099327927 | 0.074738220 |
| L_equals_ell0 | 10.000000 | 0.648054274 | 0.129610855 |
| double_L | 10.000000 | 0.004957474 | 0.073578776 |

Flux and threshold comparison. Flux units are shown in the headings; threshold depth is in mm. Blank cells retain the meaning "not reached in the domain".

| Case | F(0) (mol/m2/s) | F(0) (mmol/m2/day) | 5% depth |
|---|---:|---:|---:|
| baseline | 1.59208761e-08 | 1.375563691 |  |
| double_k | 2.26180745e-08 | 1.954201634 | 21.854707 |
| double_Ds | 2.19863354e-08 | 1.899619378 |  |
| double_C0 | 3.18417521e-08 | 2.751127383 |  |
| phi_0.6_Ds_fixed | 1.1940657e-08 | 1.031672769 |  |
| L_equals_ell0 | 1.21855065e-08 | 1.052827761 |  |
| double_L | 1.59998034e-08 | 1.382383013 | 29.981929 |

For baseline, the exponential shortcut would predict 29.9573 mm for a 5% crossing. That shortcut is invalid here: the sealed bottom remains at 9.93279% and no 5% crossing occurs. The double-k and 60 mm cases do cross the threshold, at 21.85471 and 29.98193 mm respectively. At L = 10 mm the bottom remains at 64.80543%; the boundary choice visibly affects the near-surface profile. A 1 micromol/L absolute threshold is also not reached in the baseline. Allow 0.5% rounding tolerance on nonzero numeric values, but absence/existence of crossing must be correct.

Use finite-domain flux formula, not only F proportional to sqrt(k D_s): tanh(L/ell) changes when k or D_s changes. Doubling k divides ell by sqrt(2); doubling D_s multiplies ell by sqrt(2). Doubling C_0 doubles absolute C and F, with identical C/C_0 and ell. Holding D_s fixed while setting phi = 0.6 leaves C and ell unchanged but scales physical flux and bulk inventory by 0.6/phi_baseline. Real porosity and diffusivity may covary; this exercise holds them independently to expose the algebra.

For eta = 0.05, threshold exists inside [0,L] only if eta >= 1/cosh(L/ell), with equality at L. Its location is

$$x_\eta=L-\ell\operatorname{acosh}[\eta\cosh(L/\ell)].$$

At a shallow lower boundary, the finite profile can remain above the threshold throughout. A deeper domain approaches the exponential near-surface limit. Extending the domain tests the chosen closure; it does not validate the sink.

Relative threshold x_eta is unchanged by multiplying C_0. With a fixed absolute detection threshold C_det, eta = C_det/C_0 changes when C_0 changes. Doubling C_0 lowers eta and can move the absolute detection depth deeper; a finite bottom may prevent a crossing. Avoid describing threshold movement as appearance of an exact zero front.

Rubric: predictions visible before calculations and correct controlled changes 3; finite-domain numbers with units 6; domain comparison 3; threshold existence and interpretation 3. Prompt: "Is your detector threshold a fraction of the interface value or a fixed concentration?"

## O2-E05 expected response (20 points)

Dataset is the verified model's seeded ten-point analytic profile plus independent Gaussian noise, sigma = 0.002 mol/m3. Its generating alpha is 10000 m^-2, seed 20261010. With C_0 = 0.2 and L = 0.03 fixed, minimize SSE(alpha) = sum_j [C_model(x_j; alpha) - C_synthetic,j]^2 over alpha in [100, 1e6] m^-2. The scientist uses a golden-section search in log(alpha); a sufficiently fine transparent spreadsheet search is acceptable.

Reference alpha_hat = 9671.840685391 m^-2, point recovery error = -3.281593%. At independently fixed D_s = 1e-9 m2/s, conditional k_hat = 9.671840685e-06 s^-1. SSE at the fit = 2.603122386e-05 mol2/m6; SSE at generating alpha = 3.891443004e-05; RMSE over ten points = 0.00161341947 mol/m3. Residual convention is model minus synthetic, not the reverse.

| x (mm) | Fitted C (mol/m3) | Residual (mol/m3) |
|---:|---:|---:|
| 3 | 0.149227746 | 0.002497491 |
| 6 | 0.111539754 | -0.001233663 |
| 9 | 0.083631549 | -0.002340772 |
| 12 | 0.063056144 | 0.000335590 |
| 15 | 0.048009491 | 0.001368094 |
| 18 | 0.037172301 | -0.000821563 |
| 21 | 0.029594372 | 0.002870078 |
| 24 | 0.024611273 | -0.001139776 |
| 27 | 0.021786085 | 0.000097629 |
| 30 | 0.020871098 | -0.000766412 |

For spreadsheet point fitting allow 0.5% relative error in alpha, provided the objective and residual pattern are consistent. More accurate methods should approach the reference rather than use this tolerance as a search width. The supplied parametric bootstrap (200 replicates) reports approximate 95% percentile bounds [9372.17710, 10033.39587] m^-2, conditional on known C_0,L,sigma and an exact first-order model. It is not field uncertainty. A 200-replicate Monte Carlo interval has sampling variability and is not exact coverage. The local log-alpha standard-error estimate is 0.0184681. Students may report the -3.28159% recovery error and a controlled perturbation instead of interpreting the bootstrap.

With illustrative independently uncertain D_s in [0.5, 2]e-9 m2/s, the fitted point implies k in [4.83592e-6, 1.93437e-5] s^-1 before combining profile uncertainty. This range is a sensitivity bound, not a statistical confidence interval. The original generating pair (1e-9 m2/s, 1e-5 s^-1) and doubled pair (2e-9 m2/s, 2e-5 s^-1) produce exactly the same finite-domain steady concentrations, but doubled physical flux and faster transient response.

A normalized steady profile is determined by L and alpha = k/D_s. For identical L,C_0, replacing (D_s,k) with (2D_s,2k) leaves alpha and ell unchanged, so the concentrations coincide. Physical flux doubles because F includes D_s; bulk steady inventory is unchanged for fixed phi. The transient operator doubles, so the response progresses on half the time scale for matched initial/boundary histories scaled in time. This distinction is the reason transient observations or independent flux and transport information can add identifiability.

An independently measured D_s converts fitted alpha into k = alpha D_s. An independent steady physical flux with known phi and C_0 can also constrain D_s through the known gradient. A measured transient response can constrain the transport-reaction time scale if boundary forcing is known. Accept any coherent option with identified nuisance quantities; do not accept "take more points on the same normalized steady profile" as automatically resolving the structural ambiguity.

Synthetic perturbations are deliberate teaching variability, not established sensor error, spatial representativeness or field process variability. A fit to synthetic data does not measure biological respiration. A recovery error or sensitivity range is not a confidence interval. Field use also requires surface/bottom conditions, porosity/tortuosity, spatial sampling, other oxygen sinks and model discrepancy to be considered.

Rubric: data labeling/plot 3; objective, fit and residuals 6; parameter-pair demonstration and changing flux/transient 5; uncertainty distinctions 3; informative measurement 3. Prompt: "Which combination of parameters appears in the steady equation after dividing by D_s?"

## O2-E06 expected response (15 points)

The checked publisher abstract of Gundersen and Jorgensen (1990), doi:10.1038/345604a0, challenges one-dimensional flat-interface transport/area accounting for that measured coastal geometry. About 2.5 is the study's reported three-dimensional-to-simple-one-dimensional flux ratio, not a correction transferable to all sediment or to the module's synthetic baseline. Only the abstract was inspected for this task; no detailed methods appraisal or digitized dataset is claimed.

Accept mapping of interface microtopography with spatially resolved oxygen/DBL gradients, repeated profiles across multiple surface positions, or a direct independent area-integrated flux for comparison. A spatially uniform boundary and near-equal three-dimensional and vertical flux estimates within measurement uncertainty would support retaining 1D for that application; strong lateral gradients, burrows or area discrepancies would motivate a spatial/transport revision. The test should be specified before judging agreement.

The quoted claim conflates four different steps: numerical verification (analytic/conservation/convergence), synthetic parameter recovery (fitting), independent validation (held-out field concentration/flux/transient prediction), and oxygen-sink attribution (further chemistry/biology/process evidence). Reserve an independent field profile at another time or depth/position, an independently measured flux, or a transient perturbation response that was not used to fit alpha. State how the model would predict it with measured boundary inputs and how residuals plus uncertainty would be assessed. Do not claim this pilot has performed such validation.

A finite diffusive boundary layer can make interface C_0 lower than bulk overlying-water oxygen and variable with flow. Measure water-side and interface concentrations/gradients over the relevant time window before equating the two or changing the model. Boundary data can resolve a false input assumption without immediately expanding the rate law.

Rubric: challenged assumption and no universal factor 4; discriminating observation 4; verification/fitting/validation/attribution with held-out test 5; boundary test 2. Scientific gate: any claim that schematic or synthetic agreement establishes field validity requires correction.

Optional E06 measured-summary extension is ungraded in the core 100-point module. It requires approximately 20 to 30 additional minutes, an estimate to test. Use the verified model's separately pinned task and solutions; do not give students the solution file. C6 July 2019 v2 DOU/TOU = 0.289074756. The model's illustrative flux is 1.37556369 mmol/m2/day, whereas archived v2 C6 DOU is 7.26378779 mmol/m2/day. Unequal inputs and observables prevent interpretation as a validation result or fitted k. Neither archived workbook contains concentration-depth profiles. The full version/reconciliation caveats belong to that scientist handout; do not silently apply publication corrections or treat missing values as zero.

## O2-E07 expected response (5 points)

At the new steady state, linearity with fixed k, D_s, phi and L makes C and the downward surface flux exactly one-half of their old steady values. The normalized profile and its relative 5% depth are unchanged. A fixed absolute threshold corresponds to a larger fraction of the new C_0 and may cross at a shallower depth, or be exceeded nowhere if the new interface is already below it. Immediately after the boundary step, the interior has not halved. The transient must redistribute stored oxygen; the top flux need not be half or even downward during the earliest adjustment. The old steady profile is not an initial zero profile for this event.

Relevant timescales include 1/k and L2/D_s, with the finite-domain slowest linear relaxation time [k + D_s(pi/(2L))2]^-1. This is an optional stronger answer, not required for the five-point memo. Distinguish rough scales from a statement that the system reaches exact steady state in one such interval. Repeated oxygen profiles and independently logged interface supply could reveal variable demand, advection/irrigation or an incorrect boundary forcing.

Rubric: eventual exact scaling 2; transient distinguished 1; threshold contrast 1; conditional observation/limit 1. Do not require a new solver run. Prompt after scoring: "Which stored oxygen has changed at the instant the boundary changes?"

## Evidence and teaching revision

Use pilot-protocol-en.md only after the English/Russian packets and model are accepted and willing learners are available under authorized access. Record actual first attempts, assistance and timing. No pilot has been executed and no learning gain is inferred from these answer keys. Translations retain exercise IDs, equations, numeric tolerances and data-provenance limitations. Any model change invalidates dependent numerical keys until reconciled and rechecked.
