---
title: "Appendix D --- Math Without Pain"
---

This appendix collects the quantum-mechanical derivations and detailed mathematical treatments that support the main text. Readers who want the full machinery will find it here; readers who skipped the Deep Dives can return to these sections when curiosity strikes.

## D.1 The Schrodinger equation: from waves to energy levels

The machinery that connects wave-particle duality to energy quantization is the Schrodinger equation. Before we derive it, the experimental evidence that demands it.

In 1924, Louis de Broglie proposed that every particle has an associated wavelength:

$$
\lambda = \frac{h}{mv}
$$

where $m$ is the particle's mass and $v$ its velocity. For a baseball, $\lambda$ is far smaller than an atomic nucleus and wave behavior is undetectable. For an electron, $\lambda$ is comparable to the spacing between atoms in a crystal, and wave behavior dominates. Three years later, Clinton Davisson and Lester Germer at Bell Labs fired electrons at a nickel crystal and observed a diffraction pattern --- the unmistakable signature of wave interference. Electrons were not tiny billiard balls; they were also waves. The wave-particle duality that had startled physicists with light now extended to all matter.

Now the derivation, compressed but honest.

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

## D.2 How molecules store energy: the hierarchy

Molecules store energy in four quantized modes, forming a hierarchy by the size of their energy gaps:

$$
\Delta E_{\text{electronic}} \gg \Delta E_{\text{vibrational}} \gg \Delta E_{\text{rotational}} \gg \Delta E_{\text{translational}}
$$

### Electronic energy

Electrons in atoms and molecules occupy discrete orbitals, and the energy gaps between orbitals are large---typically on the order of electron-volts (hundreds of kJ/mol). Transitions between electronic states are what make photosynthesis and the photoelectric effect work. These are the most energetic transitions in chemistry.

### Vibrational energy

Atoms in a molecule vibrate around their equilibrium positions like masses connected by springs. Quantum mechanics says these vibrations are quantized: a bond can vibrate with 0, 1, 2, ... quanta of vibrational energy, but nothing in between. The energy levels of a quantum harmonic oscillator are:

$$
E_n = \left(n + \tfrac{1}{2}\right)h\nu_{\text{vib}} \qquad n = 0, 1, 2, \ldots
$$

The $\tfrac{1}{2}h\nu_{\text{vib}}$ term---the zero-point energy---means that even at absolute zero, a bond is never perfectly still. Infrared spectroscopy probes these transitions; the specific wavelengths absorbed are fingerprints of molecular structure.

### Rotational energy

Molecules rotate, and the rotation is quantized. For a rigid rotator (a reasonable approximation for small molecules), the allowed energies are:

$$
E_J = \frac{\hbar^2}{2I}J(J+1) \qquad J = 0, 1, 2, \ldots
$$

where $I$ is the moment of inertia. Rotational energy gaps are much smaller than vibrational ones, which is why rotational transitions show up in the microwave region of the spectrum.

### Translational energy

Even the simple motion of a molecule through space is quantized when the molecule is confined. For a particle in a one-dimensional box of length $a$:

$$
\varepsilon_n = \frac{n^2 h^2}{8ma^2} \qquad n = 1, 2, 3, \ldots
$$

For a macroscopic container, the energy gaps between translational levels are fantastically small, and the quantization is undetectable---translation looks continuous. But the mathematical framework still applies and is essential for statistical mechanics.

### Thermal population and the partition function

At room temperature ($k_BT \approx 2.5$ kJ/mol $\approx 0.026$ eV), translational and rotational modes are fully excited---the thermal energy is much larger than the gaps, so many quantum states are populated. Most vibrational modes are only partially excited (their gaps are comparable to $k_BT$), and electronic transitions are essentially frozen out (the gaps are far above $k_BT$).

This hierarchy explains, for instance, why heating a gas increases its pressure (translational energy changes easily) long before it changes color (electronic transitions require much more energy).

In three dimensions, translational states can be **degenerate**: different combinations of quantum numbers $(n_x, n_y, n_z)$ can give the same total energy. Degeneracy matters for statistical mechanics---it determines how many microstates correspond to a given macrostate, which feeds directly into entropy.

The full partition function of a molecule is a product of contributions from each mode:

$$
q_{\text{total}} = q_{\text{trans}} \cdot q_{\text{rot}} \cdot q_{\text{vib}} \cdot q_{\text{elec}}
$$

From this partition function, all thermodynamic quantities---internal energy, entropy, heat capacity, and ultimately $\Delta G$---can be calculated. Statistical mechanics is the bridge between the quantum mechanics of individual molecules and the thermodynamics of bulk matter.
