# Editing Checklist

Run these checks in order on every draft before delivery.

## General pass

1. **Cut the bookends.** Delete the intro restatement and concluding summary. See if anything is lost.
2. **Ctrl+F the banned list.** Open `01-banned-words.md`. Search for every flagged word. Replace or delete each hit.
3. **Check list uniformity.** If all bullets are the same shape and length, break the pattern.
4. **Find the opinion.** If the piece doesn't take a clear position anywhere, it needs one.
5. **Verify specificity.** Every claim of "improved performance" or "better developer experience" needs a concrete anchor — a number, a comparison, an example.
6. **Read it aloud.** Listen for metronome rhythm, signposting, and filler transitions.
7. **Would a human bother writing this sentence?** If it exists only to smooth a transition or restate something obvious, delete it.
8. **Check the ratio.** If more than ~30% of the text is setup, context-setting, and recapping, the piece is underweight on substance.

## Developer content pass

9. **Run the code.** Every sample should execute (or be explicitly marked as pseudocode). Check versions, imports, dependencies.
10. **Hunt for "simply" and "just."** Ctrl+F both. Each instance is hiding complexity or is unnecessary filler. Delete or expand.
11. **Check for error paths.** If no code sample shows a failure mode, add one.
12. **Verify you're past the docs.** For each section: "Does this tell the reader something the official docs don't?" If not, cut it or add the gotcha, opinion, or experience.
13. **Check audience calibration.** Read the first two paragraphs and the most complex section. If they feel written for different people, you have an audience problem.
14. **Find the "don't use this when."** If the piece recommends a technology or pattern without saying when it's the wrong choice, add that section.
15. **Name the stack.** If any guidance says "in your framework of choice" or "using your preferred library," replace with a concrete implementation.

## Tone and style pass

16. **Sentence rhythm.** Short sentences under technical stress, longer for context. If three consecutive sentences are the same length, rewrite.
17. **Em-dash count.** Maximum one per paragraph. Ctrl+F for "—" and fix any paragraph with two or more.
18. **No rhetorical question openers.** If any H2 or H3 section opens with a question, rewrite as a statement.
19. **Bullets vs. prose.** Any bulleted list where items are full sentences or paragraphs should be rewritten as prose.
20. **Number style.** Spelled out under 10, digits for 10+. Percentages use % symbol, never "percent."
21. **Oxford comma.** Check every list of three or more items.

## Source material pass (when working from provided sources)

22. **Exact figures preserved.** Every data point from source material should appear with its original precision. No rounding, no "approximately."
23. **Quotes attributed.** Every direct quote names the person, their role, and context.
24. **No vague paraphrasing.** If you wrote "research shows" or "studies indicate," go back to the source and get the specific claim.
25. **Conflicts flagged.** If sources disagree, both positions are presented with attribution.

## Format pass (final)

26. **Metadata block present.** YAML block at top with primary keyword, secondary keywords, word count target, author, status.
27. **Time-to-read line present.** `*X min read*` on its own line directly below the H1. Value equals `ceil(body_word_count / 225)`. Recalculate after editing — do not leave a stale number.
28. **TL;DR present and earns its place.** Two to four sentences, prefixed with `**TL;DR —**`, placed between the time-to-read line and the first H2. Leads with the answer, names specific tools/numbers, works as a featured snippet, and contains no product plug. See `08-output-format.md`.
29. **Code blocks tagged.** Every fenced code block has a language identifier. No untagged fences.
30. **Editor notes block present.** HTML comment at bottom with all five sections: fact-checks, missing visuals, internal links, SEO meta description, confirmation items for reviewer.
31. **Heading hierarchy clean.** H1 → H2 → H3, no skipped levels, no H4+ unless piece exceeds 3,000 words.

## Visual pass

