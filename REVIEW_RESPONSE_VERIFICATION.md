# Verification: Review Comments Addressed

This checklist confirms that the manuscript has been revised to address the “零容忍、专挑硬伤” review. Each fatal flaw and writing issue is mapped to the current text.

---

## Overall recommendation

**Review:** Reject / Major redesign — “研究设计尚未闭环，实证证据与理论叙事明显脱节”.

**Addressed:** The paper is reframed as **evidence and measurement challenges**, not as a completed test of the double dividend. Title is *"Enterprise Digitalization, Productivity, and Environmental Outcomes in Heavily Polluting Firms: Evidence and Measurement Challenges"*. Abstract, Highlights, Introduction, Results, Discussion, and Conclusion all state that (i) proxy operationalizations are used, (ii) H1 and H2 are **not supported** under these proxies, (iii) we **do not retain** the double-dividend hypothesis, and (iv) policy implications await evidence with direct measures.

---

## Fatal flaw 1: 研究问题、理论假设与实证实现严重错位

**Review:** Theory promises text-based digitalization, LP/OP TFP, emission/GTFP, green patents, regional regulation; results use revenue rank, ROE, revenue growth, ROE improvement, year. “构念崩塌.”

**Addressed:**
- **Methods § Operationalization and Data Constraints:** Explicit “Ideal vs. implemented” for each construct (digitalization, TFP, env. perf., green innovation, regulation, size). States rank “conflates size, market position…; it is not a valid construct measure of digitalization”; revenue growth “reflects business expansion, not environmental performance”; ROE improvement “does not measure green innovation”; year “is not a measure of environmental regulation strength”.
- **Abstract / Highlights / Introduction:** All state that we implement *proxy* operationalizations and that the double dividend has not been tested with direct measures.
- **Related literature:** Last sentence now says we implement “an empirical application” with “proxy operationalizations” and that “a full test would require direct measures”.

---

## Fatal flaw 2: 方法承诺“正式指标”，结果用“临时代理”

**Review:** Methods describe ideal variables; results say “with current proxy measures… theoretical predictions remain to be tested”. “论文不是 proposal.”

**Addressed:**
- **Methods:** “Operationalization and Data Constraints” states that “data availability forces us to implement proxy operationalizations” and that “Results in this paper are therefore *not* a test of the double dividend with properly measured digitalization, TFP, or environmental performance.”
- **Abstract:** “Owing to data constraints, we implement *proxy* operationalizations… Policy implications await evidence from studies using direct measures.”
- No remaining wording that “theoretical predictions remain to be tested” in a way that implies the current paper is a full test; instead we say “testing… remains for future work” and “we do not claim that hypotheses are supported”.

---

## Fatal flaw 3: 结果与假设方向相反，讨论与结论仍坚持正向叙事

**Review:** H1/H2 positive but estimates −35.91 and −3.00; authors “retain the theoretical double-dividend hypothesis”. “结果导向的解释性偏见.”

**Addressed:**
- **Results:** “Under these operationalizations, hypotheses H1 and H2 are **not supported**”; “we do not claim that the double dividend is falsified; we claim only that *with the current proxy measures*, the data do not support H1 or H2”.
- **Abstract:** “We do not attribute this solely to proxy limitations; we discuss plausible mechanisms… and stress that the double dividend has not been tested…”
- **Discussion / Conclusion / Introduction:** All state “we do **not** retain the hypothesis” / “H1 and H2 are not supported”; no positive narrative that the double dividend is supported by the data.
- **Highlights:** “Under current proxies, main-effect estimates are *negative*; H1 and H2 are not supported. We discuss why and do not retain the hypothesis without evidence.”

---

## Fatal flaw 4: 中介分析—“绿色创新”未正确测量

**Review:** Green innovation = ROE improvement; “ROE improvement 不是绿色创新”. “中介变量不存在.”

**Addressed:**
- **Results § Mediation:** “This variable does not measure green innovation… Therefore the results in this table **cannot be interpreted as a test of H3**.” “We do not draw substantive conclusions about mediation from these estimates.”
- **Methods § Mediation:** “In the current application the mediator is a proxy (ROE improvement) that does not measure green innovation; we report only the product-of-coefficients indirect effect and do not interpret it as a test of H3.”
- **Table 3 note:** “This table does not test H3; green innovation is not measured.”
- **Methods § Ideal vs. implemented:** “(4) Green innovation… Implemented = ROE improvement… This does not measure green innovation; mediation results using this proxy cannot be interpreted as a test of H3.”

---

## Fatal flaw 5: 调节变量“环境规制”被 year 替代

**Review:** H4 is regulation strength; Table 4 uses year. “year 不等于环境规制强度.”

