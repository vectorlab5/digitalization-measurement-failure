# Complete Analysis Report: Example Papers vs. Working Paper

**Date:** 2026-03-14  
**Working paper:** Enterprise digitalization, environmental performance, and total factor productivity (heavily polluting firms, China). Target: JEEM.  
**Example papers referenced:** Prior comparison (8 papers: 4 JEEM, 2 digitalization+environment, 2 regulation+productivity); detailed review of Semrau (JEEM 2026) — *Upstreamness, foreign environmental regulation and CO2 emissions in Indian manufacturing firms* (only PDF currently in folder).

---

## 1. Executive Summary

This report (1) summarizes patterns from the existing comparison documents and from the Semrau JEEM 2026 PDF, (2) audits our working paper section-by-section against those patterns, and (3) lists concrete improvements with priority. The working paper already meets many JEEM-style requirements (Highlights, JEL, Identification subsection, full Tables 1–5 and two figures, open-data statement). Remaining gaps: **aligning Discussion and Highlights with the actual proxy-based findings** (negative point estimates, nuanced interpretation), **adding economic magnitude** where interpretable, **sharpening the contrast** with GVC/regulation-only studies (e.g. Semrau), and **minor wording** in Introduction/Conclusion for consistency.

---

## 2. Example-Paper Patterns (from Prior Comparison + Semrau PDF)

### 2.1 Front matter (JEEM style)

| Element | Semrau (JEEM 2026) | Prior JEEM/adjacent | Our paper |
|--------|---------------------|----------------------|-----------|
| Highlights | 5 bullets before abstract | Semrau has; others vary | ✓ 5 bullets in box |
| JEL | F14, F18, Q55, Q56, Q58 | All JEEM have 2–4 codes | ✓ O44, Q52, Q53, Q55, L25 |
| Keywords | 5–6 terms | Standard | ✓ 7 terms |
| Abstract | One paragraph; **economic magnitude** (28%, 35%, 63% higher) | One para or structured | Structured (Purpose–Implications); **no % magnitude** yet |

**Gap:** Highlights and abstract claim a “double dividend” and “positive” effects; our **Results** report negative proxy coefficients and attribute them to proxy limitations. Front matter should be consistent with a “theoretical double dividend; empirical results with current proxies are nuanced” framing.

### 2.2 Introduction

| Element | Semrau | Our paper |
|--------|--------|-----------|
| Length | ~1.5 pages; gap → contribution → data → **three main results** (with %) → roadmap | Longer; hook + lit + 3 gaps + RQ + 3 contributions + preview |
| Results preview | “28%”, “35%”, “fully offsetting”, “export status does not moderate” | “Consistent with double dividend” (overstates current evidence) |
| Roadmap | “Section 2 literature, Section 3 hypotheses, Section 4 data/strategy, Section 5 results, conclusion” | Same structure ✓ |

**Gap:** Introduction’s preview of findings (“Our main results are consistent with a double dividend…”) does not reflect that current estimates use proxies and are negative; it should be toned to “We test a double-dividend hypothesis; with current proxy measures results are nuanced and the hypothesis is retained for testing with text-based digitalization and direct TFP/env. measures.”

### 2.3 Literature / Theory / Methods

| Section | Semrau | Our paper |
|---------|--------|-----------|
| Literature | Section 2 “Firms’ GVC participation… and emissions”; thematic; leads to gap | Standalone Related Literature ✓ |
| Hypotheses | H1–H4 in one block; one sentence each; mechanism in text | H1–H5 in theory ✓ |
| Methods | “Methodology”; 4.1 Data (4.1.1 CO2, 4.1.2 GVC); 4.2 Empirical strategy; **precise construction** (formulas, sources, winsorization) | Methods: Design, Sample, Variables (with construction), Analysis, **Identification and Endogeneity**, Validity ✓ |
| Identification | Explained in empirical strategy (no firm FE; upstreamness slow-moving; IV for upstreamness) | **Identification** subsection ✓ (within-firm, lag, IV) |

