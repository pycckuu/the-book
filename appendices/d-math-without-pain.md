---
title: "Math Without Pain"
---

This appendix collects the quantum-mechanical derivations and detailed mathematical treatments that support the main text. Readers who want the full machinery will find it here; readers who skipped the Sidebars can return to these sections when curiosity strikes.

## The Schrödinger equation: from waves to energy levels

Planck introduced quantized oscillator energies in his account of thermal radiation, and Einstein proposed light quanta.[^appd-light-quanta] But the discreteness runs deeper. Particles themselves behave as waves---a fact confirmed experimentally in the 1920s[^davisson1927] and formalized by the Schrödinger equation. Electrons confined to an atom cannot have arbitrary energies, for the same reason a guitar string cannot vibrate at arbitrary frequencies: the boundary conditions select only certain standing-wave patterns, and each pattern corresponds to a specific energy. Bound systems have discrete levels; free particles can have a continuous spectrum. Quantum mechanics underlies the molecular energies and spectra used throughout this book.

The machinery that connects wave-particle duality to energy quantization is the Schrödinger equation. Before we motivate it, the experimental evidence that demands it.

In 1924, Louis de Broglie proposed that every particle has an associated wavelength:

$$
\lambda = \frac{h}{mv}
$$

Here $mv$ is the nonrelativistic momentum, with $m$ the mass and $v$ the speed. For a baseball, $\lambda$ is far smaller than an atomic nucleus and wave behavior is undetectable. For electrons accelerated through tens of volts, as in the experiment below, $\lambda$ can be comparable to atomic spacings in a crystal, making diffraction observable. Three years later, Clinton Davisson and Lester Germer at Bell Labs fired electrons at a nickel crystal and observed a diffraction pattern --- the unmistakable signature of wave interference. Electrons were not tiny billiard balls; they were also waves. The wave-particle duality that had startled physicists with light now extended to matter.

Now the construction, compressed but honest. We consider one nonrelativistic particle in one dimension, with a time-independent potential $V(x)$.

**Step 1: Start from a wave.** An ideal free-particle plane wave is:

$$
\Psi(x, t) = e^{i(kx - \omega t)}
$$

where $k$ is the wave number ($p = \hbar k$, with $\hbar = h/2\pi$) and $\omega$ the angular frequency ($E = \hbar\omega$). This wave is not normalizable over the whole line. A localized particle is represented by a normalized superposition, a wavepacket.

**Step 2: Extract momentum.** Differentiate twice with respect to position:

$$
\frac{\partial^2 \Psi}{\partial x^2} = -k^2 \Psi
$$

For this plane wave, $p^2 \Psi = -\hbar^2 \frac{\partial^2 \Psi}{\partial x^2}$. This motivates the momentum operator $\hat p = -i\hbar\partial/\partial x$. Using that operator for general states is a quantum postulate, not a consequence of this one example.

**Step 3: Write the energy condition.** The classical energy is $E = \frac{p^2}{2m} + V(x)$. Replacing momentum by this operator gives, for a stationary spatial state $\psi(x)$:

$$
E\,\psi = -\frac{\hbar^2}{2m}\frac{d^2 \psi}{dx^2} + V(x)\,\psi
$$

This is the **time-independent Schrödinger equation** (TISE). Boundary conditions select the allowed energies: a discrete set for bound states, potentially a continuum for unbound states.

**Step 4: Add time.** For one energy eigenstate, $\Psi(x,t) = \psi(x)e^{-iEt/\hbar}$. Differentiate once with respect to time:

$$
i\hbar\frac{\partial \Psi}{\partial t} = E\,\Psi
$$

This stationary solution, and superpositions of such solutions, satisfy the **time-dependent Schrödinger equation**:

$$
i\hbar\frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\,\Psi
$$

**What we sacrificed in this presentation:** a full mathematical treatment. The Schrödinger equation is a *postulate*, motivated here by plane waves and classical energy. It is tested within its domain, not a guarantee that every approximation to a real system will match experiment. Relativistic effects require further theory.[^appd-quantum-construction]

**What we kept:** the connection between wavelength, energy, and allowed states. Extending the Hamiltonian to interacting electrons and nuclei provides the basis for calculating atomic and molecular energies. The one-particle equation above is the starting point, not the full molecular calculation.

The probability interpretation matters too. In one dimension, $|\Psi(x,t)|^2$ is a **probability density**. The probability of finding the particle between $a$ and $b$ is $\int_a^b |\Psi(x,t)|^2\,dx$, and a normalized state obeys $\int_{-\infty}^{\infty}|\Psi(x,t)|^2\,dx=1$. The wave function predicts a distribution of measurement outcomes, rather than a classical trajectory.[^appd-probability]

## How molecules store energy: the hierarchy

Molecular energy is often separated into electronic, vibrational, rotational and translational contributions. For many ordinary molecular gases, a useful schematic ordering is:

$$
\Delta E_{\text{electronic}} \gg \Delta E_{\text{vibrational}} \gg \Delta E_{\text{rotational}} \gg \Delta E_{\text{translational}}
$$

This ordering depends on the molecule and, for translation, the size of its container. Closely spaced electronic states and soft vibrations can break the pattern.

### Electronic energy

Electronic states differ in the arrangement of electrons. Their gaps are often on the electron-volt scale, larger than ordinary rotational or vibrational gaps. Light can populate electronic states, as in the pigments used by photosynthesis. A many-electron state energy is not simply the energy of one orbital.

### Vibrational energy

Near equilibrium, a molecular vibration can be approximated by a mass on a spring. For one harmonic mode, the energy levels are:

$$
E_n = \left(n + \tfrac{1}{2}\right)h\nu_{\text{vib}} \qquad n = 0, 1, 2, \ldots
$$

