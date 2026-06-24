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

## Related technical details

### From [[javascriptallonge-michael-fogus]]: `technical-atom-2733f8b79026ed62` worked-example

Relation: nearby source page; matched terms `allong`, `javascript`

Citation: (raw/javascriptallonge.pdf p.14)

In the case of JavaScript Allongé, you'll find the Leanpub model a shining example of effectiveness.

### From [[javascriptallonge-if-functions-without-free-variables-are-pure-are-closures-impure]]: `technical-atom-62b29dbab26e9d26` exception

Relation: nearby source page; matched terms `can`, `either`, `function`, `functions`

Citation: (raw/javascriptallonge.pdf p.45)

Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without:

### From [[javascriptallonge-summary]]: `technical-atom-c0465a677414b7ed` procedure

Relation: nearby source page; matched terms `can`, `like`, `summary`, `write`

Citation: (raw/javascriptallonge.pdf p.99)

Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns.

### From [[javascriptallonge-summary]]: `technical-atom-1bb3350d91858991` requirement

Relation: nearby source page; matched terms `operators`, `return`, `summary`, `true`

Citation: (raw/javascriptallonge.pdf p.99)

- The ternary operator ( ?: ), || , and && are control flow operators, they do not always return true or false , and they have short-cut semantics.
