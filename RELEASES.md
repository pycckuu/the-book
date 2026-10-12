# Release downloads

Every new release includes separate English and Russian files. The English book
remains the main PDF and EPUB. The unified Russian builder prepares one `the-invisible-architects-ru.pdf` and
one `the-invisible-architects-ru.epub`, containing Chapters 1-10, the Epilogue
and Appendices A-Q. F-Q mirror the twelve configured English course readings.
The combined edition is under integration review; dated partial reading editions remain archived.
Chapter 5 uses a separate Russian figure with its two textual labels translated
and its chemical formulas and electron counts preserved. Chapter 6 uses a separate Russian figure with
all 17 in-image labels and its caption translated.
Chapter 7 uses a separate Russian figure: all 11 textual labels are translated
and the three Latin scientific names are preserved.
Chapter 8 uses a separate Russian schematic: eight textual objects are translated;
three chemical formulas and seven numeric depth ticks are preserved. Its scenario
CSV and the additional Appendix B CSV/JSON/readback files are included as resources.
Chapter 9 uses a separate qualitative Russian schematic: eight word labels are translated
and six chemical acceptor labels are preserved; zone thicknesses are illustrative.
Chapter 10 uses a separate idealized Russian aquifer schematic: twelve word objects
are translated and six chemical labels are preserved; manganese reduction is omitted,
sulfate reduction and methanogenesis are combined, and zone shapes and sizes are illustrative.
Russian Appendix B is included; Chapter 8 links to its Russian text. HTML resource links resolve within the extracted download bundle; PDF and EPUB name the companion files.
The Russian epilogue follows the accepted English source at `a1418c199e389ef4c6f37b36cd7aff19bce9f7d2`; it has no figure and is unnumbered. The inherited Chapter 9 Blanch note metadata is corrected in both languages at the same revision. Russian Appendix C follows the accepted English source at `ed41f4ddd6dee6613a21d0e72753a5fe7d476e9e`; it has 19 reaction equations, one summary table and no figure. Its plain-text reference to Appendix E is retained. Russian Appendix E follows the accepted English source at `4c0c04b016c7717b496979e1e43b14ae5e2229e4`; it contains ten organism entries and no figure. The builder now includes the five narrative appendices and twelve existing Russian course readings. The modeling guide remains an optional companion. Complete-edition acceptance is pending; no release is authorized by this local integration.

`scripts/build-release-translations.py` calls the existing Russian book helper
and every `courses/*/build.py` helper. It adds Russian book PDF/EPUB,
separate English/Russian module PDF/EPUB, and separate English/Russian modeling
guide PDFs when those course sources are present. It never executes a model.
`translation-assets.json` lists the added files, languages, scope and checksums.

Both publication workflows use this step before uploading release assets. A
missing Russian book helper, failed translation render or missing output fails
the build. Russian content (including `ru/`, `*-ru.*` and `*.ru.md`) without a helper
fails before rendering. Every discovered
course helper must successfully build both languages. The oxygen companion
includes the existing student packet, OPEN instructor answers, curriculum,
verification methods and unexecuted pilot in each language. The Russian companion
also includes the existing Russian Chapter 8, Toolkit appendix and schematic
assets, as separate module readings. The unified Russian book contains Chapters 1 through 10 and course Appendices F-Q;
the companion retains its existing, separately scoped readings. It ends
with the optional observed-data task and its OPEN answers, and includes their
unchanged data, saved comparison results and comparison script as resources.
The Russian glossary is also supplied as a resource. The
English companion retains the main English book as its prerequisite reading.
The modeling guide uses root-level EN/RU sources and is discovered by its helper. Russian PDFs
require PT Serif/PT Sans and `hyphen-russian`, installed by the workflows.

For local preparation, with Quarto and the typography prerequisites installed:

```sh
python3 scripts/build-release-translations.py --output /tmp/book-release-downloads
python3 scripts/test_release_translations.py
```

The manual backfill workflow uses current release tooling but only sources from
the selected tag. A tag without Russian sources cannot be rebuilt as bilingual;
it fails instead of mixing a newer translation with an older English edition.

The release change depends on the accepted Russian translation sources and their
helpers being integrated first. Building or preparing downloads does not publish
them. Main merges, workflow dispatch and releases need separate authorization.

The existing main workflow pushes the version tag before rendering. If a render
fails, the tag can exist without a release or Pages deployment. After repairing
the sources and checking tag applicability, rebuild that tag using the manual
backfill workflow rather than inventing another version. Dispatch still requires
explicit publication authorization.
