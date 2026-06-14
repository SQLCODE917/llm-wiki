---
category: source
summary: JavaScript functional programming recipes: partial application, unary functions, tap, maybe, once, and left-variadic functions.
sources: javascriptallonge.pdf
updated: 2026-06-11
---

## Recipes with Basic Functions

This chapter explores practical functional programming patterns in JavaScript, including:

- **Partial Application** (callFirst, callLast, callLeft, callRight)
- **Unary** function decorator to enforce single-argument functions
- **Tap** combinator for side-effect logging
- **Maybe** monad-inspired null-checking
- **Once** combinator to restrict function execution to a single call
- **Left-variadic functions** and array destructuring patterns

Key implementations include:
```javascript
const callFirst = (fn, larg) => (...rest) => fn.call(this, larg, ...rest);
const unary = (fn) => fn.length === 1 ? fn : something => fn.call(this, something);
```

See (raw/javascriptallonge.pdf p.79-93) for full details.
