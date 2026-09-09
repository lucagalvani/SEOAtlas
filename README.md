# SEOAtlas

[Claude Code](https://claude.com/claude-code) skills for SEO-led content teams — planning what to write, then writing it.

Two skills live here:

| Skill | What it does |
| --- | --- |
| [`seo-cluster-planner`](skills/seo-cluster-planner/) | Turns a raw keyword list into a hub-and-spoke content plan, or finds high-intent buyer queries nobody has answered yet |
| [`case-study-writer`](skills/case-study-writer/) | Writes a publication-ready B2B customer case study as a clean HTML artifact, from source docs and drafts |

## seo-cluster-planner

Two modes, one skill:

- **Keyword clustering** — give it a list of keywords (pasted, a CSV/XLSX export from Ahrefs/Semrush/Search Console, or a linked Google Sheet). It expands each seed into long-tail variants, clusters everything into pillar pages and supporting pages, and writes a three-tab XLSX (`Pillars`, `Support`, `Long-tails`).
- **AEO / competitive query-gap research** — no keyword list needed. It reasons from the customer's buying journey (company size, budget, integrations, named competitors) to construct the queries a real buyer would type or ask an AI assistant, checks who already answers each one, and tiers them by competitive gap — with zero-competition comparison pages ("X vs Y") flagged as the highest-priority find.

Both modes are domain-agnostic: it asks for the ICP/audience up front rather than assuming one.

```
skills/seo-cluster-planner/
  SKILL.md                            — main skill definition, both modes
  references/long-tail-patterns.md    — patterns for expanding a seed into 6–12 long-tails
  references/clustering-heuristics.md — rules for grouping keywords into pillar/support clusters
  references/aeo-query-research.md    — the AEO / competitive query-gap workflow
  scripts/build_plan_xlsx.py          — builds the 3-tab XLSX from a JSON plan (validates as it writes)
```

## case-study-writer

Give it the source material — PDFs, a Google Doc, a rough draft, interview notes — and it produces a case study as an HTML artifact against a fixed 12-section structure: meta line, title, lede, four-metric stats band, situation, challenge, what the customer changed, business impact, sourced quote, what's next. Two sections covering adversarial/security testing are optional and only appear when the story calls for them.

The editorial rules are the point. It reconciles every figure in a draft against the sources before writing, refuses to fabricate a quote (a missing quote beats a placeholder one), frames vulnerability testing as a standard the product was held to rather than gaps that were found, and holds the whole document to one voice.

```
skills/case-study-writer/
  SKILL.md                            — structure, editorial rules, and output CSS
```

## Install

Clone the repo, then copy the skills you want into your Claude Code skills directory, each under its own folder:

```bash
git clone https://github.com/lucagalvani/SEOAtlas.git
cp -r SEOAtlas/skills/* ~/.claude/skills/
```

Or just one of them:

```bash
cp -r SEOAtlas/skills/seo-cluster-planner ~/.claude/skills/
```

`seo-cluster-planner`'s `build_plan_xlsx.py` needs `openpyxl`:

```bash
pip install openpyxl
```

Restart Claude Code, or start a new session, so it picks up the new skills.

> **Upgrading from an earlier clone?** The skills used to sit at the repo root, so the old install copied everything into `~/.claude/skills/seo-cluster-planner/`. That still works — nothing about the skill changed — but the paths above are the current ones.

## Use

Paste a keyword list, upload a CSV/XLSX export, or just ask:

```
cluster these keywords into a content plan
```

for the AEO mode:

```
find the buyer-intent queries we're not covering compared to [competitor]
```

or, with source docs attached:

```
write a case study from these
```

Each skill asks for the context it needs up front — the ICP for a plan, the source reconciliation for a case study — then runs the full workflow.

## License

MIT — see [LICENSE](LICENSE).
