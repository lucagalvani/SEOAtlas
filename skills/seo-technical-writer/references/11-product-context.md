# Product Context — Background, Internal Linking & Plug Rules

Read this file before writing any section that mentions the product you write for, any case study that uses its data, or any internal link to its docs. Skip it for pieces that don't touch the product at all.

The whole point of this file is to keep product mentions honest, specific, and useful. A reader who spots a plug should come away with more information than they started with, not with a taste of marketing in their mouth.

**This file ships as a template.** The rules below are portable and apply as written. The three tables — what the product is, approved claims, and the internal-linking map — are yours to fill in once, then treat as the canonical source. An unfilled table is not a licence to improvise: if a claim or URL isn't in it, follow **When in doubt** at the bottom.

## What the product is

Fill this in from the product's own docs, not from its marketing site. Keep it to a paragraph or two, and write it as a practitioner would describe the tool to a colleague.

Cover:

- **What it does**, in the vocabulary its docs use. Name the primary objects and the workflow that connects them.
- **Access channels** — dashboard, SDK, CLI, API, CI integrations.
- **Positioning to hold in writing** — and, just as important, the adjacent categories it is *not*. Naming the neighbours it gets confused with is what stops a draft from quietly reframing the product as something it isn't.

Cite the docs page each part came from, so a reviewer can check it and a future writer can tell when it went stale.

## The 95/5 rule for product mentions

At least 95% of every article is reader-value content. The product fits in the remaining ~5%, and only where it adds information rather than interrupts.

Rule of thumb: if a product mention could be replaced with a generic "you could use a tool to do this" and the paragraph would read the same, the mention isn't earning its place. Cut it or move it to a spot where the specific capability matters.

### When a plug earns its place

1. **The article describes a process the product automates.** After the reader understands the manual version, one short paragraph can note which steps the product collapses, with a link to the specific docs page.
2. **The article recommends a pattern the product encodes as a first-class concept.** Cite the concrete implementation — the named object, decorator, or config surface — and link to the concept page for it.
3. **A case study illustrates a claim the rest of the article makes in the abstract.** One customer anecdote with real numbers beats ten generic recommendations. Cite sources and use exact figures (see `07-source-material.md`).
4. **The piece is explicitly about the product** (launch, feature deep-dive, changelog companion). The ratio inverts here, but even then, lead with the reader's problem.

### When a plug does NOT earn its place

1. In the TL;DR. The TL;DR is pure reader value. No exceptions.
2. In the opening paragraph of the body. The opener belongs to the reader's problem.
3. As a generic "...and tools like X can help with this" sentence bolted onto a section that doesn't need it.
4. As a footer CTA. Footer CTAs are the editor's job, not the writer's.
5. Next to competitor names in a comparison table, unless the piece is explicitly a comparison article with a shared methodology.

## Approved claims

List the claims that are directly grounded in the product's docs and can appear in content without a reviewer confirmation item. One row per claim, with the docs page that supports it. Anything stronger than what's on this list gets flagged in editor notes instead of asserted.

| Claim | Source |
|---|---|
| *(claim, phrased the way it can appear in prose)* | *(docs URL)* |

Two habits keep this table trustworthy: phrase each claim at the strength the source actually supports, and re-check the table whenever the product ships a release that touches one of these surfaces.

## Banned overclaims — rewrite or delete

The patterns below overreach on what almost any developer tool delivers, or read as sales taglines rather than technical claims. Add product-specific ones as reviewers flag them.

