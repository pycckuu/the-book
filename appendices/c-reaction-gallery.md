---
title: "Reaction Gallery"
---

This appendix collects the key biogeochemical reactions referenced throughout the book. Reactions are organized by the redox ladder -- from the most energetically favorable electron acceptors to the least -- followed by chemolithotrophic metabolisms, photosynthesis, and abiotic reference reactions. Standard-state values are reported at 25°C and 1 atm. Most entries use $\Delta G^\circ$; where the main text uses the biochemical standard state at pH 7, values are written as $\Delta G^{\circ\prime}$. Under environmental conditions, actual $\Delta G$ values differ according to $\Delta G = \Delta G^\circ + RT \ln Q$ (Chapter 1). The values here are representative standard-state benchmarks drawn from classic biochemical and geochemical thermodynamic sources; exact numbers vary with pH, speciation, and reaction convention [@Thauer1977; @Stumm1995; @Bethke2011].

The organic matter in heterotrophic reactions is represented as CH$_2$O (formaldehyde), the simplest reduced carbon compound. Real organic matter has variable composition and oxidation state; the NOSC framework (Appendix A) provides a way to estimate energy content for arbitrary organic molecules.

## Aerobic Respiration

The most energetically favorable heterotrophic metabolism. Dominates wherever oxygen is available.

$$
\text{CH}_2\text{O} + \text{O}_2 \rightarrow \text{CO}_2 + \text{H}_2\text{O}
$$

$\Delta G^\circ = -475$ kJ/mol

Yields roughly an order of magnitude more ATP per glucose molecule than anaerobic pathways (Chapter 5). In sediments, aerobic respiration consumes oxygen within the top millimeters to centimeters, creating the anoxic zone below (Chapter 8).

## Denitrification

Nitrate as terminal electron acceptor. First anaerobic metabolism in the redox sequence.

$$
5\text{CH}_2\text{O} + 4\text{NO}_3^- + 4\text{H}^+ \rightarrow 5\text{CO}_2 + 2\text{N}_2 + 7\text{H}_2\text{O}
$$

$\Delta G^\circ = -453$ kJ/mol (per mol CH$_2$O)

Produces dinitrogen gas (N$_2$), removing bioavailable nitrogen from the system. Environmentally significant in groundwater remediation and wastewater treatment (Chapter 10).

## Manganese Reduction

Manganese(IV) oxides as terminal electron acceptor.

$$
\text{CH}_2\text{O} + 2\text{MnO}_2 + 4\text{H}^+ \rightarrow \text{CO}_2 + 2\text{Mn}^{2+} + 3\text{H}_2\text{O}
$$

$\Delta G^\circ = -349$ kJ/mol

Often quantitatively minor in marine sediments because MnO$_2$ concentrations are low, but important in specific environments (Chapter 8, Chapter 9).

## Iron Reduction

Ferric iron as terminal electron acceptor.

$$
\text{CH}_2\text{O} + 4\text{Fe(OH)}_3 + 8\text{H}^+ \rightarrow \text{CO}_2 + 4\text{Fe}^{2+} + 11\text{H}_2\text{O}
$$

$\Delta G^\circ = -114$ kJ/mol

Iron reducers yield 4--5 times more energy per mole of electron donor than methanogens, giving them a competitive advantage where ferric iron is available (Chapter 9) [@Bethke2011]. Where ferric iron is supplied as mineral surfaces or colloids, the kinetics of cell-mineral attachment can become part of the rate limitation [@Bonneville2006]. The released Fe$^{2+}$ can precipitate as pyrite (FeS$_2$) or siderite (FeCO$_3$), linking the iron and sulfur cycles.

## Sulfate Reduction

Sulfate as terminal electron acceptor.

With organic matter as electron donor:

$$
2\text{CH}_2\text{O} + \text{SO}_4^{2-} + 2\text{H}^+ \rightarrow 2\text{CO}_2 + \text{H}_2\text{S} + 2\text{H}_2\text{O}
$$

$\Delta G^\circ = -77$ kJ/mol (per mol CH$_2$O)

With hydrogen as electron donor (Chapter 4):

