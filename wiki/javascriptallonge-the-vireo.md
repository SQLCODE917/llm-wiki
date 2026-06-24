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

### `technical-atom-ce93cc515740ca77` code

Citation: (raw/javascriptallonge.pdf p.182-183)

```
For objects we'd write: cons = (first, second) => {first, second} .
```

### `technical-atom-fc35774e3ffe2b16` procedure

Citation: (raw/javascriptallonge.pdf p.182-183)

Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data.

### `technical-atom-d78941c9cf360b77` procedure

Citation: (raw/javascriptallonge.pdf p.182-183)

For arrays, we'd write cons = (first, second) => [first, second] .

### `technical-atom-aa39093329fa518f` worked-example

Citation: (raw/javascriptallonge.pdf p.182-183)

One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function.

## Related technical details

### From [[javascriptallonge-a-return-to-backward-thinking]]: `technical-atom-e2b2c0d8e3d358fe` requirement

Relation: nearby source page; matched terms `data`, `functions`, `structures`, `them`

Citation: (raw/javascriptallonge.pdf p.189-190)

It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both.

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-5b37e3daf21d3949` worked-example

Relation: nearby source page; matched terms `data`, `example`, `function`, `functions`, `values`, `worked-example`

Citation: (raw/javascriptallonge.pdf p.177-179)

For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

### From [[javascriptallonge-lists-with-functions-as-data]]: `technical-atom-21a61344f2e84d80` code

Relation: nearby source page; matched terms `data`, `functions`, `them`

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
//=> 2 return l123(rest)(rest)(first) //=> 3 We write them in a backwards way, but they seem to work. How about
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-cf5b15724c23cd8a` procedure

Relation: nearby source page; matched terms `combinator`, `combinators`, `data`, `functions`

Citation: (raw/javascriptallonge.pdf p.177-179)

To Mock a Mockingbird 76 established the metaphor of songbirds for the combinators, and ever since then logicians have called the K combinator a 'kestrel,' the B combinator a 'bluebird,' and so forth.
