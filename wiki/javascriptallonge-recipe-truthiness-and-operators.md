---
page_id: javascriptallonge-recipe-truthiness-and-operators
page_kind: recipe
page_family: recipe-pattern
summary: truthiness and operators: reusable source-backed pattern with 7 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: truthiness-and-operators
projection_coverage: recipe-javascriptallonge-recipe-truthiness-and-operators@1ad15d15564993746d222c8313c9e671
---

# truthiness and operators

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-f4c050bc]].
- Evidence roles: decision, example, structured-state.

## Applicability And Rationale

- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-7239e085-00777))_
- , && , and || are a little more subtle than our examples above implied. _(javascriptallonge.pdf (source-range-7239e085-00777))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. _(javascriptallonge.pdf (source-range-7239e085-00779))_
- , && and || do not necessarily evaluate to true or false . _(javascriptallonge.pdf (source-range-7239e085-00781))_
- If we look at our examples above, we see that when we pass true and false to && and || , we do indeed get true or false as a result. _(javascriptallonge.pdf (source-range-7239e085-00788))_
- They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && . _(javascriptallonge.pdf (source-range-7239e085-00790))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00778)_

```
!5
//=> false
!undefined
//=> true
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00789)_

```
1 || 2
//=> 1
null && undefined
//=> null
undefined && null
//=> undefined
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-f4c050bc]]
