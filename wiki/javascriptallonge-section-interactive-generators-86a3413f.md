---
page_id: javascriptallonge-section-interactive-generators-86a3413f
page_kind: source
summary: interactive generators: 8 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-86a3413f@bedbf36c2326c430c28c8129f6008cce
---

# interactive generators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-interactive-generators-42a29113]] - same source heading: another source section with the same heading, Interactive Generators

## Statements

- So far, we have called iterators (and generators) with .next() . But what if we pass a value to .next() ? If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-8eb13d6b-01937))_
- Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-8eb13d6b-01940))_
- Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn't call us. It isn't a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-8eb13d6b-01941))_
- But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-8eb13d6b-01942))_
- If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1).value //=> 6 aNaughtsAndCrossesGame.next(3).value //=> 8 aNaughtsAndCrossesGame.next(7).value //=> 4 _(javascriptallonge.pdf (source-range-8eb13d6b-01940))_

## Technical atoms

### Technical frame 1: interactive generators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01940))_

> Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1)

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01939))_

```
function * generatorNaughtsAndCrosses () { const x1 = yield 0; switch (x1) { case 1: const x2 = yield 6; switch (x2) { case 2: case 4: case 5: case 7: case 8: yield 3; break ; case 3: const x3 = yield 8; switch (x3) { case 2: case 5: case 7: yield 4; break ; case 4: yield 7; break ;
```
