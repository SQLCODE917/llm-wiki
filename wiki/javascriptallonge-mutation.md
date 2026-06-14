---
category: source
summary: JavaScript mutation mechanics: array/object mutation, aliases, const/let reassignment, and var pitfalls (pages 141-157).
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

This chapter explains JavaScript's mutation model:

- Arrays and objects can mutate via element reassignment (e.g., `arr[0] = 'new'`)
- `const` prevents rebinding but allows mutation of referenced values
- Aliases share the same value identity, so mutation affects all aliases
- `let` allows reassignment within block scope
- `var` has function scope and hoisting quirks
- Destructuring creates copies (unlike linked list structure sharing)
- Mutation patterns in linked lists vs arrays
- The `reverse` algorithm for linked list copying
- `mapWith` function implementation using mutation
- `var` vs `let` in for-loop closure scenarios

Cite: (raw/javascriptallonge.pdf p.141-157)
