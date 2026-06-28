---
page_id: javascriptallonge-section-iterables-out-to-infinity-e6b19bbb
page_kind: source
summary: iterables out to infinity: 4 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-iterables-out-to-infinity-e6b19bbb@e30b2314cb30c2e5087efbe1b2341f1c
---

# iterables out to infinity

From [[javascriptallonge]].

## Statements

- There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them: _(javascriptallonge.pdf (source-range-31a4cf47-01575))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-31a4cf47-01577))_

## Technical atoms

### Technical frame 1: iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01575))_

> There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01574))_

```
const Numbers = { [Symbol.iterator] () { let n = 0; return { next: () => ({done: false , value: n++}) } } }
```

### Technical frame 2: iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01577))_

> Attempting to spread an infinite iterable into an array is always going to fail.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01576))_

```
['all the numbers', ...Numbers] //=> infinite loop! firstAndSecondElement(...Numbers) //=> infinite loop!
```
