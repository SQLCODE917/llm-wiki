---
page_id: javascriptallonge-lazy-and-eager-collections
page_kind: source
summary: Lazy and Eager Collections from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.246-260
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses lazy and eager collections in JavaScript, focusing on how iterables can be used to build more flexible and efficient data structures. It introduces the concepts of lazy and eager evaluation, and shows how to implement lazy collections using mixins.

## Key supported claims

- Lazy collections avoid computing values until needed, improving efficiency (raw/javascriptallonge.pdf p.246-260).
- Object-oriented collections should have methods for mapping, reducing, filtering, and finding, but delegate work to operations like mapWith (raw/javascriptallonge.pdf p.246-260).
- Eager collections, like arrays, return collections of their own type from methods, while lazy collections return iterable objects (raw/javascriptallonge.pdf p.246-260).
- Lazy evaluation is beneficial for memory footprint, especially with large collections and many operations (raw/javascriptallonge.pdf p.246-260).
- Lazy collections can work with infinite data structures, unlike eager collections which require finite data (raw/javascriptallonge.pdf p.246-260).

## Technical details

### `technical-atom-a52c46f037bbeeb7` code

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
const extend = function (consumer, ...providers) { for ( let i = 0; i < providers.length; ++i) { const provider = providers[i]; for ( let key in provider) { if (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } return consumer }; const LazyCollection = { map(fn) { return Object.assign({ [Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); return { next: () => { const { done, value } = iterator.next(); return ({ done, value: done ? undefined: fn(value) }); } } } }, LazyCollection); }, reduce(fn, seed) { const iterator = this [Symbol.iterator](); let iterationResult, accumulator = seed; while ((iterationResult = iterator.next(), !iterationResult.done)) { accumulator = fn(accumulator, iterationResult.value); } return accumulator;
```

### `technical-atom-7ddc2d4dcee1ea5c` code

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
[Symbol.iterator]: () => { const iterator = this [Symbol.iterator](); let remainingElements = numberToTake; return { next: () => { let { done, value } = iterator.next(); done = done || remainingElements-- <= 0; return ({ done, value: done ? undefined: value }); } } } }, LazyCollection); } }
```

### `technical-atom-58aa25a886463191` code

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false, value: n++}) } } }, LazyCollection);
```

### `technical-atom-3c723810f6878c2b` code

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
const EMPTY = { isEmpty: () => true
```

### `technical-atom-e97cd814986fada0` code

Citation: (raw/javascriptallonge.pdf p.246-260)

```
};
```

### `technical-atom-e9d064f7061e7fe2` code

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
const isEmpty = (node) => node === EMPTY;
```

### `technical-atom-8d6f83afe6ff7090` code

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
const Pair = (car, cdr = EMPTY) => Object.assign({ car, cdr, isEmpty: () => false, [Symbol.iterator]: function () { let currentPair = this; return { next: () => { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.car; currentPair = currentPair.cdr; return {done: false, value} } } } } }, LazyCollection); Pair.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next();
```

### `technical-atom-32ba891739150b9e` code

Citation: (raw/javascriptallonge.pdf p.246-260)

```javascript
return done ? EMPTY: Pair(value, iterationToList(iteration)); })(iterable[Symbol.iterator]());
```

## Related technical details

### From [[javascriptallonge-generating-iterables]]: `technical-atom-8939346e4f8483e2` code

Relation: nearby source page; matched terms `iterable`, `iterables`, `return`, `while`

Citation: (raw/javascriptallonge.pdf p.224-245)

```javascript
// Iteration const isIterable = (something) => !!something[Symbol.iterator]; const treeIterator = (iterable) => { const iterators = [ iterable[Symbol.iterator]()]; return () => { while (!!iterators[0]) { const iterationResult = iterators[0].next(); if (iterationResult.done) { iterators.shift(); } else if (isIterable(iterationResult.value)) { iterators.unshift(iterationResult.value[Symbol.iterator]()); } else { return iterationResult.value; } } return; } } const i = treeIterator([1, [2, [3, 4], 5]]); let n; while (n = i()) { console.log(n) } //=> 1 2 3 4 5
```

### From [[javascriptallonge-iteration-and-iterables]]: `technical-atom-be126e6eb38ca51a` code

Relation: nearby source page; matched terms `but`, `fat`, `iterables`, `javascript`

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is defined with a fat arrow () => { ... }. What is the value of this within that function?
```

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-06f854f6dd0c3ede` code

Relation: nearby source page; matched terms `iterable`, `iterables`, `mapwith`, `operations`

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
function * mapWith(fn, iterable) { for ( const element of iterable) { yield fn(element); } } function * mapAllWith (fn, iterable) { for ( const element of iterable) { yield * fn(element); } } function * filterWith (fn, iterable) { for ( const element of iterable) { if (!!fn(element)) yield element; } } function * compact (iterable) { for ( const element of iterable) { if (element != null) yield element; } } function * untilWith (fn, iterable) { for ( const element of iterable) { if (fn(element)) break; yield fn(element); } } function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next();
```

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-35b2273acd61afdb` code

Relation: nearby source page; matched terms `iterable`, `iterables`, `operations`, `return`

Citation: (raw/javascriptallonge.pdf p.284-287)

```javascript
for ( const element of iterable) { accumulator = fn(accumulator, element); } return accumulator; }; const first = (iterable) => iterable[Symbol.iterator]().next().value;
```
