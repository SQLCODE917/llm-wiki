---
page_id: javascriptallonge-section-and-are-control-flow-operators-70d39cfa
page_kind: source
summary: **|| and && are control-flow operators**: 4 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-are-control-flow-operators-70d39cfa@414fa2f800df3a272bd9bb49b5084cff
---

# **|| and && are control-flow operators**

From [[javascriptallonge]].

## Statements

- We’ve seen the ternary operator: It is a _control-flow_ operator, not a logical operator. _(javascriptallonge.pdf (source-range-83ecb080-01149))_
- The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-83ecb080-01159))_
- This is more than just an optimization. _(javascriptallonge.pdf (source-range-83ecb080-01159))_

## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01153))_

> **const** even = (n) => n === 0 || (n !== 1 && even(n - 2))
