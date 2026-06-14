---
category: concept
summary: JavaScript's logical operators (!, &&, ||) operate on truthiness, not strict booleans, with short-circuit evaluation.
sources: javascriptallonge-picking-the-bean-choice-and-truthiness
updated: 2026-06-11
---

JavaScript's logical operators `!`, `&&`, and `||` evaluate based on **truthiness**, not strict boolean values. Key behaviors:

- `!` returns `true` if the argument is falsy, `false` otherwise. Example: `!5` → `false`.
- `&&` returns the left operand if falsy, otherwise the right operand. Example: `null && undefined` → `null`.
- `||` returns the left operand if truthy, otherwise the right operand. Example: `1 || 2` → `1`.

These operators **short-circuit**: `a && b` skips evaluating `b` if `a` is falsy. This is critical for control flow, e.g., `isAuthorized() ? deleteRecord() : 'Forbidden'`.

**Sources**: [[javascriptallonge-picking-the-bean-choice-and-truthiness]]
