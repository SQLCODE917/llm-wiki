---
page_id: javascriptallonge-composition
page_kind: source
summary: Chapter on function composition in JavaScript Allongé.
sources: raw/javascriptallonge.pdf p.71-71
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter covers function composition in JavaScript, including the use of the compose function and decorators like once and maybe.

## Key supported claims

- Function composition chains functions together, as in `const cookAndEat = (food) => eat(cook(food));` (raw/javascriptallonge.pdf p.71-71).
- The compose function generalizes composition: `const compose = (a, b) => (c) => a(b(c));` (raw/javascriptallonge.pdf p.71-71).
- Decorators like once ensure functions execute only once, and maybe ensures functions do nothing when given null or undefined (raw/javascriptallonge.pdf p.71-71).
