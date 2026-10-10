## Let the water move

The oxygen example held its supply at a surface. Now imagine a different experiment: a short pulse of a dissolved substance enters a water-saturated column. Collect the water leaving the far end. A concentration curve rises, reaches a peak, and falls. This is a thought experiment, with synthetic results. What would its shape tell us?

Flow carries the substance forward. Different paths through the pore network spread it along the direction of flow. We represent that spreading, together with molecular diffusion, by one longitudinal coefficient $D_L$. This is a combined transport coefficient, distinct from the sediment diffusivity $D_s$ in the oxygen example. It does not include porosity.

Keep the same bookkeeping. Let $C$ be concentration per volume of porewater, $\phi$ the constant water-filled porosity, and $u$ the porewater velocity. The volumetric flow per bulk cross-sectional area, or Darcy flux, is $v_D=\phi u$. With $x$ increasing along the flow, the total solute flux is

$$
F=\phi\left(uC-D_L\frac{\partial C}{\partial x}\right).
$$

Allow an aggregate first-order loss $kC$ per volume of porewater. The bulk sink is $-\phi kC$, and, for these constant coefficients,

$$
\frac{\partial C}{\partial t}
=D_L\frac{\partial^2C}{\partial x^2}
-u\frac{\partial C}{\partial x}-kC.
$$

The equation needs an experiment around it. Our initially empty column receives a known total solute flux for a fixed time. We do not also fix the resident concentration at the inlet. At the exit, we set the dispersive gradient to zero while allowing flowing water to carry solute out. These are explicit finite-column closures, not universal boundaries for an aquifer.[^ad_boundary_ch8]

For the illustrative column, $L=1$ m, $\phi=0.30$, $u=10^{-5}$ $\mathrm{m\,s^{-1}}$, and $D_L=10^{-6}$ $\mathrm{m^2\,s^{-1}}$. Feed at $1$ $\mathrm{mol\,m^{-3}}$ of porewater for 20000 s. The conservative calculation exports almost all the input during a 600000 s observation window. With $k=10^{-5}$ $\mathrm{s^{-1}}$, it exports about 39.76 percent; about 60.24 percent enters the parent-disappearance ledger, and a small amount remains stored. These are calculated fractions of the supplied dose, not removal measured in groundwater. [The scenario table](../courses/advection-dispersion/model/results/scenario-summary.csv) retains the separate export, disappearance and storage amounts.

The reactive outlet curve also peaks earlier. That does not mean the water flows faster: loss changes the weighting of the material that survives to leave. Nor does a lower peak establish consumption. Spreading alone can lower a peak while conserving the parent. We need the integrated export and the material still inside the column.

A computer can add spreading of its own. The companion calculation therefore checks separate grid and time refinements, alongside conservation and nonnegativity. A perfectly balanced ledger can accompany a poorly resolved curve. The technical details and synthetic comparison are in the [Model Toolkit](../appendices/b-model-toolkit.md#advection-dispersion-and-parent-loss). These checks establish that the calculation behaves as intended. Identifying the processes operating in an aquifer needs independent observations.

[^ad_boundary_ch8]: M. Th. van Genuchten and J. C. Parker, "Boundary Conditions for Displacement Experiments through Short Laboratory Soil Columns," *Soil Science Society of America Journal* 48 (1984): 703-708. The paper distinguishes resident and flux concentrations and compares finite-column boundary formulations; it does not establish a universal aquifer boundary. [@vanGenuchtenParker1984]
