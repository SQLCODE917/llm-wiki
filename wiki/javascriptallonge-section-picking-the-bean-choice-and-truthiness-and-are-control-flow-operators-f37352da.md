---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-f37352da
page_kind: source
summary: Picking the Bean: Choice and Truthiness / || and && are control-flow operators: 4 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-f37352da@b18fb4ff205bd6cbc23b6590ae1fe721
---

# Picking the Bean: Choice and Truthiness / || and && are control-flow operators

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-d45c6f89]] - broader source section: Picking the Bean: Choice and Truthiness

## Statements

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and || . Consider this tail-recursive function that determines whether a positive integer is even: _(javascriptallonge.pdf (source-range-7239e085-00793))_
- This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-7239e085-00799))_

## Technical atoms

### Technical frame 1: Picking the Bean: Choice and Truthiness / || and && are control-flow operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00799))_

> This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00795))_

```
const even = (n) =>
n === 0 || (n !== 1 && even(n - 2))
even(42)
//=> true
```