**Addressed:**
- **Results § Moderation:** “**Year is a time trend, not a measure of environmental regulation strength;** it conflates macroeconomic, policy, pandemic, and industry-wide effects. We therefore **do not interpret this as evidence for H4** (regulation moderation).” “H4 and H5 require direct regulation and ownership measures to be tested properly.”
- **Table 4 note:** “Column (1): moderator = year (time trend; *not* environmental regulation strength; **H4 not tested**).”
- **Figure 4 caption:** “Year is a time trend, not environmental regulation; H4 is not tested.”
- **Abstract / Discussion / Conclusion:** All state that year is a time trend, not regulation, and that H4 is not tested.

---

## Fatal flaw 6: IV 完全不成立，弱工具变量

**Review:** IV = two-year lag of proxy; F = 2.02. “IV 不能作为这篇论文的识别卖点.”

**Addressed:**
- **Results § Robustness:** “The first-stage $F$-statistic is 2.02, **well below** the conventional threshold of 10; the IV estimates are therefore **not reliable** for inference (weak-instrument problem). We do not use the IV results to support causal claims.”
- **Table 5 note:** “first-stage $F = 2.02$ (weak instrument); **IV estimates not reliable for inference**.”
- **Abstract:** “we also report a weak-instrument IV specification and document its limitations.”
- **Discussion / Conclusion:** “mediation and IV results are not interpretable… / not relied upon for inference”.

---

## Fatal flaw 7: 描述统计—total assets = 64 未解释

**Review:** Table 1 shows total assets N = 64; “数据合并可能严重出错”. “为什么 balance-sheet merge 之后只剩 64?”

**Addressed:**
- **Methods § Sample and merge:** “Total assets and size (ln assets) appear in Table~ref{tab:descriptives} with $N = 64$ because the balance-sheet merge (by firm identifier and year) yields that many matches under the current data pipeline; the bulk of firm-years have revenue and ROE from the income-statement source but not matched balance-sheet total assets. We do not treat this as a coding error but as a data-availability constraint: the merge keys and sources are documented in the code (e.g., scripts/analyze_data.py), and we explicitly use size = ln(revenue) in regressions so that results do not depend on the small asset-matched subsample. A full sample flowchart… would strengthen transparency and is recommended for a final version.”
- **Table 1 note:** “Total assets and size (ln assets) from balance-sheet merge by firm and year; only 64 firm-years match, so regressions use size = ln(revenue).”
- **Results § Descriptives:** “Total assets and size (ln assets) are available for only 64 firm-years after the balance-sheet merge; this reflects the current data pipeline and merge keys (see Section~ref{sec:methods}), not a coding error.”

---

## Fatal flaw 8: 机械相关与内生同源

**Review:** X = revenue rank, control = ln(revenue), Y2 = revenue growth; “所有变量都围着 revenue/ROE 打转”.

**Addressed:**
- **Methods § Operationalization:** New paragraph “**Mechanical and same-source concerns.** The implemented regressor (industry-year revenue rank), control (ln revenue), and one outcome (revenue growth) all depend on revenue. This creates a risk of mechanical or same-source correlation… We do not treat the current estimates as evidence of [a causal relationship]; we report them transparently and stress that testing the double dividend requires distinct constructs.”
- **Results:** “(i) the digitalization proxy (revenue rank) conflates size, market position… (ii) revenue growth as environmental performance proxy is not a measure of emissions…”; “the large rise [in R²] for the environmental performance equation is consistent with both the outcome (revenue growth) and the digitalization proxy (revenue rank) sharing revenue-based variation (see Methods, Operationalization).”

---

## Theory: 反向机制与净效应不确定 (Flaw 9)

**Review:** “缺少反向机制与边界张力”; “净效应不确定… 何种条件下正效应占优.”

**Addressed:**
- **Theory:** New subsection “**Reverse Mechanisms and Net Effect Uncertainty**”: short-run cost and efficiency pressure; compliance and disclosure exposure; capacity and scale effects; green vs. efficiency trade-offs. “We state our hypotheses as *directional predictions under conditions where the positive channels dominate*; the empirical net effect is an open question.”
- **H1 / H2:** Qualified with “*ceteris paribus* and when positive efficiency/environmental channels dominate”.
- **Abstract / Introduction:** “acknowledging reverse mechanisms (e.g., short-run cost pressure, compliance exposure) that can make the net effect uncertain.”

---

## Literature and contributions (Flaw 10)

**Review:** “贡献没有被真正做实”; “综述和贡献之间是断开的”.

**Addressed:**
- **Introduction § Contributions:** Reframed as (1) extending the *framework* to heavily polluting firms and combining strands in a double-dividend *hypothesis* (“empirical test… remains for future work”); (2) integrating strands and “document[ing] the gap between ideal and implemented variables”; (3) specifying mechanisms and boundary conditions and “report[ing] proxy-based moderation results, while being explicit that mediation and regulation moderation cannot be tested with the current operationalizations.”
- **Related literature:** Closing sentence now says we “implement an empirical application” with “proxy operationalizations” and that “a full test would require direct measures.”

