---
category: concept
summary: JavaScript's truthiness and falsiness, where values are evaluated as true or false in boolean contexts.
sources: raw/javascriptallonge.pdf
updated: 2026-06-13
---

JavaScript's truthiness and falsiness refer to how values are evaluated in boolean contexts. Falsy values include `false`, `null`, `undefined`, `NaN`, `0`, and `''`. All other values are truthy. This behavior is fundamental to control flow and logical operations in JavaScript.

- `!5` → `false`
- `null && undefined` → `null`
- `1 || 2` → `1`

See [[javascriptallonge-picking-the-bean-choice-and-truthiness]] for more details.

In JavaScript, every value is either **truthy** or **falsy**. Falsy values include:

- `false`
- `null`
- `undefined`
- `NaN`
- `0`
- `''` (empty string)

All other values are truthy. This affects logical operators (`!`, `&&`, `||`), the ternary operator (`? :`), and `if` statements, which operate on truthiness rather than strict boolean values. For example:

```javascript
!5 // => false
!!'hello' // => true
```

**Sources**: [[javascriptallonge-picking-the-bean-choice-and-truthiness]]
