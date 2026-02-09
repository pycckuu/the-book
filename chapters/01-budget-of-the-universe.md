---
title: "The Budget of the Universe"
---

In the spring of 1943, a physicist who had already changed the world once sat down to give a series of lectures at Trinity College, Dublin. Erwin Schrodinger was sixty-one, exiled from Austria, and restless. He had won the Nobel Prize a decade earlier for an equation that described how matter behaves at atomic scales. Now he wanted to ask a question that no physicist had any business asking:

What is life?

Not what life is *made of*---biochemists were sorting that out. Not where life *came from*---that was still anyone's guess. Schrodinger wanted to know what physical rules a living system must obey simply to persist. He looked at biology and saw thermodynamics. The lectures became a slim book, published in 1944, and the book became one of the most influential scientific texts of the twentieth century.[^schrodinger1944]

Schrodinger's argument was almost unsettling in its clarity. Living systems maintain internal order---precise molecular arrangements, concentration gradients, structured membranes---in a universe that relentlessly erases differences. The Second Law of Thermodynamics says that the total disorder of a closed system can only increase. So how does a bacterium, a fern, or a physicist stay organized?

Not by violating the Second Law. By *obeying it creatively*. A living organism maintains its internal order by exporting disorder---entropy---to the surroundings. It takes in structured energy (food, sunlight) and releases degraded energy (heat, waste). The organism stays organized; the universe, on balance, becomes more disordered. The accounting always works out.

Schrodinger also made a second, remarkably prescient prediction. He argued that the genetic material---whatever it was---must be a stable, information-bearing structure. He called it an "aperiodic crystal": not a repeating lattice like salt or diamond, but an irregular arrangement capable of encoding instructions. Nine years later, Watson and Crick described the double helix of DNA. It was, almost exactly, Schrodinger's aperiodic crystal.

But this chapter is not about DNA. It is about the first half of Schrodinger's insight: the energy rules. Before there was life, before there was an ocean, before there was a planet with liquid water, there were the laws of thermodynamics and quantum mechanics. These laws---discovered in European laboratories with hydrogen atoms, metal plates, and vacuum tubes---are the constitution that every chemical reaction, every metabolic pathway, and every living organism must obey.

They are the budget of the universe.

## Energy in packets

The story begins in 1900, with a problem about light.

Physicists at the time understood that hot objects glow. Heat a piece of iron and it radiates: first a dull red, then orange, then white. The spectrum of this radiation---how much energy comes out at each wavelength---had been measured precisely. But no one could explain it. The best theoretical predictions diverged from the data at short wavelengths, predicting infinite energy where experiments showed almost none. This embarrassment became known as the "ultraviolet catastrophe."[^planck1901]

Max Planck found the fix by making an assumption he didn't entirely believe. He proposed that energy is not emitted continuously, like water from a hose, but in discrete packets---*quanta*---whose size depends on frequency:

$$
E = h\nu
$$

Here $\nu$ is the frequency of the radiation and $h$ is a new constant of nature, now called Planck's constant ($h \approx 6.626 \times 10^{-34}$ J$\cdot$s). The constant is extraordinarily small, which is why the graininess of energy is invisible in everyday life. But at atomic and molecular scales, it is everything.

This is not abstract physics. It is the reason photosynthesis works. A chlorophyll molecule absorbs red light at around 680 nm because the energy of a red photon ($E = h\nu = hc/\lambda$) matches a specific electronic transition in chlorophyll. A photon of slightly lower energy, in the infrared, cannot make that jump. A photon of much higher energy, in the ultraviolet, would overshoot and cause damage. The quantization of energy is why biology runs on specific wavelengths and not on a continuous smear.

Five years after Planck's proposal, Albert Einstein pushed the idea further. He showed that light itself behaves as a stream of particles---photons---each carrying exactly one quantum of energy $E = h\nu$. His evidence came from the photoelectric effect: when light strikes a metal surface, it can knock electrons free, but only if each individual photon carries enough energy to overcome the binding force that holds the electron in the metal.[^einstein1905] Below a threshold frequency, nothing happens---no matter how bright the light. Above it, electrons fly out immediately. The energy of the ejected electrons increases linearly with the frequency of the incoming light, exactly as $E = h\nu$ predicts. Einstein received the Nobel Prize for this work in 1921, not for relativity.

The implications ripple forward through everything that follows in this book. Chemical bonds have specific energies. Breaking them requires a minimum energy input. Forming new bonds releases specific amounts of energy. None of this would work if energy were continuous.

