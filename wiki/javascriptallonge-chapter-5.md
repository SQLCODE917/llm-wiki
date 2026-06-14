---
category: source
summary: Explains JavaScript's const keyword, lexical scoping, and function binding patterns like IIFEs.
sources: raw/javascriptallonge.pdf p.49-61
updated: 2026-06-12
---

## That Constant Coffee Craving

This chapter explores JavaScript's approach to naming values, focusing on the `const` keyword and lexical scoping. Key concepts include:

- Using IIFEs (Immediately Invoked Function Expressions) to bind values to names
- The `const` keyword for block-scoped variable binding
- Lexical scoping rules for closures and shadowing
- Comparing function parameters vs. `const` for value binding
- How `const` prevents reassignment but allows shadowing in nested blocks

Example: Binding π to a name:
```js
(diameter) => { const PI = 3.14159265; return diameter * PI }
```

The chapter demonstrates that `const` provides cleaner syntax than IIFEs for binding values while maintaining lexical scoping rules. It also explains how `const` variables shadow outer bindings in nested blocks but do not overwrite them.

See [[const]] for const semantics and [[lexical-scoping]] for scoping rules.
