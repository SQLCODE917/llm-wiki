---
page_id: javascriptallonge-recipe-destructuring-is-not-pattern-matching
page_kind: recipe
page_family: recipe-pattern
summary: destructuring is not pattern matching: reusable source-backed pattern with 6 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: destructuring-is-not-pattern-matching
projection_coverage: recipe-javascriptallonge-recipe-destructuring-is-not-pattern-matching@1a630b6077e58616a0d42538eff55a0f
---

# destructuring is not pattern matching

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-is-not-pattern-m-d5383046]].
- Evidence roles: decision, constraint, explanation, definition, example.

## Applicability And Rationale

- If it does, assignments are made where appropriate. _(javascriptallonge.pdf (source-range-7239e085-00862))_
- But this is not how JavaScript works. _(javascriptallonge.pdf (source-range-7239e085-00865))_
- JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. _(javascriptallonge.pdf (source-range-7239e085-00865))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. _(javascriptallonge.pdf (source-range-7239e085-00869))_
- As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. _(javascriptallonge.pdf (source-range-7239e085-00869))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-7239e085-00869))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00864)_

```
const [what] = [];
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00866)_

```
const [what] = [];
what
//=> undefined
const [which, what,
who
//=> undefined
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00867)_

```
const [...they] = [];
they
//=> []
const [which, what, .
they
//=> []
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-is-not-pattern-m-d5383046]]
