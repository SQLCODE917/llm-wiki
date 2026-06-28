---
page_id: javascriptallonge-section-values-are-expressions-mutation-mutation-and-data-structures-0b5bf437
page_kind: source
summary: values are expressions / Mutation / mutation and data structures: 7 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-mutation-mutation-and-data-structures-0b5bf437@ce7ee8fff35ce4b9695cc1fce74429e2
---

# values are expressions / Mutation / mutation and data structures

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-mutation-6b1093f2]] - broader source section

## Statements

- It is possible to compute anything without ever mutating an existing entity. _(javascriptallonge.pdf (source-range-83ecb080-01138))_
- In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-83ecb080-01138))_
- Mutation is a surprisingly complex subject. _(javascriptallonge.pdf (source-range-83ecb080-01138))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. _(javascriptallonge.pdf (source-range-83ecb080-01139))_
- Let’s recall linked lists from Plain Old JavaScript Objects. _(javascriptallonge.pdf (source-range-83ecb080-01139))_
- While we’re executing the mapWith function, we’re constructing a new linked list. _(javascriptallonge.pdf (source-range-83ecb080-01139))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01139))_

> One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let’s recall linked lists from Plain Old JavaScript Objects. While we’re executing the mapWith function, we’re constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01140))_

> But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:
