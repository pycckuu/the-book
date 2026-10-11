"""Render one standalone language guide without executing a model."""
import argparse
from pathlib import Path
import shutil
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lang', choices=['en', 'ru'], required=True)
    parser.add_argument('--to', choices=['html', 'pdf', 'all'], default='all')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--quarto', default='quarto')
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    output = args.output.resolve()
    if output.is_relative_to(source.parents[1]):
        parser.error('Choose a new output directory outside the repository.')
    output.mkdir(parents=True, exist_ok=False)
    stage = output / 'source'
    stage.mkdir()
    for name in [f'modeling-guide-{args.lang}.md', 'guide-format.json', 'guide.css']:
        shutil.copyfile(source / name, stage / name)
    shutil.copytree(source / 'figures' / args.lang, stage / 'figures' / args.lang)
    for fmt in (['html', 'pdf'] if args.to == 'all' else [args.to]):
        command = [args.quarto, 'render', f'modeling-guide-{args.lang}.md',
                   '--to', fmt, '--metadata-file', 'guide-format.json', '--no-execute']
        if fmt == 'pdf':
            command += ['-M', 'pdf-auto-install:false']
        with (output / f'{fmt}.log').open('w') as log:
            subprocess.run(command, cwd=stage, stdout=log,
                           stderr=subprocess.STDOUT, check=True)
        shutil.copyfile(stage / f'modeling-guide-{args.lang}.{fmt}',
                        output / f'modeling-guide-{args.lang}.{fmt}')
        print(f'{args.lang} {fmt}: complete', flush=True)


if __name__ == '__main__':
    main()
