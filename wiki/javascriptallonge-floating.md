---
page_id: javascriptallonge-floating
page_kind: source
summary: Chapter on floating-point numbers in JavaScript
sources: raw/javascriptallonge.pdf p.25-26
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses floating-point representation in JavaScript, including how numbers are represented internally as floating point, and the implications for handling monetary amounts.

## Key supported claims

- But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers (raw/javascriptallonge.pdf p.25-26).
- We can, for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers (raw/javascriptallonge.pdf p.25-26).
- It's tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, 'Nooooooooooooooooooooo.' A computer's internal representation for a floating point number is binary, while our literal number was in base ten (raw/javascriptallonge.pdf p.25-26).
- Professional programmers almost never use floating point numbers to represent monetary amounts (raw/javascriptallonge.pdf p.25-26).