1. **"The only [category] that..."** Almost never true. Adjacent tools cover overlapping surface area. Name the actual differentiator specifically, or say nothing.
2. **"Fully automated."** Rarely accurate. Name what the product automates and what a human still defines, reviews, or interprets.
3. **"Complete coverage" / "end-to-end coverage."** Meaningless without a scope. Naming the scope turns it into a claim; leaving it out leaves filler.
4. **"Drop-in replacement for [framework]."** Only if the product is genuinely pitched that way. A tool that sits alongside a framework must not be framed as a swap-out.
5. **"Eliminates [failure mode]" / "guarantees [property]."** Tools surface, catch, flag, and measure. They rarely eliminate or guarantee. Use the honest verb.
6. **"Works with any model / any framework / any use case."** Broadly true, and empty. If the integration matters, name it. If it doesn't, cut the sentence.
7. **"Powered by AI" / "AI-native."** Banned for the same reason `01-banned-words.md` bans "cutting-edge." Say what it does instead.
8. **"Enterprise-grade"** without a named standard (SOC 2, ISO 27001, a specific regulation). Unnamed, the word is marketing filler.

## Internal linking map

Build this table once, from the product's docs, and use it as the canonical source of URLs. Never invent paths. If the concept you need isn't on the map, flag it in editor notes as a reviewer confirmation item rather than guessing.

Group the rows the way the docs are grouped, so the right page is easy to find while drafting:

| Group | What belongs in it |
|---|---|
| Getting started | Introduction, registration, quickstart, changelog, blog |
| Core concepts | One row per first-class object in the product's model |
| Workflows and tutorials | The how-to pages, one row per task a reader might run |
| Advanced / production | Monitoring, scaling, and the deeper evaluation or debugging paths |
| SDK and API | Installation, usage overview, client reference, API reference |
| Integrations | One row per supported third-party tool |

Each row is a concept or anchor phrase paired with a full URL.

## How to choose the right link

Match the anchor phrase to the most specific docs page that covers it. Linking a named concept to the product homepage is lazy; link to the concept's own page.

Prefer concept pages when the article is explaining what something is. Prefer tutorial pages when the article is showing how to do something. If the reader is likely to run code right after reading your paragraph, link to the tutorial.

One internal docs link per major section is usually enough. Four or more in a 1,500-word article reads as stuffing. If you find yourself needing more, the article is probably a product tour in disguise — rethink the structure.

## Internal-link placement rules

1. **Anchor on the concept, not a CTA.** Link the noun the sentence is already about. "Click here to learn more" is never acceptable.
2. **Link once per concept per article.** If a concept is linked in section 2, don't re-link it in section 4.
3. **Do not link the product name** unless the article has not yet said what the product is. One in-body link to the introduction at first mention is fine; after that, link specific concepts instead.
4. **External links to primary sources still win.** If a section cites a research paper, the paper link takes priority. The point is to route the reader to the most useful next page, not to maximise product clicks.
5. **Editor notes list every internal link**, with the anchor phrase and target page, in the "Internal links to add" section.
6. **Add at least one internal docs link per article** where the content maps to a docs page. A piece on a topic the docs cover, with no link to it, is a missed opportunity. If no link earns its place on merit, reconsider the article's angle.
7. **Never repeat the same URL more than twice in one article.** Three or more placements means consolidating to the two most contextually relevant ones, or finding a more specific page from the map.

## Style for product mentions

Hold the house voice. Product mentions follow the same rules as the rest of the piece: no filler adjectives, no complexity-hiding "simply," no marketing verbs. "X runs the evaluation" beats "X seamlessly streamlines your evaluation workflow" on every axis the reader cares about.

Prefer the verb form that names the concrete action: "X generates tests from specifications," "X captures traces via the `@trace` decorator," "X scores outputs with an LLM judge." Never "empowers," "unlocks," or "transforms."

Match the product's own casing. Most products are lowercase in code, package names, and URLs, and capitalised in prose.

## When in doubt

If a claim or link cannot be grounded in this file or in the linked docs, do one of two things:

1. Cut the mention and move on. A clean piece with no plug beats a piece with a shaky one.
2. Flag it in editor notes as a reviewer confirmation item, phrased as a question ("Is the `@trace` decorator still the recommended entry point for agentic tracing as of the current SDK version?").

The reviewer is the last line of defence. Give them something to review, not a wall of marketing claims to validate.
