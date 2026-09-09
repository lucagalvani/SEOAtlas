# SEO for Developer Content

This file covers on-page SEO as it applies to writing technical articles for developer audiences. It does not cover site-level technical SEO (crawlability, Core Web Vitals, schema markup). That's engineering work, not writing work.

## Keyword strategy

### Primary and secondary keywords

Every piece has one primary keyword and two to five secondary keywords. These are set in the metadata block before writing begins (see `08-output-format.md`).

The primary keyword should appear in the H1 title, the TL;DR block (which doubles as the first 100 words and the extractable answer for AI overviews — see `08-output-format.md`), at least one H2 heading, the URL slug, and the meta description. Do not force it. If the natural phrasing of a sentence doesn't accommodate the keyword, write the better sentence. Keyword density is not a metric worth optimizing for directly.

Secondary keywords should appear naturally throughout the body. They are there to signal topical depth, not to be checked off a list.

### Intent-first keyword selection

Developer searches fall into four intent categories. Match the content type to the intent:

**Navigational:** "Express.js docs," "Stripe API reference." You are not competing here. Don't target these.

**Informational:** "how does connection pooling work," "what is eventual consistency." Write explainers. Lead with the answer, not the definition.

**Investigational:** "connection pooling vs. thread-per-request," "Kafka vs. RabbitMQ for event streaming." Write comparisons. Lead with the decision criteria, not the product descriptions.

**Transactional:** "best observability tool for Kubernetes," "rate limiting library Node.js." Write evaluations. Lead with the recommendation, then justify it.

Most developer content targets informational or investigational intent. If you're unclear on the intent behind a keyword, search it and look at what's ranking. That tells you what Google thinks the intent is.

### Long-tail and question-based keywords

Developer search queries are often long-tail and phrased as questions or error messages. These are high-value targets because they signal specific, actionable intent and lower competition.

Target these formats: "how to [verb] [technology] [context]" (e.g., "how to handle rate limiting in Express.js with Redis"), "[error message] [technology]" (e.g., "ECONNREFUSED Redis Docker"), "[technology A] vs [technology B] for [use case]."

Use Google's "People Also Ask" and autocomplete suggestions to find question clusters around your primary keyword. Address the most relevant questions as H2 or H3 sections within the piece.

## On-page structure for search

### Title (H1)

The H1 is the most important on-page signal. Rules:

1. Include the primary keyword, ideally near the front.
2. Under 60 characters for full display in SERPs.
3. Communicate the value proposition or outcome, not just the topic. "Implementing Rate Limiting in Express.js (With Redis and Sliding Window)" beats "Rate Limiting Guide."
4. Avoid clickbait. Developers penalize it socially and Google penalizes it algorithmically.

### Meta description

Written in the editor notes block (see `08-output-format.md`). Rules:

1. 150 to 160 characters.
2. Contains the primary keyword.
3. Communicates the specific outcome or takeaway. Use a verb: "Learn how to...," "Compare...," "Fix the..."
4. Do not repeat the title. The meta description expands on what the title promises.

### URL slug

Short, descriptive, hyphen-separated. Contains the primary keyword. No dates unless the content is explicitly time-bound (e.g., "2026 benchmarks"). No filler words (a, the, to, for, in) unless removing them makes the slug unreadable.

Good: `/rate-limiting-express-redis`
Bad: `/a-comprehensive-guide-to-implementing-rate-limiting-in-express-js-with-redis-in-2026`

### Heading hierarchy for SEO

H2s are your section-level keyword targets. Each H2 should map to a subtopic or question the reader might search for independently. H3s support the H2 above them and do not need to carry keyword weight.

Write H2s as clear topic statements or questions. "Sliding Window vs. Fixed Window" is a better H2 than "Comparison of Approaches" because someone might search the former verbatim.

Do not stuff keywords into headings. A heading that reads awkwardly to serve SEO serves neither the reader nor the search engine.

## Content depth signals

### Topical authority markers

Google and AI search engines evaluate topical depth. The following signals strengthen it:

1. **Specific data points with sources.** Cite benchmarks, papers, and official docs. Link to them. This creates outbound link signals and demonstrates E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness).
2. **Code samples that work.** Functional code signals expertise. Broken or pseudocode-only content signals shallow coverage.
3. **Comparison tables.** Structured comparative data ranks well in featured snippets and AI overviews. Use tables from `08-output-format.md` for any side-by-side evaluation.
4. **"When not to use this" sections.** Counter-recommendations signal depth that thin content doesn't have. These sections also capture search intent for queries like "[technology] downsides" or "[technology] problems."
5. **Error messages and troubleshooting.** Including real error messages and their fixes captures long-tail searches directly. Developers search error messages verbatim.

