---
page_id: javascriptallonge-section-lazy-and-eager-collections-226210f6
page_kind: source
summary: **Lazy and Eager Collections**: 13 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-lazy-and-eager-collections-226210f6@d30f24cef17beec959881379e689daee
---

# **Lazy and Eager Collections**

From [[javascriptallonge]].

## Statements

- The operations on iterables are tremendously valuable, but let’s reiterate why we care: In JavaScript, we build single-responsibility objects, and single-responsibility functions, and we compose these together to build more full-featured objects and algorithms. _(javascriptallonge.pdf (source-range-83ecb080-02737))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack _(javascriptallonge.pdf (source-range-83ecb080-02738))_
- If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- in the older style of object-oriented programming, we built “fat” objects. _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- Each collection knew how to map itself (.map), how to fold itself (.reduce), how to filter itself (.filter) and how to find one element within itself (.find). _(javascriptallonge.pdf (source-range-83ecb080-02739))_
- We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- Each one has its own variation, but the overall form is identical. _(javascriptallonge.pdf (source-range-83ecb080-02741))_
- That’s a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction. _(javascriptallonge.pdf (source-range-83ecb080-02741))_
- But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. _(javascriptallonge.pdf (source-range-83ecb080-02741))_
- That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-83ecb080-02742))_
- This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. _(javascriptallonge.pdf (source-range-83ecb080-02742))_
