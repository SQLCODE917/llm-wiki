---
page_id: javascriptallonge-section-basic-operations-on-iterables-9739baf4
page_kind: source
summary: Basic Operations on Iterables: 5 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-basic-operations-on-iterables-9739baf4@464db5c6ab195d5d5f6ab6eb7f6289d1
---

# Basic Operations on Iterables

From [[javascriptallonge]].

## Statements

- Here are the operations we’ve defined on Iterables. _(javascriptallonge.pdf (source-range-83ecb080-03051))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-03059))_

> **for** ( **let** i = 0; i < numberToTake; ++i) { **const** { done, value } = iterator.next(); **if** (!done) **yield** value; } }

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-03061))_

> **function** * zip (...iterables) { **const** iterators = iterables.map(i => i[Symbol.iterator]());

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-03063))_

> Note: zip is also the following special case of zipWith:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-03066))_

> **const** zip = callFirst(zipWith, (...values) => values);

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-03068))_

> **const** reduceWith = (fn, seed, iterable) => { **let** accumulator = seed;
