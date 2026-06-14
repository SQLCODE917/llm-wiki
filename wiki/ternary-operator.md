---
category: concept
summary: JavaScript's ternary operator (? :) as a control-flow expression for conditional assignments.
sources: raw/javascriptallonge.pdf
updated: 2026-06-13
---

JavaScript's ternary operator (`? :`) is a control-flow expression for conditional assignments. It evaluates a condition and returns one of two values based on the result.

Syntax: `condition ? value1 : value2`

For example:
```javascript
isAuthorized() ? deleteRecord() : 'Forbidden'
```

This operator is often used for concise conditional logic and is short-circuiting.

See [[javascriptallonge-picking-the-bean-choice-and-truthiness]] for more details.

The **ternary operator** (`? :`) is JavaScript's only ternary operator, acting as a concise `if` statement. It evaluates a condition and returns one of two expressions:

```javascript
condition ? trueCase : falseCase
```

Example:
```javascript
const status = isAuthorized() ? deleteRecord() : 'Forbidden';
```

Only **one** of `trueCase` or `falseCase` is evaluated, making it useful for conditional assignments without bloating code with `if` blocks. This is critical for avoiding unnecessary computations, e.g., `deleteRecord()` is only called if `isAuthorized()` returns `true`.

**Sources**: [[javascriptallonge-picking-the-bean-choice-and-truthiness]]
