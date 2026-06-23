---
page_id: javascriptallonge-rewriting-iterable-operations
page_kind: source
summary: rewriting iterable operations from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.243-245
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on rewriting iterable operations using generators in JavaScript Allongé.

## Key supported claims

- Generators simplify rewriting iterable operations like mapWith, filterWith, and untilWith. (raw/javascriptallonge.pdf p.243-245)
- The first function works directly with iterators, but rest can be rewritten using generators. (raw/javascriptallonge.pdf p.243-245)
- This approach simplifies implementation of iterable operations by leveraging generators. (raw/javascriptallonge.pdf p.243-245)

## Technical details

### `technical-atom-653bde3e9e9c4aff` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```javascript
const mapWith = (fn, iterable) => ({ [Symbol.iterator]: () => { const iterator = iterable[Symbol.iterator](); return { next: () => { const {done, value} = iterator.next(); return ({done, value: done ? undefined : fn(value)}); } } } });
```

### `technical-atom-c172f364acc1fc24` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```javascript
function * mapWith (fn, iterable) { for ( const element of iterable) { yield fn(element); } }
```

### `technical-atom-03d1fc7cec3dda78` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```javascript
function * mapWith(fn, iterable) { for ( const element of iterable) { yield fn(element); } } function * filterWith (fn, iterable) { for ( const element of iterable) { if (!!fn(element)) yield element; } }
```

### `technical-atom-077d7b8cac2a0edc` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```javascript
function * untilWith (fn, iterable) { for ( const element of iterable) { if (fn(element)) break ; yield fn(element); } }
```

### `technical-atom-0945972be4c692ed` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```javascript
const first = (iterable) => iterable[Symbol.iterator]().next().value; function * rest (iterable) { const iterator = iterable[Symbol.iterator](); iterator.next(); yield * iterator; }
```

### `technical-atom-e5fe0bb1382fd951` procedure

Citation: (raw/javascriptallonge.pdf p.243-245)

No need to return an object with a .next() method.

### `technical-atom-b7122d7c07937413` code

Citation: (raw/javascriptallonge.pdf p.243-245)

```
No need to fool around with {done} or {value} , just yield values until we're done.
```
