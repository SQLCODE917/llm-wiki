---
page_id: javascriptallonge-the-vireo
page_kind: source
summary: the vireo from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.182-183
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

The Vireo (V combinator) and related combinators in the context of data structures, as described in JavaScript Allongé.

## Key supported claims

- The Vireo is a little like JavaScript's .apply function (raw/javascriptallonge.pdf p.182-183). It takes two values and applies them to a function.
- One notable example is the 'thrush' or T combinator (raw/javascriptallonge.pdf p.182-183). It takes one value and applies it to a function.
- The V combinator is used to make data structures with functions (raw/javascriptallonge.pdf p.182-183).

## Technical details

### `technical-atom-143779ac8d3aa938` code

Citation: (raw/javascriptallonge.pdf p.182-183)

```javascript
(first, second) => (selector) => selector(first)(second)
```

### `technical-atom-5b8d643220fdac8c` code

Citation: (raw/javascriptallonge.pdf p.182-183)

```javascript
(first) => (second) => (selector) => selector(first)(second)
```

### `technical-atom-256031f8fb9c7558` code

Citation: (raw/javascriptallonge.pdf p.182-183)

```javascript
const first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second); const latin = pair("primus")("secundus"); latin(first) //=> "primus" latin(second) //=> "secundus"
```

### `technical-atom-f6282633ff3f6e06` code

Citation: (raw/javascriptallonge.pdf p.182-183)

```javascript
const first = K, second = K(I), pair = V; const latin = pair("primus")("secundus"); latin(first) //=> "primus" latin(second) //=> "secundus"
```

### `technical-atom-fc35774e3ffe2b16` procedure

Citation: (raw/javascriptallonge.pdf p.182-183)

Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data.

### `technical-atom-d78941c9cf360b77` procedure

Citation: (raw/javascriptallonge.pdf p.182-183)

For arrays, we'd write cons = (first, second) => [first, second] .

### `technical-atom-ce93cc515740ca77` code

Citation: (raw/javascriptallonge.pdf p.182-183)

```
For objects we'd write: cons = (first, second) => {first, second} .
```

### `technical-atom-aa39093329fa518f` worked-example

Citation: (raw/javascriptallonge.pdf p.182-183)

One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function.