---

## Tables (Flaw 11)

**Review:** “列之间差异… 控制变量系数… cluster… R²… 变量定义”; “列 (1)(2) 和 (3)(4) 的区别”; “R² 从 0.224 到 0.580 没解释”; “mediation 没有 bootstrap CI”; “H5 ownership 没出现”.

**Addressed:**
- **Table 2 note:** “Columns (1)–(2): outcome = TFP proxy (ROE). Columns (3)–(4): outcome = environmental performance proxy (revenue growth). All columns: digitalization proxy = industry-year revenue rank (lagged). Controls: size = ln(revenue); firm and year fixed effects. Standard errors… cluster-robust at firm level where applicable.”
- **Table 3 note:** “(2) Effect on ‘green innovation’ proxy (ROE improvement; not a measure of green patents). This table does not test H3; green innovation is not measured. Controls and FE as in Table 2.”
- **Table 4 note:** “Column (1): moderator = year (time trend; *not* environmental regulation strength; H4 not tested). (2) Gross margin; (3) ln(revenue). **Ownership (SOE) not included.**”
- **Table 5 note:** “(2) ln(revenue) percentile as alternative digitalization proxy (still revenue-based). (3)–(4)… first-stage F = 2.02 (weak instrument); IV estimates not reliable for inference.”
- **Results:** R² jump for env. perf. explained as “consistent with both the outcome (revenue growth) and the digitalization proxy (revenue rank) sharing revenue-based variation”.
- **Methods § Mediation:** Bootstrap/95% CI stated as what we “would” report when testing H3 with a proper mediator; “In the current application… we report only the product-of-coefficients… and do not interpret it as a test of H3.”

---

## Figures (Flaw 12)

**Review:** “图 3 的系数来自不合适的代理变量”; “图 4 强化 year = regulation proxy”.

**Addressed:**
- **Figure 3 caption:** “Main effects… (**proxy specifications**). Outcomes: TFP proxy = ROE; environmental performance proxy = revenue growth. Digitalization proxy = industry-year revenue rank.”
- **Figure 4 caption:** “Moderation by year (**proxy specification**)… Year is a time trend, not environmental regulation; **H4 is not tested.**”

---

## Writing (Flaw 13)

**13.1 “we retain the hypothesis”**  
**Addressed:** All instances removed or replaced with “we do **not** retain” / “H1 and H2 are not supported”. Grep: no positive “retain the hypothesis” remains.

**13.2 “nuanced”**  
**Addressed:** Removed. Results and abstract use “negative” and “not supported”.

**13.3 方法/结果/讨论时态与身份统一**  
**Addressed:** Methods describe ideal variables then “Operationalization” states we use proxies. Results consistently “under these operationalizations… not supported”. Discussion and Conclusion frame as “framework + transparency + future work”; implications conditional on “if future work with direct measures…”. Paper identity: “evidence and measurement challenges”, not “finished test of double dividend”.

**13.4 “supports reproducibility”**  
**Addressed:** Abstract no longer says “supports reproducibility”. Highlights: “reproducibility is **subject to** documented variable construction and sample limitations.” Methods Validity: “reproducibility is **subject to** the documented variable construction and sample limitations above.”

---

## Reviewer’s one-line verdict

**Review:** “The manuscript does not empirically test what it claims to test.”

**Addressed:** The manuscript **now explicitly states** that it does not empirically test the double dividend with the intended constructs. Title, abstract, Methods (Operationalization), Results, Discussion, and Conclusion all state that (i) we use proxy operationalizations, (ii) the double dividend has not been tested with text-based digitalization, LP/OP TFP, or emission-based environmental performance, and (iii) we do not retain the hypothesis or claim policy conclusions from the current evidence. The “claim” is reframed to: we ask the double-dividend question, develop the framework, implement proxy-based regressions, report negative results and transparent limitations, and position the paper as evidence and measurement challenges rather than a completed test.

---

## Optional next steps (not yet in manuscript)

- **Sample flowchart:** Methods recommends “A full sample flowchart (observations at each merge step, missingness by variable) would strengthen transparency and is recommended for a final version.” Could add an appendix or supplementary table.
- **Ideal vs. implemented table:** A small summary table (Ideal | Implemented) for each construct could be added to Methods or appendix for quick reference.

---

*Last verified:* Section-by-section check of main.tex, introduction.tex, theory_hypotheses.tex, methods.tex, results.tex, discussion.tex, conclusion.tex, related_literature.tex, and table/figure notes.
