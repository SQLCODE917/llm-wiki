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