The $\tfrac{1}{2}h\nu_{\text{vib}}$ term is the zero-point energy: even the ground state has a spread of displacements. Real vibrations become anharmonic away from equilibrium. Infrared-active vibrations leave absorption fingerprints of molecular structure.

### Rotational energy

Molecules rotate, and the rotation is quantized. For a **linear rigid rotor**, such as a diatomic molecule with fixed bond length, the allowed energies are:

$$
E_J = \frac{\hbar^2}{2I}J(J+1) \qquad J = 0, 1, 2, \ldots
$$

Here $I$ is the moment of inertia about an axis perpendicular to the molecular axis. Nonlinear molecules require more rotational constants. Rotational energy gaps are often much smaller than vibrational gaps, with transitions in the microwave region.[^appd-molecular-levels]

### Translational energy

Even the simple motion of a molecule through space is quantized when the molecule is confined. For a particle in a one-dimensional box of length $a$:

$$
\varepsilon_n = \frac{n^2 h^2}{8ma^2} \qquad n = 1, 2, 3, \ldots
$$

For ordinary gases in macroscopic containers, the levels are so closely spaced compared with $k_BT$ that sums over them can usually be approximated by integrals. Translation then looks continuous, while the quantum framework still supplies the counting of states.

### Thermal population and the partition function

At room temperature (300 K), the thermal scale is $k_BT \approx 0.0259$ eV per molecule, equivalent to the molar scale $RT \approx 2.49$ kJ/mol, with $R = N_Ak_B$.[^appd-thermal-scale]

In thermal equilibrium, level populations depend on both energy gaps and degeneracy: $p_j/p_i = (g_j/g_i)\exp[-(E_j-E_i)/(k_BT)]$, where $p_i$ is the population probability of level $i$ and $g_i$ its number of states. Large gaps suppress excited populations; they do not make them exactly zero.

For many molecular gases at 300 K, numerous translational and rotational states are populated. Many bond-stretching vibrations remain close to their ground state because $h\nu_{\text{vib}}$ exceeds $k_BT$; softer modes can be appreciably populated. Electronic excitation is usually small, with exceptions for low-lying states.[^appd-thermal-populations]

In a cubic box, different combinations of quantum numbers $(n_x,n_y,n_z)$ can share one energy. This is **degeneracy**, the number of states at a given energy. It affects both thermal populations and entropy.

A molecular partition function counts thermally weighted states: $q=\sum_i g_i\exp[-E_i/(k_BT)]$, with a declared energy zero. If the contributions are independent and additive, it factors as:

$$
q_{\text{total}} = q_{\text{trans}} \cdot q_{\text{rot}} \cdot q_{\text{vib}} \cdot q_{\text{elec}}
$$

Real molecules couple rotation, vibration and electronic structure, so this product is an approximation. Bulk thermodynamics also requires an ensemble. For $N$ identical, noninteracting molecules in the dilute classical ideal-gas limit, the canonical partition function is $Q=q^N/N!$; $q$ includes the container volume. Interacting liquids and solutions require more than this ideal-gas counting. Reaction $\Delta G$ additionally needs consistent chemical reference states, temperature and activities, as in Chapter 1. Statistical mechanics supplies the bridge, once those assumptions are stated.[^appd-partition-bridge]

[^davisson1927]: Clinton Davisson and Lester Germer, "Diffraction of Electrons by a Crystal of Nickel," *Physical Review* 30 (1927): 705–740. [@Davisson1927]

[^appd-thermal-scale]: The molecular and molar scales are related by Avogadro's constant, $R = N_Ak_B$. The values at 300 K use the exact SI definitions of $k_B$, $N_A$ and the elementary charge for the joule-to-electronvolt conversion. [NIST, *The International System of Units (SI)*, Section 2](https://www.nist.gov/pml/special-publication-330/sp-330-section-2).

[^appd-quantum-construction]: Franz Kärtner, *Fundamentals of Photonics: Quantum Electronics*, MIT 6.974 (2006), Chapter 4, pp. 199-201, motivates the nonrelativistic equation from plane waves and the classical Hamiltonian. [@Kaertner2006Quantum]

[^appd-probability]: Allan Adams, *Quantum Physics I*, MIT 8.04 (2013), lecture 3, pp. 1-5 (density, normalization and wavepackets), lecture 5, pp. 2-3 (operators and plane-wave limits), and lecture 6, pp. 1-6 (stationary states, superpositions and continuum spectra). [@Adams2013Quantum]

[^appd-molecular-levels]: Robert W. Field and Robert Guy Griffin, *Physical Chemistry II*, MIT 5.62 (2008), lecture 11, pp. 3-9: electronic, harmonic vibrational and linear rigid-rotor levels, and the approximation of uncoupled contributions. [@FieldGriffin2008StatThermo]

[^appd-thermal-populations]: MIT 5.62, lecture 11, pp. 1 and 3-7, and lecture 14, pp. 3-4, treat Boltzmann weights, degeneracy and the low-temperature vibrational limit. [@FieldGriffin2008StatThermo]

[^appd-partition-bridge]: MIT 5.62, lecture 11, pp. 1-2 and 9, distinguishes molecular and ensemble partition functions. [@FieldGriffin2008StatThermo] Karl K. Irikura, *Essential Statistical Thermodynamics*, adapted from *Computational Thermochemistry* (1998), explains the ideal-gas and uncoupled-mode approximations and the reference energies needed for thermochemistry. [NIST CCCBDB](https://cccbdb.nist.gov/thermox.asp).

[^appd-light-quanta]: Max Planck (1901), quantized oscillator energies in thermal-radiation theory, and Albert Einstein (1905), the light-quantum proposal. The opening of this appendix provides the historical context. [@Planck1901; @Einstein1905]
