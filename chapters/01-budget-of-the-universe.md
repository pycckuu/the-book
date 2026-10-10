---
title: "The Budget of the Universe"
---

2.8 kilometers below South Africa, a fracture-water community lives without sunlight. Its dominant bacterium, *Candidatus Desulforudis audaxviator*, can use hydrogen supplied by radiolytic chemistry and sulfate derived from minerals. Lin and colleagues estimated population turnover times of 45 to 300 years under stated assumptions; they did not watch individual cells divide on that schedule. The setting was chemically energy-rich, even though its inferred long-term activity was extremely slow.[^lin2006_deep]

This organism matters because it strips the problem to a different minimum: life supported by geological chemistry rather than sunlight. If you want to understand how microbes built the world, you can start here, with two questions that we must keep separate: how much usable energy a reaction releases, and how quickly that energy reaches a cell.

The question does require physics, but not the full lecture course. You only need three ideas: a reaction must actually pay under the conditions where the cell lives, not under imaginary textbook defaults; a favorable reaction can still be too slow to matter unless an enzyme lowers the barrier; and the local environment -- the concentrations of reactants and products, the temperature, the pH -- changes the arithmetic continuously, so that the same metabolism that works in one pore can fail in the next.

Erwin Schrödinger saw the problem early.[^schrodinger1944][^schrodinger_lectures] In 1943, he asked what physical rules a living system must obey simply to persist. His answer was austere and still correct: life does not evade thermodynamics. It survives by obeying thermodynamics in a way that keeps its own internal order from collapsing. A cell stays organized only by spending energy and exporting disorder to the surroundings. The accounting always balances.

This chapter keeps only the pieces of that accounting we will actually use in the story ahead: Gibbs free energy, real environmental conditions, and the distinction between favorable and fast. The deeper quantum scaffolding, why energy levels are discrete, why bonds have specific strengths, why light exchanges energy in quanta, lives in Appendix D for readers who want the full machinery.

## The budget: Gibbs free energy

In a marine sediment, sulfate reducers and hydrogenotrophic methanogens can share dissolved hydrogen. Their reactions must pay under local conditions, but thermodynamic yield alone does not decide which population grows: supply rates, kinetics, and other requirements also matter. To understand what a reaction can actually accomplish, whether it can build a molecule, pump an ion across a membrane, or power a flagellar motor, you need a sharper accounting tool.

Josiah Willard Gibbs built that tool in the 1870s.[^gibbs1873]


$$
G = H - TS
$$

Read it as a budget, with one caution: the spendable quantity is a change in free energy, not the absolute value of $G$. Enthalpy is $H = U + PV$, where $U$ is internal energy. Entropy measures the spread of microscopic possibilities; for equally probable accessible microstates, $S = k_B\ln\Omega$. It is not simply their number. At constant temperature and pressure, $\Delta G = \Delta H - T\Delta S$. For a closed process, $-\Delta G$ bounds the non-expansion work that can be delivered, with the bound reached reversibly.[^thermod1994]

At fixed temperature and pressure, the sign of $\Delta G$ gives the tendency of the specified reaction in the written direction:

- If $\Delta G < 0$: the forward reaction is thermodynamically favorable; this does not establish its rate or captured energy.
- If $\Delta G > 0$: the forward reaction needs driving, for example through coupling to a sufficiently favorable process.
- If $\Delta G = 0$: this reaction is at equilibrium, with no net thermodynamic drive; other reactions need not be at equilibrium.

The budget metaphor is useful if we keep that distinction: a favorable change supplies a return, and the cell can capture only part of it for maintenance, growth, or reproduction.

Microbes must cover costs. Their enzyme repertoire, substrate supply, and maintenance requirements constrain which reactions can sustain them; the largest positive energy return, $-\Delta G$, is not the only consideration. I borrow Simon's term *satisficing* as a lens: communities may persist in states that are adequate under local constraints. This is a hypothesis to test, not proof that microbes never optimize. Overlapping redox zones alone do not settle the issue, since optimization models can also produce coexistence.[^simon1956] The physics sets the menu; the local constraints shape what microbes can use.

