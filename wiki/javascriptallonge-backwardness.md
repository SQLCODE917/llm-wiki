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

## Related technical details

### From [[javascriptallonge-a-return-to-backward-thinking]]: `technical-atom-e2b2c0d8e3d358fe` requirement

Relation: nearby source page; matched terms `both`, `data`, `functions`, `return`, `structures`, `them`

Citation: (raw/javascriptallonge.pdf p.189-190)

It is a tenet of Object-Oriented Programming, but it is not exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both.

### From [[javascriptallonge-lists-with-functions-as-data]]: `technical-atom-21a61344f2e84d80` code

Relation: nearby source page; matched terms `about`, `data`, `first`, `functions`, `how`, `return`

Citation: (raw/javascriptallonge.pdf p.183-186)

```javascript
//=> 2 return l123(rest)(rest)(first) //=> 3 We write them in a backwards way, but they seem to work. How about
```

### From [[javascriptallonge-the-vireo]]: `technical-atom-fc35774e3ffe2b16` procedure

Relation: nearby source page; matched terms `data`, `function`, `our`, `represented`

Citation: (raw/javascriptallonge.pdf p.182-183)

Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data.

### From [[javascriptallonge-the-kestrel-and-the-idiot]]: `technical-atom-cb9e0dc41a61c284` code

Relation: nearby source page; matched terms `first`, `second`

Citation: (raw/javascriptallonge.pdf p.179-180)

```javascript
const first = K, second = K(I); first("primus")("secundus") //=> "primus" second("primus")("secundus") //=> "secundus"
```
