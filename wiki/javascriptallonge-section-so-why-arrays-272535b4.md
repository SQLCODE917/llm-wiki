---
page_id: javascriptallonge-section-so-why-arrays-272535b4
page_kind: source
summary: **so why arrays**: 7 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-so-why-arrays-272535b4@3ecd7ea22dea6075cb491f185d9db8c1
---

# **so why arrays**

From [[javascriptallonge]].

## Statements

- But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. _(javascriptallonge.pdf (source-range-83ecb080-01565))_
- Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. _(javascriptallonge.pdf (source-range-83ecb080-01565))_
- If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list. _(javascriptallonge.pdf (source-range-83ecb080-01566))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-83ecb080-01567))_
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. _(javascriptallonge.pdf (source-range-83ecb080-01568))_

## Technical atoms

> Context: If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?
_(context: javascriptallonge.pdf (source-range-83ecb080-01564))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.
_(source: javascriptallonge.pdf (source-range-83ecb080-01565))_

> Context: Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.
_(context: javascriptallonge.pdf (source-range-83ecb080-01565))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.
_(source: javascriptallonge.pdf (source-range-83ecb080-01566))_
