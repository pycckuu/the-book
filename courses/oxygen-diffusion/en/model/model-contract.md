# Oxygen diffusion and consumption: scientific contract v1

Date: 2026-10-10. Base manuscript revision: `10119d526cb96b5ad8f065bef07a93c0ce0240ed`.
Status: numerical verification completed; empirical validation has not been performed.

## Observable and assumptions

The observable is dissolved oxygen concentration against depth and time in fully water-saturated sediment. Oxygen enters at the upper interface, diffuses through the porewater, and is consumed. The pilot treats a homogeneous, dark sediment with constant water-filled porosity, diffusivity and aggregate first-order consumption coefficient. It omits porewater flow, compaction, bioirrigation, photosynthesis, explicit biomass, and dissolved donors/products. These are deliberate closure assumptions, not conclusions about every sediment.

The model describes oxygen accounting only. It does not conserve a complete carbon, nitrogen, sulfur or electron network because those species are absent. A possible balanced organic-matter reaction is CH₂O + O₂ → CO₂ + H₂O, with one mole O₂ per mole of formal CH₂O. That stoichiometry is not evidence that every oxygen sink follows this reaction. Do not convert model consumption into carbon mineralization without an independently supported reaction mixture and respiratory quotient.

## Notation and dimensions

| Symbol | Definition | SI unit |
|---|---|---|
| x | Depth, positive downward from sediment-water interface | m |
| t | Time | s |
| C | Dissolved O₂ per volume of porewater | mol m⁻³ water |
| φ | Water-filled pore volume / bulk sediment volume | dimensionless |
| Ĉ = φC | Oxygen inventory per bulk sediment volume | mol m⁻³ sediment |
| Dₛ (code D) | Tortuosity-corrected porewater diffusivity, with no porosity prefactor built in | m² s⁻¹ |
| k | Aggregate first-order oxygen consumption coefficient | s⁻¹ |
| q = kC | Positive oxygen consumption per porewater volume | mol m⁻³ water s⁻¹ |
| R = −φq | Signed source per bulk sediment volume | mol m⁻³ sediment s⁻¹ |
| F = −φDₛ Cₓ | Flux per bulk cross-sectional area, positive downward | mol m⁻² sediment s⁻¹ |
| L, C₀ | Domain depth and fixed interface concentration | m, mol m⁻³ water |

Distinguish Dₛ from an alternative bulk coefficient D_eff = φDₛ. With D_eff use F = −D_eff Cₓ, without multiplying by φ again. For spatially varying φ or Dₛ retain the conservative divergence, rather than cancelling factors across derivatives.

Units: 1 mol m⁻³ = 1 mmol L⁻¹ = 1000 µmol L⁻¹. 1 µM = 0.001 mol m⁻³. 1 m² s⁻¹ = 10⁴ cm² s⁻¹. Convert mol m⁻² s⁻¹ to mmol m⁻² d⁻¹ by multiplying by 1000 × 86400. Concentrations in µM are amounts per litre of water, not per litre of bulk sediment.

## Balance, boundaries and initial condition

\[
\frac{\partial(\phi C)}{\partial t}=-\frac{\partial F}{\partial x}-\phi kC,
\qquad F=-\phi D_s\frac{\partial C}{\partial x}.
\]

For constant φ > 0 and Dₛ this reduces to Cₜ = DₛCₓₓ − kC on 0 < x < L.

Top: C(0,t) = C₀ for t > 0. Bottom: Cₓ(L,t) = 0, a sealed reflecting boundary. Interior initial condition: C(x,0) = 0. The instantaneous top step is discontinuous at (0,0), which is acceptable for this diffusion initial-boundary problem. Do not claim smooth-solution time convergence at that corner. The verification therefore uses a separate smooth analytic eigenmode for the time-order check.

The imposed C₀ is concentration at the sediment surface. Equating it to bulk overlying-water oxygen neglects a diffusive boundary layer. If the boundary layer matters, a Robin condition F(0) = h_m(C_water − C_surface) is an extension requiring a mass-transfer coefficient h_m [m s⁻¹]. A bottom no-flux boundary is a modeling choice that needs sensitivity checking, not a measured condition.

## Transparent first-order closure

q = kC is a minimal effective sink with no independently resolved biomass or donor. If a Monod oxygen-limited consumption law were q = q_max C/(K_O + C), its low-C limit would have k = q_max/K_O, conditional on fixed donor and biomass. This does not establish that the whole depth profile is in that limit. The nonlinear law is not implemented or validated in this packet. Identifying q_max and K_O requires observations spanning the transition around K_O; low-C observations identify only their ratio.

## Analytic predictions and limits

For Dₛ > 0, k > 0, define ℓ = √(Dₛ/k):

\[
C_*(x)=C_0\frac{\cosh((L-x)/\ell)}{\cosh(L/\ell)},\quad
F_*(0)=\phi C_0\sqrt{D_s k}\tanh(L/\ell),\quad
M_*=\phi C_0\ell\tanh(L/\ell).
\]

Direct differentiation verifies DₛC*ₓₓ = kC*, C*(0) = C₀ and C*ₓ(L) = 0. Integration verifies F*(0) = φk∫C*dx = kM*. In the deep-domain limit C* = C₀ exp(−x/ℓ). In the k → 0 limit C* = C₀ and F* = 0. With Dₛ = 0 the interior follows C = C_initial exp(−kt), independent of the disconnected top. The code uses an equivalent exponential form of the steady solution to avoid cosh overflow.

Dimensionless variables ξ = x/L, τ = tDₛ/L², c = C/C₀ give c_τ = c_ξξ − Da c, with Da = kL²/Dₛ. Diffusion time L²/Dₛ competes with reaction time 1/k. Doubling k at fixed Dₛ reduces ℓ by √2; multiplying C₀ scales concentration and flux proportionally. Changing constant φ scales inventory and flux but not the concentration solution.

