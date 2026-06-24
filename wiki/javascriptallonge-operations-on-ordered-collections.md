---
page_id: javascriptallonge-operations-on-ordered-collections
page_kind: source
summary: operations on ordered collections from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.217-221
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé – A modular guide to JavaScript fundamentals and advanced techniques, chapter on operations on ordered collections.

## Key supported claims

- Many operations on ordered collections return another ordered collection. (raw/javascriptallonge.pdf p.217-221)
- This illustrates the general pattern of working with ordered collections: We make them iterables, meaning that they have a [Symbol.iterator] method, that returns an iterator. (raw/javascriptallonge.pdf p.217-221)
- 89 Yes, we also used the name mapWith for working with ordinary collections elsewhere. (raw/javascriptallonge.pdf p.217-221)
- Here's mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original: 89 (raw/javascriptallonge.pdf p.217-221)

## Technical details

### `technical-atom-50415e1f6386aada` code

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: done ? undefined : fn(value)}); } } } });
```

### `technical-atom-716deeea5691a48e` code

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const Evens = mapWith((x) => 2 * x, Numbers); for ( const i of Evens) { console.log(i) } //=> 0 2 4 ... for ( const i of Evens) { console.log(i) } //=> 0 2 4 ...
```

### `technical-atom-7439d56d23a56b66` code

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const Evens = { [Symbol.iterator] () { const iterator = Numbers[Symbol.iterator](); return { next () { const {done, value} = iterator.next(); return ({done, value: done ? undefined : 2 *value}); } } } };
```

### `technical-atom-5c3653b8cf597db3` code

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers); for ( const i of ZeroesToNines) { console.log(i) } //=> 5 1 9 ... for ( const i of ZeroesToNines) { console.log(i) } //=> 3
```

### `technical-atom-005c91f7071e2bde` code

Citation: (raw/javascriptallonge.pdf p.217-221)

```
6 1 ...
```

### `technical-atom-d72c10129ba795ef` code

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const filterWith = (fn, iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); return { next () { do { const {done, value} = iterator.next(); } while (!done && !fn(value)); return {done, value}; } } } }); const untilWith = (fn, iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); return { next () { let {done, value} = iterator.next(); done = done || fn(value); return ({done, value: done ? undefined : value}); } } } });
```

### `technical-atom-8590a4ffcf6201ab` code

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const Squares = mapWith((x) => x * x, Numbers); const EndWithOne = filterWith((x) => x % 10 === 1, Squares); const UpTo1000 = untilWith((x) => (x > 1000), EndWithOne); [...UpTo1000] //=> [1,81,121,361,441,841,961] [...UpTo1000] //=> [1,81,121,361,441,841,961]
```

### `technical-atom-ba45ce02826374bb` code

Citation: (raw/javascriptallonge.pdf p.217-221)

```javascript
const first = (iterable) => iterable[Symbol.iterator]().next().value; const rest = (iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); iterator.next(); return iterator; } });
```

## Related technical details

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-f9a05369dedddd46` requirement

Relation: nearby source page; matched terms `iterables`, `iterator`, `method`, `name`, `operations`, `representing`

Citation: (raw/javascriptallonge.pdf p.211-215)

The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.

### From [[javascriptallonge-ordered-collections]]: `technical-atom-af802d25f7fcd480` code

Relation: nearby source page; matched terms `collections`, `iterator`, `ordered`, `return`, `symbol`

Citation: (raw/javascriptallonge.pdf p.216-217)

```javascript
const RandomNumbers = { [Symbol.iterator]: () => ({ next () { return {value: Math.random()}; } }) } for ( const i of RandomNumbers) { console.log(i) } //=> 0.494052127469331 0.835459444206208 0.1408337657339871 ... for ( const i of RandomNumbers) { console.log(i) } //=> 0.7845381607767195 0.4956772483419627 0.20259276474826038 ...
```

### From [[javascriptallonge-basic-operations-on-iterables]]: `technical-atom-3f7ceba972853444` code

Relation: nearby source page; matched terms `collection`, `iterables`, `iterator`, `operations`, `return`, `symbol`

Citation: (raw/javascriptallonge.pdf p.284)

```javascript
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```

### From [[javascriptallonge-from]]: `technical-atom-096e3d7cf4be2948` code

Relation: nearby source page; matched terms `function`, `iterator`, `return`, `symbol`

Citation: (raw/javascriptallonge.pdf p.221-222)

```javascript
Stack3.from = function (iterable) { const stack = this (); for ( let element of iterable) { stack.push(element); } return stack; } Pair1.from = (iterable) => ( function iterationToList (iteration) { const {done, value} = iteration.next(); return done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]())
```
