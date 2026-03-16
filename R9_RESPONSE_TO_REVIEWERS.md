# Response to Reviewers (Round 9–style rejection)

**Use this when:** (1) Submitting to a journal that welcomes methodological notes / commentaries, or (2) Responding to a "Reject" or "Reject and resubmit" that raises audit size, mechanical relationship, or lack of methodological innovation.

---

## To the Editor

Thank you for the opportunity to submit our manuscript and for the reviewers’ time. We have read the reports carefully. Below we respond to the major concerns and clarify the scope and contribution of the paper. We believe the manuscript is suitable for publication as a **methodological note or commentary** in a journal that values measurement transparency and replication.

---

## Response to Major Concerns

### MC1: Limited scope of the literature audit (24 studies)

**Reviewer concern:** The audit includes only 24 studies; without initial hit counts and exclusion numbers, the claim that the problem is “prevalent” is insufficiently supported.

**Our response:** We agree that a larger audit (e.g., 100+ studies) and a full PRISMA report with exact hit and exclusion counts at each stage would strengthen generalizability. We have now made this explicit in the manuscript (Section 2): we describe what a full PRISMA-style report would contain (initial hits per database, deduplication, screening exclusions with reasons, full-text exclusions) and state that we report the screening flow and inclusion criteria in full so that **replication or extension to 100+ studies can be performed**. We do not claim that 24 is representative of the entire field; we claim that **within this audited set**, 83% use at least one revenue-related or accounting-based proxy, and we invite others to extend the audit. We are happy to expand the audit in a revision if the editor considers it essential; our current contribution is to document the screening structure and prevalence in this initial set.

**Changes in manuscript:** Related Literature now states explicitly what a full PRISMA report would list and that we report the flow and criteria for reproducibility and future extension.

---

### MC2: Empirical illustration demonstrates a mechanical relationship

**Reviewer concern:** Because both regressor and outcome are revenue-derived, the correlation is mechanically expected; the paper does not show that proxy-based designs mislead when the outcome is not revenue-based.

**Our response:** We agree that our illustration is deliberately mechanical: we use revenue rank, revenue growth, and ln(revenue) precisely to show that **when** researchers use this common structure (as documented in the audit), they obtain significant associations that do not identify the digitalization–environment relationship. Our controlled experiment shows that even when true digitalization is **uncorrelated** with revenue, the same structure yields significant coefficients—so the pitfall is not merely “revenue correlates with revenue” but that **readers cannot distinguish** a true effect from same-source structure. We have added in the Discussion that we **acknowledge** that a demonstration using a **non–revenue-based outcome** (e.g., emission or GTFP where data are available) would further strengthen the critique, and we encourage such work. Our contribution is to document that the prevalent pattern in the audited literature uses revenue-based proxies for both sides and to show why that pattern is problematic.

**Changes in manuscript:** Discussion now explicitly acknowledges that our illustration uses revenue-based outcomes and that a non-revenue outcome demonstration would strengthen the critique; we encourage future work in that direction.

---

### MC3: Synthetic experiment adds limited insight

**Reviewer concern:** The DGP is deliberately simplified (random walk, no industry heterogeneity, etc.); the simulation mainly shows that revenue-derived variables correlate under minimal assumptions.

**Our response:** The minimal DGP is intentional: we isolate the **same-source mechanism** without confounding from richer structure. The point is that **even** this parsimonious design suffices to produce a significant proxy regression when both regressor and outcome are revenue-based—so the pitfall does not require complex dynamics to arise. We have stated in the Methods that richer DGPs (AR(1), industry heterogeneity) could be explored in future work and in the Limitations that the controlled experiment uses a minimal DGP. We believe the experiment usefully complements the audit and the empirical illustration by showing that the result is not specific to the Chinese firm sample.

**Changes in manuscript:** Methods and Limitations already state that the DGP is minimal by design and that alternative specifications could be explored in future work.

---

### MC4: Lack of methodological innovation

**Reviewer concern:** The paper does not propose a new estimator, identification strategy, or measurement framework; it identifies a problem without providing a methodological solution.

**Our response:** We frame our contribution explicitly as **methodological critique and clarification**, not as a new technical tool. We have added a short subsection in the Discussion (“Contribution in context”) that states: we do not propose a new estimator or diagnostic; we provide the first **structured audit** of proxy use in this literature, a **transparent illustration** and **controlled experiment** that demonstrate the pitfall, and a **blueprint** (target design, variable definitions, data requirements) for valid inference with direct measures. We argue that making an under-recognized pitfall visible and the remedy (direct measures) explicit is a valuable contribution to applied practice, especially in a field where many studies rely on the proxy structure we document. We are targeting journals that accept methodological notes and commentaries; we are happy to consider a different venue if the editor views the contribution as better suited to that format.

**Changes in manuscript:** Introduction and Discussion now state clearly that the contribution is critique and clarification; Discussion includes a “Contribution in context” paragraph that preempts the “no new tool” concern.

---

### MC5: Data integration (64 observations)

**Reviewer concern:** Only 64 observations have total assets after the merge; this limits the credibility of the empirical illustration.

**Our response:** We report this diagnostic transparently and explain that the drop is due to differing coverage between open sources (we verified identifier and calendar alignment). We have added that **commercial integrated databases** (e.g., CSMAR, WIND, RESSET) typically provide consistent identifiers and broader coverage; we use **open sources** for transparency and reproducibility and report the merge so that readers can assess data choices. Our regression sample uses size = ln(revenue) so that the main results do not depend on the 64-observation subset; the illustration remains informative for the purpose of showing proxy behavior under the same-source structure.

**Changes in manuscript:** Methods and Limitations already note commercial data alternatives and our choice of open data; we have kept this explicit.

---

## Response to Minor Comments

1. **Title:** The title specifies “Measurement Failure **from Revenue-Based Proxies**” so the scope is clear.
2. **Journal tier:** We did not classify by tier; we state this as a limitation and that a future audit could report prevalence by tier.
3. **Conceptual figure:** The caption states that the figure is for reference only and that the paper does not estimate or test the depicted links.
4. **2025–2026 citations:** We state in Limitations that some cited works are from 2025–2026 (early view or in press) and that we cite as of our search date.

---

## Recommendation

We request that the manuscript be considered for publication as a **methodological note or commentary**. We have strengthened the framing of the contribution (critique and clarification, with audit + illustration + blueprint), made the limits of the audit explicit (and the path to extension to 100+ studies clear), and acknowledged where a non–revenue outcome or a larger audit would add value. We believe the paper meets the standards of journals that publish methodological critiques and transparent replications; we are open to expanding the audit or adding a short replication appendix in a revision if the editor finds it necessary.

Thank you again for your consideration.
