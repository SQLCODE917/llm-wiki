---
page_id: javascriptallonge-yielding-iterables
page_kind: source
summary: Chapter on yielding iterables from JavaScript Allongé.
sources: raw/javascriptallonge.pdf p.239-243
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Chapter on yielding iterables from JavaScript Allongé, covering tree iteration and the use of yield*.

## Key supported claims

- We take advantage of the for...of loop in a plain and direct way: For each element e, if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. This approach works well and is simpler than maintaining our own stack (raw/javascriptallonge.pdf p.239-243).
- Tucked inside of it is the same three-line idiom for yielding each element of an iterable, which can be abbreviated using yield* (raw/javascriptallonge.pdf p.239-243).
- A function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object (raw/javascriptallonge.pdf p.239-243).
- append iterates over a collection of iterables, one element at a time (raw/javascriptallonge.pdf p.239-243).
- yield* is handy when writing generator functions that operate on or create iterables (raw/javascriptallonge.pdf p.239-243).
