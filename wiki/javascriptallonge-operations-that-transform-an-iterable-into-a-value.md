---
page_id: javascriptallonge-operations-that-transform-an-iterable-into-a-value
page_kind: source
summary: operations that transform an iterable into a value from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.286-286
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

A section on functions that transform iterables into values, including reduceWith and first.

## Key supported claims

- The reduceWith function iterates over an iterable and accumulates a value using a provided function, starting with a seed value (raw/javascriptallonge.pdf p.286-286).

## Technical details

### `technical-atom-381e027872bb52af` code

Citation: (raw/javascriptallonge.pdf p.286)

```javascript
const reduceWith = (fn, seed, iterable) => { let accumulator = seed; for ( const element of iterable) { accumulator = fn(accumulator, element); } return accumulator; }; const first = (iterable) => iterable[Symbol.iterator]().next().value;
```

## Related technical details

### From [[javascriptallonge-operations-that-compose-two-or-more-iterables-into-an-iterable]]: `technical-atom-bea88b2b1d9ec37b` code

Relation: nearby source page; matched terms `const`, `function`, `iterable`, `iterables`, `operations`, `value`

Citation: (raw/javascriptallonge.pdf p.285-286)

```javascript
function * zip (...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]()); while ( true ) { const pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); if (dones.indexOf( true ) >= 0) break ; yield values; } }; function * zipWith (zipper, ...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]()); while ( true ) { const pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); if (dones.indexOf( true ) >= 0) break ; yield zipper(...values); } };
```

### From [[javascriptallonge-operations-that-transform-one-iterable-into-another]]: `technical-atom-a6111cd07d4b016c` code

Relation: nearby source page; matched terms `const`, `function`, `iterable`, `operations`, `transform`, `value`

Citation: (raw/javascriptallonge.pdf p.284-285)

```javascript
yield * iterator; } function * take (numberToTake, iterable) { const iterator = iterable[Symbol.iterator](); for ( let i = 0; i < numberToTake; ++i) { const { done, value } = iterator.next(); if (!done) yield value; } }
```

### From [[javascriptallonge-operations-that-compose-two-or-more-iterables-into-an-iterable]]: `technical-atom-e8edac7970de02f5` code

Relation: nearby source page; matched terms `const`, `iterable`, `iterables`, `operations`, `values`

Citation: (raw/javascriptallonge.pdf p.285-286)

```javascript
const zip = callFirst(zipWith, (...values) => values);
```

### From [[javascriptallonge-memoizing-an-iterable]]: `technical-atom-e6b1617bec3d7b48` code

Relation: nearby source page; matched terms `const`, `function`, `iterable`, `key`, `value`

Citation: (raw/javascriptallonge.pdf p.286-287)

```javascript
function memoize (generator) { const memos = {}, iterators = {}; return function * (...args) { const key = JSON.stringify(args); let i = 0; if (memos[key] == null ) { memos[key] = []; iterators[key] = generator(...args); } while ( true ) { if (i < memos[key].length) { yield memos[key][i++]; } else { const { done, value } = iterators[key].next(); if (done) { return ; } else { yield memos[key][i++] = value;
```