## The hydrogen-chlorine cannon

To see what quantized energy means in practice, consider a demonstration that could have come from a nineteenth-century lecture hall---and occasionally did, with spectacular results.

Mix hydrogen gas and chlorine gas in a sealed tube. At room temperature, nothing happens. The molecules drift past each other, colliding but not reacting. The reaction $\text{H}_2 + \text{Cl}_2 \rightarrow 2\text{HCl}$ is thermodynamically favorable; the products are lower in energy than the reactants. But "favorable" and "spontaneous" are not the same thing. There is a barrier in the way.

The barrier is the Cl--Cl bond. Before hydrogen and chlorine atoms can rearrange into HCl, the chlorine molecule must first be broken apart. That costs energy. How much? The bond dissociation energy of Cl$_2$ is 242 kJ/mol. The H--H bond is stronger: 436 kJ/mol. Each new H--Cl bond that forms releases 431 kJ/mol.

The overall energy balance:

$$
\Delta H = \underbrace{(436 + 242)}_{\text{bonds broken}} - \underbrace{2 \times 431}_{\text{bonds formed}} = -184 \text{ kJ/mol}
$$

The reaction releases 184 kJ of heat for every mole of H$_2$ consumed. It is exothermic---profitable, in thermodynamic terms.

But to get started, someone has to pay the activation cost: breaking that first Cl--Cl bond. Convert to the energy per single bond:

$$
E_{\text{bond}} = \frac{242 \times 10^3}{6.022 \times 10^{23}} = 4.02 \times 10^{-19} \text{ J}
$$

Now ask: what wavelength of light carries exactly this much energy per photon?

$$
\lambda = \frac{hc}{E} = \frac{(6.626 \times 10^{-34})(3.0 \times 10^8)}{4.02 \times 10^{-19}} \approx 494 \text{ nm}
$$

That is blue light. Shine a red lamp at the mixture and nothing happens---each photon is too feeble to snap a Cl--Cl bond. Shine a blue or violet lamp and the reaction ignites. Once a few Cl--Cl bonds break, the released chlorine atoms attack H$_2$ molecules, which starts a chain reaction. The temperature in the tube can soar by thousands of kelvins; the pressure can spike above 20 atmospheres. The tube becomes a cannon.

This is quantization in action. The reaction is favorable, the reactants are mixed, and yet nothing happens until a photon of the right energy arrives to pay the activation cost. Red light is too cheap. Blue light is expensive enough. The universe does not negotiate on the price.

Every reaction in biochemistry follows the same logic. Enzymes do not change whether a reaction is favorable; they lower the activation barrier so that the reaction can proceed at body temperature. They are, in effect, a substitute for the blue lamp---a way to start the cannon without the explosion.

## The budget: Gibbs free energy

The hydrogen-chlorine cannon illustrates one of the most important distinctions in all of science: the difference between energy that is *released* and energy that is *available to do work*. Not all released energy is useful. Some of it dissipates as disordered heat. Some of it goes into rearranging the surroundings in ways you cannot harness. To understand what a reaction can actually accomplish---whether it can build a molecule, pump an ion across a membrane, or power a flagellar motor---you need a sharper accounting tool.

That tool was invented by Josiah Willard Gibbs in the 1870s, and it is the single most important equation in this book.[^gibbs1873]

$$
G = H - TS
$$

Read it as a budget. $H$ is enthalpy---roughly, the total energy content of the system (heat plus pressure-volume work). $T$ is temperature. $S$ is entropy---a measure of disorder, or more precisely, the number of microscopic arrangements consistent with the macroscopic state. The product $TS$ is the energy that has been "claimed" by disorder: energy that is spread out so evenly it can no longer drive anything in a particular direction.

$G$, the Gibbs free energy, is what remains. It is what you can actually spend.

When a reaction occurs, the change in Gibbs free energy tells you the direction:

- If $\Delta G < 0$: the reaction can proceed spontaneously. It releases usable energy.
- If $\Delta G > 0$: the reaction requires an input of energy. It will not happen on its own.
- If $\Delta G = 0$: the system is at equilibrium. No net change occurs.

The biological metaphor writes itself. Enthalpy is your gross income. The entropy term $TS$ is the tax---the portion the universe takes as payment for allowing things to happen. Gibbs free energy is your disposable income: the fraction you can direct toward maintenance, growth, or reproduction.

