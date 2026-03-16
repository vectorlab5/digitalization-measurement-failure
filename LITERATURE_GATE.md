# Literature search & quality gate (Phase 5)

**Target**: PASS before starting full writing. See ideation §12.

---

## 1. Search execution log

| Keyword / query | Source | Hits (approx.) | In BibTeX | PDF in example_papers |
|-----------------|--------|-----------------|-----------|------------------------|
| enterprise digitalization environmental performance | Web/Scholar | — | 3+ | 0 |
| digitalization green TFP China | Web/Scholar | — | 2+ | 0 |
| environmental regulation firm digitalization | Web/Scholar | — | 3+ | 0 |
| JEEM firm pollution regulation | Web/Scholar | — | 0 | 0 |
| instrumental variable pollution TFP | Web/Scholar | — | 1+ | 0 |

*Update after each search batch.*

---

## 2. Example papers (blocking)

**Requirement**: ≥5 PDFs in `example_papers/`, including JEEM ≥3, theory/methods ≥1 each.

**Suggested list**: See **`refs/EXAMPLE_PAPERS_TO_DOWNLOAD.md`** (from your ScienceDirect .bib files). Minimum set: WANG201854, SHI2018187, BENATTI2024102995 (JEEM), WANG2026128596 (digital + green), XUE2025108398 (digital + GTFP).

| # | File name | Journal / type | Status |
|---|-----------|----------------|--------|
| 1 | (empty) | JEEM | ⬜ To download |
| 2 | (empty) | JEEM | ⬜ To download |
| 3 | (empty) | JEEM | ⬜ To download |
| 4 | (empty) | Theory/methods or digital+env | ⬜ To download |
| 5 | (empty) | Methods/empirical | ⬜ To download |

**Action**: Download from DTU FindIt / ScienceDirect (URLs in refs/*.bib). Name: `AuthorLastName_Year_ShortTitle.pdf`.

---

## 3. BibTeX counts

**Note:** You have 6 ScienceDirect .bib files in `refs/` (100+ entries total). Merge into `references.bib` at project root, then run reference-validator.

| Category | Minimum | Current | Status |
|----------|---------|---------|--------|
| Total entries (refs/*.bib merged) | 50 | 100+ in refs/ | ✅ Merge to references.bib |
| Theory | 12 | Many (Porter, institutional, etc.) | ⬜ Check after merge |
| Empirical / methods | 20 | Many | ⬜ Check after merge |
| Last 3 years | 12 | Many 2024–2026 | ⬜ Check after merge |
| JEEM papers | 6 | 20+ in refs/ | ✅ |
| All have abstract | 100% | Most have abstract | ⬜ Fill missing |

---

## 4. Quality gate result

- [ ] Example papers: ≥5 PDF (JEEM ≥3)
- [ ] references.bib: ≥50 entries
- [ ] Theory ≥12, Empirical/methods ≥20, Recent ≥12, JEEM ≥6
- [ ] All entries have abstract (or note “to add”)

**Result**: ❌ FAIL (do not start writing until PASS)

**Next actions**:
1. Run more searches (Google Scholar, Semantic Scholar, JEEM site) for digitalization, environmental performance, GTFP, regulation, IV.
2. Add BibTeX to `references.bib` (with abstracts where possible).
3. Download ≥5 example papers into `example_papers/`.
4. Re-run this checklist until PASS.
5. Before submission: run `reference-validator` on `references.bib`.
