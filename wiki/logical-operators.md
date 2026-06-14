---
category: concept
summary: JavaScript's logical operators (!, &&, ||) that operate on truthiness rather than strict booleans.
sources: raw/javascriptallonge.pdf
updated: 2026-06-13
---

JavaScript's logical operators (`!`, `&&`, `||`) operate on truthiness rather than strict booleans. These operators are used for control flow and boolean expressions.

- `!` (not): Negates truthiness.
- `&&` (and): Returns the first falsy value or the last value if all are truthy.
- `||` (or): Returns the first truthy value or the last value if all are falsy.

Short-circuit evaluation prevents unnecessary computations. For example:

- `null && undefined` → `null`
- `1 || 2` → `1`

See [[javascriptallonge-picking-the-bean-choice-and-truthiness]] for more details.

JavaScript's logical operators `!`, `&&`, and `||` evaluate based on **truthiness**, not strict boolean values. Key behaviors:

- `!` returns `true` if the argument is falsy, `false` otherwise. Example: `!5` → `false`.
- `&&` returns the left operand if falsy, otherwise the right operand. Example: `null && undefined` → `null`.
- `||` returns the left operand if truthy, otherwise the right operand. Example: `1 || 2` → `1`.

These operators **short-circuit**: `a && b` skips evaluating `b` if `a` is falsy. This is critical for control flow, e.g., `isAuthorized() ? deleteRecord() : 'Forbidden'`.

**Sources**: [[javascriptallonge-picking-the-bean-choice-and-truthiness]]
