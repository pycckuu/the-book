# Verification methods supplied to learners

The source code is the verified model's cell-centred finite-volume, backward-Euler model. Code `D` denotes D_s. Report concentrations are at cell centres, not boundary faces. Half-cell distance is used at the fixed top, zero flux at the bottom.

The spatial study directly solves the discrete steady problem at N = 20,40,80,160 and compares centre values to the continuous analytic steady solution. Its order acceptance is 1.8 to 2.2. It has no finite-time equilibration error.

The separate time study uses N = 100 and a smooth initial state: discrete steady concentration plus 0.02 sin(pi x/(2L)). It compares to the exact semi-discrete eigenmode at t = 20000 s with dt = 1000,500,250,125 s. Its order acceptance is 0.95 to 1.05. A continuum reference at fixed N also includes spatial error. This is different from the zero-interior boundary-step startup; the discontinuous startup corner is not used to claim a smooth time order.

Assertions check k = 0 uniform steady, D_s = 0 pure decay, small-k and deep-domain limits, surface scaling, common D_s/k scaling invariance and invalid-input rejection. Instantaneous discrete oxygen-budget residual must be less than 1e-17 mol/m2/s and cumulative startup residual less than 1e-13 mol/m2. Positivity is checked without clipping; startup concentrations must not exceed C_0 + 1e-14. Limit comparisons have their own tolerances in the source. Stability alone does not verify accuracy.

All teaching inputs and fitting observations are synthetic. Numerical verification is not empirical validation. The code prints a fit benchmark; students must still reconstruct its objective, residuals and inference limits for E05.
