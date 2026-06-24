---
page_id: javascriptallonge-recursive-iterators
page_kind: source
summary: recursive iterators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.226-226
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on recursive iterators in JavaScript Allongé, discussing how iterators maintain state and the ease of managing state in generators for recursive enumeration.

## Key supported claims

- Iterators maintain state, that's what they do. (raw/javascriptallonge.pdf p.226-226)

## Technical details

### `technical-atom-158ef15f7acb62e3` code

Citation: (raw/javascriptallonge.pdf p.226)

```javascript
// Generation const isIterable = (something) => !!something[Symbol.iterator]; const generate = (iterable) => { for ( let element of iterable) { if (isIterable(element)) { generate(element) } else { console.log(element) } } } generate([1, [2, [3, 4], 5]]) //=> 1 2 3 4 5
```

### `technical-atom-57e0d6846ecd61e8` worked-example

Citation: (raw/javascriptallonge.pdf p.226)

For example, iterating over a tree.

## Related technical details

### From [[javascriptallonge-generating-iterables]]: `technical-atom-10b9ccb62f560bfc` procedure

Relation: nearby source page; matched terms `iterators`, `state`, `they`

Citation: (raw/javascriptallonge.pdf p.224-226)

Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### From [[javascriptallonge-javascript-s-generators]]: `technical-atom-00fab8fb6887a7bc` procedure

Relation: nearby source page; matched terms `generators`, `iterators`, `javascript`

Citation: (raw/javascriptallonge.pdf p.230-231)

It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator.
