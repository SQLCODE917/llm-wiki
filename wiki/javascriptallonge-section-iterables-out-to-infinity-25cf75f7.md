---
page_id: javascriptallonge-section-iterables-out-to-infinity-25cf75f7
page_kind: source
summary: **iterables out to infinity**: 4 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-iterables-out-to-infinity-25cf75f7@6862cff4fd13cb188432253cdcbfea63
---

# **iterables out to infinity**

From [[javascriptallonge]].

## Statements

- There are useful things we can do with iterables representing an infinitely large collection. _(javascriptallonge.pdf (source-range-83ecb080-02449))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-83ecb080-02455))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02447))_

> Iterables needn’t represent finite collections:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02448))_

> **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02449))_

> There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02452))_

> ['all the numbers', ...Numbers] _//=> infinite loop!_
