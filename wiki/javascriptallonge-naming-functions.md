---
page_id: javascriptallonge-naming-functions
page_kind: source
summary: Naming Functions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.62-67
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter from JavaScript Allongé explores the nuances of naming functions in JavaScript, covering anonymous functions, named function expressions, and function declarations.

## Key supported claims

- Arrow syntax creates anonymous functions, not named (raw/javascriptallonge.pdf p.62-67).
- Function keyword allows naming functions, unlike arrow syntax (raw/javascriptallonge.pdf p.62-67).
- Named function expressions bind function name to function, not environment (raw/javascriptallonge.pdf p.62-67).
- Function declarations are hoisted to top of scope, allowing use before definition (raw/javascriptallonge.pdf p.62-67).
- Function declarations must not be inside blocks or expressions (raw/javascriptallonge.pdf p.62-67).

## Technical details

### `technical-atom-5b2db9564ba1d141` code

Citation: (raw/javascriptallonge.pdf p.62-67)

```javascript
const repeat = (str) => str + str
```

### `technical-atom-c3c551ab08b38d6b` code

Citation: (raw/javascriptallonge.pdf p.62-67)

```javascript
(str) => str + str
```

### `technical-atom-5a7c2c2feec03b0b` code

Citation: (raw/javascriptallonge.pdf p.62-67)

```javascript
function (str) { return str + str }
```

### `technical-atom-e6e76a5e6be15c59` code

Citation: (raw/javascriptallonge.pdf p.62-67)

```javascript
5. We always use a block, we cannot write function (str) str + str. This means that if we want our functions to return a value, we always need to use the return keyword
```

### `technical-atom-66f799107dabedfc` code

Citation: (raw/javascriptallonge.pdf p.62-67)

```javascript
(n) => (1.618**n - -1.618**-n) / 2.236
```

### `technical-atom-3e1227a361ce7588` code

Citation: (raw/javascriptallonge.pdf p.62-67)

```javascript
function (n) { return (1.618**n - -1.618**-n) / 2.236; }
```

### `technical-atom-73332c6ee25e1ad8` code

Citation: (raw/javascriptallonge.pdf p.62-67)

```javascript
const repeat = function repeat (str) { return str + str; }; const fib = function fib (n) { return (1.618**n - -1.618**-n) / 2.236; };
```

### `technical-atom-4dd2787bad88c9c5` code

Citation: (raw/javascriptallonge.pdf p.62-67)

```javascript
const double = function repeat (str) { return str + str; }
```

## Related technical details

### From [[javascriptallonge-magic-names]]: `technical-atom-619c03466d625e82` code

Relation: nearby source page; matched terms `arrow`, `bind`, `function`, `keyword`, `our`, `use`

Citation: (raw/javascriptallonge.pdf p.74-77)

```javascript
This works just fine, because arguments[0] refers to the 3 we passed to the function row. Our “fat arrow” function (column) => column * arguments[0] doesn’t bind arguments when it’s invoked. But if we rewrite row to use the function keyword, it stops working:
```

### From [[javascriptallonge-closures-and-scope]]: `technical-atom-58f9184c287b83f5` code

Relation: nearby source page; matched terms `bind`, `function`, `name`, `named`, `not`, `scope`

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
The function (y) => x is interesting. It contains a free variable, x.[27] A free variable is one that is not bound within the function. Up to now, we’ve only seen one way to “bind” a variable, namely by passing in an argument with the same name. Since the function (y) => x doesn’t have an argument named x, the variable x isn’t bound in this function, which makes it “free.”
```

### From [[javascriptallonge-ah-i-d-like-to-have-an-argument-please]]: `technical-atom-07b4f982763531cb` code

Relation: nearby source page; matched terms `expressions`, `function`, `functions`

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
Expressions consist either of representations of values (like 3.14159265, true, and undefined), operators that combine expressions (like 3 + 2), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( arguments) { body-statements } for creating functions.
```

### From [[javascriptallonge-that-constant-coffee-craving]]: `technical-atom-e75668d22e5ff80b` code

Relation: nearby source page; matched terms `expressions`, `function`, `functions`, `our`, `use`

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our “functions” are expressions. This one has a few more moving parts, that’s all. But we can use it just like (diameter) => diameter * 3.14159265.
```
