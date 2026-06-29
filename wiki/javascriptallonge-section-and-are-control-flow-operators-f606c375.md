---
page_id: javascriptallonge-section-and-are-control-flow-operators-f606c375
page_kind: source
summary: || and && are control-flow operators: 4 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-are-control-flow-operators-f606c375@db95e6e4a570e68779f9ba0ffb096662
---

# || and && are control-flow operators

From [[javascriptallonge]].

## Statements

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and || . Consider this tail-recursive function that determines whether a positive integer is even: _(javascriptallonge.pdf (source-range-8eb13d6b-00793))_
- This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-8eb13d6b-00799))_

## Technical atoms

### Technical frame 1: || and && are control-flow operators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00799))_

> This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00795))_

```
const even = (n) => n === 0 || (n !== 1 && even(n - 2)) even(42) //=> true
```
