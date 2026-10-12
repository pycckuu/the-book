---
title: "The Poisoning"
---

For hundreds of millions of years, the mat communities thrived.

Picture Earth around 2.8 billion years ago.[^archean_atmosphere] The atmosphere is a haze of nitrogen, carbon dioxide, methane, and water vapor. With very little free oxygen, there is little ozone to screen the ultraviolet light hammering the surface. The oceans are warm, slightly green from dissolved iron, and virtually without free oxygen, though trace amounts may have flickered locally around photosynthetic mats.

In this world, picture mats recycling part of their waste through layered communities. Sulfate reducers can supply sulfide to sulfur oxidizers; methanogens can use hydrogen released by fermenters. It is a functioning economy, but an open one: resources enter, products leave, and not every ancient mat need have contained the same guilds or reached a stable balance.

Then one lineage, the ancestors of cyanobacteria, evolved a metabolism whose waste product could poison organisms adapted to anoxic surroundings.[^cyano_evolution]

They learned to split water.

## The world before the catastrophe

To understand why this was catastrophic, you have to understand what oxygen meant to early life. Not what it means to us -- the electron acceptor our mitochondria depend on, the gas our tissues need -- but what it meant to *them*.

For organisms with oxygen-sensitive enzymes, oxygen could be a dangerous poison.[^oxygen_toxicity] Reactions involving oxygen can generate reactive oxygen species, which damage proteins, DNA, and membranes.[^ros_damage] A cell needs ways to prevent that damage or repair it. We cannot read the defense systems of every ancient organism from the rock record.

Even the producers had to manage their byproduct. Modern cyanobacteria have enzymes that remove reactive oxygen species; experiments with *Synechocystis* show both catalase-peroxidase activity and another peroxide-removing system. That is evidence about living cells, not a date for the first defense against oxygen.[^cyano_defense]

So why did they do it?

Because the prize was independence. Anoxygenic phototrophs depend on electron donors other than water. Hydrogen sulfide, hydrogen gas, and ferrous iron are examples whose availability varies with local chemistry. A phototroph tethered to hydrogen sulfide is a phototroph tethered to its supply.

Water, on the other hand, was everywhere.

The payoff was not primarily energetic but ecological: water offered an abundant source of electrons to organisms that could crack it, although light and nutrients still limited growth. The cost was a potentially toxic byproduct. As oxygen spread, it changed which metabolisms could operate where. In the long run, it also opened a new energy regime, one that became central to much of the complex life we know.

## The ladder of electron donors

The different forms of photosynthesis suggest possible routes toward the water-splitting kind. They do not give us a dated sequence of inventions. To see the possibilities, we need to look at photosynthesis not as a single process but as a family of strategies, built from related machinery but plugged into different fuel lines.

The chassis is simple in concept: capture a photon of light, use its energy to boost an electron to a higher energy state, then pass that excited electron through a chain of proteins to do useful work. The question is: where does that electron come from in the first place?

A useful starting point is to compare the electron donors that living phototrophs can use, without treating that comparison as an ancestral timetable. (The half-reactions below are written in standard acid form for electron bookkeeping; actual speciation varies with pH, and in-vivo coupling partners differ.)

