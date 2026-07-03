---
page_id: javascriptallonge-recipe-truthiness-and-the-ternary-operator
page_kind: recipe
page_family: recipe-pattern
summary: truthiness and the ternary operator: reusable source-backed pattern with 11 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: truthiness-and-the-ternary-operator
projection_coverage: recipe-javascriptallonge-recipe-truthiness-and-the-ternary-operator@0a47b3498445762492cef0efd1d9fd42
---

# truthiness and the ternary operator

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-d8796156]].
- Evidence roles: decision, explanation, constraint, example.

## Applicability And Rationale

- 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-7239e085-00765))_
- So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. _(javascriptallonge.pdf (source-range-7239e085-00765))_
- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. _(javascriptallonge.pdf (source-range-7239e085-00765))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . _(javascriptallonge.pdf (source-range-7239e085-00766))_
- If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-7239e085-00768))_
- JavaScript inherited an operator from the C family of languages, the ternary operator. _(javascriptallonge.pdf (source-range-7239e085-00768))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00772)_

```
true ? 'Hello' : 'Good bye'
//=> 'Hello'
0 ? 'Hello' : 'Good bye'
//=> 'Good bye'
[1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal'
//=> 'Pentatonic'
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00774)_

```
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\
den';
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-d8796156]]
