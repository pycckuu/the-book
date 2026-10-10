# Model interface, basis and export support

This is a one-dimensional saturated, rigid, single mobile dissolved-species continuum. x increases along u>0 on [0,L]. Resident porewater concentration C has mol m^{-3} water; bulk storage phi*C has mol m^{-3} bulk. Constant mobile porosity phi equals total saturated porosity by assumption. u is porewater velocity; Darcy volumetric flux v_D=phi*u=Q/A has m s^{-1}. D_L (code key D) has m^2 s^{-1}, combines represented molecular/mechanical spreading and excludes phi. k has s^{-1}; signed bulk source is -phi*k*C. Products, sorption, immobile exchange, density effects, coupled biomass/energetics and elemental/stoichiometric reaction balances are absent.

$$
F=\phi(uC-D_L C_x),\qquad
\partial_t(\phi C)=-\partial_x F-\phi kC.
$$

Core: C initially zero, inlet F(0,t)=phi*u*C_in(t), exit C_x(L,t)=0 with F(L,t)=phi*u*C(L,t). C_in=C_ref for 0<=t<T_p and zero thereafter. The inlet is a specified total mass flux, not simultaneous resident C(0)=C_in. The outlet is open to advective export. C_F=F/(phi*u) is flux-normalized concentration for u>0. Its exit value equals resident C(L) for this closure, approximated discretely by terminal cell average C_N. C_N is not a point measurement at L. Exported C_out_right_endpoint is this approximation and this flux-normalized value; the distinction collapses only at the specified exit. It does not collapse for resident profiles or the inlet.

Internal finite-volume faces use phi*[u*C_i-D_L*(C_{i+1}-C_i)/h], with upwind advection. One shared total face flux enters adjacent cells with opposite signs. The first/last total fluxes are prescribed phi*u*interval_average(C_in) and phi*u*C_N. Backward Euler evaluates internal transport, outlet and loss at n+1. Sum the updates:

$$
M^{n+1}-M^n=\Delta I_n-\Delta O_n-\Delta B_n,
\quad M^n=\phi h\sum_i C_i^n,
\quad \Delta O_n=\Delta t\,\phi u C_N^{n+1},
\quad \Delta B_n=\Delta t\,kM^{n+1}.
$$

Delta I_n uses the exact intersection of the time interval with [0,T_p). Input concentration in the CSV is an interval average, while output is a right-endpoint value. These supports deliberately differ according to the update. A trapezoidal diagnostic would not reproduce this ledger. M, I, O and B are mol m^{-2} bulk cross-sectional area. B records disappeared tracked parent, not mineralized carbon, microbial destruction or safe water. Missing exported parent at finite end may still be in M.

The inlet face components are a separate diagnostic reconstruction. Define C_b=(u*C_in_avg+2*D_L*C_1/h)/(u+2*D_L/h); report advective phi*u*C_b and dispersive phi*u*C_in_avg minus advective. This is the half-cell trace solving the chosen flux relation with the first cell and average feed. It is not another boundary condition and is not an independently resolved resident boundary sample. A zero total inlet during washout can have positive advective and negative dispersive diagnostic components that cancel. The actual solver uses prescribed total inlet directly. At outlet the dispersive contribution is zero; advective and total coincide. Face CSV support explicitly labels the inlet diagnostic.

## Table dictionary

- profiles: resident C_cell_average_mol_m3_water over x_left_m to x_right_m at t_s; not point samples. Time zero and subsequent declared snapshots retained. Snapshot profiles permit independent storage, spatial centroid and conditional-width calculations.
- face-fluxes: F_adv, F_disp and F_total in mol m^{-2} s^{-1} through bulk area; x_face_m. Boundary and internal components at selected steps, with support column. The trace is only populated at inlet.
- pulse-budget: every interval t_left_s to t_right_s. C_in_interval_average and C_out_right_endpoint are mol m^{-3} porewater. F_in_interval_average and F_out_right_endpoint are mol m^{-2} s^{-1}. M_previous, M_next, delta_I, delta_O, delta_B, I, O, B and both residuals are mol m^{-2} bulk area. Scaled residuals and linear_residual_scaled are dimensionless. C_min_actual/C_max_actual are actual unaltered mol m^{-3} porewater.
- independent-refinement: declared metric base/refined, absolute change, tolerance and pass_target. Peak/profile changes are concentration units; time/width changes seconds; fraction changes dimensionless. Each case has grid_only and time_only controls with unchanged physical parameters. All profile comparisons average two fine children into one coarse cell.
- steady-reference-profiles: discrete and exact finite-domain constant-feed cell averages. These are not pulse snapshots. steady-spatial gives their maximum errors and steady flux/sink budget. Fluxes/sink there have mol m^{-2} s^{-1}.
- periodic-time and periodic-spreading: separate auxiliary periodic domain and positive smooth IC. Errors are concentration units; D values are m^2 s^{-1}; phase radians. They distinguish semidiscrete temporal error from continuum error and physical spreading from artificial spreading. Mean and amplitudes can be checked from their prescribed reference; no pulse boundary validation is inferred.
- hyperbolic-limit: auxiliary D_L=0 pulse. Profile L1 error includes phi*h and has mol m^{-2} bulk area; arrival/time/width seconds. Discontinuous-edge comparisons do not establish a smooth pointwise convergence order.
- scenario-summary: outlet right-endpoint peak, sampled peak time, finite-window exported-mass quantiles, temporal moments/width, own input dose and recovery/loss/storage fractions. Quantiles condition on exported mass, not injected mass. All widths/arrival metrics retain the declared observation window.
- synthetic input/output tables: noiseless interval-average outlet flux-normalized concentrations in mol m^{-3} porewater. Raw generating series and candidate series use the same explicit right-endpoint flux reconstruction on their respective grids. Optional sigma is blank because no measurement uncertainty was supplied; no zeros masquerade as uncertainties.

Blank numeric fields mean undefined/not applicable. JSON uses null. Centroid/width and quantiles are undefined with zero storage/export. No clipping, nonnegative projection, post hoc mass correction or adjustment of physical D_L is applied. Minima and negative-value counts remain reported. All source values/parameters are synthetic, even when their units match a possible measurement.
