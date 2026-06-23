---
page_id: javascriptallonge-as-little-as-possible-about-functions-but-no-less
page_kind: source
summary: As Little As Possible About Functions, But No Less from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.30-31
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

JavaScript functions are values that evaluate expressions, return values, and have identity semantics.

## Key supported claims

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps (raw/javascriptallonge.pdf p.30-31).
- Functions represent computations to be performed (raw/javascriptallonge.pdf p.30-31).
- This is a function that is applied to no values and returns 0 (raw/javascriptallonge.pdf p.30-31).
- But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function (raw/javascriptallonge.pdf p.30-31).

## Technical details

### `technical-atom-69e1fbd469e13ef0` code

Citation: (raw/javascriptallonge.pdf p.30-31)

```javascript
() => 0
```

### `technical-atom-d5ce0404744a426c` code

Citation: (raw/javascriptallonge.pdf p.30-31)

```javascript
(() => 0) //=> [Function]
```

### `technical-atom-351705f992de337d` code

Citation: (raw/javascriptallonge.pdf p.30-31)

```
16 The simplest possible function is () => {} , we'll see that later.
```

### `technical-atom-59c2775910c3d844` requirement

Citation: (raw/javascriptallonge.pdf p.30-31)

I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read.

### `technical-atom-dbe44efe552e814c` requirement

Citation: (raw/javascriptallonge.pdf p.30-31)

But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.
