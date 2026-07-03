---
page_id: javascriptallonge-recipe-call-by-value
page_kind: recipe
page_family: recipe-pattern
summary: call by value: reusable source-backed pattern with 4 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: call-by-value
projection_coverage: recipe-javascriptallonge-recipe-call-by-value@520983436a25f14f74d600dd88707d4c
---

# call by value

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-value-ae929990]].
- Evidence roles: decision, definition, explanation, procedure, example.

## Applicability And Rationale

- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-7239e085-00291))_
- Then our circumference function was applied to 2 . _(javascriptallonge.pdf (source-range-7239e085-00295))_
- What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . _(javascriptallonge.pdf (source-range-7239e085-00295))_
- We'll see below that while JavaScript always calls by value, the notion of a 'value' has additional subtlety. _(javascriptallonge.pdf (source-range-7239e085-00296))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00294)_

```
((diameter) => diameter * 3.14159265)(1 + 1)
//=> 6.2831853
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-value-ae929990]]
