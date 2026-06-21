---
page_id: javascriptallonge-function-declarations
page_kind: source
summary: Summary of function declarations in JavaScript as described in 'JavaScript Allongé'.
sources: raw/javascriptallonge.pdf p.65-66
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Function declarations are a syntax for naming and/or defining a function in JavaScript, with specific behaviors like hoisting.

## Key supported claims

- First, function declarations are hoisted to the top of the function in which they occur (raw/javascriptallonge.pdf p.65-66).
- There is another syntax for naming and/or defining a function (raw/javascriptallonge.pdf p.65-66).
- Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const : (raw/javascriptallonge.pdf p.65-66).
- It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code (raw/javascriptallonge.pdf p.65-66).
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error (raw/javascriptallonge.pdf p.65-66).
