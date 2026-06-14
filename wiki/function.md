---
category: concept
summary: JavaScript functions, pure functions, closures, and declaration hoisting.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

JavaScript functions are first-class values that can be assigned to variables, passed as arguments, and returned from other functions. Key characteristics include:

- **Function declarations** are hoisted to the top of their scope, allowing them to be used before declaration.
- **Named function expressions** allow a function to have a name distinct from its binding (e.g., `const double = function repeat(...) { ... }`).
- **Combinators** like `compose` enable function composition (see [[combinator]]).
- **Decorators** like `not` modify function behavior (see [[function-decorator]]).
- **Magic names** like `this` and `arguments` are bound dynamically during execution.

See (raw/javascriptallonge.pdf p.62-78) for detailed examples.
