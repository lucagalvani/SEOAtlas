# Clustering heuristics

Clustering groups keywords that should live on the same page (or the same tightly-linked set of pages) because they serve the same underlying intent. Search engines have gotten much better at recognizing semantic clusters — targeting five similar keywords with five separate pages splits the ranking signal and gets all five pages stuck on page 2.

## When two keywords belong in the same cluster

Use these signals, in order of weight:

1. **Same SERP overlap.** If searching both keywords returns largely the same top 10 results, Google treats them as the same intent. This is the strongest signal but requires SERP data — use it when available.
2. **Same primary user question.** "email deliverability rate" and "how to make sure emails don't go to spam" are different phrasings of the same question. Same cluster.
3. **Same answer.** If the ideal answer to both queries is the same 1,500-word article, same cluster.
4. **Shared head term + refined angle.** "email deliverability" (head) and "email deliverability spam score" (refined angle) — the refined one is a support page under the head's pillar.
5. **Persona or use-case refinement.** "email marketing for ecommerce" is a persona-refinement of "email marketing". Support page, same cluster.

## When two keywords should split into different clusters

1. **Different intent.** "email marketing software" (informational) vs "best email marketing software" (transactional) — different clusters, or at least different roles within the same cluster (the transactional one is a standalone "best of" post).
2. **Different audience.** "email marketing for ecommerce" vs "email marketing for nonprofits" — same topic, different audiences, different pages. Different clusters unless you explicitly want to write an audience-agnostic piece.
3. **Different stage of funnel.** "what is email marketing automation" (top-funnel) vs "set up a drip campaign in Klaviyo" (deep-funnel). Different clusters.
4. **Different root concept.** "email marketing" and "SMS marketing" share a category but the second is a distinct topic (carrier compliance, character limits, opt-in law). Different clusters.

## Cluster shape

A healthy cluster has:

- **One pillar.** The broadest, highest-volume, most-canonical term. This page targets the head term and ranks for the cluster's umbrella concept.
- **3–10 support pages.** Each owns a specific sub-question or sub-angle. Each links back to the pillar. The pillar links out to all of them.
- **A cluster name that reads like a sitemap section.** "Email deliverability" works. "Email Bucket 3" doesn't.

Target: 5–15 clusters for a 50–200 seed input. If you end up with 30 clusters, some should probably merge. If you end up with 3 clusters for 150 seeds, they're too broad.

## Choosing the pillar within a cluster

When multiple keywords in a cluster could plausibly be the pillar, pick the one that:

1. Has the highest search volume (if volume data is available).
2. Is the broadest phrasing — "email marketing software" beats "email marketing software pricing" for pillar status.
3. Matches informational or investigational intent (pillars rarely work as transactional — those are better as standalone "best of" pages sitting outside the cluster).
4. Reads as a natural H1 for a 2,500–4,000-word hub article.

If no candidate keyword works as a pillar, **synthesize** one. The pillar's primary keyword doesn't have to be a seed from the input list — it can be a natural head term you assign. Note this in the pillar's `notes` field so the user knows it's synthesized.

## Choosing support pages

A support page should:

1. Answer one specific question or cover one specific sub-topic. Tight scope.
2. Have a clear primary keyword that doesn't overlap with another support page's primary keyword in the same cluster.
3. Link naturally to the pillar (there's a sentence or section where it makes sense to say "for the broader picture, see [pillar]").
4. Be large enough to justify its own page — if it's one paragraph, it belongs inside the pillar, not as its own support page.

## Dealing with noise

Some seeds won't cluster cleanly. Handle them like this:

1. **Singletons** (one seed with no close neighbors): hold aside. At the end, see if any fit into an existing cluster with a stretch. If yes, add them. If no, list them in the debrief as "uncategorized — consider for standalone posts or drop".
2. **Too-broad seeds** ("marketing", "software"): drop from the plan. Note in the debrief. These can't be pillars because the competition is too high, and they can't be support pages because they're too generic.
3. **Out-of-ICP seeds**: drop. Note in the debrief with a one-line reason.

## A worked example

Input seeds (generic B2B SaaS ICP — email marketing software):

- email marketing
- email automation
- email automation software
- drip campaign
- email deliverability
- email deliverability checklist
- email deliverability spam score
- transactional email
- email list segmentation
- welcome email sequence

One reasonable clustering:

**Cluster 1: Email automation**
- Pillar: `email automation` (includes `email automation software` as a variant)
- Support: `drip campaign`, `email list segmentation`, `welcome email sequence`
- Pillar rationale: head term, informational, natural hub

**Cluster 2: Email deliverability**
- Pillar: `email deliverability`
- Support: `email deliverability checklist`, `email deliverability spam score`
- Pillar rationale: head term

**Cluster 3: Transactional email**
- Pillar: `transactional email` (synthesized expansion: order confirmations, password resets, receipts)
- Support: expand from long-tails since only one seed landed here

Note that `email marketing` is deliberately not a pillar — it's too broad to rank competitively and it would swallow the other clusters. It can be a category page or a series intro, but it's not the hub. (Flag this in the debrief.)
