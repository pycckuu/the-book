# The Invisible Architects

**How Microbes Built the World**

> **Work in progress.** This book is under active development.

This book began as a stack of handwritten notes in a graduate student office at the University of Waterloo. I was trying to understand how microbes in sediments and groundwater make a living -- what they eat, how they breathe, why they arrange themselves in predictable layers, and what happens when you disturb those arrangements. The notes were dense with equations, short on narrative, and comprehensible mainly to me.

Years later, I realized that the story hiding inside those notes was bigger than any single research problem. It was the story of how invisible organisms -- too small to see, too numerous to count, too ancient to fully trace -- engineered the planet we live on. Not as a metaphor. As a measurable, quantifiable, physically constrained process that has been running for nearly four billion years and shows no sign of stopping.

That is the story this book tells.

The approach is chronological, story-driven, and quantitatively serious. Every equation earns its place by answering a question that the narrative raises. If a formula appears, it is because the words ran out of precision and the math picked up where they left off. The source material spans geomicrobiology, biogeochemistry, thermodynamics, quantum physics, and environmental science -- fields that rarely share a bookshelf but that describe different views of the same system.

The book is organized in four parts.

**Part I: The Rules of the Game** establishes only the physics the story actually needs: the energy budget of life and the planetary conditions that kept Earth wet, reactive, and out of equilibrium long enough for microbes to emerge.

**Part II: The First Society** introduces the earliest metabolisms, the first microbial communities, and the catastrophe that changed the atmosphere forever: the rise of oxygen. Here the emphasis shifts from physics to history, though the physics never leaves.

**Part III: The Great Mergers** traces how competition and cooperation among microbes produced the cellular architectures and metabolic partnerships that dominate life today. Syntrophy -- organisms surviving together on reactions that neither could manage alone -- turns out to be not an exception but a rule.

**Part IV: The Hidden World and the Future** opens by turning that machinery into a practical language for reading hidden systems: porewater profiles, transport, rate laws, and the conservation logic that lets us ask why a boundary sits where it does. It then moves into the deep biosphere, groundwater redox, water treatment, climate feedbacks, and the open questions that define the frontier of the field.

Throughout, *Sidebar* callouts offer the mathematical machinery for readers who want to see the derivations, check the units, and run their own back-of-the-envelope estimates. You can skip them without losing the narrative thread. Five appendices -- an energy toolkit, a model toolkit, a reaction gallery, quantum and energy derivations, and a field guide to the organisms -- hold the deeper technical scaffolding for readers who want the full apparatus.

This book is meant to be read straight through as narrative first. It can also be used as a technical companion, but the appendices and sidebars are there so the main text does not have to behave like a textbook every time it wants to be precise.

My hope is simple: that by the last page, you will look at the ground beneath your feet and see not dirt, but a reactor. Not silence, but metabolism. Not emptiness, but the invisible architects, still at work.


## Read online

Book website: https://pycckuu.github.io/the-book/

## Download

- Every merge to `main` publishes the site, bumps `book.version` in `_quarto.yml`, and creates a new GitHub Release with the latest **PDF/EPUB**.
- **PDF/EPUB** are available from the repository's **Releases**.
- The latest **PDF/EPUB** are also available as an artifact named `downloads` in the most recent GitHub Actions run.



## Modeling course

[The modeling course](courses/README.md) offers four modules with separate English and Russian files:

1. Oxygen diffusion and consumption: [English](courses/oxygen-diffusion/en/README.md), [Russian](courses/oxygen-diffusion/ru/README.md).
2. Advection, dispersion and parent loss: [English](courses/advection-dispersion/en/README.md), [Russian](courses/advection-dispersion/ru/README.md).
3. Saturation kinetics: [English](courses/saturation-kinetics/en/README.md), [Russian](courses/saturation-kinetics/ru/README.md).
4. Energy constraints: [English](courses/energy-constraints/en/README.md), [Russian](courses/energy-constraints/ru/README.md).

The separate [English modeling guide](courses/modeling-guide/modeling-guide-en.md) and [Russian modeling guide](courses/modeling-guide/modeling-guide-ru.md) walk through all four models with equations, worked calculations and saved-data graphs. Each module includes a verified model, supplied outputs for work without Python and separately titled public worked answers. Start with Chapter 8's observations, units and balances; the course home page explains the remaining prerequisites.

Both book builders include Chapters 1-10, the Epilogue, narrative Appendices A-E and all twelve course readings as Appendices F-Q. The [Russian book builder](translations/ru/README.md) produces one `the-invisible-architects-ru.pdf` and one `the-invisible-architects-ru.epub`, separate from English files. The combined Russian edition is undergoing integration review; dated partial review files remain archived. The modeling guide stays an optional companion. Learner-pilot protocols remain unexecuted; numerical verification does not establish learner outcomes or validity in a natural system.
