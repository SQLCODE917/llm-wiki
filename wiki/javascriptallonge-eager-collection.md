---
page_id: javascriptallonge-eager-collection
page_kind: concept
summary: Eager Collection: 7 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-eager-collection@0ee98d4fe39f239c4c9e5ab214884088
---

# Eager Collection

What [[javascriptallonge]] covers about eager collection:

## Statements

- This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. _(javascriptallonge.pdf (source-range-83ecb080-01776))_
- We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-83ecb080-01774))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-83ecb080-01808))_
- If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-83ecb080-01773))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-83ecb080-01774))_
- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-01778))_
- This is why “pure” functional languages like Haskell combine lazy semantics with immutable collections, and why even “impure” languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-83ecb080-01808))_

## Related pages

- [[javascriptallonge-collection]] - broader topic (3 shared statement(s))
- [[javascriptallonge-object]] - shared statements (2 shared statement(s))
- [[javascriptallonge-method]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
