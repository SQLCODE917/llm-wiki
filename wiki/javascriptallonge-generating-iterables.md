---
page_id: javascriptallonge-generating-iterables
page_kind: source
summary: Generating Iterables from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.224-226
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter explains how iterables and generators work in JavaScript, covering iterator protocols, recursive iteration, state machines, and generator syntax.

## Key supported claims

- Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples. What is there they don't do well? (raw/javascriptallonge.pdf p.224-226)
- Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. (raw/javascriptallonge.pdf p.224-226)
- Iterators have to arrange its own state such that when you call them, they compute and return the next item. (raw/javascriptallonge.pdf p.224-226)

## Technical details

### `technical-atom-25debf1bd5150c87` code

Citation: (raw/javascriptallonge.pdf p.224-226)

```javascript
const Numbers = { [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false , value: n++}) } } };
```

### `technical-atom-a98fa92391927baf` code

Citation: (raw/javascriptallonge.pdf p.224-226)

```javascript
let n = 0; while ( true ) { console.log(n++) }
```

### `technical-atom-331f02c2738cde63` code

Citation: (raw/javascriptallonge.pdf p.224-226)

```javascript
// Iteration let n = 0; () => ({done: false , value: n++}) // Generation let n = 0; while ( true ) { console.log(n++) }
```

### `technical-atom-4317039718eba4b5` procedure

Citation: (raw/javascriptallonge.pdf p.224-226)

Iterables look cool, but then again, everything looks amazing when you're given cherry-picked examples.

### `technical-atom-efb7e60dcd1e8dce` procedure

Citation: (raw/javascriptallonge.pdf p.224-226)

Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done.

### `technical-atom-10b9ccb62f560bfc` procedure

Citation: (raw/javascriptallonge.pdf p.224-226)

Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### `technical-atom-d5b243613b22833a` worked-example

Citation: (raw/javascriptallonge.pdf p.224-226)

Let's consider how they work.

### `technical-atom-e82674fd1d436f3a` worked-example

Citation: (raw/javascriptallonge.pdf p.224-226)

If, for example, you want numbers, you write:

## Related technical details

### From [[javascriptallonge-operations-on-ordered-collections]]: `technical-atom-d72c10129ba795ef` code

Relation: nearby source page; matched terms `done`, `iterable`, `iterator`, `next`, `return`

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const filterWith = (fn, iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); return { next () { do { const {done, value} = iterator.next(); } while (!done && !fn(value)); return {done, value}; } } } }); const untilWith = (fn, iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); return { next () { let {done, value} = iterator.next(); done = done || fn(value); return ({done, value: done ? undefined : value}); } } } });
```

### From [[javascriptallonge-iteration]]: `technical-atom-e4b37a182a0d29ef` code

Relation: nearby source page; matched terms `done`, `iterable`, `iteration`, `iterator`, `iterators`, `next`

Citation: (raw/javascriptallonge.pdf p.227-228)

```javascript
const isIterable = (something) => !!something[Symbol.iterator]; const treeIterator = (iterable) => { const iterators = [ iterable[Symbol.iterator]() ]; return () => { while (!!iterators[0]) { const iterationResult = iterators[0].next(); if (iterationResult.done) { iterators.shift(); } else if (isIterable(iterationResult.value)) { iterators.unshift(iterationResult.value[Symbol.iterator]()); } else { return iterationResult.value; } } return ; } } const i = treeIterator([1, [2, [3, 4], 5]]); let n; while (n = i()) { console.log(n) } //=> 1 2 3 4 5
```

### From [[javascriptallonge-from]]: `technical-atom-096e3d7cf4be2948` code

Relation: nearby source page; matched terms `done`, `function`, `iterable`, `iteration`, `iterator`, `next`

Citation: (raw/javascriptallonge.pdf p.221-222)

```javascript
Stack3.from = function (iterable) { const stack = this (); for ( let element of iterable) { stack.push(element); } return stack; } Pair1.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]())
```

### From [[javascriptallonge-operations-on-ordered-collections]]: `technical-atom-50415e1f6386aada` code

Relation: nearby source page; matched terms `done`, `iterator`, `next`, `return`

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: done ? undefined : fn(value)}); } } } });
```
