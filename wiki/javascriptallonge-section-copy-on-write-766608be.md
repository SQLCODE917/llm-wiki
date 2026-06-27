---
page_id: javascriptallonge-section-copy-on-write-766608be
page_kind: source
summary: **Copy on Write**: 12 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-766608be@a3e1522093317e24f01e61eede043e87
---

# **Copy on Write**

From [[javascriptallonge]].

## Statements

- We’ve seen how to build lists with arrays and with linked lists. _(javascriptallonge.pdf (source-range-83ecb080-01852))_
- - When you take the rest of an array with destructuring ([first, ...rest]), you are given a _copy_ of the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01853))_
- - When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-83ecb080-01854))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-01855))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-01855))_
- And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent. _(javascriptallonge.pdf (source-range-83ecb080-01858))_
- We’ll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-83ecb080-01863))_
- If we _know_ that a list doesn’t share any elements with another list, we can safely modify it. _(javascriptallonge.pdf (source-range-83ecb080-01863))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01854))_

> When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01855))_

> The consequence of this is that if you have an array, and you take it’s “rest,” your “child” array is a copy of the elements of the parent array.

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01858))_

> Whereas if you have a linked list, and you take it’s “rest,” your “child” list shares its nodes with the “parent” list.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01859))_

> Let’s confirm our understanding:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01861))_

> parentList.rest.rest.first = "three"; childList.first = "two";

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01859))_

> Let’s confirm our understanding:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01862))_

> parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_
