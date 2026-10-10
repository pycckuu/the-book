---
title: "Model Toolkit"
---

This appendix collects the mathematical machinery behind the reaction--transport models discussed in "Modeling the Invisible" and "Cities Without Sunlight". Readers who skipped the Sidebar callouts can find the full framework here; readers who followed every sidebar can use this as a concise reference.

## The diagenetic equation

The conservation (balance) equation for any species in one-dimensional sediment is Berner's diagenetic equation [@Berner1980Early]:

$$
\frac{\partial \hat{C}}{\partial t} = -\frac{\partial F}{\partial x} + \sum R
$$

where $\hat{C}$ is the bulk concentration (averaged over a volume larger than several grain diameters but smaller than the macroscopic gradient), $F$ is the flux, and $\sum R$ is the net source or sink from all reactions.

For a **solute** in porewater:

$$
\hat{C} = \varphi\, C
$$

where $\varphi$ is porosity and $C$ is concentration per unit volume of porewater.

For a **solid species**:

$$
\hat{C} = (1 - \varphi)\, B
$$

where $B$ is the amount per unit volume of solids [@Boudreau1997Diagenetic].

### Steady state

At steady state relative to the sediment--water interface ($\partial \hat{C}/\partial t = 0$), changes in a solid-phase species are observed only when following a sediment layer downward (i.e., in the reference frame of the solid phase):

$$
\frac{D\hat{C}}{Dt} = w\,\frac{\partial \hat{C}}{\partial x}
$$

where $w$ is the burial velocity of solids and $D/Dt$ is the material derivative following the solid phase.

## Transport terms

### Advection

Solute advective flux:

$$
F_A = \varphi\, u\, C
$$

Solid advective flux:

$$
F_A = (1 - \varphi)\, w\, B
$$

where $u$ is porewater velocity and $w$ is solid burial velocity.

### Compaction

During compaction, porewater moves upward relative to sediment grains but usually still moves downward in the interface-anchored reference frame --- appearing slower than the solids.

### Externally impressed flow (Darcy)

