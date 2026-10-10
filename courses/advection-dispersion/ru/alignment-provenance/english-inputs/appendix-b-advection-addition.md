## Advection, dispersion and parent loss {#advection-dispersion-and-parent-loss}

This reference extends the oxygen example to a single dissolved species in a saturated, rigid column. It uses one mobile water region, constant coefficients and a flow coordinate $0\leq x\leq L$. All parameters and observations below are illustrative or synthetic. The coefficient $k$ here is a loss constant, not the permeability denoted by $k$ in the earlier Darcy expression. Write $\phi$ for the porosity denoted by $\varphi$ elsewhere in this appendix.

### State, flux and boundary conditions

Resident $C$ has units $\mathrm{mol\,m^{-3}}$ of porewater; bulk storage $\phi C$ has units per bulk volume. Porosity is dimensionless. Porewater velocity $u$ and Darcy flux $v_D=Q/A=\phi u$ have units $\mathrm{m\,s^{-1}}$, but are different quantities. Here all saturated porosity is mobile. The combined longitudinal coefficient $D_L$ has units $\mathrm{m^2\,s^{-1}}$ and excludes porosity. It already represents the molecular and mechanical spreading included in this model; adding the oxygen diffusivity again would double count the molecular contribution.

The loss constant $k$ has units $\mathrm{s^{-1}}$. With positive flow and nonnegative loss,

$$
F=\phi(uC-D_L C_x),\qquad
\partial_t(\phi C)=-\partial_xF-\phi kC.
$$

Flux is per bulk cross-sectional area, in $\mathrm{mol\,m^{-2}\,s^{-1}}$. Constant $\phi$, $u$ and $D_L$ give $C_t=D_LC_{xx}-uC_x-kC$. A variable-coefficient extension must return to the conservative form.

Initially $C(x,0)=0$. The feed is $C_{\mathrm{in}}=C_{\mathrm{ref}}$ for $0\leq t<T_p$ and zero thereafter. For $u>0$ and $D_L>0$, impose

$$
F(0,t)=\phi uC_{\mathrm{in}}(t),\qquad C_x(L,t)=0.
$$

The inlet fixes total solute supply, not an additional resident concentration. The exit has zero dispersive flux and remains open to advective export. Boundary choice and the distinction between resident and flux concentrations matter in column experiments.[^ad_boundary_app]

Define flux-normalized concentration $C_F=F/v_D$ only for $v_D>0$. In the interior it differs from $C$ by $-(D_L/u)C_x$. At this exit $C_F(L,t)=C(L,t)$. The discrete terminal cell average approximates the exit trace; it is not a point sample at $L$.

Let $M=\phi\int_0^L C\,dx$ be inventory per bulk area. Cumulative input $I$, export $O$ and parent disappearance $B$ use the same $\mathrm{mol\,m^{-2}}$ basis. The budget is

$$
\frac{dM}{dt}=\phi uC_{\mathrm{in}}-\phi uC(L,t)-kM,
\qquad M(t)-M(0)=I(t)-O(t)-B(t).
$$

A deficit in export can remain in storage. The disappearance ledger records loss of the tracked parent; products and elemental balances are not represented. It does not establish mineralization, microbial causation or water safety. Sorption, immobile exchange, biomass dynamics and energetic regulation are absent.

### Scales and controlled scenarios

The accepted reference uses $L=1$ m, $\phi=0.30$, $u=10^{-5}$ $\mathrm{m\,s^{-1}}$, $D_L=10^{-6}$ $\mathrm{m^2\,s^{-1}}$, $C_{\mathrm{ref}}=1$ $\mathrm{mol\,m^{-3}}$ and $T_p=20000$ s. Compare $k=0$ and $k=10^{-5}$ $\mathrm{s^{-1}}$. The advective scale is $\tau_a=L/u=100000$ s; $\mathrm{Pe}=uL/D_L=10$ and $\mathrm{Da}=kL/u$ is zero or one. These column-scale ratios are not pore-scale ratios from another study.

The [four-case table](../courses/advection-dispersion/model/results/scenario-summary.csv) also compares conservative cases with $2u$ or $2D_L$, holding the physical pulse duration fixed. Doubling $u$ doubles the input from $0.06$ to $0.12$ $\mathrm{mol\,m^{-2}}$. Each fraction uses its own dose. At fixed $u$, changing $\phi$ scales all amount ledgers while leaving $C$ unchanged. At fixed Darcy flux, changing $\phi$ changes $u$ and can change the concentration history.

### Finite-volume update and its ledger

Use $N$ equal cells, $h=L/N$, with resident cell averages $C_i$. One shared internal face flux appears with opposite signs in neighboring balances:

$$
F_{i+1/2}^{n+1}=\phi\left[uC_i^{n+1}
-D_L\frac{C_{i+1}^{n+1}-C_i^{n+1}}h\right].
$$

