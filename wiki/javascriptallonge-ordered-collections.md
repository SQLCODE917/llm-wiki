---
page_id: javascriptallonge-ordered-collections
page_kind: source
summary: Summary of ordered collections in JavaScript Allongé
sources: raw/javascriptallonge.pdf p.216-217
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This section of JavaScript Allongé discusses ordered collections, focusing on the semantic properties of iterables and how they relate to ordered collections.

## Key supported claims

- The iterables we're discussing represent ordered collections (raw/javascriptallonge.pdf p.216-217). One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning (raw/javascriptallonge.pdf p.216-217).
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator], and ensuring that our iterators start at the beginning and work forward (raw/javascriptallonge.pdf p.216-217).
- Iterables needn't represent ordered collections (raw/javascriptallonge.pdf p.216-217). We could make an infinite iterable representing random numbers (raw/javascriptallonge.pdf p.216-217).
- Therefore, RandomNumbers is not an ordered collection (raw/javascriptallonge.pdf p.216-217).
