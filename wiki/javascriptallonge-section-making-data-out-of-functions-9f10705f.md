---
page_id: javascriptallonge-section-making-data-out-of-functions-9f10705f
page_kind: source
summary: **Making Data Out Of Functions**: 15 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-making-data-out-of-functions-9f10705f@10d9a44ccce02ff662fbe8def9585ddf
---

# **Making Data Out Of Functions**

From [[javascriptallonge]].

## Statements

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. _(javascriptallonge.pdf (source-range-83ecb080-02032))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-02033))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-02033))_
- They searched for a radically simpler set of tools that could accomplish all of the same things. _(javascriptallonge.pdf (source-range-83ecb080-02040))_
- We can model lists just using functions. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- They established that arbitrary computations could be represented a small set of axiomatic components. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- For example, we don’t need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- For example, we don’t need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- The oscin.es[77] library contains code for all of the standard combinators and for experimenting using the standard notation. _(javascriptallonge.pdf (source-range-83ecb080-02043))_
- Let’s start with some of the building blocks of combinatory logic, the K, I, and V combinators, nicknamed the “Kestrel”, the “Idiot Bird”, and the “Vireo:” _(javascriptallonge.pdf (source-range-83ecb080-02044))_

## Technical atoms

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
