# Analytical references and proposed numerical accounting

AD-CONTRACT-0.1. These are checked algebraic constructions, not executed numerical results. They describe the proposed baseline and auxiliary tests. Derivations are original checks of the specified constant-coefficient problem, not claims of new empirical science.

## Finite steady solution with the actual proposed boundaries

For constant C_in=C_ref, solve D_L*C''-u*C'-k*C=0. Let

$$
s=\sqrt{u^2+4D_Lk},\quad r_+=\frac{u+s}{2D_L},\quad
r_-=-\frac{2k}{u+s}.
$$

The latter expression avoids subtractive cancellation and gives r_-=0 at k=0. Both r have m^{-1}; r_-<=0<r_+ for u>0, D_L>0. Use bounded exponentials

$$
C_*(x)=a\exp(r_-x)+b\exp(r_+(x-L)).
$$

The two linear conditions fixing a and b are

$$
(u-D_Lr_-)a+(u-D_Lr_+)e^{-r_+L}b=uC_{\rm ref},
$$

$$
r_-e^{r_-L}a+r_+b=0.
$$

Substitution checks both the differential equation and the boundary conditions. The choice of exponential arguments prevents large positive exponents in the represented domain. Future evaluation must also handle coefficient conditioning and small exponents; positivity of a and b follows for k>0 from r_-<0, r_+>0 and |r_-|<r_+.

At k=0, b=0, a=C_ref: a conservative constant-feed steady state is uniform, F_in=F_out=v_D*C_ref and S=0. At k>0, integrate the differential equation to obtain F_in-F_out=phi*k*integral(C_* dx). This is the continuum steady mass check. It is independent of the transient discretization.

Compare finite-volume cell averages with exact averages, not with point samples at cell centers without explanation. For either exponential, average over [x_left,x_right] using its integral; take the r=0 limit directly and use expm1-based forms when appropriate. At fixed geometry and D_L>0, the k->0 limit must approach the uniform solution. Do not use the oxygen cosh solution for this flowing/open column.

## Hyperbolic advection and disappearance limit

For the auxiliary D_L=0 case, initially empty column and u>0:

$$
C(x,t)=C_{\rm in}(t-x/u)\exp(-kx/u),
$$

where C_in(s)=0 for s<=0. This follows along a characteristic with dC/dt=-kC. The finite pulse arrives at a position after x/u, lasts T_p and is attenuated by exp(-kx/u). The outflow time-integrated fraction is exp(-kL/u); at k=0 it is one. A time-limited partial outflow integral must retain storage. No independent outlet condition is imposed on this first-order hyperbolic PDE.

For the discontinuous rectangular pulse, numerical edges will be smeared by the proposed upwind scheme. Compare integrated quantities, timing and grid-refined profiles; do not assert smooth pointwise first-order convergence at a jump. This auxiliary test isolates artificial spreading and is not a physical claim that molecular diffusion literally vanishes.

## Smooth periodic auxiliary reference

Use a separate periodic domain of length L, beta=2*pi/L, positive background C_b and 0<=a_0<C_b. Its initial cell averages correspond to C_b+a_0*cos(beta*x). The continuum solution is

$$
C(x,t)=e^{-kt}\left[C_b+a_0e^{-D_L\beta^2t}\cos(\beta(x-ut))\right].
$$

Check by differentiation. Mean disappearance is exp(-kt); the mode translates with u and decays from dispersion by exp(-D_L*beta^2*t). Positivity is guaranteed for the stated amplitude. Periodic boundaries remove the inlet step and outlet interaction; this is exclusively a smooth verification test, not the teaching pulse's boundary model.

For an upwind/centered finite-volume spatial operator on equal cells of width h, theta=beta*h, the exact semidiscrete eigenvalue is

$$
\lambda_h=-k-\frac{4D_L\sin^2(\theta/2)}{h^2}
-\frac{u(1-\cos\theta)}h-i\frac{u\sin\theta}h.
$$

The exact semidiscrete background is C_b*exp(-kt); the initial mode amplitude for true cell averages is a_0*sinc(beta*h/2). Multiply that amplitude by exp(Re(lambda_h)*t), with phase beta*x+Im(lambda_h)*t. This independently evaluates the spatially discretized ODE without time stepping. Future time refinement compares backward Euler against this exact semidiscrete reference, at one fixed grid. Continuum comparison alone will plateau when spatial error dominates. No eigenvalue computation or solver has been run in this gate.

## Proposed conservative spatial and temporal scheme

After contract acceptance only: reuse the prior standard-library finite-volume/backward-Euler approach with newly specified boundary fluxes. Cell states C_i are porewater averages. For u>0, internal face flux is

$$
F_{i+1/2}=\phi\left[uC_i-D_L\frac{C_{i+1}-C_i}{h}\right].
$$

The boundary face fluxes are F_{1/2}=v_D*average(C_in over the time interval) and F_{N+1/2}=v_D*C_N. Use one face flux value in both adjacent cell balances. The last expression is the discrete zero-dispersive-outflow closure, not a second prescribed concentration. The update is

$$
\phi h\frac{C_i^{n+1}-C_i^n}{\Delta t}
=F_{i-1/2}^{n+1}-F_{i+1/2}^{n+1}
-\phi h kC_i^{n+1}.
$$

Inflow is known; all internal flux and loss terms use n+1. Sum the update: internal faces cancel exactly. Discrete inventory is M^n=phi*h*sum(C_i^n); the discrete loss increment is Delta t*k*M^{n+1}. The discrete outflow increment is Delta t*v_D*C_N^{n+1}. This is the budget to verify. Using trapezoidal diagnostic sinks or an analytic boundary flux with a backward-Euler update would test a different budget.

For h>0, Delta t>0, u>=0, D_L>=0 and k>=0, the backward-Euler matrix has positive diagonal, nonpositive off-diagonals and strict row diagonal dominance. Its inverse is nonnegative. With nonnegative initial states and feed, this gives a nonnegative discrete solution in exact arithmetic. The future code must reject invalid inputs, report minimum concentration, linear residual and any floating-point negativity, and never silently clip or rescale a solution. A tolerance may diagnose roundoff but cannot overwrite negative values. Matrix structure is a pre-implementation argument, not an executed positivity test.

Upwind advection is first order in space; centered dispersion is second order in the smooth interior. The coupled transport method is generally first order in space and time. Do not inherit the oxygen solver's overall second-order spatial claim. Backward Euler has no positivity CFL restriction for this operator, but accuracy still requires refinement.

For smooth pure advection (D_L=k=0) and small h and Delta t, Taylor expansion gives leading artificial diffusion

$$
D_{\rm num}\simeq\frac{u h}{2}+\frac{u^2\Delta t}{2}.
$$

The positive temporal term is specific to backward Euler. The forward-Euler expression with a negative Courant contribution does not apply. This leading long-wavelength diagnostic is not an exact error formula for general reacting, dispersive flow or discontinuous fronts. Use amplitude decay in the periodic pure-advection test, where the continuum has no spreading, together with independent grid/time refinement. Physical D_L must remain fixed as the mesh changes.
