---
page_id: javascriptallonge-section-like-this-iterables-out-to-infinity-7f1f5ba0
page_kind: source
summary: Like this: / iterables out to infinity: 4 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-like-this-iterables-out-to-infinity-7f1f5ba0@aeb79613e5fa14a8705936bccd5522cd
---

# Like this: / iterables out to infinity

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-like-this-66cb3108]] - broader source section: Like this:

## Statements

- There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them: _(javascriptallonge.pdf (source-range-7239e085-01575))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-7239e085-01577))_

## Technical atoms

### Technical frame 1: Like this: / iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01575))_

> There are useful things we can do with iterables representing an infinitely large collection. But let's point out what we can't do with them:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01574))_

```
const Numbers = {
[Symbol.iterator] () {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}
```

### Technical frame 2: Like this: / iterables out to infinity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01577))_

> Attempting to spread an infinite iterable into an array is always going to fail.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01576))_

```
['all the numbers', ...Numbers]
//=> infinite loop!
firstAndSecondElement(...Numbers)
//=> infinite loop!
```
