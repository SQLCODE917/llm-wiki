---
category: concept
summary: JavaScript's evaluation strategy where arguments are evaluated before passing, with reference types sharing values (call-by-sharing).
sources: raw/javascriptallonge.pdf
updated: 2026-06-12
---

JavaScript employs a **call-by-value** evaluation strategy, where function arguments are evaluated before being passed. For **value types** (primitives like numbers, strings), the value is copied into the function's environment. For **reference types** (objects, arrays), the reference (memory address) is passed, leading to **call-by-sharing** semantics: changes to the referenced object inside the function affect the original. This is a specialization of call-by-value, distinguishing JavaScript from languages with strict call-by-reference or call-by-name strategies.

Example:
```js
function modify(arr) { arr.push(4); }
let a = [1, 2, 3];
modify(a);
// a is now [1, 2, 3, 4]
```

Cite: (raw/javascriptallonge.pdf p.30-43)
