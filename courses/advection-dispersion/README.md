# Advection, dispersion and parent loss

This module follows the oxygen module with a moving pulse in a finite saturated column. It distinguishes porewater velocity from Darcy flux, physical dispersion from numerical spreading, and aggregate parent disappearance from retained storage or exported mass.

- [English exercises, open answers and teaching materials](en/README.md)
- [Russian reading, exercises and open answers](ru/README.md)
- [Shared model and supplied outputs](model/README.md)
- [Finite-column contract](model/contract-and-evidence/model-contract.md)

The default English book includes the exercises followed by their worked answers. Both are openly available. Both language source packages are integrated locally. Both language modules pass bounded HTML/PDF/EPUB build and portability checks. The final independent review is pending. Book readings must accompany the course assets.

Six exercises total 100 points and 270 planned minutes, with an optional 20-minute prerequisite bridge. The learner protocol is planned and unexecuted. All numerical observations are synthetic; no field validity or learning gain is claimed.

## Render the language modules locally

From the repository root, use Quarto with XeLaTeX and PT Serif/PT Sans installed:

```sh
python3 courses/advection-dispersion/build.py --lang en --output /tmp/advection-en
python3 courses/advection-dispersion/build.py --lang ru --output /tmp/advection-ru
```

Choose new output directories outside this repository. `--to html`, `--to pdf` or `--to epub` renders one format; `--quarto /path/to/quarto` selects a local installation. The script copies the source into an isolated project, renders readings and copies companion files. It never runs the numerical model. In HTML, companion links remain clickable. PDF and EPUB name the supplied companion files; use the source bundle for calculations. The prerequisite book readings remain part of the course.

See [validation scope](VALIDATION.md). Source and build acceptance do not establish field validity, learner outcomes or publication authority.
