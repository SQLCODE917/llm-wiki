---
page_id: javascriptallonge-section-iterables-out-to-infinity-d7fa34ef
page_kind: source
summary: iterables out to infinity: 4 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-iterables-out-to-infinity-d7fa34ef@9e818fca73e7a415337c1461a34499a9
---

# iterables out to infinity

From [[javascriptallonge]].

## Statements

- There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them: _(javascriptallonge.pdf (source-range-8eb13d6b-01574))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-8eb13d6b-01576))_

## Technical atoms

### Technical frame 1: iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01574))_

> There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01573))_

```
const Numbers = { [Symbol.iterator] () { let n = 0; return { next: () => ({done: false , value: n++}) } } }
```

### Technical frame 2: iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01576))_

> Attempting to spread an infinite iterable into an array is always going to fail.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01575))_

```
['all the numbers', ...Numbers] //=> infinite loop! firstAndSecondElement(...Numbers) //=> infinite loop!
```
