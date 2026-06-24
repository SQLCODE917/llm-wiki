---
page_id: javascriptallonge-function-decorators
page_kind: source
summary: function decorators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.69-70
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Function decorators are higher-order functions that take one function as an argument, return another function, and the returned function is a variation of the argument function.

## Key supported claims

- A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. (raw/javascriptallonge.pdf p.69-70)
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. (raw/javascriptallonge.pdf p.69-70)
- Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. (raw/javascriptallonge.pdf p.69-70)
- You'll see other function decorators in the recipes, like once and maybe. (raw/javascriptallonge.pdf p.69-70)
- This implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. (raw/javascriptallonge.pdf p.69-70)

## Technical details

### `technical-atom-abf406fcb9db5ce1` code

Citation: (raw/javascriptallonge.pdf p.69-70)

```javascript
const not = (fn) => (x) => !fn(x)
```

### `technical-atom-e9d511db5f47e977` code

Citation: (raw/javascriptallonge.pdf p.69-70)

```javascript
const something = (x) => x != null ;
```

### `technical-atom-ee945f387e56d8e2` code

Citation: (raw/javascriptallonge.pdf p.69-70)

```javascript
const nothing = (x) => !something(x);
```

### `technical-atom-1f262d158639ac24` code

Citation: (raw/javascriptallonge.pdf p.69-70)

```javascript
const nothing = not(something);
```

## Related technical details

### From [[javascriptallonge-unary]]: `technical-atom-898e42c84ba44bb3` procedure

Relation: nearby source page; matched terms `argument`, `decorator`, `function`, `modifies`, `one`, `takes`

Citation: (raw/javascriptallonge.pdf p.82-83)

'Unary' is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

### From [[javascriptallonge-combinators]]: `technical-atom-0c6ee2e3b1a2e9c0` exception

Relation: nearby source page; matched terms `combinator`, `combinators`, `function`, `functions`, `higher-order`, `pure`

Citation: (raw/javascriptallonge.pdf p.68-69)

In this book, we will be using a looser definition of 'combinator:' Higher-order pure functions that take only functions as arguments and return a function.

### From [[javascriptallonge-combinators]]: `technical-atom-573c28eb9a1b4a43` exception

Relation: nearby source page; matched terms `combinator`, `combinators`, `function`, `higher-order`

Citation: (raw/javascriptallonge.pdf p.68-69)

'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35

### From [[javascriptallonge-function-declaration-caveats-34]]: `technical-atom-68210eea018a360c` code

Relation: nearby source page; matched terms `but`, `function`, `not`, `return`

Citation: (raw/javascriptallonge.pdf p.66-67)

```javascript
function trueDat () { return true } But this is not: ( function trueDat () { return true })
```
