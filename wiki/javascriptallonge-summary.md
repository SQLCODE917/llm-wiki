---
page_id: javascriptallonge-summary
page_kind: source
summary: summary from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.283-283
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

A comprehensive modular guide to JavaScript fundamentals and advanced techniques, spanning 20 chapters.

## Key supported claims

- We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. But as we see here, it's also possible to use a generator interactively, passing values in and receiving a value in return, just like an ordinary function. (raw/javascriptallonge.pdf p.283-283)
- Again, the salient difference is that an 'interactive' generator is stateful, and it embodies its state in its control flow. (raw/javascriptallonge.pdf p.283-283)

## Technical details

### `technical-atom-a21f6839ff55796a` requirement

Citation: (raw/javascriptallonge.pdf p.99)

is a logical operator, it always returns true or false .

### `technical-atom-1bb3350d91858991` requirement

Citation: (raw/javascriptallonge.pdf p.99)

- The ternary operator ( ?: ), || , and && are control flow operators, they do not always return true or false , and they have short-cut semantics.

### `technical-atom-37102d1f47fd8468` procedure

Citation: (raw/javascriptallonge.pdf p.99)

And finally, while folding is a special case of linear recursion, mapping is a special case of folding.

### `technical-atom-66c4cc503e9088bc` procedure

Citation: (raw/javascriptallonge.pdf p.99)

Although we showed how to use tail calls to map and fold over arrays with [first, ...rest] , in reality this is not how it ought to be done.

### `technical-atom-c0465a677414b7ed` procedure

Citation: (raw/javascriptallonge.pdf p.99)

Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns.
