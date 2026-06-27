---
page_id: javascriptallonge-section-interactive-generators-97a9d42e
page_kind: source
summary: **interactive generators**: 10 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-interactive-generators-97a9d42e@73d540ed5340db6e08b913a88a2a5e42
---

# **interactive generators**

From [[javascriptallonge]].

## Statements

- If we could do that, a generator function that played naughts and crosses would look like this: _(javascriptallonge.pdf (source-range-83ecb080-03026))_
- So far, we have called iterators (and generators) with .next(). _(javascriptallonge.pdf (source-range-83ecb080-03026))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- We can then get the first move by calling .next(). _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- We can then get the first move by calling .next(). _(javascriptallonge.pdf (source-range-83ecb080-03033))_
- It isn’t a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block. _(javascriptallonge.pdf (source-range-83ecb080-03042))_
- But the generator function allows us to maintain state implicitly. _(javascriptallonge.pdf (source-range-83ecb080-03043))_
- And sometimes, we want to use implicit state instead of explicitly storing state in our data. _(javascriptallonge.pdf (source-range-83ecb080-03043))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-03033))_

> We can then get the first move by calling .next(). Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. If we wanted to pass some state to the generator before it begins, we’d do that with parameters.):

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-03032))_

> **const** aNaughtsAndCrossesGame = generatorNaughtsAndCrosses();
