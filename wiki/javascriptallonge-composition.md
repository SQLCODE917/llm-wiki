---
page_id: javascriptallonge-composition
page_kind: source
summary: composition from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.71-71
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This chapter covers function composition in JavaScript, including the use of the compose function and decorators like once and maybe.

## Key supported claims

- Function composition chains functions together, as in `const cookAndEat = (food) => eat(cook(food));` (raw/javascriptallonge.pdf p.71-71).
- The compose function generalizes composition: `const compose = (a, b) => (c) => a(b(c));` (raw/javascriptallonge.pdf p.71-71).
- Decorators like once ensure functions execute only once, and maybe ensures functions do nothing when given null or undefined (raw/javascriptallonge.pdf p.71-71).
- Functions can be composed in various ways for flexible code organization (raw/javascriptallonge.pdf p.71-71).

## Technical details

### `technical-atom-797143f76a99b37b` code

Citation: (raw/javascriptallonge.pdf p.71)

```javascript
const cookAndEat = (food) => eat(cook(food));
```

### `technical-atom-5a14afdbf0af7bbe` code

Citation: (raw/javascriptallonge.pdf p.71)

```javascript
const compose = (a, b) => (c) => a(b(c)); const cookAndEat = compose(eat, cook);
```

### `technical-atom-5943f50d596a5207` code

Citation: (raw/javascriptallonge.pdf p.71)

```javascript
const actuallyTransfer= (from, to, amount) => // do something const invokeTransfer = once(maybe(actuallyTransfer(...)));
```

### `technical-atom-1485abab22045392` exception

Citation: (raw/javascriptallonge.pdf p.71)

But like many patterns, using it when it applies is only 20% of the benefit.

### `technical-atom-21b43dcc13c31c32` exception

Citation: (raw/javascriptallonge.pdf p.71)

In the recipes, we'll look at a decorator called once: It ensures that a function can only be executed once.