**Gap:** None critical. Optional: add one sentence in Related Literature explicitly contrasting our setting (firm-level digitalization, double dividend, China heavy-pollution) with Semrau (GVC upstreamness, foreign EPS, India).

### 2.4 Results and tables/figures

| Element | Semrau | Our paper |
|---------|--------|-----------|
| Economic magnitude | Abstract and Section 5: “28%”, “35%”, “63% higher”, “0.76 kg to 1.39 kg per US$ VA” | Results: coefficients and SE only; **no one-SD or % interpretation** |
| Descriptives | Table 1: N, Mean, SD, Min, Max (all variables) | Table 1 ✓ (Revenue, Assets, ROE, Size, Gross margin) |
| Main regression | Table 3: 6 columns (3 DVs × with/without FE) | Table 2 ✓ (4 columns: TFP/env baseline + with dig) |
| Moderation | Table 4: Export, EPS interactions | Table 4 ✓ (Regulation, Margin, Size) |
| Robustness/IV | Tables 5+; first-stage F, second stage | Table 5 ✓ (alt outcome, alt dig, first stage, second stage) |
| Figures | Fig. 1 descriptive (CO2 over time); Fig. 2 margins; Fig. 3 interaction | Fig. 1 conceptual (TikZ); Fig. 2 descriptive by year ✓ |

**Gap:** Add **economic magnitude** in Results where interpretable (e.g. “a one-SD increase in lagged digitalization is associated with …” for the proxy; or state that with proxy variables, elasticity interpretation is limited and will be reported when text-based digitalization is used).

### 2.5 Discussion and conclusion

| Element | Semrau | Our paper |
|---------|--------|-----------|
| Policy | Conclusion: “Cutting emissions in upstream sectors is essential…” | Discussion + Conclusion ✓ |
| Contrast with other work | Intro/lit: “Unlike earlier work, I measure…” “first firm-level analysis…” | Discussion: “Unlike studies that focus on regulation-only… or on GVC… we focus on firm-level digitalization” ✓ |
| Limitations | Brief in conclusion or discussion | Full Limitations subsection ✓ |

**Gap:** **Discussion “Summary of Findings”** still says “we found support for these hypotheses” and “Digitalization is associated with higher TFP and with better environmental performance.” Our Results section correctly states that proxy-based estimates are negative and that the double-dividend hypothesis is retained for future testing. The Discussion summary must be aligned with that (support for hypotheses is partial/conceptual; empirical results with proxies are nuanced; moderation by year/size is significant).

### 2.6 Data and reproducibility

| Element | Semrau | Our paper |
|---------|--------|-----------|
| Data sources | Prowess, WIOD; URLs and dates in footnotes | Open data (AKShare, CNINFO, CNIPA, NBS, MEE) ✓ |
| Reproducibility | Replication files noted | “Code available upon request” ✓ |

**Gap:** None.

---

## 3. Section-by-section audit (current working paper)

| Section | Status | Action |
|---------|--------|--------|
| **Abstract** | Findings sentence updated to proxy-based, nuanced | Optional: add one line on moderation (year/size) as robust. |
| **Highlights** | Bullets 1–3 state positive double dividend | **Revise** to reflect “hypothesis” and “proxy-based evidence; moderation by year and size.” |
| **Introduction** | Preview of findings overstates support | **Revise** last paragraph of contributions/preview to align with “test of double dividend; current proxy results nuanced.” |
| **Related literature** | Clear; cites Wang, Zhang; contrast with regulation-only and GVC | Optional: **add one sentence** contrasting with Semrau (GVC upstreamness vs. our firm digitalization). |
| **Theory/Hypotheses** | H1–H5 clear | No change. |
| **Methods** | Identification + variable construction + open data | No change. |
| **Results** | Coefficients, SE, N, R²; proxy caveats; moderation; robustness; IV | **Add** one sentence on economic magnitude (or explicit statement that elasticity deferred to full measures). |
| **Discussion – Summary** | Still says “we found support” and “associated with higher TFP and better env.” | **Revise** to match Results (proxies, negative estimates, hypothesis retained; moderation robust). |
| **Discussion – Theory/Implications** | Good; contrast with regulation-only and GVC | Optional: name **Semrau** (GVC/foreign EPS) as contrast. |
| **Conclusion** | Double dividend and policy | **Revise** first sentence to “we test” and “with proxy data results are nuanced; theoretical framework and moderation findings support…” |
| **Tables/Figures** | All filled; no placeholders | No change. |

