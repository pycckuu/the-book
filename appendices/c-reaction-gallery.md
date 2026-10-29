---
title: "Reaction Gallery"
---

This appendix collects the key biogeochemical reactions referenced throughout the book. The redox ladder is a useful organizing picture, followed here by chemolithotrophic metabolisms, photosynthesis, and abiotic reference reactions. It is not a universal ranking of microbial competitors.[^appc-bethke2011]

For a specified chemical reaction, $\Delta G = \Delta G^\circ + RT\ln Q$, with dimensionless activities referenced to the stated standard states. For a matched fixed-pH convention, use $\Delta G' = \Delta G^{\circ\prime} + RT\ln Q'$; the proton reservoir is already accounted for and must not be counted again in $Q'$. Temperature, species, phases, standard states and the reaction basis belong with any quoted energy (Chapter 1).[^appc-conventions1994]

The two energies quoted below use Thauer and colleagues' historical pH 7 convention at 25°C: gases referenced to 1 atm, dissolved species to the unit-activity molal reference, and water as pure liquid. Their prime notation fixes the proton activity for specified species; it must not be transferred without checking to a dataset that groups protonation species or fixes additional reservoirs. The other equations illustrate material balances without supplying thermodynamic input values.[^appc-thauer1977]

CH$_2$O is an idealized organic-carbon unit in the heterotrophic balances. Its stoichiometry matches formaldehyde, but it does not specify a phase or a universal energy of formation for organic matter. The NOSC framework (Appendix A) characterizes carbon oxidation state; a whole-reaction energy also requires the other reactants, products and their conditions.

## Aerobic Respiration

Oxygen is a powerful electron acceptor. Its local supply and the rates of consumption and transport help determine where aerobic respiration can operate.

$$
\text{CH}_2\text{O} + \text{O}_2 \rightarrow \text{CO}_2 + \text{H}_2\text{O}
$$

Reaction Gibbs energy does not by itself give an ATP yield; that requires the cell's coupling mechanism and conditions (Chapter 1). In sediments, aerobic respiration consumes oxygen within the top millimeters to centimeters, creating the anoxic zone below (Chapter 8).

## Denitrification

Nitrate as terminal electron acceptor. First anaerobic metabolism in the redox sequence.

$$
5\text{CH}_2\text{O} + 4\text{NO}_3^- + 4\text{H}^+ \rightarrow 5\text{CO}_2 + 2\text{N}_2 + 7\text{H}_2\text{O}
$$

Produces dinitrogen gas (N$_2$), removing bioavailable nitrogen from the system. Environmentally significant in groundwater remediation and wastewater treatment (Chapter 10).

## Manganese Reduction

Manganese(IV) oxides as terminal electron acceptor.

$$
\text{CH}_2\text{O} + 2\text{MnO}_2 + 4\text{H}^+ \rightarrow \text{CO}_2 + 2\text{Mn}^{2+} + 3\text{H}_2\text{O}
$$

Often quantitatively minor in marine sediments because MnO$_2$ concentrations are low, but important in specific environments (Chapter 8, Chapter 9).

## Iron Reduction

Ferric iron as terminal electron acceptor.

$$
\text{CH}_2\text{O} + 4\text{Fe(OH)}_3 + 8\text{H}^+ \rightarrow \text{CO}_2 + 4\text{Fe}^{2+} + 11\text{H}_2\text{O}
$$

Bethke and colleagues distinguish energy stored through ATP coupling from reaction energy and show that a fixed competitive hierarchy does not follow from thermodynamics alone. Mineral form and water composition also matter.[^appc-bethke2011] Where ferric iron is supplied as mineral surfaces or colloids, the kinetics of cell-mineral attachment can become part of the rate limitation [@Bonneville2006]. The released Fe$^{2+}$ can precipitate with sulfide as iron sulfides, which may later convert to pyrite (FeS$_2$), or with carbonate as siderite (FeCO$_3$); the sulfide route links the iron and sulfur cycles.

## Sulfate Reduction

Sulfate as terminal electron acceptor.

With organic matter as electron donor:

$$
2\text{CH}_2\text{O} + \text{SO}_4^{2-} + 2\text{H}^+ \rightarrow 2\text{CO}_2 + \text{H}_2\text{S} + 2\text{H}_2\text{O}
$$

With hydrogen as electron donor (Chapters 1 and 4): the equation below uses HS$^-$ as the sulfide species, whereas those chapters write H$_2$S. Converting between them requires the corresponding proton balance. The reference energy must match the chosen reaction and thermodynamic convention.

$$
4\text{H}_2\text{(g)} + \text{SO}_4^{2-}\text{(aq)} + \text{H}^+\text{(aq)} \rightarrow \text{HS}^-\text{(aq)} + 4\text{H}_2\text{O}\text{(l)}
$$

$\Delta G^{\circ\prime} \approx -152$ kJ per mol of reaction as written (Thauer et al., Table 14, reaction 54). H$^+$ is shown to balance the chemical equation; the quoted value uses the fixed pH 7 reference, so its activity is not an additional factor in $Q'$. This is not an energy per mole of organic carbon or an environmental yield.

