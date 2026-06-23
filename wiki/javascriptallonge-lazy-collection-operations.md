---
page_id: javascriptallonge-lazy-collection-operations
page_kind: source
summary: lazy collection operations from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.253-256
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé – A modular guide to JavaScript fundamentals and advanced techniques, focusing on lazy collection operations and their efficiency.

## Key supported claims

- When working with very large collections and many operations, this can be important (raw/javascriptallonge.pdf p.253-256).
- The effect is even more pronounced when we use methods like first, until, or take: (raw/javascriptallonge.pdf p.253-256).
- This expression begins with a stack containing 30 elements (raw/javascriptallonge.pdf p.253-256).

## Technical details

### `technical-atom-73ed00db8219d949` code

Citation: (raw/javascriptallonge.pdf p.253-256)

```javascript
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0)
```

### `technical-atom-f67fb88b9bd0b506` code

Citation: (raw/javascriptallonge.pdf p.253-256)

```javascript
Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first()
```

### `technical-atom-0a45861b594c6c78` code

Citation: (raw/javascriptallonge.pdf p.253-256)

```javascript
Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => { console.log(`squaring ${ x } `); return x * x }) .filter((x) => { console.log(`filtering ${ x } `); return x % 2 == 0 }) .first() //=> squaring 29 filtering 841 squaring 28 filtering 784 784
```

### `technical-atom-21ef9586a52922ff` code

Citation: (raw/javascriptallonge.pdf p.253-256)

```javascript
[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29] .reverse() .map((x) => { console.log(`squaring ${ x } `); return x * x }) .filter((x) => { console.log(`filtering ${ x } `); return x % 2 == 0 })[0] //=> squaring 0 squaring 1 squaring 2 squaring 3 ... squaring 28 squaring 29 filtering 0 filtering 1 filtering 4 ... filtering 784 filtering 841 784
```

### `technical-atom-94dd91d8f0291f4d` code

Citation: (raw/javascriptallonge.pdf p.253-256)

```javascript
const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false , value: n++}) } } }, LazyCollection); const firstCubeOver1234 = Numbers .map((x) => x * x * x) .filter((x) => x > 1234) .first() //=> 1331
```

### `technical-atom-744115e2e3a310d4` procedure

Citation: (raw/javascriptallonge.pdf p.253-256)

Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer.
