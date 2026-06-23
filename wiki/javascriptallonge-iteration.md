---
page_id: javascriptallonge-iteration
page_kind: source
summary: // Iteration from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.227-228
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses iteration in JavaScript, comparing iterative and generative approaches to handling data structures like trees.

## Key supported claims

- If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next, we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. (raw/javascriptallonge.pdf p.227-228)
- In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit, while the iteration version's stack is explicit. (raw/javascriptallonge.pdf p.227-228)
- A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out. (raw/javascriptallonge.pdf p.227-228)

## Technical details

### `technical-atom-e4b37a182a0d29ef` code

Citation: (raw/javascriptallonge.pdf p.227-228)

```javascript
const isIterable = (something) => !!something[Symbol.iterator]; const treeIterator = (iterable) => { const iterators = [ iterable[Symbol.iterator]() ]; return () => { while (!!iterators[0]) { const iterationResult = iterators[0].next(); if (iterationResult.done) { iterators.shift(); } else if (isIterable(iterationResult.value)) { iterators.unshift(iterationResult.value[Symbol.iterator]()); } else { return iterationResult.value; } } return ; } } const i = treeIterator([1, [2, [3, 4], 5]]); let n; while (n = i()) { console.log(n) } //=> 1 2 3 4 5
```

### `technical-atom-b526abb079ec9050` procedure

Citation: (raw/javascriptallonge.pdf p.227-228)

If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack.

### `technical-atom-cae674bcd9bcea03` procedure

Citation: (raw/javascriptallonge.pdf p.227-228)

A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We're reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out.
