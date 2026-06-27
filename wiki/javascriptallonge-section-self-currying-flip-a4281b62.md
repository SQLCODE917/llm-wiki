---
page_id: javascriptallonge-section-self-currying-flip-a4281b62
page_kind: source
summary: **self-currying flip**: 2 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-self-currying-flip-a4281b62@a1b998ed907168b84a42f358715eeb91
---

# **self-currying flip**

From [[javascriptallonge]].

## Statements

- Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). _(javascriptallonge.pdf (source-range-83ecb080-02266))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02266))_

> Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We _could_ make that into flip:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02268))_

> Now if we write mapWith = flip(map), we can call mapWith(fn, list) or mapWith(fn)(list), our choice.
