#!/usr/bin/env python3
"""Read archived Zenodo spreadsheets without modifying them; write derived CSV/JSON.
Run after oxygen_model.py: python3 compare_measured.py
No depth-profile observations are present. These are station summaries.
"""
import csv
import hashlib
import json
import statistics
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def read_summary(path):
    with zipfile.ZipFile(path) as z:
        strings = [''.join(x.itertext()) for x in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        root = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        assert not root.findall('.//s:f', NS), 'Unexpected formulas; inspect before extracting'
        data = []
        for row in root.findall('.//s:row', NS):
            cells = {}
            for cell in row.findall('s:c', NS):
                v = cell.find('s:v', NS)
                if v is not None:
                    cells[cell.get('r')] = strings[int(v.text)] if cell.get('t') == 's' else float(v.text)
            r = int(row.get('r'))
            if r in range(3, 11):
                data.append(dict(source_row=r, station=cells['A'+str(r)], season=cells['E'+str(r)],
                                 bottom_O2_uM=cells['H'+str(r)], TOU=cells['I'+str(r)],
                                 DOU=cells['J'+str(r)], OPD_mm=cells['L'+str(r)]))
        assert len(data) == 8
        return data


def main():
    paths = [ROOT/'data'/'Beck.Oxygen.Data.xlsx', ROOT/'data'/'latest-Beck.Oxygen.Data.xlsx']
    expected = ['3aa0ff04a92467b2ebcbeba730d47d09','80aeb327b8ebecd9d359c1c1b5ba0e00']
    for path, md5 in zip(paths, expected):
        assert hashlib.md5(path.read_bytes()).hexdigest() == md5
    v1, v2 = map(read_summary, paths)
    rows = []
    for a,b in zip(v1,v2):
        assert (a['station'],a['season']) == (b['station'],b['season'])
        ratio = b['DOU']/b['TOU'] if isinstance(b['DOU'],float) else None
        rows.append(dict(station=b['station'], season=b['season'], source_row=b['source_row'],
                         bottom_O2_uM=b['bottom_O2_uM'],
                         TOU_v1_mmol_m2_day=a['TOU'],TOU_v2_mmol_m2_day=b['TOU'],
                         DOU_v1_mmol_m2_day=a['DOU'],DOU_v2_mmol_m2_day=b['DOU'],
                         OPD_v1_mm=a['OPD_mm'],OPD_v2_mm=b['OPD_mm'],DOU_div_TOU_v2=ratio,
                         status='missing DOU and OPD, excluded from ratio' if ratio is None else 'reported measured summary; no uncertainty column'))
    out = ROOT/'results';out.mkdir(exist_ok=True)
    with (out/'measured-version-comparison.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    ratios=[r['DOU_div_TOU_v2'] for r in rows if r['DOU_div_TOU_v2'] is not None]
    synthetic_flux=json.loads((out/'verification.json').read_text())['analytic_steady']['surface_flux_mol_m2_s']*86400*1000
    report=dict(version1='10.5281/zenodo.12536642',version2='10.5281/zenodo.15367775',
                source_sheet='Table',source_range='A1:L10',row_count=8,paired_flux_rows=7,
                v2_mean_station_ratio=statistics.mean(ratios),
                v2_ratio_of_sums=sum(b['DOU'] for b in v2 if isinstance(b['DOU'],float))/sum(b['TOU'] for b in v2 if isinstance(b['DOU'],float)),
                illustrative_model_flux_mmol_m2_day=synthetic_flux,
                C6_July2019_v2=rows[1],
                warning='Archived versions contain different measured summaries. Neither contains raw profiles or error estimates. Do not silently mix with published article corrections or identify k from these data.',
                hashes={str(p.name):dict(md5=m,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p,m in zip(paths,expected)})
    (out/'measured-comparison.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
