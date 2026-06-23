---
page_id: javascriptallonge-flipping-methods
page_kind: source
summary: flipping methods from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.196-197
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

A section on flipping methods in JavaScript, detailing how the `flip` function handles context and arguments.

## Key supported claims

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods (raw/javascriptallonge.pdf p.196-197).

## Technical details

### `technical-atom-9068ab765ef9c6b4` code

Citation: (raw/javascriptallonge.pdf p.196-197)

```javascript
const flipAndCurry = (fn) => (first) => function (second) { return fn.call( this , second, first); } const flip = (fn) => function (first, second) { return fn.call( this , second, first); } const flip = (fn) => function (first, second) { if (arguments.length === 2) { return fn.call( this , second, first); } else { return function (second) { return fn.call( this , second, first); }; }; };
```