$$
u_x = -\frac{k}{\varphi\,\mu}\,\frac{\partial p'}{\partial x}
$$

where $k$ is permeability, $\mu$ is dynamic viscosity, and $p'$ is the reduced pressure [@Boudreau1997Diagenetic].

## Reaction rate expressions

### Respiration (dual-Monod)

$$
R_{\text{resp}} = k_{\text{resp}} \cdot [B] \cdot \frac{[\text{TED}]}{[\text{TED}] + K_m^{\text{TED}}} \cdot \frac{[\text{TEA}]}{[\text{TEA}] + K_m^{\text{TEA}}}
$$

where TED denotes the electron donor and TEA the terminal electron acceptor; TED is retained as the equation identifier [@Jin2005; @Thullner2007].

### Hydrolysis (Michaelis--Menten)

$$
R_{\text{hydr}} = k_{\text{cat}} \cdot [E] \cdot \frac{[\text{POM}]}{[\text{POM}] + K_m^{\text{POM}}}
$$

where $k_{\text{cat}}$ is the turnover number, $[E]$ is enzyme concentration, and POM is particulate organic matter [@Dale2006; @Thullner2007].

### Thermodynamic factor

The logistic gate formerly shown here is a heuristic, not a net thermodynamic rate law: it remains one-half at chemical equilibrium. ["Modeling the Invisible"](../chapters/08-the-equation.md) defines the coupled driving force and points to a primary formulation [@Jin2003]. Application requires a consistent reaction and energy basis, plus a domain for forward or reverse rates. The oxygen pilot does not use thermodynamic gating. The broader treatment remains [@Jin2005; @Regnier2011].

### Temperature dependence (Arrhenius)

$$
k = k^\circ \exp\!\left[-\frac{E_a}{R}\left(\frac{1}{T} - \frac{1}{298.15}\right)\right]
$$

Note: The Arrhenius equation is semi-empirical, derived for elementary reactions. Apparent $E_a$ values are generally calculated from rate measurements [@Arndt2013; @Leal2015].

## Growth, yield, and decay

Standard biomass model [@Thullner2007; @Dale2010]:

$$
\frac{\partial [B]}{\partial t} = Y \cdot R_{\text{resp}} - \mu_{\text{dec}} \cdot [B]
$$

Yield coefficient approaches:

- Theoretical (energy-based), @Rittmann2001: $R^2 = 0.9$.
- Theoretical (Gibbs dissipation), @Heijnen1992: $R^2 = 0.9$.
- Empirical, @Roden2011: $Y = 0.28 + 0.0211 \cdot (-\Delta G')$.

Monod growth kinetics:

$$
r_X = \mu_{\max}\,\frac{S}{K + S} \cdot X
$$

## Mineral dissolution/precipitation rate laws

Mineral reactions are commonly expressed using transition-state theory (TST) rate laws [@Leal2015]:

$$
r = k \cdot a_i \left(1 - \frac{Q}{K}\right)
$$

where $k$ is the rate constant, $a_i$ is the activity of a catalytic or inhibiting species, $Q$ is the ion activity product, and $K$ is the equilibrium constant. When $Q/K < 1$ the mineral dissolves; when $Q/K > 1$ it precipitates. Near-equilibrium behavior can be adjusted with empirical exponents:

$$
r = k \cdot a_i \left[\left(1 - \frac{Q}{K}\right)^\xi\right]^\nu
$$

When aqueous speciation reactions are much faster than mineral reactions, modelers sometimes replace the fast aqueous reactions with algebraic equilibrium constraints (the partial-equilibrium assumption), solving only the slower mineral kinetics as differential equations.

## Software and tools

Several geochemical modeling codes implement the frameworks described above:

- **PHREEQC** (Parkhurst and Appelo, 1999, 2013)
- **The Geochemist's Workbench** (Bethke, 2007)
- **EQ6** (Wolery and Daveler, 1992)
- **CHESS** (van der Lee and Windt, 2002)
- **CrunchFlow** for multicomponent reactive transport in porous media [@Steefel2005]
- **PFLOTRAN** for massively parallel subsurface flow and reactive transport [@Hammond2014]

Increasingly, modelers do not choose a single monolithic code and stay inside it forever. They couple solvers. **Alquimia v1.0** is one example: a generic interface designed to let multiphysics simulators talk to mature geochemical engines such as PFLOTRAN and CrunchFlow without rewriting the chemistry each time [@Molins2025].

For readers who want to build and run their own reaction--transport simulations of the processes described in this book, the open-source **[PorousMediaLab](https://github.com/biogeochemistry/PorousMediaLab)** provides a Python-based framework for modeling biogeochemical reactions in porous media. It implements many of the rate expressions and transport equations presented here, and can serve as a hands-on companion to the mathematical theory.

The frontier is moving again. Machine-learning surrogates and physics-informed neural networks are beginning to accelerate selected parts of reactive-transport workflows, especially where repeated forward solves are the main computational cost [@Adhikari2026]. These approaches do not replace conservation laws; they try to solve them faster.


## Oxygen pilot: sign and volume conventions

For the pilot, use $C$ [mol m$^{-3}$ porewater], $\phi$ [dimensionless], $D_s$ [m$^2$ s$^{-1}$, tortuosity corrected, excluding porosity], $k$ [s$^{-1}$] and depth $x$ [m, downward]. The bulk inventory is $\phi C$, the positive porewater consumption rate is $q=kC$, the signed bulk source is $R=-\phi kC$, and the downward flux is $F=-\phi D_s C_x$. The general conservative balance is:

$$
\frac{\partial(\phi C)}{\partial t}
=\frac{\partial}{\partial x}\left(\phi D_s C_x\right)-\phi kC.
$$

Only for constant porosity and diffusivity does this reduce to $C_t=D_sC_{xx}-kC$. The surface concentration is fixed at $C_0$, the lower boundary has $C_x(L)=0$, and the initial interior concentration is zero. The discontinuous surface step is not used to establish a smooth time-convergence order.

At steady state, $C_*=C_0\cosh((L-x)/\ell)/\cosh(L/\ell)$ with $\ell=\sqrt{D_s/k}$. Its inward flux equals its depth-integrated bulk consumption. The numerical companion checks this equality, second-order spatial convergence, first-order time convergence with a smooth analytic mode, and nonnegativity without clipping. All default parameters and fitting observations are synthetic or illustrative. Measured station summaries are used only in a separate provenance and observable-comparison exercise. These are numerical checks, not independent empirical validation.
