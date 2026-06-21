---
page_id: javascriptallonge-interactive-generators
page_kind: source
summary: Summary of interactive generators in JavaScript Allongé.
sources: raw/javascriptallonge.pdf p.282-283
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Interactive Generators chapter covering generators, stateful functions, and examples.

## Key supported claims

- So far, we have called iterators (and generators) with .next(). (raw/javascriptallonge.pdf p.282-283)
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet.) (raw/javascriptallonge.pdf p.282-283)
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters. (raw/javascriptallonge.pdf p.282-283)
- If we could do that, a generator function that played naughts and crosses would look like this: (raw/javascriptallonge.pdf p.282-283)
- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. (raw/javascriptallonge.pdf p.282-283)
