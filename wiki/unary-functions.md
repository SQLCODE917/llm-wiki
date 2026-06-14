---
category: concept
summary: Decorator to enforce single-argument functions in JavaScript
sources: javascriptallonge.pdf
updated: 2026-06-11
---

The `unary` decorator ensures a function only accepts one argument, preventing unexpected behavior from JavaScript's `.map` method which provides three arguments (element, index, array). Example:

```javascript
const unary = (fn) => fn.length === 1 ? fn : something => fn.call(this, something);

['1','2','3'].map(unary(parseInt)) //=> [1,2,3]
```

This fixes issues like `parseInt` misinterpreting array indexes as radix parameters. See [[javascriptallonge-recipes-with-basic-functions]] (raw/javascriptallonge.pdf p.79-93).
