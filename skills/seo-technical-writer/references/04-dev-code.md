# Code Sample Artifacts

## Toy code that teaches nothing

AI defaults to trivially simple examples: hello world, to-do CRUD, a `User` class with `name` and `email`. These confirm syntax but don't demonstrate the concept.

**Fix:** Write code that mirrors a real decision. If explaining connection pooling, show a pool under contention — not an isolated `getConnection()` call. The code should make the reader think "oh, that's how I'd actually use this."

## Code without consequences

AI examples almost never show what happens when things go wrong. No error paths, no edge cases, no "here's what this looks like when the database is down."

**Fix:** Include at least one non-happy-path example per code section. Show the error. Show the timeout. Show the race condition. That's where the real teaching happens.

## Comment-stuffed code

Over-commenting to the point of redundancy:

```
// Get the user from the database
const user = await db.getUser(id);
// Check if user exists
if (!user) {
  // Return 404 error
  return res.status(404).json({ error: 'Not found' });
}
```

**Fix:** Comments explain *why*, not *what*. If the code is readable, the "what" is self-evident. Reserve comments for non-obvious decisions, workarounds, and context the code alone can't communicate.

## Sanitized variable names and structure

AI code is perfectly formatted, perfectly named, perfectly organized. Real codebases have legacy naming, pragmatic shortcuts, context-dependent structure.

**Fix:** Use realistic naming. Reference actual libraries and versions. Include occasional pragmatic shortcuts a senior dev would recognize. Don't over-abstract a 10-line script into three files with an interface.

## Framework-agnostic vagueness

Describing concepts in abstract, framework-neutral terms. "Implement middleware that intercepts the request" — in what? Express? Fastify? Hono?

**Fix:** Pick a stack and commit. For general audiences, show two concrete implementations rather than one abstract description.

## Missing dependency and version context

Code samples without library versions, runtime versions, or peer dependencies. Looks right but doesn't run.

**Fix:** Pin versions. Start code sections with the install command. If behavior changed between v2 and v3, say so. A working `package.json` snippet beats a paragraph of explanation.

## Outdated patterns presented as current

Training data lag means code may use deprecated APIs, old syntax, or abandoned patterns. `var` instead of `const/let`. Class components instead of hooks. `moment.js` instead of modern alternatives.

**Fix:** Verify every sample against the current stable version. Check changelogs and migration guides. If unsure whether a pattern is current, say so explicitly.
