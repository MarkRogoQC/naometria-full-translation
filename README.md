# Naometria — Complete Release

> **Naometria, seu Nuda et Prima Libri Intus et Foris**
> Simon Studion · 1604 · inter Scorpiones
> Two volumes · 2,140 manuscript pages · Early New High German + Latin

---

## What Is This?

Naometria is a prophetic-chronological manuscript written around 1604 by Simon Studion, a Württemberg scholar and member of the Scorpiones — an esoteric fraternity of reformers within the Lutheran church. The work applies Hebrew gematria (numerical letter-values), calendar computations, and scriptural exegesis to decode biblical prophecy, predicting the fall of the dual Antichrist (Papal Rome and the Ottoman Empire) through a system of numerical correspondences.

This release contains a full-page AI-OCR transcription, English translations of readable text, and AI visual descriptions for pages where OCR was impossible (damaged pages, illustrations, diagrams).

The original manuscript is held by the Württembergische Landesbibliothek Stuttgart and available as a free digital facsimile:

**Source:** https://digital.wlb-stuttgart.de/sammlungen/sammlungsliste/werksansicht?tx_dlf%5Bid%5D=5049

---

## File Structure

```
naometria_release/
├── README.md                          ← You are here
├── navigation_index.md                ← Section-by-section guide to all 2,140 pages
│
├── (manuscript PDFs at digital.wlb-stuttgart.de)
│
├── raw_text/                          ← Page-by-page AI-OCR transcription
│   ├── teil1/                         1,115 .txt files (one per page)
│   └── teil2/                         1,025 .txt files
│
├── translation/                       ← English translations + original text
│   ├── v1_*.md                        10 files covering Volume 1
│   └── v2_*.md                        4 files covering Volume 2
│       Each file: ## Translation (English) + ## Original Text (Latin/ENHG)
│
├── compiled/                          ← Combined outputs for reading/searching
│   ├── naometria_translated_complete.txt   All translations concatenated
│   └── naometria_complete.txt             Structured OCR + visual descriptions
│
├── visual_descriptions/               ← AI page descriptions for blocked pages
│   ├── image_pages_catalog.md          Complete catalog of all image/plate pages
│   └── blocked_page_analysis/          46 AI analysis + neutral descriptions
│
└── reference/                         ← Study aids and indices
    ├── alphabetical_index_cleaned.md   2,703-entry Latin/German subject index
    ├── gematria_guide.md               How to decode the index & gematric system
    ├── name_gematria_catalog.md         Key figures with gematric breakdowns
    ├── naometria_skeleton_key.md        Condensed reference: numbers, dates, symbols
    ├── naometria_structure.md           Manuscript structure & section analysis
    ├── naometria_study_guide.md         Study orientation & approach
    ├── scripture_cross_reference.md     Biblical source passages
    ├── complete_timeline.md             Chronological events & correspondences
    ├── index_garbled_resolution.md      OCR issues in the index & fixes
    ├── naometric_calculator_data.md     Gematric calculator reference data
    ├── studion_content_notes.md          Thematic notes by page range (58+ pages)
    ├── naometria_operations.py          Core library: gematria, resolutio, divisio, contradictio
    ├── naometria_operations_guide.md     User guide for the operations library
    ├── naometria_pipeline.py            Batch CLI tool: full index processing + single-name decomposition
    ├── naometria_pipeline_output.csv     2,700 index entries processed through all three operations
    └── naometria_pipeline_summary.txt    Band frequency distributions
```

---

## Quick Start

### I just want to browse the book
→ Open `compiled/naometria_translated_complete.txt` — all English translations in one file. Use `navigation_index.md` to find your way around.

### I want to see what a specific page looks like
→ Download the free digital facsimile from Württembergische Landesbibliothek Stuttgart:
   https://digital.wlb-stuttgart.de/sammlungen/sammlungsliste/werksansicht?tx_dlf%5Bid%5D=5049

### I want to search for a person/place/topic
→ Check `reference/alphabetical_index_cleaned.md` — 2,703 indexed subjects with page numbers. Then use `reference/gematria_guide.md` to understand the gematric annotations.

