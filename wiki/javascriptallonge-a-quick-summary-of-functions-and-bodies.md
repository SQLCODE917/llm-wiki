---
page_id: javascriptallonge-a-quick-summary-of-functions-and-bodies
page_kind: source
summary: a quick summary of functions and bodies from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.40-40
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

A quick summary of functions and bodies in JavaScript Allongé.

## Key supported claims

- Expressions consist either of representations of values (like 3.14159265 , true , and undefined ), operators that combine expressions (like 3 + 2 ), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( arguments ) { body-statements } for creating functions. (raw/javascriptallonge.pdf p.40-40)
- A return statement accepts any valid JavaScript expression. (raw/javascriptallonge.pdf p.40-40)
- Since a function can contain a return statement with an expression, we can write a function that returns a function, or an array that contains another array expression. Or a function that returns an array, an array of functions, a function that returns an array of functions, and so forth. (raw/javascriptallonge.pdf p.40-40)

## Technical details

### `technical-atom-5e2b194ce75f5bf0` exception

Citation: (raw/javascriptallonge.pdf p.40)

How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure).
