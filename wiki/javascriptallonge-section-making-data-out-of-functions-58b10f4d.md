---
page_id: javascriptallonge-section-making-data-out-of-functions-58b10f4d
page_kind: source
summary: Making Data Out Of Functions: 12 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-making-data-out-of-functions-58b10f4d@b0c94acc95d5be1fdfa7336db875ec30
---

# Making Data Out Of Functions

From [[javascriptallonge]].

## Statements

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-31a4cf47-01328))_
- A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things. _(javascriptallonge.pdf (source-range-31a4cf47-01330))_
- They established that arbitrary computations could be represented a small set of axiomatic components. For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. We can model lists just using functions. _(javascriptallonge.pdf (source-range-31a4cf47-01331))_
- The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation. _(javascriptallonge.pdf (source-range-31a4cf47-01333))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-31a4cf47-01328))_
- For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-31a4cf47-01331))_

## Technical atoms

### Technical frame 1: Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01328))_

> In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01326))_

> [Figure] (p.177)

### Technical frame 2: Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01330))_

> A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01329))_

```
const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } }; OneTwoThree.first //=> 1 OneTwoThree.rest.first //=> 2 OneTwoThree.rest.rest.first //=> 3 const length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) //=> 3
```

### Technical frame 3: Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01333))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01336))_

```
const K = (x) => (y) => x; const I = (x) => (x); const V = (x) => (y) => (z) => z(x)(y);
```

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01333))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01335))_

| entry | content |
| --- | --- |
| 76 | http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 |
| 77 | http://oscin.es |

<details>
<summary>Raw table text</summary>

```
76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422
77 http://oscin.es
```

</details>
