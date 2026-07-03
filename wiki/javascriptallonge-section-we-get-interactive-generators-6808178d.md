---
page_id: javascriptallonge-section-we-get-interactive-generators-6808178d
page_kind: source
page_family: section-reference
summary: We get: / interactive generators: 8 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-get-interactive-generators-6808178d@3409a212e96ca1f0e09aee7f29320d45
---

# We get: / interactive generators

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-get-2605e005]] - broader source section: We get:

### Other

- [[javascriptallonge-section-we-ll-keep-it-simple-interactive-generators-1f19e24c]] - same source heading: another source section with the same heading, We'll keep it simple: / Interactive Generators

## Statements

- So far, we have called iterators (and generators) with .next() . But what if we pass a value to .next() ? If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-7239e085-01938))_
- Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-7239e085-01941))_
- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-7239e085-01942))_
- But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-7239e085-01943))_
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-7239e085-01941))_
