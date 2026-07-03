---
page_id: javascriptallonge-recipe-evaluation-time
page_kind: recipe
page_family: recipe-pattern
summary: evaluation time: reusable source-backed pattern with 2 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: evaluation-time
projection_coverage: recipe-javascriptallonge-recipe-evaluation-time@f990b1b5e7c9450fa2fff034e3f34109
---

# evaluation time

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-evaluation-time-a314598a]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. _(javascriptallonge.pdf (source-range-7239e085-01519))_
- Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-7239e085-01519))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01518)_

```
const name = "Harry";
const greeting = (name) => `Hello my name is ${name}`;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01521)_

```
const greeting = (name) => 'Hello my name is ' + name;
greeting('Arthur Dent')
//=> 'Hello my name is Arthur Dent'
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-evaluation-time-a314598a]]
