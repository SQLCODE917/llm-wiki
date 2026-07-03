---
page_id: javascriptallonge-recipe-iterables-out-to-infinity
page_kind: recipe
page_family: recipe-pattern
summary: iterables out to infinity: reusable source-backed pattern with 2 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: iterables-out-to-infinity
projection_coverage: recipe-javascriptallonge-recipe-iterables-out-to-infinity@d69cef10ce9098734d51c436eceba8f3
---

# iterables out to infinity

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-like-this-iterables-out-to-infinity-7f1f5ba0]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- There are useful things we can do with iterables representing an infinitely large collection. _(javascriptallonge.pdf (source-range-7239e085-01575))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-7239e085-01577))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01574)_

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

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01576)_

```
['all the numbers', ...Numbers]
//=> infinite loop!
firstAndSecondElement(...Numbers)
//=> infinite loop!
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-like-this-iterables-out-to-infinity-7f1f5ba0]]
