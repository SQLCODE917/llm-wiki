---
page_id: javascriptallonge-section-operations-on-numbers-c93c2f75
page_kind: source
summary: **operations on numbers**: 5 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-operations-on-numbers-c93c2f75@84003de7e8777f0fd2613fedb3f0ec4d
---

# **operations on numbers**

From [[javascriptallonge]].

## Statements

- As we’ve seen, JavaScript has many common arithmetic operators. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- These can be combined to make more complex expressions, like 2 * 5 + 1. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. _(javascriptallonge.pdf (source-range-83ecb080-00240))_
- JavaScript has many more operators. _(javascriptallonge.pdf (source-range-83ecb080-00242))_

## Technical atoms

> Context: In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2), because the * operator has a _higher precedence_ than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the nam
_(context: javascriptallonge.pdf (source-range-83ecb080-00240, source-range-83ecb080-00242))_

> 2 * 5 + 1 _//=> 11_ 1 + 5 * 2 _//=> 11_
_(source: javascriptallonge.pdf (source-range-83ecb080-00241))_
