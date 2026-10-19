---
title: "The First City"
---

What did the first self-sustaining communities look like?

Among the early answers the rock record preserves are stromatolites from about 3.43 billion years ago, interpreted as products of microbial communities.[^oldest_stromatolites] To explore how a community could work, picture a mat a few millimeters thick: green on top, pink beneath, dark below. Three zones, multiple metabolic guilds, and material passing between them. This is a thought experiment assembled from modern microbial physiology, not a recovered cross-section of an Archean community.

As the last chapter argued, a lone metabolism can persist where geological fluxes supply reactants and remove products. Biological partnerships offer another way to recycle them, but there is no universal threshold at which life must close its own loops. A sulfur oxidizer paired with a sulfur reducer is one plausible partnership under suitable conditions. The rock record preserves layered structures interpreted as microbial communities; it does not identify all their members or reconstruct their waste flows.

Mat-built structures are prominent in the Precambrian fossil record, across more than two billion years.[^mat_dominance] Their persistence does not show that one community design dominated all life or remained unchanged. Modern mats still offer a window into layered communities.[^sharkbay] Stromatolites preserve a long record of such structures, though preservation is uneven and their biological origin must be assessed in context.[^stromatolite_record] The scene invites a question: how can chemistry, gradients, and metabolic partnerships help a community persist?

## Three neighborhoods

A bacterial mat is not a uniform film. It is layered, and the layering is not accidental -- it is imposed by physics. Light attenuates with depth. Chemical gradients steepen. Each layer creates the boundary conditions for the layer below it, the way a city's infrastructure determines what can be built on each block.

The analogy to a city is more than decorative. A city works because different neighborhoods specialize: one district generates power, another processes waste, a third manufactures goods. A bacterial mat can contain similarly linked districts, defined by wavelength, chemistry, and metabolic strategy rather than zoning laws. How strongly they depend on one another also depends on supplies from outside the mat.

The metaphor has limits. A mat has no mayor, no planner, no hierarchy issuing instructions from the top. Gradients sort the organisms. Metabolism reshapes the gradients. Local interactions build the order.

