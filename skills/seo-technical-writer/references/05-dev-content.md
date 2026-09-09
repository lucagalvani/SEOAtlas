# Developer Content — Structure, Substance & Audience

## Structural patterns

### The "What / Why / How" template on repeat

AI defaults to the same three-act structure for every article. Fine occasionally, predictable when every piece follows the same skeleton.

**Fix:** Let purpose dictate structure. Troubleshooting guide → lead with symptoms. Comparison piece → lead with decision criteria. Migration guide → lead with what breaks.

### Listicles disguised as articles

"5 Best Practices for X" where each item gets two shallow paragraphs. Ranks for SEO, teaches nothing beyond the headings.

**Fix:** Go deep on each item. Show the anti-pattern, the fix, and *why* the fix works at the systems level. One well-explained practice beats seven platitudes.

### The false getting-started guide

"Getting Started with X" that covers installation and hello world, then stops. Reader finishes knowing X installs correctly but not how to use it for anything real.

**Fix:** End with the reader having built something small but real — something that demonstrates X's actual value proposition.

### Missing "when NOT to use this"

AI content almost never says when a tool or pattern is the wrong choice. Every technology is universally beneficial.

**Fix:** Every recommendation needs a counter-indication. "Don't use this if..." is the highest-value sentence in developer content.

## Substance problems

### Regurgitated docs

Rephrasing official documentation without adding experience, gotchas, or opinions on what the docs get wrong.

**Fix:** Assume the reader has skimmed the docs. Add what docs can't: real-world experience, failure stories, performance under load, integration pain points, opinions on API design choices.

### Benchmark-free performance claims

"X is faster than Y" with no numbers, methodology, or hardware context.

**Fix:** Show the benchmark. Specify hardware, dataset size, concurrency, measurement methodology. If you can't benchmark, qualify honestly: "In our testing with [context], we saw [result], but YMMV depending on [variables]."

### Missing operational context

Explaining how to build something without covering how to run, monitor, debug, or recover it. Content that stops at "deploy" is half the story.

**Fix:** For architecture/infrastructure content, address: how you know it's working, how you know it's broken, what the failure modes are, how you recover.

### Abstracting away the hard parts

Glossing over difficult aspects with "simply configure your database connection" or "just set up your CI/CD pipeline."

**Fix:** If it's actually simple, brevity proves it without the adjective. If it's not, walk through the hard part — that's the value.

## Audience calibration

### Talking down to seniors

Over-explaining fundamentals. Defining "API" in a piece about API gateway patterns.

**Fix:** State assumed knowledge once at the top. Write to that level consistently. Don't oscillate between beginner and advanced.

### Talking past juniors

Assuming knowledge the reader doesn't have. Jargon without context. Skipping "obvious" foundational steps.

**Fix:** If targeting intermediates, assume language fundamentals but not the specific library or pattern. Calibrate to the specific knowledge gap.

### One-audience-fits-all

Trying to serve beginners, intermediates, and seniors simultaneously. Serves none well.

**Fix:** Pick one segment. Write title, intro, and depth for that segment only. A piece for seniors doesn't include "What is Docker?" sidebars.

### Ignoring the reader's actual task

Writing about a technology in the abstract rather than addressing what the reader is trying to accomplish.

**Fix:** Frame around the task, not the technology. "Adding real-time notifications with WebSockets" > "Understanding WebSockets." The technology is the means; the task is what the reader cares about.