32. **Density check.** Roughly one visual per 400–600 words of body. A 1,800-word piece needs three to four. Count your `<!-- VISUAL -->` markers.
33. **Architecture = visual.** Any section describing how components connect or how data flows must have a diagram placeholder. No exceptions.
34. **Before/after = visual.** Any section showing the effect of a change (performance, code, config) needs a side-by-side visual.
35. **No decorative visuals.** Every `<!-- VISUAL -->` marker has a "why it's needed" that explains what the visual communicates that prose doesn't. If you can't articulate it, cut the placeholder.
36. **Descriptions are production-ready.** Each visual description is specific enough that a designer could produce it without reading the full article. Not "architecture diagram" but "request flow from client through rate limiter to Redis, showing the 429 branch."
37. **Editor notes mirror body.** The "Missing visuals" section in editor notes lists every `<!-- VISUAL -->` marker with line reference and priority.

## SEO pass (for content targeting organic search)

38. **Primary keyword placement.** Appears in H1, first 100 words (the TL;DR counts), at least one H2, meta description, and URL slug.
39. **TL;DR is the extractable answer.** The TL;DR reads cleanly when lifted into a featured snippet or AI overview: direct, specific, self-contained. No pronouns that depend on the body ("this approach," "that tool").
40. **H2s are searchable.** Each H2 reads as a topic statement or question someone might search. No vague labels like "Comparison" or "Details."
41. **Extractable answers.** Each major section opens with a direct one-to-two sentence answer before expanding. This is the sentence AI engines will pull.
42. **External links to primary sources.** All outbound links go to docs, papers, or repos. No aggregator blogs.
43. **Internal link suggestions.** Two to five listed in editor notes. Product-docs internal links follow `11-product-context.md`.
44. **Meta description quality.** 150–160 characters, contains primary keyword, uses a verb, doesn't repeat the title.
45. **URL slug.** Short, keyword-containing, no filler words, no dates unless time-bound.
46. **Long-tail capture.** Error messages, troubleshooting, or "when not to use this" sections are included where relevant.

## Product pass (for content that mentions the product)

Skip this section only if the piece makes zero reference to the product. Otherwise every check is mandatory.

47. **95/5 ratio holds.** At least 95% of the body is reader-value content. Product mentions fit in the remaining ~5%, placed where they add information, not where they'd be convenient promotion. See `11-product-context.md`.
48. **TL;DR is product-free.** No product mention in the TL;DR. The TL;DR belongs to the reader.
49. **Every product claim is sourced.** Features, behaviors, and concepts named match the current product docs. If a claim can't be pinned to a docs page, cut it or move it to the reviewer confirmation items.
50. **Internal links use the canonical map.** Product-docs links follow the URL table in `11-product-context.md`. No invented paths, no marketing-page substitutions where a docs page exists.
51. **No banned product overclaims.** Search for the phrases flagged in `11-product-context.md` (e.g., "the only platform," "fully automated," "complete evaluation"). Rewrite or delete.

## Human voice pass (FINAL — run after all other passes)

Read `10-human-voice-pass.md` and apply every technique. This is not optional. This is the gate between "clean AI text" and "text that reads like a human wrote it." Confirm all 10 before marking the piece as ready:

52. **Cold open.** First two sentences after the TL;DR are situation-specific. Not a definition, not a category statement.
53. **Conviction present.** Every comparison or evaluation leads with a recommendation, not a menu of options.
54. **Asymmetry.** Section depths are deliberately uneven. The most interesting section is longer. The most obvious section is shorter.
55. **Specificity ratchet.** Every paragraph contains at least one proper noun, number, or named tool/library/version.
56. **Sentence shape.** No three consecutive sentences are within five words of each other in length.
57. **Transitions deleted.** No sentence exists solely to connect two paragraphs.
58. **"Says who" cleared.** No anonymous authority claims remain. Every opinion is attributed or owned.
59. **Parentheticals present.** Two to four asides per 1,000 words break the clean-sentence pattern.
60. **"Actually" test passed.** Every section contains something the reader didn't already know or that contradicts a default assumption.
61. **Voice holds.** The voice from the opening carries through the full piece. No flattening in the middle paragraphs.