![Selected electron donors and oxidation products. Electron counts follow the displayed donor amounts and endpoints: one H$_2$S to sulfate gives 8 electrons; two H$_2$O to O$_2$ give 4. Arrows omit proton and water balancing; Fe(III) identifies oxidation state, not mineral phase. Rows have no potential scale or universal kinetic or evolutionary ranking. PSII oxidizes water; PSII and PSI operate in series in oxygenic photosynthesis.[^griffin2007][^water_splitting]](../sources/img/ch5_electron_donor_ladder.png){#fig-electron-donor-ladder}

**Hydrogen gas.** The simplest donor. One molecule of H$_2$ yields two protons and two electrons:

$$\text{H}_2 \longrightarrow 2\text{H}^+ + 2e^-$$

Hydrogen can supply electrons, but a metabolism built on it depends on local production and consumption. Volcanic settings are one possible source, not the only habitat. The fermenters in our mat economy can supply it too.

**Hydrogen sulfide.** A donor used by living sulfur phototrophs, including purple and green sulfur bacteria. Complete oxidation to sulfate has this electron bookkeeping:

$$\text{H}_2\text{S} + 4\,\text{H}_2\text{O} \longrightarrow \text{SO}_4^{2-} + 10\,\text{H}^+ + 8e^-$$

More electrons per molecule in this half-reaction, but that does not by itself establish a larger energy yield. Sulfide remains a local resource: its supply can involve geological inputs and microbial sulfur cycling, not just volcanic gases meeting seawater.

**Elemental sulfur.** Here is the bookkeeping for oxidation of sulfur all the way to sulfate:

$$\text{S} + 4\,\text{H}_2\text{O} \longrightarrow \text{SO}_4^{2-} + 8\,\text{H}^+ + 6e^-$$

**Organic compounds.** For bookkeeping, CH$_2$O below stands for organic carbon with an average carbon oxidation state of zero. It is not a claim that a particular phototroph grows on formaldehyde:

$$\text{CH}_2\text{O} + \text{H}_2\text{O} \longrightarrow \text{CO}_2 + 4\,\text{H}^+ + 4e^-$$

All of these share a common limitation. The electron donor is something the organism must *find* -- a molecule supplied by geology or by other organisms. The phototroph is a tenant paying rent with whatever the environment provides. And in evolutionary terms, a tenant is always vulnerable to eviction.

### An intermediate rung: nitrogen photosynthesis

In 1970, the biochemist John Olson published a theoretical model proposing that the transition from anoxygenic to oxygenic photosynthesis did not happen directly. There could have been an intermediate stage, he argued, in which organisms used nitrogen compounds -- specifically nitrite -- as electron donors.[^olson1970]

It was an elegant hypothesis. Nitrite offered a possible intermediate donor between the easier donors and water. If organisms could use it, they would demonstrate that this smaller bridge was chemically and biologically possible, even if they could not tell us whether evolution had crossed it.

Thirty-seven years later, a modern organism made that proposed chemistry visible.

In 2007, at the University of Konstanz in Germany, a team of microbiologists ran a patient experiment. They enriched bacteria from sewage sludge and freshwater sediments in anoxic, bicarbonate-buffered mineral medium under continuous light, repeatedly feeding small amounts of nitrite to avoid its toxicity.[^griffin2007]

After several weeks, some cultures developed a faint pink color, typical of purple phototrophs. Their spectra showed bacteriochlorophyll. Nitrite was consumed, nitrate formed, and biomass increased together. Dark and uninoculated controls showed neither growth nor nitrite oxidation; light-dark shifts and nitrite starvation tested the dependence on both light and nitrite. Here was anoxygenic phototrophic nitrite oxidation in living bacteria.

$$\text{NO}_2^- + \text{H}_2\text{O} \longrightarrow \text{NO}_3^- + 2\,\text{H}^+ + 2e^-$$

Thirty-seven years from an evolutionary proposal to a demonstration of the proposed metabolism. The experiment supplied a modern example of a donor Olson had implicated. It did not identify an ancient intermediate or establish the order in which photosynthetic systems evolved.

### The final step: splitting water

These known donors can be arranged by oxidation difficulty, though whether evolution climbed them in exactly this order remains uncertain:

$$\text{H}_2 \rightarrow \text{H}_2\text{S} \rightarrow \text{N compounds} \rightarrow \text{H}_2\text{O}$$

The ladder points toward the difficulty of extracting electrons from water and the machinery that makes it possible. It is a schematic comparison of donors, not evidence that every lineage climbed these rungs in this order. Donor availability also depends on the environment.

The final step -- water -- was the hardest and the most consequential:

$$2\text{H}_2\text{O} \longrightarrow 4\text{H}^+ + \text{O}_2 + 4e^-$$

Water is everywhere. An organism that can use it as an electron source escapes dependence on those particular donors. But light, nutrients, and other environmental constraints still limit where it can grow.[^water_splitting]

It is also an organism that produces oxygen as waste.

## How photosynthesis actually works (told briefly)

The molecular story is worth a paragraph, because it reveals something beautiful about the machinery -- and something that will matter enormously when we get to respiration.

A quantum of light strikes a chlorophyll molecule. The photon's energy excites it. In a reaction center, that excitation can drive charge separation: an electron is transferred to an acceptor and onward through carriers. Some of these reactions help build an electrochemical proton gradient across a membrane, which drives ATP synthesis. Not every carrier handoff is a separate proton pump.

In oxygenic linear flow, two photosystems work in series: light excites the electrons again in Photosystem I, and the chain supplies reducing power as NADPH. That reducing power can then be used to convert CO$_2$ to organic carbon. The carbon in CO$_2$ starts at an oxidation state of +4; by the time it is incorporated into sugar, it has been reduced. The electron has done real chemical work.

But there is a catch. If the electron departs chlorophyll and leaves the chain as reducing power for carbon fixation, it does not come back. The chlorophyll is left with a hole -- an electron vacancy. Something must refill it.

In anoxygenic phototrophs, the refill comes from sulfide, or hydrogen, or one of the other donors we listed. In cyanobacteria, the refill comes from water. When water supplies those electrons, the overall oxidation leaves protons and molecular oxygen.

In cyclic electron flow, electrons return through the photosynthetic carrier system and help build the proton gradient.

Viruses now sit inside this machinery too. Some cyanophages carry `psbA`, the gene for the D1 core protein of Photosystem II, and some also carry `psbD`.[^slesak2022] In one studied phage-host pair, viral D1 protein was detected during infection, and phage replication depended on the host's light reactions. That supports a role during infection; it does not prove the same function for every annotated viral gene. Some researchers argue that phage-host gene traffic may also have shaped early oxygenic photosynthesis. That ancient role remains a hypothesis.

That is the outline of the invention. The rest is consequences.

## The Great Oxidation Event

The consequences took time to arrive. Oxygenic photosynthesis was operating by the Great Oxidation Event, and several interpretations of older rocks place it earlier. Its origin date remains unresolved: proposed early signals are indirect, and some biomarker interpretations have been challenged.[^cyano_timing] Oxygen production need not immediately cause atmospheric accumulation. Reactions with reduced minerals, gases, and organic matter can consume oxygen as it is produced.[^oxygen_sinks]

Think of it as a bathtub with the drain open. The faucet is running, oxygenic phototrophs are producing oxygen, but the drain can keep the level low. Reduced iron, volcanic gases, and organic matter all contribute to that drain. It is a changing balance of production and consumption, rather than a sponge that permanently removes every molecule.

The drain changed as the planet changed. Iron-rich sediments, including banded iron formations, preserve part of that history, but they are not a simple meter of atmospheric oxygen: iron can be oxidized through pathways that do not require free oxygen.[^bif] Weathering, volcanic gases, organic burial, and biological recycling changed the balance too. The sinks were replenished as well as depleted.

And then, around 2.4 billion years ago, the faucet won.[^goe_timing]

Oxygen began to persist in the atmosphere, enough to reshape the chemistry of the planet's surface. The proxies establish a transition more securely than they establish one oxygen percentage at its beginning.[^goe_oxygen_levels] This is the Great Oxidation Event, a profound change in the chemical world life inhabited.

But the phrase "the Great Oxidation Event" is slightly misleading if it sounds too singular. The rise of oxygen was not a clean flip from off to on. Geochemical proxies preserve hints of earlier oxygen "whiffs," while reconstructions of the transition and its aftermath allow substantial rises and falls rather than a smooth climb.[^goe_whiffs][^goe_oxygen_levels] The surface ocean, the deep ocean, and the atmosphere did not oxygenate in lockstep. The poisoning was staggered, uneven, and regionally messy, as the planet's sinks, sources, and microbial communities changed together.

For oxygen-sensitive anaerobes, that change could be lethal. Enzymes could be damaged, reactive oxygen species could accumulate, and a formerly suitable habitat could become hostile. It is reasonable to infer ecological losses and displacement. But the rock record does not provide a census of these organisms, or establish a global mass extinction caused by oxygen. The poisoning is a picture of the hazard, not a witnessed history of every ancient lineage.[^goe_oxygen_levels]

Anoxic habitats remained available in sediments and other places where oxygen supply could not keep up with consumption. Modern anaerobes still occupy such habitats, including waterlogged soils and, much later in life's history, animal guts. Their distribution shows how anoxic refuges work. It does not establish that particular living lineages were expelled from the surface at the GOE and remained confined ever since.

The rise of oxygen unfolded over a long interval. Its consequences are still unfolding. What follows is not the full story, but a tour of important aftershocks: how life uses the poison as an electron acceptor, how it copes with chemical incompatibilities, how captured cyanobacteria became the engines of plants, and how oxygen helped sustain demanding ways of life.

## The invention of respiration

The chemistry that made oxygen dangerous also made it useful as an electron acceptor. Modern cells show how closely respiration and photosynthesis can be connected. They do not identify the first aerobic respirer or establish that respiration was invented by a cyanobacterium.[^respiration_ancestry]

The logic is startlingly simple once you see it. Photosynthetic electron transport couples light-driven electron transfer to energy conservation. In oxygenic linear flow, the chain supplies reducing power as NADPH, which can then help reduce CO$_2$ to organic carbon.

Now imagine a different route through related machinery. Instead of energizing electrons with light, take them from an organic substrate. Instead of using reducing power to fix carbon, transfer those electrons to oxygen. Proton translocation and ATP synthesis can again capture part of the available energy. This comparison explains the chemistry; it is not a literal reversal of the whole photosynthetic pathway or a reconstruction of its ancestry.[^respiration_origin]

Aerobic respiration couples electron transfer to oxygen with energy conservation. Oxygen is reduced to water, and the cell can use part of the released energy to make ATP.

The deep irony is that the two processes can share molecular parts. In modern cyanobacteria, respiration and photosynthesis overlap in the thylakoid membrane, using components including plastoquinone and the cytochrome *b*$_6$*f* complex. Mutant experiments in *Synechocystis* show how respiratory terminal oxidases help cells cope with changing light.[^shared_complexes]

This is evidence for an interconnected toolkit, not a direction arrow in evolutionary time. Shared components can reflect common ancestry and later recruitment or gene transfer. Their presence alone does not establish that photosynthesis was invented first and then repurposed into aerobic respiration.

Purple phototrophs provide another illustration of metabolic versatility. They are not simply close relatives of cyanobacteria: purple bacteria include phototrophic proteobacteria, whereas cyanobacteria are a distinct lineage. Some purple bacteria combine anoxygenic photosynthesis with aerobic respiration, as in the group containing the nitrite-oxidizing isolate. Similar metabolic options do not place these organisms on one ancestral ladder.[^griffin2007][^water_splitting]

::: {.callout-note}
## Sidebar --- Electron transfer energetics and the thermodynamic factor

When comparing different metabolisms -- iron reduction versus sulfate reduction, say, or aerobic versus anaerobic respiration -- the temptation is to compare energy yields per mole of reaction. This can be misleading, because different reactions transfer different numbers of electrons. One useful normalization is reaction energy **per electron transferred**. It does not replace specifying the reaction, activities, temperature, and energy actually conserved as ATP.[^larowe2011]

This matters practically because microbial rate laws in reactive transport models need to respect thermodynamics. A reaction that is thermodynamically favorable on paper may stall if local concentrations push it close to equilibrium. The following logistic expression illustrates a smooth weighting of reaction energy. It is not the Jin-Bethke net-respiration factor:

$$F_T = \frac{1}{\exp\!\left(\frac{\Delta G_r}{RT}\right) + 1}$$

where $\Delta G_r$ is the in-situ Gibbs energy per mole of the reaction as written, $T$ is absolute temperature, and $R$ uses matching energy units. This makes the exponent dimensionless. The published rate laws cited here use a different thermodynamic factor.[^jin2005][^dale2006][^regnier2011]

Read this particular $F_T$ as a smooth weighting. It approaches one for a large negative $\Delta G_r$, equals $1/2$ at zero, and remains positive for unfavorable reactions. It therefore cannot by itself enforce zero net respiration at equilibrium or a minimum energy for ATP synthesis. Jin and Bethke instead account for both released and conserved energy; their factor vanishes when the coupled driving force vanishes. Any restriction against reverse operation must also be stated. The published law is not obtained simply by shifting this logistic curve, and neither curve is a universal observation of microbial communities.

Temperature also matters. The Arrhenius relation gives the temperature dependence of the rate constant:

$$k(T) = A\,\exp\!\left(-\frac{E_a}{RT}\right)$$

where $E_a$ is the apparent activation energy.[^middelburg1996] A caveat: when this expression is applied to complex microbial processes, the fitted $E_a$ values are "apparent" -- empirical summaries of many underlying steps. Arrhenius strictly relates the rate *constant* $k$ to temperature, not the rate itself; the rate also depends on substrate concentrations, biomass, and other factors.[^arndt2013_poisoning]
:::

## The day shift and the night shift

Oxygen created another problem, one that reveals the precision of microbial adaptation.

Nitrogen fixation, the conversion of N$_2$ into biologically usable ammonia, replenishes a nutrient needed for proteins and nucleic acids. Nitrogenase is oxygen-sensitive and needs protection from molecular oxygen.[^nitrogenase_sensitivity] That does not mean nitrogen fixation is impossible in an oxygenated habitat.

An anoxic cell can avoid this particular conflict while its surroundings remain anoxic. But for cyanobacteria -- organisms that produce oxygen as a byproduct of their core metabolism -- it was a biochemical incompatibility. How do you fix nitrogen when your own photosynthesis is flooding the cell with the one substance that destroys the nitrogen-fixing enzyme?

Some filamentous cyanobacteria use specialized cells called heterocysts. Their envelopes limit oxygen entry, respiration consumes oxygen, and oxygen-producing Photosystem II is suppressed: a spatial solution that protects nitrogenase while neighboring cells carry out oxygenic photosynthesis.[^heterocysts]

Other cyanobacteria separate the conflicting activities in time. A field study published in 2006 gave a detailed example, not the first discovery of temporal separation.

In Yellowstone hot-spring mats, researchers studied thermophilic *Synechococcus* ecotypes at sites where the usual heterocyst-forming cyanobacteria were absent. Could these unicellular inhabitants contribute fixed nitrogen?

The answer turned out to be time.[^steunou2006]

In the sampled mats, photosynthetic oxygen production declined toward evening and oxygen consumption left the sampled layer anoxic. *Synechococcus* nitrogenase transcripts and nitrogenase activity in mat samples appeared in the evening. These are community-layer and gene-expression observations, not a continuous measurement of every cell.

Dawn was not a simple off-switch. A follow-up reported a larger activity peak in early morning, before the mat became strongly oxygenated.[^steunou2006]

The gene-expression patterns were varied, not one binary program: different fermentation genes changed in different directions. Fermentation was proposed as an energy source; its ATP contribution was not directly measured here.

The measurements support temporal separation in this setting. They do not show that every individual cell follows the same schedule. Time is a compartment too.

## Houses for cyanobacteria

There is a line, sometimes repeated among biologists with a taste for provocation, that goes like this: plants are just comfortable houses built for the convenience of cyanobacteria.[^markov_houses]

It sounds like a joke. The image has a biological basis, though a chloroplast is an integrated organelle, not an autonomous tenant.

Every plant cell that photosynthesizes does so using organelles called chloroplasts. Chloroplasts have their own DNA. They have their own ribosomes. They divide within the host cell, using machinery that includes proteins encoded in the host nucleus. Their genome is unmistakably cyanobacterial -- not "similar to" cyanobacteria in the way that a cousin resembles a cousin, but derived from cyanobacteria in the way that a captured soldier becomes a citizen of the conquering nation.

An ancient eukaryotic lineage acquired a cyanobacterium through endosymbiosis.[^endosymbiosis] Over time, the partners became integrated. Many genes were lost or transferred to the host nucleus, and proteins made outside the organelle came to service it. The descendant plastid retained photosynthetic machinery and other metabolic functions. The water-splitting, oxygen-producing apparatus had moved into a new cellular home.

Every leaf on every tree, every blade of grass, every strand of kelp in the ocean uses photosynthetic machinery with cyanobacterial ancestry. In kelp, that machinery arrived through an algal endosymbiosis. The host supplies much of the structure, protection, and molecular support.

The cyanobacteria poisoned the world. Then they moved indoors.

## The nitrogen bargain

The oxygen problem also helps explain one of the important symbioses in the living world, one that still shapes human civilization. It does not by itself date the origin of that partnership.

Plants need nitrogen for amino acids, nucleotides, and chlorophyll. Plants cannot fix N$_2$ themselves. Nitrogenase systems reduce N$_2$ through coupled electron and proton transfers; they occur in bacteria and archaea, not in the plant itself.[^n2_bond] Available nitrogen often limits plant growth, but the response to more nitrogen depends on other resources and conditions.[^nitrogen_limitation]

Evolution's answer was partnership. Plants associate with nitrogen-fixing bacteria from several groups. In legumes, rhizobia, including members of *Rhizobium*, occupy root nodules.[^legume_symbiosis] The plant supplies carbon, and the bacteria supply fixed nitrogen. A working nodule must protect nitrogenase while still supplying oxygen for respiration. Other plant partnerships need not use exactly the same structure or oxygen-control mechanism.

Agriculture benefits from that deal. Soybean fields, clover pastures, and many acacias can draw on nitrogen-fixing partners. They can also use available nitrogen from soil or fertilizer. A root nodule solves a present biochemical problem; it is not a pocket of the Archean world preserved inside a plant.

## The energetics of a new world

The Great Oxidation Event did not merely change the atmosphere. It rewrote the energy budget of the biosphere.

Consider glucose fermentation to ethanol. The products retain chemical energy that complete oxidation can release. Fermentation conserves only part of that opportunity as ATP. That example is useful, but it should not stand in for every anaerobic metabolism: different donors, acceptors, and concentrations give different reaction energies.

Oxygen changes the opportunity. Well-coupled aerobic oxidation of glucose can conserve substantially more ATP than glycolytic fermentation of the same glucose to lactate or ethanol. But the yield depends on the pathway, organism, transport costs, and coupling. ATP actually conserved is not the same quantity as the Gibbs energy released by a reaction. There is no single aerobic-to-anaerobic multiplier that ranks all metabolisms.[^atp_yield]

The difference can be large, and sustained oxygen supply helps support energy-demanding tissues and activities. It does not guarantee fast growth or large cells by itself. Nutrients, resource delivery, cellular architecture, and the costs of growth still matter. The claim that one energetic transition was necessary for cellular complexity belongs to a model that we will meet in Chapter 7, not to an established consequence of the GOE.

The irony survives the qualification. A molecule that threatened oxygen-sensitive life also became central to the physiology of animals, plants, and many fungi. The poisoning and the opportunity were two faces of the same chemistry. But we cannot replay a planet without oxygenic photosynthesis and know that it would never have developed anything more complex than a microbial mat.

## The long aftermath

The transition was not clean. Reconstructions allow substantial fluctuations during the GOE and its aftermath. The "Boring Billion," roughly 1.8 to 0.8 billion years ago, is generally interpreted as a lower-oxygen interval, but its atmospheric oxygen level and stability remain uncertain.[^boring_billion] Large regions of the deep ocean remained anoxic, with ferruginous and sulfidic conditions differing among environments.

Researchers now treat the delay as a systems problem, not a single missing switch. In EONS model scenarios, early oxygenic photosynthesis can coexist with a delayed atmospheric rise; this is conditional on the model inputs and nutrient-redox feedbacks, not an independent date for the invention.[^horne2025] Modern culture experiments motivate another proposal: nickel and urea availability could have constrained ancient cyanobacterial productivity, if the relevant conditions occurred in Archean waters.[^ratnayake2025] Cyanobacteria did not invent oxygen one day and transform the planet the next. Geology, ocean chemistry, and nutrient supply kept pushing back.

This means that for over a billion years, Earth was chemically partitioned. Oxygenated surface environments formed a new world, dangerous to oxygen-sensitive anaerobes and open to aerobic innovation. Large regions of the deep ocean and sediments remained anoxic, with sulfidic or ferruginous conditions differing among places. These were patchy worlds, separated by changing gradients rather than one global boundary.

You can still see boundaries of this kind in stratified lakes, oxygen-minimum zones, and waterlogged soils. Where oxygen supply falls behind consumption, anaerobic processes become possible. Sulfate reduction, methanogenesis, and iron reduction still participate in these changing chemical landscapes.

Modern Earth contains both oxygenated and anoxic environments, separated by gradients that microbes create and exploit. Porewater profiles show the present balance of transport and reaction. They echo the planet's long redox history, but they are not a direct record of a single boundary preserved for 2.4 billion years.

## Takeaway

- Cyanobacteria learned to split water, accessing an abundant electron donor and releasing oxygen. Its spread threatened oxygen-sensitive metabolisms, but a global census of ancient losses and refuges is unavailable.
- Photosynthesis and respiration share components in modern cyanobacteria. That overlap helps explain their chemistry; it does not establish which process evolved first.
- Nitrogenase needs protection from oxygen. Some cyanobacteria separate nitrogen fixation from oxygen production in space or time; measured schedules depend on the organisms and conditions. Root nodules balance that protection with oxygen supply for respiration.
- Plants and many algae house plastids with cyanobacterial ancestry. These organelles still split water, but their machinery is integrated with the host cell rather than independent of it.
- Aerobic oxidation can conserve more ATP than fermentation of the same substrate under specified conditions. Oxygen helped support demanding ways of life; a universal ATP multiplier or energetic necessity for complexity is a stronger claim.
- The rise of oxygen was staggered and uneven. Modern oxic-anoxic gradients illustrate continuing chemical partitioning, rather than a boundary unchanged since the GOE.

[^archean_atmosphere]: The opening is a reconstructed scene, not a measured gas mixture. Kasting, "Earth's Early Atmosphere," *Science* 259 (1993): 920-926, discusses atmospheric models and geological constraints; Archean gas abundances remain uncertain. Low oxygen implies weak ozone screening, but the scene should not be read as one composition shared by all Archean times. [doi:10.1126/science.11536547](https://doi.org/10.1126/science.11536547). [@Kasting1993]

[^cyano_evolution]: The origin date of oxygenic photosynthesis is unresolved. Roger Buick, "When did oxygenic photosynthesis evolve?" *Philosophical Transactions of the Royal Society B* 363 (2008): 2731-2743, reviews early interpretations. Timothy W. Lyons, Christopher T. Reinhard, and Noah J. Planavsky, "The rise of oxygen in Earth's early ocean and atmosphere," *Nature* 506 (2014): 307-315, especially pp. 307-309 and Fig. 1, discuss conflicting signals and biomarker contamination concerns. [doi:10.1098/rstb.2008.0041](https://doi.org/10.1098/rstb.2008.0041); [doi:10.1038/nature13068](https://doi.org/10.1038/nature13068). [@Buick2008; @Lyons2014]

[^oxygen_toxicity]: Oxygen-sensitive enzymes and reactive oxygen species give oxygen toxicity its biochemical basis. James A. Imlay, "Pathways of Oxidative Damage," *Annual Review of Microbiology* 57 (2003): 395-418, distinguishes the reactivity of molecular oxygen from that of its partially reduced products. [doi:10.1146/annurev.micro.57.030502.090938](https://doi.org/10.1146/annurev.micro.57.030502.090938). This modern mechanism does not identify the defense repertoire of all ancient cells. [@Imlay2003]

[^ros_damage]: Reactive oxygen species include superoxide ($\mathrm{O}_{2}^{\bullet-}$), hydrogen peroxide ($\mathrm{H}_{2}\mathrm{O}_{2}$), and the hydroxyl radical ($\mathrm{HO}^{\bullet}$). Their reactions can damage cellular targets. Imlay (2003), *Annual Review of Microbiology* 57: 395-418, reviews the mechanisms; these species should not be confused with molecular oxygen itself. [@Imlay2003]

[^water_splitting]: Modern oxygenic photosynthesis uses two photosystems in series. Robert E. Blankenship, "Early Evolution of Photosynthesis," *Plant Physiology* 154 (2010): 434-438, Fig. 1 and the discussion of photosynthetic subsystems, distinguishes cyanobacteria from purple phototrophic proteobacteria and discusses horizontal gene transfer and uncertain evolutionary paths. The donor ladder is a comparison, not a dated phylogeny. [doi:10.1104/pp.110.161687](https://doi.org/10.1104/pp.110.161687). [@Blankenship2010]

[^slesak2022]: Debbie Lindell et al., "Photosynthesis genes in marine viruses yield proteins during host infection," *Nature* 438 (2005): 86-89, Figs. 1-3 and Methods (p. 88), studied phage P-SSP7 infecting *Prochlorococcus* MED4. Detection of viral D1 and dependence on host light reactions do not directly prove incorporation of viral D1 into functional Photosystem II. Ireneusz Ślesak and Halina Ślesak, "Cyanophages as an important factor in the early evolution of oxygenic photosynthesis," *Scientific Reports* 12 (2022): 20581, use comparative sequences, phylogeny, and structural models to propose an ancient role. This is not an experimental reconstruction of ancestral cells. [doi:10.1038/nature04111](https://doi.org/10.1038/nature04111); [doi:10.1038/s41598-022-24795-1](https://doi.org/10.1038/s41598-022-24795-1). [@Lindell2005; @Slesak2022]

[^cyano_timing]: Buick (2008), especially the evidence assessment and conclusions, and Lyons et al. (2014), pp. 307-310, support separating the origin of oxygen production from its sustained atmospheric accumulation. Neither provides an uncontested origin window of 2.7-3.0 Ga. Some signals can have alternative biological or abiotic explanations. [@Buick2008; @Lyons2014]

[^oxygen_sinks]: Before atmospheric oxygen accumulation, O$_2$ produced by cyanobacteria was consumed by reduced minerals (particularly dissolved Fe$^{2+}$), volcanic gases (H$_2$, H$_2$S), and organic matter. Holland (2006) quantifies these oxygen sinks. [@Holland2006]

[^bif]: Banded iron formations record iron cycling, not a unique oxygen-producing metabolism or the exhaustion of all oxygen sinks. Cornelis Klein, "Some Precambrian banded iron-formations (BIFs) from around the world: Their age, geologic setting, mineralogy, metamorphism, geochemistry, and origin," *American Mineralogist* 90 (2005): 1473-1499, reviews their distribution. Lyons et al. (2014), p. 308, explicitly discuss iron oxidation without free oxygen. The alternative iron pathways qualified in Chapters 1-3 remain applicable here. [@Klein2005; @Lyons2014]

[^goe_timing]: The Great Oxidation Event occurred ~2.4 Ga, marked by the disappearance of mass-independent sulfur isotope fractionation and the appearance of red beds (oxidized continental sediments). Holland (2006) and Lyons et al. (2014) provide detailed reviews. [@Holland2006; @Lyons2014]

[^goe_oxygen_levels]: PAL denotes atmospheric oxygen partial pressure divided by its present value; a percentage of PAL is not an oxygen volume percentage. Lyons et al. (2014), Fig. 1 (p. 308) and pp. 310-311, distinguish the GOE transition, its possible overshoot and aftermath, and the much later mid-Proterozoic. David C. Catling and Mark W. Claire, "How Earth's atmosphere evolved to an oxic state: A status report," *Earth and Planetary Science Letters* 237 (2005): 1-20, Fig. 7 (p. 9) and section 5.1 (pp. 10-11), combine bounds from different proxies and times with model-dependent interpretations; Fig. 7 uses oxygen partial pressure in bar. These are not a single measured percentage at the start of the GOE. [doi:10.1016/j.epsl.2005.06.013](https://doi.org/10.1016/j.epsl.2005.06.013). [@Lyons2014; @Catling2005]

[^respiration_origin]: The comparison in the text concerns electron flow and energy conservation, not a demonstrated historical reversal of photosynthesis. Modern cyanobacterial overlap is described and experimentally investigated by Lea-Smith et al. (2013), Fig. 1 and the terminal-oxidase mutant results. [@LeaSmith2013]

[^larowe2011]: Douglas E. LaRowe and Philippe Van Cappellen, "Degradation of natural organic matter: A thermodynamic analysis," *Geochimica et Cosmochimica Acta* 75 (2011): 2030-2042, pp. 2035-2036 and Figs. 1-2, normalize energies per electron for comparison while showing that activities and mineral phases can change their ordering. Eq. 1 uses CH$_2$O as a simplified biomass representation. [doi:10.1016/j.gca.2011.01.020](https://doi.org/10.1016/j.gca.2011.01.020). [@LaRowe2011]

[^jin2005]: Qusheng Jin and Craig M. Bethke, "Predicting the rate of microbial respiration in geochemical environments," *Geochimica et Cosmochimica Acta* 69 (2005): 1133-1143, Eq. 9 (p. 1134) and section 4 (p. 1136). Their factor is one minus an exponential of the coupled reaction energy, with a stoichiometric divisor. It is not the logistic expression displayed here. They discuss possible cellular prevention of reverse electron transfer. [doi:10.1016/j.gca.2004.08.010](https://doi.org/10.1016/j.gca.2004.08.010). [@Jin2005]

[^dale2006]: Andrew W. Dale, Pierre Regnier, and Philippe Van Cappellen, "Bioenergetic controls on anaerobic oxidation of methane (AOM) in coastal marine sediments: A theoretical analysis," *American Journal of Science* 306 (2006): 246-294, Appendix A, Eq. A-19 (p. 288), use a one-minus-exponential driving-force factor for their modelled pathways. This is a theoretical AOM study, not a general field validation of the logistic expression. [doi:10.2475/ajs.306.4.246](https://doi.org/10.2475/ajs.306.4.246). [@Dale2006]

[^regnier2011]: Pierre Regnier et al., "Quantitative analysis of anaerobic oxidation of methane (AOM) in marine sediments: A modeling perspective," *Earth-Science Reviews* 106 (2011): 105-130. This is an AOM modelling review, not evidence for a universal community-rate law. [doi:10.1016/j.earscirev.2011.01.002](https://doi.org/10.1016/j.earscirev.2011.01.002). [@Regnier2011]

[^middelburg1996]: Jack J. Middelburg et al., "Organic matter mineralization in intertidal sediments along an estuarine gradient," *Marine Ecology Progress Series* 132 (1996): 157-168, Table 3 (p. 161), report apparent activation energies of 54-125 kJ mol$^{-1}$ for carbon-dioxide and total-carbon release at eight Westerschelde stations. This is a particular study, not a universal range for marine sediments. [doi:10.3354/meps132157](https://doi.org/10.3354/meps132157). [@Middelburg1996]

[^arndt2013_poisoning]: Sandra Arndt et al., "Quantifying the Degradation of Organic Matter in Marine Sediments: A Review and Synthesis," *Earth-Science Reviews* 123 (2013): 53--86. Apparent activation energies in diagenetic models aggregate multiple temperature-sensitive processes. [@Arndt2013]

[^heterocysts]: David G. Adams, "Heterocyst formation in cyanobacteria," *Current Opinion in Microbiology* 3 (2000): 618-624, reviews the differentiation system. The protection combines restricted oxygen diffusion, oxygen consumption, and loss of oxygen-producing Photosystem II; it is not an impermeable wall. [doi:10.1016/S1369-5274(00)00150-8](https://doi.org/10.1016/S1369-5274(00)00150-8). [@Adams2000]

[^endosymbiosis]: Patrick J. Keeling, "The endosymbiotic origin, diversification and fate of plastids," *Philosophical Transactions of the Royal Society B* 365 (2010): 729-748, sections 2-4, distinguishes primary and later algal endosymbioses. Hongbo Gao et al., "ARC5, a cytosolic dynamin-like protein from plants, is part of the chloroplast division machinery," *PNAS* 100 (2003): 4328-4333, Figs. 1-5, use mutant, complementation, and localization experiments to test host-encoded division machinery. Eva C. M. Nowack, Michael Melkonian, and Gernot Glöckner, "Chromatophore genome sequence of Paulinella sheds light on acquisition of photosynthesis by eukaryotes," *Current Biology* 18 (2008): 410-418, describe an independent cyanobacterial acquisition, so every photosynthetic eukaryote cannot simply be assigned one capture. No precise date is asserted here. [doi:10.1098/rstb.2009.0103](https://doi.org/10.1098/rstb.2009.0103); [doi:10.1073/pnas.0530206100](https://doi.org/10.1073/pnas.0530206100); [doi:10.1016/j.cub.2008.02.051](https://doi.org/10.1016/j.cub.2008.02.051). [@Keeling2010; @Gao2003; @Nowack2008]

[^n2_bond]: James B. Howard and Douglas C. Rees, "Structural basis of biological nitrogen fixation," *Chemical Reviews* 96 (1996): 2965-2982, review nitrogenase. Reducing N$_2$ enzymatically should not be equated with the energy required to dissociate gaseous N$_2$ into separate atoms. Patti A. Murray and Stephen H. Zinder, "Nitrogen fixation by a methanogenic archaebacterium," *Nature* 312 (1984): 284-286, report fixation in *Methanosarcina barkeri* strain 227: the capability is not restricted to bacteria. [doi:10.1021/cr9500545](https://doi.org/10.1021/cr9500545); [doi:10.1038/312284a0](https://doi.org/10.1038/312284a0). [@HowardRees1996; @MurrayZinder1984]

[^legume_symbiosis]: Thomas Ott et al., "Symbiotic leghemoglobins are crucial for nitrogen fixation in legume root nodules but not for general plant growth and development," *Current Biology* 15 (2005): 531-535, report RNA-interference experiments in *Lotus japonicus*. Removing symbiotic leghemoglobins disrupted nodule oxygen balance and nitrogen fixation; mineral nitrogen supported plant growth. This tests a particular nodule mechanism, not every plant-microbe partnership. [doi:10.1016/j.cub.2005.01.042](https://doi.org/10.1016/j.cub.2005.01.042). [@Ott2005]

[^atp_yield]: Shona A. Mookerjee, Akos A. Gerencser, David G. Nicholls, and Martin D. Brand, "Quantifying intracellular rates of glycolytic and oxidative ATP production and consumption using extracellular flux measurements," *Journal of Biological Chemistry* 292 (2017): 7189-7207, Fig. 1, Table 1, and the definitions of glycolytic and oxidative ATP production, distinguish maximum stoichiometric yields from flux estimates with proton leak and shuttle assumptions. Their worked experiments concern starved, non-growing mammalian C2C12 myoblasts, not all organisms or all anaerobic pathways. [doi:10.1074/jbc.M116.774471](https://doi.org/10.1074/jbc.M116.774471). [@Mookerjee2017]

[^boring_billion]: The interval roughly 1.8-0.8 Ga is distinct from the initial GOE. Lyons et al. (2014), p. 311 and Box 2, discuss low-oxygen reconstructions, proxy uncertainty, and spatially varied marine redox conditions. The name should not imply a directly measured constant atmospheric oxygen level or a biologically inactive planet. [@Lyons2014]

[^goe_whiffs]: Ariel D. Anbar et al., "A whiff of oxygen before the Great Oxidation Event?" *Science* 317 (2007): 1903--1906. Redox-sensitive metal enrichments in the Mount McRae Shale suggest transient oxygenation before permanent atmospheric oxygen buildup. [@Anbar2007]

[^ratnayake2025]: Dilan M. Ratnayake et al., "Biogeochemical impact of nickel and urea in the Great Oxidation Event," *Communications Earth & Environment* 6 (2025): 654, Results and Methods (cyanobacterial growth experiments), test modern *Synechococcus* sp. PCC 7002 in modified medium while varying nickel and urea. Their Archean interpretation additionally depends on proposed ancient availability and chemistry; the cultures do not measure those ocean conditions. [doi:10.1038/s43247-025-02576-8](https://doi.org/10.1038/s43247-025-02576-8). [@Ratnayake2025]

[^horne2025]: Julia Elizabeth Horne, Colin Goldblatt, and Lee Kump, "An early origin of oxygenic photosynthesis delays the Great Oxidation," *Philosophical Transactions of the Royal Society B* 380 (2025): 20240094, section 3, Fig. 2, and section 4. EONS explores prescribed origins and feedbacks, rather than independently dating the origin. The authors identify limitations, including omission of seafloor-weathering and hydrothermal phosphorus inputs. The result is conditional on that model. [doi:10.1098/rstb.2024.0094](https://doi.org/10.1098/rstb.2024.0094). [@Horne2025]

[^olson1970]: J. M. Olson, "The Evolution of Photosynthesis," *Science* 168 (1970): 438-446. [doi:10.1126/science.168.3930.438](https://doi.org/10.1126/science.168.3930.438). The nitrogen-donor intermediate is a historical hypothesis, described explicitly by Griffin et al. (2007), p. 1870, final discussion column; it is not an observed ancestral stage. [@Olson1970; @Griffin2007]

[^griffin2007]: Benjamin M. Griffin, Joachim Schott, and Bernhard Schink, "Nitrite, an Electron Donor for Anoxygenic Photosynthesis," *Science* 316 (2007): 1870. The published body and Fig. 1 describe anoxic bicarbonate-buffered enrichments, repeated nitrite feeds, light-dark and uninoculated controls, and triplicate growth/chemical time courses. The study supplies a modern metabolic example, not an ancestral sequence. [doi:10.1126/science.1139478](https://doi.org/10.1126/science.1139478). [@Griffin2007]

[^respiration_ancestry]: Jose Castresana and David Moreira, "Respiratory chains in the last common ancestor of living organisms," *Journal of Molecular Evolution* 49 (1999): 453-460. [doi:10.1007/PL00006568](https://doi.org/10.1007/PL00006568). Their published abstract infers ancient respiratory chains from homologous components, conditional on the assumed deepest split and absence of lateral transfer. It does not establish photosynthesis-to-aerobic-respiration directionality; that stronger claim is not used here. [@Castresana1999]

[^shared_complexes]: David J. Lea-Smith et al., "Thylakoid Terminal Oxidases Are Essential for the Cyanobacterium *Synechocystis* sp. PCC 6803 to Survive Rapidly Changing Light Intensities," *Plant Physiology* 162 (2013): 484-495, Fig. 1, Results, and Materials and Methods. The study compares terminal-oxidase mutants under different illumination regimes and measures respiratory oxygen uptake. This is present-day physiology, not a test of evolutionary direction. [doi:10.1104/pp.112.210260](https://doi.org/10.1104/pp.112.210260). [@LeaSmith2013]

[^nitrogenase_sensitivity]: Nitrogenase requires protection from oxygen. Fixation can occur in oxygenated environments where organisms control enzyme exposure. The hot-spring mat measurements and the nodule experiment below provide examples; they do not establish one universal concentration threshold or irreversible response for every nitrogenase. [@Steunou2006; @Ott2005; @HowardRees1996]

[^steunou2006]: Anne-Soisig Steunou et al., *PNAS* 103 (2006): 2398-2403, Figs. 2-4 and Methods, used mat samples, transcript assays, oxygen profiles, and acetylene reduction, not continuous individual-cell N$_2$ flux. Their follow-up, "Regulation of nif gene expression and the energetics of N2 fixation over the diel cycle in a hot spring microbial mat," *ISME Journal* 2 (2008): 364-378, reports an early-morning activity peak in its abstract. [doi:10.1073/pnas.0507513103](https://doi.org/10.1073/pnas.0507513103); [doi:10.1038/ismej.2007.117](https://doi.org/10.1038/ismej.2007.117). [@Steunou2006; @Steunou2008]

[^markov_houses]: The houses image is a paraphrased metaphor attributed to Alexander Markov, *Birth of Complexity*, not a verified verbatim quotation or a claim that chloroplasts live independently of their hosts. [@Markov2010]

[^nitrogen_limitation]: David S. LeBauer and Kathleen K. Treseder, "Nitrogen limitation of net primary productivity in terrestrial ecosystems is globally distributed," *Ecology* 89 (2008): 371-379, report a meta-analysis of nitrogen-addition experiments with heterogeneous productivity responses. Nitrogen can be limiting without being the only resource constraint or producing the same response everywhere. Vitousek and Howarth (1991) provide broader review context. [doi:10.1890/06-2057.1](https://doi.org/10.1890/06-2057.1). [@LeBauerTreseder2008; @VitousekHowarth1991]

[^cyano_defense]: Martin Tichy and Wim Vermaas, "In Vivo Role of Catalase-Peroxidase in *Synechocystis* sp. Strain PCC 6803," *Journal of Bacteriology* 181 (1999): 1875-1882, Results (katG mutants and peroxide decomposition), Figs. 1-4, and Discussion. Catalase-peroxidase-deficient mutants retain a light-dependent peroxide-removing activity and grow under the laboratory conditions tested. These experiments demonstrate defenses in this modern strain, not their time of origin. [doi:10.1128/JB.181.6.1875-1882.1999](https://doi.org/10.1128/JB.181.6.1875-1882.1999). [@TichyVermaas1999]