$$
4\text{H}_2 + \text{SO}_4^{2-} + 2\text{H}^+ \rightarrow \text{H}_2\text{S} + 4\text{H}_2\text{O}
$$

$\Delta G^{\circ\prime} = -152$ kJ/mol

Sulfate reduction is ancient, though how widespread it was before the Great Oxidation Event — when ocean sulfate concentrations were far lower — remains debated. In modern marine sediments, where sulfate is abundant (~28 mM in seawater), sulfate reducers are major players. The sulfate-methane transition zone, where sulfate reduction meets methanogenesis, is one of the most studied features in porewater geochemistry (Chapter 8).

## Methanogenesis

Carbon dioxide as terminal electron acceptor -- the bottom of the redox ladder. Methanogenesis is not heterotrophic respiration but a distinct anaerobic metabolism performed exclusively by archaea.

Hydrogenotrophic methanogenesis (Chapter 4):

$$
4\text{H}_2 + \text{CO}_2 \rightarrow \text{CH}_4 + 2\text{H}_2\text{O}
$$

$\Delta G^{\circ\prime} = -131$ kJ/mol

Acetoclastic methanogenesis:

$$
\text{CH}_3\text{COOH} \rightarrow \text{CH}_4 + \text{CO}_2
$$

$\Delta G^\circ = -36$ kJ/mol

Methanogens operate on the thinnest energy margins of any major anaerobic metabolism. They lose the competition for hydrogen and acetate wherever sulfate is available, which is why methanogenesis dominates only below the sulfate depletion zone (Chapter 9).

## Anaerobic Methane Oxidation (AOM)

Sulfate-driven anaerobic methane oxidation, carried out by consortia of anaerobic methanotrophic archaea and sulfate-reducing bacteria (Chapter 8):

$$
\text{CH}_4 + \text{SO}_4^{2-} \rightarrow \text{HCO}_3^- + \text{HS}^- + \text{H}_2\text{O}
$$

$\Delta G^\circ = -17$ kJ/mol

Among the least energetically favorable reactions in the microbial repertoire. AOM consumes an estimated 90% of the methane produced in marine sediments before it can reach the water column, making it one of the most important biological filters on Earth's greenhouse gas budget [@Knittel2009].

## Nitrification

A two-step chemolithotrophic process: ammonia oxidation followed by nitrite oxidation.

Step 1 -- Ammonia oxidation:

$$
\text{NH}_4^+ + \tfrac{3}{2}\text{O}_2 \rightarrow \text{NO}_2^- + 2\text{H}^+ + \text{H}_2\text{O}
$$

$\Delta G^\circ = -275$ kJ/mol

Step 2 -- Nitrite oxidation (Chapter 5):

$$
\text{NO}_2^- + \tfrac{1}{2}\text{O}_2 \rightarrow \text{NO}_3^-
$$

$\Delta G^\circ = -76$ kJ/mol

Nitrification links the reduced and oxidized ends of the nitrogen cycle. It is strictly aerobic, which is why nitrate production ceases at the oxygen boundary in sediments.

## Anammox

Anaerobic ammonium oxidation -- ammonium oxidized with nitrite as the electron acceptor.

$$
\text{NH}_4^+ + \text{NO}_2^- \rightarrow \text{N}_2 + 2\text{H}_2\text{O}
$$

$\Delta G^\circ = -358$ kJ/mol

Discovered in the late 1990s, anammox removes bioavailable nitrogen without requiring oxygen [@Strous1999]. It is now recognized as a major route of fixed-nitrogen loss in both oxygen-minimum zones and engineered wastewater systems.

## Iron Oxidation

Chemolithotrophic oxidation of ferrous iron.

$$
4\text{Fe}^{2+} + \text{O}_2 + 10\text{H}_2\text{O} \rightarrow 4\text{Fe(OH)}_3 + 8\text{H}^+
$$

$\Delta G^\circ = -44$ kJ/mol (per mol Fe, at pH 7)

*Ferroplasma acidiphilum* (Appendix E) illustrates a modern iron-dependent metabolism. In acidic environments the abiotic rate is slow enough to leave iron-oxidizing microorganisms a kinetic window [@Golyshina2000].

## Sulfide Oxidation