Advection is first-order upwind; dispersion uses centered gradients. Backward Euler gives

$$
\phi h(C_i^{n+1}-C_i^n)
=\Delta t_n(F_{i-1/2}^{n+1}-F_{i+1/2}^{n+1})
-\Delta t_n\phi h kC_i^{n+1}.
$$

The inlet is the known interval-average flux. Its dose increment is the exact overlap of $[t_n,t_{n+1})$ with $[0,T_p)$, multiplied by $\phi uC_{\mathrm{ref}}$. This handles a step crossing the feed endpoint without changing the dose. The outlet is $\phi uC_N^{n+1}$, so the saved ledger uses

$$
M^{n+1}-M^n=\Delta I_n-\Delta O_n-\Delta B_n,
\quad \Delta O_n=\Delta t_n\phi uC_N^{n+1},
\quad \Delta B_n=\Delta t_n kM^{n+1}.
$$

Use these increments for readback. Trapezoidal integration of the displayed diagnostics tests a different ledger. Optional inlet component exports use a declared half-cell diagnostic trace

$$
C_b=\frac{u\overline C_{\mathrm{in}}+2D_L C_1^{n+1}/h}{u+2D_L/h}.
$$

Its advective component is $\phi uC_b$; its dispersive component is prescribed total inlet flux minus that amount. This reconstruction is not an extra boundary condition or an independently measured resident inlet. During washout the components can cancel while total input is zero.

The linear system has a positive diagonal, nonpositive off-diagonals and strict row diagonal dominance. Nonnegative initial states and feed therefore give a nonnegative solution in exact arithmetic. Actual minima, negative counts and residuals remain exported; the code applies no clipping, rescaling or mass correction. Backward Euler permits large steps without a positivity CFL restriction here, but that says nothing about accuracy. The coupled method is generally first order in space and time, unlike the oxygen model's diffusion-only spatial result.

### Matched references and verification

For a separate constant-feed steady problem, $D_L C_*''-uC_*'-kC_*=0$. Define

$$
s=\sqrt{u^2+4D_Lk},\quad
r_+=\frac{u+s}{2D_L},\quad r_-=-\frac{2k}{u+s}.
$$

Use $C_*(x)=a\exp(r_-x)+b\exp(r_+(x-L))$, with

$$
(u-D_Lr_-)a+(u-D_Lr_+)e^{-r_+L}b=uC_{\mathrm{ref}},
\qquad r_-e^{r_-L}a+r_+b=0.
$$

The exponents stay bounded on the domain and the expression for $r_-$ avoids subtraction of nearly equal numbers. Compare true analytic cell averages with numerical averages. For $k=0$, the steady solution is uniform. [Steady profiles](../courses/advection-dispersion/model/results/steady-reference-profiles.csv) and [spatial errors](../courses/advection-dispersion/model/results/steady-spatial.csv) are separate from pulse results. The reactive spatial orders approach one (about 0.981, 0.990 and 0.995).

Auxiliary tests deliberately change the problem. At $D_L=0$, characteristics give $C(x,t)=C_{\mathrm{in}}(t-x/u)e^{-kx/u}$, with zero feed before switch-on. No independent outflow gradient is imposed on this hyperbolic equation. Its time-integrated survival is $e^{-kL/u}$. A smooth periodic mode separately checks translation, dispersion and decay without the pulse boundaries. With $\beta=2\pi/L$ and $0\leq a_0<C_b$, its continuum solution is

$$
C(x,t)=e^{-kt}\left[C_b+a_0e^{-D_L\beta^2t}\cos(\beta(x-ut))\right].
$$

For cell width $h$, $\theta=\beta h$, the spatial operator has the exact mode eigenvalue

$$
\lambda_h=-k-\frac{4D_L\sin^2(\theta/2)}{h^2}
-\frac{u(1-\cos\theta)}h-i\frac{u\sin\theta}h.
$$

Its initial cell-average amplitude includes $\sin(\beta h/2)/(\beta h/2)$. Time refinement uses the mode evolving as $\exp(\lambda_h t)$ and the background evolving as $\exp(-kt)$, at fixed grid. Comparison with the continuum solution instead plateaus at fixed spatial error. [Periodic time checks](../courses/advection-dispersion/model/results/periodic-time.csv) report both errors. Closed zero-flow tests check decay and conservation, not delivery through the finite-column inlet.

For smooth pure advection, the leading long-wave numerical spreading is

$$
D_{\mathrm{num}}\simeq\frac{uh}{2}+\frac{u^2\Delta t}{2}.
$$

The positive time term is specific to backward Euler. This is an auxiliary diagnostic, not a universal error formula for dispersive reacting pulses. Keep physical $D_L$ fixed during refinement.