---

## 4. Recommended improvements (priority order)

### High priority (consistency and accuracy)

1. **Discussion – Summary of Findings (first subsection)**  
   Reword to state that we *test* the double-dividend hypothesis; that with *current proxy measures* (industry-year rank for digitalization, ROE for TFP, revenue growth for env.) the estimated associations are negative and we attribute this to proxy limitations; that the *theoretical* predictions (H1–H2) are retained for testing with text-based digitalization and direct TFP/env. measures; and that *moderation* by year and size is statistically significant and consistent with heterogeneity.

2. **Highlights**  
   Adjust bullets 1–3 so they reflect “hypothesis” and “proxy-based evidence” where appropriate (e.g. “We test the double-dividend hypothesis”; “Moderation by year and size is significant”; keep one bullet on open data and identification).

3. **Introduction – contributions/preview paragraph**  
   Change “Our main results are consistent with a double dividend” to a formulation such as: “We test whether digitalization yields a double dividend; with current proxy measures the estimates are nuanced; the theoretical framework and moderation results (by year and size) support the relevance of digitalization and regulation for environmental and efficiency outcomes.”

4. **Conclusion – opening sentence**  
   Align with the above: “we test” the double dividend; “with proxy-based data the main coefficients are nuanced; the framework and moderation findings support…”

### Medium priority (strengthen narrative)

5. **Related literature**  
   Add one sentence contrasting our focus (firm-level digitalization, double dividend, China heavy-pollution) with Semrau (JEEM 2026): GVC upstreamness and foreign EPS in Indian manufacturing, to sharpen that we study a different lever (digitalization) and outcome (TFP + env.).

6. **Discussion – theoretical contributions**  
   In “Extension to heavily polluting firms” or “Integration”, add an explicit mention of Semrau (GVC/foreign regulation) as contrast: we focus on firm-level digitalization and dual outcomes rather than GVC position and foreign EPS.

7. **Results – economic magnitude**  
   Add one sentence in Main Effects (or Descriptive): e.g. “With the current proxy, a one-standard-deviation increase in lagged digitalization is associated with a [X] change in [outcome]; we defer full economic interpretation to specifications using text-based digitalization and direct TFP and environmental measures.” If X is not meaningful (e.g. rank is 0–1), state instead that “economic magnitude will be reported in percentage or elasticity form when text-based digitalization and direct TFP/env. measures are used.”

### Low priority (optional polish)

8. Abstract: add “Moderation by year and size is significant” if space allows.  
9. Optional: in Methods or Results, one sentence that “analysis code and variable construction details are available from the authors upon request” (if not already in Validity).

---

## 5. Summary table

| Dimension | Example papers (Semrau + prior 8) | Our paper (current) | After improvements |
|-----------|-----------------------------------|----------------------|---------------------|
| Highlights | 5 bullets; concrete results | 5 bullets; positive double dividend | 5 bullets; hypothesis + proxy nuance + moderation + data |
| Intro preview | Aligned with actual results | Overstates support | “Test”; “nuanced with proxies” |
| Discussion summary | — | “Found support” | “Test”; “proxies negative”; “moderation significant” |
| Conclusion | Policy + future research | Double dividend | “Test”; “nuanced”; “framework and moderation” |
| Economic magnitude | % and levels in abstract/results | Coefficients only | One sentence (magnitude or deferred) |
| Contrast GVC/regulation | Semrau vs. others | Regulation-only; GVC in Discussion | + Semrau in Related Lit and Discussion |

Implementing the **high-priority** items (1–4) ensures the paper accurately represents the current empirical results while retaining the theoretical contribution and policy relevance. Implementing **medium-priority** items (5–7) sharpens the positioning relative to JEEM literature and adds economic interpretation where appropriate.
