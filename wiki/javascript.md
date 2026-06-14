---
category: entity
summary: JavaScript features including closures, scope chains, and global environment isolation.
sources: raw/javascriptallonge.pdf
updated: 2026-06-11
---

JavaScript is a dynamic language with:

- **First-class functions** (assignable, passable, returnable)
- **Closures** capturing outer scope variables (e.g., [[javascriptallonge-closures-and-scope]]).
- **Scope chains** via hierarchical environments (`'..'` references as explained in [[javascriptallonge-closures-and-scope]].
- **Global environment** with IIFEs to avoid pollution: `(() => { ... })()` isolates code from the global scope (discussed in [[javascriptallonge-closures-and-scope]].

These features enable functional programming patterns and modular code organization.
