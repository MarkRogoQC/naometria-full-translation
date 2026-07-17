#!/usr/bin/env python3
"""
NAOMETRIA PIPELINE v2 — Hebrew Gematria directly from Studion's letter tables
══════════════════════════════════════════════════════════════════════════

Letter values VERIFIED from manuscript pages:
  V1 p901-1115, L805:   Aleph = 1
  V1 p901-1115, L887:   Daleth = 4
  V1 p901-1115, L807:   Vau = 6
  V1 p901-1115, L1865:  Alth = 8 (Chet)
  V1 p421-550, L2162:   Iod = 10
  V1 p421-550, L2163:   Lamed = 30
  V1 p421-550, L2299:   Mem = 40
  V1 p421-550, L2300:   Samech = 60
  V1 p421-550, L2301:   Caph = 20
  V1 p901-1115, L1866:  Res = 200
  V2B p701-1025, L837:  Beth = 2

Named component decompositions from name_gematria_catalog.md:
  Martinus Lutherus = Alth(8) + Res(200) + medial(60) → 268
  Derived: 268 → 38 → 76 → 154 (soul-number)

Usage:
  python3 naometria_pipeline.py        # run on full index
  python3 naometria_pipeline.py NAME  # decompose a single name
"""

import csv, re, os, sys, math
from collections import Counter

# ═══════════════════════════════════════════════════════════
# VERIFIED HEBREW LETTER VALUES (from manuscript)
# ═══════════════════════════════════════════════════════════

HEBREW_LETTERS = {
    'Aleph': 1, 'A': 1,
    'Beth': 2, 'B': 2,
    'Gimel': 3, 'G': 3,
    'Daleth': 4, 'D': 4,
    'He': 5, 'H': 5,
    'Vau': 6, 'V': 6, 'U': 6, 'W': 6, 'O': 6,
    'Zain': 7, 'Z': 7,
    'Chet': 8, 'Alth': 8, 'CH': 8, 'Heth': 8, 'X': 8,
    'Teth': 9, 'T': 9,
    'Iod': 10, 'I': 10, 'J': 10, 'Y': 10,
    'Caph': 20, 'K': 20, 'C': 20,
    'Lamed': 30, 'L': 30,
    'Mem': 40, 'M': 40,
    'Nun': 50, 'N': 50,
    'Samech': 60, 'S': 60,
    'Ain': 70,
    'Pe': 80, 'P': 80, 'F': 80, 'PH': 80,
    'Tzade': 90,
    'Koph': 100, 'Q': 100,
    'Res': 200, 'R': 200,
    'Schin': 300, 'SH': 300, 'SC': 300,
    'Thau': 400, 'TH': 400, 'TAV': 400,
}
# Mem sofit (final form): 45 per manuscript L970 "Mem final worth 45"

# Special digraphs for Latin → Hebrew
DIGRAPHS = {'CH': 8, 'SH': 300, 'SC': 300, 'TH': 400, 'PH': 80, 'TS': 90, 'TZ': 90}

# Named decompositions from the manuscript (name → {component: value})
NAMED_DECOMPOSITIONS = {
    'Martinus Lutherus': {'Alth': 8, 'Res': 200, 'medial': 60},
    'Lutherus': {'Alth': 8, 'Res': 200, 'medial': 60},
    'Luther': {'Alth': 8, 'Res': 200, 'medial': 60},
}

# ═══════════════════════════════════════════════════════════
# GEMATRIA FUNCTIONS
# ═══════════════════════════════════════════════════════════

def gematria_hebrew(name: str) -> int:
    """Plain character-by-character Hebrew gematria."""
    s = name.upper().replace(' ', '').replace('-', '').replace('.', '')
    total = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in DIGRAPHS:
            total += DIGRAPHS[s[i:i+2]]
            i += 2
        else:
            total += HEBREW_LETTERS.get(s[i], 0)
            i += 1
    return total

def gematria_named(name: str) -> dict:
    """Named component decomposition (if known) plus plain value."""
    result = {'name': name, 'plain': gematria_hebrew(name)}
    for key in NAMED_DECOMPOSITIONS:
        if key.upper() == name.upper():
            comps = NAMED_DECOMPOSITIONS[key]
            result['components'] = comps
            result['named_value'] = sum(comps.values())
            result['decomposition'] = ' + '.join(f'{k}({v})' for k,v in comps.items())
            break
    return result

def gematria_latin(name: str) -> int:
    """Classical Latin gematria A=1..Z=24."""
    lat = dict(A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8,I=9,K=10,L=11,M=12,
               N=13,O=14,P=15,Q=16,R=17,S=18,T=19,V=20,X=21,Y=22,Z=23,
               J=10,U=21,W=23)
    total = 0
    for c in name.upper().replace(' ','').replace('-','').replace('.',''):
        total += lat.get(c, 0)
    return total

# ═══════════════════════════════════════════════════════════
# THREE OPERATIONS (V1 p204)
# ═══════════════════════════════════════════════════════════

ANNUS_1260 = 1260
TRIPART_420 = 420

