---
page_id: javascriptallonge-function-decorators
page_kind: source
summary: Summary of function decorators in JavaScript Allongé
sources: raw/javascriptallonge.pdf p.69-70
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Function decorators are higher-order functions that take one function as an argument, return another function, and the returned function is a variation of the argument function.

## Key supported claims

- A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. (raw/javascriptallonge.pdf p.69-70)
- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. (raw/javascriptallonge.pdf p.69-70)
- Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. (raw/javascriptallonge.pdf p.69-70)
- You'll see other function decorators in the recipes, like once and maybe. (raw/javascriptallonge.pdf p.69-70)
- This implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. (raw/javascriptallonge.pdf p.69-70)
