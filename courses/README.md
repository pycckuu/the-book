# Modeling course

The course turns selected questions from the narrative into small models whose assumptions, units and accounting can be inspected. Read the book for the story; use the modules to make predictions, check calculations and test what a simplified model can support.

## Available modules

1. **Oxygen diffusion and consumption**: read a steady porewater profile, account for diffusive supply and aggregate consumption, and distinguish an identifiable ratio from separate rate and diffusivity parameters. [English](oxygen-diffusion/en/README.md), [Russian](oxygen-diffusion/ru/README.md).
2. **Advection, dispersion and parent loss**: follow a finite-column pulse, separate physical and numerical spreading, and account for input, export, parent loss and retained storage. [English](advection-dispersion/en/README.md), [Russian](advection-dispersion/ru/README.md).
3. **Saturation kinetics**: distinguish a mechanistic Michaelis-Menten approximation from an empirical Monod response and track substrate depletion under stated capacity assumptions. [English](saturation-kinetics/en/README.md), [Russian](saturation-kinetics/ru/README.md).
4. **Energy constraints**: connect a reversible batch reaction to its declared basis, gross and net conversion, Gibbs availability and power, including boundary and empty-state domains. [English](energy-constraints/en/README.md), [Russian](energy-constraints/ru/README.md).

Use the separate [English modeling guide](modeling-guide/modeling-guide-en.md) or [Russian modeling guide](modeling-guide/modeling-guide-ru.md) to orient yourself before the exercises. It explains the four examples with equations, worked calculations, saved-data graphs and the limits of each model. The guide adds no assessment workload.

Each module supplies English and Russian readings, exercises, separately titled public worked answers, a verified model and saved outputs. The supplied tables support a route without Python. Attempt the exercises before consulting the answers and record what help you used. Access to answers does not establish unaided mastery.

## Entry skills and reading order

Start with Chapter 8's observations, units and signed balances, supported by Appendix B's model toolkit. Use the guide, then oxygen, advection-dispersion, saturation and energy in that order. Completing every previous solver is not a prerequisite: each module's diagnostic and existing optional bridge help you check preparation.

- **Transport:** distinguish concentration from amount, identify the volume basis and track flux signs.
- **Saturation:** distinguish rate from accumulation; use elementary derivatives and exponential decay.
- **Energy:** use dimensionless logarithms and a declared reaction basis, with the selected Gibbs passages in Chapter 1.

The guide and worksheet instructions supply the worked modeling steps. Appendix D contains quantum and energy derivations; it is not the elementary units, logarithms and differential-equation refresher needed to enter these modules. All existing exercise IDs, points and planned durations remain unchanged.

## Delivery and evidence

All four modules' exercises, scientific readings and public answers are included as F-Q in the English book and the combined Russian book builder, in the same order. The guide is a standalone reading with its own [build instructions](modeling-guide/README.md). Module helpers and release downloads keep English and Russian in separate files.

The [Russian book builder](../translations/ru/README.md) assembles Chapters 1-10, the Epilogue and Appendices A-Q into one `the-invisible-architects-ru.pdf` and one `the-invisible-architects-ru.epub`, separately from English files.

Numerical verification concerns the declared equations and illustrative or synthetic scenarios. It does not establish validity in a natural system, biological mechanism or learner performance. Learner-pilot protocols remain unexecuted; their durations are planned rather than observed.

## Planned extensions

The following blocks are a development sequence, not available or verified modules:

1. **Growth, yield and maintenance:** couple substrate accounting to biomass, distinguish growth from maintenance and decay, and examine what observations can identify.
2. **Coupled redox processes:** combine a bounded set of donor and acceptor balances and test when supply or inhibition changes the predicted ordering.
3. **Mineral and methane applications:** add selected reaction closures only after their accounting and prerequisite models are established.

The proposed order adds one dependency at a time. It is not a promise that one simple rate law transfers unchanged to every metabolism. Community interactions, general calibration and uncertainty, and speciation/mineral applications extend beyond the four accepted companions. Each new block needs a declared model contract, checked sources, numerical verification, exercises and public answers, aligned Russian materials and rendered review before joining the available modules.

The accepted modules do not certify every inherited equation or claim in the book.
