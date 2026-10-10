# Numerical verification report

AD-NUMERICS-1. All current targets PASS. Results/verification.json records actual inputs, outputs, errors and failures. This is numerical verification, not validation against independent natural observations. Proposed teaching defaults and exercise values still require Editor acceptance. All coefficients and observations are synthetic.

## Reference and convergence evidence

B01 rejects 14 invalid-input cases and preserves the zero solution; the all-zero budget uses an absolute branch. B02 conservative finite steady profiles are uniform. B03 compares reactive cell averages with the actual finite flux-inlet/open-exit solution.

Finite steady spatial orders at N=50,100,200,400: 0.980704, 0.990331, 0.995160. Independent continuum flux-minus-integrated-sink residual: -2.118e-22 mol m^-2 s^-1. No oxygen cosh or semi-infinite concentration-inlet reference was substituted.

At periodic N=64, k=0.0 s^-1 and dt=1000,500,250,125 s, semidiscrete temporal orders are 0.973003, 0.985896, 0.992903. At dt=5 s, semidiscrete error is 3.06261e-05 whereas continuum error remains 0.00672712 mol m^-3. Time refinement cannot eliminate fixed spatial error.
At periodic N=64, k=1e-05 s^-1 and dt=1000,500,250,125 s, semidiscrete temporal orders are 0.974867, 0.987185, 0.993432. At dt=5 s, semidiscrete error is 3.33093e-05 whereas continuum error remains 0.00550804 mol m^-3. Time refinement cannot eliminate fixed spatial error.

Isolated periodic dispersion continuum-error orders: 1.962555, 1.966141, 1.897834. dt=1 s time error is nonzero and starts to contaminate the finest error. This is a controlled approximate second-order dispersion check, not a second-order claim for coupled upwind transport.

Smooth pure-advection measured artificial-diffusion/leading-estimate ratios at N=40,80,160,320: 0.997896, 0.999461, 0.999859, 0.999962. Separate grid/time refinements reduce artificial spreading. u*h/2+u^2*dt/2 is a long-wave backward-Euler diagnostic, not exact physical dispersion or a universal discontinuous-front error formula.

Auxiliary hyperbolic positive-loss export fraction: 0.368338812, versus exp(-kL/u)=0.367879441. Hyperbolic profile L1 errors include phi, have mol/m2 bulk-area units and decrease with refinement; no smooth pointwise order is asserted.

B07 quantifies changed-domain pulse and constant-feed sensitivity while retaining the physical pulse duration and common h. It does not assert that the finite exit is irrelevant. B08 fixed-u porosity variation leaves C unchanged and scales inventory/export. At fixed Darcy flux, changing phi changes u and C. Simultaneous steady rescaling of u,D_L,k changes C by 0, confirming a concentration-only steady inference ambiguity. Closed uniform decay agrees with its backward-Euler closed form and converges to exp(-kt).

## Proposed teaching default

N=400, dt=100 s, observation window 600000 s. All four core cases independently pass N=800 at fixed dt and dt=50 s at fixed N. Metrics/floors were declared before solving in metric-definitions.json. Fixed-snapshot profile and outlet peak/quantile/width changes meet the declared 2% scale-aware targets; recovery/loss/storage fraction changes meet absolute 0.005. Actual values, controls, thresholds and pass flags are in independent-refinement.csv. The long-wave artificial-diffusion heuristic is <=5% of physical D_L in every core case; this is not proof of universal 5% PDE error.

| Scenario | Peak C (mol/m3 water) | t50 (s) | Export/input | Disappearance/input | Storage/input at end |
| --- | ---: | ---: | ---: | ---: | ---: |
| conservative | 0.223666517 | 102018.564 | 0.999999729 | 0 | 2.71053788e-07 |
| reactive | 0.107993746 | 89707.2784 | 0.397559419 | 0.602440581 | 7.66327085e-10 |
| faster-flow | 0.517012054 | 58033.1258 | 1 | 0 | 9.61531271e-25 |
| more-dispersion | 0.192999537 | 96776.7124 | 0.999967533 | 0 | 3.2466868e-05 |

t50 and temporal width condition on exported mass during the reported window. Flux-normalized exit and resident exit coincide in the imposed continuum closure; terminal cell average approximates the exit trace. At 600000 s all retained fractions are below the proposed 0.001 threshold. Extension to 800000 s preserves declared timing/width/fraction targets for all cases. No finite window is labeled exactly complete washout. Faster-flow input is 0.12 mol/m2; other cases 0.06 mol/m2. Physical T_p stays 20000 s.

## Algebra, positivity and independent table readback

Largest core scaled linear residual: 2.026e-16. Largest scaled cumulative update-budget residual: 9.846e-13. The nonzero amount scale is phi*L*C_ref=0.30 mol/m2. Actual global minimum is zero, including initial states; negative-value counts are zero. No clipping or post hoc mass correction was applied. Budget/positivity alone do not establish PDE accuracy.

B05 also tests a dt=7000 s step crossing T_p=20000 s, preserving exactly the overlap input. readback_exports.py independently reconstructs saved CSV increments, mass ledgers, profile storage, face component sums, raw synthetic interval observations and RMSE without invoking the solver. Results/export-readback.json is PASS and records actual discrepancies. Different summation orders slightly change absolute cumulative residuals; both remain reported.

## Failed attempt and correction

First run failed B04: the auxiliary cyclic Thomas rank-one construction swapped its first/last advection corner coefficients. Its matrix residuals were large and time refinement did not approach the specified semidiscrete solution. Correct alpha/beta placement restored the reference; B06 additionally checks periodic mean and residual. The finite-column solver uses a different tridiagonal path and was unaffected. The original FAIL report and exact source are retained in run-history/attempt-01-source. The next PASS source is preserved under attempt-02-source; the final PASS additionally corrects the hyperbolic L1 volume basis, checks steady scale/domain behavior and exports steady references. No failed tolerance was relaxed.

The initial 400000 s window left the more-dispersion retained fraction above the effectively-complete threshold. Final outputs extend to 600000 s and check 800000 s. The earlier short-window evidence remains in the first run report. Finite-window exports were not silently labeled complete recovery.

## Synthetic inference and scientific limits

Eight noiseless interval-average outlet observations use current code at N=800, dt=50 s. Candidates use N=400, dt=100 s with k=0,1e-5,2e-5 s^-1 and all other physical inputs known. The matching-k residual is small and nonzero because the grid differs. Raw generating series, units, support and hashes are supplied. No measurement sigma, confidence interval, optimizer, global-identifiability proof or empirical fit is claimed.

- k0: RMSE 0.0745291496 mol/m3 water.
- k1: RMSE 0.000266739245 mol/m3 water.
- k2: RMSE 0.0314275984 mol/m3 water.

No field dataset, aquifer validation, learner trial, optional high-Pe expansion, coupled microbial mechanism, elemental reaction balance or water-safety claim is supplied. Constant D_L/single mobile region remain closure assumptions; k aggregates parent loss. P02 is checked pore-scale numerical evidence for a bounded transfer critique, not field validation of this teaching model.
