# AEO / competitive query-gap research

This is a different problem from keyword clustering. Keyword clustering starts from *keywords you already have* and organizes them into pages. This starts from *no keyword list at all* — it reasons from the customer's buying journey to construct the queries a real buyer would type or ask an AI assistant, then finds which of those queries nobody has answered yet.

## Why not just use a keyword-volume / prompt-tracking tool

Tools that claim to measure "how often LLMs mention your brand" and reverse-engineer content from that measure a noisy, gameable proxy. Search volume for AI-assistant queries is largely invisible anyway — most of these queries lack reliable volume data entirely. Don't anchor the plan on volume. Anchor it on **whether a real buyer would ask this, and whether anyone has answered it well**.

## Step 1 — Establish the frame

Ask the user for, or infer from context:
- **Product/company name** and one-sentence category description
- **3–8 named competitors or alternatives** (the more specific, the better — generic "alternatives to X" queries are weaker than named comparisons)
- **Whether to scope to a specific vertical/industry, or go industry-agnostic.** Don't assume — ask once, like the ICP question in the main clustering workflow.

## Step 2 — Generate candidate queries from the customer-journey axes

Combine these axes to generate candidate queries. Drop any axis that doesn't apply — drop the vertical axis entirely for an industry-agnostic product, for example. Aim for dozens of candidates, not a handful: generation is a volume game. Targeting, in Step 4, is not.

- **Vertical / industry** (optional): "[category] for healthcare," "[category] for financial services"
- **Company size / persona**: startup, seed-stage, mid-market, enterprise; buyer role — engineer, PM, procurement, executive
- **Budget / pricing stage**: free/open-source vs. paid, self-hosted vs. managed, "is [category] worth paying for"
- **Integrations / framework / stack**: "[category] for [popular adjacent tool/framework]," "[category] + [stack component]"
- **Alternatives / competitors**: "[competitor] vs [product]," "[competitor] alternatives," "is [competitor] worth it"
- **Buyer process / stage**: build vs. buy, who owns this decision internally, evaluation checklist, how to get started, red flags to watch for
- **Use-case / technical scenario**: a specific job-to-be-done the product solves, phrased the way a practitioner would search it, not the way a vendor would name the feature

Generate every axis combination that produces a plausible query. Don't pre-filter for competitiveness yet — filter for that in Step 4.

## Step 3 — Check who currently owns each query

For each candidate query, determine who currently ranks, appears in AI-assistant answers, or has published content answering it directly. Use whatever research capability is available — web search, SERP tools — or delegate the check to parallel sub-tasks when the query list is long.

For each query, record whether content exists, who owns it (a named competitor, an adjacent-but-different vendor, a non-vendor authority site, or nobody), and how directly it answers the query.

## Step 4 — Tier by competitive gap

Sort every researched query into one of these tiers. Sorting them well is the core judgment call in this exercise — spend the effort here, not on padding the query list.

1. **Zero-competition comparisons.** A direct "[named competitor] vs [product]" query where *neither the competitor nor anyone else* has published a comparison. This is usually the single best opportunity in any run — low effort, high intent, no one to outrank because no one has shown up.
2. **Adjacent-authority pillar topics.** Topics heavily covered, but only by non-competitors — regulatory bodies, generic educational sites, adjacent-category blogs. The content already ranking doesn't connect the topic to the product's actual approach. The wedge is connecting an established topic to a specific methodology, not out-writing the existing content.
3. **Unclaimed buyer/process questions.** Practical questions about the buying or adoption process itself (who owns this decision, build vs. buy, an evaluation checklist) that no vendor in the category has claimed the framing for — usually answered generically by non-vendor sites, if at all.
4. **Adjacent-vendor-owned use-cases.** Real use cases the product solves, currently answered by vendors in a *different* category (not a direct competitor). Winnable, but expect more effort since someone competent already has content there.
5. **Frontier / new-and-unclaimed.** New integrations, frameworks, or personas that are recent enough that no vendor — competitor or otherwise — has claimed them yet. Time-sensitive: these move to a lower tier once someone else notices.
6. **Do-not-pursue.** Categories already saturated by multiple aggressive, competent competitors — generic "best [category] tools" roundups, broad pricing comparisons, generic company-size persona pages that three or four competitors have already each written five versions of. State this explicitly in the output; don't just quietly omit these queries. A visible do-not-pursue list is as useful to the user as the list of things to pursue.

## Step 5 — Turn tiers into an actual content plan

A tiered query list is not a deliverable on its own. For each query worth pursuing, produce:
- The target query, stated the way a buyer would actually type or ask it
- A working title
- 2–4 supporting queries the same page should also capture
- The competitive angle — what makes this piece different from (or first compared to) anything that exists
- The tier, so the user can see the plan's priority order at a glance

## Quality bar

1. **Every query is something a real buyer would type or ask an AI assistant** — not a mechanically-generated axis combination that reads unnaturally. If a generated combination doesn't sound like real language, drop it before researching it.
2. **Named comparisons beat generic ones.** "[Competitor] vs [product]" is a real query with real intent. "Alternatives to [category]" is weaker and more contested.
3. **The do-not-pursue list is explicit**, with a one-line reason each — not silently dropped queries.
4. **Tier 1 opportunities get flagged first and loudest.** They're rare, they're the highest-leverage find in any run, and they're easy to bury under a long list of lower-tier queries if the output isn't structured to surface them.
5. **Re-running this later will find different gaps.** Zero-competition queries don't stay zero-competition — note the date of the research so the user knows when to re-check Tier 1 and Tier 5 findings.

## Output

Present the result as a tiered table or list — tier, query, working title, competitive angle — grouped by tier, Tier 1 first. If the user wants a spreadsheet instead, reuse the same three-tab XLSX builder from keyword clustering: treat each pursued query as a support-page entry and note its tier in the `notes` field. A plain tiered list usually reads clearer, though — AEO gaps don't nest into a hub-and-spoke hierarchy the way keyword clusters do.
