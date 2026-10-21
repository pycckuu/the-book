"""Build the complete modeling volume from existing readings, without executing models."""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess


def prepare(repo, stage, lang):
    """Stage one language's guide and four modules with their original relative paths."""
    for name in ['courses', 'sources/img', 'filters']:
        shutil.copytree(repo / name, stage / name,
                        ignore=shutil.ignore_patterns('__pycache__', '.quarto', '_book'))
    for name in ['sources/bibliograph.bib', 'translations/ru/chapter-callouts.lua']:
        target = stage / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(repo / name, target)
    guide = f'courses/modeling-guide/modeling-guide-{lang}.md'
    oxygen = f'courses/oxygen-diffusion/{lang}'
    observed = 'courses/oxygen-diffusion/optional-observed-data'
    # Keep the accepted Russian companion's prerequisite readings; use the main English sources.
    if lang == 'ru':
        prerequisites = [f'{oxygen}/chapters/08-the-equation.ru.md',
                         f'{oxygen}/appendices/b-model-toolkit.ru.md']
    else:
        prerequisites = ['chapters/08-the-equation.md', 'appendices/b-model-toolkit.md']
        for name in prerequisites:
            (stage / name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(repo / name, stage / name)
    sections = [
        ('Oxygen diffusion and consumption' if lang == 'en' else 'Диффузия и потребление кислорода',
         prerequisites + [f'{oxygen}/{p}' for p in [f'student-packet-{lang}.md',
             f'instructor-packet-{lang}.md', f'curriculum-{lang}.md', 'verification-methods.md',
             f'pilot-protocol-{lang}.md']] + [f'{observed}/{p}' for p in
             (['data-comparison-task.md', 'data-comparison-solutions.md'] if lang == 'en' else
              ['data-comparison-task-ru.md', 'data-comparison-solutions-ru.md'])]),
        ('Advection, dispersion and parent loss' if lang == 'en' else 'Адвекция, дисперсия и потери',
         [f'courses/advection-dispersion/{lang}/{p}' for p in [f'module-reading-{lang}.qmd',
          f'student-packet-{lang}.qmd', f'worked-answers-{lang}.qmd', f'curriculum-{lang}.md',
          f'pilot-protocol-{lang}.md']]),
        ('Saturation kinetics' if lang == 'en' else 'Кинетика насыщения',
         [f'courses/saturation-kinetics/{lang}/{p}' for p in ['scientific-reading.md',
          'student-packet.md', 'OPEN-worked-answers.md', 'curriculum.md', 'pilot-protocol.md']]),
        ('Energy constraints' if lang == 'en' else 'Энергетические ограничения',
         [f'courses/energy-constraints/{lang}/{p}' for p in ['scientific-reading.md',
          'student-packet.md', 'OPEN-worked-answers.md', 'curriculum.md', 'pilot-protocol.md']])]
    readings = [guide] + [p for _, paths in sections for p in paths]
    seen_ids = set()
    for index, name in enumerate(readings):
        path = stage / name
        text = path.read_text(encoding='utf-8')  # A missing reading must fail the whole volume.
        # Move each document title into the book heading hierarchy, preserving its body.
        title = re.search(r'^title: ["\']?(.+?)["\']?$', text, re.MULTILINE)
        if title:
            body = re.sub(r'\A---\n.*?\n---\n\s*', '', text, count=1, flags=re.DOTALL)
            if not re.match(r'# ', body):
                body = '# ' + title[1] + '\n\n' + body
            text = body
        # Each source retains its own note definitions when combined with overlapping readings.
        text = re.sub(r'\[\^([^\]]+)\]', lambda m: f'[^volume-{index}-{m[1]}]', text)
        for anchor in re.findall(r'\{#([\w-]+)', text):
            if anchor in seen_ids:
                renamed = f'volume-{index}-{anchor}'
                text = re.sub(r'(?<=\{#)' + re.escape(anchor) + r'(?=[}\s])', renamed, text)
                text = text.replace('](#' + anchor + ')', '](#' + renamed + ')')
            else:
                seen_ids.add(anchor)
        path.write_text(text, encoding='utf-8')
    title = 'Modeling' if lang == 'en' else 'Моделирование'
    intro = (
        'Read the optional guide, then oxygen, advection-dispersion, saturation and energy. '
        'Chapter 8 and Appendix B are reproduced for reference. Return to Chapter 1 and Appendix A '
        'in the [Book](https://pycckuu.github.io/the-book/the-invisible-architects.pdf) for energy foundations. '
        'Attempt exercises before consulting open answers and record help used. The measured-data comparison '
        'is optional. Data, code and worksheets retain their named resource paths. '
        'Learner pilots are unexecuted; durations are planned, not measured.' if lang == 'en' else
        'Начните с необязательного руководства, затем проходите модули по порядку: кислород, '
        'адвекция и дисперсия, насыщение, энергия. Глава 8 и приложение B повторены для справки. '
        'Основы энергетики изложены в главе 1 и приложении A '
        '[книги](https://pycckuu.github.io/the-book/the-invisible-architects-ru.pdf). '
        'Сначала сохраните собственную попытку, затем сравните её с открытыми решениями '
        'и запишите использованную помощь. Сравнение с измерениями необязательно. '
        'Данные, программы и рабочие листы сохраняют свои пути в комплекте ресурсов. '
        'Учебные пилоты пока не проведены; длительность занятий является плановой.')
    (stage / 'index.md').write_text(f'# {title} {{.unnumbered}}\n\n{intro}\n', encoding='utf-8')
    config = {
        'project': {'type': 'book', 'output-dir': '_book', 'resources': ['courses']},
        'book': {'title': title, 'author': 'Igor Markelov', 'output-file': f'modeling-{lang}',
                 'chapters': ['index.md', guide] + [dict(part=t, chapters=p) for t, p in sections]},
        'execute': {'enabled': False},
        'filters': ['translations/ru/chapter-callouts.lua', 'filters/companion-links.lua',
                    'filters/modeling-layout.lua', 'filters/delayed-footnotes.lua'],
        'bibliography': 'sources/bibliograph.bib', 'suppress-bibliography': True,
        'lang': lang, 'format': {'html': {'toc': True}, 'epub': {'toc': True},
        'pdf': {'documentclass': 'scrbook', 'pdf-engine': 'xelatex', 'mainfont': 'PT Serif',
                'sansfont': 'PT Sans', 'toc': True, 'toc-depth': 2,
                'include-in-header': {'text': r'\sloppy\interfootnotelinepenalty=10000\def\UrlBreaks{\do\/\do\-\do\_\do\.}'
                    + '\n' + r'\renewcommand{\chaptermark}[1]{\markboth{' + title + '}{' + title
                    + r'}}\renewcommand{\sectionmark}[1]{}'}}}}
    (stage / '_quarto.yml').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
    return readings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lang', choices=['en', 'ru'], required=True)
    parser.add_argument('--to', choices=['html', 'pdf', 'epub', 'all'], default='all')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--quarto', default='quarto')
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    output = args.output.resolve()
    if output.is_relative_to(repo):
        parser.error('Choose a new output directory outside the source repository.')
    output.mkdir(parents=True, exist_ok=False)
    stage = output / 'project'
    prepare(repo, stage, args.lang)
    for fmt in ['html', 'pdf', 'epub'] if args.to == 'all' else [args.to]:
        command = [args.quarto, 'render', '--to', fmt]
        if fmt == 'pdf':
            command += ['-M', 'latex-auto-install:false']
        log_path = output / f'{fmt}.log'
        try:
            with log_path.open('w') as log:
                subprocess.run(command, cwd=stage, stdout=log, stderr=subprocess.STDOUT, check=True)
        except subprocess.CalledProcessError:
            print(log_path.read_text(encoding='utf-8', errors='replace')[-16000:], flush=True)
            raise
        shutil.copytree(stage / '_book', output / fmt)
        print(f'{args.lang} modeling {fmt}: built', flush=True)


if __name__ == '__main__':
    main()
