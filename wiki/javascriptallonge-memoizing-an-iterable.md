---
page_id: javascriptallonge-memoizing-an-iterable
page_kind: source
summary: memoizing an iterable from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.286-287
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé – A modular guide to JavaScript fundamentals and advanced techniques, focusing on memoizing iterables.

## Key supported claims

- The memoize function creates a generator that caches results using memos and iterators (raw/javascriptallonge.pdf p.286-287).
- The implementation is served by the Pot: Collections 264 (raw/javascriptallonge.pdf p.286-287).

## Technical details

### `technical-atom-e6b1617bec3d7b48` code

Citation: (raw/javascriptallonge.pdf p.286-287)

```javascript
function memoize (generator) { const memos = {}, iterators = {}; return function * (...args) { const key = JSON.stringify(args); let i = 0; if (memos[key] == null ) { memos[key] = []; iterators[key] = generator(...args); } while ( true ) { if (i < memos[key].length) { yield memos[key][i++]; } else { const { done, value } = iterators[key].next(); if (done) { return ; } else { yield memos[key][i++] = value;
```

## Related technical details

### From [[javascriptallonge-operations-that-compose-two-or-more-iterables-into-an-iterable]]: `technical-atom-bea88b2b1d9ec37b` code

Relation: nearby source page; matched terms `const`, `function`, `iterable`, `iterables`, `iterators`

Citation: (raw/javascriptallonge.pdf p.285-286)

```javascript
function * zip (...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]()); while ( true ) { const pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); if (dones.indexOf( true ) >= 0) break ; yield values; } }; function * zipWith (zipper, ...iterables) { const iterators = iterables.map(i => i[Symbol.iterator]()); while ( true ) { const pairs = iterators.map(j => j.next()), dones = pairs.map(p => p.done), values = pairs.map(p => p.value); if (dones.indexOf( true ) >= 0) break ; yield zipper(...values); } };
```

### From [[javascriptallonge-how-to-run-the-examples]]: `technical-atom-ad281399ada1cea7` code

Relation: nearby source page; matched terms `const`, `function`, `key`

Citation: (raw/javascriptallonge.pdf p.289-290)

```javascript
const before = (decoration) => (method) => function (...args) { decoration.apply( this , args); return method.apply( this , args) }; And it would be 'transpiled' into: var before = function (decoration) { return function (method) { return function () { for ( let _len = arguments.length, args = Array(_len), _key = 0; _key < _le\ n; _key++) { args[_key] = arguments[_key]; } decoration.apply( this , args); return method.apply( this , args); }; }; };
```

### From [[javascriptallonge-operations-that-compose-two-or-more-iterables-into-an-iterable]]: `technical-atom-e8edac7970de02f5` code

Relation: nearby source page; matched terms `const`, `iterable`, `iterables`

Citation: (raw/javascriptallonge.pdf p.285-286)

```javascript
const zip = callFirst(zipWith, (...values) => values);
```

### From [[javascriptallonge-operations-that-transform-one-iterable-into-another]]: `technical-atom-bfed2cc6c8f4d01a` code

Relation: nearby source page; matched terms `const`, `function`, `iterable`

Citation: (raw/javascriptallonge.pdf p.284-285)

```javascript
function * mapWith(fn, iterable) { for ( const element of iterable) { yield fn(element); } } function * mapAllWith (fn, iterable) { for ( const element of iterable) { yield * fn(element); } } function * filterWith (fn, iterable) { for ( const element of iterable) { if (!!fn(element)) yield element; } } function * compact (iterable) { for ( const element of iterable) { if (element != null ) yield element; } } function * untilWith (fn, iterable) { for ( const element of iterable) { if (fn(element)) break ; yield fn(element); } } function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next();
```
