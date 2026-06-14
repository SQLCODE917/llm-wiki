---
category: concept
summary: Non-primitive data types in JavaScript compared by reference identity.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

Reference types in JavaScript, such as objects and arrays, are compared by identity rather than value. For example, [1, 2, 3] === [1, 2, 3] evaluates to false because each array is a distinct object. This contrasts with value types like numbers, which are compared by their content. [[javascriptallonge-forewords-to-the-first-edition]]
