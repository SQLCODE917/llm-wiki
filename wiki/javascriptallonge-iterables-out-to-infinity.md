---
page_id: javascriptallonge-iterables-out-to-infinity
page_kind: source
summary: iterables out to infinity from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.215-216
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on iterables out to infinity from JavaScript Allongé.

## Key supported claims

- There are useful things we can do with infinite iterables, (raw/javascriptallonge.pdf p.215-216)
- Attempting to spread an infinite iterable into an array fails, (raw/javascriptallonge.pdf p.215-216)
- First and second element of an infinite iterable causes an infinite loop, (raw/javascriptallonge.pdf p.215-216)

## Technical details

### `technical-atom-6afb74908999e9bc` code

Citation: (raw/javascriptallonge.pdf p.215-216)

```javascript
const Numbers = { [Symbol.iterator] () { let n = 0; return { next: () => ({done: false , value: n++}) } } }
```

### `technical-atom-ef48bceaea29f284` code

Citation: (raw/javascriptallonge.pdf p.215-216)

```javascript
['all the numbers', ...Numbers] //=> infinite loop! firstAndSecondElement(...Numbers) //=> infinite loop!
```

### `technical-atom-c38fd21e3f99a4e6` requirement

Citation: (raw/javascriptallonge.pdf p.215-216)

Attempting to spread an infinite iterable into an array is always going to fail.

## Related technical details

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-6eadb95cbdf43456` code

Relation: nearby source page; matched terms `first`, `firstandsecondelement`, `iterables`, `second`

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
const firstAndSecondElement = (first, second) => ({first, second}) firstAndSecondElement(...stack) //=> {"first":5,"second":10}
```

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-3f7ceba972853444` code

Relation: nearby source page; matched terms `iterable`, `iterables`, `loop`

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-13e57f96247ba73c` worked-example

Relation: nearby source page; matched terms `element`, `iterables`, `spread`

Citation: (raw/javascriptallonge.pdf p.211-215)

For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

### From [[javascriptallonge-from]]: `technical-atom-096e3d7cf4be2948` code

Relation: nearby source page; matched terms `element`, `function`, `iterable`

Citation: (raw/javascriptallonge.pdf p.221-222)

```javascript
Stack3.from = function (iterable) { const stack = this (); for ( let element of iterable) { stack.push(element); } return stack; } Pair1.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]())
```
