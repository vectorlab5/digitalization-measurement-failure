# Figure 1 — Conceptual Model: Generation Prompt

Use this prompt with an AI image generator (e.g., DALL·E, Midjourney, FLUX) or as a brief for a designer to reproduce or adapt Figure 1.

---

## Prompt (concise)

**Conceptual path diagram for an academic paper (Journal of Environmental Economics and Management style).**

- **Layout:** One central box at the top center; three outcome boxes below in a row (left, center, right). Clean, uncluttered; no 3D or decorative clutter.
- **Nodes (rounded rectangles, soft borders):**
  - **Top center:** “Enterprise digitalization” (main driver).
  - **Bottom left:** “TFP” (Total Factor Productivity).
  - **Bottom center:** “Environmental performance”.
  - **Bottom right:** “Green innovation”.
- **Arrows (directed, same line weight):**
  - From **Enterprise digitalization** down to **TFP**, labeled **H1** (small circle or badge on the arrow).
  - From **Enterprise digitalization** down to **Environmental performance**, labeled **H2**.
  - From **Enterprise digitalization** diagonally down-right to **Green innovation**, curved arc, labeled **H3a**.
  - From **Green innovation** diagonally up-left to **Environmental performance**, curved arc, labeled **H3b**.
- **Moderators (clearly secondary, e.g. dashed boxes or smaller badges):**
  - **H4: regulation** — placed near the arrow from digitalization to Environmental performance (e.g. above or beside it).
  - **H5: size, ownership** — placed near the arrow from digitalization to TFP (e.g. above or beside it).
- **Style:** Academic, minimal. Light fills (e.g. light blue-grey for digitalization, light warm grey for TFP, light teal/sage for environmental performance and green innovation). Dark grey or navy arrows and text. Sans-serif font. Labels H1–H3b in small circles or pills on the arrows; H4 and H5 in smaller dashed boxes so they read as moderators. No photos, no icons; diagram only.
- **Caption (for reference):** “Conceptual model of hypothesized relationships. H1–H2: direct effects of digitalization on TFP and environmental performance. H3a–H3b: mediation path via green innovation. H4–H5: moderation by regulation and firm characteristics.”

---

## Prompt (single paragraph, copy-paste)

Conceptual path diagram for an academic economics paper: one central box at top “Enterprise digitalization”; below it three boxes in a row labeled “TFP”, “Environmental performance”, “Green innovation”. Arrows: from Enterprise digitalization to TFP (label H1), to Environmental performance (label H2), and in a curved arc to Green innovation (label H3a); from Green innovation in a curved arc to Environmental performance (label H3b). Two moderator labels in smaller dashed boxes: “H4: regulation” near the digitalization–Environmental performance arrow, “H5: size, ownership” near the digitalization–TFP arrow. Style: minimal, academic; light pastel fills (blue-grey, warm grey, teal/sage), dark grey arrows, sans-serif; hypothesis labels H1–H3b as small circles on arrows. No 3D, no photos, diagram only.

---

## Element checklist (for verification)

| Element | Description |
|--------|-------------|
| Node: Enterprise digitalization | Top center, main driver |
| Node: TFP | Bottom left |
| Node: Environmental performance | Bottom center |
| Node: Green innovation | Bottom right |
| Arrow + H1 | Digitalization → TFP |
| Arrow + H2 | Digitalization → Environmental performance |
| Arrow + H3a | Digitalization → Green innovation (curved) |
| Arrow + H3b | Green innovation → Environmental performance (curved) |
| Badge H4: regulation | Moderator on digitalization–Environmental performance |
| Badge H5: size, ownership | Moderator on digitalization–TFP |

---

## Reference

- **Paper:** Enterprise Digitalization and the Double Dividend: Total Factor Productivity and Environmental Performance in Heavily Polluting Firms.
- **Figure label in manuscript:** Figure 1, `\label{fig:model}`.
- **Current implementation:** TikZ in `main.tex` (lines 73–120).