![A hypothetical anoxygenic mat, using modern guilds to illustrate three zones: a green phototrophic canopy, a purple phototrophic middle, and a dark recycling zone. The chosen order is not a universal sequence or a reconstruction from Archean fossils. The reactions on the left are simplified balances; the sulfide-oxidation equations end at elemental sulfur. The sulfur loop on the right additionally assumes oxidation to sulfate, which those equations do not themselves describe. External supply and export are omitted from the drawing.](../sources/img/ch4_mat_cross_section.png){#fig-mat-cross-section}

### The green canopy

In our chosen top layer live green sulfur bacteria, anoxygenic phototrophs. This cast illustrates one possible arrangement. It does not fix the order in which photosynthetic lineages evolved or date the emergence of oxygenic photosynthesis.[^anoxygenic_evolution]

These surface-dwellers harvest sunlight, but their electron source in this example is not water. It is hydrogen sulfide, H$_2$S -- the same gas that gives rotten eggs their smell.[^h2s_phototrophs] The overall logic is straightforward: capture photons, use their energy to strip electrons from H$_2$S, and feed those electrons into carbon fixation. The displayed balance ends at elemental sulfur; some organisms can oxidize it further to sulfate, depending on their machinery and conditions:

$$
\text{CO}_2 + 2\,\text{H}_2\text{S} \xrightarrow{h\nu} \text{CH}_2\text{O} + 2\,\text{S}^0 + \text{H}_2\text{O}
$$

Sunlight supplies the driving energy, while H$_2$S can arrive from hydrothermal sources or reactions deeper in the mat. Its availability is a local condition, not a consequence of anoxia alone. Where sulfide, light, and the other nutrients suffice, the canopy is the city's power plant: it converts the primary energy input into organic carbon that other guilds can consume.

But there is a constraint that matters. The visible green or brown color reflects the combined absorption of bacteriochlorophylls and carotenoids; it is not a direct map of the wavelengths that power photosynthesis. In green sulfur bacteria, bacteriochlorophyll *c*, *d*, or *e* in chlorosome antennae absorbs strongly in the red and far-red, with peaks around 720--750 nm, transferring energy toward a bacteriochlorophyll *a* reaction center (P840).[^bchl_green] In the arrangement drawn here, the canopy therefore changes the spectrum reaching the next layer. Absorption, scattering, pigment abundance, and the incoming light all matter.

### The pink middle

Below our green canopy, the light is different. Some red and far-red light has been absorbed; near-infrared light can remain available. This is one possible filtered environment for a second phototrophic layer.

These are purple bacteria.[^purple_bacteria] Bacteriochlorophyll *a* or *b* lets different members of this group absorb near-infrared light, often around 800--900 nm, with some peaks beyond that range. This can create spectral niches.[^spectral_niche] But physics does not require green bacteria to sit above purple bacteria: a measured modern mat contained purple layers above a green sulfur bacterial layer. The drawing chooses an order to illustrate the principle, not to prescribe it.

The metabolic logic is similar to the top layer: capture photons, fix carbon, grow. For the sulfide-using guild chosen here, the simplified elemental-sulfur balance is the same. Longer wavelengths mean less energy per photon, since photon energy is inversely proportional to wavelength. That fact alone does not establish a smaller metabolic yield or tighter growth margin: absorbed photon flux and the photosynthetic machinery also matter. The pink layer is the city's secondary industry, using a different part of the available light.

Spectral partitioning is an observable feature of modern microbial mats.[^niche_partitioning] It is a plausible ingredient of ancient communities, but the age of this particular arrangement is not read directly from a stromatolite. The principle resembles a forest canopy: organisms reshape the light environment for their neighbors, here across millimeters rather than meters.

### The dark basement

Below the pink layer, the light is effectively gone. Whatever survives here must live without photons entirely. This is the mat's basement -- its recycling district -- and it runs on chemistry alone.

Several guilds can coexist in this dark zone. Their interactions offer possible recycling loops; whether those loops sustain the community depends on supply, export, and reaction rates.

**Fermenters** break down the organic matter that rains from above -- dead cells, exudates, structural polymers. Fermentation does not require an external electron acceptor; it reshuffles the carbon and hydrogen within organic molecules, producing a mix of small organic acids, alcohols, CO$_2$, and molecular hydrogen (H$_2$). The energy yield per molecule is modest, but the substrates are abundant.

**Sulfate reducers** can pick up where the fermenters leave off.[^sulfate_reduction] The H$_2$-using guild in our example reduces sulfate to hydrogen sulfide. Sulfate may enter from the surrounding water or be formed by sulfur oxidation within the mat:

$$
4\,\text{H}_2 + \text{SO}_4^{2-} + 2\,\text{H}^+ \longrightarrow \text{H}_2\text{S} + 4\,\text{H}_2\text{O}
$$

Read that equation carefully. If sulfur oxidizers produce sulfate above, sulfate reducers can return it to H$_2$S below. The elemental-sulfur reaction shown for the canopy is only part of that proposed loop: oxidation from S$^0$ to sulfate is an additional step. Internal recycling can regenerate fuel; it does not eliminate the need to balance external sulfur inputs and losses.

A caveat about scale: Archean seawater sulfate estimates are much lower than the modern ocean's roughly 28 millimolar, but they are model-dependent. A culture-based calibration suggested less than 200 micromolar; later reconstructions inferred roughly 80 micromolar for a 2.7-billion-year-old basin or less than 2.5 micromolar using a modern low-sulfate analog.[^archean_sulfate] These are different reconstructions, not measurements of one uniform Archean ocean. Short diffusion distances can help couple a thin mat, but trace sulfate alone does not demonstrate an adequate flux. Sulfate production, delivery, consumption, and sulfur losses must be checked.

**Methanogens** run a parallel operation. They too consume the H$_2$ from fermentation, but instead of reducing sulfate, they reduce CO$_2$ to methane:

$$
4\,\text{H}_2 + \text{CO}_2 \longrightarrow \text{CH}_4 + 2\,\text{H}_2\text{O}
$$

Methanogens and sulfate reducers can compete for the same electron donor, H$_2$.[^thermodynamic_competition] Adequate sulfate supply often favors sulfate reducers, while sulfate limitation can leave more H$_2$ available to methanogens. The outcome also depends on uptake kinetics, population sizes, other substrates, and transport. Neither the presence of sulfate nor a comparison of standard energy yields alone decides which guild persists. The redox ladder is a tendency shaped by local supply, not a rigid law.

Methanogens today inhabit many anoxic settings, including wetlands, rice paddies, landfills, and animal intestines.[^methanogens] Their persistence across such different environments shows how widespread the niche is. Organic carbon and low oxygen can support methane production, but do not guarantee it: usable substrates, suitable conditions, and methanogens must also be present.

## The beauty of the closed cycle

Step back and look at our mat as a single system. You see a proposed community with linked material flows, not a demonstrated closed system.

The top and middle layers fix CO$_2$ using sunlight and H$_2$S. Their simplified reactions produce elemental sulfur; further oxidation can supply sulfate. The dark layer ferments organic matter, producing H$_2$ and small molecules. Sulfate reducers can return sulfate to H$_2$S, while methanogens convert CO$_2$ to methane. Methane may escape or be consumed if suitable methane oxidizers and electron acceptors are present. Each arrow describes a possible process, not a recovered Archean flux.

Sunlight supplies energy, and the ocean supplies dissolved gases, nutrients, and minerals. Matter can also leave by diffusion, export, and burial. Heat carries part of the dissipated energy to the surroundings. Recycling can reduce dependence on fresh substrate supply, but neither the material budget nor the energy budget is closed.

This suggests a route to buffering fluctuations in external supply. If the ocean delivers less H$_2$S, an internal sulfur cycle might partially compensate, provided its sources and losses balance. If organic carbon accumulates, some may be consumed later, exported, or buried. Those alternatives affect both community persistence and the growing sedimentary structure.

Metabolic interdependence can help a community persist, but fossil recurrence does not establish continuous stability of one architecture.[^mat_stability] Remove fermenters and the internal H$_2$ supply may fall. Remove sulfate reducers and sulfide regeneration may decline, unless other sources compensate. Remove phototrophs and the local light-driven carbon input disappears. These are dependencies to measure, not a guarantee that every guild is indispensable. The community works within an environment.

## Stromatolites: the fossil cities

If bacterial mats were the living cities, stromatolites are their ruins.

A stromatolite is a layered sedimentary structure, often dome-shaped or columnar.[^stromatolite_formation] In mat-built examples, microorganisms can trap and bind grains and influence mineral precipitation. Photosynthetic CO$_2$ uptake can shift pH and carbonate saturation; other metabolisms, extracellular materials, and abiotic water chemistry also contribute. Successive growth, sediment accumulation, precipitation, and alteration can produce lamination. No single crust-growth sequence explains every stromatolite.

The result can be a laminated structure recording growth and environmental change. Among the oldest well-preserved examples interpreted as microbial are those of the roughly 3.43-billion-year-old Strelley Pool Formation in the Pilbara.[^oldest_stromatolites] The case rests on their shapes, sedimentary setting, and associations. A layered form alone is not proof of life, and even a microbial interpretation does not identify the specific guilds in our drawing.[^stromatolite_biosignatures]

You can still visit living stromatolites today. In Shark Bay, Western Australia, hypersalinity and other environmental stresses limit many competitors and grazers.[^sharkbay_modern] Cyanobacteria are important builders in these modern communities, which differ across sites and mat types. They are working ecosystems and useful analogs, not replicas of an Archean sulfur mat. Similar layering does not establish identical metabolisms or closed material loops.

The difference is context. Stromatolites are conspicuous in the Precambrian shallow-water rock record. That record does not establish mat dominance in every habitat or measure their share of global biomass. Mat-forming communities persist today in varied settings, including places where grazing and competition are reduced. The living examples let us investigate processes that ancient rocks preserve only incompletely.

## Reading the isotopes: fingerprints of ancient metabolism

What can isotopes tell us about carbon fixation in these communities? They provide clues, but not a roster of ancient guilds.

Carbon has two stable isotopes: ^12^C (six protons, six neutrons) and ^13^C (six protons, seven neutrons). Their different masses affect reaction and equilibrium behavior. Many carbon-fixation reactions preferentially incorporate the lighter isotope, but the size and direction of an isotope effect depend on the process and conditions.

Several carbon-fixation pathways exist: the Calvin cycle, the reverse TCA cycle used by green sulfur bacteria, the Wood-Ljungdahl pathway, and others.[^carbon_fixation_pathways] RuBisCO preferentially incorporates ^12^C during CO$_2$ fixation.[^rubisco][^carbon_fractionation] Cultured organisms using different pathways can show different carbon isotope discrimination. But the whole-cell signal also depends on CO$_2$ supply, uptake, and growth conditions. A numerical range is not a universal pathway label, and depleted organic carbon alone cannot identify our green canopy.

This isotopic fingerprint can survive geological time, but its interpretation needs the rock context. As Chapter 2 explains, reports of light carbon in ancient Greenland rocks involve distinct occurrences at Isua and Akilia. Their ages, alteration histories, and possible abiotic sources must be assessed separately.[^isua_carbon] Such carbon can be consistent with biological fixation without uniquely establishing its origin or the organisms responsible.

A similar story plays out with nitrogen. The enzyme nitrogenase, which fixes atmospheric N$_2$ into biologically usable ammonia (NH$_3$), also discriminates between isotopes.[^nitrogenase] Together, the carbon-fixation enzymes and nitrogenase are the key catalysts by which inorganic substances enter the biosphere -- the gatekeepers between the mineral world and the living one.

The quantitative framework for isotope fractionation -- the $\delta^{13}$C scale, its measurement, and its limitations as a biosignature -- is detailed in Appendix A.

## Microbes as geological agents

Microbial mats did not merely inhabit the early Earth -- they reshaped it. Photosynthetic CO$_2$ uptake can raise local pH and favor carbonate precipitation where water chemistry permits it; sulfate reduction supplies sulfide that can react with available metals; iron oxidation can promote iron-oxide precipitation. The sedimentary rock record is, to a remarkable degree, a record of microbial metabolism.[^microbial_geology] The relationship between life and geology is bidirectional: the planet shaped the first communities, and those communities shaped the planet back.

## Biomineralization: when metabolism becomes rock

Here the title turns literal. Microbes do more than alter water chemistry. They build minerals.

Sometimes they do it indirectly. Cyanobacterial CO$_2$ uptake can raise local pH and favor carbonate precipitation, but net mineral growth also depends on water chemistry, organic matrices, and other metabolic processes. Sulfate reducers alter alkalinity and sulfide availability in ways that favor carbonate and sulfide precipitation. Iron oxidizers and iron reducers shift iron between soluble and insoluble forms, helping to create the mineral patterns that later geologists read back as environmental history.[^konhauser2007_biomineral]

Some microbes build more directly. Magnetotactic bacteria precipitate chains of magnetite or greigite crystals inside their own cells, using the minerals as internal compass needles.[^konhauser2007_biomineral] Other microbes coat themselves in iron oxides or nucleate manganese minerals on their surfaces. In each case, the cell is manufacturing part of the mineral world around it.

Banded iron formations, stromatolitic carbonates, and other sedimentary structures can record biological contributions alongside chemical precipitation, sediment supply, and later alteration. Metabolism helped shape the rock record; that does not make every mineral or laminated structure a unique metabolic signature.

## The first metabolisms

Chemoautotrophy is one proposed starting point for early metabolism, not an observed first step. Phylogenetic analyses place methanogenesis -- CO$_2$ + 4 H$_2$ $\rightarrow$ CH$_4$ + 2 H$_2$O -- deep in archaeal evolutionary history, but do not establish that it preceded all other metabolisms or assign it a direct geological age.[^methanogenesis_ancient] Geological processes can supply H$_2$ and CO$_2$ in suitable settings. The example needs no light or complex organic feedstock, but it still needs adequate local supply and catalysts that make the reaction accessible.

We have now surveyed the mat from the outside: its layers, its cycles, its geological legacy. But we have not yet asked *how fast* any of this runs. That question takes us from geology into chemistry -- from the architecture of the community to the machinery inside each cell. The detour is necessary, because the mat's stability depends not just on which reactions occur, but on the rates at which they occur and how those rates respond to changing substrate supply.

## The speed limit of life: why enzymes matter

We have been describing metabolisms -- reactions that microbes catalyze to earn a living. But there is a question we have deferred since Chapter 1: *why* do these reactions need catalysis at all?

The thermodynamic answer is clear enough. Many of the reactions that life depends on are spontaneous -- they have negative $\Delta G$ under environmental conditions. Hydrogen and CO$_2$ "want" to become methane in the same way that a ball at the top of a hill "wants" to roll down. The free energy is there.

But spontaneity says nothing about speed. A reaction can be thermodynamically favorable and yet proceed so slowly that it might as well not happen. Uncatalyzed reactions used in biochemistry can have extraordinarily long half-lives under specified laboratory conditions.[^catalytic_necessity] That lesson does not supply a universal time to detectable methane from CO$_2$ and H$_2$; such a time would also depend on the conditions, amount, and detection limit. Available free energy is only part of the story.

This is why enzymes exist. They are the difference between a reaction that is possible in principle and a reaction that is fast enough to sustain a living cell.

Most enzymes are protein catalysts; catalytic RNAs are another class, as Chapter 3 described. Enzymes can accelerate specific reactions enormously without being consumed or changing the reaction's equilibrium. The enhancement depends on the reaction and comparison conditions: one experimental estimate for orotidine 5'-phosphate decarboxylase is roughly 10$^{17}$-fold.[^enzyme_acceleration] Catalysis happens at the **active site**, often assisted by **cofactors** such as metal ions or organic molecules. Iron cofactors motivate hypotheses about biochemical evolution, but are not a direct measurement of the ocean where life originated. Further details on active-site mechanisms and inhibition types are in Appendix A.

How fast? That depends on substrate supply. Michaelis and Menten (1913) formalized the relationship:[^michaelis_menten] $V = V_{\max}[\text{S}]/([\text{S}] + K_m)$, where $V_{\max}$ is the maximum rate at full saturation and $K_m$ is the substrate concentration at which the rate is half-maximal.

Here $[\text{S}]$ is free substrate concentration on the assay volume basis, and $V$ and $V_{\max}$ are rates on that same basis. The law describes a reduced single-enzyme mechanism under suitable approximation conditions. A similar curve for microbial growth or uptake does not identify that mechanism or its constants.[^saturation_meaning]

At low substrate ($[\text{S}] \ll K_m$), the rate scales linearly with supply -- the enzyme has idle time between encounters. At high substrate ($[\text{S}] \gg K_m$), the rate plateaus at $V_{\max}$ -- every enzyme molecule is busy. In a bacterial mat, substrate concentrations are set not by a lab technician but by the balance between production, consumption, and diffusion. For this law, substrate must greatly exceed $K_m$ for the rate to approach $V_{\max}$; merely exceeding it is not enough. Well below $K_m$, the rate is approximately proportional to supply.

This simple curve illustrates a kinetic speed limit. Metabolism is never infinitely fast, even when energy is abundant. Appendix A covers the Lineweaver-Burk graphical method, enzyme inhibition types, and temperature/pH dependencies.

## The mat as a metabolic circuit

Now we can put the pieces together. The bacterial mat is not just a community of organisms sharing space. It is a metabolic circuit -- a system in which the waste of each guild becomes the substrate of another, and the kinetics of each enzyme determines the rate at which that handoff occurs.

The phototrophs at the top fix carbon at a rate governed by light intensity and their carbon-fixation enzymes -- the reverse TCA cycle in the green canopy, RuBisCO-based Calvin cycle in some purple bacteria below. The fermenters in the dark layer process the organic carbon at rates governed by their hydrolytic and fermentative enzymes. The sulfate reducers consume H$_2$ at rates dictated by their hydrogenases and dissimilatory sulfite reductases. And the methanogens compete for the same H$_2$ using their own enzymatic machinery.

A saturation curve is a useful first approximation for selected steps. Local substrate concentrations depend on the reactions that produce and consume them, and on transport. Representing the entire mat as coupled hyperbolas is a selected simplification, rather than a mechanism established for every handoff.

These couplings suggest feedback loops that can buffer changes in supply. Their effect on mat stability depends on transport, community responses, and the reaction network; a saturation curve or a closed batch calculation alone does not establish that stability. In a simplified model, excess organic carbon can accumulate and increase fermentation rates along a saturation curve. Scarce sulfate can slow sulfate reduction and allow H$_2$ to accumulate, potentially favoring methanogens. These are possible feedbacks to test, not a guarantee of self-regulation or eventual consumption.

This is the satisficing lens used in this book: ask whether a community can cover maintenance costs under local constraints, rather than assuming a community-wide objective. A steady state in a selected kinetic model does not establish that organisms never optimize. Coexistence alone does not distinguish these interpretations. The material loops and the conditions that sustain them must be checked, rather than inferred from the saturation curve.

A model that assumes sulfate reducers always exclude methanogens wherever sulfate is present, or that one reaction dominates each depth interval, can miss overlap and coexistence. Those observations call for checking substrate use, transport, and local energy conditions. The satisficing lens asks whether each guild can cover its costs in that setting. Negative $\Delta G$ for both reactions is a starting condition to examine, not sufficient evidence for coexistence or a test that rules out optimization.

## What we sacrificed

The three-layer model described in this chapter is a useful idealization, but real bacterial mats are messier. Gradients are not sharp boundaries; they are continuous. Species are not neatly confined to one layer; many are motile and migrate with the light cycle. The chemistry is not limited to sulfur and carbon; nitrogen, phosphorus, iron, and trace metals all play roles that we have omitted here.

We also treated enzymes as isolated catalysts following simple Michaelis-Menten kinetics. In reality, enzymes inside cells are organized into pathways and complexes, subject to allosteric regulation, product inhibition, and competition for shared cofactors. The Michaelis-Menten equation describes one enzyme acting on one substrate in a well-mixed solution. Inside a cell -- let alone inside a millimeter-thick mat with steep gradients -- the conditions for that equation are only approximately met.

These simplifications are not errors. They are deliberate trades: we sacrifice realism for a framework that can be interrogated quantitatively. The Michaelis-Menten curve, the closed sulfur cycle, the three-layered architecture -- these are models, not photographs. Their value is that they let you ask, "What would change if I doubled the sulfate supply?" or "What happens to the mat if light intensity drops?" and get a directional answer. We will build on them, adding complexity where it earns its keep.

## Takeaway

- Mat-built stromatolites are prominent in the Precambrian fossil record across more than two billion years; this does not demonstrate a universal, continuously stable community design.
- Light attenuation and chemical gradients can organize metabolic guilds into layers. The three-layer order here is an illustrative choice, not a universal architecture.
- Stromatolites include ancient structures interpreted as microbial, such as the roughly 3.43-billion-year-old Strelley Pool examples. They do not preserve a complete metabolic roster.
- Carbon isotope discrimination provides clues to carbon fixation, but its magnitude depends on physiology and conditions. Ancient light carbon needs geological context and is not a unique biosignature.
- Microbial communities do not merely leave traces in rocks; they help build the rocks themselves through biomineralization, from carbonate crusts to iron minerals to intracellular magnetite.
- Enzymes can produce enormous reaction-specific rate enhancements; Michaelis-Menten kinetics ($V = V_{\max}[\text{S}]/([\text{S}] + K_m)$) illustrates a common speed-versus-supply tradeoff; pathways and cells can require additional kinetics.
- The satisficing lens asks whether communities can persist under local constraints. Testing that interpretation requires more than a saturation curve or the observation of coexistence.

[^sharkbay]: Modern Shark Bay mats are analogs, not replicas of the hypothetical Archean community. Their composition and accretion mechanisms vary. Erica P. Suosaari et al., "New multi-scale perspectives on the stromatolites of Shark Bay, Western Australia," *Scientific Reports* 6 (2016): 20557, [DOI:10.1038/srep20557](https://doi.org/10.1038/srep20557). [@Suosaari2016]

[^mat_dominance]: The abundance of preserved mat-built structures is not a census of all Precambrian life. David J. Des Marais, "Microbial Mats and the Early Evolution of Life," *Trends in Ecology and Evolution* 5 (1990): 140--144, [DOI:10.1016/0169-5347(90)90219-4](https://doi.org/10.1016/0169-5347(90)90219-4), provides historical synthesis. [@DesMarais1990]

[^stromatolite_record]: Stromatolites provide one of the longest continuous records of biological activity on Earth, with morphological and geochemical signatures spanning from the Archean to the present. See J. William Schopf, "Fossil Evidence of Archaean Life," *Philosophical Transactions of the Royal Society B* 361 (2006): 869--885. [@Schopf2006]

[^anoxygenic_evolution]: The historical order and dates of photosynthetic innovations are inferences, not identified by the layers of this schematic. Robert E. Blankenship, "Early Evolution of Photosynthesis," *Plant Physiology* 154 (2010): 434--438, [DOI:10.1104/pp.110.161687](https://doi.org/10.1104/pp.110.161687), reviews the evolutionary questions. [@Blankenship2010]

[^h2s_phototrophs]: In tested *Chlorobaculum tepidum*, complete sulfide oxidation requires machinery beyond elemental-sulfur formation. Carina Holkenbrink et al., "Sulfur globule oxidation in green sulfur bacteria is dependent on the dissimilatory sulfite reductase system," *Microbiology* 157 (2011): 1229--1239, [DOI:10.1099/mic.0.044669-0](https://doi.org/10.1099/mic.0.044669-0). This organism-specific result does not prove an Archean sulfate flux. [@Holkenbrink2011]

[^purple_bacteria]: "Purple bacteria" is an ecological label encompassing different lineages and pigment systems; absorption peaks are not confined to one universal 800--900 nm band. Beverly K. Pierson, Vicki M. Sands, and Judith L. Frederick, "Spectral Irradiance and Distribution of Pigments in a Highly Layered Marine Microbial Mat," *Applied and Environmental Microbiology* 56 (1990): 2327--2340, [DOI:10.1128/aem.56.8.2327-2340.1990](https://doi.org/10.1128/aem.56.8.2327-2340.1990). [@Pierson1990]

[^spectral_niche]: Pierson, Sands, and Frederick, "Spectral Irradiance and Distribution of Pigments in a Highly Layered Marine Microbial Mat" (1990), cited above, measured spectral light profiles and pigments in a modern intertidal mat containing cyanobacteria, two purple bacterial layers, and green sulfur bacteria. It is a counterexample to a compulsory green-over-purple ordering, not evidence of the same ordering in the Archean. [@Pierson1990]

[^niche_partitioning]: Modern spectral measurements support wavelength-dependent niche partitioning; its presence in an ancient mat is an inference. Pierson, Sands, and Frederick (1990), full publication identity given above. [@Pierson1990]

[^bchl_green]: Pigment color and absorption bands must be distinguished. Niels-Ulrik Frigaard and Donald A. Bryant, "Seeing green bacteria in a new light: genomics-enabled studies of the photosynthetic apparatus in green sulfur bacteria and filamentous anoxygenic phototrophic bacteria," *Archives of Microbiology* 182 (2004): 265--276, [DOI:10.1007/s00203-004-0718-9](https://doi.org/10.1007/s00203-004-0718-9), provides an apparatus overview; Pierson et al. (1990), cited above, supplies primary mat spectra. [@Frigaard2004; @Pierson1990]

[^sulfate_reduction]: Bo Barker Jørgensen, "Mineralization of Organic Matter in the Sea Bed: The Role of Sulphate Reduction," *Nature* 296 (1982): 643--645, concerns modern marine mineralization. The displayed hydrogen-driven balance is illustrative, not an inventory of all sulfate-reducer substrates. [@Jorgensen1982]

[^archean_sulfate]: Kirsten S. Habicht et al., "Calibration of Sulfate Levels in the Archean Ocean," *Science* 298 (2002): 2372--2374, [DOI:10.1126/science.1078265](https://doi.org/10.1126/science.1078265), inferred <200 micromolar from culture fractionation and geological records. J. W. Jamieson et al., "Neoarchaean seawater sulphate concentrations from sulphur isotopes in massive sulphide ore," *Nature Geoscience* 6 (2013): 61--64, [DOI:10.1038/ngeo1647](https://doi.org/10.1038/ngeo1647), estimated roughly 80 micromolar for the 2.7 Ga Kidd Creek setting. Sean A. Crowe et al., "Sulfate was a trace constituent of Archean seawater," *Science* 346 (2014): 735--739, [DOI:10.1126/science.1258966](https://doi.org/10.1126/science.1258966), inferred <2.5 micromolar with a Lake Matano-informed model. These reconstructions differ in method and scope. [@Habicht2002; @Jamieson2013; @Crowe2014Sulfate]

[^thermodynamic_competition]: Derek R. Lovley, Daryl F. Dwyer, and Michael J. Klug, "Kinetic Analysis of Competition Between Sulfate Reducers and Methanogens for Hydrogen in Sediments," *Applied and Environmental Microbiology* 43 (1982): 1373--1379, [DOI:10.1128/aem.43.6.1373-1379.1982](https://doi.org/10.1128/aem.43.6.1373-1379.1982), used sulfate additions and inhibition in lake sediments. Hydrogen supply, population sizes, and sulfate availability affected competition; coexistence was observed. This is modern experimental evidence, not a recovered ancient community. [@Lovley1982Hydrogen]

[^methanogens]: Rudolf K. Thauer, Kurt Jungermann, and Karl Decker, "Energy Conservation in Chemotrophic Anaerobic Bacteria," *Bacteriological Reviews* 41 (1977): 100--180, [DOI:10.1128/br.41.1.100-180.1977](https://doi.org/10.1128/br.41.1.100-180.1977), provides biochemical context. Its erratum at page 809 is a separate record. Environmental suitability does not guarantee methane production. [@Thauer1977]

[^mat_stability]: Metabolic coupling is a possible mechanism of persistence, not a stability result established by fossil longevity. Allwood et al. (2006), identified below, supports a geological microbial interpretation; a saturation law for a selected reaction does not by itself establish stability of the whole mat. [@Allwood2006]

[^stromatolite_formation]: Suosaari et al., "New multi-scale perspectives on the stromatolites of Shark Bay, Western Australia" (2016), identified above, combines field observations, microscopy, microbial community analysis, and carbonate fabrics. The study finds pervasive micrite but does not uniquely resolve the precipitation mechanism. [@Suosaari2016]

[^oldest_stromatolites]: Among the oldest well-preserved Archean stromatolites are those from the ~3.43 Ga Strelley Pool Formation (Pilbara, Western Australia). Abigail C. Allwood et al., "Stromatolite Reef from the Early Archaean Era of Australia," *Nature* 441 (2006): 714--718. [@Allwood2006]

[^stromatolite_biosignatures]: Allwood et al., "Stromatolite Reef from the Early Archaean Era of Australia" (2006), identified above, argues for microbial formation from an assemblage and its facies context. No individual shape or lamination alone identifies a metabolic guild. [@Allwood2006]

[^sharkbay_modern]: Suosaari et al. (2016), identified above, examines modern Hamelin Pool structures, community variation, and environmental controls. Analogy does not establish that oxygenic photosynthesis was absent at the age of every ancient stromatolite. [@Suosaari2016]

[^carbon_fixation_pathways]: Georg Fuchs, "Alternative Pathways of Carbon Dioxide Fixation: Insights into the Early Evolution of Life?" *Annual Review of Microbiology* 65 (2011): 631--658, gives pathway context. Pathway inventories and typical isotope ranges should not be treated as a fixed code for identifying ancient organisms. [@Fuchs2011]

[^rubisco]: RuBisCO (ribulose-1,5-bisphosphate carboxylase/oxygenase) catalyzes CO$_2$ fixation in the Calvin cycle. Gerald Karp, *Cell and Molecular Biology: Concepts and Experiments*, 7th ed. (Wiley, 2013), provides cell-biological context. The modern pathways chosen here do not identify those of a particular ancient mat. [@Karp2008]

[^carbon_fractionation]: R. Sirevåg, B. B. Buchanan, J. A. Berry, and J. H. Troughton, "Mechanisms of CO2 fixation in bacterial photosynthesis studied by the carbon isotope fractionation technique," *Archives of Microbiology* 112 (1977): 35--38, [DOI:10.1007/BF00446651](https://doi.org/10.1007/BF00446651), compared isotope incorporation in cultured phototrophs. Renée Z. Wang et al., "Carbon Isotope Fractionation by an Ancestral Rubisco Suggests That Biological Proxies for CO2 through Geologic Time Should Be Reevaluated," *PNAS* 120 (2023): e2300466120, [DOI:10.1073/pnas.2300466120](https://doi.org/10.1073/pnas.2300466120), also distinguishes enzyme and whole-cell effects. Enzyme measurements must be distinguished from whole-cell signatures. [@Sirevag1977; @Wang2023Rubisco]

[^isua_carbon]: Isua and Akilia are distinct occurrences, and light carbon is not a unique biological signature. Manfred Schidlowski, "A 3,800-Million-Year Isotopic Record of Life from Carbon in Sedimentary Rocks" (1988), is historical synthesis. Aivo Lepland et al., "Questioning the Evidence for Earth's Earliest Life: Akilia Revisited," *Geology* 33 (2005): 77--79, DOI:10.1130/G20890.1; Mark A. van Zuilen et al., "Reassessing the Evidence for the Earliest Traces of Life," *Nature* 418 (2002): 627--630, DOI:10.1038/nature00934, address site-specific interpretation limits. They do not disprove every proposed Greenland biosignature. [@Schidlowski:1988de; @Lepland2005; @vanZuilen2002]

[^nitrogenase]: Nitrogenase catalyzes the reduction of atmospheric N$_2$ to NH$_3$, the only biological pathway for nitrogen fixation. The enzyme also fractionates nitrogen isotopes, preferentially incorporating ^14^N. James B. Howard and Douglas C. Rees, "Structural Basis of Biological Nitrogen Fixation," *Chemical Reviews* 96 (1996): 2965--2982. [@HowardRees1996]

[^microbial_geology]: Microbial metabolism drives mineral precipitation, dissolution, and transformation. Photosynthesis can alter pH and carbonate saturation; sulfate reduction supplies sulfide that can precipitate with available metals; iron oxidation can promote iron-oxide formation. Kurt Konhauser, *Introduction to Geomicrobiology* (Blackwell, 2007), provides a comprehensive treatment of microbe--mineral interactions across geological time. [@Konhauser2007]

[^konhauser2007_biomineral]: Kurt Konhauser, *Introduction to Geomicrobiology* (Blackwell, 2007). Konhauser's treatment of carbonate precipitation, iron mineral formation, magnetotactic bacteria, and other microbe-mineral systems remains one of the clearest geomicrobiological overviews of how microbes literally build minerals. [@Konhauser2007]

[^methanogenesis_ancient]: Éric Bapteste, Céline Brochier, and Yan Boucher, "Higher-level classification of the Archaea: evolution of methanogenesis and methanogens," *Archaea* 1 (2005): 353--363, [DOI:10.1155/2005/859728](https://doi.org/10.1155/2005/859728), analyzes histories of methanogenic genes. The inference of an early common history is conditional on phylogenetic reconstruction, not an observation or a clock date for the first metabolism. [@Bapteste2005]

[^catalytic_necessity]: Richard Wolfenden and Mark J. Snider, "The Depth of Chemical Time and the Power of Enzymes as Catalysts," *Accounts of Chemical Research* 34 (2001): 938--945, reviews uncatalyzed biochemical reaction times. Those reaction-specific comparisons do not set a universal time to detectable methane formation. [@Wolfenden2001]

[^enzyme_acceleration]: Anna Radzicka and Richard Wolfenden, "A Proficient Enzyme," *Science* 267 (1995): 90--93, [DOI:10.1126/science.7809611](https://doi.org/10.1126/science.7809611), reports an approximately 10$^{17}$-fold rate enhancement for orotidine 5'-phosphate decarboxylase. The estimated transition-state dissociation constant is a different quantity from a rate enhancement. No universal enhancement range is inferred. [@Radzicka1995]

[^michaelis_menten]: Leonor Michaelis and Maud L. Menten, "Die Kinetik der Invertinwirkung," *Biochemische Zeitschrift* 49 (1913): 333--369. The historical rapid-equilibrium interpretation differs from the later quasi-steady-state reduction. Kenneth A. Johnson and Roger S. Goody, “The Original Michaelis Constant: Translation of the 1913 Michaelis-Menten Paper,” *Biochemistry* 50 (2011): 8264--8269, [doi:10.1021/bi201284u](https://doi.org/10.1021/bi201284u). [@Michaelis1913; @JohnsonGoody2011]

[^saturation_meaning]: Approximation conditions and errors must be assessed for the enzyme system. A growth half-saturation concentration is not automatically an uptake Michaelis constant. Kashvi Srivastava et al., “Accuracy Versus Predominance: Reassessing the Validity of the Quasi-Steady-State Approximation,” *Bulletin of Mathematical Biology* 87 (2025): 73, [doi:10.1007/s11538-025-01451-z](https://doi.org/10.1007/s11538-025-01451-z); Justus Wilhelm Fink et al., “Microbial population dynamics decouple growth response from environmental nutrient concentration,” *PNAS* 120 (2023): e2207295120, [doi:10.1073/pnas.2207295120](https://doi.org/10.1073/pnas.2207295120). [@Srivastava2025QSSA; @Fink2023Growth]
