---
page_id: javascriptallonge-naming-functions
page_kind: source
summary: Source summary of JavaScript Allongé chapter on naming functions.
sources: raw/javascriptallonge.pdf p.62-78
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Chapter on naming functions in JavaScript Allongé, covering arrow functions, function keyword, named function expressions, and hoisting.

## Key supported claims

- Arrow functions bind anonymous functions; the function stays unnamed (raw/javascriptallonge.pdf p.62-78).
- `function` keyword with a name creates an internal name separate from the environment binding (raw/javascriptallonge.pdf p.62-78).
- Named function expressions give the function an internal name for recursion, but the outer variable is the environment binding; might help debugging (raw/javascriptallonge.pdf p.62-78).
- Function declarations are hoisted to the top of the scope; cannot appear inside blocks and can be called before declaration (raw/javascriptallonge.pdf p.62-78).
- Functions always use a block; writing `function (str) str + str` is invalid (raw/javascriptallonge.pdf p.62-78).
