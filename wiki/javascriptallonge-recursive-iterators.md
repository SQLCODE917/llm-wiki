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
