---
page_id: javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-so-why-arrays-ecae5c27
page_kind: source
summary: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays: 7 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-so-why-arrays-ecae5c27@3e1f2841786d8b3189637e9ec8ee1525
---

# Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-83116d81]] - broader source section: Composing and Decomposing Data / Garbage, Garbage Everywhere
- [[javascriptallonge-array]] - topic hub: opens the topic page for Array

## Statements

- Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it. _(javascriptallonge.pdf (source-range-7239e085-01055))_
- We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list. _(javascriptallonge.pdf (source-range-7239e085-01056))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-7239e085-01057))_
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. _(javascriptallonge.pdf (source-range-7239e085-01058))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01056))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01055))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

### Technical frame 2: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01057))_

> Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation).

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01056))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.