The reference resolution is $N=400$, $\Delta t=100$ s and a 600000 s window. Separate $N=800$ and $\Delta t=50$ s controls pass declared scale-aware 2 percent metric/profile targets; recovery, disappearance and storage changes are below 0.005. Conditional resident spatial widths also pass separate reconstructed controls. An 800000 s extension checks window stability. These differences support the chosen teaching resolution; they are not a bound on every possible continuum error. The metric target is $|z_{\mathrm{fine}}-z_{\mathrm{base}}|\leq0.02\max(|z_{\mathrm{fine}}|,z_{\mathrm{floor}})$. Floors are $0.01C_{\mathrm{ref}}$ for peak, $0.01\tau_a$ for temporal metrics and $0.01L$ for spatial width. Profile comparisons use the maximum absolute difference across declared snapshots and coarse cells, after averaging fine children, with scale $\max(C_{\mathrm{fine,max}},0.01C_{\mathrm{ref}})$. Undefined moments remain undefined. Linear residuals must be below $10^{-12}$; budget residuals below $10^{-10}$ after scaling by $\phi LC_{\mathrm{ref}}$ or the initial inventory. The all-zero branch instead checks an absolute amount residual of $10^{-14}$ $\mathrm{mol\,m^{-2}}$.

All four cases retain less than 0.001 of their dose at the reported end, with the window checks also passing. This is effective washout under a declared criterion, not exact complete export. The largest core scaled update-budget residual is about $9.85\times10^{-13}$; the actual concentration minimum is zero and negative counts are zero. Algebraic balance and positivity are checked separately from curve accuracy. [Verification exports](../courses/advection-dispersion/model/results/verification.json) preserve these results. A retained first attempt failed the periodic auxiliary checker and was corrected. Its recorded 400000 s more-dispersion storage was insufficient for the washout criterion; that case was not part of the first formal window gate.

### What is being observed and inferred?

The outlet peak is the maximum sampled right-endpoint concentration. Reported $t_{10}$, $t_{50}$ and $t_{90}$ are quantiles of exported mass within the chosen window, reconstructed with constant flux in each update interval. They are not quantiles of injected dose or sharp first-arrival times. Temporal width is the standard deviation of that exported-mass distribution. Resident spatial width describes only material still in the finite column and includes the cell-internal $h^2/12$ contribution. It is a different quantity. Both widths are undefined when their conditioning amount is zero.

Eight [synthetic observations](../courses/advection-dispersion/model/results/observations-synthetic.csv) are interval-average outlet flux-normalized concentrations generated at $N=800$, $\Delta t=50$ s with $k=10^{-5}$ $\mathrm{s^{-1}}$. There is no added noise or measurement uncertainty. Candidates at the reference resolution vary only $k$ among $0$, $10^{-5}$ and $2\times10^{-5}$ $\mathrm{s^{-1}}$, with all transport and feed inputs known. Equal-weight RMSE uses prediction minus observation on the same intervals. The [open comparison table](../courses/advection-dispersion/model/results/candidate-scores-open-answers.csv) gives about 0.07453, 0.0002667 and 0.03143 $\mathrm{mol\,m^{-3}}$, respectively. The matching-$k$ score is nonzero because the generating grid is finer. No optimizer, confidence interval or independent natural-data validation is implied.

At steady state, multiplying $u$, $D_L$ and $k$ by the same positive factor preserves concentrations under these boundaries. A steady concentration profile alone cannot identify all three absolute rates. Transient timing provides another observable, but any inference still depends on transport, feed, measurement support and the chosen closure. This exercise demonstrates conditional consistency among three candidates, not general identifiability.

Pore-scale numerical evidence also cautions against transferring a constant $D_L$ to every scale or medium.[^ad_gouze_app] Generated sandstone-like geometries are not a field validation dataset for this column. The companion model, exported tables and [readback instructions without Python](../courses/advection-dispersion/model/no-python-readback.md) allow verification of a transparent reference before asking which assumptions natural observations support.

[^ad_boundary_app]: M. Th. van Genuchten and J. C. Parker, "Boundary Conditions for Displacement Experiments through Short Laboratory Soil Columns," *Soil Science Society of America Journal* 48 (1984): 703-708, equations 3, 16, 22 and 27. The study compares closures, including practical effluent alternatives. The selected closure here is a teaching assumption. [@vanGenuchtenParker1984]

[^ad_gouze_app]: Philippe Gouze et al., "Modeling Longitudinal Dispersion in Variable Porosity Porous Media: Control of Velocity Distribution and Microstructures," *Frontiers in Water* 3 (2021): 766338, Sections 2.1-2.3, 3.4 and 4. The checked evidence is pore-scale numerical work in generated media; no field calibration or parameter transfer is supplied. [@Gouze2021Dispersion]
