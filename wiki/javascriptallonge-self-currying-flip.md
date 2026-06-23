---
page_id: javascriptallonge-self-currying-flip
page_kind: source
summary: self-currying flip from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.196-196
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on self-currying flip function in JavaScriptAllongé, covering flip function and argument order reversal.

## Key supported claims

- Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). (raw/javascriptallonge.pdf p.196-196)
- Now if we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice. (raw/javascriptallonge.pdf p.196-196)

## Technical details

### `technical-atom-8a3beed3e846ae78` code

Citation: (raw/javascriptallonge.pdf p.196)

```javascript
const flip = (fn) => function (first, second) { if (arguments.length === 2) { return fn(second, first); } else { return function (second) { return fn(second, first); }; }; };
```

### `technical-atom-f30515c7413d55b0` formula

Citation: (raw/javascriptallonge.pdf p.196)

Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.
