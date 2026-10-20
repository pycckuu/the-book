---
title: "Energy Toolkit"
---

This appendix collects two sets of tools referenced throughout the book. Sections A.1--A.5 cover enzyme kinetics: the graphical methods, inhibition types, and environmental dependencies that extend the Michaelis-Menten framework introduced in Chapter 4. Sections A.6--A.7 cover geochemical estimation tools: methods for assessing the energy content of organic matter and detecting ancient metabolism in the rock record.

Use this appendix by topic. For the Gibbs budget, reaction direction and energy-versus-power distinction, return to Chapter 1. For saturation practice, the reciprocal plot is background: the teaching module does not require a reciprocal fit.

**Enzyme Kinetics and Regulation**

## Linearizing the Michaelis-Menten curve: Lineweaver-Burk

The Michaelis-Menten equation is a hyperbola, which can be awkward to fit by eye. In 1934, Hans Lineweaver and Dean Burk showed that taking the reciprocal of both sides converts it to a straight line:[^appa_lineweaver]

$$
\frac{1}{V} = \frac{K_m}{V_{\max}} \cdot \frac{1}{[\text{S}]} + \frac{1}{V_{\max}}
$$

Plot $1/V$ against $1/[\text{S}]$ and you get a line with:

- **y-intercept** = $1/V_{\max}$
- **x-intercept** = $-1/K_m$
- **slope** = $K_m/V_{\max}$

This is the Lineweaver-Burk (or double-reciprocal) plot. It was historically important because it allowed $K_m$ and $V_{\max}$ to be extracted from experimental data using a ruler and graph paper. Modern curve-fitting software has made the graphical method less necessary, but the plot remains a powerful diagnostic tool because different types of inhibition produce visually distinct patterns.[^appa_diagnostic]

For positive substrate and rate, reciprocal linearization is an algebraic identity. It does not preserve additive rate errors: a small rate error is multiplied approximately by $1/V^2$ after inversion. Low-rate observations can therefore dominate an unweighted reciprocal fit. Fit the original rate law with an explicit observation-error model when estimating parameters.

## Competitive inhibition

A competitive inhibitor binds the free enzyme in a way that excludes substrate binding, most often at the active site; many competitive inhibitors resemble the substrate. In the simple reversible model, the apparent $K_m$ increases by the factor $(1+[\text{I}]/K_I)$, while $V_{\max}$ is unchanged: at sufficiently high substrate concentration, the rate approaches the uninhibited $V_{\max}$.[^appa_competitive]

On a Lineweaver-Burk plot, competitive inhibition changes the slope and x-intercept but leaves the y-intercept ($1/V_{\max}$) unchanged. The lines pivot around the y-axis.

## Non-competitive inhibition

A mixed inhibitor can bind both the free enzyme and the enzyme-substrate complex; in the simple model here, the complex containing inhibitor does not form product. This lowers the apparent $V_{\max}$. Pure non-competitive inhibition is the equal-affinity case below: the apparent $K_m$ is unchanged only when $K_I' = K_I$. Otherwise the apparent $K_m$ also changes. A kinetic pattern alone does not identify an allosteric mechanism.

The inhibitor dissociation constant is:

$$
K_I = \frac{[\text{E}][\text{I}]}{[\text{EI}]}
$$

