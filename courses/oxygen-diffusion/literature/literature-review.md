# Literature discovery and evidence appraisal

Search date and cutoff: 2026-10-10. This is a focused discovery update for chapter claims and pilot mechanisms, not a systematic review or exhaustive claim of the latest paper.

## Baseline read before discovery

Read book-bible.md, CITATIONS.md, README.md, Chapter 8, Appendix B, the bibliography, and the actual Chapter 8 generator `sources/figures/fig_ch8_porewater_profile.py`. The initially requested `scripts/gen_ch4_figure.py` was also inspected but generates a different figure. Baseline bibliography includes Rabouille1991, Berner1980Early, Boudreau1997Diagenetic, LiGregory1974, Jin2005, Thullner2007, VanCappellen1996, Dale2008 and Stolpovsky2011. Existing bibliography entries establish editorial context; their contents are not all newly full-text verified. Stored local Mendeley paths do not establish accessible full text.

No new matching keys for the proposed Burdorf2024, Daviray2024, BeckMaiti2025, Auer2025 or Jin2003 were found in the baseline. `literature-additions.bib` records the additions integrated into the source bibliography.

## Coverage

Web discovery covered: oxygen microprofiles and first-order consumption; recent sediment oxygen diffusion; oxygen sink attribution by cable bacteria and fauna; porewater-vs-bulk rate conventions; permeable beach transport; public oxygen datasets; thermodynamic net-rate formulation. Exact queries are preserved in `search-log.json`. Main recent-discovery horizon was 2023 to the cutoff, with foundational searches for the equation and equilibrium correction. Searches returned records outside that range; those were screened rather than treated as recent evidence.

Primary sources used are in `source-to-claim.csv`. Five full-text primary papers were inspected at equation/method/result/discussion level. Auer's publisher HTML was available even though its AWI PDF was access-denied. Burdorf's publisher page was 403 on direct fetch, so its full open-access repository PDF was read. ASM full HTML was available after a PMC access-check failure. Daviray and Beck/Maiti publisher HTML were accessible. No paywall purchase, account registration, author contact or credentials were needed.

Two Zenodo versions were downloaded and compared. Daviray's raw plotted data require a request; no request was sent. Auer's PANGAEA dataset was identified but not downloaded. A 2026 USGS Samoa oxygen dataset was discovered, but detailed metadata/direct page retrieval failed through the browser tool and the dataset was not imported. It is a candidate for later data work, not evidence used here. A photogranule article with a November 2026 issue date was excluded as beyond the search cutoff and outside the sediment pilot. General reviews and search-engine summaries were discovery aids; they were not used as new primary validation.

## Scientific decisions

Keep the analytically checkable first-order baseline. The new papers inform scope and caveats, not parameter values. No paper is used to claim that Dₛ = 10⁻⁹ m² s⁻¹ or k = 10⁻⁵ s⁻¹ was measured for this pilot.

The strongest correction is observational attribution: a measured O₂ curve constrains net oxygen transport and demand under a stated model, rather than a unique metabolism. S01 and S02 provide independent cable-bacteria evidence; S03 independently exposes DOU-versus-TOU limitations. S04 is an adverse transfer example for a diffusion-only mud closure. Apparent conflicts between a simple oxygen-depletion story and those studies reflect different mechanisms and transport settings, not a contradiction of mass conservation.

S01's attribution percentage depends on the authors' assumption about the extra uptake during incubation. S02 has limited station/core replication. S03 interprets a flux gap and uses a historical chamber correction. These qualifications must accompany causal teaching claims. Do not teach specific sink fractions as general sediment facts.

S05 supplies an actual net thermodynamic-rate formulation to replace the logistic attribution. The logistic's failure at equilibrium is also directly demonstrable mathematically. This packet excludes all thermodynamic gating from the oxygen baseline; broader coupled energetics require an explicit reaction and energy convention.

## Exact figure finding

The generator docstring calls the curves schematic and states that there are no measured data. Lines defining the profiles use exp(−z/1.4), a sulfate logistic with scale 0.92, and a methane logistic with scale 0.95. The axes use relative concentration. The crossing is computed numerically from arbitrarily scaled curves. The oxygen tail is masked below 0.01; an oxic-band threshold uses 0.02. Neither is a measured detection limit. The sampled oxygen-band boundary is 5.60935 cm and the sampled plotted crossing is 79.73289 cm for these choices (the underlying oxygen threshold is 5.47683 cm).

Consequences: replace the opening's measured-site language with an explicit thought experiment; label caption relative and schematic; describe the drawn crossing as an illustration rather than a measured SMT depth. Changing individual curve scales moves the crossing without changing any underlying measured chemistry, because none is supplied. A crossing of separately normalized curves cannot locate an SMT or establish concentrations, zone width, reaction rate or AOM attribution. The pilot code does not generate sulfate or methane and must not be claimed as the source of that figure.

The resulting corrections are integrated in Chapter 8 and the oxygen/energetic sections of Appendix B.

## Open scientific issues outside the pilot edits

Appendix B's standalone yield R² = 0.9 entries omit dataset/conditions and should not be taught as universal predictive performance. Its empirical yield expression needs an energy and yield unit/basis check before use. The nested mineral-rate powers can become non-real for precipitation unless signed branches or exponent restrictions are specified. Darcy permeability k shares a symbol with the pilot consumption coefficient; the module explicitly defines its local notation. These broader toolkit issues are flagged for later scope, not silently fixed or validated by the oxygen packet.
