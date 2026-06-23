---
page_id: javascriptallonge-ordered-collections
page_kind: source
summary: ordered collections from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.216-217
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section of JavaScript Allongé discusses ordered collections, focusing on the semantic properties of iterables and how they relate to ordered collections.

## Key supported claims

- The iterables we're discussing represent ordered collections (raw/javascriptallonge.pdf p.216-217). One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning (raw/javascriptallonge.pdf p.216-217).
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator], and ensuring that our iterators start at the beginning and work forward (raw/javascriptallonge.pdf p.216-217).
- Iterables needn't represent ordered collections (raw/javascriptallonge.pdf p.216-217). We could make an infinite iterable representing random numbers (raw/javascriptallonge.pdf p.216-217).
- Therefore, RandomNumbers is not an ordered collection (raw/javascriptallonge.pdf p.216-217).

## Technical details

### `technical-atom-a18f6a4b28071fd1` code

Citation: (raw/javascriptallonge.pdf p.216-217)

```javascript
const abc = ["a", "b", "c"]; for ( const i of abc) { console.log(i) } //=> a b c for ( const i of abc) { console.log(i) } //=> a b c
```

### `technical-atom-af802d25f7fcd480` code

Citation: (raw/javascriptallonge.pdf p.216-217)

```javascript
const RandomNumbers = { [Symbol.iterator]: () => ({ next () { return {value: Math.random()}; } }) } for ( const i of RandomNumbers) { console.log(i) } //=> 0.494052127469331 0.835459444206208 0.1408337657339871 ... for ( const i of RandomNumbers) { console.log(i) } //=> 0.7845381607767195 0.4956772483419627 0.20259276474826038 ...
```

### `technical-atom-5feaaf7ac478828f` code

Citation: (raw/javascriptallonge.pdf p.216-217)

```
for ( const i of RandomNumbers) { console.log(i) } //=> 0.7845381607767195 0.4956772483419627 0.20259276474826038 ...
```

### `technical-atom-ad997c57b78950fc` requirement

Citation: (raw/javascriptallonge.pdf p.216-217)

Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers.
