---
page_id: javascriptallonge-section-operations-that-transform-an-iterable-into-a-value-572613ca
page_kind: source
summary: operations that transform an iterable into a value: 1 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-operations-that-transform-an-iterable-into-a-value-572613ca@85e65aebe708fc1c079de8e47c21edb4
---

# operations that transform an iterable into a value

From [[javascriptallonge]].

## Technical atoms

### Technical frame 1: operations that transform an iterable into a value

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01958))_

```
const reduceWith = (fn, seed, iterable) => { let accumulator = seed; for ( const element of iterable) { accumulator = fn(accumulator, element); } return accumulator; }; const first = (iterable) => iterable[Symbol.iterator]().next().value;
```
