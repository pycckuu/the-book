"""Render one Russian book with Chapters 1-10, the Epilogue and Appendices A-Q outside the source repository."""
import argparse
import hashlib
import json
import re
import string
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
    chapters = ['translations/ru/chapters/01-budget-of-the-universe.md',
                'translations/ru/chapters/02-the-stage.md',
                'translations/ru/chapters/03-spark.md',
                'translations/ru/chapters/04-the-first-city.md',
                'translations/ru/chapters/05-the-poisoning.md',
                'translations/ru/chapters/06-cannibals-and-voters.md',
                'translations/ru/chapters/07-the-merger.md',
                'translations/ru/chapters/08-the-equation.md',
                'translations/ru/chapters/09-cities-without-sunlight.md',
                'translations/ru/chapters/10-the-water-planet.md']
    epilogue = ['translations/ru/chapters/epilogue.md']
    appendices = ['translations/ru/appendices/a-energy-toolkit.md',
                  'translations/ru/appendices/b-model-toolkit.md',
                  'translations/ru/appendices/c-reaction-gallery.md',
                  'translations/ru/appendices/d-math-without-pain.md',
                  'translations/ru/appendices/e-dramatis-personae.md']
    course_readings = ['courses/oxygen-diffusion/ru/student-packet-ru.md',
                       'courses/oxygen-diffusion/ru/instructor-packet-ru.md',
                       'courses/oxygen-diffusion/optional-observed-data/data-comparison-task-ru.md',
                       'courses/oxygen-diffusion/optional-observed-data/data-comparison-solutions-ru.md',
                       'courses/saturation-kinetics/ru/scientific-reading.md',
                       'courses/saturation-kinetics/ru/student-packet.md',
                       'courses/saturation-kinetics/ru/OPEN-worked-answers.md',
                       'courses/energy-constraints/ru/scientific-reading.md',
                       'courses/energy-constraints/ru/student-packet.md',
                       'courses/energy-constraints/ru/OPEN-worked-answers.md',
                       'courses/advection-dispersion/ru/student-packet-ru.qmd',
                       'courses/advection-dispersion/ru/worked-answers-ru.qmd']
    appendix_titles = ['Энергетический инструментарий', 'Инструментарий моделирования',
                       'Галерея реакций', 'Математика без боли', 'Действующие лица']
    for name in course_readings:
        source = (repo / name).read_text(encoding='utf-8')
        title = re.search(r'^title: "(.+)"$', source, re.MULTILINE)
        appendix_titles.append(title[1] if title else re.search(r'^# (.+)$', source, re.MULTILINE)[1])
    # Solutions remain public, separately titled readings after the exercises.
    for index in (6, 8):
        appendix_titles[index] += ' (ОТКРЫТЫЕ)'
    appendices += course_readings
    resources = sorted(set(re.findall(
        r'\]\(\.\./\.\./\.\./(courses/[^)]+)\)',
        (repo / appendices[1]).read_text(encoding='utf-8'))))
    resource_roots = ['courses/oxygen-diffusion/ru', 'courses/oxygen-diffusion/optional-observed-data',
                      'courses/advection-dispersion/ru', 'courses/advection-dispersion/model',
                      'courses/saturation-kinetics/ru', 'courses/saturation-kinetics/model',
                      'courses/energy-constraints/ru', 'courses/energy-constraints/model',
                      'courses/modeling-guide']
    resources = sorted(set(resources) | {
        str(path.relative_to(repo)) for root in resource_roots for path in (repo / root).rglob('*')
        if path.is_file() and '__pycache__' not in path.parts and not path.name.startswith('.')
        and str(path.relative_to(repo)) not in course_readings})
    files = chapters + epilogue + appendices + resources + ['sources/bibliograph.bib', 'sources/img/ch3_rna_world.png', 'sources/img/ch4_mat_cross_section.png', 'translations/ru/img/ch6_cannibalism.png', 'translations/ru/img/ch5_electron_donor_ladder.png', 'translations/ru/img/ch7_integration_spectrum.png', 'translations/ru/img/ch8_porewater_profile.png', 'translations/ru/img/ch9_redox_ladder.png', 'translations/ru/img/ch10_aquifer_rtm.png',
             'translations/ru/chapter-callouts.lua', 'filters/companion-links.lua', 'filters/delayed-footnotes.lua', 'courses/README.md']
    for name in files:
        target = stage / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(repo / name, target)
    # The epilogue follows Chapter 10 without becoming Chapter 11.
    epilogue_source = stage / epilogue[0]
    text = epilogue_source.read_text(encoding='utf-8')
    text = re.sub(r'^title:.*\n', '', text, count=1, flags=re.MULTILINE)
    text = text.replace('---\n\n', '---\n\n# Эпилог. Что такое жизнь? {#sec-epilogue-ru .unnumbered}\n\n', 1)
    text = re.sub(r'^(#{2,6}) (.+)$',
                  r'\1 `\\texorpdfstring{\\phantomsection}{}`{=latex}\2 {.unnumbered}', text, flags=re.MULTILINE)
    epilogue_source.write_text(text, encoding='utf-8')
    # Keep A-E and mirror the English course appendix order as F-Q.
    for appendix, letter, title in zip(appendices, string.ascii_uppercase[:17], appendix_titles):
        appendix_source = stage / appendix
        text = appendix_source.read_text(encoding='utf-8')
        heading = f'# Приложение {letter}. {title} {{#sec-appendix-{letter.lower()}-ru .unnumbered}}\n\n'
        if appendix in course_readings:
            text = re.sub(r'\A---\n.*?\n---\n\s*', '', text, count=1, flags=re.DOTALL)
            text = re.sub(r'\A# [^\n]+\n\s*', '', text, count=1)
            text = heading + text
        else:
            text = re.sub(r'^title:.*\n', '', text, count=1, flags=re.MULTILINE)
            text = text.replace('---\n\n', '---\n\n' + heading, 1)
        if letter in ('A', 'B'):
            # Preserve A.1-A.7 and make Chapter 10's B.5/B.6 references findable.
            for number, heading in enumerate(re.findall(r'^## .+$', text, re.MULTILINE), 1):
                text = text.replace(heading, f'## {letter}.{number} {heading[3:]}', 1)
        # Give each unnumbered PDF heading its own TOC destination.
        text = re.sub(r'^(#{2,6}) (.+)$',
                      r'\1 `\\texorpdfstring{\\phantomsection}{}`{=latex}\2 {.unnumbered}', text, flags=re.MULTILINE)
        text = re.sub(r'(\{#[^}\n]+)\} \{\.unnumbered\}', r'\1 .unnumbered}', text)
        if letter == 'B':
            text = text.replace('{#advection-dispersion-and-parent-loss} {.unnumbered}',
                                '{#advection-dispersion-and-parent-loss .unnumbered}')
        if letter == 'E':
            # Start each organism's field list after its bold name paragraph.
            text = re.sub(r'^(\*\*.*\*\*)\n(?=- )', r'\1\n\n', text, flags=re.MULTILINE)
        if letter == 'D':
            # Keep the closing explanation with its source note instead of a one-line final page.
            text = re.sub(r'(Реальные молекулы[^\n]+\[\^appd-partition-bridge\])',
                          r'```{=latex}\n\\begin{samepage}\n```\n\n\1\n\n```{=latex}\n\\end{samepage}\n```', text)
        appendix_source.write_text(text, encoding='utf-8')
    first_chapter = stage / chapters[0]
    first_chapter.write_text(first_chapter.read_text(encoding='utf-8').replace(
        '../appendices/d-math-without-pain.md', '#sec-appendix-d-ru'), encoding='utf-8')
    fourth_chapter = stage / chapters[3]
    fourth_chapter.write_text(fourth_chapter.read_text(encoding='utf-8').replace(
        '../appendices/a-energy-toolkit.md', '#sec-appendix-a-ru'), encoding='utf-8')
    # Keep the last Chapter 7 takeaway on its page instead of two orphaned lines.
    seventh_chapter = stage / chapters[6]
    seventh_chapter.write_text(seventh_chapter.read_text(encoding='utf-8').replace(
        '## Главное\n', '```{=latex}\n\\vspace{-\\baselineskip}\n```\n\n## Главное\n\n```{=latex}\n\\enlargethispage{2\\baselineskip}\n\\vspace{-\\baselineskip}\n```\n', 1), encoding='utf-8')
    eighth_chapter = stage / chapters[7]
    (stage / 'index.md').write_text(
        '# Как читать эту книгу {.unnumbered}\n\n'
        'Книга объединяет главы 1-10, эпилог и приложения A-Q. Приложения A-E дополняют повествование; '
        'F-Q содержат задания, научные пояснения и открытые решения четырёх учебных модулей. '
        'Сначала выполните задания самостоятельно, затем сравните свою работу с решениями и запишите использованную помощь. '
        'Сравнение с измерениями в H-I остаётся необязательным.\n\n'
        'Начните моделирование с главы 8 и приложения B. Порядок учебных приложений повторяет английскую книгу; '
        'для прохождения курса используйте последовательность: кислород (F-I), адвекция и дисперсия (P-Q), насыщение (J-L), энергия (M-O). '
        'В энергетическом модуле используются глава 1 и приложение A. '
        '[Руководство по моделированию](courses/modeling-guide/modeling-guide-ru.md) остаётся необязательным сопровождением и входит в комплект ресурсов. '
        'Данные, программы и рабочие листы находятся в комплекте ресурсов. '
        'Учебные пилоты пока не проведены; заявленная длительность занятий является плановой.\n', encoding='utf-8')
    config = {
        'project': {'type': 'book', 'output-dir': '_book', 'resources': resources},
        'book': {'title': 'Невидимые архитекторы',
                 'author': 'Igor Markelov', 'output-file': 'the-invisible-architects-ru',
                 'chapters': ['index.md'] + chapters + epilogue + appendices},
        'filters': ['translations/ru/chapter-callouts.lua', 'filters/companion-links.lua', 'filters/delayed-footnotes.lua'],
        'execute': {'enabled': False},
        'bibliography': 'sources/bibliograph.bib', 'suppress-bibliography': True,
        'lang': 'ru', 'format': {
            'html': {'toc': True}, 'epub': {'toc': True},
            'pdf': {'documentclass': 'scrbook', 'pdf-engine': 'xelatex',
                    'mainfont': 'PT Serif', 'sansfont': 'PT Sans', 'toc': True, 'toc-depth': 2,
                    'include-in-header': {'text': r'\interfootnotelinepenalty=10000'}}}}
    (stage / '_quarto.yml').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
    (output / 'inputs.json').write_text(json.dumps({
        str(p.relative_to(stage)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(stage.rglob('*')) if p.is_file()}, indent=2) + '\n')
    # Format-specific links always start from the same staged source text.
    linked_sources = {stage / name: (stage / name).read_text(encoding='utf-8')
                      for name in ['index.md', chapters[7], chapters[9], epilogue[0], appendices[1], appendices[4]] + course_readings}
    for fmt in (['html', 'pdf', 'epub'] if args.to == 'all' else [args.to]):
        for path, original in linked_sources.items():
            text = original
            if fmt != 'html' or str(path.relative_to(stage)) in course_readings or path.name == 'index.md':
                def book_link(match):
                    label, url = match[1], match[2]
                    if re.match(r'^[a-zA-Z][\w+.-]*:', url) or url.startswith('#'):
                        return match[0]
                    target, _, fragment = url.partition('#')
                    resolved = (path.parent / target).resolve()
                    if resolved in [stage / name for name in chapters + epilogue + appendices]:
                        if fmt == 'html':
                            return match[0]
                        name = str(resolved.relative_to(stage))
                        anchor = fragment or ('sec-appendix-' + string.ascii_lowercase[appendices.index(name)] + '-ru'
                                              if name in appendices else 'sec-epilogue-ru' if name in epilogue else
                                              re.search(r'^title: "(.+)"$', (stage / name).read_text(encoding='utf-8'),
                                                        re.MULTILINE)[1].lower().replace(' ', '-') if name in chapters else '')
                        return f'[{label}](#{anchor})' if anchor else match[0]
                    # Quarto must keep unrendered Markdown support files as raw downloads.
                    return match[0] + '{project-resolve-ignore="true"}' if fmt == 'html' else match[0]
                text = re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)', book_link, text)
            if fmt == 'pdf':
                text = text.replace('../../../courses/', 'courses/')
            if fmt == 'pdf' and str(path.relative_to(stage)) in course_readings:
                letter = string.ascii_uppercase[appendices.index(str(path.relative_to(stage)))]
                # Full course titles stay in the contents; running heads fit the page.
                text = re.sub(r'(^# [^\n]+\n)', lambda m: m[0] + '\n```{=latex}\n'
                              '\\renewcommand{\\sectionmark}[1]{}\n'
                              f'\\markboth{{Приложение {letter}}}{{Приложение {letter}}}\n'
                              '\\sloppy\n\\setcounter{figure}{0}\n'
                              f'\\renewcommand{{\\thefigure}}{{{letter}.\\arabic{{figure}}}}\n'
                              '```\n', text, count=1, flags=re.MULTILINE)
                if str(path.relative_to(stage)) == 'courses/energy-constraints/ru/OPEN-worked-answers.md':
                    # Wrap the gross/net inventory balance, preserving its terms and order.
                    text = re.sub(r'\$\$\n(\\Xi_\+=.*?)\n\$\$',
                                  lambda m: '$$\n\\begin{gathered}\n' +
                                  m[1].replace(',\\quad', ',\\\\') +
                                  '\n\\end{gathered}\n$$', text, count=1, flags=re.DOTALL)
            if fmt == 'pdf' and path.name == '10-the-water-planet.md':
                # Short running heads; keep full section titles and TOC entries.
                for heading, short in [('Быстрые и медленные реакции: приём частичного равновесия', 'Частичное равновесие'),
                                       ('Инструкция по эксплуатации возрастом 4.5 миллиарда лет', 'Инструкция по эксплуатации планеты')]:
                    title = f'## {heading}\n'
                    text = text.replace(title,
                                        '```{=latex}\n\\let\\bookrusectionmark\\sectionmark\n'
                                        f'\\renewcommand{{\\sectionmark}}[1]{{\\markright{{\\thesection\\quad {short}}}}}\n'
                                        '```\n\n' + title + '\n```{=latex}\n'
                                        '\\let\\sectionmark\\bookrusectionmark\n```\n', 1)
                # Keep the final takeaway together instead of a four-line final page.
                text = text.replace('## Главное\n',
                                    '## Главное\n\n```{=latex}\n\\enlargethispage{4\\baselineskip}\n```\n', 1)
            if fmt == 'pdf' and path.name == 'epilogue.md':
                # Keep each definition and the two-item summary intact.
                for pattern in (r'^\*\*Жизнь[^\n]+$', r'^1\. \*\*Генетическая информация[^\n]+\n2\. [^\n]+$'):
                    text = re.sub(pattern,
                                  lambda m: '```{=latex}\n\\begin{samepage}\n```\n\n' + m[0] +
                                  '\n\n```{=latex}\n\\end{samepage}\n```', text, flags=re.MULTILINE)
                # Keep the closing synthesis and question on the same page.
                text = re.sub(r'(Эти три утверждения составляют.*?Вопрос в том, приложим ли мы усилие, чтобы понять их\.)',
                              lambda m: '```{=latex}\n\\begin{samepage}\n```\n\n' + m[0] +
                              '\n\n```{=latex}\n\\end{samepage}\n```', text, count=1, flags=re.DOTALL)
            if fmt == 'pdf' and path.name == 'e-dramatis-personae.md':
                # Avoid stretching vertical gaps when a complete profile moves to the next page.
                text = text.replace('\n# Приложение E.',
                                    '\n```{=latex}\n\\raggedbottom\n```\n\n# Приложение E.', 1)
                # Keep short organism entries together; the three-note entry may span pages.
                text = re.sub(r'^(\*\*[^\n]+\*\*\n\n(?:- [^\n]+\n){5})',
                              lambda m: m[0] if '[^deep-life-appe]' in m[0] else
                              '```{=latex}\n\\begin{samepage}\n```\n\n' + m[0] +
                              '\n```{=latex}\n\\end{samepage}\n```\n',
                              text, flags=re.MULTILINE)
                text += '\n```{=latex}\n\\flushbottom\n```\n'
            if fmt == 'pdf' and path.name == 'b-model-toolkit.md':
                # Split three long balances across rows without changing source math.
                for first_line in (r'\frac{dM}{dt}', r'M^{n+1}-M^n', r'(u-D_Lr_-)a'):
                    text = re.sub(r'\$\$\n(' + re.escape(first_line) + r'.*?)\n\$\$',
                                  lambda m: '$$\n\\begin{gathered}\n' + re.sub(
                                      r',\s*\\qquad\s*|,\s*\\quad\s*',
                                      lambda _: ',\\\\\n', m[1]) + '\n\\end{gathered}\n$$',
                                  text, flags=re.DOTALL)
            if fmt == 'epub':
                text = re.sub(r'\[([^]]+)\]\(\.\./\.\./\.\./(courses/[^)]+)\)',
                              lambda m: f'{m[1]} (отдельный ресурс этой редакции: {m[2]})', text)
            path.write_text(text, encoding='utf-8')
        command = [args.quarto, 'render', '--to', fmt]
        if fmt == 'pdf':
            command += ['-M', 'latex-auto-install:false']
        with (output / f'{fmt}.log').open('w') as log:
            subprocess.run(command, cwd=stage, stdout=log, stderr=subprocess.STDOUT, check=True)
        shutil.copytree(stage / '_book', output / fmt)
        for resource in resources:
            target = output / fmt / resource
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(repo / resource, target)
        print(f'ru complete book chapters01-10 epilogue appendices-a-q {fmt}: built', flush=True)


if __name__ == '__main__':
    main()
