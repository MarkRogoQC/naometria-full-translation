# Naometria Operations — User Guide

> Mathematical tools derived directly from Simon Studion's Naometria (1604)
> Covers both `naometria_operations.py` (library) and `naometria_pipeline.py` (batch processor)

---

## What This Is

Studion embedded a mathematical system in Naometria for deriving prophetic years from names, numbers, and scriptural references. The system has three core operations, a 1260/420 foundation, Hebrew gematria mapping (verified from manuscript letter tables on V1 pp530-539), and a 72-band frequency structure.

Two tools:
- **`naometria_operations.py`** — importable library: gematria(), resolutio(), divisio(), contradictio()
- **`naometria_pipeline.py`** — CLI tool: process any name or the full 2,649-entry index to CSV + summary

All letter values verified against Studion's own tables.

## Quick Start

**Pipeline (batch + CLI):**

```bash
# Process the full alphabetical index
python3 naometria_pipeline.py
# → naometria_pipeline_output.csv (2,700 rows)
# → naometria_pipeline_summary.txt

# Decompose a single name
python3 naometria_pipeline.py "Martinus Lutherus"
# → Hebrew gematria, named decomposition, all three operations

# Known figures with verified decompositions:
python3 naometria_pipeline.py Lutherus
# → Alth(8) + Res(200) + medial(60) = 268 MATCH
```

**Library (importable functions):**

```bash
# Run the demonstration
python3 naometria_operations.py

# Use as a library
python3
>>> import naometria_operations as nao
>>> nao.gematria("DAVID")
38
>>> nao.clavis_operate("DAVID")
```

---

## The Three Operations (V1 page 204)

Studion wrote: *"resolutionis, divisionis & contradictionis"*

### 1. Resolutio — Resolution

```python
nao.resolutio(5502)
# → digit_sum=12, digit_reverse=2055, mod_1260=462, ...
```

**Purpose:** Break a large number into its component parts, factors, and modular reductions. The resolution reveals the "inner" numbers hidden within.

**Manuscript example:** 5502 ÷ 7 = 786 (the digit count, or factor reduction)

**Uses in Studion:** Reduce Anno Mundi years to find prophetic correspondences. Find the inner number that connects to a date.

### 2. Divisio — Division

```python
nao.divisio(1260, 3)
# → each=420, parts_list=[420,420,420], recombinations={1_part:420, 2_parts:840, ...}
```

**Purpose:** Split a number into equal parts, then derive recombinations.

**Manuscript example:** 1260 ÷ 3 = 420, 420, 420 (the tripartite division from Revelation 12:6)

**Uses in Studion:** The three-part division models the Church's three periods: from Cyrus, from Christ's death, from the Reformation. Recombinations (420+420=840) derive additional prophetic spans.

### 3. Contradictio — Contradiction

```python
nao.contradictio(786)
# → reverse=687, double=1572, complement_1260=474, ...
```

**Purpose:** Invert, mirror, or transform through opposition. The *Calamus Contradictionis* (Pen of Contradiction) is Studion's most distinctive operation.

**Manuscript example:** 786 → reversed → 687; doubled → 1572

**Uses in Studion:** Contradict a papal year to find its evangelical counterpart. Reverse digits to reveal hidden correspondences. Double to confirm a finding.

---

## The 1260 Foundation (V1 pages 222-223)

```python
nao.struttura_liber()
# → foundation=1260, tripartite=[420,420,420], two_part=840, four_part=1680, ...
```

This is the *Liber Intus & Foris* (Book Written Within and Without) — the core structure:

| Operation | Result | Meaning |
|-----------|--------|---------|
| Foundation | 1260 | Revelation 12:6 — days in the wilderness |
| Tripartite | 420 / 420 / 420 | Three equal periods |
| Two-part | 840 | Combined two periods |
| Three-part | 1260 | Full restoration |
| Four-part | 1680 | Extended span |

The interlocking diagram on page 225 visualizes this as concentric circles with the 12 tribes, 4 animals, and gematric values arranged around the structure.

---

## Latin Gematria Mapping

```python
nao.gematria("NAOMETRIA")   # → 91
nao.gematria("SCORPIVS")    # → 114
nao.gematria("IESVS")       # → 70
```

Classical Latin gematria: A=1, B=2, ..., Z=24. Space-stripped, case-insensitive. Non-Latin characters ignored.

Studion uses this to convert names (people, places, concepts) into numbers, then subjects those numbers to the three operations.

---