Chemolithotrophic oxidation of hydrogen sulfide.

$$
\text{H}_2\text{S} + 2\text{O}_2 \rightarrow \text{SO}_4^{2-} + 2\text{H}^+
$$

$\Delta G^\circ = -798$ kJ/mol

Energetically generous. Sulfide-oxidizing bacteria thrive at redox interfaces where H$_2$S from below meets O$_2$ from above -- the same interface that defines the boundary between the sulfate and oxygen zones in sediment profiles.

## Photosynthesis

### Oxygenic photosynthesis

Water-splitting reaction (Chapter 5):

$$
6\text{CO}_2 + 6\text{H}_2\text{O} + \text{light} \rightarrow \text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2
$$

$\Delta G^\circ = +2870$ kJ/mol (endergonic; driven by light energy)

The reaction that oxygenated the atmosphere. The electron donor is water; the waste product is molecular oxygen (Chapter 5) [@Buick2008; @Blankenship2010].

### Anoxygenic photosynthesis

Using hydrogen sulfide as electron donor (Chapter 4):

$$
\text{CO}_2 + 2\text{H}_2\text{S} + \text{light} \rightarrow \text{CH}_2\text{O} + 2\text{S}^0 + \text{H}_2\text{O}
$$

Preceded oxygenic photosynthesis by at least several hundred million years. No oxygen is produced; elemental sulfur is the waste product [@Blankenship2010].

## Abiotic Reference Reactions

### Silicate weathering

The long-term thermostat of Earth's climate (Chapter 10):

$$
\text{CaSiO}_3 + \text{CO}_2 \rightarrow \text{CaCO}_3 + \text{SiO}_2
$$

Consumes CO$_2$; rate enhanced by plant roots and microbial activity in soils [@Walker1981; @Berner1983].

### Hydrogen-chlorine reaction

The non-equilibrium demonstration from Chapter 1:

$$
\text{H}_2 + \text{Cl}_2 \rightarrow 2\text{HCl}
$$

$\Delta G^\circ = -191$ kJ/mol

A mixture of H$_2$ and Cl$_2$ can sit indefinitely at room temperature (kinetically inhibited), but a single photon of the right wavelength triggers an explosive chain reaction. Chapter 1 estimated the reaction enthalpy from bond energies (~$-184$ kJ/mol); the standard Gibbs energy is slightly more negative. Thermodynamics says "yes"; kinetics says "not yet."

### Radiolytic hydrogen production

The energy source for the deep biosphere (Chapter 9):

$$
2\text{H}_2\text{O} \xrightarrow{\text{radiation}} 2\text{H}_2 + \text{O}_2
$$

Uranium and thorium decay in crustal rocks splits water molecules, producing H$_2$ that sustains microbial communities kilometers below the surface -- independent of photosynthesis.

## The Redox Ladder (Summary)

The terminal electron acceptor sequence, ordered by decreasing energy yield per mole of CH$_2$O oxidized:

| Electron Acceptor | Product | $\Delta G^\circ$ (kJ/mol CH$_2$O) | Chapter |
|---|---|---|---|
| O$_2$ | H$_2$O | $-475$ | 5, 8 |
| NO$_3^-$ | N$_2$ | $-453$ | 8, 10 |
| MnO$_2$ | Mn$^{2+}$ | $-349$ | 8, 9 |
| Fe(OH)$_3$ | Fe$^{2+}$ | $-114$ | 8, 9 |
| SO$_4^{2-}$ | H$_2$S | $-77$ | 4, 8 |
| CO$_2$ | CH$_4$ | $-36$ | 4, 8 |

Values are per mole of CH$_2$O oxidized, except the methanogenesis entry, which is the acetoclastic figure (per mole acetate) listed above; hydrogenotrophic CO$_2$ reduction (CO$_2$ + 4H$_2$) yields $-131$ kJ/mol per reaction. The bottom rung is therefore approximate and not on the identical per-mol-CH$_2$O basis as the rows above it.

This is the sequence that produces the layered porewater profiles in Chapter 8 and the predictable community structures in Chapter 9. It emerges wherever transport is limited and biology is present -- in sediments, in aquifers, and in contaminated groundwater (Chapter 10).
