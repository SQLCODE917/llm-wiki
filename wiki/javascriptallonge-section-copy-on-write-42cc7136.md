---
page_id: javascriptallonge-section-copy-on-write-42cc7136
page_kind: source
summary: Copy on Write: 11 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-copy-on-write-42cc7136@4a07816558212524f38df72a1f4795d7
---

# Copy on Write

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-copy-write]] - topic hub: opens the topic page for Copy Write
- [[javascriptallonge-section-copy-on-write-e50e229e]] - same source heading: another source section with the same heading, copy-on-write

## Statements

- We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them: _(javascriptallonge.pdf (source-range-8eb13d6b-01224))_
- When you take the rest of an array with destructuring ( [first, ...rest] ), you are given a copy of the elements of the array. _(javascriptallonge.pdf (source-range-8eb13d6b-01225))_
- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. _(javascriptallonge.pdf (source-range-8eb13d6b-01226))_
- The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-8eb13d6b-01227))_
- This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-8eb13d6b-01231))_
- And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-8eb13d6b-01227))_

## Technical atoms

### Technical frame 1: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01224))_

> We've seen how to build lists with arrays and with linked lists. We've touched on an important difference between them:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01222))_

> [Figure] (p.158)

### Technical frame 2: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01231))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01227))_

> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

### Technical frame 3: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01231))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01228))_

> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

### Technical frame 4: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01231))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01230))_

```
const parentArray = [1, 2, 3]; const [aFirst, ...childArray] = parentArray; parentArray[2] = "three"; childArray[0] = "two"; parentArray //=> [1,2,"three"] childArray //=> ["two",3] const EMPTY = { first: {}, rest: {} }; const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; const childList = parentList.rest; parentList.rest.rest.first = "three"; childList.first = "two"; parentList //=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\ {},"rest":{}}}}} childList //=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}
```
