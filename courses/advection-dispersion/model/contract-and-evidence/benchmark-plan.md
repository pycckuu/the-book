# Verification plan, not verification results

AD-CONTRACT-0.1. None of the following cases has been implemented or executed. Proposed tolerances are acceptance targets, not measured errors. Editor must accept the contract before solver construction. Keep a machine-readable verification report later, with inputs, actual outputs and failures.

## Mandatory cases

B01. Zero feed, zero initial concentration, any proposed nonnegative k and positive u,D_L: all states and all budget entries stay zero. Test input validation, including negative coefficients and invalid phi. Passing the zero solution alone is insufficient.

B02. Conservative constant feed: k=0. Compare the directly solved discrete steady system with the uniform continuum C_ref, and inlet with advective outlet. This checks boundary assembly and avoids mistaking an unfinished transient for spatial error. The general k>0 steady solve follows separately.

B03. Reactive finite steady profile: use the two-characteristic-root construction with actual inlet/outlet boundaries. Compare cell averages and outflow; check the continuum integral independently. Refine N=50,100,200,400 at fixed physical coefficients. Expected asymptotic coupled spatial order is approximately one, not two. For an isolated smooth dispersion-only periodic test, expect approximately two. A direct steady solve is permitted only after the gate, like the transient solver.

B04. Smooth time accuracy: use the separate periodic cosine/reference in analytical-checks.md, at one fixed grid, for k=0 and k>0. Compare with its exact semidiscrete solution and refine aligned Delta t values. Target first-order temporal convergence, separate from the continuum spatial discrepancy. Also compare against the continuum mode to show a fixed-grid error plateau.

B05. Finite pulse budget: initially zero, core flux inlet and advective outlet, k=0 then positive k. Accumulate exact injected amount, discrete export, discrete disappearance and remaining storage using the update's own time rule. Report both each-step and cumulative residual. Extend the washout interval when claiming nearly complete recovery, and quantify remaining inventory. A balance can pass while the curve is too broad: this case must not substitute for B06.

B06. Numerical spreading and limiting transport: D_L=k=0 auxiliary delayed-pulse comparison; independently use the smooth periodic mode to measure artificial amplitude decay against the no-spreading continuum. Refine h at small time error and Delta t at fixed h. Compare the observed smooth long-wave behavior to u*h/2+u^2*Delta t/2 as a diagnostic, not a fitted physical dispersion. Report mass, location, width or mode amplitude and phase. Do not hide diffusion by setting a coarser-grid D_L to a smaller value.

B07. Domain and closure sensitivity: repeat a continuous-feed and a pulse calculation with L changed, keeping u,D_L,k and the physical feed duration fixed. Compare internal profiles before the pulse interacts appreciably with the farther exit. Quantify changes rather than asserting a finite boundary is irrelevant. Distinguish this sensitivity study from convergence to a single specified boundary-value problem. Do not compare different pulse durations unknowingly by holding T_p/tau_a constant while changing L.

B08. Porosity/velocity and limiting checks: at independently fixed u,D_L,k the concentration is independent of constant phi, whereas inventory and flux scale with phi. At fixed measured Darcy flux, changing phi changes u and thus transit time: test these as different cases. Check k->0 against the conservative model. Set u=0 with this flux inlet only for a closed initial-inventory diffusion/decay test; it has no fed input and is not the oxygen surface-concentration case. A separate uniform closed reaction test has C=C_initial*exp(-kt); backward Euler should converge to this ODE solution.

## Proposed measurable acceptance thresholds

- Scaled linear residual <=10^{-12} and scaled discrete each-step/cumulative budget residual <=10^{-10}, using sum of absolute input/export/loss/storage terms plus an explicitly stated nonzero reference amount. Report absolute residuals as well; the all-zero case needs an absolute branch. Do not equate these algebraic tolerances with accuracy against the PDE.
- No unreported negative concentrations, clipping or mass correction. Proposed diagnostic roundoff threshold is 10^{-12} times C_ref or the declared initial concentration scale. Preserve and report the actual minimum even if within tolerance; values below the threshold fail. For the nonnegative bounded feed, also inspect overshoot relative to max(initial,C_ref).
- For nonzero smooth-reference errors before roundoff or contamination, adjacent-refinement orders should approach 1; propose [0.8,1.2] for sufficiently refined coupled spatial and semidiscrete temporal comparisons. The optional smooth isolated dispersion space test targets [1.8,2.2]. Report the complete errors and orders; no forced pass at the coarsest grids or at zero error.
- Final teaching resolution must change the documented outlet peak/time/profile diagnostics by less than 2% under independent grid/time refinement, with a specified absolute criterion for quantities near zero. Exact scalar tolerances will be finalized with observables after contract acceptance. No default grid is scientifically accepted now.
- For diagnosing dispersive accuracy at nonzero D_L, initially require the long-wave artificial-diffusion estimate <=5% of D_L. This is a resolution heuristic to verify, not a proof of total error <=5%. At D_L=0 the ratio is undefined; show decreasing artificial spreading instead.

## Candidate parameter and resolution design

Use model-contract.md candidate scales at Pe=10 and Da_a=0 or 1. Proposed pulse end is 0.2*tau_a; a starting observation window is 3*tau_a, subject to a remaining-inventory check. All are illustrative.

Proposed smooth refinement family: N=50,100,200,400 and Delta t=1000,500,250,125 s, with grid-only and time-only comparisons rather than only paired refinement. These values align with the proposed pulse endpoint. For a formal time-order demonstration, use the periodic smooth test and its semidiscrete reference. Do not infer two independent orders from one diagonal path through (h,Delta t).

Optional Pe=1 and Pe=100 comparisons change D_L at fixed L,u; optional Da_a=10 changes k. High Pe must be presented as an accuracy stress test. The preceding grid family is not guaranteed to resolve Pe=100: u*h/(2D_L)=Pe/(2N) alone shows the limitation. For a 5% combined long-wave heuristic, one tentative Pe=100 pair is N=2000 and Delta t=50 s at the proposed L,u; these are draft resolution inputs, not a completed cost/accuracy claim. Do not enlarge the core workload to implement a different transport theory.

## Reporting and validation boundary

The future report should store contract version, code hash, all coefficients and volume bases, feed schedule, IC/BC, grid/time scheme, reference type, cell-average comparison, numerical minima/maxima, linear and mass residuals, cumulative storage/export/loss, refinement errors/orders and observed spreading. Tag core pulse versus auxiliary periodic, zero-dispersion or closed tests. No future report may call these empirical validation.

A data-comparison task can first use explicitly synthetic arrival/flux records generated by an accepted model, while keeping a held-out numerical perturbation distinct from independent nature. If field or column data are later selected, freeze raw files, DOI, units, concentration sampling mode, flow/porosity, injection/recovery protocol, missing data and uncertainties before fitting. This gate has not downloaded or selected a calibration dataset.
