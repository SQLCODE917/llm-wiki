---
category: concept
summary: JavaScript's mechanism for resolving variable names based on their position in the source code, rather than runtime context.
sources: raw/javascriptallonge.pdf p.49-61
updated: 2026-06-11
---

Lexical scoping in JavaScript determines variable resolution by analyzing the static structure of the code. Bindings created with `const` or function parameters are looked up in the environment where they are declared, not where they are used. This enables predictable closure behavior and prevents accidental overwriting of variables.

Key aspects:
- Closures retain access to lexically scoped variables
- `const` variables shadow outer bindings in nested blocks
- Parameters bind to the environment of function invocation

Example conflict resolution:
```js
((PI) => { ((PI) => {})(); return (diameter) => diameter * PI; })(3.14159265)(2)
```

See [[javascriptallonge-chapter-5]] for detailed explanations and examples.