### Real conditions, not standard ones

The standard reaction Gibbs energy $\Delta G^\circ$ is a reference for specified standard states at a stated temperature. The reaction quotient $Q$ is dimensionless and uses activities relative to those states; dilute concentrations may sometimes approximate them. Real environments require the actual temperature and activities, not just a standard number. To know the actual energy available, you need the master equation:

$$
\Delta G = \Delta G^\circ + RT \ln Q
$$

Here $R$ is the gas constant (8.314 J mol$^{-1}$ K$^{-1}$), $T$ is absolute temperature, and $Q$ is the **reaction quotient**---the ratio of product activities to reactant activities, each raised to the power of its stoichiometric coefficient.

The reaction quotient captures how concentrations shift the energy balance. When products accumulate, $Q$ increases, and $\Delta G$ becomes less negative: less energy is available. When reactants are abundant, $Q$ is small, and there is more energy to harvest. At equilibrium, $Q$ equals the equilibrium constant $K_{\text{eq}}$, and $\Delta G = 0$:

$$
\Delta G^\circ = -RT \ln K_{\text{eq}}
$$

The expression is a special case of the one above, evaluated at the point where the reaction has no net tendency to move in either direction.

For biochemical reactions at a specified pH, often pH 7, a transformed convention is useful: $\Delta G' = \Delta G^{\circ\prime} + RT\ln Q'$. Its reactants and quotient must match that convention. The proton reservoir is already accounted for and must not be added again as an ordinary proton-activity factor. Temperature, pH and other relevant solution conditions must accompany the reference data.[^thermod1994]

::: {.callout-note}
## Sidebar --- The hydrogen threshold

Two guilds can compete for dissolved H$_2$ in marine sediment: sulfate reducers and hydrogenotrophic methanogens. Their balanced chemical equations, before choosing a transformed convention:

**Sulfate reduction:**

$$4\text{H}_2 + \text{SO}_4^{2-} + 2\text{H}^+ \longrightarrow \text{H}_2\text{S} + 4\text{H}_2\text{O}$$

**Hydrogenotrophic methanogenesis:**

$$4\text{H}_2 + \text{CO}_2 \longrightarrow \text{CH}_4 + 2\text{H}_2\text{O}$$

As H$_2$ is consumed, the reaction quotient rises and the forward reaction becomes less favorable, with the other activities held fixed. A cell needs both sufficient energy per reaction and a sufficient rate of energy supply. Apparent minimum reaction energies estimated in one marine sediment were about $-19$ kJ per mol sulfate and $-11$ kJ per mol methane; these are condition-dependent field estimates, not a universal single-ion price.[^hoehler2001]

Lovley and Goodwin reported steady-state H$_2$ concentrations of roughly 1 to 1.5 nM in sediments dominated by sulfate reduction and 7 to 10 nM where methane production predominated.[^lovley1988] Those associations illustrate competition for shared hydrogen; they are not universal stopping concentrations. Methanogenesis can coexist with sulfate reduction when substrates do not impose the same competition.[^oremland1982]

Calculating a hydrogen threshold requires the other reactant and product activities, temperature, a minimum-yield criterion, and consistent thermodynamic reference data. The H$_2$ ranges alone do not reproduce a boundary or uniquely predict sediment zonation.
:::

::: {.callout-note}
## Sidebar --- Oxidation state as an energy proxy

A useful first screen for an organic molecule is the **average oxidation state of its carbon atoms**. It tells us about oxidation and electron transfer, not the complete energy yield.

Methane (CH$_4$) carbon is $-4$, glucose (C$_6$H$_{12}$O$_6$) averages 0, and carbon dioxide (CO$_2$) carbon is $+4$. Oxidizing methane to CO$_2$ transfers electrons, but the energy return still depends on the electron acceptor, products, and conditions.

