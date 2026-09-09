---
name: seo-cluster-planner
description: Turn a list of seed keywords into a hub-and-spoke content plan — expand each seed into long-tail variants, then cluster everything into pillar pages (one per cluster) and supporting pages (the spokes). Produces an XLSX with three tabs (Pillars, Support, Long-tails). Also supports an alternate AEO / answer-engine mode — building high-intent buyer queries from the customer journey (company size, budget, integrations, competitors) and tiering them by competitive content gaps, for when the goal is appearing in AI-assistant answers or winning zero-competition comparison pages rather than ranking a keyword list. Use this whenever the user wants to plan SEO topics from keywords, build a content cluster, map pillar and supporting pages, expand seeds into long-tails, turn a keyword list / keyword spreadsheet into a content calendar or topic map, find buyer-intent queries for AEO, find competitive content gaps, or plan comparison ("X vs Y") pages. Trigger on phrases like "cluster these keywords", "build a content plan", "pillar and support pages", "long-tail keywords from this list", "topic map", "content calendar from keywords", "AEO", "answer engine optimization", "buyer-intent queries", "competitive content gaps", "queries we're not covering", or whenever an SEO keyword list (CSV / XLSX / pasted) needs to become a structured plan — even if the user doesn't use the word "skill".
---

# SEO Cluster Planner

Turn a raw keyword list into a hub-and-spoke content plan, or run a competitive AEO query-gap analysis. It runs in one of two modes — pick the one that matches what the user actually wants:

- **Keyword clustering** (default) — the user has a keyword list and wants pillar/support pages built from it. Output: one XLSX with three tabs (**Pillars**, **Support**, **Long-tails**). Covered by the rest of this file.
- **AEO / competitive query-gap research** — the user wants high-intent buyer queries that nobody, including competitors, has covered yet, aimed at appearing in AI-assistant answers rather than classic SERPs. Output: a tiered query list and content plan. See `references/aeo-query-research.md` for the full workflow — read it when this mode applies, don't load it for a standard clustering run.

Use AEO mode when the user mentions AEO, answer-engine optimization, competitor comparison pages, "queries we're not covering," or explicitly contrasts it with keyword-volume-driven SEO. Use keyword clustering for everything else. If genuinely unclear which one fits, ask.

This skill serves SEO-led content teams who have a list of keywords (their own research, an export from Ahrefs/Semrush, Google Search Console, or a Google Sheet) and need a structured plan that says *what to write, in what order, and how pages link to each other*.

## Inputs this skill accepts

Detect the input type at runtime — don't ask the user to pre-format it.

1. **Pasted keywords in chat.** One per line, comma-separated, or bulleted. Treat every line/item as a seed.
2. **Uploaded file.** `.xlsx`, `.xls`, `.csv`, `.tsv`. Use whatever file the user just uploaded or attached to the conversation. Read it with pandas. If the sheet has multiple columns, try to detect:
   - The keyword column (look for headers containing `keyword`, `query`, `term`, `kw`)
   - Optional: volume (`volume`, `search volume`, `searches`, `vol`)
   - Optional: difficulty (`kd`, `difficulty`, `keyword difficulty`)
   - Optional: intent (`intent`)
   - Optional: cluster/cluster_name (`cluster`, `topic`, `group`) — if already clustered, respect the grouping as a strong prior but still validate it
3. **A linked Google Sheet** (like the one attached at the project level). If the user points at a linked Sheet and a Drive/Sheets connector is available, read it through that connector. If no connector is available, tell the user and ask them to export to CSV/XLSX.

If the input is ambiguous (e.g. the uploaded file has no obvious keyword column), ask one clarifying question before proceeding. Otherwise proceed silently.

## ICP context (ask once per run)

Before generating the plan, confirm the ICP/domain so the long-tails and clusters use the right vocabulary. Don't assume a domain — ask.

Ask in one short message, e.g.:
> "Before I build this — who's the audience/ICP for these keywords? (e.g. the industry, product category, or type of buyer)"

If the user has already specified the ICP in their request, skip the question.