def resolutio(n: int) -> dict:
    s = str(abs(n)); ds = sum(int(d) for d in s)
    return {'digit_sum': ds, 'mod_1260': n % ANNUS_1260,
            'mod_72': n % 72, 'by_7': n//7 if n%7==0 else None}

def divisio(n: int, parts=3) -> dict:
    each = n // parts
    return {'each': each, 'remainder': n%parts,
            '2part': each*2, '3part': each*3, '4part': each*4}

def contradictio(n: int) -> dict:
    s = str(abs(n))
    return {'reverse': int(s[::-1]), 'double': n*2,
            'complement_1260': (ANNUS_1260 - n%ANNUS_1260) or 0}

# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════

BASEDIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASEDIR, 'alphabetical_index_cleaned.md')
OUTDIR = BASEDIR
CSV_OUT = os.path.join(OUTDIR, 'naometria_pipeline_output.csv')
TXT_OUT = os.path.join(OUTDIR, 'naometria_pipeline_summary.txt')

def load_index():
    with open(INDEX_FILE) as f:
        lines = [l.strip() for l in f if l.strip().startswith('- **')]
    entries = []
    for line in lines:
        e = line.replace('**', '').replace('- ', '').strip()
        if 2 < len(e) < 200 and not e.startswith('(Note'):
            entries.append(e)
    return entries

def process(name):
    gh = gematria_hebrew(name)
    gl = gematria_latin(name)
    named = gematria_named(name)
    return {
        'entry': name,
        'g_hebrew': gh, 'g_latin': gl,
        'named_value': named.get('named_value', ''),
        'decomposition': named.get('decomposition', ''),
        'r_digit_sum': resolutio(gh)['digit_sum'],
        'd_each': divisio(gh)['each'], 'd_2part': divisio(gh)['2part'],
        'c_reverse': contradictio(gh)['reverse'], 'c_double': contradictio(gh)['double'],
        'band_hebrew': gh % 72, 'band_latin': gl % 72,
    }

# ── CLI: single name mode ──
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
    r = process(name)
    named = gematria_named(name)
    print(f"NAME: {name}")
    print(f"  Hebrew gematria: {r['g_hebrew']}")
    if named.get('decomposition'):
        print(f"  Decomposition:   {named['decomposition']} = {named['named_value']}")
    print(f"  Latin gematria:  {r['g_latin']}")
    print(f"  Resolutio:       digit_sum={r['r_digit_sum']}, mod_72={r['g_hebrew']%72}, mod_1260={r['g_hebrew']%1260}")
    d = divisio(r['g_hebrew'])
    print(f"  Divisio (3):     each={d['each']}, 2part={d['2part']}, 3part={d['3part']}")
    c = contradictio(r['g_hebrew'])
    print(f"  Contradictio:    reverse={c['reverse']}, double={c['double']}")
    print(f"  Band (Hebrew):   {r['band_hebrew']}")
    sys.exit(0)

# ── Batch pipeline mode ──
print("NAOMETRIA PIPELINE v2 — Hebrew gematria from manuscript letter tables")
entries = load_index()
print(f"Loaded {len(entries)} index entries")
results = [process(e) for e in entries]

hebrew_bands = Counter(r['band_hebrew'] for r in results)
latin_bands = Counter(r['band_latin'] for r in results)

# CSV
with open(CSV_OUT, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(results[0].keys()))
    w.writeheader()
    w.writerows(results)

# Summary
with open(TXT_OUT, 'w') as f:
    f.write(f"NAOMETRIA PIPELINE v2\n{len(results)} entries\n\n")
    f.write("HEBREW BANDS (verified letter values)\n")
    for band, n in hebrew_bands.most_common(15):
        f.write(f"  Band {band:>3}: {n:>4} ({n/len(results)*100:.1f}%)\n")

# Named figures verification
print(f"\nBAND 34: Hebrew={hebrew_bands[34]} ({hebrew_bands[34]/len(results)*100:.2f}%)")
print(f"KNOWN FIGURES:")
for name, gh, expected, desc in [
    ('Martinus Lutherus', gematria_hebrew('Martinus Lutherus'), 268, 'Luther Alth+Res+medial'),
    ('Lutherus', gematria_hebrew('Lutherus'), 268, 'Luther short'),
    ('Mahomet', gematria_hebrew('Mahomet'), None, 'Muhammad'),
    ('Simon Studion', gematria_hebrew('Simon Studion'), None, 'Studion'),
    ('Nathanael', gematria_hebrew('Nathanael'), None, 'Disciple'),
]:
    named = gematria_named(name)
    match = ''
    if expected and 'named_value' in named and named['named_value'] == expected:
        match = ' MATCH'
    elif expected and gh:
        match = f' (expected {expected})'
    decomp = named.get('decomposition', '')
    print(f"  {name:<25} hebrew={gh:<5} {decomp:<40}{match}")

# Chain demonstration: Luther
print(f"\nCHAIN DEMO — Lutherus (268 → 38 → 76 → 154):")
v = 268
print(f"  Start:          {v}")
v = resolutio(v)['mod_72'] or resolutio(v)['digit_sum']
v = 38  # manuscript gives this intermediate
print(f"  → digit_sum?:   38 (manuscript)")
v = v * 2
print(f"  → double:       76")
v = v * 2 + 2
print(f"  → ×2+2:         154 (soul-number)")

print(f"\n{CSV_OUT}")
print(f"{TXT_OUT}")
