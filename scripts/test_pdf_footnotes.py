"""Read back the real fixture PDF: labels, named destinations, and note order."""
import re
import sys
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from pypdf import PdfReader


def check(pdf):
    reader = PdfReader(pdf)
    text = '\n'.join(page.extract_text() for page in reader.pages)
    notes = ['Outside before text', 'First distinct note text', 'Second distinct note text',
             'Third distinct note text', 'Outside after text', 'Fourth distinct note text',
             'First figure note text', 'Second figure note text']
    for number, words in enumerate(notes, 1):
        phrase = r'\s+'.join(map(re.escape, words.split()))
        assert re.search(r'(?<!\d)' + str(number) + r'\s*' + phrase, text), (number, words)
    names = reader.named_destinations
    points = []
    for number in range(1, 9):
        name = f'Hfootnote.{number}'
        assert name in names, name
        dest = names[name]
        points.append((reader.get_destination_page_number(dest), -float(dest['/Top'])))
    assert points == sorted(points) and len(set(points)) == 8, points
    targets = []
    for page in reader.pages:
        for annotation in page.get('/Annots', []):
            action = annotation.get_object().get('/A', {})
            if action.get('/S') == '/GoTo':
                target = action.get('/D')
                if isinstance(target, str):
                    assert target in names, target
                    if target.startswith('Hfootnote.'):
                        targets.append(target)
    assert sorted(targets) == [f'Hfootnote.{n}' for n in range(1, 9)], targets
    print('PASS: eight printed note labels, eight distinct ordered destinations, eight resolved calls')


if __name__ == '__main__':
    # An existing fixture PDF can be checked for the pre-fix negative control.
    if len(sys.argv) == 2:
        check(sys.argv[1])
    else:
        repo = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory(prefix='book-footnotes-') as tmp:
            stage = Path(tmp)
            shutil.copyfile(repo / 'scripts/fixtures/delayed-footnotes.qmd', stage / 'check.qmd')
            shutil.copyfile(repo / 'filters/delayed-footnotes.lua', stage / 'delayed-footnotes.lua')
            shutil.copyfile(repo / 'sources/img/ch5_electron_donor_ladder.png', stage / 'figure.png')
            subprocess.run([os.environ.get('QUARTO', 'quarto'), 'render', 'check.qmd',
                            '--to', 'pdf', '-M', 'latex-auto-install:false'], cwd=stage, check=True)
            check(stage / 'check.pdf')
