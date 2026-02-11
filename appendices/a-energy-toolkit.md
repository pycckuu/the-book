---
title: "Appendix A --- Energy Toolkit"
---

This appendix collects two sets of tools referenced throughout the book. Sections A.1--A.5 cover enzyme kinetics: the graphical methods, inhibition types, and environmental dependencies that extend the Michaelis-Menten framework introduced in Chapter 4. Sections A.6--A.7 cover geochemical estimation tools: methods for assessing the energy content of organic matter and detecting ancient metabolism in the rock record.

# Enzyme Kinetics and Regulation

## A.1 Linearizing the Michaelis-Menten curve: Lineweaver-Burk

The Michaelis-Menten equation is a hyperbola, which can be awkward to fit by eye. In 1934, Hans Lineweaver and Dean Burk showed that taking the reciprocal of both sides converts it to a straight line:

$$
\frac{1}{V} = \frac{K_m}{V_{\max}} \cdot \frac{1}{[\text{S}]} + \frac{1}{V_{\max}}
$$

Plot $1/V$ against $1/[\text{S}]$ and you get a line with:

- **y-intercept** = $1/V_{\max}$
- **x-intercept** = $-1/K_m$
- **slope** = $K_m/V_{\max}$

This is the Lineweaver-Burk (or double-reciprocal) plot. It was historically important because it allowed $K_m$ and $V_{\max}$ to be extracted from experimental data using a ruler and graph paper. Modern curve-fitting software has made the graphical method less necessary, but the plot remains a powerful diagnostic tool because different types of inhibition produce visually distinct patterns.

## A.2 Competitive inhibition

A competitive inhibitor is a molecule that resembles the substrate closely enough to bind the active site but cannot be catalyzed. While the inhibitor occupies the active site, the substrate is locked out. The effect: the enzyme appears to have a higher $K_m$ (it needs more substrate to reach half-saturation) but $V_{\max}$ is unchanged -- if you add enough substrate, you can always outcompete the inhibitor.

On a Lineweaver-Burk plot, competitive inhibition changes the slope and x-intercept but leaves the y-intercept ($1/V_{\max}$) unchanged. The lines pivot around the y-axis.

## A.3 Non-competitive inhibition

A non-competitive inhibitor binds at a site other than the active site (an allosteric site), distorting the enzyme's shape so that catalysis is impaired whether or not substrate is bound. The effect: $V_{\max}$ decreases (fewer functional enzyme molecules) but $K_m$ is unchanged.

The inhibitor dissociation constant is:

$$
K_I = \frac{[\text{E}][\text{I}]}{[\text{EI}]}
$$

For the simplest case of pure non-competitive inhibition (where $K_I' = K_I$, meaning the inhibitor binds the free enzyme and the enzyme-substrate complex with equal affinity), the rate equation becomes:

$$
V = \frac{V_{\max}[\text{S}]}{K_m + [\text{S}]} \cdot \frac{K_I}{K_I + [\text{I}]}
$$

The second factor is a simple scaling term: it multiplies the uninhibited rate by the fraction of enzyme molecules not bound to inhibitor.

On a Lineweaver-Burk plot, non-competitive inhibition changes the slope and y-intercept but leaves the x-intercept ($-1/K_m$) unchanged. The lines pivot around the x-axis.

## A.4 Irreversible inhibition

Some inhibitors form covalent bonds with the enzyme, permanently inactivating it. These are not governed by equilibrium binding constants; the effect is time-dependent and cumulative. Many toxins and pharmaceutical drugs work this way -- aspirin, for instance, irreversibly acetylates cyclooxygenase.

## A.5 pH and temperature optima

Every enzyme has a pH and temperature at which it works best. Deviate too far in either direction and the rate drops, often sharply.

- **Temperature**: increasing temperature raises the kinetic energy of molecules, generally speeding reactions. But proteins are only marginally stable. Beyond the optimum, the enzyme begins to denature -- its three-dimensional structure unfolds, and the active site geometry is lost. The rate curve rises, peaks, then crashes. For most mesophilic enzymes the peak is near 35--40 degrees C. For thermophilic enzymes from hot-spring archaea, the peak can exceed 80 degrees C.
- **pH**: active-site residues have ionizable groups (histidine, glutamate, lysine) that must be in the correct protonation state for catalysis. Shifting the pH protonates or deprotonates these groups, disrupting substrate binding or transition-state stabilization. Most intracellular enzymes are optimized near pH 7, but enzymes in extreme environments (stomach acid, soda lakes) have shifted optima.

These optima are not arbitrary. They are the result of evolutionary tuning to the conditions the organism actually encounters. The thermal record preserved in reconstructed ancestral proteins -- 60--70 degrees C for the earliest life, cooling to 35--37 degrees C for modern mesophiles -- is precisely the evolutionary shift in temperature optimum, tracked across billions of years.

# Geochemical Estimation Tools

## A.6 The NOSC: a simple proxy for energy content

In 2011, Douglas LaRowe and Philippe Van Cappellen showed that the energetic content of organic compounds scales, to a useful approximation, with a single number: the Nominal Oxidation State of Carbon (NOSC).

The empirical relation is:

$$
\Delta G_{\text{Cox}}^0 = 60.3 - 28.5 \times \text{NOSC}
$$

where $\Delta G_{\text{Cox}}^0$ is the standard Gibbs energy of the oxidation half reaction in kJ per mole of carbon.

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

where $Z$ is the net charge of the organic compound, and $a, b, c, d, e, f$ are the stoichiometric coefficients of C, H, N, O, P, and S.

The NOSC spectrum runs from fully reduced (methane, CH$_4$, NOSC = $-4$) to fully oxidized (carbon dioxide, CO$_2$, NOSC = $+4$). A molecule with a low NOSC is energy-rich: it has many electrons to give away. A molecule with a high NOSC is energy-spent: its carbon has already been stripped.

As Arndt et al. noted: "NOSC has the advantage that it does not require structural information to estimate energetic potential of complex natural organic matter." This makes it particularly useful for the complex, heterogeneous mixtures of natural organic matter found in sediments and soils, where detailed structural characterization is often impossible.

## A.7 Isotope fractionation as a biosignature

Isotope ratios are among the most durable biosignatures available to geologists. The logic is simple:

1. Enzymes discriminate between isotopes because lighter atoms vibrate faster and are slightly easier to incorporate.
2. This discrimination produces a measurable offset ($\delta^{13}$C, $\delta^{15}$N) between the substrate pool and the biological product.
3. The offset is preserved in minerals long after the organisms have decomposed.

For carbon, the standard measure is $\delta^{13}$C, reported in parts per thousand (per mil) relative to a standard:

$$
\delta^{13}\text{C} = \left(\frac{(^{13}\text{C}/^{12}\text{C})_{\text{sample}}}{(^{13}\text{C}/^{12}\text{C})_{\text{standard}}} - 1\right) \times 1000
$$

Typical autotrophic biomass has $\delta^{13}$C values around $-20$ to $-35$ per mil, while inorganic marine carbonate sits near $0$ per mil. A graphite inclusion at $-28$ per mil in a 3.8-billion-year-old rock is hard to explain without biology.

The catch: some abiotic processes (like Fischer-Tropsch synthesis in hydrothermal systems) can also fractionate carbon. The isotope signal is suggestive, not proof. Context matters -- and so does finding the signal preserved in the right mineral host, at the right age, in rocks that haven't been cooked beyond recognition.
