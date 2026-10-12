"""Render one language module in a new directory, without running the model."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lang', choices=['en', 'ru'], required=True)
    parser.add_argument('--to', choices=['html', 'pdf', 'epub', 'all'], default='all')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--quarto', default='quarto')
    args = parser.parse_args()
    module = Path(__file__).resolve().parent
    repo = module.parents[1]
    output = args.output.resolve()
    if output.is_relative_to(repo):
        parser.error('Choose an output directory outside the source repository.')
    output.mkdir(parents=True, exist_ok=False)
    stage = output / 'project'
    relative = Path('courses/oxygen-diffusion')
    shutil.copytree(module, stage / relative)
    for name in ['sources/bibliograph.bib', 'filters/companion-links.lua']:
        target = stage / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(repo / name, target)
    lang = args.lang
    readings = [f'student-packet-{lang}.md', f'instructor-packet-{lang}.md',
                f'curriculum-{lang}.md', 'verification-methods.md',
                f'pilot-protocol-{lang}.md']
    if lang == 'ru':
        readings = ['chapters/08-the-equation.ru.md',
                    'appendices/b-model-toolkit.ru.md'] + readings
    chapters = [str(relative / lang / p) for p in readings]
    if lang == 'ru':
        chapters += [str(relative / 'optional-observed-data' / p) for p in
                     ['data-comparison-task-ru.md', 'data-comparison-solutions-ru.md']]
    title = ('Oxygen diffusion and consumption: course companion' if lang == 'en'
             else 'Диффузия и потребление кислорода: учебные материалы')
    intro = ('Attempt the exercises before consulting the open worked answers. '
             'Use the supplied model/data companions and prerequisite book readings. '
             'All cases are illustrative or synthetic. The learner pilot is unexecuted.'
             if lang == 'en' else
             'Попробуйте выполнить задания до чтения открытых решений. Используйте '
             'сопутствующие модель и данные. Предварительное чтение включено в этот пакет. '
             'Все случаи условные или синтетические. Учебный пилот не выполнен.')
    (stage / 'index.md').write_text('---\ntitle: "' +
                                  ('Module overview' if lang == 'en' else 'Обзор модуля') +
                                  '"\n---\n\n' + intro + '\n', encoding='utf-8')
    config = {
        'project': {'type': 'book', 'output-dir': '_book', 'resources': [
            str(relative / lang / 'model'), str(relative / lang / 'data'),
            str(relative / lang / 'evidence')] +
            ([str(relative / p) for p in ['ru/sources', 'glossary.ru.md',
              'optional-observed-data/data', 'optional-observed-data/results',
              'optional-observed-data/compare_measured.py']] if lang == 'ru' else [])},
        'book': {'title': title, 'author': 'Igor Markelov',
                 'output-file': f'oxygen-diffusion-module-{lang}',
                 'chapters': ['index.md'] + chapters},
        'filters': ['filters/companion-links.lua'],
        'bibliography': 'sources/bibliograph.bib', 'suppress-bibliography': True,
        'lang': lang, 'format': {
            'html': {'toc': True}, 'epub': {'toc': True},
            'pdf': {'documentclass': 'scrbook', 'pdf-engine': 'xelatex',
                    'mainfont': 'PT Serif', 'sansfont': 'PT Sans', 'toc': True}}}
    (stage / '_quarto.yml').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    (output / 'inputs.json').write_text(json.dumps({str(p.relative_to(stage)): sha(p)
        for p in sorted(stage.rglob('*')) if p.is_file()}, indent=2) + '\n')
    for fmt in (['html', 'pdf', 'epub'] if args.to == 'all' else [args.to]):
        command = [args.quarto, 'render', '--to', fmt]
        if fmt == 'pdf':
            command += ['-M', 'pdf-auto-install:false']
        with (output / f'{fmt}.log').open('w') as log:
            subprocess.run(command, cwd=stage, stdout=log, stderr=subprocess.STDOUT, check=True)
        shutil.copytree(stage / '_book', output / fmt)
        print(f'{lang} {fmt}: complete', flush=True)


if __name__ == '__main__':
    main()
