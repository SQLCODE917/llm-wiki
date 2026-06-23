---
page_id: javascriptallonge-the-kestrel-and-the-idiot
page_kind: source
summary: the kestrel and the idiot from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.179-180
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on the kestrel and the idiot functions from JavaScript Allongé, discussing combinators and function manipulation.

## Key supported claims

- The kestrel, or K, is a function that makes constant functions, such that K(x)(y) => x (raw/javascriptallonge.pdf p.179-180).
- The identity function is a function that evaluates to whatever parameter you pass it, so I(42) => 42 (raw/javascriptallonge.pdf p.179-180).
- Given two values, we can say that K always returns the first value: K(x)(y) => x (raw/javascriptallonge.pdf p.179-180).

## Technical details

### `technical-atom-fd5f49f3f2ce290f` code

Citation: (raw/javascriptallonge.pdf p.179-180)

```javascript
const K = (x) => (y) => x; const fortyTwo = K(42); fortyTwo(6) //=> 42 fortyTwo("Hello") //=> 42
```

### `technical-atom-e8d6f99024d7e30f` code

Citation: (raw/javascriptallonge.pdf p.179-180)

```javascript
K(6)(7) //=> 6 K(12)(24) //=> 12
```

### `technical-atom-4f64013f1e1330ba` code

Citation: (raw/javascriptallonge.pdf p.179-180)

```javascript
Therefore, K(I)(x)(y) => y :
```

### `technical-atom-4d145fb366989e74` code

Citation: (raw/javascriptallonge.pdf p.179-180)

```javascript
K(I)(6)(7) //=> 7 K(I)(12)(24) //=> 24
```

### `technical-atom-2917e835cafb48fd` code

Citation: (raw/javascriptallonge.pdf p.179-180)

```javascript
K("primus")("secundus") //=> "primus" K(I)("primus")("secundus") //=> "secundus"
```

### `technical-atom-cb9e0dc41a61c284` code

Citation: (raw/javascriptallonge.pdf p.179-180)

```javascript
const first = K, second = K(I); first("primus")("secundus") //=> "primus" second("primus")("secundus") //=> "secundus"
```

### `technical-atom-7623fe166844150a` requirement

Citation: (raw/javascriptallonge.pdf p.179-180)

A constant function is a function that always returns the same thing, no matter what you give it.

### `technical-atom-3f938f381ee52883` worked-example

Citation: (raw/javascriptallonge.pdf p.179-180)

For example, (x) => 42 is a constant function that always evaluates to 42.
