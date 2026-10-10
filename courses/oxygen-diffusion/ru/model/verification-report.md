# Numerical verification report v1

Run on 2026-10-10 with Python 3.9.6, standard library only. Machine-readable evidence: `results/verification.json`. Re-run `python3 oxygen_model.py --out results`.

## Grid convergence against the analytic steady solution

| Cells | Max concentration error, mol m⁻³ water | Successive order |
|---:|---:|---:|
| 20 | 5.06549059 × 10⁻⁴ | |
| 40 | 1.33598412 × 10⁻⁴ | 1.92280 |
| 80 | 3.42763867 × 10⁻⁵ | 1.96262 |
| 160 | 8.67899927 × 10⁻⁶ | 1.98161 |

Errors compare centre values at identical depths. Observed order approaches two. The maximum steady flux-minus-integrated-sink residual among these runs is 4.96 × 10⁻²¹ mol m⁻² s⁻¹. Accuracy errors are much larger than accounting residuals, so balance alone would not demonstrate accurate profiles.

## Time convergence with an exact discrete eigenmode

At 100 cells, initial condition Cᵢ = C*ᵢ,discrete + 0.02 sin(πxᵢ/(2L)). The continuous boundary conditions are compatible with this smooth mode. For the discrete operator the exact eigenvalue is λ_h = k + 4Dₛ/h² sin²(πh/(4L)). The independent exact decay is exp(−λ_h t). Compare at t = 20000 s.

| Time step, s | Max concentration error, mol m⁻³ water | Successive order |
|---:|---:|---:|
| 1000 | 2.49727566 × 10⁻⁵ | |
| 500 | 1.25340774 × 10⁻⁵ | 0.99450 |
| 250 | 6.27904214 × 10⁻⁶ | 0.99724 |
| 125 | 3.14253185 × 10⁻⁶ | 0.99862 |

This isolates time discretization and verifies first-order backward Euler. Comparison against the continuum smooth solution instead reaches a spatial-error plateau around 2.20 × 10⁻⁵ at this fixed grid. Do not infer failed time convergence from that plateau or silently treat the discrete benchmark as a continuum benchmark.

## Analytic limits and input behavior

Runnable assertions check: k = 0 gives a uniform steady profile; Dₛ = 0 gives independent backward-Euler decay with continuum error decreasing on time refinement; k → 0 gives the uniform limit; a deep domain gives the exponential; doubling C₀ doubles concentration; scaling Dₛ,k together leaves steady concentrations unchanged. Invalid negative or nonfinite coefficients, invalid porosity and invalid initial arrays raise errors.

## Transient oxygen balance and positivity

The step initial condition is run at N = 80, Δt = 1000 s to t = 10000, 100000 and 1000000 s. Across these runs the maximum instantaneous residual is 3.00 × 10⁻²¹ mol m⁻² s⁻¹. At the longest run the cumulative residual M_final − M_initial − cumulative_inflow + cumulative_consumption is 3.82 × 10⁻¹⁶ mol m⁻². Interior concentrations remain nonnegative (the reported global minimum includes the initial zero state), and never exceed C₀. No values are clipped. The longest-run final inventory is 0.00159180239 mol m⁻², close to the analytic steady 0.00159208761 mol m⁻², with both finite time and grid error.

The initial corner discontinuity is not used to claim a time order. The no-flux lower boundary and the top half-cell coefficient are tested through their analytic steady solution and global balance. These results apply to the stated constant-coefficient first-order system. No nonlinear extension, heterogeneous system or empirical prediction has been validated here.
