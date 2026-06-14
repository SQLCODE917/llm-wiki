---
category: concept
summary: Higher-order functions that modify or wrap another function's behavior.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

A **function decorator** is a higher-order function that takes a function as input and returns a modified version of it. For example:

```javascript
const not = (fn) => (x) => !fn(x);
```
This decorator transforms a predicate function into its negation. Decorators can add behavior like caching, validation, or error handling while preserving the original function's interface.

See (raw/javascriptallonge.pdf p.62-78) for examples like `not` and `maybe`.
