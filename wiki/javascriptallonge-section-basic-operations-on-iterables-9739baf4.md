---
page_id: javascriptallonge-section-basic-operations-on-iterables-9739baf4
page_kind: source
summary: Basic Operations on Iterables: 5 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-basic-operations-on-iterables-9739baf4@643c3512e1dd01af7848fa7ce063be1a
---

# Basic Operations on Iterables

From [[javascriptallonge]].

## Statements

- Here are the operations we’ve defined on Iterables. _(javascriptallonge.pdf (source-range-83ecb080-03051))_

## Technical atoms

> **for** ( **let** i = 0; i < numberToTake; ++i) { **const** { done, value } = iterator.next(); **if** (!done) **yield** value; } }
_(source: javascriptallonge.pdf (source-range-83ecb080-03059))_

> **function** * zip (...iterables) { **const** iterators = iterables.map(i => i[Symbol.iterator]());
_(source: javascriptallonge.pdf (source-range-83ecb080-03061))_

> Context: Note: zip is also the following special case of zipWith:
_(context: javascriptallonge.pdf (source-range-83ecb080-03063))_

> **const** zip = callFirst(zipWith, (...values) => values);
_(source: javascriptallonge.pdf (source-range-83ecb080-03066))_

> **const** reduceWith = (fn, seed, iterable) => { **let** accumulator = seed;
_(source: javascriptallonge.pdf (source-range-83ecb080-03068))_
