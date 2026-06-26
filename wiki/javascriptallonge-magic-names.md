---
page_id: javascriptallonge-magic-names
page_kind: source
summary: Magic Names from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.74-77
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

The Magic Names chapter from JavaScript Allongé discusses the 'arguments' magic name and how it behaves differently for functions defined with the function keyword versus fat arrow functions.

## Key supported claims

- JavaScript binds argument values to magic names in addition to declared argument names (raw/javascriptallonge.pdf p.74-77).
- The 'arguments' magic name contains all passed arguments regardless of declared parameters (raw/javascriptallonge.pdf p.74-77).
- Fat arrow functions inherit 'arguments' from their enclosing scope, unlike regular functions (raw/javascriptallonge.pdf p.74-77).
- Do not define custom bindings for magic names like 'arguments' (raw/javascriptallonge.pdf p.74-77).

## Technical details

### `technical-atom-1ebee9894eea982f` code

Citation: (raw/javascriptallonge.pdf p.74-77)

```javascript
const plus = function (a, b) { return arguments[0] + arguments[1]; } plus(2,3) //=> 5
```

### `technical-atom-fe9a500a6aa863d4` code

Citation: (raw/javascriptallonge.pdf p.74-77)

```javascript
const args = function (a, b) { return arguments; } args(2,3) //=> { '0': 2, '1': 3 }
```

### `technical-atom-b37e567e18ab7194` code

Citation: (raw/javascriptallonge.pdf p.74-77)

```javascript
const plus = function () { return arguments[0] + arguments[1]; } plus(2,3) //=> 5
```

### `technical-atom-bfde6aeec1103aaf` code

Citation: (raw/javascriptallonge.pdf p.74-77)

```javascript
const howMany = function () { return arguments['length']; } howMany() //=> 0 howMany('hello') //=> 1 howMany('sharks', 'are', 'apex', 'predators') //=> 4
```

### `technical-atom-83c066e41153e7e2` code

Citation: (raw/javascriptallonge.pdf p.74-77)

```javascript
( function () { return ( function () { return arguments[0]; })('inner'); })('outer') //=> "inner"
```

### `technical-atom-1569c989e16c27c6` code

Citation: (raw/javascriptallonge.pdf p.74-77)

```javascript
( function () { return (() => arguments[0])('inner'); })('outer') //=> "outer"
```

### `technical-atom-d4cccaa229fb10dc` code

Citation: (raw/javascriptallonge.pdf p.74-77)

```javascript
const row = function () { return mapWith( (column) => column * arguments[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) } row(3) //=> [3,6,9,12,15,18,21,24,27,30,33,36]
```

### `technical-atom-619c03466d625e82` code

Citation: (raw/javascriptallonge.pdf p.74-77)

```javascript
This works just fine, because arguments[0] refers to the 3 we passed to the function row. Our “fat arrow” function (column) => column * arguments[0] doesn’t bind arguments when it’s invoked. But if we rewrite row to use the function keyword, it stops working:
```

## Related technical details

### From [[javascriptallonge-unary]]: `technical-atom-2fb846e09e5cacfd` procedure

Relation: nearby source page; matched terms `argument`, `arguments`, `function`

Citation: (raw/javascriptallonge.pdf p.82-83)

“Unary” is a function decorator that modifies the number of arguments a function takes: Unary takes any function and turns it into a function taking exactly one argument.

### From [[javascriptallonge-combinators-and-function-decorators]]: `technical-atom-4ec0e2f5cfc99090` code

Relation: nearby source page; matched terms `arguments`, `function`, `functions`, `javascript`, `values`

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
As we’ve seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function.
```

### From [[javascriptallonge-building-blocks]]: `technical-atom-cc7f0e20542b4dff` code

Relation: nearby source page; matched terms `argument`, `function`, `second`

Citation: (raw/javascriptallonge.pdf p.71-73)

```javascript
This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:
```

### From [[javascriptallonge-partial-application]]: `technical-atom-a57295fce728475d` code

Relation: nearby source page; matched terms `function`, `name`, `you`

Citation: (raw/javascriptallonge.pdf p.80-81)

```javascript
const callFirst = (fn, larg) => function (...rest) { return fn.call( this, larg, ...rest); } const callLast = (fn, rarg) => function (...rest) { return fn.call( this, ...rest, rarg); } const greet = (me, you) => `Hello, ${ you }, my name is ${ me } `;
```
