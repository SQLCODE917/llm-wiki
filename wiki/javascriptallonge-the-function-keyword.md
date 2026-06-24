---
page_id: javascriptallonge-the-function-keyword
page_kind: source
summary: the function keyword from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.74-75
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section discusses the function keyword and its associated 'magic' names, particularly 'arguments'.

## Key supported claims

- The function keyword creates functions with 'magic' names like this and arguments (raw/javascriptallonge.pdf p.74-75).
- The arguments object contains all arguments passed to a function, regardless of declaration (raw/javascriptallonge.pdf p.74-75).
- The arguments object looks like an array but is actually an object with integer keys (raw/javascriptallonge.pdf p.74-75).
- The arguments object has a length property indicating how many arguments were passed (raw/javascriptallonge.pdf p.74-75).
- The arguments binding is commonly used for functions that accept variable arguments (raw/javascriptallonge.pdf p.74-75).

## Technical details

### `technical-atom-60318a8d1d1dc1e6` code

Citation: (raw/javascriptallonge.pdf p.74-75)

```javascript
(str) => str + str
```

### `technical-atom-43be6e04d58a2398` code

Citation: (raw/javascriptallonge.pdf p.74-75)

```javascript
function (str) { return str + str }
```

### `technical-atom-4f45e6a6ad3e7426` code

Citation: (raw/javascriptallonge.pdf p.74-75)

```javascript
(n) => (1.618**n - -1.618**-n) / 2.236
```

### `technical-atom-9b2e7b5be612a8dd` code

Citation: (raw/javascriptallonge.pdf p.74-75)

```javascript
function (n) { return (1.618**n - -1.618**-n) / 2.236; }
```

### `technical-atom-e3ae7448df2db828` code

Citation: (raw/javascriptallonge.pdf p.74-75)

```javascript
const repeat = function repeat (str) { return str + str; }; const fib = function fib (n) { return (1.618**n - -1.618**-n) / 2.236; };
```

### `technical-atom-8aacb0eaceffe66c` code

Citation: (raw/javascriptallonge.pdf p.74-75)

```javascript
const double = function repeat (str) { return str + str; }
```

### `technical-atom-45332f81dcf151e1` code

Citation: (raw/javascriptallonge.pdf p.74-75)

```javascript
double .name //=> 'repeat'
```

### `technical-atom-a0be480414fb4de1` code

Citation: (raw/javascriptallonge.pdf p.74-75)

```javascript
someBackboneView.on('click', function clickHandler () { //... });
```

## Related technical details

### From [[javascriptallonge-rebinding]]: `technical-atom-7c21d7d7a5e7d689` exception

Relation: nearby source page; matched terms `binding`, `bound`, `but`, `function`, `name`

Citation: (raw/javascriptallonge.pdf p.60-61)

We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope.

### From [[javascriptallonge-function-declarations]]: `technical-atom-824639bdc70ea377` exception

Relation: nearby source page; matched terms `declaration`, `function`, `like`, `looks`

Citation: (raw/javascriptallonge.pdf p.65-66)

It's called a function declaration statement , and it looks a lot like a named function expression, only we use it as a statement:

### From [[javascriptallonge-naming-functions]]: `technical-atom-948ee531147ee69c` formula

Relation: nearby source page; matched terms `function`, `functions`, `name`

Citation: (raw/javascriptallonge.pdf p.62)

It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 .

### From [[javascriptallonge-function-declaration-caveats-34]]: `technical-atom-4140475af23ddd75` code

Relation: nearby source page; matched terms `declaration`, `function`, `variable`

Citation: (raw/javascriptallonge.pdf p.66-67)

```javascript
( function (camelCase) { return fizzbuzz(); if (camelCase) { function fizzbuzz () { return "Fizz" + "Buzz"; } } else { function fizzbuzz () { return "Fizz" + "Buzz"; } } })( true ) //=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?
```
