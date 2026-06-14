---
category: concept
summary: JavaScript functions that accept a variable number of arguments, with the first argument fixed and the rest collected in an array.
sources: raw/javascriptallonge.pdf
updated: 2026-06-13
---

JavaScript functions that accept a variable number of arguments, with the first argument fixed and the rest collected in an array. This pattern is used in functional programming to create flexible function signatures.

See [[javascriptallonge-recipes-with-basic-functions]] for more details.

Left-variadic functions are functions that take a fixed number of leading arguments and collect the rest in an array. This allows for flexible function signatures where the first few arguments are fixed, and the rest are passed in later.

Example:
```javascript
const callLeft = (fn, ...args) => (...rest) => fn.call(this, ...args, ...rest);
```

This is useful for creating partial application patterns where the first arguments are fixed and the rest are passed in later.

See [[javascriptallonge-recipes-with-basic-functions]] for more details.

In functional programming, **left-variadic functions** are functions that can accept a variable number of arguments, typically on the left side of the function call. This allows for flexible function definitions and is discussed in *JavaScript Allongé* (raw/javascriptallonge.pdf p.305-320).
