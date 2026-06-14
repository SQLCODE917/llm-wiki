---
category: source
summary: JavaScript's truthiness, logical operators (!, &&, ||), ternary operator, and control-flow semantics explained with examples.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

## Picking the Bean: Choice and Truthiness

JavaScript treats values as truthy or falsy, not just boolean. Falsy values include `false`, `null`, `undefined`, `NaN`, `0`, and `''`. Logical operators (!, &&, ||) operate on truthiness, not strict booleans. The ternary operator (`? :`) is a control-flow expression. Examples:

- `!5` → `false`
- `null && undefined` → `null`
- `1 || 2` → `1`
- `||` and `&&` short-circuit evaluation prevents unnecessary computations.

**Sources**: [raw/javascriptallonge.pdf p.94-108]
