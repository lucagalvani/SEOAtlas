# SEOAtlas

A [Claude Code](https://claude.com/claude-code) skill that turns a raw keyword list into a structured content plan — or, in its alternate mode, finds high-intent buyer queries that nobody has answered yet.

Two modes, one skill:

- **Keyword clustering** — give it a list of keywords (pasted, a CSV/XLSX export from Ahrefs/Semrush/Search Console, or a linked Google Sheet). It expands each seed into long-tail variants, clusters everything into pillar pages and supporting pages, and writes a three-tab XLSX (`Pillars`, `Support`, `Long-tails`).
- **AEO / competitive query-gap research** — no keyword list needed. It reasons from the customer's buying journey (company size, budget, integrations, named competitors) to construct the queries a real buyer would type or ask an AI assistant, checks who already answers each one, and tiers them by competitive gap — with zero-competition comparison pages ("X vs Y") flagged as the highest-priority find.

Both modes are domain-agnostic: it asks for the ICP/audience up front rather than assuming one.

## What's in here

```
SKILL.md                              — main skill definition, both modes
references/long-tail-patterns.md      — patterns for expanding a seed into 6–12 long-tails
references/clustering-heuristics.md   — rules for grouping keywords into pillar/support clusters
references/aeo-query-research.md      — the AEO / competitive query-gap workflow
scripts/build_plan_xlsx.py            — builds the 3-tab XLSX from a JSON plan (validates as it writes)
```

## Install

Clone this repo, then copy the whole thing into your Claude Code skills directory under its own folder:

```bash
git clone https://github.com/lucagalvani/SEOAtlas.git
mkdir -p ~/.claude/skills/seo-cluster-planner
cp -r SEOAtlas/* ~/.claude/skills/seo-cluster-planner/
```

`scripts/build_plan_xlsx.py` needs `openpyxl`:

```bash
pip install openpyxl
```

Restart Claude Code, or start a new session, so it picks up the new skill.

## Use

Paste a keyword list, upload a CSV/XLSX export, or just ask:

```
cluster these keywords into a content plan
```

or, for the AEO mode:

```
find the buyer-intent queries we're not covering compared to [competitor]
```

It asks once for the ICP/audience, then runs the full workflow and hands back either the XLSX path or a tiered query list — plus a debrief of what it dropped and why.

## License

MIT — see [LICENSE](LICENSE).
