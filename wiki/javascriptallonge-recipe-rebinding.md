---
page_id: javascriptallonge-recipe-rebinding
page_kind: recipe
page_family: recipe-pattern
summary: rebinding: reusable source-backed pattern with 2 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: rebinding
projection_coverage: recipe-javascriptallonge-recipe-rebinding@fc4c2bee0954d16c5ef1544e0ac64205
---

# rebinding

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-that-constant-coffee-craving-rebinding-c21c4915]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- We can shadow it by using const to declare a new binding with a new function or block scope, but we cannot rebind a name that was bound with const in an existing scope. _(javascriptallonge.pdf (source-range-7239e085-00496))_
- This is valuable, as it greatly simplifies the analysis of programs to see at a glance that when something is bound with const , we need never worry that its value may change. _(javascriptallonge.pdf (source-range-7239e085-00497))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00493)_

```
const evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
n = n - 2;
return evenStevens(n);
}
}
evenStevens(42)
//=> true
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00495)_

```
evenStevens = (n) => {
if (n === 0) {
return true;
}
else if (n == 1) {
return false;
}
else {
return evenStevens(n - 2);
}
}
//=> ERROR, evenStevens is read-only
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-that-constant-coffee-craving-rebinding-c21c4915]]
