---
title: "The Budget of the Universe"
---

2.8 kilometers below South Africa, a microbial community lives in water filling fractures in the rock. Sunlight does not reach it. Its dominant bacterium, *Candidatus Desulforudis audaxviator*, can use hydrogen supplied by radiolytic chemistry and sulfate derived from minerals.

The setting was chemically energy-rich. Yet Lin and colleagues estimated population turnover times of 45 to 300 years under their stated assumptions. They inferred extremely slow long-term activity.[^lin2006_deep] How can such slow population turnover coexist with abundant chemical energy?

To answer, we will follow how a cell obtains energy from a chemical reaction and what it can spend that energy on. We will need the same reasoning in marine sediments and groundwater: how much energy is available, and how quickly can a cell obtain it?

## What a cell needs energy for

A cell does work. It builds molecules, moves ions across a membrane, and sometimes powers a flagellar motor. These activities require energy. It spends part of the energy it captures on maintenance; only part can support growth and reproduction.

A cell exchanges matter and energy with its surroundings. Its energy balance must therefore include changes outside the cell. Maintaining its internal organization carries a cost; staying alive does not by itself mean there is energy left for rapid growth.

For our bacterium, the energy source involves the conversion of hydrogen and sulfate. Hydrogen donates electrons, while sulfate accepts them in a reduction reaction. We therefore call hydrogen an electron donor and sulfate an electron acceptor. To establish whether the cell can obtain energy from that conversion, we need to consider the whole reaction, including its reactants and products.

## How much work can a reaction supply?

Thermodynamics provides a tool for this accounting: Gibbs free energy. Josiah Willard Gibbs developed it in the 1870s.[^gibbs1873] We are interested in its change during a reaction, written $\Delta G$.

At a specified temperature and pressure, the sign of $\Delta G$ shows whether the reaction is favorable in the direction we have written:

- If $\Delta G < 0$, the reaction is thermodynamically favorable. A cell may capture part of the energy it releases for work. The sign alone does not establish how much the cell can capture or how quickly.
- If $\Delta G > 0$, the reaction needs an additional energy source. A cell can, for example, couple it to a sufficiently favorable process so that the combined balance allows the conversion.
- If $\Delta G = 0$, this reaction is at equilibrium, with no net thermodynamic driving force. Other reactions in the same environment need not be at equilibrium.

This gives us a first way to assess a cell's possibilities. We write the reaction and ask whether it can supply work under the conditions at hand. Before calculating, though, we need to specify those conditions.

## Why the same reaction can give different returns

Picture two pores in a rock. Their temperatures are the same, their reactants are equally available, and the same reaction is favorable in both. Products are carried away from the first pore but accumulate in the second. The chemical equation has not changed, but the reaction supplies less energy in the second pore.

A reference value for reaction energy is therefore not enough. It describes specified standard states of the substances involved. To calculate the energy in natural water, we must account for its composition and temperature:

$$
\Delta G = \Delta G^\circ + RT \ln Q
$$

Here $\Delta G^\circ$ is the standard reaction Gibbs energy, $R$ is the gas constant, and $T$ is absolute temperature. The reaction quotient, $Q$, accounts for the relative amounts of products and reactants. The calculation uses chemical activities, which account for both the amount of each substance and interactions between the components of the solution. Activities are expressed relative to chosen standard states. Dilute concentrations can sometimes approximate these activities.

With the other conditions unchanged, accumulating products increases $Q$. The reaction Gibbs energy becomes less negative, reducing the energy return. Removing products has the opposite effect. The availability of reactants also changes the balance.

We can now explain the difference between the two pores: more products have accumulated in the second, so the same written reaction supplies less energy. We have not yet established how quickly cells metabolize in either pore. That requires the next part of the explanation.

## Why a favorable energy balance is not enough

Return to the bacterium using hydrogen and sulfate. Even with a negative $\Delta G$, a reaction can be too slow to supply the cell with energy. Before becoming products, the reactants must cross an activation barrier, an energy threshold along the reaction pathway. The overall energy return and the height of that barrier describe different aspects of the reaction.

Enzymes, biological catalysts, provide a reaction pathway with lower activation free-energy barriers. A slow reaction can then proceed fast enough to matter for the cell. The enzyme does not change the final $\Delta G$ or turn an unfavorable reaction into a favorable one.

Having a suitable enzyme still does not determine the rate of metabolism. The rate at which reactants reach the cell also matters. To assess an energy source, we therefore need the reaction's energy return as well as information about catalysis and supply.

This is why we separated two questions at the start. A large store of chemical energy does not by itself mean a cell can obtain energy rapidly. Slow life deep in the crust is consistent with an energy-rich setting. Energy inventories alone cannot establish what limits its rate.

## What changes when cells share an environment?

So far, we have considered one cell's possibilities. In a community, cells draw on a shared environment: they consume reactants and release products. They thereby change the conditions that determine the energy return of their neighbors' reactions.

