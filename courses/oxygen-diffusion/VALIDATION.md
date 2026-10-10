# Validation of module 1.0 repository copy

The accepted chapter, oxygen/energetic appendix changes and bibliography are integrated into the existing book. Repository presentation removes an unused footnote, replaces hard-coded chapter numbers with titles, reflows the inherited yield notes and instructor sensitivity tables, and clarifies companion-file references. Scientific source code, contracts, mathematical expressions, numerical reports, synthetic inputs and workbooks are unchanged. All exercise IDs and numerical conditions retain their reviewed meaning.

The model and teaching checker were run from the repository copy. Model verification JSON, profiles, synthetic fitting data and the teaching checker JSON/sensitivity/residual tables reproduced the archived outputs byte for byte. The optional archive comparator passed both workbook hash assertions and reproduced its values. Markdown relative links and cited chapter/toolkit bibliography keys resolve.

The prior bilingual review covers 358 aligned blocks in seven documents and 53 glossary terms. The schematic English/Russian PNGs were visually reviewed; generators differ only in approved labels. These checks establish source alignment and numerical correctness for the stated model. They do not establish field validity or learner efficacy. The learner pilot remains unexecuted.

## Local book builds

The full English book passed all existing configured formats with Quarto 1.10.19 and a private TinyTeX 2026.10 environment:

```sh
quarto render --to html
quarto render --to pdf
quarto render --to epub
```

Each command exited 0. The publication-style HTML payload with PDF/EPUB downloads has no missing internal file or anchor targets. All book EPUB links and archive CRC checks passed. The PDF has 260 pages. Changed chapter equations, figures, citations and toolkit content were inspected visually; this is a targeted inspection, not every-page typography certification.

The initial PDF attempt failed because the existing BasicTeX installation lacked `tcolorbox.sty`; the pristine base failed identically. The private TinyTeX build passed without changes to the system TeX installation or CI infrastructure. Existing source chapter numbering did not match rendered numbering, so the affected toolkit references now use chapter titles. The inherited yield table and new instructor E04 tables were reflowed after visual inspection found clipping/overlap. Their equations, citations and exact answer cells are preserved.

## Bilingual course reading outputs

Private review overlays rendered the English and Russian student/instructor readings separately in HTML, PDF and EPUB. All 12 commands exited 0. Their internal references resolve; all seven exercise IDs are present. Student outputs contain no instructor solutions, completed sensitivity/residual tables, checker or pilot protocol. The main book explicitly excludes `courses/**` from copied resources. Repository visibility itself is not access control.

Course PDFs/EPUBs are reading outputs. E03/E05 require the companion `model/` and `data/` assets, or their documented no-Python route. Optional measured-data handouts and provenance files are identified as companion files rather than dead EPUB links. Supply the learner assets listed in each language README separately from instructor material.

The existing book configuration is English only. A full Russian book build is not configured; the Russian course overlays do not establish one. HTML references and stored math were checked, and changed HTML was sampled visually. EPUB XHTML/MathML and links were checked, but visual behavior in a physical e-reader was not tested.

Independent scientific, teaching and Russian reviews were reconciled with the repository copy. Subsequent presentation-only deltas preserve reviewed mathematical fragments, citation keys, model/data hashes and exact instructor table cells; affected reading outputs were rebuilt and inspected.

## Hosted CI and release boundary

No workflow runs on pull-request events. Existing publication workflows run on main or manual dispatch and can deploy the site, so they were not dispatched for validation. Local builds are passing; no GitHub CI result or deployed behavior is claimed. This pull request neither merges main nor publishes the book.
