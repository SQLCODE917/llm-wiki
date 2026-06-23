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
