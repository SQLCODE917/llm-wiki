---
page_id: javascriptallonge-section-left-variadic-functions-f2a30dd2
page_kind: source
summary: **Left-Variadic Functions**: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-left-variadic-functions-f2a30dd2@d893e384d282b6cc616c9970d68d8374
---

# **Left-Variadic Functions**

From [[javascriptallonge]].

## Statements

- A _variadic function_ is a function that is designed to accept a variable number of arguments.[52] In JavaScript, you can make a variadic function by gathering parameters. _(javascriptallonge.pdf (source-range-83ecb080-01039))_
- This can be useful when writing certain kinds of destructuring algorithms. _(javascriptallonge.pdf (source-range-83ecb080-01041))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-83ecb080-01041))_
- For example, we might want to have a function that builds some kind of team record. _(javascriptallonge.pdf (source-range-83ecb080-01041))_

## Technical atoms

> Context: A _variadic function_ is a function that is designed to accept a variable number of arguments.[52] In JavaScript, you can make a variadic function by gathering parameters. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01039))_

> **const** abccc = (a, b, ...c) => { console.log(a); console.log(b); console.log(c); }; abccc(1, 2, 3, 4, 5) 1 2 [3,4,5]
_(source: javascriptallonge.pdf (source-range-83ecb080-01040))_
