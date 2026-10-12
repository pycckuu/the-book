"""Check release asset selection and missing-Russian failure without publishing."""
import importlib.util
import sys
sys.dont_write_bytecode = True
import json
from pathlib import Path
import tempfile
import subprocess
import unittest

spec = importlib.util.spec_from_file_location('translations',
                                             Path(__file__).with_name('build-release-translations.py'))
translations = importlib.util.module_from_spec(spec)
spec.loader.exec_module(translations)

# A stand-in for existing Quarto helpers, not a model or document renderer.
HELPER = '''import argparse
from pathlib import Path
p = argparse.ArgumentParser()
p.add_argument('--to'); p.add_argument('--output'); p.add_argument('--quarto')
p.add_argument('--lang', default='ru')
a = p.parse_args()
folder = Path(a.output) / a.to
folder.mkdir(parents=True)
name = Path(__file__).parent.name + '-' + a.lang + '.' + a.to
(folder / name).write_bytes(b'rendered file')
'''


class ReleaseAssets(unittest.TestCase):
    def test_bilingual_assets_and_missing_russian(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo, output = root / 'repo', root / 'dist'
            repo.mkdir()
            with self.assertRaisesRegex(SystemExit, 'requires Russian'):
                translations.build(repo, output, 'quarto')
            helpers = [repo / 'translations/ru/build-chapter01.py',
                       repo / 'courses/advection-dispersion/build.py',
                       repo / 'courses/saturation-kinetics/build.py',
                       repo / 'courses/energy-constraints/build.py',
                       repo / 'courses/modeling-guide/build.py']
            for helper in helpers:
                helper.parent.mkdir(parents=True, exist_ok=True)
                helper.write_text(HELPER)
            for helper in helpers[1:]:
                if helper.parent.name != 'modeling-guide':
                    (helper.parent / 'ru').mkdir()
            # The real guide has root-level language files, not en/ and ru/.
            guide = helpers[-1].parent
            (guide / 'modeling-guide-ru.md').write_text('Russian guide source')
            helpers[-1].unlink()
            with self.assertRaisesRegex(SystemExit, 'modeling-guide requires'):
                translations.build(repo, output, 'quarto')
            helpers[-1].write_text(HELPER)
            loose = repo / 'courses/unbuilt/reading.ru.md'
            loose.parent.mkdir()
            loose.write_text('Russian reading without a directory named ru')
            with self.assertRaisesRegex(SystemExit, 'unbuilt requires'):
                translations.build(repo, output, 'quarto')
            loose.unlink()
            loose.parent.rmdir()
            # A translated course may never disappear because its helper is missing.
            missing = repo / 'courses/oxygen-diffusion/ru'
            missing.mkdir(parents=True)
            with self.assertRaisesRegex(SystemExit, 'oxygen-diffusion requires'):
                translations.build(repo, output, 'quarto')
            oxygen_helper = missing.parent / 'build.py'
            oxygen_helper.write_text(HELPER)
            helpers.append(oxygen_helper)
            assets = translations.build(repo, output, 'quarto')
            self.assertEqual(len(assets), 20)
            self.assertEqual(len(list(output.glob('*.pdf'))), 11)
            self.assertEqual(len(list(output.glob('*.epub'))), 9)
            self.assertEqual({a['language'] for a in assets}, {'en', 'ru'})
            self.assertEqual(json.loads((output / 'translation-assets.json').read_text())['assets'], assets)
            with self.assertRaisesRegex(SystemExit, 'overwrite'):
                translations.build(repo, output, 'quarto')
            # A failed Russian module render must stop the entire release step.
            helpers[-1].write_text(HELPER + "\nif a.lang == 'ru': raise SystemExit(3)\n")
            with self.assertRaises(subprocess.CalledProcessError):
                translations.build(repo, root / 'failed-dist', 'quarto')


if __name__ == '__main__':
    unittest.main()
