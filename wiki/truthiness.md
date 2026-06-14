---
category: concept
summary: JavaScript's truthiness determines behavior of logical operators and conditionals, with falsy values including false, null, undefined, NaN, 0, and empty string.
sources: javascriptallonge-picking-the-bean-choice-and-truthiness
updated: 2026-06-11
---

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
