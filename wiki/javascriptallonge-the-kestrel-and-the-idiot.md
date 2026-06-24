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

## Related technical details

### From [[javascriptallonge-the-vireo]]: `technical-atom-fc35774e3ffe2b16` procedure

Relation: nearby source page; matched terms `function`, `given`, `makes`

Citation: (raw/javascriptallonge.pdf p.182-183)

Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data.

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-cf5b15724c23cd8a` procedure

Relation: nearby source page; matched terms `combinators`, `functions`, `kestrel`

Citation: (raw/javascriptallonge.pdf p.177-179)

To Mock a Mockingbird 76 established the metaphor of songbirds for the combinators, and ever since then logicians have called the K combinator a 'kestrel,' the B combinator a 'bluebird,' and so forth.

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-5b37e3daf21d3949` worked-example

Relation: nearby source page; matched terms `function`, `functions`, `values`

Citation: (raw/javascriptallonge.pdf p.177-179)

For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

### From [[javascriptallonge-lists-with-functions-as-data]]: `technical-atom-1facdd66430f4b84` code

Relation: nearby source page; matched terms `can`, `first`, `functions`

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
const length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair)); length(l123) //=> 3 const reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(rest(aPair), pair(first(aPair), delayed)); const mapWith = (fn, aPair, delayed = EMPTY) => aPair === EMPTY ? reverse(delayed) : mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed)); const doubled = mapWith((x) => x * 2, l123); first(doubled) //=> 2 first(rest(doubled)) //=> 4 first(rest(rest(doubled))) //=> 6 Can we do the same with the linked lists we build out of functions? Yes: const first = K, l123 = pair(1)(pair(2)(pair(3)(EMPTY)));
```
