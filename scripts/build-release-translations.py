"""Add the Russian book and complete EN/RU modeling volumes to release downloads."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def build(repo, output, quarto):
    targets = [(repo / 'translations/ru/build-chapters.py', None, 'book'),
               (repo / 'scripts/build-modeling.py', 'en', 'modeling'),
               (repo / 'scripts/build-modeling.py', 'ru', 'modeling')]
    for helper, _, _ in targets:
        if not helper.is_file():
            raise SystemExit(f'Release requires two-volume build helper: {helper.relative_to(repo)}')
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='book-release-') as temporary:
        for index, (helper, lang, _) in enumerate(targets):
            for fmt in ['pdf', 'epub']:
                stage = Path(temporary) / f'{index}-{fmt}'
                command = [sys.executable, str(helper), '--to', fmt, '--output', str(stage),
                           '--quarto', quarto]
                if lang:
                    command += ['--lang', lang]
                subprocess.run(command, cwd=repo, check=True)
                files = list((stage / fmt).glob(f'*.{fmt}'))
                if len(files) != 1:
                    raise SystemExit(f'Expected one {fmt} from {helper}, found {len(files)}.')
                destination = output / files[0].name
                if destination.exists():
                    raise SystemExit(f'Refusing to overwrite release asset {destination.name}.')
                shutil.copyfile(files[0], destination)
    expected = {f'{name}.{fmt}': (lang, scope) for name, lang, scope in [
        ('the-invisible-architects', 'en', 'book'), ('the-invisible-architects-ru', 'ru', 'book'),
        ('modeling-en', 'en', 'modeling'), ('modeling-ru', 'ru', 'modeling')]
        for fmt in ['pdf', 'epub']}
    actual = {p.name for p in output.iterdir() if p.suffix in ['.pdf', '.epub']}
    if actual != expected.keys():
        raise SystemExit(f'Expected only two volumes per language: missing={expected.keys()-actual}, '
                         f'unexpected={actual-expected.keys()}')
    assets = [{'file': name, 'language': lang, 'scope': scope,
               'sha256': hashlib.sha256((output / name).read_bytes()).hexdigest()}
              for name, (lang, scope) in sorted(expected.items())]
    (output / 'translation-assets.json').write_text(
        json.dumps({'assets': assets}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return assets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path.cwd())
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--quarto', default='quarto')
    args = parser.parse_args()
    assets = build(args.repo.resolve(), args.output.resolve(), args.quarto)
    print(f'Validated {len(assets)} bilingual two-volume release assets.', flush=True)


if __name__ == '__main__':
    main()
