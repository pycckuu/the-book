# Oxygen diffusion and consumption: curriculum and prerequisite map

Revision O2-TEACHING-1.0.1-EN, bilingual module 1.0, 10 October 2026.

## Module purpose

Explain how a porewater oxygen profile can be produced by conservation, diffusive transport and oxygen consumption, then decide what the profile can and cannot establish about a real sediment. Audience: graduate students and advanced undergraduates in environmental science, geochemistry, biology and related natural sciences.

Students move through one process chain: observable profile -> assumptions -> conservation and rate law -> simulation -> comparison -> uncertainty and limits. The narrative chapter supplies the scientific question. The course packet and appendix hold the computation. There is no new competing chapter or solver.

## Prerequisite map

- Concentration units and sediment porosity -> distinguish porewater C from bulk phi C -> O2-E02.
- Difference quotients, derivative signs and area under a curve -> infer flux direction, curvature and integrated sink -> O2-E01, O2-E02, O2-E03.
- Conservation in a well-mixed box -> conservation in adjacent sediment slabs -> O2-E02.
- First-order rate law and a rate constant with inverse-time units -> explain what a phenomenological oxygen sink assumes -> O2-E02, O2-E04.
- Spreadsheet formulas or executing a documented Python script -> inspect the verified model's simulation and exported profiles -> O2-E03, O2-E04. Writing a PDE solver is not a prerequisite.
- Residuals and distinction between observation, illustration and simulation -> synthetic recovery vs independent validation -> O2-E05, O2-E06.
- Each preceding step -> a concise prediction for changed conditions -> O2-E07.

Entry diagnostic (ungraded, 10 minutes): convert 200 micromol/L to mol/m3; calculate a slope between two concentration/depth points; show arrows for oxygen entering a slab; distinguish porewater and bulk concentration at phi = 0.8. The numeric example is an entry diagnostic, not a proposed model parameter. Students missing two or more items receive a 20-minute units/gradient/conservation bridge before E02. Instructor checks the correction, rather than using prior course titles as evidence of readiness.

## Measurable outcomes and evidence

O2-LO1: identify axes, gradient direction and data provenance, and distinguish what is observed from what is inferred (E01, 10 points).

O2-LO2: derive the one-dimensional oxygen balance from a slab, define every term and unit, use a consistent reaction-volume basis, and state boundary conditions (E02, 15 points).

O2-LO3: reproduce the pinned model, compare numerical and analytic/reference results, and explain a flux budget and convergence test (E03, 20 points).

O2-LO4: predict and quantify effects of changing transport, reaction or surface supply, stating which assumptions remain fixed (E04, 15 points).

O2-LO5: compare a model to explicitly synthetic data, inspect residuals, identify which parameter combination is constrained, and propose an independent measurement (E05, 20 points).

O2-LO6: use one checked primary-paper result to test a model assumption, propose a discriminating observation, and distinguish verification, calibration and validation (E06, 15 points).

O2-LO7: transfer the balance to a changed oxygen-supply scenario and write a prediction with a limit and a proposed test (E07, 5 points).

Provisional mastery rule: at least 70/100, plus correct flux sign/reaction basis and no claim that schematic or synthetic data validate nature. A failing gate requires targeted revision even if the total passes. This is a planned teaching criterion, not an observed student outcome.

## Reading alignment

- Observation and motivation: chapter8 opening and "The porewater profile, explained". The archived upstream generator declares a schematic; the current chapter corrects the upstream opening. E01 uses the archived generator as an explicitly schematic case, without implying that the corrected chapter retains the measured-data error.
- Conservation: chapter8 "Conservation: the only law you need"; Appendix B "The diagenetic equation" (solute bulk concentration). E02.
- Diffusion and timescale: chapter8 "What moves: transport". E02 through E04.
- Reaction closure: chapter8 "What reacts: rate expressions"; Appendix B "Reaction rate expressions". The accepted q = kC oxygen sink is a deliberate aggregate-demand reduction, not the full dual-Monod mechanism and not uniquely organic-carbon respiration. E02, E04, E06.
- Data, portability and limits: chapter8 "One equation, all scales" and "What we sacrificed". E05 through E07.
- Coupled models: chapter8 "Coupling: one organism's waste is another's substrate", extension reading only. The oxygen-only pilot does not solve sulfate or methane.

## Teaching sequence

Prework: approximately 45 minutes including the diagnostic. Live module: 180 minutes including a 10-minute break. Follow-up: approximately 90 minutes. The prerequisite bridge, if needed, adds 20 minutes. The optional measured-summary extension within E06 adds approximately 20 to 30 minutes and is ungraded; it does not silently expand the core workload. All times are plans to measure in the learner pilot.

1. 0 to 20 minutes: read an oxygen profile and establish provenance (E01).
2. 20 to 50 minutes: draw a slab, choose assumptions, derive the balance (E02).
3. 50 to 95 minutes: reproduce and inspect the verified simulation; analytic and conservation checks (E03).
4. 95 to 105 minutes: break.
5. 105 to 130 minutes: predict before a parameter change, then compute and explain (E04).
6. 130 to 160 minutes: compare synthetic profiles and identify an inference limit (E05, remaining calculation as follow-up).
7. 160 to 180 minutes: critique a checked field study and write an exit prediction (E06 discussion, E07 independent exit response). E06 written report as follow-up.

Student packet contains prompts, reading links, approved model inputs, commands and submission instructions. Instructor packet contains expected results, derivations, tolerances, misconception prompts and 100-point rubric. Instructor results are never linked from student materials.

## Language and handoff

Exercise IDs O2-E01 to O2-E07 and outcome IDs O2-LO1 to O2-LO7 are invariant between English and Russian. Symbols, unit conversions, equation labels, numerical tolerances, data flags and CSV column names are aligned. Learner evidence must record packet revision and language. Equivalent learner performance remains an open pilot question.


## Numerical provenance and current state

Accepted scientific contract v1, approved by the editor. Baseline: phi = 0.8; C_0 = 0.2 mol/m3 porewater; D_s = 1e-9 m2/s; k = 1e-5 s^-1; L = 0.03 m. Fixed upper C, no-flux lower face, zero initial interior. Numerical model code, contract, results and source hashes are recorded in `provenance.json`.

The numerical results, sensitivity cases, fit residuals and balance were independently checked with the model and teaching checker. Student prompts and instructor keys are separate. Source hashes are recorded in `provenance.json`.

The curriculum draft 0.1 is superseded by this frozen teaching revision. The learner-pilot protocol is prepared, unexecuted, and records no actual attempts, feedback or learning gains. No recruitment or external action occurred.
