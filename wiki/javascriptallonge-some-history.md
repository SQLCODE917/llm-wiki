---
page_id: javascriptallonge-some-history
page_kind: source
summary: some history from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.128-130
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section traces the history of Lisp, describing its early implementation on the IBM 704, the fundamental cons cell data structure, and how concepts like CAR and CDR influenced JavaScript's handling of lists and data structures.

## Key supported claims

- Lisp, an acronym for LISt Processing, was one of the first high-level languages implemented on the IBM 704 computer (raw/javascriptallonge.pdf p.128-130).
- The 704's 36-bit word allowed fast storage and retrieval of 36-bit values, with macros CAR and CDR fetching parts of the register (raw/javascriptallonge.pdf p.128-130).
- In Lisp, the basic data type was the cons cell, storing two 15-bit values in one 36-bit word, forming linked lists (raw/javascriptallonge.pdf p.128-130).
- Lisp's design was driven by hardware constraints, with lists implemented as linked structures for performance (raw/javascriptallonge.pdf p.128-130).

## Technical details

### `technical-atom-1451d25bd3016c58` code

Citation: (raw/javascriptallonge.pdf p.128-130)

```javascript
const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
```

### `technical-atom-d38984d5b4083a09` code

Citation: (raw/javascriptallonge.pdf p.128-130)

```javascript
const oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, null )))));
```

### `technical-atom-75aab7329b283251` code

Citation: (raw/javascriptallonge.pdf p.128-130)

```javascript
oneToFive //=> [1,[2,[3,[4,[5,null]]]]]
```

### `technical-atom-749bb0a56b85ef20` code

Citation: (raw/javascriptallonge.pdf p.128-130)

```javascript
const node5 = [5, null ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1;
```

### `technical-atom-99b7fc7c713718bc` code

Citation: (raw/javascriptallonge.pdf p.128-130)

```javascript
car(oneToFive) //=> 1
```

### `technical-atom-74f447b66d73d9da` code

Citation: (raw/javascriptallonge.pdf p.128-130)

```javascript
cdr(oneToFive) //=> [2,[3,[4,[5,null]]]]
```

### `technical-atom-5ca2ae0ca0604e0a` exception

Citation: (raw/javascriptallonge.pdf p.128-130)

Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance.

### `technical-atom-04ba09a2311c5fc1` exception

Citation: (raw/javascriptallonge.pdf p.128-130)

In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array.