Two groups can compete for dissolved hydrogen in marine sediments. Sulfate reducers use it when reducing sulfate, while hydrogenotrophic methanogens use it to produce methane from carbon dioxide. The second group's name refers to its use of hydrogen. As hydrogen is consumed, the reactions become less favorable if the other conditions remain unchanged. Measuring its concentration can therefore help us investigate which processes predominate. The closing sidebar gives the observations and limits of that inference.[^hoehler2001][^lovley1988][^oremland1982]

Energy return alone cannot explain which organisms will persist in a community. Enzyme repertoire, supply rates and maintenance costs also matter.

We will carry this way of reasoning into the rest of the book. First identify the reaction an organism uses. Then consider the environment's composition, the energy return, the reaction rate and the supply of reactants. This takes us from an individual cell to a community that changes its surroundings.

## From deep water to the early Earth

We now have an explanation for how life can obtain energy without sunlight, and a reason to distinguish an energy store from the rate at which a cell can use it. We will meet *D. audaxviator* again in the deep-biosphere chapter, where we will ask how long a community can persist with extremely slow metabolism.

The same physical constraints applied before the first cells, including in the hydrothermal settings considered by origin-of-life hypotheses.[^martinrussell2003] Knowing the rules of a reaction does not establish where suitable conditions existed or how long they lasted.

The next step in our story is therefore the planet itself. Before moving from chemistry to the first metabolisms, we need to understand how Earth retained liquid water, reactants and energy sources. That is the subject of the next chapter.

## Takeaway

- A cell needs energy for work and maintenance. It can capture only part of a reaction's energy return.
- At a specified temperature and pressure, a negative $\Delta G$ means the written reaction is thermodynamically favorable. It does not determine the rate.
- Environmental composition changes the energy return. A standard reaction energy alone is not enough for natural water.
- Enzymes lower activation barriers without changing the final thermodynamic balance. Reactant supply can also limit metabolism.
- In a community, cells change conditions for one another. Understanding the outcome requires reactions, environmental conditions and rates of exchange.

## If you want to check the calculation

The next two sidebars give definitions and a field example for readers who want the details. You can continue to the next chapter without them.

::: {.callout-note}
## Sidebar: what enters the energy balance

Erwin Schrödinger discussed the problem of maintaining order in a living system in his 1943 lectures.[^schrodinger1944] A complete thermodynamic balance must include the cell's exchanges with its surroundings: the Second Law applies to living systems too.

Gibbs free energy is defined as

$$
G = H - TS
$$

Here $T$ is absolute temperature, $S$ is entropy, and $H$ is enthalpy. Enthalpy is $H = U + PV$, where $U$ is internal energy, $P$ is pressure, and $V$ is volume. Entropy measures the spread of microscopic possibilities; for equally probable accessible microstates, $S = k_B\ln\Omega$. It is not simply their number.

At constant temperature and pressure, $\Delta G = \Delta H - T\Delta S$. For a closed process, $-\Delta G$ bounds the non-expansion work that can be delivered, with the bound reached reversibly. For a cell, the complete accounting must include exchanges with its surroundings.[^thermod1994]

In $\Delta G = \Delta G^\circ + RT\ln Q$, the gas constant $R$ is 8.314 J mol$^{-1}$ K$^{-1}$. The dimensionless reaction quotient $Q$ is the ratio of product activities to reactant activities, each raised to the power of its stoichiometric coefficient. Activities are relative to the standard states at the stated temperature and account for departures from ideal solution behavior.

At equilibrium, $Q$ equals the equilibrium constant $K_{\text{eq}}$, and $\Delta G = 0$. It follows that

$$
\Delta G^\circ = -RT \ln K_{\text{eq}}
$$

For biochemical reactions at a specified pH, often pH 7, a transformed convention is useful: $\Delta G' = \Delta G^{\circ\prime} + RT\ln Q'$. Its reactants and quotient must match that convention. The proton reservoir is already accounted for and must not be added again as an ordinary proton-activity factor. Temperature, pH and other relevant solution conditions must accompany the reference data.[^thermod1994]

For organic compounds, nominal carbon oxidation state can help screen oxidation-half-reaction energies. The complete donor-acceptor reaction still requires its own Gibbs accounting; accessibility and the environment also affect reactivity.[^ch01_larowe2011] [Appendix A](../appendices/a-energy-toolkit.md) develops this tool.

[Appendix D](../appendices/d-math-without-pain.md) develops the quantum description of molecular energy levels and the link between statistical models and thermodynamics.[^atkins2010]
:::

::: {.callout-note}
## Sidebar: what hydrogen can tell us about marine sediments

Two guilds can compete for dissolved H$_2$ in marine sediment: sulfate reducers and hydrogenotrophic methanogens. Their balanced chemical equations, before choosing a transformed convention:

**Sulfate reduction:**

$$4\text{H}_2 + \text{SO}_4^{2-} + 2\text{H}^+ \longrightarrow \text{H}_2\text{S} + 4\text{H}_2\text{O}$$

**Hydrogenotrophic methanogenesis:**

