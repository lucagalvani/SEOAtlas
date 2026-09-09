# Output Format

Every article deliverable follows this structure. No exceptions.

## Metadata block

YAML-style block at the very top of the file, before the title:

```
---
primary_keyword: "rate limiting express.js"
secondary_keywords: ["API throttling", "express middleware", "token bucket"]
word_count_target: 1800
author: "[AUTHOR NAME]"
status: draft
---
```

All fields are required. `author` uses a placeholder if not specified in the brief. `status` is always `draft` on first delivery.

## Article opener (mandatory)

Every article opens with three elements, in this exact order, immediately after the H1 title. No preamble, no restatement, no "In this article" framing.

```markdown
# H1 Title

*X min read*

**TL;DR —** Two to four sentences that answer the core question of the piece. Lead with the recommendation or conclusion. Name the specific tools, numbers, or tradeoffs that matter. Someone who reads only this block and the H2s should leave with the actual answer.

[Body begins with the first real section — no "introduction" header]
```

### Time-to-read line

Format: `*X min read*` on its own line, immediately below the H1. Italic, no bold, no emoji, no "estimated," no "approximately."

Calculate as: `ceil(word_count / 225)`. 225 words per minute is the standard reading speed for technical prose. Round up. A 1,800-word piece is `*8 min read*`. A 2,700-word piece is `*12 min read*`. Count the body word count only — exclude the metadata block, TL;DR, code blocks, and editor notes.

For pieces with heavy code (more than ~20% of body is code blocks), use `*X min read*` based on prose words only and add a second line: `*~Y code snippets*`. Readers parse code at a different rate than prose, and a single number misleads.

### TL;DR block

Format: a single paragraph prefixed with `**TL;DR —**` (em dash, not hyphen). Placed on its own line between the time-to-read line and the first H2. One blank line separates it from the surrounding elements.

Rules for the TL;DR:

1. **Two to four sentences. No bullet points, no sub-lists, no nested structure.** The TL;DR is scannable prose, not a second table of contents.
2. **Lead with the answer, not the setup.** "Use a sliding-window limiter backed by Redis when you need per-user fairness; fixed-window is fine under 1k RPS." — not "Rate limiting is important for APIs, and there are several approaches to consider."
3. **Name the specific thing.** If the article recommends a tool, version, pattern, or number, it appears in the TL;DR. Generic TL;DRs ("this article covers X, Y, and Z") fail the purpose.
4. **No marketing verbs.** No "explore," "dive into," "unlock," "unpack." See `01-banned-words.md`.
5. **No product plug in the TL;DR.** The TL;DR is pure reader value. Product mentions go in the body where they earn their place (see `11-product-context.md`).
6. **Must work as a featured snippet.** Google and AI answer engines pull the first direct answer in the article. The TL;DR is that answer. Write it to be quoted verbatim.

### What the TL;DR is not

Not an abstract ("This paper discusses..."). Not a teaser ("Read on to find out..."). Not a summary of the article's structure ("First we'll cover A, then B, then C"). If the TL;DR could be deleted and the reader would lose nothing, it's failing.

## Body structure

```markdown
# H1 Title

*8 min read*

**TL;DR —** [two to four sentences, see above]

Body text organized with H2s for major sections and H3s for subsections.

Code blocks always specify the language:

​```javascript
const example = true;
​```

Tables for comparative data:

| Metric | Before | After |
|---|---|---|
| p99 latency | 340ms | 85ms |
| Error rate | 2.3% | 0.4% |
```

### Rules for body elements

H2s are major sections. H3s are subsections within an H2. Do not skip heading levels. Do not use H4 or deeper unless the piece exceeds 3,000 words and genuinely needs it.

Code blocks require a language tag. No untagged fences. Use `text` for plain output.

Tables are for comparative data only. Do not use tables for single-column lists or for content that reads better as prose.

### Visual placeholders

Every article must include inline visual markers at the points where a visual should appear in the published piece. These are not decorative. Each visual must earn its place by communicating something that prose alone handles poorly: spatial relationships, system architecture, data comparisons, process flow, before/after states, or UI context.

Use this syntax for visual placeholders:

```markdown
<!-- VISUAL: [type] | [description] | [why it's needed] -->
```

**Type** is one of: `diagram`, `screenshot`, `table`, `code-output`, `chart`, `illustration`, `flowchart`, `comparison`.

**Description** is a specific brief for whoever will create the visual. Not "architecture diagram" but "Request flow from client through nginx reverse proxy → Express rate limiter middleware → Redis counter → response, showing the 429 path branching after the Redis check."

**Why it's needed** explains what the visual communicates that the surrounding prose doesn't. This prevents decorative visuals and helps the editor prioritize which ones to produce first.

Example in context:

