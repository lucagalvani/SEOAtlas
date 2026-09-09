---
name: case-study-writer
description: Write a B2B customer case study as a clean HTML artifact. Use this whenever the user wants to write, draft, or rewrite a case study — even if they don't use the word "skill". Trigger on phrases like "write a case study", "draft a case study", "rewrite this case study", or when the user provides source material (PDFs, docs, notes) and asks for a case study from it.
---

# Case Study Writer

Produce a polished, publication-ready customer case study as an HTML artifact. The output follows a fixed structure and a strict set of editorial rules, so every case study a team ships reads as one voice.

The structure below suits a B2B story where a customer replaced a manual or partial process with a vendor's product and can show numbers for it. Sections 8 and 9 are optional and apply only when the story involves risk, security, or adversarial testing.

## Inputs this skill accepts

Detect at runtime — don't ask the user to pre-format anything.

1. **Source documents** — PDFs, Google Docs, uploaded files. Read them in full. Extract metrics, quotes, timelines, and cost figures. Flag any gap between what the source supports and what the draft claims.
2. **Existing draft** — Google Doc or pasted text. Treat it as a starting point, not the truth. Check every figure against the source PDFs.
3. **Comments on the draft** — if the document has inline comments (e.g. Google Doc comments), read them and treat them as editorial instructions.
4. **A brief or notes** — free-form description of the customer, the product, and the results.

If you have a source document and a draft, reconcile them before writing. Errors to look for: wrong multipliers, unsupported cost claims, overstated ROI, placeholder quotes attributed to generic titles.

---

## Fixed document structure

Every case study follows this exact section order. Do not add, remove, or reorder sections.

### 1. Meta line
`[Company] · Case Study · [Year]`

Small, muted, above the title.

### 2. H1 title
Pattern: **"How [Client] [delivered/achieved user/customer outcome], [business/efficiency metric]"**

Rules:
- Lead with the customer/user impact (scale, safety, reliability)
- End with the cost or efficiency win
- No em dashes in the title
- No question marks
- Specific beats generic: "2 million customers" beats "at scale"

### 3. Lede (subtitle)
One or two short sentences. Its job is to frame the story — not repeat the stats below it.

Rules:
- Never restate numbers already in the stats band
- No contrast constructions ("not X — Y")
- No "this is what happens when..." meta-framing
- Should create forward pull: why does this case matter?

Good model: "Most banks find AI reliability gaps in production. [Client] finds them first."

### 4. Stats band
Exactly 4 metrics in a horizontal row. Pick the four that best represent: customer/user scale, cost reduction, performance improvement, and reliability/incidents.

Each stat has:
- A large number (with unit: M+, %, ×, or a plain integer)
- A short label (1–2 lines, explains what the number measures)

### 5. The situation
2–3 paragraphs. Cover:
- What the client does and what the product is
- Who relies on it and at what scale
- The regulatory/compliance context, where one applies (state regulations as current facts, not "coming soon" or "taking effect")

Rules:
- Don't use "is not X — it is Y" contrast constructions
- Regulations already in force: use present tense ("Under the EU AI Act, ..." not "as the EU AI Act takes effect...")

### 6. The challenge
2–3 paragraphs. Name the specific ceilings the client hit before the change. Use concrete numbers where the source supports them.

Typical structure:
- **A cost ceiling** — what one full cycle of the old process cost manually
- **A scope ceiling** — what the manual approach couldn't cover and why

End with one short sentence stating the root cause. Do not add a second "clever" sentence restating it.

### 7. What [Client] changed
Intro sentence + 3 numbered subsections. Each subsection: H3 heading + one paragraph.

The three points should cover, in this order:
1. **What got automated** — the work that moved from ad-hoc and manual to systematic and specification-driven
2. **How it was tailored to the client** — the client's own policies, rules, or thresholds replacing generic defaults
3. **How it was wired into the workflow** — where it runs in the release or operating cycle, and how that differs from what the client already had

### 8. How [Product] was tested before reaching any customer *(optional)*
Include this section only when the story involves risk, security, or adversarial testing. Intro paragraph + 3 H3 subsections, one per attack/test class.

Rules — this section must NOT paint the client in a bad light:
- Frame as "the standard [product] was held to," not "gaps we found in [product]"
- These are industry-wide attack patterns, not client-specific failures
- Each example ends on a pass or a confirmation, not a discovery: "the refusal behaviour was validated against this class before deployment" — not "this was discovered and fixed"
- The intro should make clear: any product in this domain faces these attack classes; testing for them is what rigorous evaluation looks like

### 9. Adversarial results (collapsible technical section) *(optional)*
Pairs with section 8 — include or omit them together. Implemented as a `<details>` element with a "Technical detail" label. Closed by default.

Contains:
- One intro paragraph (methodology, what the table shows)
- A before/after table with columns: Risk dimension, Framework ref (the relevant published framework, e.g. OWASP), Score iter. 1, Score iter. 2, Delta
- A footnote noting any dimension still on a roadmap and the test set size

The summary/toggle label: `[Technical detail badge] [Title] [Click to expand hint]`

