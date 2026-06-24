---
page_id: javascriptallonge-so-why-arrays
page_kind: source
summary: so why arrays from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.131-131
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé discusses why arrays are used instead of linked lists in JavaScript, covering performance and memory access characteristics.

## Key supported claims

- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). (raw/javascriptallonge.pdf p.131-131)
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. (raw/javascriptallonge.pdf p.131-131)
- And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it. (raw/javascriptallonge.pdf p.131-131)

## Technical details

### `technical-atom-8b9bc553c75c20d8` procedure

Citation: (raw/javascriptallonge.pdf p.131)

If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

## Related technical details

### From [[javascriptallonge-iterator-objects]]: `technical-atom-ccb654b6a11d4ba0` procedure

Relation: nearby source page; matched terms `element`, `have`, `instead`, `you`

Citation: (raw/javascriptallonge.pdf p.209-210)

Instead of having a function that you call to get the next element, you have an object with a .next() method.

### From [[javascriptallonge-summary]]: `technical-atom-c0465a677414b7ed` procedure

Relation: nearby source page; matched terms `cases`, `has`, `instead`

Citation: (raw/javascriptallonge.pdf p.99)

Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns.

### From [[javascriptallonge-iterator-objects]]: `technical-atom-c703f21c7091114e` procedure

Relation: nearby source page; matched terms `all`, `other`, `used`

Citation: (raw/javascriptallonge.pdf p.209-210)

The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system.

### From [[javascriptallonge-if-functions-without-free-variables-are-pure-are-closures-impure]]: `technical-atom-182b7d333da55239` requirement

Relation: nearby source page; matched terms `them`, `use`, `you`

Citation: (raw/javascriptallonge.pdf p.45)

They always mean the same thing wherever you use them.
