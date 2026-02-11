# Book Bible (v0.1)

## One‑sentence promise
A physics‑minded, story‑driven guide to how microbes survive on tight energy budgets, why that creates predictable reaction patterns in sediments and groundwater, and how reaction–transport models turn those patterns into forecasts for methane, CO\(_2\), and water quality.

## Central thesis (three claims, nested)

1. **Satisficing, not optimizing.** Microbial communities do not maximize growth rate or energy yield. They satisfice -- they find strategies that cover maintenance costs under local thermodynamic and kinetic constraints. The distinction matters because optimization models predict sharp redox zonation and competitive exclusion, while satisficing models predict the fuzzy coexistence, overlap, and apparent inefficiency that field data actually show.

2. **One equation, all scales.** The conservation equation $\partial C / \partial t = -\partial F / \partial x + \Sigma R_i$ describes a sediment pore, an aquifer, and the global ocean. This is not analogy. The math is identical; only the parameters change. The book demonstrates this identity explicitly, from millimeters to the planet.

3. **Water quality is geomicrobiology.** Contaminated groundwater is a bioreactor. The same organisms, reactions, and constraints that shaped the Archean atmosphere operate in every aquifer plume today. We underperform at prediction because we treat water treatment as a pure engineering problem (fixed parameters, black-box biology) rather than a geomicrobiology problem (adaptive communities, thermodynamic constraints, coupled transport). The fix is not more data. It is better theory.

## Target reader
- Graduate students and working scientists in environmental science, geochemistry, and microbial ecology who want the conceptual bridge between microbiology and reactive transport modeling
- Environmental scientists/engineers who want intuition for RTMs without a "pure math" text
- Accessible to advanced undergraduates willing to engage with equations
- Anyone who's looked at a porewater profile and wanted to understand the processes behind its shape.

## Voice and style rules
- **Story‑first**: chapters open with a scene/paradox (field, lab, or “thought experiment”), then earn the abstractions.
- **Physics‑native metaphors**: use metaphors that genuinely map to the science (circuits, resistance, boundary layers), not cute mascots.
- **Rigor without heaviness**: keep the main narrative light; move derivations out of the flow.
- **No black boxes**: when we simplify, we say what we sacrificed (and what we kept).
- **Microbes are characters**: not cartoons—real organisms with constraints, strategies, and tradeoffs.
- **Concrete observables**: regularly return to what you would actually measure (profiles, fluxes, rates, proxies).

## Three‑layer reading (so nobody gets lost)
- **Main text**: story + intuition; minimal equations; emphasize constraints and "what would happen if…"
- **Equation Corner / Sidebar callouts**: 1–3 key equations, with units and meaning; one small back‑of‑the‑envelope estimate when helpful. Cap at 2 callouts per chapter.
- **Appendices**: clean derivations, extra math, and "if you want the full machinery" details
  - **Appendix A** (Energy Toolkit): Lineweaver-Burk, inhibition types, pH/temperature optima
  - **Appendix B** (Model Toolkit): diagenetic equation, transport terms, rate expressions, partial equilibrium, growth/yield/decay, software tools
  - **Appendix C** (Reaction Gallery): placeholder
  - **Appendix D** (Math Without Pain): Schrodinger equation derivation, molecular energy hierarchy, partition functions
  - **Appendix E** (Dramatis Personae): One-page cards for key organisms (*D. audaxviator*, *Synechococcus*, *B. subtilis*, *M. xanthus*, *Ruthia magnifica*, *Carsonella ruddii*, *Lokiarchaeota*, *Riftia pachyptila*, *Elysia viridis*)

## Physics‑forward mental models (recurring)
### Microbe as a battery + circuit
- **Electron donor** = anode (high chemical potential electrons)
- **Electron acceptor** = cathode (low chemical potential electrons)
- **Enzymes/kinetics** = internal resistance (how hard it is to move charge through the microbe’s machinery)
- **Transport limits** = external resistance (how hard it is to deliver reactants/remove products)
- **Power** \(\approx\) (energy per electron) \(\times\) (electron flux)

### Sediment as a reaction–diffusion medium
Redox “zones” are emergent structure, like boundary layers: they arise because transport is limited and reactions are selective.

### Thermodynamics vs kinetics (always together)
- **Thermodynamics**: available work (what is thermodynamically possible)
- **Kinetics + biology**: how fast the reaction proceeds; whether it covers maintenance; what is accessible under constraints

## A small toolkit of “back‑of‑the‑envelope” physics
Use short, satisfying estimates to anchor intuition:
- Diffusion timescale: \(\tau \sim L^2/D\)
- Energy–voltage bridge: \(\Delta G = -nF\Delta E\)
- Nernst intuition: \(E\) shifts with concentration via \(\ln Q\)
- Flux estimate: \(J \sim -D\,\partial C/\partial x\)

## Notation: keep a small alphabet
Prefer consistency over completeness.

- **Thermo**: \(\Delta G\), \(\Delta G^\circ\), \(Q\), \(K\), \(R\), \(T\), \(F\), \(n\)
- **Transport**: \(J\) (flux), \(D\) (diffusion), \(u\) or \(w\) (advection/burial velocity)
- **Concentrations vs activities**: pick one convention per chapter and state it once; park nuance in the Energy Toolkit appendix

## Chapter structure
1. Budget of the Universe -- energy, entropy, free energy
2. The Stage -- three planets, why Earth won
3. Spark -- first metabolisms, origin of life
4. The First City -- bacterial mats, Michaelis-Menten, biogeochemical cycles
5. The Poisoning -- oxygen, GOE, redox consequences
6. Cannibals and Voters -- microbial social behavior, quorum sensing, bistability
7. The Merger -- endosymbiosis, eukaryotic cell
8. The Equation -- conservation law, transport, rate expressions, scale invariance (Claim 2)
9. Cities Without Sunlight -- deep biosphere, satisficing, maintenance energy (Claim 1)
10. The Water Planet -- water quality, RTM applications, geomicrobiology vs engineering (Claim 3)
- Epilogue: What Is Life? -- three definitions, three claims, open questions

## What the book is (and is not)
- **Is**: a coherent bridge between geomicrobiology and modeling; a “why the model works” book
- **Is not**: a full RTM textbook, a code manual, or a comprehensive review of all metabolisms

## Repeating chapter pattern (consistent rhythm)
- Hook scene (1–2 pages)
- Concept: the biological/chemical rule
- Model: the minimal equation(s) that capture it (Equation Corner)
- Data: what you’d measure to test it
- Take‑home summary (5 bullets)

## Visual program (simple but frequent)
- Line‑drawn figures (zones, ladders, profiles, flux cartoons)
- “Microbe Cards” (half‑page): methanogens, sulfate reducers, iron reducers, cable bacteria (optional), Shewanella, deep subsurface specialists
- “Profile Detective” callouts: interpret one curve bend at a time

## References (practical)
- Keep citations light in the main text; put density in notes/appendices
- Add “Further reading” lists when a chapter touches a large literature

