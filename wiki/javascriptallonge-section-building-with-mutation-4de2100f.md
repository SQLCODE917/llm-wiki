---
page_id: javascriptallonge-section-building-with-mutation-4de2100f
page_kind: source
summary: **building with mutation**: 8 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-building-with-mutation-4de2100f@62c8406b13694582722957c1cbad832c
---

# **building with mutation**

From [[javascriptallonge]].

## Statements

- Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-83ecb080-01740))_
- As noted, one pattern is to be more liberal about mutation when building a data structure. _(javascriptallonge.pdf (source-range-83ecb080-01740))_
- If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation: _(javascriptallonge.pdf (source-range-83ecb080-01743))_
- This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. _(javascriptallonge.pdf (source-range-83ecb080-01747))_
- But when we’re in the midst of creating a brand new list, we aren’t sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time. _(javascriptallonge.pdf (source-range-83ecb080-01747))_
- Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. _(javascriptallonge.pdf (source-range-83ecb080-01747))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01740))_

> As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01741))_

> **const** reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed });

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01740))_

> As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01742))_

> **const** copy = (node) => reverse(reverse(node));
