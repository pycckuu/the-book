---
title: "Modeling the Invisible"
---

![Schematic porewater profiles, drawn from analytic functions rather than measured data. Each curve uses a relative concentration scale; their plotted crossing illustrates a transition and does not locate a measured sulfate-methane transition.](../sources/img/ch8_porewater_profile.png){#fig-porewater-profile}

A sediment core can look, at first glance, like three quiet curves on a page. The x-axis is concentration. The y-axis is depth below the sediment-water interface, increasing downward. The curves are oxygen, sulfate, and methane in an imagined marine sediment. This is a thought experiment: the figure uses smooth analytic functions, not measurements from a core.

In the sketch, oxygen falls steeply below the interface. Sulfate stays high near the surface and declines farther down. Methane rises from below. The relative scales show a possible arrangement, not concentrations or detection limits measured at a particular site.

The sketch places sulfate falling and methane rising around a transition horizon. In a measured core, we would locate the sulfate-methane transition from actual concentrations and the processes that connect them, not from the crossing of separately scaled curves. Neither its width nor its reaction rate can be read from this drawing.

A familiar biological explanation is anaerobic oxidation of methane by archaea associated with sulfate-reducing bacteria. One balanced net reaction is:

$$
\text{CH}_4 + \text{SO}_4^{2-} \longrightarrow \text{HCO}_3^- + \text{HS}^- + \text{H}_2\text{O}
$$

The organisms are real. The reaction is real. But the *shape* of the curves -- why oxygen drops fast and sulfate drops slowly, why methane rises from below, why the transition zone sits here and not somewhere else -- cannot be explained by intuition alone. It requires bookkeeping.

This chapter is about that bookkeeping: how to turn a porewater profile into a quantitative story. The same conservation law, written once and applied species by species, lets us ask practical questions. Why does this boundary sit where it does? How far would it move if organic matter delivery doubled? How much methane escapes if transport outruns biology?

One equation is enough to begin.

## Conservation: the only law you need

Every model in this book -- every profile, every flux, every prediction -- rests on a single principle: **mass is conserved**.[^berner1980] Whatever enters a volume of sediment must either leave it, react within it, or accumulate. There are no other options.

Write this as an equation. Consider a thin slab of sediment at some depth $x$, with thickness $\Delta x$. Let $\hat{C}$ be the bulk concentration of a chemical species -- the amount per unit volume of sediment (not per unit volume of porewater; that distinction matters and we will get to it). The rate of change of $\hat{C}$ in that slab is:

$$
\frac{\partial \hat{C}}{\partial t} = -\frac{\partial F}{\partial x} + \sum R_i
$$

Three terms. Each one does exactly one job. Here $\hat{C}$ is in mol per cubic meter of bulk sediment, $F$ in mol per square meter of sediment per second, and each $R_i$ in mol per cubic meter of bulk sediment per second. A porewater rate must be multiplied by porosity before it enters this bulk balance.

**The left side** ($\partial \hat{C} / \partial t$) is the rate of accumulation. If the concentration in the slab is increasing, this term is positive. If it is decreasing, this term is negative. At steady state -- when the profile is not changing with time -- this term is zero.

**The first term on the right** ($-\partial F / \partial x$) is the negative divergence of flux. $F$ is the flux of the species -- the amount moving through a unit area per unit time. If more stuff flows into the slab from above than flows out below, the concentration increases. If more flows out than in, it decreases. The minus sign and the derivative handle the bookkeeping automatically.

**The second term** ($\sum R_i$) is the sum of all reactions that produce or consume the species. A reaction that produces the species contributes a positive $R_i$. A reaction that consumes it contributes a negative $R_i$. If there are multiple reactions acting on the same species -- which there always are -- you add them all up.

That is the entire equation. It says: the rate of change equals what comes in minus what goes out, plus what is produced minus what is consumed. It is an accounting identity, nothing more, nothing less.

Everything else is details. Important details -- but details.

## What moves: transport

The flux $F$ has two components in most sediment and groundwater settings: diffusion and advection.

**Molecular diffusion** moves dissolved species down their concentration gradients. The flux is:

$$
F_{\text{diff}} = -\phi \cdot D_s \cdot \frac{\partial C}{\partial x}
$$

where $\phi$ is porosity (the fraction of the sediment that is porewater), $D_s$ is the effective diffusion coefficient in the sediment (smaller than in free water, because the pore network is tortuous), and $C$ is the porewater concentration. The minus sign means stuff moves from high concentration to low. This is Fick's first law, applied to a porous medium.[^fick1855] Here $D_s$ includes the tortuosity correction, but not the separate porosity prefactor already present in the flux. Some conventions absorb porosity into a bulk diffusion coefficient; mixing the two conventions would count porosity twice.[^boudreau1997]

A useful intuition: the timescale for diffusion to operate over a distance $L$ is:

$$
\tau_{\text{diff}} \sim \frac{L^2}{D_s}
$$

For $D_s \approx 10^{-5}$ cm$^2$/s (a typical value for ions in sediment[^ligregory1974]) and $L = 1$ cm, $\tau \approx 10^5$ seconds -- about a day. For $L = 1$ m, $\tau \approx 10^{9}$ seconds -- about 30 years. Diffusion acts quickly over millimeters and can take decades over meters. This scaling compares distances, but it does not set a universal depth of biological activity. Supply, consumption and boundary conditions must be considered together. Permeable beaches provide a useful counterexample to transferring a diffusion-only picture without checking flow.[^auer2025_eq]

**Advection** moves material with the flowing medium. For dissolved species, the flux is:

$$
F_{\text{adv}} = \phi \cdot u \cdot C
$$

where $u$ is the porewater velocity. For solid species (organic particles, minerals, biomass), the corresponding flux uses the solid-phase velocity $w$ and the solid fraction $(1 - \phi)$.[^berner1980] The distinction between porewater and solid velocities is critical in compacting sediments, where the solid framework moves downward faster than the interstitial fluid.

In a typical marine sediment, advection is burial: the continuous rain of particles from the water column buries the sediment column downward, carrying porewater and solid phases with it. In groundwater systems, advection is groundwater flow, driven by hydraulic gradients.

The total flux combines both:

$$
F = -\phi \cdot D_s \cdot \frac{\partial C}{\partial x} + \phi \cdot u \cdot C
$$

Plug this into the conservation equation and you get:

$$
\frac{\partial (\phi C)}{\partial t} = \frac{\partial}{\partial x}\left(\phi D_s \frac{\partial C}{\partial x}\right) - \frac{\partial (\phi u C)}{\partial x} + \sum R_i
$$

This is the reaction-transport equation for a dissolved species in a porous medium. It looks intimidating, but every term is doing something you already understand: diffusion spreading things out, advection carrying things along, reactions creating or destroying.

## What reacts: rate expressions

The reaction terms $R_i$ are where the biology enters the equation. In a sediment, the major reactions are microbially mediated: aerobic respiration, denitrification, manganese reduction, iron reduction, sulfate reduction, methanogenesis. Each one oxidizes organic matter (or hydrogen, or methane) using a different terminal electron acceptor.

We built the kinetic framework for these reactions in earlier chapters. The key expressions are:

**Michaelis-Menten kinetics**[^michaelis1913_eq] for a single-substrate reaction:

$$
r = V_{\max} \cdot \frac{[S]}{[S] + K_m}
$$

**Dual-Monod kinetics** for respiration limited by both electron donor and acceptor:

$$
r = k_{\max} \cdot [B] \cdot \frac{[\text{TED}]}{[\text{TED}] + K_{m,\text{TED}}} \cdot \frac{[\text{TEA}]}{[\text{TEA}] + K_{m,\text{TEA}}}
$$

where $[B]$ is biomass concentration, and both electron donor (TED) and acceptor (TEA) act as independent rate-limiting factors.[^thullner2007]

**The thermodynamic factor** $F_T$ requires an explicit energy convention. A net rate must vanish when the coupled process has no driving force. A logistic gate $1/(1+\exp(\Delta G_r/(RT)))$ would still give $1/2$ at chemical equilibrium, so we will not use it as that law.

For one published formulation, define the remaining drive $f=-\Delta G_r-m\Delta G_p$, where $m$ is the ATP conserved per reaction and $\Delta G_p$ is the phosphorylation free energy. The factor is:

$$
F_T=1-\exp\left(-\frac{f}{\chi RT}\right)
$$

Here $\chi$ reflects the reaction mechanism. All energies and stoichiometric quantities must use a consistent reaction basis. This expression reaches zero at $f=0$, not generally at $\Delta G_r=0$. Its application needs an explicit domain and treatment of regulation or reverse flux; it is not a universal sediment rate law.[^jin2003_eq] The oxygen teaching model below uses a first-order sink without a thermodynamic factor.
A rate expression for a microbially mediated reaction can then be written:

$$
r = k_{\max} \cdot [B] \cdot \frac{[\text{TED}]}{[\text{TED}] + K_{m,\text{TED}}} \cdot \frac{[\text{TEA}]}{[\text{TEA}] + K_{m,\text{TEA}}} \cdot F_T
$$

Kinetics times thermodynamics. Supply times demand times feasibility. Let $r$ denote reaction progress on a stated volume basis. The substrate-only expressions give a positive forward rate; with an energetic factor, the net rate may be signed. For species $j$, $R_j=\nu_j r$ when $r$ is per bulk sediment volume, or $R_j=\phi\nu_j r$ when it is per porewater volume. The stoichiometric coefficient $\nu_j$ is negative for a reactant and positive for a product. $V_{\max}$ and $k_{\max}[B]$ must have the units of $r$. A positive respiration rate is not itself a positive source of oxygen. The biomass-specific rate constant $k_{\max}$ is distinct from the oxygen pilot's first-order $k$.

## Start with one species

Before coupling an ecosystem, try a single curve. Imagine a dark, fully saturated sediment, with oxygen held at $C_0$ at the surface and no flux through a lower boundary at depth $L$. Let depth $x$ increase downward. Keep porosity $\phi$ and diffusivity $D_s$ constant. Start with no oxygen in the interior and turn on the surface supply at $t=0$.

For this teaching example, let the porewater consumption rate be $q=kC$, where $k$ has units s$^{-1}$. The bulk sink is then $R=-\phi kC$:

$$
\frac{\partial(\phi C)}{\partial t}
=\frac{\partial}{\partial x}\left(\phi D_s\frac{\partial C}{\partial x}\right)-\phi kC.
$$

With constant porosity, $\partial C/\partial t=D_s\partial^2C/\partial x^2-kC$. At steady state the solution is:

$$
C_*(x)=C_0\frac{\cosh((L-x)/\ell)}{\cosh(L/\ell)},\qquad
\ell=\sqrt{\frac{D_s}{k}}.
$$

The length $\ell$ compares diffusive delivery with consumption. More rapid consumption makes the profile thinner. In a deep domain it approaches an exponential near the surface. At a finite sealed lower boundary, it flattens. Oxygen approaches low values without an exact zero at finite depth; a reported penetration depth needs a stated detection threshold.

Use $L=0.03$ m, $D_s=10^{-9}$ m$^2$/s, $k=10^{-5}$ s$^{-1}$, $\phi=0.8$, and $C_0=0.2$ mol/m$^3$ of porewater. These are illustrative choices, not observations from a field site. They give $\ell=0.01$ m and a steady inward oxygen flux of about 1.376 mmol/m$^2$/day. The bottom still contains about 19.87 $\mu$M oxygen. A 1 $\mu$M threshold would not be crossed inside this chosen domain.

Now we can ask whether a computer reproduces something we know. The companion finite-volume model compares its steady solution with this curve, checks that inflow balances consumption and accumulation, refines its grid and time step, and rejects negative concentrations without clipping them. These checks verify the calculation. They do not validate the first-order assumption against nature.

A steady profile alone identifies $k/D_s$, not $k$ and $D_s$ separately. An independent diffusivity or an additional flux or transient observation is needed to separate them. The companion fit therefore estimates only this ratio from clearly labeled synthetic observations. Its separate measured-data exercise asks which archived flux corresponds to the model and whether the data version is reproducible. The distinction matters: solving an equation correctly and choosing the right equation for a core are different tasks.

## Coupling: one organism's waste is another's substrate

In a real sediment, there are not three independent species obeying three independent equations. There are dozens of species, linked by shared reactions.

When aerobic respiration consumes oxygen and organic carbon, it produces CO$_2$ and water. The CO$_2$ affects pH, which affects carbonate equilibria, which affects calcium concentrations. When sulfate reduction consumes sulfate and organic carbon, it produces sulfide. The sulfide reacts with dissolved iron to precipitate iron sulfide minerals. The iron came from the dissolution of iron oxides, which was mediated by iron-reducing bacteria, which were competing with sulfate reducers for the same organic carbon.

Every reaction feeds into every other reaction through the shared pool of chemical species. This coupling is what makes a sediment column behave like an ecosystem rather than a collection of independent reactions.

In the conservation equation, coupling appears naturally. Each species has its own equation, with its own transport terms and its own reaction terms. But the reaction terms for different species share parameters: the rate of sulfate consumption appears (with a stoichiometric coefficient) in both the sulfate equation and the sulfide equation. The rate of organic matter oxidation appears in the equations for oxygen, sulfate, methane, DIC, alkalinity, and ammonium. The equations are not independent. They are a coupled system, and they must be solved simultaneously.

This is what reaction-transport models do.[^steefel2005] Classic early-diagenetic models already used this strategy to couple carbon, oxygen, nitrogen, sulfur, iron, and manganese in a single redox-stratified sediment column.[^vancappellen1996_eq] They solve the coupled system -- all the conservation equations, all the transport terms, all the rate expressions -- simultaneously, in space and time. The output is a set of profiles: concentration as a function of depth (and time, if the system is not at steady state).

## The porewater profile, explained

Return to the profile that opened this chapter. We can now read it.

**Oxygen drops steeply** where net demand competes with resupply. Aerobic organic-matter respiration can contribute, but reduced inorganic compounds, sulfur oxidation linked to cable bacteria, and fauna can also matter. The O$_2$ profile alone does not apportion these sinks. A diffusion-only surface flux should be compared with diffusive oxygen uptake, rather than automatically equated with total chamber uptake.[^oxygen_sinks_eq] In the first-order example, a thin curve reflects the ratio $k/D_s$ and a stated boundary condition, not a unique biological mechanism.

**Sulfate declines gradually** in this sketch. Seawater sulfate can start at much higher concentrations than oxygen, but concentration alone does not establish a universally smaller rate constant for sulfate reduction. Both supply and net consumption shape a measured profile; the typical seawater concentrations provide context, not measurements represented by this drawing.[^millero2013] Under steady, constant-coefficient diffusion with a positive consumption rate $q$, the relation is $D_s C_{xx}=q$. Curvature can then constrain net consumption if $D_s$ is known. Advection, variable porosity, nonlocal exchange and changing concentrations alter that interpretation.[^berner1980]

**Methane rises from below** in the sketch, suggesting a deeper source such as methanogenesis in sulfate-depleted sediment. Methane diffuses upward, toward lower concentrations. At the sulfate-methane transition zone, it meets the descending sulfate, and the anaerobic oxidation of methane (AOM) consortium consumes both.[^knittel2009] In a measured profile, the width of the overlap zone can constrain reaction relative to transport, given actual concentrations, transport coefficients and boundary conditions. The graphical crossing in this sketch supplies none of those constraints. The classic AOM consortium illustrates a syntrophic partnership: archaea and bacteria associated in methane oxidation under a limited energy budget. This example does not establish an obligatory partnership for every methane-oxidation pathway.[^knittel2009] The same coupled reaction-transport logic has been used to estimate methane escape from passive and active continental margins, where small changes in bioenergetics or transport shift the seafloor methane flux substantially.[^dale2008_eq]

A measured profile can become a test of this bookkeeping. Transport and reactions together shape its gradients and curvature. Our opening sketch only illustrates that idea; it is not a solution of a coupled system. The oxygen curve we have just derived is a solution we can check.

## One equation, all scales

**The conservation framework does not change with scale.**

The same conservation principle that describes oxygen diffusing into a millimeter-thick surface layer of sediment describes sulfate declining over a meter of marine mud. The same principle, expressed through different transport operators (advection-dominated flow instead of diffusion-dominated), describes nitrate attenuation in a kilometer-scale aquifer plume. The same principle, with yet different operators (wind-driven mixing instead of molecular diffusion), describes CO$_2$ uptake by the global ocean.

$$
\frac{\partial \hat{C}}{\partial t} = -\frac{\partial F}{\partial x} + \sum R_i
$$

The $F$ changes -- not just its parameters but its mathematical form. The $R_i$ changes. The geometry changes. What persists is the conservation law itself: accumulation equals net flux plus net reaction.

This is more than analogy. The conservation law is the same physical principle in each case. But the transport operators, boundary conditions, and closure terms differ enough between a sediment pore and the Southern Ocean that calling the models "identical" would overstate the case. What is identical is the accounting: mass in, mass out, mass transformed. The organisms differ. The minerals differ. The timescales differ by factors of millions. The bookkeeping does not.

Why? Because conservation of mass is not a biological principle, or a geological principle, or a chemical principle. It is a physical principle. It does not care whether the reacting species is sulfate in a pore or CO$_2$ in the atmosphere. It does not care whether the transport mechanism is molecular diffusion or ocean circulation. It cares only that matter is neither created nor destroyed, and that the accounting balances.

This shared accounting is the reason that reaction-transport models are portable. A model calibrated on one fjord's sediment can provide a starting framework for another fjord[^boudreau1997]. Useful predictions still require checking the new site's transport, boundary conditions, reaction parameters and independent observations. A model built for early diagenesis can be adapted for groundwater contamination, because the coupling between transport and reaction works the same way in both settings.

The portability is not infinite. Parameters must be recalibrated. Biology adapts. New reactions become important at new scales. But the framework -- the conservation equation, the transport operators, the rate expressions -- carries across. It is the scaffold on which all the site-specific details hang.

## What we sacrificed

The equation we have built is powerful. It is also wrong -- in the precise, useful sense that all models are wrong.

Here is what we assumed and what we set aside:

**Steady-state biology.** The rate expressions treat the microbial community as a fixed catalyst: a set of rate constants and half-saturation constants that do not change with time. Real communities adapt. They shift their gene expression, change their community composition, and enter dormancy.[^stolpovsky2011_eq] For a particular core near steady state, fixed effective rates may be a useful approximation, provided the measurement period and conditions support it. For perturbed systems -- a contaminated aquifer receiving a fresh plume, a sediment exposed to a sudden change in overlying water chemistry -- it is not. Modeling the lag phase and community adaptation remains an open problem.

**No explicit objective function.** The rate laws in this chapter do not tell microbes to maximize growth, yield, or community energy harvest. They encode local constraints: substrate supply, electron acceptors, thermodynamic throttling, biomass, decay. That matters for the argument of this book. The equations already behave more like bookkeeping systems than like optimization problems. A formal satisficing model would need stronger machinery than this chapter provides. What this framework can do, already, is represent overlapping viable metabolisms without pretending that any guild is solving for a global best state.

**Effective rate constants.** The $k_{\max}$ and $K_m$ values in our rate expressions are not fundamental properties of individual enzymes. They are effective parameters that lump together the effects of enzyme kinetics, cell physiology, community composition, and pore-scale transport. They are fit to data, not derived from first principles. This means they work in the conditions where they were calibrated and may not transfer to new conditions. A truly predictive model would derive its rate parameters from thermodynamics and enzyme kinetics alone. We are not there yet.

**No pore-scale heterogeneity.** The conservation equation treats the sediment as a continuum: smooth gradients, averaged concentrations, representative elementary volumes. Real sediments have hot spots -- microzones of intense activity around organic particles, biofilms on grain surfaces, channels and burrows that short-circuit diffusion. These features matter at the pore scale, and they are invisible to the continuum equation.

**One dimension.** The equation as written is one-dimensional: depth only. Real sediments have lateral variability. Real aquifers have three-dimensional flow fields. The extension to multiple dimensions is mathematically straightforward (replace $\partial/\partial x$ with $\nabla$) but computationally expensive and data-hungry.

These are real limitations, and we state them here so that the equation earns no undeserved trust. But the limitations are not fatal. They define the frontier -- the place where the current framework runs out of answers and new science is needed. The equation is the best tool we have. It is also the starting point for whatever replaces it.

## Takeaway

- The conservation equation $\partial \hat{C} / \partial t = -\partial F / \partial x + \sum R_i$ is the single equation on which all reaction-transport models rest. It says: accumulation = transport + reaction.
- Transport has two components: molecular diffusion (Fick's law, $F \propto -D \, \partial C / \partial x$) and advection ($F \propto u \cdot C$). The diffusion timescale $\tau \sim L^2/D$ must be compared with consumption and the actual boundary and flow conditions.
- Reaction terms combine Michaelis-Menten kinetics (supply limitation), dual-Monod kinetics (donor + acceptor limitation), and the thermodynamic factor $F_T$ (limitation by a specified coupled driving force).
- Coupling between species arises naturally: shared reaction terms link the equations for oxygen, sulfate, methane, iron, and all other species into a system that must be solved simultaneously.
- The conservation law carries across scales: the same accounting principle -- accumulation equals flux plus reaction -- applies whether the system is a sediment pore, an aquifer, or the global ocean. The transport operators and closure terms change, but the framework is portable.
- The model assumes steady-state biology, effective rate constants, continuum averaging, and one-dimensionality. These assumptions define the current frontier; relaxing them is the work of the next generation of models.

[^berner1980]: Robert A. Berner, *Early Diagenesis: A Theoretical Approach* (Princeton University Press, 1980). The conservation equation framework for sediment geochemistry. [@Berner1980Early]

[^fick1855]: Adolf Fick, "Ueber Diffusion," *Annalen der Physik* 170 (1855): 59–86. [@Fick1855]

[^ligregory1974]: Diffusion coefficients for major ions in seawater and sediment: Yuan-Hui Li and Sandra Gregory, "Diffusion of Ions in Sea Water and in Deep-Sea Sediments," *Geochimica et Cosmochimica Acta* 38 (1974): 703–714. [@LiGregory1974]

[^michaelis1913_eq]: Leonor Michaelis and Maud Menten, "Die Kinetik der Invertinwirkung," *Biochemische Zeitschrift* 49 (1913): 333–369. [@Michaelis1913]

[^jin2005_eq]: The thermodynamic factor $F_T$ and its coupling with Monod kinetics: Qusheng Jin and Craig M. Bethke, "Predicting the Rate of Microbial Respiration in Geochemical Environments," *Geochimica et Cosmochimica Acta* 69 (2005): 1133–1143. [@Jin2005]

[^knittel2009]: Katrin Knittel and Antje Boetius, "Anaerobic Oxidation of Methane: Progress with an Unknown Process," *Annual Review of Microbiology* 63 (2009): 311–334. [@Knittel2009]

[^millero2013]: Seawater concentrations from Frank J. Millero, *Chemical Oceanography*, 4th ed. (CRC Press, 2013). [@Millero2013]

[^steefel2005]: Carl I. Steefel, Donald J. DePaolo, and Peter C. Lichtner, "Reactive Transport Modeling: An Essential Tool and a New Research Approach for the Earth Sciences," *Earth and Planetary Science Letters* 240 (2005): 539–558. [@Steefel2005]

[^boudreau1997]: Bernard P. Boudreau, *Diagenetic Models and Their Implementation* (Springer, 1997). The definitive reference on implementing reaction-transport models for sediment diagenesis, including detailed treatment of tortuosity corrections, boundary conditions, and numerical solution methods. [@Boudreau1997Diagenetic]

[^thullner2007]: Martin Thullner, Pierre Regnier, and Philippe Van Cappellen, "Modeling Microbially Induced Carbon Degradation in Redox-Stratified Subsurface Environments: Concepts and Open Questions," *Geomicrobiology Journal* 24 (2007): 139--155. Comprehensive treatment of dual-Monod kinetics and biomass dynamics in redox-stratified systems. [@Thullner2007]

[^vancappellen1996_eq]: Philippe Van Cappellen and Yifeng Wang, "Cycling of Iron and Manganese in Surface Sediments: A General Theory for the Coupled Transport and Reaction of Carbon, Oxygen, Nitrogen, Sulfur, Iron, and Manganese," *American Journal of Science* 296 (1996): 197--243. A landmark multicomponent reaction-transport model for redox-stratified sediments. [@VanCappellen1996]

[^dale2008_eq]: A. W. Dale, Philippe Van Cappellen, D. R. Aguilera, and Pierre Regnier, "Methane Efflux from Marine Sediments in Passive and Active Margins: Estimations from Bioenergetic Reaction-Transport Simulations," *Earth and Planetary Science Letters* 265 (2008): 329--344. [@Dale2008]

[^stolpovsky2011_eq]: Konstantin Stolpovsky et al., "Incorporating Dormancy in Dynamic Microbial Community Models," *Ecological Modelling* 222 (2011): 3092--3102. [@Stolpovsky2011]

[^jin2003_eq]: Qusheng Jin and Craig M. Bethke, "A New Rate Law Describing Microbial Respiration," *Applied and Environmental Microbiology* 69 (2003): 2340--2348, equations 6 and 11. [@Jin2003]

[^oxygen_sinks_eq]: Laurine D. W. Burdorf et al., "Electrogenic Sulfur Oxidation by Cable Bacteria in Two Seasonally Hypoxic Coastal Systems," *Estuarine, Coastal and Shelf Science* 297 (2024): 108615; Hannah Beck and Kanchan Maiti, "The Importance of Fauna-Mediated Sediment O2 Consumption in the NGOM Hypoxic Zone," *Frontiers in Marine Science* 12 (2025): 1532999. Attribution depends on the study design and its assumptions. [@Burdorf2024; @BeckMaiti2025]

[^auer2025_eq]: F. Auer et al., "Extensive Oxygen Consumption in the Intertidal Infiltration Zone of Beach Aquifers: The Impact of Seasonal Input, Filtration Efficiency, and Morphodynamics," *Journal of Geophysical Research: Biogeosciences* 130 (2025): e2024JG008291. [@Auer2025]
