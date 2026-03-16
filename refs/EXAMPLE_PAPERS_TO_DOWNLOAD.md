# Example papers to download (for `example_papers/`)

**Requirement (ideation §12.2):** ≥5 PDFs total; **JEEM ≥3**, theory/methods ≥1 each.

Below are **prioritized suggestions** from your ScienceDirect .bib files in `refs/`. Download via DTU FindIt / ScienceDirect and save as `AuthorLastName_Year_ShortTitle.pdf` in `**example_papers/`**.

---

## 1. JEEM papers (download at least 3)


| #   | Bib key               | Title                                                                                                  | Why download                                                                               |
| --- | --------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| 1   | **WANG201854**        | Environmental regulation, emissions and productivity: Evidence from Chinese COD-emitting manufacturers | JEEM 2018; **regulation + emissions + productivity**, China; direct precedent for your RQ. |
| 2   | **SHI2018187**        | Environmental regulation and firm exports: Evidence from the eleventh Five-Year Plan in China          | JEEM 2018; **regulation + firm behavior**, China; identification (policy variation).       |
| 3   | **SEMRAU2026103324**  | Upstreamness, foreign environmental regulation and CO2 emissions in Indian manufacturing firms         | JEEM 2026; **firm-level CO2**, GVC, regulation; recent JEEM style.                         |
| 4   | **BENATTI2024102995** | Environmental regulation and productivity growth in the euro area: Testing the Porter hypothesis       | JEEM 2024; **regulation + productivity**, Porter hypothesis; theory + empirics.            |
| 5   | **ALBRIZIO2017209**   | Environmental policies and productivity growth: Evidence across industries and firms                   | JEEM 2017; **policy stringency + productivity**; methods (panel, heterogeneity).           |
| 6   | **WANG2026103314**    | Consumer response to environmental standards: Evidence from gasoline regulation in China               | JEEM 2026; **environmental standards**, China; identification (boundary design).           |


**Suggested first 3:** WANG201854, SHI2018187, BENATTI2024102995 (regulation + firm + productivity; China + Europe).

---

## 2. Digitalization + environmental performance / GTFP (empirical & close to your topic)


| #   | Bib key             | Title                                                                                              | Journal                                      | Why download                                                                                                                                          |
| --- | ------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **WANG2026128596**  | Integrating Environmental Management into the Digital Economy and Green Development of Enterprises | J. Environmental Management 2026             | **Digital economy + green development**, mechanism (green tech innovation, green management innovation), GTFP.                                        |
| 2   | **ZHANG2026116098** | Digitalization and supplier environmental performance: An institutional perspective                | J. Business Research 2026                    | **Digitalization → environmental performance**, institutional theory; dyadic panel, China.                                                            |
| 3   | **XUE2025108398**   | Digital transformation of energy enterprises, ESG performance, and green total factor productivity | Finance Research Letters 2025                | **Digital transformation + ESG + GTFP**; energy firms, mechanism (ESG).                                                                               |
| 4   | **NAZIR2026100029** | Improving environmental performance in manufacturing through sustainability with digitalization    | Sustainable Cities and Society Advances 2026 | **Digital technologies + sustainability → environmental performance**; mediation (supply chain collaboration), moderation (env. regulation pressure). |
| 5   | **LU2026105596**    | Greening to grow: Evidence from environmental regulation and industrial firm productivity in China | J. Public Economics 2026                     | **Environmental regulation + firm productivity**; heterogeneity (pollution intensity), mechanisms (selection, reallocation, upgrading).               |


**Suggested:** WANG2026128596, ZHANG2026116098, XUE2025108398 (digital + env/GTFP; use for Theory and Related work).

---

## 3. Theory / methods (at least 1)


| #   | Bib key               | Title                                                                                              | Journal                  | Why download                                                                                       |
| --- | --------------------- | -------------------------------------------------------------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------- |
| 1   | **BENATTI2024102995** | Environmental regulation and productivity growth in the euro area: Testing the Porter hypothesis   | JEEM 2024                | Porter hypothesis; panel local projections; firm-level emissions.                                  |
| 2   | **ALBRIZIO2017209**   | Environmental policies and productivity growth: Evidence across industries and firms               | JEEM 2017                | EPS index, industry/firm heterogeneity; methods reference.                                         |
| 3   | **LU2026105596**      | Greening to grow: Evidence from environmental regulation and industrial firm productivity in China | J. Public Economics 2026 | Identification (geographic × industry intensity); mechanisms (selection, reallocation, upgrading). |


---

## 4. Minimum set to reach “≥5 PDFs, JEEM ≥3”

1. **WANG201854** (JEEM 2018) – regulation, emissions, productivity, China
2. **SHI2018187** (JEEM 2018) – regulation, firm exports, China
3. **BENATTI2024102995** (JEEM 2024) – Porter hypothesis, productivity
4. **WANG2026128596** (J. Env. Mgmt 2026) – digital economy, green development, GTFP
5. **XUE2025108398** (Finance Res. Letters 2025) – digital transformation, ESG, GTFP

Optional 6th: **ZHANG2026116098** (digitalization, supplier environmental performance, institutional theory).

---

## 5. Where to get PDFs

- **ScienceDirect/Elsevier:** Use the `url` in each .bib file (e.g. `https://www.sciencedirect.com/science/article/pii/S0095069617305028` for WANG201854).  
- **DTU FindIt:** [https://findit.dtu.dk/](https://findit.dtu.dk/) → search by title or DOI; download “covered by DTU” if available.  
- Save in `**example_papers/`** with names like:  
`Wang_2018_EnvironmentalRegulationEmissionsProductivity.pdf`,  
`Shi_2018_EnvironmentalRegulationFirmExports.pdf`,  
`Benatti_2024_PorterHypothesisProductivity.pdf`,  
`Wang_2026_DigitalEconomyGreenDevelopmentEnterprises.pdf`,  
`Xue_2025_DigitalTransformationESGGTFP.pdf`.

---

## 6. Your .bib files in `refs/`

- `ScienceDirect_citations_1773511012467.bib` – digital transformation, tourism, ESG, green development  
- `ScienceDirect_citations_1773511040580.bib` – environmental performance, governance, digitalization  
- `ScienceDirect_citations_1773511064280.bib` – GTFP, digital finance, green bonds, AI & GTFP  
- `ScienceDirect_citations_1773511083541.bib` – regulation, data governance, JEEM (Semrau, Wang), firm productivity  
- `ScienceDirect_citations_1773511132976.bib` – **many JEEM** (regulation, exports, productivity, leakage, etc.)  
- `ScienceDirect_citations_1773511157228.bib` – **JEEM** (water stress & productivity, Porter, policies & productivity)

Consider merging these into a single `**references.bib`** at project root and running **reference-validator** before submission.