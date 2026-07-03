---
page_id: javascriptallonge-recipe-call-by-sharing
page_kind: recipe
page_family: recipe-pattern
summary: call by sharing: reusable source-backed pattern with 12 statement(s) and 1 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: call-by-sharing
projection_coverage: recipe-javascriptallonge-recipe-call-by-sharing@6c3ce470d28f3db230ecab022c062ae2
---

# call by sharing

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-sharing-96a55cff]].
- Evidence roles: decision, constraint, definition, explanation, procedure, structured-state, example.

## Applicability And Rationale

- Now it is time to take another look at the distinction between value and reference types. _(javascriptallonge.pdf (source-range-7239e085-00320))_
- At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. _(javascriptallonge.pdf (source-range-7239e085-00320))_
- Earlier, we distinguished JavaScript's value types from its reference types . _(javascriptallonge.pdf (source-range-7239e085-00320))_
- There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original. _(javascriptallonge.pdf (source-range-7239e085-00321))_
- Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. _(javascriptallonge.pdf (source-range-7239e085-00322))_
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-7239e085-00322))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00327)_

```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-sharing-96a55cff]]