Microbes are accountants. They do not run reactions because the reactions are interesting. They run reactions because $\Delta G$ is negative enough to cover the cost of staying alive.

### Real conditions, not standard ones

The standard Gibbs energy $\Delta G^\circ$ is a reference point, measured under a specific set of conditions (typically 1 mol/L concentrations, 1 atm pressure, 25$^\circ$C). Real environments are nothing like this. A bacterium in a sediment pore faces concentrations that are orders of magnitude different from standard conditions. To know the actual energy available, you need the master equation:

$$
\Delta G = \Delta G^\circ + RT \ln Q
$$

Here $R$ is the gas constant (8.314 J mol$^{-1}$ K$^{-1}$), $T$ is absolute temperature, and $Q$ is the **reaction quotient**---the ratio of product activities to reactant activities, each raised to the power of its stoichiometric coefficient.

The reaction quotient is the universe's way of adjusting the price. When products accumulate, $Q$ increases, and $\Delta G$ becomes less negative: the reaction becomes less profitable. When reactants are abundant, $Q$ is small, and there is more energy to harvest. At equilibrium, $Q$ equals the equilibrium constant $K_{\text{eq}}$, and $\Delta G = 0$:

$$
\Delta G^\circ = -RT \ln K_{\text{eq}}
$$

This is not a separate equation. It is a special case of the one above, evaluated at the point where the reaction has no net tendency to move in either direction.

For biochemical reactions, a modified convention is often used: $\Delta G^{\circ\prime}$, where the prime indicates standard conditions at pH 7 rather than the chemist's convention of pH 0. Since most biology operates near neutral pH, this keeps the reference point close to reality.[^karp2008]

::: {.callout-note}
## Equation Corner --- Oxidation state as an energy proxy

A powerful shortcut for estimating how much free energy an organic molecule contains: look at the **average oxidation state of its carbon atoms**.

Methane (CH$_4$) is the most reduced single-carbon compound. Each carbon is surrounded by hydrogen; the oxidation state is $-4$. Carbon dioxide (CO$_2$) is fully oxidized: oxidation state $+4$. When an organism oxidizes methane all the way to CO$_2$, it extracts the maximum possible energy from that carbon atom.

Most organic molecules fall between these extremes. Glucose (C$_6$H$_{12}$O$_6$) has an average carbon oxidation state of 0. Fatty acids, with their long hydrocarbon chains, are more reduced (roughly $-2$ per carbon) and carry more energy per carbon. Carboxylic acids are more oxidized and carry less.

The insight is practical: **the oxidation state of the carbon atoms in an organic molecule provides a direct measure of its free-energy content**. You do not need to look up $\Delta G_f^\circ$ for every compound. A quick glance at the molecular formula tells you whether the molecule is energy-rich or energy-poor.

This will matter enormously when we start asking how microbes process organic matter in sediments. The "freshness" or "reactivity" of organic material is, at bottom, an oxidation-state story.
:::

## Waves, particles, and the quantum foundation

Planck's quanta and Einstein's photons answered the question of how much energy light carries. But they opened a deeper question: what *is* light? And if photons behave like particles, do particles ever behave like waves?

In 1924, Louis de Broglie---then a graduate student in Paris---proposed that the answer is yes. Every particle, he argued, has an associated wavelength:[^haslett1972]

$$
\lambda = \frac{h}{mv}
$$

where $m$ is the particle's mass and $v$ its velocity. For a baseball, $\lambda$ is absurdly small---far smaller than an atomic nucleus---and wave behavior is undetectable. For an electron, $\lambda$ is comparable to the spacing between atoms in a crystal, and wave behavior dominates.

Three years later, Clinton Davisson and Lester Germer at Bell Labs fired a beam of electrons at a nickel crystal and observed a diffraction pattern---the unmistakable signature of wave interference.[^davisson1927] Electrons were not tiny billiard balls. They were *also* waves. De Broglie's prediction was confirmed, and the wave-particle duality that had startled physicists with light now extended to all matter.

This duality is not a philosophical curiosity. It is the reason atoms have discrete energy levels, the reason chemical bonds exist, and the reason the periodic table has the structure it does. Electrons confined to an atom cannot have arbitrary energies for the same reason that a guitar string cannot vibrate at arbitrary frequencies: the boundary conditions select only certain standing-wave patterns, and each pattern corresponds to a specific energy.

::: {.callout-note}
## Deep Dive --- The Schrodinger equation: from waves to energy levels

