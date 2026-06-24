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

## Related technical details

### From [[javascriptallonge-recursive-iterators]]: `technical-atom-158ef15f7acb62e3` code

Relation: nearby source page; matched terms `code`, `generation`, `isiterable`, `iterator`, `recursive`, `something`

Citation: (raw/javascriptallonge.pdf p.226)

```javascript
// Generation const isIterable = (something) => !!something[Symbol.iterator]; const generate = (iterable) => { for ( let element of iterable) { if (isIterable(element)) { generate(element) } else { console.log(element) } } } generate([1, [2, [3, 4], 5]]) //=> 1 2 3 4 5
```

### From [[javascriptallonge-operations-on-ordered-collections]]: `technical-atom-d72c10129ba795ef` code

Relation: nearby source page; matched terms `code`, `iterator`, `next`, `symbol`, `while`

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const filterWith = (fn, iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); return { next () { do { const {done, value} = iterator.next(); } while (!done && !fn(value)); return {done, value}; } } } }); const untilWith = (fn, iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); return { next () { let {done, value} = iterator.next(); done = done || fn(value); return ({done, value: done ? undefined : value}); } } } });
```

### From [[javascriptallonge-from]]: `technical-atom-096e3d7cf4be2948` code

Relation: nearby source page; matched terms `code`, `function`, `iteration`, `iterator`, `next`, `stack`

Citation: (raw/javascriptallonge.pdf p.221-222)

```javascript
Stack3.from = function (iterable) { const stack = this (); for ( let element of iterable) { stack.push(element); } return stack; } Pair1.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]())
```

### From [[javascriptallonge-operations-on-ordered-collections]]: `technical-atom-50415e1f6386aada` code

Relation: nearby source page; matched terms `code`, `iterator`, `next`, `symbol`

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: done ? undefined : fn(value)}); } } } });
```