The steady first-order profile is strictly positive at every finite depth if C₀ > 0. An operational oxygen penetration depth requires a specified concentration threshold. For a deep exponential domain x_det = ℓ ln(C₀/C_det), if C_det < C₀. For the finite sealed domain there may be no threshold crossing at all. Do not clip values to zero to manufacture a front.

## Illustrative inputs

| Input | Value | Provenance |
|---|---:|---|
| L | 0.03 m | Teaching choice |
| Dₛ | 1 × 10⁻⁹ m² s⁻¹ | Teaching choice, not an O₂ measurement or literature calibration |
| k | 1 × 10⁻⁵ s⁻¹ | Teaching choice |
| φ | 0.8 | Teaching choice |
| C₀ | 0.2 mol m⁻³ water (200 µM) | Teaching choice, not assigned to a field site |
| N, Δt | 80 cells, 1000 s | Numerical settings |

These give ℓ = 0.01 m, Da = 9, L²/Dₛ = 900000 s, and 1/k = 100000 s. At steady state the analytic bottom concentration is 0.0198655855 mol m⁻³ (19.8656 µM), inventory is 0.00159208761 mol m⁻² and inward flux is 1.59208761 × 10⁻⁸ mol m⁻² s⁻¹ (1.37556369 mmol m⁻² d⁻¹). A 1 µM threshold is never crossed in this 3 cm sealed domain. The nonzero bottom value is part of the example and exposes the boundary choice.

## Numerical method and accounting

Equal cells of width h = L/N store centre concentrations Cᵢ. Top face flux uses the half-cell distance: F₀ = 2φDₛ(C₀ − C₁)/h. Interior face flux is Fᵢ = −φDₛ(Cᵢ₊₁ − Cᵢ)/h. Bottom face flux is zero. Each cell obeys φh(Cᵢⁿ⁺¹ − Cᵢⁿ)/Δt = Fᵢ₋₁ⁿ⁺¹ − Fᵢⁿ⁺¹ − φhkCᵢⁿ⁺¹.

Set a = Dₛ/h². The decay-diffusion matrix A has diagonal (3a+k, 2a+k, ..., a+k), off-diagonals −a, and top forcing b₁ = 2aC₀. Backward Euler solves (I + Δt A)Cⁿ⁺¹ = Cⁿ + Δt b with Thomas elimination. Both the reaction and boundary flux use the new time level. The matrix has positive diagonals, nonpositive off-diagonals and strict row diagonal dominance for Δt > 0. Its inverse preserves nonnegativity for nonnegative inputs. Large Δt remains stable and positive, but loses time accuracy. Stability is not a convergence test.

Sum the cells to obtain (Mⁿ⁺¹ − Mⁿ)/Δt = F₀ⁿ⁺¹ − φkhΣCᵢⁿ⁺¹. Interior fluxes cancel. Both instantaneous and cumulative residuals are saved. Negative concentrations raise an error. No clipping or absolute-value repair is used.

## Identifiability and uncertainty

A single steady normalized profile with known L constrains α = k/Dₛ, or equivalently ℓ. Multiplying Dₛ and k by the same factor leaves its shape unchanged. Separate estimates of Dₛ and k from that profile are structurally non-identifiable. Known φ, C₀ and an independent flux can add a second constraint, but only under correct boundaries and transport assumptions. A transient relaxation rate λ = Dₛ(π/(2L))² + k together with α can also separate Dₛ and k in this ideal model.

The supplied synthetic fit estimates only α. It assumes known C₀, L and independent Gaussian measurement error σ = 0.002 mol m⁻³. Seed 20261010 generates ten observations from the analytic solution with α_true = 10000 m⁻². The fitted value is 9671.84069 m⁻²; a 200-replicate parametric bootstrap yields an approximate 95% percentile interval [9372.17710, 10033.39587] m⁻². This interval is conditional on the exact model and noise design. At fixed Dₛ = 10⁻⁹ m² s⁻¹, k = 9.67184069 × 10⁻⁶ s⁻¹. The code records log-α sensitivity and its local error estimate.

If Dₛ is independently uncertain over [0.5, 2] × 10⁻⁹ m² s⁻¹, the point estimate for k spans [4.83592 × 10⁻⁶, 1.93437 × 10⁻⁵] s⁻¹ before combining profile uncertainty. This illustrative range is not a statistical confidence interval. Unknown surface C₀, interface depth, sensor smoothing, heterogeneous k and boundary-layer resistance introduce further confounding. A profile concentrated only near the top or only below detection has weak practical information about ℓ.

## Thermodynamic boundary

The baseline does not calculate ΔG or F_T. The manuscript logistic F_T = 1/(1 + exp(ΔGᵣ/(RT))) gives 1/2 at ΔGᵣ = 0 and remains positive for unfavorable ΔGᵣ. As a multiplier of a one-way positive rate it therefore cannot by itself enforce zero net rate at equilibrium or reverse reaction direction. This is a mathematical diagnostic, independent of a data fit. It may be labeled a heuristic gate, but not a validated thermodynamic law. Proposed manuscript edits remove it from the instructional rate law. See `source-to-claim.csv` for the checked primary alternative and scope limitations.

## Empirical limits

Numerical verification asks whether the code solves this stated equation. Calibration fits parameters. Validation asks whether predictions match independent measured observations under stated conditions. The analytic and synthetic checks satisfy the first task, not the third. The measured-data exercise in `data-comparison-task.md` audits observational provenance and observable compatibility. It does not validate or calibrate this model. Scientific sink-attribution evidence and search limits are recorded separately in `literature-review.md` and `source-to-claim.csv`.
