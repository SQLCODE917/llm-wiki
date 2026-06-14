---
category: source
summary: JavaScript functions as values, reference types, and function application mechanics (pages 30-43).
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

This chapter explores JavaScript functions as first-class values, their identity as reference types, and mechanics of function application. Key points include:

- Functions are values but not identical when redefined: `(() => 0) === (() => 0)` evaluates to `false`.
- Function application syntax: `fn_expr(args)`.
- Return statements terminate function evaluation: `() => { return 0 }()` returns `0`.
- Blocks evaluate to `undefined` unless using `return`.
- `undefined` represents absent values, distinct from SQL `NULL`.
- `void` operator guarantees `undefined` generation (prefer `void 0`).
- Call-by-value strategy evaluates arguments before passing, with reference types sharing values (call-by-sharing).

Cite: (raw/javascriptallonge.pdf p.30-43)
