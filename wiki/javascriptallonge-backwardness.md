---
page_id: javascriptallonge-backwardness
page_kind: source
summary: backwardness from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.180-182
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses how functions operate on data structures, contrasting conventional approaches with the backwardness of K and I combinators.

## Key supported claims

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data (raw/javascriptallonge.pdf p.180-182).
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object (raw/javascriptallonge.pdf p.180-182).
- You call them and pass them the bits, and they choose what to return (raw/javascriptallonge.pdf p.180-182).

## Technical details

### `technical-atom-e2bc09ff66f4620b` code

Citation: (raw/javascriptallonge.pdf p.180-182)

```javascript
const first = ([first, second]) => first, second = ([first, second]) => second; const latin = ["primus", "secundus"]; first(latin) //=> "primus" second(latin) //=> "secundus"
```

### `technical-atom-931474fff335fabf` code

Citation: (raw/javascriptallonge.pdf p.180-182)

```javascript
const first = ({first, second}) => first, second = ({first, second}) => second; const latin = {first: "primus", second: "secundus"}; first(latin) //=> "primus" second(latin) //=> "secundus"
```

### `technical-atom-0f83c91dfeba5e71` code

Citation: (raw/javascriptallonge.pdf p.180-182)

```javascript
const first = K, second = K(I); const latin = (selector) => selector("primus")("secundus"); latin(first) //=> "primus" latin(second) //=> "secundus"
```
