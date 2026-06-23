---
page_id: javascriptallonge-higher-order-functions
page_kind: source
summary: higher-order functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.68-68
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript Allongé discusses higher-order functions, which are functions that take functions as arguments, return functions, or both.

## Key supported claims

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. (raw/javascriptallonge.pdf p.68-68)
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. (raw/javascriptallonge.pdf p.68-68)
- Higher-order functions dominate JavaScript Allongé. (raw/javascriptallonge.pdf p.68-68)
- But before we go on, we'll talk about some specific types of higher-order functions. (raw/javascriptallonge.pdf p.68-68)

## Technical details

### `technical-atom-4156650bc7d6a27a` code

Citation: (raw/javascriptallonge.pdf p.68)

```javascript
const repeat = (num, fn) => (num > 0) ? (repeat(num - 1, fn), fn(num)) : undefined repeat(3, function (n) { console.log(`Hello ${ n } `) }) //=> 'Hello 1' 'Hello 2' 'Hello 3' undefined
```
