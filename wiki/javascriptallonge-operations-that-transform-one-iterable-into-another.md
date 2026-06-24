---
page_id: javascriptallonge-operations-that-transform-one-iterable-into-another
page_kind: source
summary: operations that transform one iterable into another from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.284-285
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section describes operations that transform one iterable into another, focusing on generator functions that process iterables. Key functions include `mapWith`, `mapAllWith`, `filterWith`, `compact`, `untilWith`, `rest`, and `take`.

## Key supported claims

- The `mapWith` function maps each element of an iterable using a provided function, as described in (raw/javascriptallonge.pdf p.284-285).
- The `take` function takes a specified number of elements from an iterable, as described in (raw/javascriptallonge.pdf p.284-285).

## Technical details

### `technical-atom-bfed2cc6c8f4d01a` code

Citation: (raw/javascriptallonge.pdf p.284-285)

```javascript
function * mapWith(fn, iterable) { for ( const element of iterable) { yield fn(element); } } function * mapAllWith (fn, iterable) { for ( const element of iterable) { yield * fn(element); } } function * filterWith (fn, iterable) { for ( const element of iterable) { if (!!fn(element)) yield element; } } function * compact (iterable) { for ( const element of iterable) { if (element != null ) yield element; } } function * untilWith (fn, iterable) { for ( const element of iterable) { if (fn(element)) break ; yield fn(element); } } function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next();
```

### `technical-atom-a6111cd07d4b016c` code

Citation: (raw/javascriptallonge.pdf p.284-285)

```javascript
yield * iterator; } function * take (numberToTake, iterable) { const iterator = iterable[Symbol.iterator](); for ( let i = 0; i < numberToTake; ++i) { const { done, value } = iterator.next(); if (!done) yield value; } }
```

## Related technical details

### From [[javascriptallonge-operations-that-transform-an-iterable-into-a-value]]: `technical-atom-381e027872bb52af` code

Relation: nearby source page; matched terms `const`, `element`, `iterable`, `iterator`, `operations`, `transform`

Citation: (raw/javascriptallonge.pdf p.286)

```javascript
const reduceWith = (fn, seed, iterable) => { let accumulator = seed; for ( const element of iterable) { accumulator = fn(accumulator, element); } return accumulator; }; const first = (iterable) => iterable[Symbol.iterator]().next().value;
```

### From [[javascriptallonge-operations-that-compose-two-or-more-iterables-into-an-iterable]]: `technical-atom-bea88b2b1d9ec37b` code

Relation: nearby source page; matched terms `const`, `function`, `iterable`, `iterables`, `iterator`, `operations`

Citation: (raw/javascriptallonge.pdf p.285-286)

```javascript
function * zip (...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]()); while ( true ) { const pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); if (dones.indexOf( true ) >= 0) break ; yield values; } }; function * zipWith (zipper, ...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]()); while ( true ) { const pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); if (dones.indexOf( true ) >= 0) break ; yield zipper(...values); } };
```

### From [[javascriptallonge-memoizing-an-iterable]]: `technical-atom-e6b1617bec3d7b48` code

Relation: nearby source page; matched terms `const`, `function`, `generator`, `iterable`, `key`, `yield`

Citation: (raw/javascriptallonge.pdf p.286-287)

```javascript
function memoize (generator) { const memos = {}, iterators = {}; return function * (...args) { const key = JSON.stringify(args); let i = 0; if (memos[key] == null ) { memos[key] = []; iterators[key] = generator(...args); } while ( true ) { if (i < memos[key].length) { yield memos[key][i++]; } else { const { done, value } = iterators[key].next(); if (done) { return ; } else { yield memos[key][i++] = value;
```

### From [[javascriptallonge-this-seems-familiar]]: `technical-atom-45ad4257e07d061d` procedure

Relation: nearby source page; matched terms `function`, `generator`, `procedure`, `using`, `yield`

Citation: (raw/javascriptallonge.pdf p.280-282)

With iterators, we wrote a generator function using function * , and then used yield to yield values while maintaining the implicit state of the generator's control flow.
