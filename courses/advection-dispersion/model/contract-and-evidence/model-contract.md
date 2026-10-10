# Advection, dispersion and aggregate loss: draft scientific contract

Revision AD-CONTRACT-0.1. Status: proposed, awaiting Editor acceptance. Source base b6f5fd80c963e8cd5b739e930893a0c7ec7c871a. This gate supplies equations and future checks, not an implemented or verified solver, solved examples, field validation or a learner trial. All candidate inputs are illustrative; no observations are fitted.

## Observable and physical setting

Imagine a known pulse of a dissolved, non-sorbing solute entering a saturated, rigid column. Record its resident concentration along the column and its exported concentration and molar flux over time. First use a conservative tracer (k=0); then repeat the thought experiment with a positive aggregate first-order disappearance coefficient. The second case is a hypothetical parent species, not an assertion that a conservative tracer reacts.

The domain is a constant-area column, x in [0,L], with x increasing along the prescribed flow. The frame is fixed to the solid matrix. The fluid has constant density, steady throughflow and no lateral exchange. The single mobile aqueous continuum has constant porosity phi. The proposal assumes all modeled porewater belongs to that continuum: no separate immobile region, retardation, sorption, solid transport, density feedback, growth, donor limitation, redox switching or thermodynamic gate. These sacrifices limit transfer to aquifers and microbial processes.

## Notation and units

- C(x,t): resident solute concentration, mol m^{-3} of modeled porewater. A spatially averaged porewater sample is a resident observable; an effluent sample is a flux observable.
- phi: dimensionless saturated mobile porosity, 0<phi<=1. Bulk inventory density is phi*C, mol m^{-3} of bulk medium. Equal total and mobile porosity is an assumption here.
- u>0: mean porewater velocity in the x direction, m s^{-1}, consistent with Chapter 8. This is a continuum average, not a velocity at each pore.
- v_D: Darcy volumetric flux through bulk cross-sectional area, m s^{-1}; v_D=phi*u. If Q is volumetric flow in m^3 s^{-1} and A is column area in m^2, v_D=Q/A. Never use Q/A as u without dividing by phi.
- D_L>0: constant longitudinal hydrodynamic dispersion coefficient, m^2 s^{-1}. It includes the represented molecular and mechanical spreading; it excludes the separate phi prefactor. It is distinct from the oxygen model's molecular D_s. No second molecular term is added to this already combined coefficient.
- k>=0: first-order disappearance coefficient, s^{-1}; q_loss=k*C>=0 is a positive porewater rate, mol m^{-3} water s^{-1}. The signed bulk source is R=-phi*k*C. k is not permeability or a biomass-specific maximum rate.
- F=phi*(u*C-D_L*C_x): total molar flux per bulk area, mol m^{-2} s^{-1}, positive in the x direction. Its advective part is v_D*C; its dispersive part is -phi*D_L*C_x.
- C_in(t)>=0: imposed feed concentration expressed as incoming molar flux divided by v_D, mol m^{-3} water. It need not equal resident C(0,t).
- C_F=F/v_D=C-(D_L/u)*C_x: flux-normalized concentration within this particular constant-flow closure. At the proposed exit, C_x=0 implies C_F(L,t)=C(L,t). This does not imply the two observables are interchangeable everywhere.

Unit check: phi*C/t, F/x and phi*k*C are all mol m^{-3} bulk s^{-1}; u*C and D_L*C_x are both mol m^{-2} s^{-1} before multiplication by phi. v_D/phi has velocity units. D_L/u is a length.

## Balance, initial condition and boundaries

The conservation statement is

$$
\frac{\partial(\phi C)}{\partial t}=-\frac{\partial F}{\partial x}-\phi kC.
$$

With constant phi, u and D_L it reduces to

$$
C_t=D_L C_{xx}-u C_x-kC.
$$

Core initial condition: C(x,0)=0 in the interior. A rectangular feed is C_in=C_ref for 0<t<T_p, and zero thereafter. A constant feed is a separate steady benchmark. Pulse endpoints are handled by exact interval overlap or aligned time steps, not by silently sampling away part of the injected mass.

Proposed inlet for u>0:

$$
F(0,t)=v_D C_{\rm in}(t),\qquad
u C(0,t)-D_L C_x(0,t)=u C_{\rm in}(t).
$$

The condition prescribes total input mass flux; it is often called a third-type or Danckwerts-type inlet. It is motivated by a feed with negligible dispersive exchange in its upstream section, not by a universal aquifer interface. We do not also impose C(0,t)=C_in(t).

Proposed outlet:

$$
C_x(L,t)=0,\qquad F(L,t)=v_D C(L,t).
$$

