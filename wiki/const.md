---
category: concept
summary: JavaScript's block-scoped variable declaration that prevents reassignment but allows shadowing in nested blocks.
sources: raw/javascriptallonge.pdf p.49-61
updated: 2026-06-12
---

The `const` keyword in JavaScript binds values to names within the lexical scope of a block. Unlike function parameters, `const` variables cannot be rebound (reassigned) after initialization, but they can shadow outer bindings in nested blocks. This provides clearer scoping rules compared to function-based IIFEs.

Key characteristics:
- Block-scoped (not function-scoped)
- Prevents reassignment (but allows shadowing)
- Useful for binding constants like π in localized scopes

Example:
```js
(diameter) => { const PI = 3.14159265; return diameter * PI }
```

See [[javascriptallonge-chapter-5]] for detailed examples and comparisons with IIFEs.
