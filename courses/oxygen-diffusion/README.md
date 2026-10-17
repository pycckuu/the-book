# Oxygen diffusion and consumption: bilingual module 1.0

This module connects Chapter 8's story about porewater profiles to a verifiable one-dimensional oxygen model, seven exercises and separately titled open worked answers. It uses constant water-filled porosity, tortuosity-corrected diffusivity and aggregate first-order oxygen consumption. A normalized steady profile constrains alpha = k/D_s; the oxygen sink does not uniquely identify a metabolism.

- [English exercises and open answers](en/README.md)
- [Russian exercises and open answers](ru/README.md)
- [Bilingual glossary](glossary-bilingual.tsv)
- [Literature appraisal](literature/literature-review.md) and [source-to-claim ledger](literature/source-to-claim.csv)
- [Optional measured-summary version exercise](optional-observed-data/data-comparison-task.md), with [open worked answers](optional-observed-data/data-comparison-solutions.md)

From `en/`, run `python3 model/oxygen_model.py --out my-run`. For instructor checks, run `python3 check_teaching.py`. For the optional version audit, follow the [fresh working-copy instructions](optional-observed-data/data-comparison-task.md) to preserve the archived results. All numerical scripts use Python 3.9+ and the standard library. Figure regeneration separately requires matplotlib and numpy. These verification commands require normal Python without `-O`/`-OO` and with `PYTHONOPTIMIZE` unset; archived evidence remains historical.

The prescribed inputs and fitting observations are synthetic. Numerical verification establishes correctness for the stated equation, not field validity. The learner protocol is prepared and has not been executed. The science review of Appendix B covers the oxygen/energetic changes, not every inherited equation.

The optional workbooks are CC BY 4.0 data by Beck and Maiti, pinned to Zenodo versions 12536642 and 15367775 with original bytes and attribution. They contain station summaries, not raw depth profiles. The published mean DOU/TOU of 0.33 +/- 0.07 is not reconciled to the archive's changed cells and older metadata ratio; neither version is assumed correct merely because it is newer.

The book's default English render includes the exercises, worked answers, and optional measured-data task and answers as appendices. Answers and numerical keys are intentionally public. Russian course materials are provided as a separate source-aligned reading path. No learner efficacy or empirical validation is claimed.
