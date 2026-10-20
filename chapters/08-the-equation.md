---
title: "Modeling the Invisible"
---

Imagine a sediment core in front of you. You want to know where oxygen can reach and where methane might escape. The drawing offers a first clue: three curves, for oxygen, sulfate, and methane. Concentration runs along the x-axis; depth below the sediment-water interface increases downward along the y-axis. This is an imagined marine sediment, a thought experiment drawn with smooth analytic functions rather than measurements from a core.

In the sketch, oxygen falls steeply below the interface. Sulfate stays high near the surface and declines farther down. Methane rises from below. The relative scales show a possible arrangement, not concentrations or detection limits measured at a particular site.

![Schematic porewater profiles, drawn from analytic functions rather than measured data. The curve shapes are not solutions of a reaction-transport balance, so their curvature does not indicate where species are produced or consumed. Each curve uses a relative concentration scale; their plotted crossing illustrates a transition and does not locate a measured sulfate-methane transition.](../sources/img/ch8_porewater_profile.png){#fig-porewater-profile}

The sketch places sulfate falling and methane rising around a transition horizon. In a measured core, we would locate the sulfate-methane transition from actual concentrations and the processes that connect them, not from the crossing of separately scaled curves. Neither its width nor its reaction rate can be read from this drawing.

A familiar biological explanation is anaerobic oxidation of methane by archaea associated with sulfate-reducing bacteria. One balanced net reaction is:

$$
\text{CH}_4 + \text{SO}_4^{2-} \longrightarrow \text{HCO}_3^- + \text{HS}^- + \text{H}_2\text{O}
$$

Knowing the organisms and the reaction gives us part of the story. For a measured core, though, we still need to explain the *shape* of the curves: why oxygen drops fast and sulfate drops slowly, why methane rises from below, and why the transition sits here rather than somewhere else. Naming a metabolism does not settle those questions. We need to follow the material as well as the organisms.

Let us follow the material through a small volume of sediment. Track what enters, what leaves, and what is produced or consumed inside. That bookkeeping turns a porewater profile into a quantitative story.

Written once and applied species by species, the same conservation law lets us ask: How far would the boundary move if organic matter delivery doubled? How much methane escapes if transport outruns biology?

One equation is enough to begin.

## Conservation: the only law you need

Every model in this book -- every profile, every flux, every prediction -- rests on a single principle: **mass is conserved**.[^berner1980] Whatever enters a volume of sediment must either leave it, react within it, or accumulate. There are no other options.

Picture a thin slab of sediment at depth $x$, with thickness $\Delta x$. We will keep track of one chemical species inside it. Call its bulk concentration $\hat{C}$: the amount per unit volume of sediment, not per unit volume of porewater. We will return to that distinction. The equation records how quickly $\hat{C}$ changes in the slab:

$$
\frac{\partial \hat{C}}{\partial t} = -\frac{\partial F}{\partial x} + \sum R_i
$$

Three terms. Each one does exactly one job. Here $\hat{C}$ is in mol per cubic meter of bulk sediment, $F$ in mol per square meter of sediment per second, and each $R_i$ in mol per cubic meter of bulk sediment per second. A porewater rate must be multiplied by porosity before it enters this bulk balance.

**The left side** ($\partial \hat{C} / \partial t$) is the rate of accumulation. If the concentration in the slab is increasing, this term is positive. If it is decreasing, this term is negative. At steady state -- when the profile is not changing with time -- this term is zero.

**The first term on the right** ($-\partial F / \partial x$) compares what enters with what leaves. $F$ is the flux: the amount of the species passing through a unit area per unit time. If more flows into the slab from above than flows out below, concentration increases. If more leaves than enters, it decreases. The mathematical name is the negative divergence of flux. The minus sign and the derivative perform the comparison for us.

**The second term** ($\sum R_i$) is the sum of all reactions that produce or consume the species. A reaction that produces the species contributes a positive $R_i$. A reaction that consumes it contributes a negative $R_i$. If there are multiple reactions acting on the same species -- which there always are -- you add them all up.

That is the entire equation. It says: the rate of change equals what comes in minus what goes out, plus what is produced minus what is consumed. It is an accounting identity, nothing more, nothing less.

A steady oxygen concentration can coexist with continuing reactions. When supply minus export matches consumption, the slab keeps the same oxygen inventory.

The ledger is in place. Now we need to find out how material crosses the slab and what happens to it inside.

## What moves: transport

Material can cross the slab because a concentration gradient drives diffusion or because flowing water carries it along. In most sediment and groundwater settings, these give the two components of the flux $F$: diffusion and advection.

**Molecular diffusion** moves dissolved species down their concentration gradients. The flux is:

$$
F_{\text{diff}} = -\phi \cdot D_s \cdot \frac{\partial C}{\partial x}
$$

where $\phi$ is porosity (the fraction of the sediment that is porewater), $D_s$ is the effective diffusion coefficient in the sediment (smaller than in free water, because the pore network is tortuous), and $C$ is the porewater concentration. The minus sign means stuff moves from high concentration to low. This is Fick's first law, applied to a porous medium.[^fick1855] Here $D_s$ includes the tortuosity correction, but not the separate porosity prefactor already present in the flux. Some conventions absorb porosity into a bulk diffusion coefficient; mixing the two conventions would count porosity twice.[^boudreau1997]

How long does that journey take? For diffusion over a distance $L$, a useful timescale is:

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

Read the right side as a list of actions: diffusion spreads material, advection carries it along, and reactions produce or consume it. The left side records the resulting change in what is stored. This is the reaction-transport equation for a dissolved species in a porous medium. The notation has grown, but the ledger has not changed.

## Start with one species

Before coupling an ecosystem, let us set up an experiment we can follow from the start. Imagine a dark, fully saturated sediment. Hold oxygen at $C_0$ at the surface and allow no flux through the lower boundary at depth $L$. Let depth $x$ increase downward, and keep porosity $\phi$ and diffusivity $D_s$ constant. There is no oxygen in the interior when we turn on the surface supply at $t=0$. Which steady oxygen profile follows from these boundaries and the sink we choose below?

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

![Oxygen at three saved startup times, at numerical cell centres. Depth is horizontal and concentration is per porewater volume. The dashed curve is a finite-domain steady analytical reference, not an exact transient. The analytical values are evaluated at cell centres, not exactly averaged over each cell. Times are displayed in days; a curve indistinguishable from zero on this linear scale does not establish exact depletion.](../courses/modeling-guide/figures/en/oxygen-depth-profiles.png){#fig-oxygen-worked-profile}

At first, oxygen accumulates while diffusion feeds the surface layers and the sink consumes it. The profiles approach the dashed steady curve, where inward supply balances consumption. This calculation follows oxygen alone; it does not solve for the sulfate and methane in our opening sketch.

We can now compare the computer's steady oxygen profile with this independent solution. The companion finite-volume model compares its steady solution with this curve, checks that inflow balances consumption and accumulation, refines its grid and time step, and rejects negative concentrations without clipping them. These checks verify the calculation. They do not validate the first-order assumption against nature.

A steady profile alone identifies $k/D_s$, not $k$ and $D_s$ separately. Imagine two versions of this same slab, with the same surface concentration, porosity and lower boundary. In the second, multiply both diffusivity $D_s$ and the consumption coefficient $k$ by two. The steady concentration profile is unchanged, although the inward flux doubles and the transient response is faster. More points on that same steady curve would not distinguish the two explanations. An independent diffusivity, flux or transient observation adds different information. The companion fit therefore estimates only the ratio from clearly labeled synthetic observations. Its separate measured-data exercise asks which archived flux corresponds to the model and whether the data version is reproducible. Solving the equation correctly and choosing it for a core remain different tasks.

## What reacts: rate expressions

The reaction terms $R_i$ are where the biology enters the equation. In a sediment, the major reactions are microbially mediated: aerobic respiration, denitrification, manganese reduction, iron reduction, sulfate reduction, methanogenesis. Each one oxidizes organic matter (or hydrogen, or methane) using a different terminal electron acceptor.

We have solved one profile with a deliberately simple consumption law. Before we couple species, we need to choose how their reactions enter the same ledger. The earlier chapters gave us ways to ask how a rate responds to substrate supply and to the available driving force. Here we bring those expressions together. Each answers a different part of the question: how fast can the reaction proceed?

**Michaelis-Menten kinetics**[^michaelis1913_eq] for a reduced single-enzyme reaction, under suitable approximation conditions:

$$
r = V_{\max} \cdot \frac{[S]}{[S] + K_m}
$$

**Dual-Monod kinetics** for respiration limited by both electron donor and acceptor:

$$
r = k_{\max} \cdot [B] \cdot \frac{[\text{TED}]}{[\text{TED}] + K_{m,\text{TED}}} \cdot \frac{[\text{TEA}]}{[\text{TEA}] + K_{m,\text{TEA}}}
$$

where $[B]$ is biomass concentration. Electron donor (TED) and acceptor (TEA) are represented by a separable empirical product in this closure; independence is an assumption, not a result of the single-enzyme law.[^thullner2007] The retained $K_m$ labels denote half-saturation parameters on each stated substrate basis, not automatically enzyme constants.

**The thermodynamic factor** $F_T$ requires an explicit energy convention. A net rate must vanish when the coupled process has no driving force. A logistic gate $1/(1+\exp(\Delta G_r/(RT)))$ would still give $1/2$ at chemical equilibrium, so we will not use it as that law.

For one published formulation, define the remaining drive $f=-\Delta G_r-m\Delta G_p$, where $m$ is the ATP conserved per reaction and $\Delta G_p$ is the phosphorylation free energy. The factor is:

$$
F_T=1-\exp\left(-\frac{f}{\chi RT}\right)
$$

Here $\chi$ reflects the reaction mechanism. All energies and stoichiometric quantities must use a consistent reaction basis. This expression reaches zero at $f=0$, not generally at $\Delta G_r=0$. Its application needs an explicit domain and treatment of regulation or reverse flux; it is not a universal sediment rate law.[^jin2003_eq] The oxygen teaching model above uses a first-order sink without a thermodynamic factor.
A rate expression for a microbially mediated reaction can then be written:

$$
r = k_{\max} \cdot [B] \cdot \frac{[\text{TED}]}{[\text{TED}] + K_{m,\text{TED}}} \cdot \frac{[\text{TEA}]}{[\text{TEA}] + K_{m,\text{TEA}}} \cdot F_T
$$

Kinetics times thermodynamics. Supply times demand times feasibility. Let $r$ denote reaction progress on a stated volume basis. The substrate-only expressions give a positive forward rate; with an energetic factor, the net rate may be signed. For species $j$, $R_j=\nu_j r$ when $r$ is per bulk sediment volume, or $R_j=\phi\nu_j r$ when it is per porewater volume. The stoichiometric coefficient $\nu_j$ is negative for a reactant and positive for a product. $V_{\max}$ and $k_{\max}[B]$ must have the units of $r$. A positive respiration rate is not itself a positive source of oxygen. The biomass-specific rate constant $k_{\max}$ is distinct from the oxygen pilot's first-order $k$.

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

## Coupling: one organism's waste is another's substrate

The single-species examples let us follow one ledger at a time. A real sediment does not stop at three independent species obeying three independent equations. Dozens of species are linked by shared reactions. A product of one reaction can become the reactant of the next.

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

The accounting survives the change in scale; the model must change with the system. Between a sediment pore and the Southern Ocean, transport operators, boundary conditions, reaction closures and geometry differ. Changing a few coefficients does not turn a pore-scale model into an ocean model. Organisms, minerals and timescales differ too. In each setting, we still account for what enters, what leaves, what reacts and what accumulates.

A model calibrated on one fjord's sediment can provide a starting framework for another fjord.[^boudreau1997] An early-diagenetic framework can also be adapted to groundwater contamination. In either case, useful predictions require checking the new site's transport, boundaries, reaction parameters and independent observations. Biology adapts, and new reactions can matter. Conservation lets us carry the accounting across; it does not remove the need to recalibrate parameters or test the new model.

## What we sacrificed

Before using the equation to interpret a real core, we need to be clear about its limits. The model keeps the bookkeeping explicit. It does not describe every feature of the sediment.

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

Continue with the oxygen exercises and worked answers listed in the book's appendices. Try each exercise before reading its solution.

[^berner1980]: Robert A. Berner, *Early Diagenesis: A Theoretical Approach* (Princeton University Press, 1980). The conservation equation framework for sediment geochemistry. [@Berner1980Early]

[^fick1855]: Adolf Fick, "Ueber Diffusion," *Annalen der Physik* 170 (1855): 59–86. [@Fick1855]

[^ligregory1974]: Diffusion coefficients for major ions in seawater and sediment: Yuan-Hui Li and Sandra Gregory, "Diffusion of Ions in Sea Water and in Deep-Sea Sediments," *Geochimica et Cosmochimica Acta* 38 (1974): 703–714. [@LiGregory1974]

[^michaelis1913_eq]: Leonor Michaelis and Maud Menten, "Die Kinetik der Invertinwirkung," *Biochemische Zeitschrift* 49 (1913): 333–369. [@Michaelis1913]


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
