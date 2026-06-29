---
page_id: javascriptallonge-section-the-simplest-possible-block-c9be17c8
page_kind: source
summary: the simplest possible block: 5 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-simplest-possible-block-c9be17c8@b16f6121e24568e6ac1f7f756122d2d0
---

# the simplest possible block

From [[javascriptallonge]].

## Statements

- There's another thing we can put to the right of an arrow, a block . A block has zero or more statements , separated by semicolons. 18 _(javascriptallonge.pdf (source-range-8eb13d6b-00214))_
- It returns the result of evaluating a block that has no statements. What would that be? Let's try it: _(javascriptallonge.pdf (source-range-8eb13d6b-00217))_

## Technical atoms

### Technical frame 1: the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00217))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00216))_

```
() => {}
```

### Technical frame 2: the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00217))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00218))_

```
(() => {})() //=> undefined
```
