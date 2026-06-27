---
page_id: javascriptallonge-section-mutation-and-data-structures-ae403ce7
page_kind: source
summary: **mutation and data structures**: 9 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mutation-and-data-structures-ae403ce7@0cdd90286abb92fd85730f7bb4334e5e
---

# **mutation and data structures**

From [[javascriptallonge]].

## Statements

- Mutation is a surprisingly complex subject. _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about. _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- It is possible to compute anything without ever mutating an existing entity. _(javascriptallonge.pdf (source-range-83ecb080-01715))_
- While we’re executing the mapWith function, we’re constructing a new linked list. _(javascriptallonge.pdf (source-range-83ecb080-01716))_
- Let’s recall linked lists from Plain Old JavaScript Objects. _(javascriptallonge.pdf (source-range-83ecb080-01716))_
- One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. _(javascriptallonge.pdf (source-range-83ecb080-01716))_

## Technical atoms

> Context: One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let’s recall linked lists from Plain Old JavaScript Objects. While we’re executing the mapWith function, we’re constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith.
_(context: javascriptallonge.pdf (source-range-83ecb080-01716))_

> But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:
_(source: javascriptallonge.pdf (source-range-83ecb080-01717))_

> const ThreeToFive = OneToFive.rest.rest;
_(source: javascriptallonge.pdf (source-range-83ecb080-01724))_

> ThreeToFive.first = "three"; ThreeToFive.rest.first = "four"; ThreeToFive.rest.rest.first = "five";
_(source: javascriptallonge.pdf (source-range-83ecb080-01727))_