The machinery that connects wave-particle duality to energy quantization is the Schrodinger equation. Here is the logic, compressed but honest.

**Step 1: Start from a wave.** A free particle moving in one dimension can be described by a wave function:

$$
\Psi(x, t) = e^{i(kx - \omega t)}
$$

where $k$ is the wave number (related to momentum by de Broglie: $p = \hbar k$, with $\hbar = h/2\pi$) and $\omega$ is the angular frequency (related to energy by Planck: $E = \hbar\omega$).

**Step 2: Extract momentum.** Differentiate twice with respect to position:

$$
\frac{\partial^2 \Psi}{\partial x^2} = -k^2 \Psi
$$

Since $p = \hbar k$, this means $p^2 \Psi = -\hbar^2 \frac{\partial^2 \Psi}{\partial x^2}$.

**Step 3: Write the energy condition.** Total energy is kinetic plus potential: $E = \frac{p^2}{2m} + V$. Substituting:

$$
E\,\Psi = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\,\Psi
$$

This is the **time-independent Schrodinger equation** (TISE). It says: the allowed energies of a quantum system are those values $E$ for which this equation has well-behaved solutions.

**Step 4: Add time.** From $E = \hbar\omega$ and $\Psi \propto e^{-i\omega t}$, differentiate once with respect to time:

$$
i\hbar\frac{\partial \Psi}{\partial t} = E\,\Psi
$$

Combining with the TISE gives the **time-dependent Schrodinger equation**:

$$
i\hbar\frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\,\Psi
$$

**What we sacrificed in this presentation:** rigor. The argument above is a plausibility construction, not a derivation from first principles. The Schrodinger equation is a *postulate*---it cannot be derived from classical mechanics any more than Newton's second law can be derived from kinematics. Its justification is that it works: every prediction it makes matches experiment.

**What we kept:** the direct connection between de Broglie's wavelength, Planck's energy quantization, and the equation that governs all of chemistry. The TISE is the equation that produces the energy levels of hydrogen, the shapes of molecular orbitals, and the bond energies that appear in every reaction in this book.

The probability interpretation matters too. $|\Psi|^2$ gives the probability of finding the particle at a given location. Before measurement, the electron does not have a definite position; it has a probability distribution. As physicists learned to say: in the absence of a measurement, there is no single trajectory---only a spread of possibilities weighted by $|\Psi|^2$.
:::

## How molecules store energy

Quantization does not stop at individual atoms. Molecules store energy in multiple ways, each governed by the same quantum rules but operating at different scales. Understanding these modes matters because they determine how much energy a collection of molecules carries at a given temperature---which, in turn, determines the thermodynamic properties that feed into $\Delta G$.

**Electronic energy.** Electrons in atoms and molecules occupy discrete orbitals, and the energy gaps between orbitals are large---typically on the order of electron-volts (hundreds of kJ/mol). Transitions between electronic states are what make photosynthesis and the photoelectric effect work. These are the most energetic transitions in chemistry.

**Vibrational energy.** Atoms in a molecule vibrate around their equilibrium positions like masses connected by springs. Quantum mechanics says these vibrations are quantized: a bond can vibrate with 0, 1, 2, ... quanta of vibrational energy, but nothing in between. The energy levels of a quantum harmonic oscillator are:

$$
E_n = \left(n + \tfrac{1}{2}\right)h\nu_{\text{vib}} \qquad n = 0, 1, 2, \ldots
$$

The $\tfrac{1}{2}h\nu_{\text{vib}}$ term---the zero-point energy---means that even at absolute zero, a bond is never perfectly still. Infrared spectroscopy probes these transitions; the specific wavelengths absorbed are fingerprints of molecular structure.

**Rotational energy.** Molecules rotate, and the rotation is quantized. For a rigid rotator (a reasonable approximation for small molecules), the allowed energies are:

$$
E_J = \frac{\hbar^2}{2I}J(J+1) \qquad J = 0, 1, 2, \ldots
$$

where $I$ is the moment of inertia. Rotational energy gaps are much smaller than vibrational ones, which is why rotational transitions show up in the microwave region of the spectrum.

**Translational energy.** Even the simple motion of a molecule through space is quantized when the molecule is confined. For a particle in a one-dimensional box of length $a$:

$$
\varepsilon_n = \frac{n^2 h^2}{8ma^2} \qquad n = 1, 2, 3, \ldots
$$

For a macroscopic container, the energy gaps between translational levels are fantastically small, and the quantization is undetectable---translation looks continuous. But the mathematical framework still applies and is essential for statistical mechanics.

::: {.callout-note}
## Deep Dive --- How molecules store energy: the hierarchy

The four modes of molecular energy form a hierarchy by the size of their energy gaps:

$$
\Delta E_{\text{electronic}} \gg \Delta E_{\text{vibrational}} \gg \Delta E_{\text{rotational}} \gg \Delta E_{\text{translational}}
$$

At room temperature ($k_BT \approx 2.5$ kJ/mol $\approx 0.026$ eV), translational and rotational modes are fully excited---the thermal energy is much larger than the gaps, so many quantum states are populated. Most vibrational modes are only partially excited (their gaps are comparable to $k_BT$), and electronic transitions are essentially frozen out (the gaps are far above $k_BT$).

This hierarchy explains, for instance, why heating a gas increases its pressure (translational energy changes easily) long before it changes color (electronic transitions require much more energy).

In three dimensions, translational states can be **degenerate**: different combinations of quantum numbers $(n_x, n_y, n_z)$ can give the same total energy. Degeneracy matters for statistical mechanics---it determines how many microstates correspond to a given macrostate, which feeds directly into entropy.

The full partition function of a molecule is a product of contributions from each mode:

$$
q_{\text{total}} = q_{\text{trans}} \cdot q_{\text{rot}} \cdot q_{\text{vib}} \cdot q_{\text{elec}}
$$

From this partition function, all thermodynamic quantities---internal energy, entropy, heat capacity, and ultimately $\Delta G$---can be calculated. Statistical mechanics is the bridge between the quantum mechanics of individual molecules and the thermodynamics of bulk matter.
:::

## Chemical equilibrium and the reaction quotient

We have assembled the pieces: energy comes in quanta, bonds have specific energies, and the Gibbs free energy tracks how much usable work a reaction can deliver. Now we can formalize the concept of chemical equilibrium.

Every chemical species in a mixture has a **chemical potential** $\mu_i$---a measure of how much the system's free energy would change if you added one more mole of that species. For an ideal system:

$$
\mu_i = \mu_i^\circ + RT \ln a_i
$$

where $\mu_i^\circ$ is the standard chemical potential and $a_i$ is the **activity** of species $i$ (roughly, its effective concentration, corrected for non-ideal behavior). When activities are moderate and solutions are dilute, activities are often approximated by concentrations, which is what we will do in most of this book. The appendix on the Energy Toolkit discusses when and why that approximation breaks down.[^atkins2010]

The reaction quotient $Q$ for a general reaction $a\text{A} + b\text{B} \rightleftharpoons c\text{C} + d\text{D}$ is:

$$
Q = \frac{a_{\text{C}}^c \cdot a_{\text{D}}^d}{a_{\text{A}}^a \cdot a_{\text{B}}^b}
$$

Plugging the chemical potentials into the Gibbs energy expression gives us back the master equation:

$$
\Delta G = \Delta G^\circ + RT \ln Q
$$

At equilibrium, $\Delta G = 0$. The system has no net tendency to shift in either direction. The reaction quotient at this point equals the equilibrium constant:

$$
Q_{\text{eq}} = K_{\text{eq}}
$$

and therefore:

$$
\Delta G^\circ = -RT \ln K_{\text{eq}}
$$

This equation is a Rosetta Stone. It connects the standard free energy change (which you can look up in tables or calculate from bond energies) to the equilibrium constant (which tells you how far a reaction will go before it stops). A large negative $\Delta G^\circ$ means a large $K_{\text{eq}}$: the reaction strongly favors products. A $\Delta G^\circ$ near zero means the reaction is easily reversible and sensitive to conditions.

For microbial metabolism, the critical quantity is rarely $\Delta G^\circ$. It is $\Delta G$---the energy available *right here, right now*, at the actual concentrations in the local environment. Two identical reactions can have completely different $\Delta G$ values in different environments, because $Q$ depends on what has been consumed and what has accumulated. A reaction that is profitable near the sediment surface, where oxygen is present, may become unprofitable a centimeter deeper, where oxygen has been depleted.

This is why mud tells stories. The concentration profiles---oxygen dropping to zero, sulfate declining, methane appearing---are the visible signatures of $Q$ shifting through space, dragging $\Delta G$ with it.

## The rules before the game

Stand back for a moment and consider what we have assembled.