### Content length

There is no magic word count. The right length is however many words it takes to fully cover the topic for the target audience without padding. That said, for competitive informational keywords, pieces under 1,200 words rarely rank on page one. For investigational keywords (comparisons, evaluations), 1,800 to 3,000 words is typical for top-ranking content.

Padding to hit a word count is worse than publishing a shorter piece. Google's helpful content system explicitly penalizes content that exists primarily for search engines rather than readers. Write for the reader. The length will follow.

## Internal and external linking

### Internal links

Every piece should include two to five internal links to other content on the same site. These go in the editor notes block as suggestions if the full content library is not available.

Internal links serve two purposes: they distribute page authority, and they reduce bounce rate by giving the reader somewhere to go next. Link from contextually relevant sentences, not from generic "related articles" footers.

**Anchor text.** Never use the exact article title as the link text. Title-as-anchor reads like a footnote citation and breaks the flow of prose. Write anchor text that describes what the reader will get from clicking, using the words that fit the surrounding sentence. The title can inform the anchor text, but the anchor text should be a phrase that would make sense if the link were removed.

Good: "the calibration loop covered in [How to optimize your LLM Judge](…)" → anchor: "How to optimize your LLM Judge" is the title but it also functions as a description of the destination — acceptable when the title is already descriptive. Avoid: "See [LLM as a Judge: The Complete Guide](…) for details" — this is a dead drop. Better: "…for the full pipeline setup, [start with the complete guide](…)."

The test: if you read the anchor text aloud in the sentence without the link, does the sentence still communicate something? If yes, the anchor text is working. If the sentence only makes sense because the link is there, the anchor text is a crutch.

### External links

Link to primary sources: official documentation, research papers, GitHub repos, RFC specs. Do not link to competitors' blog posts unless they are the canonical source for a specific claim.

External links to authoritative sources strengthen E-E-A-T signals. Do not avoid them out of fear of "sending traffic away." Search engines reward content that connects readers to the best information, even when it lives elsewhere.

## AI search and GEO (Generative Engine Optimization)

AI answer engines (Google AI Overviews, ChatGPT search, Perplexity) are now a significant discovery channel for developer content. They use RAG (Retrieval Augmented Generation) to pull content chunks and synthesize answers.

### What makes content citable by AI engines

1. **Direct, extractable answers.** The TL;DR (see `08-output-format.md`) is the primary extractable answer for the whole piece. Within the body, also open each major section with a clear factual statement before expanding. AI systems pull the first complete answer they find, not the nuanced discussion three paragraphs down.
2. **Structured headings as questions.** H2s phrased as questions (e.g., "How does sliding window rate limiting work?") are directly matchable to user queries.
3. **Tables and lists for comparative data.** AI systems extract structured data more reliably than prose comparisons.
4. **Named entities over generic terms.** "Redis 7.2" is more citable than "a caching layer." "Express.js 5.x" is more citable than "your web framework."
5. **Concise definitions early.** If the piece introduces a concept, define it in one to two sentences within the first paragraph of that section. AI engines favor early, tight definitions.

### What AI engines skip

Decorative intros, personal anecdotes that don't contain data, rhetorical questions, and vague claims without figures. This aligns with the anti-slop rules in `03-tone-and-voice.md`. Writing that's good for developers is also good for AI retrieval.

## SEO checklist for writers

Run this after the main editing pass in `06-editing-checklist.md`:

1. Primary keyword appears in: H1, first 100 words, at least one H2, meta description, URL slug.
2. Secondary keywords appear naturally in the body (not forced).
3. H2s are searchable topic statements or questions, not vague labels.
4. At least one comparison table or structured data element exists for investigational content.
5. All external links point to primary sources (docs, papers, repos), not aggregator blogs.
6. Internal link suggestions are listed in editor notes (two to five minimum).
7. Meta description is 150 to 160 characters, contains primary keyword, uses a verb.
8. URL slug is short, keyword-containing, no filler words.
9. Error messages or troubleshooting sections are included where relevant (long-tail capture).
10. Each major section opens with a direct, extractable answer before expanding into nuance.
11. No internal link uses the exact article title as its anchor text. Anchor text is a contextual phrase that works in the surrounding sentence.