Sulfate reduction is ancient, though how widespread it was before the Great Oxidation Event — when ocean sulfate concentrations were far lower — remains debated. In modern marine sediments, where sulfate is abundant (~28 mM in seawater), sulfate reducers are major players. The sulfate-methane transition zone, where sulfate reduction meets methanogenesis, is one of the most studied features in porewater geochemistry (Chapter 8).

## Methanogenesis

Carbon dioxide as terminal electron acceptor -- the bottom of the redox ladder. Methanogenesis is not heterotrophic respiration but a distinct anaerobic metabolism performed exclusively by archaea.

Hydrogenotrophic methanogenesis (Chapter 4):

$$
4\text{H}_2\text{(g)} + \text{CO}_2\text{(g)} \rightarrow \text{CH}_4\text{(g)} + 2\text{H}_2\text{O}\text{(l)}
$$

$\Delta G^{\circ\prime} \approx -131$ kJ per mol of reaction as written (Thauer et al., p. 118). There is no net proton in this specified-species equation; its gas reference is not a dissolved-gas reference or a field energy estimate.

Acetoclastic methanogenesis:

$$
\text{CH}_3\text{COOH} \rightarrow \text{CH}_4 + \text{CO}_2
$$

Methanogenesis can operate at small energy returns, but a standard number does not establish a universal margin or exclusion by sulfate reducers. Shared substrates, local activities, supply and physiology determine competition and possible coexistence (Chapters 1 and 4).[^appc-bethke2011]

## Anaerobic Methane Oxidation (AOM)

Sulfate-driven anaerobic methane oxidation, carried out by consortia of anaerobic methanotrophic archaea and sulfate-reducing bacteria (Chapter 8):

$$
\text{CH}_4 + \text{SO}_4^{2-} \rightarrow \text{HCO}_3^- + \text{HS}^- + \text{H}_2\text{O}
$$

Among the least energetically favorable reactions in the microbial repertoire. AOM consumes an estimated 90% of the methane produced in marine sediments before it can reach the water column, making it one of the most important biological filters on Earth's greenhouse gas budget [@Knittel2009].

## Nitrification

A two-step chemolithotrophic process: ammonia oxidation followed by nitrite oxidation.

Step 1 -- Ammonia oxidation:

$$
\text{NH}_4^+ + \tfrac{3}{2}\text{O}_2 \rightarrow \text{NO}_2^- + 2\text{H}^+ + \text{H}_2\text{O}
$$

Step 2 -- Nitrite oxidation (Chapter 5):

$$
\text{NO}_2^- + \tfrac{1}{2}\text{O}_2 \rightarrow \text{NO}_3^-
$$

Nitrification links the reduced and oxidized ends of the nitrogen cycle. Both steps as written use O$_2$, so in sediments nitrification is largely confined to the oxic zone. Chapter 5 describes an exception: anoxygenic phototrophs that oxidize nitrite to nitrate using light.

## Anammox

Anaerobic ammonium oxidation -- ammonium oxidized with nitrite as the electron acceptor.

$$
\text{NH}_4^+ + \text{NO}_2^- \rightarrow \text{N}_2 + 2\text{H}_2\text{O}
$$

Anammox was first reported from a wastewater reactor in the mid-1990s; in 1999 Strous and colleagues identified the responsible organism as a previously unknown planctomycete [@Strous1999]. It removes bioavailable nitrogen without requiring oxygen. It is now used in wastewater treatment and contributes to fixed-nitrogen loss in oxygen-minimum zones, where its share relative to denitrification varies.

## Iron Oxidation

Chemolithotrophic oxidation of ferrous iron.

$$
4\text{Fe}^{2+} + \text{O}_2 + 10\text{H}_2\text{O} \rightarrow 4\text{Fe(OH)}_3 + 8\text{H}^+
$$

*Ferroplasma acidiphilum* (Appendix E) illustrates a modern iron-dependent metabolism. In acidic environments the abiotic rate is slow enough to leave iron-oxidizing microorganisms a kinetic window [@Golyshina2000]. The equation shows the circumneutral product. At the low pH where *F. acidiphilum* grows (optimum about 1.7), much of the ferric iron stays dissolved as Fe$^{3+}$ rather than precipitating as Fe(OH)$_3$.

## Sulfide Oxidation

Chemolithotrophic oxidation of hydrogen sulfide.

$$
\text{H}_2\text{S} + 2\text{O}_2 \rightarrow \text{SO}_4^{2-} + 2\text{H}^+
$$

Energetically generous. Sulfide-oxidizing bacteria thrive at redox interfaces where H$_2$S from below meets O$_2$ from above -- the same interface that defines the boundary between the sulfate and oxygen zones in sediment profiles.

## Photosynthesis

### Oxygenic photosynthesis

Water-splitting reaction (Chapter 5):

$$
6\text{CO}_2 + 6\text{H}_2\text{O} + \text{light} \rightarrow \text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2
$$

The reaction that oxygenated the atmosphere. The electron donor is water; the waste product is molecular oxygen (Chapter 5) [@Buick2008; @Blankenship2010].

