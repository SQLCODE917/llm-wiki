---
page_id: javascriptallonge-flip
page_kind: source
summary: Flip from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.195-197
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on flip functions and currying in JavaScript Allongé, covering argument reversal and function composition techniques.

## Key supported claims

- Flip reverses argument order in functions (raw/javascriptallonge.pdf p.195-197).
- Currying combines with flip for cleaner function definitions (raw/javascriptallonge.pdf p.195-197).
- Flip handles context differently for methods (raw/javascriptallonge.pdf p.195-197).
- Flip function takes arguments in reverse order (raw/javascriptallonge.pdf p.195-197).
- Flip returns function with reversed argument order (raw/javascriptallonge.pdf p.195-197).

## Technical details

### `technical-atom-0eed0753a9a51c63` code

Citation: (raw/javascriptallonge.pdf p.195-197)

```javascript
const mapWith = (fn) => (list) => list.map(fn);
```

### `technical-atom-8864be63f0d1287a` code

Citation: (raw/javascriptallonge.pdf p.195-197)

```javascript
const mapWith = (fn) => (list) => map(list, fn);
```

### `technical-atom-643f0654f0843207` code

Citation: (raw/javascriptallonge.pdf p.195-197)

```javascript
const mapWith = (fn, list) => map(list, fn);
```

### `technical-atom-6f1a6d8af8f7a336` code

Citation: (raw/javascriptallonge.pdf p.195-197)

```javascript
const mapper = (list) => (fn) => map(list, fn);
```

### `technical-atom-5e12113b4bab5f1d` code

Citation: (raw/javascriptallonge.pdf p.195-197)

```javascript
Let’s return to the implementation of mapWith that relies on a map function rather than a method:
```

### `technical-atom-46f8909fd16287cb` code

Citation: (raw/javascriptallonge.pdf p.195-197)

```javascript
const mapWith = (first) => (second) => map(second, first);
```

### `technical-atom-132c6369b0c4a80c` code

Citation: (raw/javascriptallonge.pdf p.195-197)

```javascript
const wrapper = (fn) =>
```

### `technical-atom-b39bbfbb10f500bf` code

Citation: (raw/javascriptallonge.pdf p.195-197)

```javascript
(first) => (second) => fn(second, first);
```

## Related technical details

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-cd36d849b171aa54` code

Relation: nearby source page; matched terms `function`, `functions`, `identity`, `now`, `pass`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42. Very simple, but useful. Now we’ll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value.
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-aea76708de48efca` code

Relation: nearby source page; matched terms `function`, `functions`, `returns`, `what`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K, is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value.
```

### From [[javascriptallonge-mapwith]]: `technical-atom-b81c568b25c3fe2e` procedure

Relation: nearby source page; matched terms `argument`, `function`, `mapwith`, `procedure`, `returns`, `takes`

Citation: (raw/javascriptallonge.pdf p.193-194)

Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array.

### From [[javascriptallonge-why]]: `technical-atom-1131be1317bdb5fe` code

Relation: nearby source page; matched terms `function`, `return`

Citation: (raw/javascriptallonge.pdf p.201)

```javascript
const factorial = Y( function (fac) { return function (n) { return (n == 0 ? 1: n * fac(n - 1)); } }); factorial(5) //=> 120
```
