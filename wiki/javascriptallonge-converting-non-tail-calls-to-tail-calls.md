---
page_id: javascriptallonge-converting-non-tail-calls-to-tail-calls
page_kind: source
summary: Chapter on converting non-tail-calls to tail-calls in JavaScript
sources: raw/javascriptallonge.pdf p.120-121
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Chapter on converting non-tail-calls to tail-calls in JavaScript, covering transformation techniques and examples.

## Key supported claims

- And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization (raw/javascriptallonge.pdf p.120-121).
- The obvious solution is push the 1 + work into the call to length (raw/javascriptallonge.pdf p.120-121).
- This lengthDelaysWork function calls itself in tail position (raw/javascriptallonge.pdf p.120-121).
- This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string (raw/javascriptallonge.pdf p.120-121).
- But while we're doing that, it's annoying to remember to call it with a zero (raw/javascriptallonge.pdf p.120-121).
