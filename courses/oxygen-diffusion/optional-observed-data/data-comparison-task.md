# Measured data comparison: student task

This exercise uses archived measured station summaries, not the synthetic fitting observations. It tests whether an observable and its provenance support a comparison before a parameter fit is attempted.

Sources: Beck and Maiti, *Sediment oxygen flux in the NGOM hypoxic zone*, Zenodo [v1, DOI 10.5281/zenodo.12536642](https://zenodo.org/records/12536642) and [v2, DOI 10.5281/zenodo.15367775](https://zenodo.org/records/15367775). CC BY 4.0. Article: [Beck and Maiti (2025), DOI 10.3389/fmars.2025.1532999](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2025.1532999/full).

Downloaded 2026-10-10. Files under `data/` are byte-preserved originals. The unprefixed spreadsheet is v1; `latest-Beck.Oxygen.Data.xlsx` is the pinned v2 record, not an automatically refreshed file. Metadata for each version is saved. Both spreadsheets contain one sheet, `Table`, with headers in row 1 and units in row 2. Rows 3 to 10 contain eight station-season summaries. They contain TOU, DOU and oxygen penetration depth, not raw depth-concentration profiles. Missing values are the text `n/d`.

1. From `optional-observed-data/`, run `python3 ../en/model/oxygen_model.py --out results`, then `python3 compare_measured.py`. Inspect `results/measured-version-comparison.csv`. Identify which record the article links and whether its file equals the latest record. Record the DOI and file hashes used in your answer.
2. For C6 in July 2019 (row 4), compare DOU, TOU and penetration depth between versions. Compute DOU/TOU from v2, explaining what each flux measures. Never treat missing DOU as zero.
3. Convert the illustrative model's analytic surface flux to mmol m⁻² d⁻¹. Compare it descriptively with v2 C6 DOU. Explain why a discrepancy does not by itself identify a faulty solver or provide a fitted value for k.
4. Compute the mean station DOU/TOU for the seven rows with paired fluxes, and the ratio of their summed DOU to summed TOU. Explain the distinction. Compare them with the article's reported mean ratio without altering the archived table to make it match. Inspect article Section 4.1 for the chamber water-respiration correction.
5. State why these summaries are insufficient to fit a depth profile or validate the first-order closure. Specify a minimum additional dataset and a genuinely independent validation design.

The article and archived versions do not agree in every aggregate or input description. Detecting this is an outcome of the exercise. The archive descriptions retain an older reciprocal ratio. Do not silently substitute that description for the spreadsheet calculation. The reported article D5 2019 profile has a disturbance caveat; the B5 2019 DOU/OPD are absent. Do not infer a faunal fraction as an exact 1 − DOU/TOU biological measurement.

Instructor answers are in a separate file. Do not distribute them with the student task.
