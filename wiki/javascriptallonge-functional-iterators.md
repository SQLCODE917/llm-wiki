---
page_id: javascriptallonge-functional-iterators
page_kind: source
summary: Chapter on functional iterators in JavaScript Allongé
sources: raw/javascriptallonge.pdf p.206-209
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter explores the concept of functional iterators and how to separate the mechanism of traversing data structures from the operations performed on them.

## Key supported claims

- The way we've written .iterator as a method, each object knows how to return an iterator for itself. (raw/javascriptallonge.pdf p.206-209)
- We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method: (raw/javascriptallonge.pdf p.206-209)
- Note that it uses the function keyword, so when we invoke it with stack.iterator() , JavaScript sets this to the value of stack . (raw/javascriptallonge.pdf p.206-209)
