---
page_id: javascriptallonge-recipe-value-types
page_kind: recipe
page_family: recipe-pattern
summary: value types: reusable source-backed pattern with 7 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: value-types
projection_coverage: recipe-javascriptallonge-recipe-value-types@8b76027d6ecdcba4302c1e6e27c67a30
---

# value types

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-and-identity-value-types-eb382c99]].
- Evidence roles: decision, example, structured-state, technical-atom.

## Applicability And Rationale

- Third, some types of cups have no distinguishing marks on them. _(javascriptallonge.pdf (source-range-7239e085-00124))_
- If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. _(javascriptallonge.pdf (source-range-7239e085-00124))_
- This is the case with the strings, numbers, and booleans we have seen so far. _(javascriptallonge.pdf (source-range-7239e085-00124))_
- Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. _(javascriptallonge.pdf (source-range-7239e085-00126))_
- We'll use both terms interchangeably. _(javascriptallonge.pdf (source-range-7239e085-00126))_
- We haven't encountered the fourth possibility yet. _(javascriptallonge.pdf (source-range-7239e085-00127))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00125)_

```
2 + 2 === 4
//=> true
(2 + 2 === 4) === (2 !== 5)
//=> true
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-and-identity-value-types-eb382c99]]