For the simplest case of pure non-competitive inhibition (where $K_I' = K_I$, meaning the inhibitor binds the free enzyme and the enzyme-substrate complex with equal affinity), the rate equation becomes:

$$
V = \frac{V_{\max}[\text{S}]}{K_m + [\text{S}]} \cdot \frac{K_I}{K_I + [\text{I}]}
$$

The second factor is a simple scaling term: it multiplies the uninhibited rate by the fraction of enzyme molecules not bound to inhibitor. This form assumes rapid binding equilibria, an inactive enzyme-substrate-inhibitor complex, and a free inhibitor concentration close to the total.[^appa_inhibition]

For pure non-competitive inhibition, a Lineweaver-Burk plot changes its slope and y-intercept but keeps the x-intercept ($-1/K_m$) unchanged. The lines pivot around the x-axis.

## Irreversible inhibition

Some inhibitors form covalent bonds with the enzyme, permanently inactivating it. Their effect is not described by an equilibrium dissociation constant alone: many first bind reversibly and then inactivate the enzyme at a finite rate, so inhibition increases with exposure time. Many toxins and pharmaceutical drugs work this way -- aspirin, for instance, irreversibly acetylates cyclooxygenase.[^appa_irreversible]

## pH and temperature optima

Every enzyme has a pH and temperature at which it works best. Deviate too far in either direction and the rate drops, often sharply.

- **Temperature**: increasing temperature raises the kinetic energy of molecules, generally speeding reactions. But proteins are only marginally stable. Beyond the optimum, the enzyme begins to denature -- its three-dimensional structure unfolds, and the active site geometry is lost. The rate curve rises, peaks, then crashes. The apparent optimum is not a fixed constant: it depends on assay duration, because longer assays allow more denaturation, and on pH, substrate and stabilizing conditions. Enzymes from organisms that grow at high temperature often remain stable and active at temperatures that rapidly denature their mesophilic counterparts.
- **pH**: active-site residues have ionizable groups (histidine, glutamate, lysine) that must be in the correct protonation state for catalysis. Shifting the pH protonates or deprotonates these groups, disrupting substrate binding or transition-state stabilization. Many cytoplasmic enzymes are most active near neutral pH. Enzymes that act in acidic or alkaline compartments or outside the cell, such as pepsin in stomach acid, can have shifted optima.

These optima often reflect the conditions an enzyme encounters, but an activity optimum need not equal the organism's usual environment.[^appa_optima] Thermal stability of reconstructed ancestral elongation factors suggests that the environments of sampled bacterial lineages cooled by about 30 degrees C between roughly 3.5 and 0.5 billion years ago. These are stability measurements of inferred proteins, not catalytic optima, and the inference depends on the reconstruction method and on linking protein stability to the organisms' environment. As Chapter 2 explains, it does not show that the first organisms were thermophiles.[^appa_ancestral_stability]

**Geochemical Estimation Tools**

## The NOSC: a simple proxy for energy content

In 2011, Douglas LaRowe and Philippe Van Cappellen showed that the energetic content of organic compounds scales, to a useful approximation, with a single number: the Nominal Oxidation State of Carbon (NOSC).

The empirical relation is:

$$
\Delta G_{\text{Cox}}^0 = 60.3 - 28.5 \times \text{NOSC}
$$

where $\Delta G_{\text{Cox}}^0$ is the standard Gibbs energy of the oxidation half reaction in kJ per mole of carbon. The relation is a regression at 25 degrees C and 1 bar (correlation coefficient 0.94); at a given NOSC, individual compounds can deviate by as much as 30 kJ (mol C)$^{-1}$.[^appa_nosc_regression]

The general oxidation half reaction for organic matter is:

$$
\text{C}_a\text{H}_b\text{N}_c\text{O}_d\text{P}_e\text{S}_f^{\,Z} + (3a + 4e - d)\,\text{H}_2\text{O} \;\longrightarrow
$$
$$
a\,\text{HCO}_3^- + c\,\text{NH}_4^+ + e\,\text{HPO}_4^{2-} + f\,\text{HS}^-
$$
$$
+ (5a + b - 4c - 2d + 7e - f)\,\text{H}^+ + (-Z + 4a + b - 3c - 2d + 5e - 2f)\,e^-
$$

where $Z$ is the net charge of the organic compound, and $a, b, c, d, e, f$ are the stoichiometric coefficients of C, H, N, O, P, and S. For a compound containing carbon ($a > 0$), its NOSC is:[^appa_nosc_definition]

$$
\text{NOSC} = 4 - \frac{-Z + 4a + b - 3c - 2d + 5e - 2f}{a}
$$

The NOSC spectrum runs from fully reduced (methane, CH$_4$, NOSC = $-4$) to fully oxidized (carbon dioxide, CO$_2$, NOSC = $+4$). Carbon with a low NOSC has more electrons to donate per carbon atom, so its oxidation can release more energy when coupled to an electron acceptor; carbon with a high NOSC has fewer electrons left to donate. Most oxidation half reactions have positive $\Delta G_{\text{Cox}}^0$, so energy becomes available only after coupling to the reduction of an electron acceptor, and the available Gibbs energy also depends on activities and temperature, as in Chapter 1.[^appa_nosc_coupling]

As Arndt and colleagues explain, NOSC lets us estimate the energetic potential of complex natural organic matter without knowing its molecular structure.[^appa_nosc_structure] This makes it particularly useful for the complex, heterogeneous mixtures of natural organic matter found in sediments and soils, where detailed structural characterization is often impossible.

## Isotope fractionation as a biosignature

Isotope ratios are among the most durable biosignatures available to geologists. The logic is simple:

1. Isotopic substitution changes vibrational energies and reaction kinetics. Many carbon-fixation reactions preferentially incorporate the lighter isotope, but the magnitude and direction of the effect depend on the process and conditions, as Chapter 4 explains.
2. This discrimination produces a measurable offset ($\delta^{13}$C, $\delta^{15}$N) between the substrate pool and the biological product.
3. The offset can survive in sedimentary organic matter, graphite or carbonate minerals long after the organisms have decomposed; later alteration can modify it.

For carbon, the standard measure is $\delta^{13}$C, reported in parts per thousand (per mil) relative to the VPDB (Vienna Pee Dee Belemnite) reference scale:[^appa_isotope_scale]

$$
\delta^{13}\text{C} = \left(\frac{(^{13}\text{C}/^{12}\text{C})_{\text{sample}}}{(^{13}\text{C}/^{12}\text{C})_{\text{standard}}} - 1\right) \times 1000
$$

Organic carbon from biological fixation commonly has $\delta^{13}$C values of roughly $-20$ to $-30$ per mil, while marine carbonate lies near $0$ per mil. Such a range is not a pathway label, and a light value in an ancient rock is not, by itself, proof of life. Its interpretation requires the source carbon, mineral setting, age and alteration history; Chapter 2 treats the Isua and Akilia occurrences separately.[^appa_ancient_carbon]

The catch: some abiotic processes (see Chapter 2) can also fractionate carbon. The isotope signal is suggestive, not proof. Context matters -- and so does finding the signal preserved in the right mineral host, at the right age, in rocks that haven't been cooked beyond recognition.

[^appa_lineweaver]: Hans Lineweaver and Dean Burk, "The Determination of Enzyme Dissociation Constants," *Journal of the American Chemical Society* 56 (1934): 658-666. [@Lineweaver1934]

[^appa_diagnostic]: Nelson and Cox, *Lehninger Principles of Biochemistry*, 7th ed. (2017), provides the background for the inhibition patterns shown by reciprocal plots. Reciprocal linearization changes the error structure; it is not a substitute for fitting the original rate law. [@Nelson2017]

[^appa_competitive]: Nelson and Cox, *Lehninger Principles of Biochemistry*, 7th ed. (2017), gives the standard reversible competitive-inhibition model. The substrate and inhibitor bind mutually exclusively; the apparent Michaelis constant increases while the limiting rate is unchanged. [@Nelson2017]

[^appa_irreversible]: Nelson and Cox, *Lehninger Principles of Biochemistry*, 7th ed. (2017), gives the biochemical background for irreversible inhibition, including aspirin acetylation. Reversible binding can precede the time-dependent inactivation step. [@Nelson2017]

[^appa_inhibition]: David L. Nelson and Michael M. Cox, *Lehninger Principles of Biochemistry*, 7th ed. (W. H. Freeman, 2017), provides the biochemical background. The reversible rate laws here use the simple inactive inhibitor-complex model and its stated binding assumptions; kinetic patterns do not by themselves establish a binding site. [@Nelson2017]

[^appa_optima]: Nelson and Cox, *Lehninger Principles of Biochemistry*, 7th ed. (2017), gives the biochemical background for pH and temperature effects. The apparent activity optimum depends on assay conditions and need not coincide with the organism's growth conditions. [@Nelson2017]

[^appa_ancestral_stability]: Eric A. Gaucher, Sridhar Govindarajan, and Omjoy K. Ganesh, "Palaeotemperature Trend for Precambrian Life Inferred from Resurrected Proteins," *Nature* 451 (2008): 704-707, abstract, reports the thermostability trend of reconstructed elongation factors. Stability measurements and inferred environmental trends are distinct from catalytic optima and from the temperature preferences of the first organisms, as discussed in Chapter 2. [@Gaucher2008]

[^appa_nosc_regression]: Douglas E. LaRowe and Philippe Van Cappellen, "Degradation of Natural Organic Matter: A Thermodynamic Analysis," *Geochimica et Cosmochimica Acta* 75 (2011): 2030-2042, p. 2037, Eq. 14, gives the standard-state regression at 25 degrees C and 1 bar with correlation coefficient 0.94; p. 2036 describes deviations up to 30 kJ per mole of carbon. [@LaRowe2011]

[^appa_nosc_definition]: LaRowe and Van Cappellen (2011), p. 2031, Reaction (2) and Eq. 4, defines the oxidation half reaction and the nominal oxidation state of carbon. The half-reaction reference species are bicarbonate, ammonium, hydrogen phosphate and bisulfide, as written above. [@LaRowe2011]

[^appa_nosc_coupling]: LaRowe and Van Cappellen (2011), p. 2036, distinguishes the oxidation half reaction from the overall reaction coupled to a terminal electron acceptor. A half-reaction standard Gibbs energy is not the available energy of a complete metabolism under local conditions. [@LaRowe2011]

[^appa_nosc_structure]: Sandra Arndt et al., "Quantifying the Degradation of Organic Matter in Marine Sediments: A Review and Synthesis," *Earth-Science Reviews* 123 (2013): 53-86, p. 61, discusses estimating energetic potential from NOSC without structural information. [@Arndt2013]

[^appa_isotope_scale]: NIST, *Reference Material 8540: IAEA-CH-7*, information sheet dated 10 November 2022, p. 1, identifies the VPDB carbon isotope scale. The delta definition compares isotope-number ratios; its value is conventionally reported in per mil, as discussed in Chapter 2. [@NIST8540; @IUPACDelta2025]

[^appa_ancient_carbon]: Chapter 2 distinguishes the localities and evidence: Aivo Lepland et al., "Questioning the Evidence for Earth's Earliest Life: Akilia Revisited," *Geology* 33 (2005): 77-79, addresses Akilia; Mark A. van Zuilen, Aivo Lepland, and Gustaf Arrhenius, "Reassessing the Evidence for the Earliest Traces of Life," *Nature* 418 (2002): 627-630, discusses reassessment of ancient carbon evidence. Chapter 4 separates enzyme and whole-cell fractionation, including the experiment reported by Renée Z. Wang et al., "Carbon Isotope Fractionation by an Ancestral Rubisco Suggests That Biological Proxies for CO2 through Geologic Time Should Be Reevaluated," *PNAS* 120 (2023): e2300466120. A carbon isotope value alone does not identify an ancient organism or its pathway. [@Lepland2005; @vanZuilen2002; @Wang2023Rubisco]
