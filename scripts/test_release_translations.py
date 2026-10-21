"""Check the delivered two-volume file contract and complete source selection."""
import importlib.util
import json
import re
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
sys.dont_write_bytecode = True


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(file))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


release = load('release', 'build-release-translations.py')
modeling = load('modeling', 'build-modeling.py')
# Only stand in for the external renderer; release naming and failure policy are real.
HELPER = '''import argparse
from pathlib import Path
p = argparse.ArgumentParser()
p.add_argument('--to'); p.add_argument('--output'); p.add_argument('--quarto')
p.add_argument('--lang', default='ru')
a = p.parse_args()
folder = Path(a.output) / a.to
folder.mkdir(parents=True)
name = 'modeling-' + a.lang if Path(__file__).name == 'build-modeling.py' else 'the-invisible-architects-ru'
(folder / (name + '.' + a.to)).write_bytes(b'rendered document')
'''


class TwoVolumeRelease(unittest.TestCase):
    def test_release_contract_and_render_failure(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            repo, output = root / 'repo', root / 'dist'
            repo.mkdir()
            with self.assertRaisesRegex(SystemExit, 'requires two-volume'):
                release.build(repo, output, 'quarto')
            for name in ['translations/ru/build-chapters.py', 'scripts/build-modeling.py']:
                helper = repo / name
                helper.parent.mkdir(parents=True)
                helper.write_text(HELPER)
            output.mkdir()
            for fmt in ['pdf', 'epub']:
                (output / f'the-invisible-architects.{fmt}').write_bytes(b'English book')
            # Old standalone modules must not silently reappear as extra release files.
            extra = output / 'oxygen-diffusion-module-ru.pdf'
            extra.write_bytes(b'old module')
            with self.assertRaisesRegex(SystemExit, 'unexpected='):
                release.build(repo, output, 'quarto')
            extra.unlink()
            # The first failed run already produced files. A rerun must not overwrite them.
            with self.assertRaisesRegex(SystemExit, 'overwrite'):
                release.build(repo, output, 'quarto')
            for file in output.iterdir():
                if not file.name.startswith('the-invisible-architects.'):
                    file.unlink()
            assets = release.build(repo, output, 'quarto')
            self.assertEqual(len(assets), 8)
            self.assertEqual({(a['language'], a['scope']) for a in assets},
                             {('en', 'book'), ('ru', 'book'), ('en', 'modeling'), ('ru', 'modeling')})
            for lang in ['en', 'ru']:
                for scope in ['book', 'modeling']:
                    self.assertEqual(sum(a['language'] == lang and a['scope'] == scope for a in assets), 2)
            self.assertEqual(json.loads((output / 'translation-assets.json').read_text())['assets'], assets)
            (repo / 'scripts/build-modeling.py').write_text(HELPER + "\nraise SystemExit(3)\n")
            with self.assertRaises(subprocess.CalledProcessError):
                release.build(repo, root / 'failed', 'quarto')

    def test_complete_modeling_readings_and_no_execution(self):
        repo = Path(__file__).resolve().parents[1]
        for lang in ['en', 'ru']:
            with self.subTest(lang=lang), tempfile.TemporaryDirectory() as temporary:
                stage = Path(temporary) / 'project'
                readings = modeling.prepare(repo, stage, lang)
                config = json.loads((stage / '_quarto.yml').read_text())
                self.assertFalse(config['execute']['enabled'])
                self.assertEqual(len(readings), len(set(readings)))
                # Compare with the independently maintained module source inventories.
                for module in ['oxygen-diffusion', 'advection-dispersion',
                               'saturation-kinetics', 'energy-constraints']:
                    folder = repo / 'courses' / module / lang
                    for source in folder.iterdir():
                        if source.suffix in ['.md', '.qmd'] and any(
                                word in source.name for word in ['student-packet', 'instructor-packet',
                                'worked-answers', 'curriculum', 'pilot-protocol', 'verification-methods',
                                'scientific-reading', 'module-reading']):
                            self.assertIn(str(source.relative_to(repo)), readings)
                for name in readings:
                    self.assertTrue((stage / name).is_file(), name)
                combined = '\n'.join((stage / name).read_text() for name in readings)
                notes = re.findall(r'^\[\^([^\]]+)\]:', combined, re.MULTILINE)
                anchors = re.findall(r'\{#([\w-]+)', combined)
                self.assertEqual(len(notes), len(set(notes)), 'ambiguous note definitions')
                self.assertEqual(len(anchors), len(set(anchors)), 'ambiguous explicit destinations')
                self.assertTrue(any('modeling-guide' in name for name in readings))
                self.assertEqual(sum('optional-observed-data/' in name for name in readings), 2)


if __name__ == '__main__':
    unittest.main()
