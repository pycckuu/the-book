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
    relative = Path('courses/advection-dispersion')
    shutil.copytree(module, stage / relative)
    for name in ['sources/bibliograph.bib', 'filters/companion-links.lua']:
        target = stage / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(repo / name, target)
    lang = args.lang
    readings = [f'module-reading-{lang}.qmd', f'student-packet-{lang}.qmd',
                f'worked-answers-{lang}.qmd', f'curriculum-{lang}.md',
                f'pilot-protocol-{lang}.md']
    title = ('Advection, dispersion and parent loss' if lang == 'en'
             else 'Адвекция, дисперсия и потеря исходного вещества')
    intro = ('Attempt the exercises before consulting the open worked answers. '
             'Use the supplied model/data companions and prerequisite book readings. '
             'All cases are illustrative or synthetic. The learner pilot is unexecuted.'
             if lang == 'en' else
             'Попробуйте выполнить задания до чтения открытых решений. Используйте '
             'сопутствующие модель, данные и предварительное чтение из книги. '
             'Все случаи условные или синтетические. Учебный пилот не выполнен.')
    (stage / 'index.md').write_text('---\ntitle: "' +
                                  ('Module overview' if lang == 'en' else 'Обзор модуля') +
                                  '"\n---\n\n' + intro + '\n', encoding='utf-8')
    config = {
        'project': {'type': 'book', 'output-dir': '_book', 'resources': [
            str(relative / 'model'), str(relative / lang / 'worksheets'),
            str(relative / lang / 'evidence')]},
        'book': {'title': title, 'author': 'Igor Markelov',
                 'output-file': f'advection-dispersion-module-{lang}',
                 'chapters': ['index.md'] + [str(relative / lang / p) for p in readings]},
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
