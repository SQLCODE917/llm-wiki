---
page_id: javascriptallonge-making-data-out-of-functions
page_kind: source
summary: Making Data Out Of Functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.177-190
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter explores how data structures can be represented using only functions, delving into combinatory logic and the K, I, and V combinators. It demonstrates how functions can be used to model lists and pairs without relying on arrays or objects, and how this approach leads to a deeper understanding of computation and data representation.

## Key supported claims

- Functions model data structures like lists and pairs without arrays or objects, using K, I, and V combinators (raw/javascriptallonge.pdf p.177-190).
- K combinator creates constant functions, I combinator is identity function (raw/javascriptallonge.pdf p.177-190).
- V combinator, or Vireo, creates pairs from two values (raw/javascriptallonge.pdf p.177-190).
- Functions manipulate data structures allowing powerful abstractions (raw/javascriptallonge.pdf p.177-190).
- Computation performed using only functions, without traditional data structures (raw/javascriptallonge.pdf p.177-190).

## Technical details

### `technical-atom-a602b6ed0e697ed4` code

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
const EMPTY = {}; const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY  } } };
```

### `technical-atom-bcf2f885fa6c8526` code

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
OneTwoThree.rest.rest.first //=> 3 const length = (node, delayed = 0) => node === EMPTY ? delayed: length(node.rest, delayed + 1);
```

### `technical-atom-0c6f56ffdca20542` code

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
const K = (x) => (y) => x; const I = (x) => (x); const V = (x) => (y) => (z) => z(x)(y);
```

### `technical-atom-aea76708de48efca` code

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K, is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value.
```

### `technical-atom-e872e51be415c3cc` code

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
const K = (x) => (y) => x; const fortyTwo = K(42);
```

### `technical-atom-cd36d849b171aa54` code

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42. Very simple, but useful. Now we’ll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value.
```

### `technical-atom-5c8bfdbaaac4c2b2` code

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.
```

### `technical-atom-546c17e6abda1a4f` formula

Citation: (raw/javascriptallonge.pdf p.177-190)

> 76http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422

## Related technical details

### From [[javascriptallonge-why]]: `technical-atom-dff96b94ef792fdf` exception

Relation: nearby source page; matched terms `combinators`, `combinatory`, `javascript`, `logic`, `without`

Citation: (raw/javascriptallonge.pdf p.201)

This has little practical utility in JavaScript, but in combinatory logic it’s essential: With fixed-point combinators it’s possible to compute everything computable without binding names.

### From [[javascriptallonge-flip]]: `technical-atom-46f8909fd16287cb` code

Relation: nearby source page; matched terms `code`, `first`, `second`

Citation: (raw/javascriptallonge.pdf p.195-197)

```javascript
const mapWith = (first) => (second) => map(second, first);
```

### From [[javascriptallonge-flip]]: `technical-atom-b39bbfbb10f500bf` code

Relation: nearby source page; matched terms `code`, `first`, `second`

Citation: (raw/javascriptallonge.pdf p.195-197)

```javascript
(first) => (second) => fn(second, first);
```

### From [[javascriptallonge-why]]: `technical-atom-e050bf725570ce45` exception

Relation: nearby source page; matched terms `function`, `functions`, `without`

Citation: (raw/javascriptallonge.pdf p.201)

It enables you to make recursive functions without needing to bind a function to a name in an environment.
