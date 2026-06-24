---
page_id: javascriptallonge-ordered-collections
page_kind: source
summary: ordered collections from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.216-217
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section of JavaScript Allongé discusses ordered collections, focusing on the semantic properties of iterables and how they relate to ordered collections.

## Key supported claims

- The iterables we're discussing represent ordered collections (raw/javascriptallonge.pdf p.216-217). One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning (raw/javascriptallonge.pdf p.216-217).
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator], and ensuring that our iterators start at the beginning and work forward (raw/javascriptallonge.pdf p.216-217).
- Iterables needn't represent ordered collections (raw/javascriptallonge.pdf p.216-217). We could make an infinite iterable representing random numbers (raw/javascriptallonge.pdf p.216-217).
- Therefore, RandomNumbers is not an ordered collection (raw/javascriptallonge.pdf p.216-217).

## Technical details

### `technical-atom-a18f6a4b28071fd1` code

Citation: (raw/javascriptallonge.pdf p.216-217)

```javascript
const abc = ["a", "b", "c"]; for ( const i of abc) { console.log(i) } //=> a b c for ( const i of abc) { console.log(i) } //=> a b c
```

### `technical-atom-af802d25f7fcd480` code

Citation: (raw/javascriptallonge.pdf p.216-217)

```javascript
const RandomNumbers = { [Symbol.iterator]: () => ({ next () { return {value: Math.random()}; } }) } for ( const i of RandomNumbers) { console.log(i) } //=> 0.494052127469331 0.835459444206208 0.1408337657339871 ... for ( const i of RandomNumbers) { console.log(i) } //=> 0.7845381607767195 0.4956772483419627 0.20259276474826038 ...
```

### `technical-atom-5feaaf7ac478828f` code

Citation: (raw/javascriptallonge.pdf p.216-217)

```
for ( const i of RandomNumbers) { console.log(i) } //=> 0.7845381607767195 0.4956772483419627 0.20259276474826038 ...
```

### `technical-atom-ad997c57b78950fc` requirement

Citation: (raw/javascriptallonge.pdf p.216-217)

Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers.

## Related technical details

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-3f7ceba972853444` code

Relation: nearby source page; matched terms `collection`, `get`, `iterable`, `iterables`, `iterator`, `symbol`

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```

### From [[javascriptallonge-operations-on-ordered-collections]]: `technical-atom-50415e1f6386aada` code

Relation: nearby source page; matched terms `collection`, `collections`, `iterator`, `ordered`, `symbol`

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: done ? undefined : fn(value)}); } } } });
```

### From [[javascriptallonge-operations-on-ordered-collections]]: `technical-atom-7439d56d23a56b66` code

Relation: nearby source page; matched terms `collections`, `iterator`, `numbers`, `ordered`, `symbol`

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const Evens = { [Symbol.iterator] () { const iterator = Numbers[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: done ? undefined : 2 *value}); } } } };
```

### From [[javascriptallonge-operations-on-ordered-collections]]: `technical-atom-d72c10129ba795ef` code

Relation: nearby source page; matched terms `collections`, `iterable`, `iterator`, `ordered`, `symbol`

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const filterWith = (fn, iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); return { next () { do { const {done, value} = iterator.next(); } while (!done && !fn(value)); return {done, value}; } } } }); const untilWith = (fn, iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); return { next () { let {done, value} = iterator.next(); done = done || fn(value); return ({done, value: done ? undefined : value}); } } } });
```
