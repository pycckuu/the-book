# Citations (GitHub-first, Quarto-friendly)

This repo is written to be readable as plain Markdown on GitHub *and* to render cleanly via Quarto (PDF/EPUB/HTML).

Quarto/Pandoc citations (`@Key`) are great for rendered output, but they look noisy in raw GitHub Markdown. The convention below keeps the main text readable while still preserving a real bibliography for Quarto.

## Default rule: cite in footnotes

In the main text, use a Markdown footnote marker:

- `… as Schrödinger asked.[^schrodinger1944]`

Then put the human-readable citation in the footnote definition, and include the Pandoc citation key inside the footnote so Quarto can build the bibliography:

- `[^schrodinger1944]: Erwin Schrödinger, *What Is Life?* (Cambridge University Press, 1944). [@Schrodinger1944]`

On GitHub, this reads like an ordinary footnote. In Quarto output, it also connects to the bibliography entry.

## Keep citations light in the narrative
- Prefer **one citation per claim cluster** (cite once at the end of a paragraph/section rather than after every sentence).
- Put citation density in:
  - short “Further reading” lists, or
  - appendices/notes sections, or
  - Equation Corner callouts (when a specific equation/history needs attribution).

## BibTeX source of truth
- All references live in `sources/bibliograph.bib`.
- Add a BibTeX entry first, then cite it via `[@Key]` inside a footnote.

## Citation keys
Prefer short, stable keys:
- Books: `AuthorYear` (e.g. `Schrodinger1944`)
- Articles: `AuthorYear` or `AuthorYYYYa` when needed

