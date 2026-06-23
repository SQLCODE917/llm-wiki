---
page_id: javascriptallonge-function-parameters-are-eager
page_kind: source
summary: function parameters are eager from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.98-99
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Function parameters are always eagerly evaluated in JavaScript, unlike the ternary operator and logical operators.

## Key supported claims

- Function parameters are always eagerly evaluated in JavaScript. (raw/javascriptallonge.pdf p.98-99)
- JavaScript evaluates expressions for parameters before passing values to a function. (raw/javascriptallonge.pdf p.98-99)
- Control-flow semantics can be achieved by passing anonymous functions. (raw/javascriptallonge.pdf p.98-99)

## Technical details

### `technical-atom-5ecb59ffe5b652d2` code

Citation: (raw/javascriptallonge.pdf p.98-99)

```javascript
const or = (a, b) => a || b const and = (a, b) => a && b const even = (n) => or(n === 0, and(n !== 1, even(n - 2))) even(42) //=> Maximum call stack size exceeded.
```

### `technical-atom-a5e9f6ba003c055d` code

Citation: (raw/javascriptallonge.pdf p.98-99)

```javascript
const or = (a, b) => a() || b() const and = (a, b) => a() && b() const even = (n) => or(() => n === 0, () => and(() => n !== 1, () => even(n - 2))) even(7) //=> false
```

### `technical-atom-187fa25d1ca2e804` requirement

Citation: (raw/javascriptallonge.pdf p.98-99)

In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated :

### `technical-atom-ab2c16e0bbf23b9b` code

Citation: (raw/javascriptallonge.pdf p.98-99)

```
Nowourexpression or(n === 0, and(n !== 1, even(n - 2))) is calling functions, and JavaScript always evaluates the expressions for parameters before passing the values to a function to invoke.
```