### 10. Business impact
Intro sentence + 4 `<strong>`-led paragraphs, one per impact dimension:
1. Direct cost saving — with exact before/after figures and % reduction
2. Coverage multiplier — how much more ground is covered than before
3. Regulatory/risk exposure mitigated — with methodology note if modelled
4. Combined ROI and payback period

### 11. Quote
A single `<blockquote>` with:
- The verbatim quote (real, sourced, attributed)
- `<footer>` with first name + last name, title, company

Rules:
- Must be a real quote from a named person — never a placeholder
- Never attribute to a generic title like "AI Platform Lead" without a name
- If no verified quote is available, omit the section entirely rather than fabricate

### 12. What's next
1 paragraph + 3 bullet points.

The paragraph: what the continuous programme looks like now.
The bullets: what's in the pipeline (new use cases, wider coverage, further automation).

---

## Editorial rules (apply throughout)

- **No em dashes in titles or headings.** Use a comma, colon, or period instead.
- **No contrast constructions** of the form "X is not Y — it is Z." State what it is directly.
- **No "taking effect," "coming soon," or "advances"** for regulations already in force. Use present tense.
- **No repeating stats** in the lede that are already in the stats band.
- **No placeholder quotes.** A missing quote is better than a fabricated one.
- **Positive framing for vulnerability sections.** The client ran rigorous tests; the product passed them. Not: the product had gaps that were fixed.
- **Concrete numbers over vague claims.** "€51,726" beats "over €50K." Use the source figures.
- **Past tense for the pilot/engagement**, present tense for the ongoing programme.
- **No footnote disclaimers** in the published artifact.

---

## Output format

Produce a clean HTML artifact using this minimal CSS structure:

```css
body { max-width: 720px; margin: 48px auto; padding: 0 24px 80px; font-family: Georgia, serif; font-size: 17px; line-height: 1.7; color: #111; }
h1 { font-size: 2em; line-height: 1.2; margin: 0 0 16px; }
h2 { font-size: 1.25em; margin: 48px 0 12px; }
h3 { font-size: 1em; font-weight: bold; margin: 24px 0 4px; }
p { margin: 0 0 16px; }
.lede { font-size: 1.1em; color: #444; margin-bottom: 32px; }
.stats { display: flex; gap: 40px; border-top: 1px solid #ddd; border-bottom: 1px solid #ddd; padding: 24px 0; margin: 32px 0 40px; flex-wrap: wrap; }
.stat-n { font-size: 2.2em; font-weight: bold; display: block; line-height: 1; font-family: system-ui, sans-serif; }
.stat-l { font-size: 0.8em; color: #555; font-family: system-ui, sans-serif; }
blockquote { border-left: 3px solid #aaa; margin: 32px 0; padding: 0 0 0 20px; font-style: italic; color: #333; }
blockquote footer { font-style: normal; font-size: 0.85em; color: #777; margin-top: 8px; }
table { width: 100%; border-collapse: collapse; font-size: 0.9em; margin: 24px 0; font-family: system-ui, sans-serif; }
th { background: #f2f2f2; text-align: left; padding: 8px 12px; border-bottom: 2px solid #ccc; font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.05em; }
td { padding: 9px 12px; border-bottom: 1px solid #e8e8e8; vertical-align: top; font-variant-numeric: tabular-nums; }
tfoot td { background: #f7f7f7; font-weight: bold; border-top: 2px solid #ccc; border-bottom: none; }
.note { font-size: 0.82em; color: #777; font-style: italic; }
hr { border: none; border-top: 1px solid #ddd; margin: 40px 0; }
.meta { font-size: 0.82em; color: #888; font-family: system-ui, sans-serif; margin-bottom: 32px; }
```

For the collapsible technical section:
```css
.tech-section { border: 1px solid #d0d0d0; border-radius: 4px; background: #f9f9f7; margin: 40px 0; font-family: system-ui, sans-serif; }
.tech-section summary { display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; padding: 14px 18px; cursor: pointer; font-size: 0.95em; font-weight: 600; color: #222; list-style: none; user-select: none; }
.tech-section summary::-webkit-details-marker { display: none; }
.tech-section summary::before { content: '▶'; font-size: 0.7em; color: #888; transition: transform 0.15s; flex-shrink: 0; }
.tech-section[open] summary::before { transform: rotate(90deg); }
.tech-label { font-size: 0.72em; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; background: #e8e8e2; color: #555; padding: 2px 7px; border-radius: 2px; flex-shrink: 0; }
.toggle-hint { font-size: 0.78em; font-weight: 400; color: #999; margin-left: auto; }
.tech-section[open] .toggle-hint { display: none; }
.tech-body { padding: 4px 18px 20px; border-top: 1px solid #e0e0d8; font-size: 0.92em; }
.tech-body p { margin-top: 14px; }
```

Do not add decorative elements, extra colour, or elaborate design. The document should be clean and readable — content carries it, not styling.

---

## Before you write

1. Read all source documents in full.
2. List every factual claim in the existing draft and check each one against the sources.
3. Note any errors, unsupported claims, or missing data points.
4. Read all inline comments from the doc author and treat them as editorial instructions.
5. Then write the case study, incorporating corrections and comment resolutions.

Do not write the case study before completing steps 1–4.
