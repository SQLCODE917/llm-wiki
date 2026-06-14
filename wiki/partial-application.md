---
category: concept
summary: Function technique to fix arguments in JavaScript
sources: javascriptallonge.pdf
updated: 2026-06-11
---

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
