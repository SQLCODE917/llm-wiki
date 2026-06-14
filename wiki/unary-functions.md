---
category: concept
summary: Unary functions in JavaScript, which accept exactly one argument, enforced via decorators.
sources: raw/javascriptallonge.pdf
updated: 2026-06-13
---

Unary functions in JavaScript are functions that accept exactly one argument. They are often enforced via decorators to ensure strict argument handling.

Example:
```javascript
const unary = (fn) => fn.length === 1 ? fn : something => fn.call(this, something);
```

See [[javascriptallonge-recipes-with-basic-functions]] for more details.

A unary function is one that accepts exactly one argument. In JavaScript, this can be enforced via a decorator to ensure that functions are used with only one argument, regardless of how many are passed.

```javascript
const unary = (fn) => fn.length === 1 ? fn : something => fn.call(this, something);
```

This is useful in functional programming to prevent accidental multiple arguments from causing issues.

See [[javascriptallonge-recipes-with-basic-functions]] for more details.

The `unary` decorator ensures a function only accepts one argument, preventing unexpected behavior from JavaScript's `.map` method which provides three arguments (element, index, array). Example:

```javascript
const unary = (fn) => fn.length === 1 ? fn : something => fn.call(this, something);

['1','2','3'].map(unary(parseInt)) //=> [1,2,3]
```

This fixes issues like `parseInt` misinterpreting array indexes as radix parameters. See [[javascriptallonge-recipes-with-basic-functions]] (raw/javascriptallonge.pdf p.79-93).
