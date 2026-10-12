# Process modeling guide

Read the language files separately: [English](modeling-guide-en.md) and [Russian](modeling-guide-ru.md). Each explains four examples, from system boundaries and units to independent references, actual numerical checks and inference limits. Five figures in each language use saved illustrative model outputs.

Calculated display values use three significant figures. Input settings, equations, thresholds and raw saved tables keep their precision. Chemical formula letters are upright, atom counts are subscripts and charges are superscripts. Artificial A/B are declared equivalents. The guide does not change any solver, model case, exercise workload or default.

## Build either language

Use Python 3 and Quarto, with XeLaTeX, PT Serif and PT Sans for PDF. Russian PDF needs the `hyphen-russian` and `ruhyphen` TeX packages. A missing font or language pattern is a build setup issue, not permission to substitute unreadable glyphs.

From the repository root:

```sh
python3 courses/modeling-guide/build.py --lang en --output /tmp/model-guide-en
python3 courses/modeling-guide/build.py --lang ru --output /tmp/model-guide-ru
```

Choose new output directories. Use `--to html` for standalone HTML with embedded figures and native MathML, or `--to pdf` for PDF. The helper explicitly supplies `guide-format.json`; it does not run a numerical model. The guides link exact companion revisions for the reproducible model commands and the no-Python saved-data route.

## Evidence scope

`figure-sources.json` identifies the exact source tables or archive members, hashes, support and units used for the saved-data figures. Oxygen and advection data are unchanged published inputs; saturation and energy companions are separate reviewed open changes. Their inclusion here does not merge those revisions or publish a new whole-book edition. The configured book chapter list is unchanged.

All cases are illustrative or synthetic. Numerical verification does not establish field validity, biological mechanism or learner performance.
