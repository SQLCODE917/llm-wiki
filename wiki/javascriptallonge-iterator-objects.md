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

## Related technical details

### From [[javascriptallonge-summary]]: `technical-atom-c0465a677414b7ed` procedure

Relation: nearby source page; matched terms `can`, `has`, `instead`, `iterator`, `method`, `next`

Citation: (raw/javascriptallonge.pdf p.99)

Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns.

### From [[javascriptallonge-so-why-arrays]]: `technical-atom-8b9bc553c75c20d8` procedure

Relation: nearby source page; matched terms `instead`, `javascript`, `procedure`

Citation: (raw/javascriptallonge.pdf p.131)

If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

### From [[javascriptallonge-if-functions-without-free-variables-are-pure-are-closures-impure]]: `technical-atom-62b29dbab26e9d26` exception

Relation: nearby source page; matched terms `can`, `function`, `functions`, `used`

Citation: (raw/javascriptallonge.pdf p.45)

Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without:

### From [[javascriptallonge-representing-naughts-and-crosses-as-a-stateless-function]]: `technical-atom-203cbced3f1f6964` procedure

Relation: nearby source page; matched terms `function`, `procedure`, `then`

Citation: (raw/javascriptallonge.pdf p.275)

We encode each position of the board in some fashion, and then we build a dictionary from positions to moves.
