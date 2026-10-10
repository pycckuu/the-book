"""Render the partial Russian Chapter 1 edition outside the source repository."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--to', choices=['html', 'pdf', 'epub', 'all'], default='all')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--quarto', default='quarto')
    args = parser.parse_args()
    russian = Path(__file__).resolve().parent
    repo = russian.parents[1]
    output = args.output.resolve()
    if output.is_relative_to(repo):
        parser.error('Choose an output directory outside the source repository.')
    output.mkdir(parents=True, exist_ok=False)
    stage = output / 'project'
    chapter = 'translations/ru/chapters/01-budget-of-the-universe.md'
    files = [chapter, 'sources/bibliograph.bib',
             'appendices/d-math-without-pain.md',
             'filters/companion-links.lua', 'translations/ru/chapter-callouts.lua']
    for name in files:
        target = stage / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(repo / name, target)
    (stage / 'index.md').write_text(
        '# Частичная русская редакция {.unnumbered}\n\n'
        'Здесь представлена глава «Бюджет Вселенной». Остальные главы книги '
        'пока доступны на английском.\n', encoding='utf-8')
    config = {
        'project': {'type': 'book', 'output-dir': '_book', 'resources': [
            'appendices/d-math-without-pain.md']},
        'book': {'title': 'Невидимые архитекторы: Бюджет Вселенной',
                 'author': 'Igor Markelov', 'output-file': 'the-invisible-architects-chapter01-ru',
                 'chapters': ['index.md', chapter]},
        'filters': ['filters/companion-links.lua', 'translations/ru/chapter-callouts.lua'],
        'bibliography': 'sources/bibliograph.bib', 'suppress-bibliography': True,
        'lang': 'ru', 'format': {
            'html': {'toc': True}, 'epub': {'toc': True},
            'pdf': {'documentclass': 'scrbook', 'pdf-engine': 'xelatex',
                    'mainfont': 'PT Serif', 'sansfont': 'PT Sans', 'toc': True}}}
    (stage / '_quarto.yml').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
    (output / 'inputs.json').write_text(json.dumps({
        str(p.relative_to(stage)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(stage.rglob('*')) if p.is_file()}, indent=2) + '\n')
    for fmt in (['html', 'pdf', 'epub'] if args.to == 'all' else [args.to]):
        command = [args.quarto, 'render', '--to', fmt]
        if fmt == 'pdf':
            command += ['-M', 'pdf-auto-install:false']
        with (output / f'{fmt}.log').open('w') as log:
            subprocess.run(command, cwd=stage, stdout=log, stderr=subprocess.STDOUT, check=True)
        shutil.copytree(stage / '_book', output / fmt)
        print(f'ru chapter01 {fmt}: complete', flush=True)


if __name__ == '__main__':
    main()
