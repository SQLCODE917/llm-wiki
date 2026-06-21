---
page_id: javascriptallonge-yes-consider-this-variation
page_kind: source
summary: Summary of the 'Yes. Consider this variation' section from javascriptallonge.pdf, pages 155-157, focusing on closure and variable scoping with var vs let.
sources: raw/javascriptallonge.pdf p.155-157
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This section from JavaScript Allongé explores the pitfalls of using `var` in loops and how `let` provides a cleaner solution, demonstrating closure behavior with a practical example.

## Key supported claims

- So when the function is called, JavaScript looks up i in its enclosing environment (its closure, obviously), and gets the value 3, as cited in (raw/javascriptallonge.pdf p.155-157).
- But at the time we call one of the functions, i has the value 3, which is why the loop terminated, as cited in (raw/javascriptallonge.pdf p.155-157).
- The answer is that pesky var i, as cited in (raw/javascriptallonge.pdf p.155-157).