```markdown
The sliding window algorithm tracks requests across two adjacent time windows,
weighting the previous window's count by the fraction of time that has elapsed
in the current window.

<!-- VISUAL: diagram | Timeline showing two adjacent 60-second windows with
request dots. Current window is 40 seconds in. Previous window had 45 requests.
Visual shows the weighted calculation: 45 × (20/60) + current_count. Arrow
indicates the "sliding" overlap. | The weighted calculation is hard to grasp
from text alone — the visual makes the overlap between windows intuitive. -->

This means a client who sent 45 requests in the previous window still has
partial count carried forward into the current window.
```

### When to place visuals

Insert a visual placeholder at every point where one of these conditions is true:

1. **Architecture or system flow.** Any time the text describes how components connect, how data moves through a system, or how a request travels through a pipeline. Text descriptions of architectures are almost always insufficient alone.

2. **Before/after comparisons.** When showing the effect of a change (performance improvement, code refactor, configuration shift), a side-by-side visual makes the contrast immediate.

3. **Decision trees or conditional logic.** If the reader needs to choose between approaches based on multiple criteria, a flowchart or decision matrix is faster to parse than nested prose.

4. **Terminal or UI output.** When the reader needs to know what success (or failure) looks like, a screenshot or formatted code-output block showing the actual terminal response or UI state is essential.

5. **Data with three or more dimensions.** When comparing more than two things across more than one axis, use a chart or table rather than describing the data in prose. Tables are already covered above. Charts are for trends, distributions, or relationships where the shape of the data matters.

6. **Process sequences with more than three steps.** If a process has branching, parallelism, or conditional steps, a flowchart or sequence diagram communicates it faster than a numbered list.

### When NOT to place visuals

Do not insert visual placeholders for:

- Decoration or visual relief ("break up the text"). If the text needs breaking up, the text is too long or poorly structured.
- Simple linear processes with three or fewer steps. A sentence handles these fine.
- Concepts that are purely abstract and don't have a spatial or structural representation.
- Stock-photo-style images ("a developer at a laptop"). These add nothing.

### Visual density guideline

As a rough target, developer articles should include one visual for every 400 to 600 words of body text. A 1,800-word article should have three to four visuals. A 3,000-word article should have five to seven. These are guidelines, not rules. Some topics are inherently more visual (system architecture, data pipelines) and some are inherently less (API design philosophy, coding conventions). Let the content dictate the count.

## Editor notes block

Placed at the very end of the file, after the body. Not inline. Uses an HTML comment so it doesn't render if the markdown is published accidentally:

```markdown
<!--
## Editor Notes

### Fact-checks needed
- [ ] Verify the Zheng et al. (2023) citation — confirm >10% figure is from Table 3
- [ ] Confirm Express v5 middleware API hasn't changed since last stable release

### Missing visuals
- [ ] VISUAL line 47: Architecture diagram — request flow through rate limiter (priority: high — core concept)
- [ ] VISUAL line 82: Screenshot — 429 response in Postman/curl (priority: medium — supports troubleshooting section)
- [ ] VISUAL line 105: Chart — sliding window vs. fixed window throughput comparison under burst traffic (priority: high — supports the main comparison argument)

### Internal links to add
- [ ] Link to "Getting Started with Express" guide
- [ ] Link to API design best practices article

### SEO meta description
"How to implement rate limiting in Express.js with the token bucket pattern. Includes production code, failure modes, and benchmarks comparing sliding window vs. fixed window."

### Confirmation items for technical reviewer
- [ ] Is the Redis-backed approach still recommended over in-memory for >1 instance?
- [ ] Verify the recommended rate-limiter-flexible version is current

### Promotion assets
Short summary: "One sentence maximum. Dense, no filler. Leads with what the reader learns, not what the article covers."
CTA title: "Action-oriented headline for the CTA block."
CTA description: "One sentence maximum. Connects the article's core takeaway to the product action. Specific to what the reader just learned — no generic pitch."
Button text: "Three to five words. Imperative. No exclamation marks."

Placement: appended at the very bottom of the Google Doc as plain text, after the article body. No heading, no special formatting.
-->
```

### What goes in editor notes

Every deliverable must include all six sections, even if some are empty (mark as "None identified"):

1. **Fact-checks needed** — Any claim, figure, or version number that needs verification.
2. **Missing visuals** — A summary of all `<!-- VISUAL -->` placeholders in the body, with line references, priority (high/medium/low), and production notes for the designer or editor. This is the visual production queue.
3. **Internal links to add** — Cross-references to other content on the same site. Use best guesses if the full content library isn't available.
4. **SEO meta description** — One draft, under 160 characters, containing the primary keyword.
5. **Confirmation items for technical reviewer** — Questions for the subject matter expert. These are the things the writer is unsure about and flagging honestly rather than guessing.
6. **Promotion assets** — Four elements used by the content team when publishing: (a) **Short summary**: one sentence, dense and specific, no filler; (b) **CTA title**: action-oriented headline for the CTA block; (c) **CTA description**: one sentence connecting the article's core takeaway to the product action — specific to what the reader just learned, not a generic pitch; (d) **Button text**: 3–5 words, imperative, no exclamation marks. Appended at the very bottom of the Google Doc as plain text — no heading, no special formatting. These are required. Leave no field blank.
