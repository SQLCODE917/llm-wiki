---
page_id: javascriptallonge-section-commas-fa06a684
page_kind: source
summary: **commas**: 7 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-commas-fa06a684@0990c884321bac87467b60999a977d25
---

# **commas**

From [[javascriptallonge]].

## Statements

- The comma operator in JavaScript is interesting. _(javascriptallonge.pdf (source-range-83ecb080-00298))_
- In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00303))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00298))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00300))_

> (1 + 1, 2 + 2) _//=> 4_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00301))_

> We can use commas with functions to create functions that evaluate multiple expressions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00302))_

> (() => (1 + 1, 2 + 2))() _//=> 4_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00301))_

> We can use commas with functions to create functions that evaluate multiple expressions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00303))_

> This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later.

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00303))_

> This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00304))_

> () => (1 + 1, 2 + 2)

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00306))_

> () => ( 1 + 1, 2 + 2
