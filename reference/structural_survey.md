# Naometria Structural Survey

## Overview
- **Teil 1:** 1,115 pages, 287MB (Cod.theol.et.phil.qt.23a)
- **Teil 2:** 1,025 pages, 263MB (Cod.theol.et.phil.qt.23b)
- **Total:** 2,140 pages, 550MB
- **Format:** Scanned manuscript — zero text layer. Every page = 1 RGB JPEG image at ~140-150ppi. Height uniform at 1500px, width varies 634-1500px.

## Blank Pages: NONE
Every page has content. JPEG sizes range 77K-451K — the "smallest" pages (77-85K) are section transitions with light content (title pages, blank rectos before sections), not true blanks. The PDF contains only the active manuscript leaves.

## Section Transitions (by image size drop)

### Teil 1
| Zone | Pages | Marker | Type |
|------|-------|--------|------|
| A | p1-p4 | — | Opening — title(s), preliminary matter (largest = 313K, 267K, 148K, 132K → decreasing format) |
| B | ~p10 | 137K | Section end or subsection title |
| C | ~p188 | 129K | Section boundary |
| D | **p218** | **85K** | Strongest transition — smallest file in both volumes. Likely book/part division. |
| E | ~p618 | 172K | Mid-volume transition |
| F | p1082-p1084 | 126-129K | Near-end, closing transitional pages |
| G | p1113-p1114 | 181K, 247K | Narrow format pages (654px, 772px) — foldouts or appendices |

### Teil 2
| Zone | Pages | Marker | Type |
|------|-------|--------|------|
| A | p1-p5 | 115K | Opening — title/transition |
| B | **p875** | 117K | Major section boundary |
| C | **p910-p912** | **94-111K** | Strongest transition cluster (3 pages) — book/part division |
| D | p1015-p1016 | 77-97K | Near-end transition. p1016 = smallest file in both volumes (77K) |
| E | p1023-p1024 | 154K, 189K | Narrow format pages (634px, 684px) — foldouts or appendices |

## Key Plates & Diagrams (Top 1% by image size)

### Teil 1
| Page | Size | Width | Notes |
|------|------|-------|-------|
| **p477** | **451K** | **1500px** | **LARGEST in either volume** — full-width engraving/plate |
| p1081 | 391K | 1500px | Near-end full-width plate |
| p1083 | 364K | 1500px | Companion to p1081 |
| p225 | 357K | 1177px | Significant engraving |
| p617 | 354K | 1425px | Near-full-width plate |
| p485-p489 | cluster | 1160-1168px | **5 consecutive plates** (335-356K) — major illustration sequence |
| p96 | 333K | 1163px | Early illustration |

### Teil 2
| Page | Size | Width | Notes |
|------|------|-------|-------|
| **p873** | **373K** | **1500px** | **Largest in Teil 2** — full-width plate |
| p37 | 353K | 1182px | Early illustration |
| p169 | 350K | 1201px | Mid-volume engraving |
| p926-p988 | **cluster (344-351K)** | 1139-1201px | **7+ plates** in the final ~60 pages — major illustration section |
| p928 | 347K | 1139px | Part of end-sequence |

## Structural Pattern
The pattern suggests **5-6 major sections per volume**, marked by:
1. A small/transitional page (77-130K)
2. Sometimes followed by a cluster of small pages (910-912 in T2)
3. Key plates appear near section boundaries

Volume-end narrow pages (p1113-1114 in T1, p1023-1024 in T2) use a different format — possibly foldout diagrams, catch-all appendices, or damaged leaf replacements.

## Section Hypothesis

### Teil 1 (~7 sections)
1. **p1-p10**: Preliminary — title, preface, dedication
2. **p11-p188**: Opening section — textual foundation, maybe Books I-II
3. **p189-p218**: Section transition — **p218 (85K)** likely a part/book title page
4. **p219-p477**: Core section — architecture & geometry, culminating in **p477 plate (451K)** — the sunflower/heliotrope diagram
5. **p478-p618**: Continuation — culminating in **p617 plate**
6. **p619-p1081**: Long final section — ending with **p1081/p1083 plates** (gematria, constraint-satisfaction)
7. **p1082-p1115**: Closing — including narrow foldouts (p1113-1114)

### Teil 2 (~5-6 sections)
1. **p1-p37**: Opening — title, **p37 plate**
2. **p38-p169**: Early section — **p169 plate**
3. **p170-p873**: Long middle section — culminating in **p873 plate (373K)** — likely the gematric/Revelation mapping
4. **p874-p912**: Section transition — **3-page cluster (p910-912)** — major division
5. **p913-p1016**: Final section — **plate cluster p926-p988 (7+ plates)** — the closing illustrations/tables
6. **p1017-p1025**: Closing — narrow format pages (p1023-1024)

## For OCR Pipeline
- **No text layer** — must render to image then OCR
- Every page is RGB JPEG at ~1150×1500px
- Tesseract deu+lat struggles with Fraktur — GPT-4-mini vision-OCR is the viable path
- ~2,140 pages total, ~550MB of image data
- OCR priority: start with section-transition pages (small files ≈ simple text pages) for calibration, then the large illustration pages (plates need special handling)

## Visual Verification Needed
I don't have a working vision model on this session — can't show you the actual page images. The section divisions above are inferred from image-size statistics. Visual spot-check of p218 (T1 transition), p477 (T1 plate), p910-912 (T2 transition), p873 (T2 plate) would confirm or correct the section boundaries.
