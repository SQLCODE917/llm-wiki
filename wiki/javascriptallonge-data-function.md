---
page_id: javascriptallonge-data-function
page_kind: concept
summary: Making Data Out Of Functions: 64 statement(s) and 52 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-data-function@c5a292a9e26e19ade0a9b48be4c64a97
---

# Making Data Out Of Functions

What [[javascriptallonge]] covers about making data out of functions:

## Statements

_Showing 14 of 64 statements selected for this topic._

- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-02033))_
- A _constant function_ is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- The _identity function_ is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-83ecb080-02056))_
- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-83ecb080-02076))_
- Our latin data structure is no longer a dumb data structure, it’s a function. _(javascriptallonge.pdf (source-range-83ecb080-02093))_
- It says, “take these two values and apply them to this function.” There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-83ecb080-02198))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-83ecb080-02085))_
- Functions are a fundamental building block of computation. _(javascriptallonge.pdf (source-range-83ecb080-02166))_
- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. _(javascriptallonge.pdf (source-range-83ecb080-02032))_
- We can model lists just using functions. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- The kestrel, or K, is a function that makes constant functions. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-83ecb080-02095))_

## Technical atoms

_Showing 6 of 52 technical atoms selected for this topic._

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02033))_

> For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02036))_

> **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02037))_

> OneTwoThree.first _//=> 1_ OneTwoThree.rest.first _//=> 2_

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02038))_

> OneTwoThree.rest.rest.first _//=> 3_ **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02039))_

> length(OneTwoThree) _//=> 3_

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02049))_

> **const** K = (x) => (y) => x; **const** I = (x) => (x); **const** V = (x) => (y) => (z) => z(x)(y);

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02053))_

> **const** K = (x) => (y) => x; **const** fortyTwo = K(42);


## Source

- [[javascriptallonge]]