Planck showed that energy comes in packets. Einstein showed that light carries these packets as particles. De Broglie showed that particles behave as waves. Schrodinger wrote the equation that predicts the allowed energy states of any quantum system. From those energy states come bond energies, activation barriers, and the discrete electronic transitions that make photosynthesis and respiration possible.

Gibbs, working half a century before quantum mechanics, already had the thermodynamic framework: enthalpy minus the entropy tax gives you the free energy---the budget. With the reaction quotient $Q$ adjusting the budget for local conditions, you can calculate the energy available from any reaction in any environment.

These discoveries were made in an era when "biology" meant looking at cells through microscopes and cataloging species in jars. Planck was worrying about the spectrum of hot metal. Einstein was thinking about the photoelectric effect in a patent office. Gibbs was a reclusive professor in New Haven writing papers that almost nobody read. De Broglie was a French aristocrat writing a doctoral thesis that his examiners weren't sure they believed.

None of them were thinking about bacteria.

And yet. The rules they uncovered---quantized energy, wave-particle duality, the Gibbs budget, chemical equilibrium---are the same rules that govern every metabolic reaction in every living cell that has ever existed. They governed the first autocatalytic cycles in hydrothermal vents 4 billion years ago. They govern the sulfate-reducing bacteria 3 kilometers underground in a South African gold mine today. They will govern whatever organisms exist on whatever planets we eventually find.

This is the deepest lesson of the opening chapter. The physics was not designed for biology. It was designed for hydrogen atoms and metal plates. But biology had no choice except to obey it. Evolution does not negotiate with the Second Law. Natural selection can explore an enormous space of molecular strategies, but every strategy must balance the Gibbs budget. Every organism must find an energy source with $\Delta G < 0$ under local conditions, harvest that energy efficiently enough to cover the cost of maintenance and reproduction, and export the resulting entropy to the environment.

The rest of this book is the story of how microbes---the oldest, most successful, and most diverse organisms on Earth---solved that problem in every environment the planet offered. In hot springs and frozen Antarctic lakes. In sunlit surface waters and in sediments where no photon has penetrated for millions of years. On sulfur, on iron, on methane, on hydrogen, on organic matter that other organisms discarded as waste.

But all of those solutions are constrained by the same budget. And the budget was set before the first cell divided.

## Takeaway

- Energy comes in discrete packets ($E = h\nu$), which is why specific photons break specific bonds and why photosynthesis requires specific wavelengths.
- The Gibbs free energy $G = H - TS$ is the universal budget: enthalpy minus the entropy tax gives the energy available to do work.
- Under real conditions, $\Delta G = \Delta G^\circ + RT \ln Q$ adjusts the budget for actual concentrations. At equilibrium, $\Delta G = 0$ and the reaction quotient equals $K_{\text{eq}}$.
- Wave-particle duality and the Schrodinger equation explain *why* energy levels are discrete, *why* bonds have the strengths they do, and *why* molecules store energy in electronic, vibrational, rotational, and translational modes.
- These rules---discovered with hydrogen atoms and metal plates---are the same rules that will govern every bacterium, every enzyme, every metabolic pathway for the next 4.5 billion years of Earth's history.

[^schrodinger1944]: Erwin Schrodinger, *What Is Life? The Physical Aspect of the Living Cell* (Cambridge University Press, 1944). [@Schrodinger1944]

[^planck1901]: Max Planck, "Ueber das Gesetz der Energieverteilung im Normalspectrum," *Annalen der Physik* 309, no. 3 (1901): 553--563. [@Planck1901]

[^einstein1905]: Albert Einstein, "Concerning an Heuristic Point of View Toward the Emission and Transformation of Light" (1905). [@Einstein1905]

[^haslett1972]: Jared W. Haslett, "Phase Waves of Louis deBroglie," *American Journal of Physics* 40, no. 9 (1972): 1315. [@Haslett1972]

[^davisson1927]: C. Davisson and L. Germer, "Diffraction of Electrons by a Crystal of Nickel," *Physical Review* 30, no. 5 (1927): 705--740. [@Davisson1927]

[^gibbs1873]: Willard Gibbs, "A Method of Geometrical Representation of the Thermodynamic Properties of Substances by Means of Surfaces" (1873). [@Gibbs1873]

[^karp2008]: Gerald Karp, *Cell and Molecular Biology: Concepts and Experiments*, 7th ed. [@Karp2008]

[^atkins2010]: Peter Atkins and Loretta Jones, *Chemical Principles: The Quest for Insight* (2010). [@Atkins2010]
