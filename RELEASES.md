# Two-volume releases

Each release contains two volumes per language, each in PDF and EPUB:

| Volume | English basename | Russian basename | Contents |
| --- | --- | --- | --- |
| Book | `the-invisible-architects` | `the-invisible-architects-ru` | Chapters 1-10, Epilogue, Appendices A-E |
| Modeling | `modeling-en` | `modeling-ru` | Guide, four complete modules, exercises, public answers, curricula, unexecuted pilot protocols |

This is eight document files, plus `translation-assets.json` with language, volume and SHA256 for every file. Individual module and guide helpers remain available for local work; CI does not add their separate downloads to new releases. Source, data and worksheet paths remain in the repository and staged resource trees. PDF/EPUB text names those companion resources; download the repository source archive to use them offline.

## Build

The normal root Quarto project builds the English Book and site:

```sh
quarto render
python3 scripts/build-release-translations.py --output _book
```

The release helper expects the English Book PDF and EPUB already in the output folder. It adds the Russian Book and both Modeling volumes, and rejects missing or unexpected PDF/EPUB assets. Every volume is rendered from the selected checkout, with native Quarto contents, page numbers, links and EPUB navigation. No PDF concatenation or numerical model execution is involved.

For one volume:

```sh
python3 translations/ru/build-chapters.py --output /tmp/book-ru
python3 scripts/build-modeling.py --lang en --output /tmp/modeling-en
python3 scripts/build-modeling.py --lang ru --output /tmp/modeling-ru
python3 scripts/test_release_translations.py
```

Use `--to pdf` or `--to epub` to render one format. Choose new output directories outside the repository. Quarto, XeLaTeX, PT Serif/PT Sans and `hyphen-russian` are required; workflows install them and rebuild the XeLaTeX format.

## CI and publication

Pull requests build the site and all eight document files without deploying or creating a release. A merge to main uses the same build, then deploys Pages and publishes the versioned release. The `downloads` artifact contains the same eight files and checksum manifest.

The manual rebuild workflow uses sources and build helpers from the selected tag. Older tags without the two-volume helper fail explicitly instead of mixing new sources into a historical release. Existing releases are not rewritten automatically.

The main workflow tags the version before rendering. A tag alone does not prove successful publication: inspect the build, deployment and release results. Source or packaging acceptance does not establish learner performance, field validity or completion of the unexecuted pilot protocols.