Long-chain fatty acids are relatively reduced carboxylic acids; specified short-chain acids can be more oxidized. Fatty acids and carboxylic acids are not opposing categories.

The shortcut has a precise limit: LaRowe and Van Cappellen relate nominal carbon oxidation state to an oxidation-half-reaction energy estimate.[^larowe2011] That estimate can help screen compounds; the complete donor-acceptor reaction still requires its own Gibbs accounting.

Buried-carbon reactivity also depends on accessibility and the environment. Oxidation state alone is not a universal depth or freshness index.
:::

## Why favorable reactions still stall

A negative $\Delta G$ is permission, not speed: it tells you that a reaction can proceed, not whether it will proceed fast enough to matter for a cell.

The second half of the microbial energy problem appears here. A sulfate reducer can, in principle, earn a living by coupling hydrogen oxidation to sulfate reduction. But the reactants still have to cross an activation barrier before any useful chemistry occurs. Without a catalyst, that barrier can make a favorable reaction effectively inert on biological timescales.

Enzymes solve this problem without rewriting the thermodynamics. They do not make an unfavorable reaction favorable or change the final balance in the Gibbs ledger; they change the path, stabilizing intermediate states, lowering the activation cost, and making a reaction that would otherwise be geologically slow run on the timescale of metabolism.

The deeper reason molecules have specific bond energies, activation barriers, and wavelength thresholds is quantum-mechanical, and the full argument belongs in Appendix D.[^atkins2010] For the purposes of this book, two facts are enough: chemical bonds have definite energetic costs, and life survives only because enzymes turn thermodynamic permission into biological speed.

## The rules before the game

Planck introduced energy quanta in his account of thermal radiation,[^planck1901] and Einstein proposed light quanta.[^einstein1905] The wave nature of matter, confirmed experimentally in the 1920s and formalized by the Schrödinger equation, explains why atoms and molecules have discrete energy levels. From those energy levels come bond energies, activation barriers, and the electronic transitions that make photosynthesis and respiration possible.

Gibbs, working half a century before quantum mechanics, already had the thermodynamic framework: enthalpy minus the entropy term gives you the free energy. With the reaction quotient $Q$ adjusting for local conditions, you can calculate the energy available from any reaction in any environment.

The rules they uncovered, quantized energy, Gibbs free energy, chemical equilibrium, are the same rules that govern every metabolic reaction in every living cell that has ever existed. They would have constrained early chemistry, including the hydrothermal settings proposed in origin-of-life hypotheses.[^martinrussell2003] They govern the sulfate-reducing bacteria 2.8 kilometers underground in a South African gold mine today.[^lin2006_deep] Evolution operates within the Second Law: a cell can drive an unfavorable step by coupling it to a favorable process, and the complete accounting must include its exchanges with the surroundings.

*D. audaxviator*, 2.8 kilometers underground, obeys every rule in this chapter, and so does every other organism we will meet. The rules were set before the first cell divided.

## Takeaway

- The central question is not "how much energy exists?" but "how much useful work can a favorable chemical change supply, and how quickly can a cell capture it?"
- At fixed temperature and pressure, reaction Gibbs energy constrains chemical driving; actual activities enter through $\Delta G = \Delta G^\circ + RT\ln Q$. Use matching transformed quantities when pH is held fixed.
- Local concentrations matter. A metabolism that pays in one environment can fail in another because the reaction quotient changes the available energy.
- A favorable reaction is not necessarily a fast one. Enzymes do not change the final thermodynamic balance; they lower activation barriers so metabolism can run on biological timescales.
- The deeper quantum explanation sits in Appendix D. In the main text, the important point is simpler: every microbe in this book lives or dies by the same energy accounting.

[^schrodinger1944]: Erwin Schrödinger, *What Is Life? The Physical Aspect of the Living Cell* (Cambridge University Press, 1944). [@Schrodinger1944]

