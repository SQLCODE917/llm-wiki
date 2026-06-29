---
page_id: javascriptallonge-section-operations-that-transform-one-iterable-into-another-eaef9d21
page_kind: source
summary: operations that transform one iterable into another: 2 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-operations-that-transform-one-iterable-into-another-eaef9d21@06a37290e01a03a903f4218543d7060e
---

# operations that transform one iterable into another

From [[javascriptallonge]].

## Technical atoms

### Technical frame 1: operations that transform one iterable into another

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01949))_

```
function * mapWith(fn, iterable) { for ( const element of iterable) { yield fn(element); } } function * mapAllWith (fn, iterable) { for ( const element of iterable) { yield * fn(element); } } function * filterWith (fn, iterable) { for ( const element of iterable) { if (!!fn(element)) yield element; } } function * compact (iterable) { for ( const element of iterable) { if (element != null ) yield element; } } function * untilWith (fn, iterable) { for ( const element of iterable) { if (fn(element)) break ; yield fn(element); } } function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next();
```

### Technical frame 2: operations that transform one iterable into another

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01950))_

```
yield * iterator; } function * take (numberToTake, iterable) { const iterator = iterable[Symbol.iterator](); for ( let i = 0; i < numberToTake; ++i) { const { done, value } = iterator.next(); if (!done) yield value; } }
```
