# Source Material Handling

## What counts as source material

Decks, research papers, whitepapers, knowledge base excerpts, internal docs, customer interviews, benchmark reports, changelogs, release notes. Anything you're given as input to write from.

## Extraction rules

When working from source material, extract these four things:

1. **Specific data points with their exact figures.** If a paper says ">10% accuracy shift from swapping candidate order," write that exact figure. Do not round, soften, or generalize. "Approximately 10%" is not the same as ">10%."

2. **Direct quotes, attributed accurately.** Name the person, their role, and the context. "Jane Kim, principal engineer at Stripe, said during the 2024 post-mortem..." not "According to industry experts..."

3. **Failure mode examples with concrete details.** Source material often contains the most valuable content buried in appendices, footnotes, and "limitations" sections. Extract those first. A specific failure scenario teaches more than a success summary.

4. **Before/after comparisons.** If the source shows a change, preserve the contrast with both numbers. "Latency dropped from 340ms to 85ms at p99" not "latency improved significantly."

## What not to do

Never paraphrase research into vague claims. This is the single most common failure when writing from source material.

**Bad:** "Research shows that evaluation order can affect model accuracy."
**Good:** "Zheng et al. (2023) found that swapping the order of two candidate responses shifted GPT-4's preference rating by >10%, even when the responses were identical in quality."

**Bad:** "Several companies have reported improvements after adopting this approach."
**Good:** "Notion's infrastructure team reduced their CI pipeline time from 47 minutes to 12 minutes after migrating to Bazel in Q3 2024."

## When source material conflicts

If two sources disagree on a data point, present both with attribution and note the discrepancy. Do not silently pick one. The reader decides.

## When source material is vague

If the source itself is vague ("we saw significant improvements"), flag it in the editor notes block as needing a follow-up with the author or technical reviewer. Do not invent specificity the source doesn't provide.