### I want to understand Studion's numerical system
→ Start with `reference/naometria_skeleton_key.md` (the condensed guide), then `reference/gematria_guide.md` (how the index works), then `reference/name_gematria_catalog.md` (detailed breakdowns for key figures).

### I want to run Studion's gematria on names
→ `cd reference && python3 naometria_pipeline.py "Martinus Lutherus"` — single name. Or run the full batch with `python3 naometria_pipeline.py`. See `naometria_operations_guide.md` for details.

### I want to see the illustrations and diagrams
→ Open `visual_descriptions/image_pages_catalog.md` — all 20+ image/plate pages catalogued with descriptions. The ⬛ markers in `navigation_index.md` show where they are in context.

### I want the raw unfiltered source
→ The original manuscript is available from Württembergische Landesbibliothek Stuttgart (see above for the link). `raw_text/` contains the AI-OCR transcriptions.

---

## What's Included vs What's Not

**Included:**
- Page-by-page AI-OCR transcription of all 2,140 pages
- Human English translations of all readable text (∼1,800+ pages)
- AI-generated visual descriptions for 25 image pages (12 Volume 1: damaged text, diagrams, plates; 13 Volume 2: musical notation pages 900-912)
- Full alphabetical index of subjects, names, and places
- Gematric decoder with operation guide
- Character catalog (key prophetic figures)
- Scripture cross-references
- Structural survey of section divisions
- Study guide

**Not included:**
- Full English translations for the 25 image pages (visual descriptions provided instead)
- Polished modern-English translations (these are scholarly-literal translations preserving 1604 syntax)

---

## About the Translation Files

Each `translation/v*_p*.md` file contains two sections:

```
## Translation
[Page 9]
NAOMETRIA OR, Nüida, and first of the book within, and outside...
(English translation of each page)

## Original Text
[Page 9]
NAOMETRIA SEV Nüida, et prima Libri intus, & foris...
(Original Latin/Early New High German text)
```

**Blocked pages** (image-only pages where OCR failed) have a `[Page X]` marker in the Original Text section with an AI-generated visual description of what the page looks like. These are marked with ⬛ in the navigation index.

---

## Known Limitations

- **OCR quality:** AI vision-OCR from 1604 Fraktur/Latin manuscript at 140-150ppi. Handwritten pages and heavily damaged areas may have errors. The `raw_text/` preserves the raw output.
- **Translation style:** Literal/scholarly — maintains 1604 syntax. Not modernized English prose.
- **Music pages:** Volume 2 pages 900-912 contain musical notation with embedded text — visual descriptions provided for all 13 pages.
- **25 image pages:** V1 pages 47, 155, 225, 232, 275, 325, 477, 617, 937, 1025, 1081, 1083 + V2 pages 900-912. Visual descriptions are the best available content. See `visual_descriptions/image_pages_catalog.md` for details.
- **Pipeline coverage:** The gematria pipeline processes 2,700 of 2,703 index entries (99.9%). 3 entries are truncated note artifacts.
- **Gematria:** Studion's system is arcane and internally consistent but built on his own prophetic-calendrical framework. The `gematria_guide.md` explains operations; it does not validate claims.
- **Page numbering:** The WLB Stuttgart PDF page numbers differ slightly from the manuscript's original foliation in some sections. The PDF page numbers are the authoritative reference.

---

## Credits

- **Author:** Simon Studion (1543–1605), inter Scorpiones
- **Manuscript:** Württembergische Landesbibliothek Stuttgart, Cod.theol.et.phil.qt.23a-b
- **Digital facsimile:** https://digital.wlb-stuttgart.de/sammlungen/sammlungsliste/werksansicht?tx_dlf%5Bid%5D=5049
- **OCR, Translation & Visual Descriptions:** AI-assisted
- **Compilation:** 2026

---

## License

This manuscript is in the public domain (1604). The OCR and translations in this release are provided for educational and research purposes. Free to use, share, and adapt with attribution.

---

Generated: 2026-07-17 12:40 BST
