---
page_id: javascriptallonge-section-yielding-iterables-096757a1
page_kind: source
summary: **yielding iterables**: 10 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yielding-iterables-096757a1@0af777ff5b7be1ca714519a0332506db
---

# **yielding iterables**

From [[javascriptallonge]].

## Statements

- It works, but as we’ve just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object:[93] _(javascriptallonge.pdf (source-range-83ecb080-02689))_
- > 93There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-02690))_
- > 93There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-83ecb080-02690))_
- If e is not an iterable, yield e. _(javascriptallonge.pdf (source-range-83ecb080-02694))_
- We take advantage of the for...of loop in a plain and direct way: For each element e, if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. _(javascriptallonge.pdf (source-range-83ecb080-02694))_
- This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping. _(javascriptallonge.pdf (source-range-83ecb080-02695))_
- These three lines say, in essence, “yield all the elements of TreeIterable(e), in order.” This comes up quite often when we have collections that are compounds, collections made from other collections. _(javascriptallonge.pdf (source-range-83ecb080-02698))_
- Tucked inside of it is the same three-line idiom for yielding each element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-02704))_
- yield* is handy when writing generator functions that operate on or create iterables. _(javascriptallonge.pdf (source-range-83ecb080-02711))_

## Technical atoms

> But if you can write it as a simple generator, write it as a simple generator.
_(source: javascriptallonge.pdf (source-range-83ecb080-02690))_
