# Human Voice — Final Pass

This is the last pass before delivery. Run it after every other checklist item is complete. Its purpose is not detection. The other reference files handle detection. This file is about rewriting. Every technique here is an active transformation you apply to the draft.

If the draft still reads like AI output after passing the banned words list, the structural checks, and the tone rules, the problem is not individual words or formatting. The problem is texture. AI text has a recognizable texture: even distribution of attention, consistent emotional temperature, predictable paragraph shapes, and a lack of the small irregularities that make human writing feel alive. This pass breaks that texture.

## 1. The cold open rewrite

Read the first two sentences of the piece. If they could introduce any article on any vaguely related topic, rewrite them. The opening must be specific to this exact piece and no other.

**AI texture:** "Rate limiting is an essential technique for protecting APIs from abuse and ensuring fair resource allocation across clients."

**Human rewrite:** "Your API is going to get hit by a bot at 3 AM on a Saturday. Rate limiting decides whether that bot takes down your service or just gets a 429."

The rewrite works because it's situation-specific, implies experience, and puts the reader in a concrete moment. The AI version works as a Wikipedia lede. That's the problem.

**Technique:** Start with a consequence, a scenario, or a claim. Never start with a definition or a category statement.

## 2. The conviction injection

Find every paragraph that presents options without recommending one. Rewrite to lead with the recommendation, then explain why, then acknowledge the exception.

**AI texture:** "There are several approaches to rate limiting, each with different tradeoffs. Fixed window is simpler to implement, while sliding window provides smoother rate enforcement. Token bucket offers flexibility for burst traffic. The best choice depends on your requirements."

**Human rewrite:** "Use sliding window. It's marginally harder to implement than fixed window, but it eliminates the burst-at-boundary problem that will otherwise page you at 2 AM. The only case for token bucket is if you need to allow controlled bursts, like a CI system that batches API calls."

The AI version is a menu. The human version is advice. Developers came here for advice.

**Technique:** For every comparison or evaluation, write this sentence first: "If I were building this today, I would use X because Y." Then edit from there. You can soften it, but the opinion must survive.

## 3. The asymmetry pass

Read through the piece and check whether every section gets roughly equal depth. If they do, the piece has AI texture. Real writers spend more time on the parts they find interesting, surprising, or hard. They skim the obvious parts.

**Technique:** Pick the one section that contains the most surprising or counterintuitive insight. Expand it by 30%. Then pick the most obvious section and cut it by 30%. The resulting unevenness is a signal of human judgment. This is not about word count balance. It is about attention distribution.

## 4. The specificity ratchet

Go through every paragraph and find the most generic sentence. Replace it with the most specific version you can write.

**AI texture:** "This can lead to performance issues in production environments."

**One turn of the ratchet:** "This adds roughly 15ms of latency per request."

**Two turns:** "This added 15ms of latency per request in our load test (10k concurrent connections, c5.xlarge, us-east-1), which pushed p99 past our 200ms SLO."

You don't always need two turns. But you always need at least one. Zero specificity in a technical claim means the sentence shouldn't exist.

**Technique:** Every paragraph must contain at least one proper noun, one number, or one named tool/library/version. If it doesn't, the paragraph is operating at a level of abstraction that reads as AI-generated.

## 5. The sentence shape audit

Copy five consecutive sentences from the middle of the draft. Look at them as shapes. How many words in each?

AI texture tends to produce sentences of 15–25 words with remarkably consistent length. Human writing is jagged: a 6-word sentence, then a 32-word sentence, then 11, then 28, then 8.

**Technique:** After every sentence longer than 20 words, write one under 10. After every complex, multi-clause sentence, write a blunt one. Vary paragraph length too. A one-sentence paragraph after a dense four-sentence paragraph creates visual and cognitive rhythm.

If you find three consecutive sentences within five words of each other in length, rewrite at least one of them.

## 6. The transition deletion

Find every sentence that exists solely to connect two paragraphs. Sentences like "With that in mind, let's look at how this works in practice" or "Now that we understand the theory, we can turn to implementation."

Delete them. Start the next paragraph with its actual first point. If the jump feels abrupt, that's fine. Developers are used to jumping. The connecting tissue that AI inserts reads as filler because it is filler.

**Technique:** Read the last sentence of a paragraph and the first sentence of the next. If the second paragraph makes sense without a transition, the transition shouldn't exist. If it doesn't make sense, the problem is usually paragraph ordering, not a missing transition sentence.

## 7. The "says who" pass

Find every claim that lacks attribution. Not just data claims (those should have been caught in earlier passes) but opinion claims and characterizations.

**AI texture:** "This is widely considered the best approach." "Most teams find that..." "The consensus in the community is..."

Who considers it? Which teams? What community? If you can't name the source, rewrite as a direct personal statement: "I'd recommend this approach because..." or drop the authority claim entirely and let the reasoning speak for itself. Anonymous consensus is an AI writing tic. Real writers either cite someone or own the opinion.

## 8. The parenthetical injection

Human writers use parentheticals, asides, and mid-sentence qualifications. AI text almost never does. It produces clean, complete sentences with no interruptions.

**Technique:** Find two to three places in the draft where a brief aside would add value. These are moments where the writer would naturally add context that's relevant but not worth a full sentence.

**Examples:** "Redis (or Valkey, if you've made the switch) handles this well." "The official docs recommend approach A, though their example (last updated in 2021, notably) uses a deprecated API." "We benchmarked this on c5.xlarge instances (the cheapest option that didn't throttle network I/O in our tests)."

Don't overdo it. Two to four parentheticals per 1,000 words is enough. The goal is to break the clean-sentence pattern, not to make the text hard to read.

## 9. The "actually" test

Read each section and ask: does this section contain something the reader doesn't already know, or something that contradicts what they might assume? If neither, the section is confirming conventional wisdom, and AI is very good at confirming conventional wisdom. That's why it reads as AI.

**Technique:** Every section needs at least one of these: a specific fact the reader probably didn't know, a recommendation that goes against the default assumption, a concrete failure story, or an explicit "the docs say X but in practice Y." If a section has none of these, it needs rewriting or cutting. Content that only confirms what the reader already believes is not worth publishing.

## 10. The final read

Read the entire piece from top to bottom as a skeptical senior engineer who has seen too many mediocre blog posts. At every paragraph, ask: "Would I keep reading?" If the answer is no, that paragraph is where the piece loses the reader.

The most common failure point is paragraph three to five. The opening was rewritten to be specific (step 1), but then the text settles into an AI-generated cruise altitude of even, balanced, noncommittal prose. The voice established in the opening must carry through the entire piece. If it doesn't, the reader notices the shift and checks out.

**Technique:** Flag any paragraph where the voice noticeably flattens or where you'd personally start skimming. Those paragraphs get rewritten or cut. The piece should hold attention at a consistent level from beginning to end. That doesn't mean every paragraph is dramatic. It means every paragraph earns its place.

## Checklist summary

Before marking a piece as ready for delivery, confirm:

1. Opening is situation-specific, not a generic definition or category statement.
2. Every comparison or evaluation contains a clear recommendation.
3. Section depths are deliberately uneven, reflecting editorial judgment.
4. Every paragraph contains at least one proper noun, number, or named tool.
5. No three consecutive sentences are within five words of each other in length.
6. All pure-transition sentences have been deleted.
7. Anonymous authority claims ("widely considered," "most teams") have been replaced with named sources or owned opinions.
8. Two to four parenthetical asides exist per 1,000 words.
9. Every section contains at least one fact, counter-assumption, or practical insight the reader probably didn't already have.
10. The voice established in the opening holds through the full piece with no flattening.
