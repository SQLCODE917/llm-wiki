---
page_id: javascriptallonge-section-ordered-collections-243e57d8
page_kind: source
summary: **ordered collections**: 11 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-ordered-collections-243e57d8@715ae490a19258e1c47894b8d4aee530
---

# **ordered collections**

From [[javascriptallonge]].

## Statements

- The iterables we’re discussing represent _ordered collections_ . _(javascriptallonge.pdf (source-range-83ecb080-02457))_
- One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. _(javascriptallonge.pdf (source-range-83ecb080-02457))_
- Iterables needn’t represent ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-02461))_
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator], and ensuring that our iterators start at the beginning and work forward. _(javascriptallonge.pdf (source-range-83ecb080-02461))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. _(javascriptallonge.pdf (source-range-83ecb080-02467))_
- Every time we get an iterator from an ordered collection, we start iterating from the beginning. _(javascriptallonge.pdf (source-range-83ecb080-02467))_
- Right now, we’re just looking at ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-02467))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02457))_

> The iterables we’re discussing represent _ordered collections_ . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02458))_

> **const** abc = ["a", "b", "c"];
