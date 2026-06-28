---
page_id: javascriptallonge-section-the-simplest-possible-block-e6c07091
page_kind: source
summary: the simplest possible block: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-simplest-possible-block-e6c07091@8047e24ea0e481252a2bb1ec64ed0b77
---

# the simplest possible block

From [[javascriptallonge]].

## Statements

- There's another thing we can put to the right of an arrow, a block . A block has zero or more statements , separated by semicolons. 18 _(javascriptallonge.pdf (source-range-31a4cf47-00214))_
- It returns the result of evaluating a block that has no statements. What would that be? Let's try it: _(javascriptallonge.pdf (source-range-31a4cf47-00217))_

## Technical atoms

### Technical frame 1: the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00217))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00216))_

```
() => {}
```

### Technical frame 2: the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00217))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00218))_

```
(() => {})() //=> undefined
```