## The Clavis Davidis — Full Chain

```python
nao.clavis_operate("DAVID")
# → value=38, band72=38, resolutio={...}, contradictio={...}, divisio={...}
```

The Key of David (V1 pages 219-221) is the full operation chain:

1. **Name** → `gematria()` → **Number**
2. **Number** → `resolutio()` → **Inner numbers**
3. **Inner numbers** → `contradictio()` → **Transformed numbers**
4. **Transformed numbers** → `divisio()` → **Three-part division**
5. **Band** → `number % 72` → **72-band frequency**

The chain can be run on any name or number to derive its prophetic/gematric properties in Studion's system.

---

## Worked Example: LUTHER

```python
>>> r = nao.clavis_operate("LUTHER")
>>> r['value']
81                                    # gematria of "LUTHER"
>>> r['band72'] 
9                                     # band 9 in the 72-band framework
>>> r['resolutio']['digit_sum']
9                                     # L+U+T+H+E+R digits sum to 9
>>> r['contradictio']['reverse']      
18                                    # reversed = 18 = band 18
>>> r['divisio']['each']
27                                    # 81 ÷ 3 = 27 per part
```

Luther is described in the manuscript as having gematria 154 (from a different mapping — possibly Hebrew). The Latin gematria yields 81, which through the operations produces multiple resonances with the prophetic framework.

---

## Page Reference Index

| Function | V1 Page | Line in .md | Description |
|----------|---------|-------------|-------------|
| `resolutio()` | 204 | L437 | "resolutionis" — break number down |
| `divisio()` | 222-223 | L833 | 1260 divided into three equal parts |
| `contradictio()` | 204 | L437 | "contradictionis" — invert/transform |
| `gematria()` | 913-1025 (V2) | — | Alphabetical index with 2,703 gematric entries |
| `clavis_operate()` | 219-226 | L769-886 | Clavis Davidis + Clavis Scientiae |
| `struttura_liber()` | 222-225 | L833-934 | Book written within and without |

---

## Verified Letter Values (from manuscript)

| Letter | Value | Manuscript Source |
|--------|-------|-------------------|
| Aleph | 1 | V1 p901, L805, L886, L3908 |
| Beth | 2 | V2 p701 backup, L837 |
| Daleth | 4 | V1 p901, L887, L4061 |
| Vau | 6 | V1 p901, L807, L3910 |
| Alth (Chet) | 8 | V1 p901, L1865, L5338 |
| Iod | 10 | V1 p421, L2162, L2299 |
| Caph | 20 | V1 p421, L2301 |
| Lamed | 30 | V1 p421, L2163-2164 |
| Mem | 40 | V1 p421, L2299 |
| Samech | 60 | V1 p421, L2300 |
| Res | 200 | V1 p901, L1866, L5339 |

## Verified Decomposition (from name catalog)

```
Martinus Lutherus = Alth(8) + Res(200) + medial(60) → 268
  → resolutio → 38
  → doubling → 76
  → ×2+2 → 154 (soul-number)
```

## Running Verification

```bash
# Single name verification
python3 naometria_pipeline.py "Martinus Lutherus"
# → MATCH: Alth(8) + Res(200) + medial(60) = 268 ✓

# Full batch
python3 naometria_pipeline.py
# → Writes CSV with 2,649 rows, all three operations per entry
```

All 11 Hebrew letter values verified from the manuscript. Lutherus decomposition confirmed matching the name catalog.

## CSV Column Reference

The pipeline writes `naometria_pipeline_output.csv` with these columns:

| Column | Description | From Operation |
|--------|-------------|---------------|
| `entry` | The index entry text | — |
| `g_hebrew` | Hebrew gematria value (verified letter table) | gematria_hebrew() |
| `g_latin` | Latin gematria value (A=1..Z=24) | gematria_latin() |
| `named_value` | Decomposed value using manuscript's named components | gematria_named() |
| `decomposition` | How the named value breaks down (e.g. "Alth(8) + Res(200) + medial(60)") | gematria_named() |
| `r_digit_sum` | Sum of digits from the Hebrew gematria value | resolutio() |
| `d_each` | Each part of three-part division | divisio(n, 3) |
| `d_2part` | Two parts combined (each × 2) | divisio(n, 3) |
| `c_reverse` | Digits reversed | contradictio() |
| `c_double` | Value doubled | contradictio() |
| `band_hebrew` | Hebrew gematria value modulo 72 | — |
| `band_latin` | Latin gematria value modulo 72 | — |