Only the dispersive contribution is zero. The column is open to advective export. This is a chosen finite-column exit closure; a sealed exit F=0 or a fixed exit C=0 would describe a different experiment. Boundary geometry and sampling mode are essential to interpreting column data. The primary boundary analysis supporting this distinction is [van Genuchten and Parker (1984)](https://www.ars.usda.gov/arsuserfiles/20360500/pdf_pubs/P0846.pdf), equations 3, 16 and 27; source appraisal is in source-to-claim.csv.

A concentration-type inlet can define a legitimate imposed-concentration reservoir, but then actual total input includes its dispersive component. It is incorrect to account only for v_D*C_in while imposing such a different boundary. We will not teach that Dirichlet boundaries inherently violate conservation.

The inlet step is initially incompatible with the zero interior, just as a switched supply can be. It is suitable for a pulse experiment but not for proving smooth temporal order. u=0 with this flux inlet gives zero input and a closed diffusion problem; it does not recover the oxygen model's fixed-concentration surface. D_L=0 is a separate hyperbolic limiting test with only an inflow concentration, not an extra independent outflow boundary condition.

## Integrated parent-species accounting

Work per unit bulk cross-sectional area unless A is explicitly multiplied in:

$$
M(t)=\phi\int_0^L C\,dx,\qquad
S(t)=\phi k\int_0^L C\,dx=kM(t),
$$

$$
\frac{dM}{dt}=F(0,t)-F(L,t)-S(t).
$$

M has mol m^{-2}, S has mol m^{-2} s^{-1}. Define cumulative input I, exported amount O and disappeared parent amount B as time integrals of F(0), F(L) and S. The budget is M(t)-M(0)=I(t)-O(t)-B(t). For the specified pulse I_total=v_D*C_ref*T_p. At finite simulation end, remaining M must be retained; exported deficit is not automatically reaction loss. At k=0, B=0, and eventual complete washout gives O_total=I_total for this finite, connected, open column. That limiting identity is not a claim that any selected end time is long enough.

For k>0 the ledger conserves the tracked parent by explicitly recording its disappearance. It does not conserve all chemical elements across an unspecified reaction. Products, electron balance and biomass are unmodeled. A chemical interpretation would require balanced additional species. Apparent disappearance cannot by itself be attributed to biodegradation, complete mineralization, or safe water.

## Candidate scales, not accepted student values

Propose L=1 m, phi=0.30, u=10^{-5} m s^{-1}, D_L=10^{-6} m^2 s^{-1}, C_ref=1 mol m^{-3}, and T_p=0.2*L/u. Use k=0 first, then k=10^{-5} s^{-1}. These are chosen mathematical scales, not representative measurements of a named aquifer, tracer or reaction. Define Pe=uL/D_L, Da_a=kL/u, tau_a=L/u, tau_d=L^2/D_L and tau_r=1/k for k>0. The choices make Pe=10 and Da_a=0 or 1 by definition. The optional relation D_L=D_m,p+alpha_L*|u| is not separately parameterized or fitted in this gate; one flow experiment cannot partition a combined D_L into both contributions.

The student default resolution and reported numerical values remain unset until contract acceptance and successful verification. Proposed resolution families and error gates are in benchmark-plan.md. No results files are supplied at this stage.

## Analytical references and inference

The finite-domain steady reference, the zero-dispersion delayed pulse and a smooth periodic auxiliary mode are derived in analytical-checks.md. The auxiliary mode has different initial and boundary conditions; it must never be passed off as the core pulse solution. No semi-infinite Ogata-Banks expression is silently used as the exact reference for this finite flux-inlet system.

The steady equation and its inlet/outlet conditions are invariant under (u,D_L,k) -> s*(u,D_L,k), s>0, when only resident concentrations and the known feed concentration are observed. A steady profile therefore cannot identify all three absolute rates: it can constrain u/D_L and k/D_L under sufficient information. One steady effluent concentration alone supplies still less. Constant phi cancels from concentration evolution if u is separately prescribed. Absolute measured flux plus independently known phi or known volumetric flow can supply additional constraints; these must be stated, not invented.

Proposed inference progression: obtain transport information from a conservative pulse with independently known flow, feed schedule and geometry; then examine only k conditional on transport assumptions for an illustrative reactive pulse. Before any future fit, inspect sensitivities and practical uncertainty, especially input recovery, incomplete observation windows and correlations between residence time, D_L and k. Timing, broadening and recovery are useful observables, not automatic unique parameter measurements. Separate experiments or held-out perturbations would be needed for empirical validation. No calibration or field dataset is authorized or available here.

A widened profile is a spreading observable; this single-concentration closure does not resolve contact between separate electron donors and acceptors at pore scale. A fitted D_L does not establish a mixing-controlled reaction mechanism. Long-tailed breakthrough can reflect velocity heterogeneity, mobile/immobile exchange, sorption, boundary behavior or incomplete sampling; it is not a unique first-order reaction signature. This single-region closure is a deliberate reference model rather than an asserted law for all groundwater. Scientific evidence and access limits are recorded separately.