[^planck1901]: Max Planck, "Ueber das Gesetz der Energieverteilung im Normalspectrum," *Annalen der Physik* 309, no. 3 (1901): 553--563. [@Planck1901]

[^einstein1905]: Albert Einstein, "Concerning an Heuristic Point of View Toward the Emission and Transformation of Light" (1905). [@Einstein1905]

[^gibbs1873]: Willard Gibbs, "A Method of Geometrical Representation of the Thermodynamic Properties of Substances by Means of Surfaces" (1873). [@Gibbs1873]

[^thermod1994]: IUBMB-IUPAC Joint Commission on Biochemical Nomenclature, "Recommendations for Nomenclature and Tables in Biochemical Thermodynamics" (1994), sections 4.1 to 4.3 and 5.1: chemical and transformed conventions, and thermodynamic definitions. [@IUPACIUBMB1994]

[^atkins2010]: Peter Atkins and Loretta Jones, *Chemical Principles: The Quest for Insight* (2010). [@Atkins2010]

[^schrodinger_lectures]: The three lectures were delivered 5, 12, and 19 February 1943 at Trinity College Dublin. See Erwin Schrödinger, *What Is Life?* (Cambridge University Press, 1944), preface. [@Schrodinger1944]

[^larowe2011]: Douglas E. LaRowe and Philippe Van Cappellen, "Degradation of Natural Organic Matter: A Thermodynamic Analysis," *Geochimica et Cosmochimica Acta* 75 (2011): 2030-2042, sections 3.1 and 3.3. The oxidation-half-reaction proxy is not a complete metabolic yield or a universal reactivity law. [@LaRowe2011]


[^martinrussell2003]: William Martin and Michael J. Russell, "On the Origins of Cells," *Philosophical Transactions of the Royal Society B* 358 (2003): 59–85. [@MartinRussell2003]

[^lin2006_deep]: Li-Hung Lin et al., "Long-Term Sustainability of a High-Energy, Low-Diversity Crustal Biome," *Science* 314 (2006): 479-482. Turnover is a conditional population estimate, not directly observed cell division. Dylan Chivian et al., "Environmental Genomics Reveals a Single-Species Ecosystem Deep within Earth," *Science* 322 (2008): 275-278, supplies the organism identity and sampled fluid-phase genomic evidence. [@Lin2006; @Chivian2008]

[^simon1956]: Herbert A. Simon, "Rational Choice and the Structure of the Environment," *Psychological Review* 63 (1956): 129-138. William R. Harcombe et al., "Metabolic Resource Allocation in Individual Microbes Determines Ecosystem Interactions and Spatial Dynamics," *Cell Reports* 7 (2014): 1104-1115, demonstrates coexistence in a biomass-optimizing model of laboratory communities, not universal sediment validity. [@Simon1956; @Harcombe2014]

[^hoehler2001]: Tori M. Hoehler et al., "Apparent Minimum Free Energy Requirements for Methanogenic Archaea and Sulfate-Reducing Bacteria in an Anoxic Marine Sediment," *FEMS Microbiology Ecology* 38 (2001): 33-41. Apparent minima were $-19.1 \pm 1.7$ kJ per mol sulfate and $-10.6 \pm 0.7$ kJ per mol methane under the sampled conditions. [@Hoehler2001]

[^lovley1988]: Derek R. Lovley and Steve Goodwin, "Hydrogen Concentrations as an Indicator of the Predominant Terminal Electron-Accepting Reactions in Aquatic Sediments," *Geochimica et Cosmochimica Acta* 52 (1988): 2993–3003. [@Lovley1988]

[^oremland1982]: Ronald S. Oremland and Sandra Polcin, "Methanogenesis and Sulfate Reduction: Competitive and Noncompetitive Substrates in Estuarine Sediments," *Applied and Environmental Microbiology* 44 (1982): 1270-1276. The reported coexistence depends on substrate competition; it is not an assertion of unrestricted hydrogenotrophic coexistence. [@OremlandPolcin1982]
