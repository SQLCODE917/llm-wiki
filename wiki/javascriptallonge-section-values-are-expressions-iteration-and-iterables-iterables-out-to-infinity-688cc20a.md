---
page_id: javascriptallonge-section-values-are-expressions-iteration-and-iterables-iterables-out-to-infinity-688cc20a
page_kind: source
summary: values are expressions / Iteration and Iterables / iterables out to infinity: 2 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-iteration-and-iterables-iterables-out-to-infinity-688cc20a@5a486fcb8113aa03b30502b0217ad699
---

# values are expressions / Iteration and Iterables / iterables out to infinity

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-iteration-and-iterables-70b2511b]] - broader source section

## Statements

- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-83ecb080-01580))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01576))_

> Iterables needn’t represent finite collections: **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } } There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01579))_

> firstAndSecondElement(...Numbers) _//=> infinite loop!_
