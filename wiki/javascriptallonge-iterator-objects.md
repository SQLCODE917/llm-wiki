---
page_id: javascriptallonge-iterator-objects
page_kind: source
summary: iterator objects from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.209-210
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on iterator objects from JavaScript Allongé, covering the implementation of iterators as objects rather than functions, and the mechanics of iterating using .next() method.

## Key supported claims

- Iteration for functions and objects has been around for many, many decades. (raw/javascriptallonge.pdf p.209-210)
- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. (raw/javascriptallonge.pdf p.209-210)
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. (raw/javascriptallonge.pdf p.209-210)
- Fortunately, an iterator object is almost as simple as an iterator function. (raw/javascriptallonge.pdf p.209-210)
- Instead of having a function that you call to get the next element, you have an object with a .next() method. (raw/javascriptallonge.pdf p.209-210)

## Technical details

### `technical-atom-c703f21c7091114e` procedure

Citation: (raw/javascriptallonge.pdf p.209-210)

The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system.

### `technical-atom-ccb654b6a11d4ba0` procedure

Citation: (raw/javascriptallonge.pdf p.209-210)

Instead of having a function that you call to get the next element, you have an object with a .next() method.
