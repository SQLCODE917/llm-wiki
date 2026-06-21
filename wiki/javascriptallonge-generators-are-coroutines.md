---
page_id: javascriptallonge-generators-are-coroutines
page_kind: source
summary: Generators as coroutines in JavaScript, with behavioral differences from ordinary functions.
sources: raw/javascriptallonge.pdf p.231-234
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Generators in JavaScript behave as coroutines, with a distinct execution model compared to ordinary functions. They suspend and resume execution at yield points, enabling a producer-consumer model.

## Key supported claims

- This is where generators behave very, very differently from ordinary functions (raw/javascriptallonge.pdf p.231-234).
- The body of our generator runs until it returns, ends, or encounters a yield statement, which is yield 1; (raw/javascriptallonge.pdf p.231-234).
- When we call interator.next() , the body of our generator begins to be evaluated (raw/javascriptallonge.pdf p.231-234).
