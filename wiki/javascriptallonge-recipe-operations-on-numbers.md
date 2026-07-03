---
page_id: javascriptallonge-recipe-operations-on-numbers
page_kind: recipe
page_family: recipe-pattern
summary: operations on numbers: reusable source-backed pattern with 4 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: operations-on-numbers
projection_coverage: recipe-javascriptallonge-recipe-operations-on-numbers@ab66dd9dc803675811fba801d84fded7
---

# operations on numbers

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-a-rich-aroma-basic-numbers-operations-on-numbers-57cbae24]].
- Evidence roles: decision, constraint, example, technical-atom.

## Applicability And Rationale

- As we've seen, JavaScript has many common arithmetic operators. _(javascriptallonge.pdf (source-range-7239e085-00157))_
- These can be combined to make more complex expressions, like 2 * 5 + 1 . _(javascriptallonge.pdf (source-range-7239e085-00157))_
- In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. _(javascriptallonge.pdf (source-range-7239e085-00158))_
- JavaScript has many more operators. _(javascriptallonge.pdf (source-range-7239e085-00160))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00159)_

```
2 * 5 + 1
//=> 11
1 + 5 * 2
//=> 11
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-a-rich-aroma-basic-numbers-operations-on-numbers-57cbae24]]
