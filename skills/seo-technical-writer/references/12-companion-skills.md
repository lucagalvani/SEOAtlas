# Companion skills

This file is the index of skills that sit next to the writing flow. Each one is triggered by its own description rather than called explicitly. Read this file when planning a task, so the right skill fires — or so none does.

Companion skills are additive to the reference files in this folder (`01-banned-words.md` through `11-product-context.md`). The writing rules in those files apply **inside** whatever a skill produces. A skill doesn't exempt a draft from the tone, voice, or product-mention rules.

## How to read this file

For each skill:

- **What it does** — the job the skill performs.
- **When to use it** — trigger phrases and task shapes. If a user request matches these, the skill should fire.
- **Inputs** — what the skill accepts.
- **Outputs** — what it produces and where the deliverable lands.
- **Do not use when** — out-of-scope cases, so an adjacent-looking task doesn't load the wrong skill.

---

## seo-cluster-planner

Ships in this repo, at `skills/seo-cluster-planner/`.

**What it does.** Turns a raw keyword list into a hub-and-spoke content plan — expands each seed into long-tail variants, clusters everything into pillar pages and supporting pages, and produces an XLSX with three tabs (Pillars, Support, Long-tails). An alternate AEO mode reasons from the buying journey to find high-intent queries nobody has answered, tiered by competitive gap.

**When to use it.** When the user has a list of keywords (their own research, an Ahrefs/Semrush export, GSC data, a Google Sheet) and needs a structured plan that says what to write, in what order, and how pages link together. Trigger phrases: "cluster these keywords", "build a content plan", "pillar and support pages", "long-tail keywords from this list", "topic map", "content calendar from keywords". For the AEO mode: "AEO", "answer engine optimization", "buyer-intent queries", "queries we're not covering", "competitive content gaps".

**Inputs.**
- Pasted keywords (one per line, comma-separated, or bulleted).
- Uploaded file (`.xlsx`, `.xls`, `.csv`, `.tsv`) with optional volume, difficulty, intent, or cluster columns.
- A linked Google Sheet (read via connector if available; otherwise the skill asks for an export).
- For AEO mode: no keyword list at all — the ICP, competitors, and buying-journey context instead.

**Outputs.** A single `.xlsx` saved to `outputs/` as `seo-content-plan-YYYY-MM-DD.xlsx` with three tabs: Pillars (one row per cluster), Support (one row per supporting page), Long-tails (one row per long-tail). Plus a short in-chat debrief listing any seeds dropped as duplicates, out-of-scope, or too broad to cluster. AEO mode returns a tiered query list instead.

**Do not use when.** The user wants an individual article drafted — that's this skill's own writing flow, starting at `05-dev-content.md`. Also not for a keyword-research run from scratch with no seed list and no ICP context.

**Where it hands off.** A finished plan is the input to the writing flow: take one row (target keyword, intent, pillar or support role, the cluster it belongs to) and draft against it. The cluster gives you the internal links, which is half of check 43 in `06-editing-checklist.md` already answered.

---

## Other skills worth wiring up

These aren't in this repo, but the writing flow assumes something fills each slot. Add an entry in the format above for whichever ones you install.

| Slot | What it does | Fires when |
|---|---|---|
| **Article → social** | Turns a finished draft into per-platform post ideas — angles, hook lines, the source beat each rides on. Ideas, not finished posts. | After a draft is done and the user wants distribution. |
| **Article visuals** | Hero images, technical diagrams, data charts, OG and square social cards, inline explainer SVGs. Picks the generation method per type. | Only on explicit request. Never auto-generate visuals while the user is writing copy. |
| **Tracker sync** | Maps a finished cluster plan into rows matching a content-tracker spreadsheet's column schema. | Right after a plan is generated, or "add this to the tracker". |

## Keeping this file current

Whenever a skill is added, add an entry here with the same structure. If a skill is retired or renamed, update the entry in place rather than deleting it — users may reference the old name.

Skills are not a substitute for the writing rules in `01`–`11`. Every draft a skill produces still runs through `06-editing-checklist.md` and ends with `10-human-voice-pass.md` before delivery.
