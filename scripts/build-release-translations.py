"""Add separate Russian book and bilingual course files to release downloads."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def build(repo, output, quarto):
    # Use only translation sources in this release, never a newer checkout.
    russian = repo / 'translations/ru'
    helper = next((russian / name for name in ['build-chapters.py', 'build-chapter01.py']
                   if (russian / name).is_file()), None)
    if helper is None:
        raise SystemExit('Release requires Russian book sources and their build helper.')
    targets = [(helper, None, ['pdf', 'epub'], 'partial Russian book')]
    for course in sorted((repo / 'courses').glob('*')):
        if not course.is_dir():
            continue
        helper = course / 'build.py'
        if not helper.is_file():
            if any((p.is_dir() and p.name == 'ru') or p.match('*-ru.*')
                   or p.match('*.ru.md') for p in course.rglob('*')):
                raise SystemExit(f'Russian course {course.name} requires a bilingual build helper.')
            continue
        for lang in ['en', 'ru']:
            targets.append((helper, lang, ['pdf'] if course.name == 'modeling-guide'
                            else ['pdf', 'epub'], course.name))
    output.mkdir(parents=True, exist_ok=True)
    assets = []
    with tempfile.TemporaryDirectory(prefix='book-release-') as temporary:
        for index, (helper, lang, formats, scope) in enumerate(targets):
            for fmt in formats:
                stage = Path(temporary) / f'{index}-{fmt}'
                command = [sys.executable, str(helper), '--to', fmt, '--output', str(stage),
                           '--quarto', quarto]
                if lang:
                    command += ['--lang', lang]
                subprocess.run(command, cwd=repo, check=True)
                # Book/module helpers place files in <format>/; the guide uses its root.
                folder = stage / fmt if (stage / fmt).is_dir() else stage
                files = list(folder.glob(f'*.{fmt}'))
                if len(files) != 1:
                    raise SystemExit(f'Expected one {fmt} from {helper}, found {len(files)}.')
                source = files[0]
                destination = output / source.name
                if destination.exists():
                    raise SystemExit(f'Refusing to overwrite release asset {destination.name}.')
                shutil.copyfile(source, destination)
                assets.append({'file': source.name, 'language': lang or 'ru', 'scope': scope,
                               'sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
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
    print(f'Built {len(assets)} separate translation/course release assets.', flush=True)


if __name__ == '__main__':
    main()