Store the confirmed ICP as `icp_context` and use it for:
- Disambiguating polysemous seeds (e.g. "evaluation" could mean HR performance reviews or product evaluation — ICP decides)
- Generating on-theme long-tails (an email-marketing-tool run shouldn't produce "how to evaluate employees")
- Naming clusters in domain-native language

## Workflow

1. **Load the seeds.** Parse input, extract seed keywords and any available metadata (volume, KD, intent).
2. **Normalize.** Lowercase, strip whitespace, de-duplicate, fix obvious typos.
3. **Confirm ICP** (see above).
4. **Expand each seed into long-tails.** Target 6–12 long-tails per seed. Use the patterns in `references/long-tail-patterns.md`. Prioritize question-based and error-message queries for developer ICPs — they convert better and have lower competition.
5. **Cluster.** Group seeds + long-tails into topic clusters using the heuristics in `references/clustering-heuristics.md`. Each cluster becomes one pillar page. Aim for 5–15 clusters for a typical 50–200 seed input; fewer seeds = fewer clusters.
6. **Assign roles within each cluster.**
   - **Pillar page:** broad, high-volume, high-intent head term. Usually informational or investigational. Designed to rank for the cluster's primary concept and link out to every support page.
   - **Support pages:** narrower, often long-tail. Each answers one specific question or covers one specific sub-topic. Each support page links back to the pillar.
   - Target 5–10 support pages per pillar. If a cluster has <3 candidate support pages, consider merging it into an adjacent cluster.
7. **Write the plan.** Call `scripts/build_plan_xlsx.py` with the plan as JSON. The script writes a three-tab XLSX (Pillars, Support, Long-tails) to the outputs folder.

## Output spec (what the XLSX must contain)

The script enforces this structure — don't hand-roll the XLSX. Pass it a JSON object shaped as:

```json
{
  "icp_context": "B2B SaaS — email marketing software buyers",
  "generated_at": "2026-04-17",
  "clusters": [
    {
      "cluster_name": "Email deliverability",
      "pillar": {
        "primary_keyword": "email deliverability",
        "proposed_title": "Email Deliverability: A Practitioner's Guide to Reaching the Inbox",
        "intent": "informational",
        "volume": 1900,
        "difficulty": 42,
        "notes": "Head term — make this the canonical hub"
      },
      "support_pages": [
        {
          "primary_keyword": "email deliverability checklist",
          "proposed_title": "Email Deliverability Checklist: 12 Things to Check Before You Hit Send",
          "intent": "informational",
          "volume": 210,
          "difficulty": 22,
          "parent_cluster": "Email deliverability",
          "notes": ""
        }
      ],
      "long_tails": [
        {"keyword": "how to improve email deliverability rate", "parent_seed": "email deliverability", "intent_guess": "informational"}
      ]
    }
  ]
}
```

The script will produce:
- **Pillars tab:** one row per cluster. Columns: cluster_name, primary_keyword, proposed_title, intent, volume, difficulty, support_page_count, notes.
- **Support tab:** one row per support page. Columns: parent_cluster, primary_keyword, proposed_title, intent, volume, difficulty, notes.
- **Long-tails tab:** one row per long-tail. Columns: keyword, parent_seed, parent_cluster, intent_guess.

Save the file to the current workspace's `outputs/` folder (create it if it doesn't exist). Name it `seo-content-plan-YYYY-MM-DD.xlsx`.

## Quality bar

Every plan must pass these checks before delivery:

1. **Every cluster has exactly one pillar page** and at least 3 support pages. No orphan pillars.
2. **No duplicate primary keywords** across pillars or support pages. A keyword appears at most once as a primary target.
3. **Intent is assigned** to every pillar and support page (one of: `informational`, `investigational`, `transactional`, `navigational`). Long-tails get a best-guess tag but it's not load-bearing.
4. **Cluster names are domain-native.** "Email deliverability" not "Marketing Stuff Bucket 2". The cluster name should read like a section of the sitemap.
5. **Long-tails actually expand the seed.** If the seed is "email deliverability", "email deliverability checklist" is fine but "email" alone is not a valid long-tail.
6. **Metadata is preserved.** If the input had volume/KD columns, those values flow through to the output — don't drop them.

## What to do with what's NOT in the plan

Keep a running list (in memory during the run, then print at the end) of seeds that were:
- **Dropped as duplicates** (near-duplicate of another seed — note which one it merged into)
- **Out-of-scope for the ICP** (e.g. a "CRM software" seed in an email-marketing-tool run)
- **Too broad to cluster meaningfully** (e.g. "AI")

Print this at the end of the run as a brief debrief so the user can decide whether to push back on any of the judgment calls.

## Responding to the user

After the XLSX is saved, reply with a short summary:
- Number of clusters, pillars, support pages, long-tails
- The ICP context used
- The path to the saved XLSX file
- The debrief list of dropped/out-of-scope seeds

Don't recap the methodology — the user doesn't need to read back what they asked for.

## Reference files

Read these when relevant — don't load them all at the start:

- `references/long-tail-patterns.md` — Concrete patterns for expanding a seed into 6–12 long-tails. Read before step 4.
- `references/clustering-heuristics.md` — Rules of thumb for grouping keywords into clusters. Read before step 5, especially if the input has >40 seeds.
- `references/aeo-query-research.md` — The alternate AEO / competitive query-gap workflow described above. Read this instead of the two files above when the user wants buyer-intent query research and competitive-gap tiering rather than keyword clustering.