### Anoxygenic photosynthesis

Using hydrogen sulfide as electron donor (Chapter 4):

$$
\text{CO}_2 + 2\text{H}_2\text{S} + \text{light} \rightarrow \text{CH}_2\text{O} + 2\text{S}^0 + \text{H}_2\text{O}
$$

Anoxygenic photosynthesis is widely thought to have preceded the oxygenic kind, but the dates and the size of the gap remain inferences (Chapters 4 and 5). No oxygen is produced; elemental sulfur is the waste product [@Blankenship2010].

## Abiotic Reference Reactions

### Silicate weathering

The long-term thermostat of Earth's climate (Chapter 10):

$$
\text{CaSiO}_3 + \text{CO}_2 \rightarrow \text{CaCO}_3 + \text{SiO}_2
$$

Consumes CO$_2$; rate enhanced by plant roots and microbial activity in soils [@Walker1981; @Berner1983].

### Hydrogen-chlorine reaction

A classic demonstration of kinetic inhibition:

$$
\text{H}_2 + \text{Cl}_2 \rightarrow 2\text{HCl}
$$

A mixture of H$_2$ and Cl$_2$ can sit indefinitely at room temperature (kinetically inhibited), but light of a suitable wavelength can split Cl$_2$ and start a chain reaction that may become explosive. Any quoted reaction energy would require specified phases, standard states and temperature. Thermodynamics says "yes"; kinetics says "not yet."

### Radiolytic hydrogen production

One proposed energy source for deep-subsurface communities (Chapter 9):

$$
2\text{H}_2\text{O} \xrightarrow{\text{radiation}} 2\text{H}_2 + \text{O}_2
$$

The equation is a net balance. Radiation from the decay of uranium, thorium and potassium in crustal rocks splits water into H$_2$ and oxidants such as H$_2$O$_2$, which react with minerals rather than accumulating as free O$_2$. The H$_2$ can support some communities kilometers below the surface, such as the Mponeng fracture community in Chapter 9, independently of photosynthesis.

## The Redox Ladder (Summary)

A commonly used sequence of terminal electron-accepting processes, useful for interpreting redox zonation:

| Electron Acceptor | Product | Chapter |
|---|---|---|
| O$_2$ | H$_2$O | 5, 8 |
| NO$_3^-$ | N$_2$ | 8, 10 |
| MnO$_2$ | Mn$^{2+}$ | 8, 9 |
| Fe(OH)$_3$ | Fe$^{2+}$ | 8, 9 |
| SO$_4^{2-}$ | H$_2$S | 4, 8 |
| CO$_2$ | CH$_4$ | 4, 8 |

The distinction between reaction bases matters: an energy per mole of CH$_2$O oxidized is not on the same basis as an acetoclastic figure per mole of acetate. Acetoclastic methanogenesis is a dismutation of acetate, not the hydrogenotrophic CO$_2$ reduction represented by the last row. The latter has the $-131$ kJ per reaction gas-reference example above; it must not be inserted into a per-mol-CH$_2$O comparison. The bottom rung is therefore approximate, not an identical carbon-basis extension of the rows above it.

This sequence helps organize the porewater profiles in Chapter 8. It does not predict a unique community structure wherever transport is limited: mineral phases, activities, substrate supply and physiological constraints can change energetic comparisons, allow overlap and support coexistence.[^appc-bethke2011]

[^appc-thauer1977]: Rudolf K. Thauer, Kurt Jungermann, and Karl Decker, "Energy conservation in chemotrophic anaerobic bacteria," *Bacteriological Reviews* 41(1) (1977): 100-180, DOI [10.1128/br.41.1.100-180.1977](https://doi.org/10.1128/br.41.1.100-180.1977). See p. 148 for conventions, p. 118 for the gas-phase methane reaction, and Table 14, reaction 54 and notes (p. 152), for sulfate reduction to HS$^-$. Erratum: 41(3): 809, DOI [10.1128/br.41.3.809-809.1977](https://doi.org/10.1128/br.41.3.809-809.1977). [@Thauer1977]

[^appc-bethke2011]: Craig M. Bethke, Robert A. Sanford, Matthew F. Kirk, Qusheng Jin, and Theodore M. Flynn, "The thermodynamic ladder in geomicrobiology," *American Journal of Science* 311(3) (2011): 183-210, DOI [10.2475/03.2011.01](https://doi.org/10.2475/03.2011.01). Tables 1-3 (pp. 186, 188, 192) distinguish the specified environment, reaction basis and energy capture; discussion on pp. 205-206 limits a fixed competitive hierarchy. [@Bethke2011]

[^appc-conventions1994]: IUBMB-IUPAC Joint Commission on Biochemical Nomenclature, "Recommendations for Nomenclature and Tables in Biochemical Thermodynamics" (1994), sections 4.1-4.3 and 5.1, [official recommendations](https://iubmb.qmul.ac.uk/thermod/). Chemical and transformed conventions are used as in Chapter 1. [@IUPACIUBMB1994]
