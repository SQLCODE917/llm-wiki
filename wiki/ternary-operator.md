---
category: concept
summary: JavaScript's ternary operator (?) is a control-flow expression that evaluates a condition and returns one of two values.
sources: javascriptallonge-picking-the-bean-choice-and-truthiness
updated: 2026-06-11
---

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
