---
page_id: javascriptallonge-recipe-and-are-control-flow-operators
page_kind: recipe
page_family: recipe-pattern
summary: || and && are control-flow operators: reusable source-backed pattern with 3 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: and-are-control-flow-operators
projection_coverage: recipe-javascriptallonge-recipe-and-are-control-flow-operators@11ad9d564eda676d3678f75f4a5d8922
---

# || and && are control-flow operators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-f37352da]].
- Evidence roles: decision, example.

## Applicability And Rationale

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. _(javascriptallonge.pdf (source-range-7239e085-00793))_
- This is more than just an optimization. _(javascriptallonge.pdf (source-range-7239e085-00799))_
- The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-7239e085-00799))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00795)_

```
const even = (n) =>
n === 0 || (n !== 1 && even(n - 2))
even(42)
//=> true
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-f37352da]]
