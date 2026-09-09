# SEOAtlas

[Claude Code](https://claude.com/claude-code) skills for SEO-led technical content — deciding what to write, then writing it without it reading like AI wrote it.

| Skill | What it does |
| --- | --- |
| [`seo-cluster-planner`](skills/seo-cluster-planner/) | Turns a raw keyword list into a hub-and-spoke content plan, or finds high-intent buyer queries nobody has answered yet |
| [`seo-technical-writer`](skills/seo-technical-writer/) | Drafts and edits long-form developer content against a strict anti-AI-slop editorial standard |

They're built to hand off to each other: the planner produces a row (target keyword, intent, pillar or support role, cluster), and the writer drafts against it — the cluster supplies the internal links.

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

## seo-technical-writer

Writes for practitioners — engineers, platform and ML teams — and holds the draft to an editorial standard rather than a word count. The skill body carries the role, the core principles, and the non-negotiable tone rules; twelve reference files carry the detail, loaded only when a task needs them.

The anti-slop machinery is the point. A banned-words list for the first pass, structural anti-patterns for outlining, code-sample standards, a 51-item editing checklist, and a human-voice pass that runs last on every draft with no exceptions. On-page SEO and GEO formatting live in their own file, so a piece aimed at organic search gets its title and outline planned against them before drafting starts.

```
skills/seo-technical-writer/
  SKILL.md                              — role, principles, tone rules, output defaults
  references/01-banned-words.md         — delete-on-sight words and phrases
  references/02-structural-artifacts.md — structural and formatting anti-patterns
  references/03-tone-and-voice.md       — voice, hedging, sentence-level fixes
  references/04-dev-code.md             — code example standards
  references/05-dev-content.md          — structure, depth, audience calibration
  references/06-editing-checklist.md    — the 51-item editing pass
  references/07-source-material.md      — extracting from decks, papers, research
  references/08-output-format.md        — required markdown structure and metadata
  references/09-seo.md                  — keyword placement, headings, GEO, on-page checklist
  references/10-human-voice-pass.md     — the final de-slop rewrite, every draft
  references/11-product-context.md      — the 95/5 product-mention rule (template — fill in once)
  references/12-companion-skills.md     — which neighbouring skill fires, and where it hands off
```

`11-product-context.md` ships as a template. Fill in its three tables once for the product you write about — what it is, the claims its docs support, and the canonical URL map — and the plug rules, banned overclaims, and link placement rules apply as written.

## Install

Clone the repo, then copy the skills you want into your Claude Code skills directory, each under its own folder:

```bash
git clone https://github.com/lucagalvani/SEOAtlas.git
cp -r SEOAtlas/skills/* ~/.claude/skills/
```

Or just one of them:

```bash
cp -r SEOAtlas/skills/seo-technical-writer ~/.claude/skills/
```

`seo-cluster-planner`'s `build_plan_xlsx.py` needs `openpyxl`:

```bash
pip install openpyxl
```

Restart Claude Code, or start a new session, so it picks up the new skills.

> **Upgrading from an earlier clone?** `seo-cluster-planner` used to sit at the repo root, so the old install copied everything into `~/.claude/skills/seo-cluster-planner/`. That still works — nothing about the skill itself changed — but the paths above are the current ones.

## Use

Paste a keyword list, upload a CSV/XLSX export, or just ask:

```
cluster these keywords into a content plan
```

for the AEO mode:

```
find the buyer-intent queries we're not covering compared to [competitor]
```

then, with a plan row or a brief in hand:

```
write the pillar post for [keyword]
```

and on anything already drafted, by you or by a model:

```
edit this draft — full checklist, then the human voice pass
```

## License

MIT — see [LICENSE](LICENSE).
