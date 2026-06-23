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
