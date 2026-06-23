---
page_id: javascriptallonge-bonus
page_kind: source
summary: bonus from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.175-176
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Summary of the bonus chapter from JavaScript Allongé, focusing on lazy evaluation and collection operations in JavaScript.

## Key supported claims

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. (raw/javascriptallonge.pdf p.175-176)
- In Smalltalk, for example, they are known as collect , select , and detect . (raw/javascriptallonge.pdf p.175-176)
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. (raw/javascriptallonge.pdf p.175-176)

## Technical details

### `technical-atom-06627249e05d277a` code

Citation: (raw/javascriptallonge.pdf p.175-176)

```javascript
const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);
```

### `technical-atom-88e9bb41a37459ac` code

Citation: (raw/javascriptallonge.pdf p.175-176)

```javascript
const firstInArray = (fn, array) => array.filter(fn)[0];
```

### `technical-atom-071065f77ad2e28e` worked-example

Citation: (raw/javascriptallonge.pdf p.175-176)

In Smalltalk, for example, they are known as collect , select , and detect .
