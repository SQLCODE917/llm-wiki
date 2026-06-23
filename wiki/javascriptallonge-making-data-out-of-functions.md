---
page_id: javascriptallonge-making-data-out-of-functions
page_kind: source
summary: Making Data Out Of Functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.177-179
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on modeling data using functions, including K, I, and V combinators.

## Key supported claims

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list (raw/javascriptallonge.pdf p.177-179).
- We can model lists just using functions (raw/javascriptallonge.pdf p.177-179).
- We have used arrays and objects to represent the structure of data, and extensively used the ternary operator to write algorithms that terminate when we reach a base case (raw/javascriptallonge.pdf p.177-179).

## Technical details

### `technical-atom-94b1271483ea8499` code

Citation: (raw/javascriptallonge.pdf p.177-179)

```javascript
const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest.first //=> 2 OneTwoThree.rest.rest.first //=> 3 const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) //=> 3
```

### `technical-atom-8dbeecd17e154409` code

Citation: (raw/javascriptallonge.pdf p.177-179)

```javascript
const K = (x) => (y) => x; const I = (x) => (x); const V = (x) => (y) => (z) => z(x)(y);
```

### `technical-atom-f36933c62676c874` formula

Citation: (raw/javascriptallonge.pdf p.177-179)

76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422

### `technical-atom-5b37e3daf21d3949` worked-example

Citation: (raw/javascriptallonge.pdf p.177-179)

For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

### `technical-atom-9c77a5de5c2d57ec` procedure

Citation: (raw/javascriptallonge.pdf p.177-179)

A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations.

### `technical-atom-ac4a59dfcff9d986` worked-example

Citation: (raw/javascriptallonge.pdf p.177-179)

For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list.

### `technical-atom-cf5b15724c23cd8a` procedure

Citation: (raw/javascriptallonge.pdf p.177-179)

To Mock a Mockingbird 76 established the metaphor of songbirds for the combinators, and ever since then logicians have called the K combinator a 'kestrel,' the B combinator a 'bluebird,' and so forth.
