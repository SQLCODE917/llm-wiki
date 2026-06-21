---
page_id: javascriptallonge-unary
page_kind: source
summary: Summary of the Unary function decorator section from 'JavaScript Allongé'.
sources: raw/javascriptallonge.pdf p.82-83
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

'Unary' is a function decorator that modifies the number of arguments a function takes.

## Key supported claims

- Unary modifies the number of arguments a function takes, converting any function into one that accepts exactly one argument (raw/javascriptallonge.pdf p.82-83).
- Unary fixes issues with JavaScript's map method when using functions like parseInt that have optional arguments (raw/javascriptallonge.pdf p.82-83).
- Unary is implemented as a function decorator that checks function length and wraps functions taking more than one argument (raw/javascriptallonge.pdf p.82-83).
