---
page_id: javascriptallonge-recipe-quasi-literals
page_kind: recipe
page_family: recipe-pattern
summary: quasi-literals: reusable source-backed pattern with 5 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: quasi-literals
projection_coverage: recipe-javascriptallonge-recipe-quasi-literals@48694591d94dc5304788e8673c640686
---

# quasi-literals

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-a1ab40aa]].
- Evidence roles: decision, constraint, procedure, explanation, example.

## Applicability And Rationale

- Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-7239e085-01505))_
- The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-7239e085-01507))_
- A quasi-literal can contain an expression to be evaluated. _(javascriptallonge.pdf (source-range-7239e085-01507))_
- Aquasi-literal is computationally equivalent to an expression using + . _(javascriptallonge.pdf (source-range-7239e085-01510))_
- Quasi-literals are expressions that resemble their result. _(javascriptallonge.pdf (source-range-7239e085-01513))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01506)_

```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01509)_

```
`A popular number for nerds is ${40 + 2}`
//=> 'A popular number for nerds is 42'
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01512)_

```
'A popular number for nerds is ' + (40 + 2)
//=> 'A popular number for nerds is 42'
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01514)_

```
'A popular number for nerds is' + (40 + 2)
//=> 'A popular number for nerds is42'
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-a-warm-cup-basic-strings-and-quasi-literals-quasi-literals-a1ab40aa]]
