---
category: concept
summary: Functional programming concepts including closures and scope chains in JavaScript.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

Functional programming emphasizes functions as first-class citizens. Key concepts from JavaScript include:

- **Closures**: Functions that capture and retain access to variables from their lexical scope (e.g., [[javascriptallonge-closures-and-scope]]).
- **Scope chains**: Hierarchical environments allowing nested functions to access outer variables (e.g., `[[javascriptallonge-closures-and-scope]]` explains the `'..'` parent environment reference).
- **Pure functions** vs. closures: Pure functions depend only on inputs (e.g., `(x) => x`), while closures use external variables (e.g., `(y) => x` from [[javascriptallonge-closures-and-scope]]).

These mechanisms enable functional programming patterns like currying and partial application, as discussed in [[javascriptallonge-closures-and-scope]].
