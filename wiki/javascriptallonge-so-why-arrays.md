---
page_id: javascriptallonge-so-why-arrays
page_kind: source
summary: Summary of the 'so why arrays' section from javascriptallonge.pdf
sources: raw/javascriptallonge.pdf p.131-131
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé discusses why arrays are used instead of linked lists in JavaScript, covering performance and memory access characteristics.

## Key supported claims

- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). (raw/javascriptallonge.pdf p.131-131)
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. (raw/javascriptallonge.pdf p.131-131)
- And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it. (raw/javascriptallonge.pdf p.131-131)