$$4\text{H}_2 + \text{CO}_2 \longrightarrow \text{CH}_4 + 2\text{H}_2\text{O}$$

As H$_2$ is consumed, the reaction quotient rises and the forward reaction becomes less favorable, with the other activities held fixed. A cell needs both sufficient energy per reaction and a sufficient rate of energy supply. Apparent minimum reaction energies estimated in one marine sediment were about $-19$ kJ per mol sulfate and $-11$ kJ per mol methane; these are condition-dependent field estimates, not a universal single-ion price.

Lovley and Goodwin reported steady-state H$_2$ concentrations of roughly 1 to 1.5 nM in sediments dominated by sulfate reduction and 7 to 10 nM where methane production predominated. Those associations illustrate competition for shared hydrogen; they are not universal stopping concentrations. Methanogenesis can coexist with sulfate reduction when substrates do not impose the same competition.

Calculating a hydrogen threshold requires the other reactant and product activities, temperature, a minimum-yield criterion, and consistent thermodynamic reference data. The H$_2$ ranges alone do not reproduce a boundary or uniquely predict sediment zonation.

I borrow Simon's term *satisficing* for an idea we will revisit: communities may persist in states that are adequate under local constraints. This is a hypothesis to test, not proof that microbes never optimize. Even overlapping zones of different redox processes do not settle the issue, since optimization models can also produce coexistence.[^simon1956]
:::

[^schrodinger1944]: Erwin Schrödinger, *What Is Life? The Physical Aspect of the Living Cell* (Cambridge University Press, 1944). [@Schrodinger1944]

[^gibbs1873]: Willard Gibbs, "A Method of Geometrical Representation of the Thermodynamic Properties of Substances by Means of Surfaces" (1873). [@Gibbs1873]

[^thermod1994]: IUBMB-IUPAC Joint Commission on Biochemical Nomenclature, "Recommendations for Nomenclature and Tables in Biochemical Thermodynamics" (1994), sections 4.1 to 4.3 and 5.1: chemical and transformed conventions, and thermodynamic definitions. [@IUPACIUBMB1994]

[^atkins2010]: Peter Atkins and Loretta Jones, *Chemical Principles: The Quest for Insight* (2010). [@Atkins2010]

[^ch01_larowe2011]: Douglas E. LaRowe and Philippe Van Cappellen, "Degradation of Natural Organic Matter: A Thermodynamic Analysis," *Geochimica et Cosmochimica Acta* 75 (2011): 2030-2042, sections 3.1 and 3.3. The oxidation-half-reaction proxy is not a complete metabolic yield or a universal reactivity law. [@LaRowe2011]


[^martinrussell2003]: William Martin and Michael J. Russell, "On the Origins of Cells," *Philosophical Transactions of the Royal Society B* 358 (2003): 59–85. [@MartinRussell2003]

[^lin2006_deep]: Li-Hung Lin et al., "Long-Term Sustainability of a High-Energy, Low-Diversity Crustal Biome," *Science* 314 (2006): 479-482. Turnover is a conditional population estimate, not directly observed cell division. Dylan Chivian et al., "Environmental Genomics Reveals a Single-Species Ecosystem Deep within Earth," *Science* 322 (2008): 275-278, supplies the organism identity and sampled fluid-phase genomic evidence. [@Lin2006; @Chivian2008]

[^simon1956]: Herbert A. Simon, "Rational Choice and the Structure of the Environment," *Psychological Review* 63 (1956): 129-138. William R. Harcombe et al., "Metabolic Resource Allocation in Individual Microbes Determines Ecosystem Interactions and Spatial Dynamics," *Cell Reports* 7 (2014): 1104-1115, demonstrates coexistence in a biomass-optimizing model of laboratory communities, not universal sediment validity. [@Simon1956; @Harcombe2014]

[^hoehler2001]: Tori M. Hoehler et al., "Apparent Minimum Free Energy Requirements for Methanogenic Archaea and Sulfate-Reducing Bacteria in an Anoxic Marine Sediment," *FEMS Microbiology Ecology* 38 (2001): 33-41. Apparent minima were $-19.1 \pm 1.7$ kJ per mol sulfate and $-10.6 \pm 0.7$ kJ per mol methane under the sampled conditions. [@Hoehler2001]

[^lovley1988]: Derek R. Lovley and Steve Goodwin, "Hydrogen Concentrations as an Indicator of the Predominant Terminal Electron-Accepting Reactions in Aquatic Sediments," *Geochimica et Cosmochimica Acta* 52 (1988): 2993–3003. [@Lovley1988]

[^oremland1982]: Ronald S. Oremland and Sandra Polcin, "Methanogenesis and Sulfate Reduction: Competitive and Noncompetitive Substrates in Estuarine Sediments," *Applied and Environmental Microbiology* 44 (1982): 1270-1276. The reported coexistence depends on substrate competition; it is not an assertion of unrestricted hydrogenotrophic coexistence. [@OremlandPolcin1982]
