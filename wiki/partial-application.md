---
category: concept
summary: Partial application in JavaScript, where a function is called with fewer arguments than it expects, returning a new function.
sources: raw/javascriptallonge.pdf
updated: 2026-06-13
---

Partial application in JavaScript involves calling a function with fewer arguments than it expects, returning a new function that accepts the remaining arguments. This is a functional programming technique used to create specialized functions from general ones.

Example:
```javascript
const callFirst = (fn, larg) => (...rest) => fn.call(this, larg, ...rest);
```

See [[javascriptallonge-recipes-with-basic-functions]] for more details.

Partial application is a functional programming technique where a function is called with fewer arguments than it requires, producing a new function with the remaining arguments pre-filled. This allows for creating specialized versions of generic functions.

In JavaScript, partial application can be implemented using closures:

```javascript
const add = (a, b) => a + b;
const addFive = add.bind(null, 5); // Partially apply 'a' to 5
addFive(3); // Returns 8
```

See [[javascriptallonge-recipes-with-basic-functions]] for more details.

Partial application is a functional programming pattern where a function is called with fewer arguments than it requires, producing a new function with the remaining arguments pre-filled. JavaScript implementations include:

- `callFirst(fn, larg)` - fixes the first argument
- `callLast(fn, rarg)` - fixes the last argument
- `callLeft(fn, ...args)` - fixes multiple leading arguments
- `callRight(fn, ...args)` - fixes multiple trailing arguments

Example:
```javascript
const greet = (me, you) => `Hello, ${you}, my name is ${me}`;
const heliosSaysHello = callFirst(greet, 'Helios');
heliosSaysHello('Eartha') //=> 'Hello, Eartha, my name is Helios'
```

See [[javascriptallonge-recipes-with-basic-functions]] for implementation details (raw/javascriptallonge.pdf p.79-93).
