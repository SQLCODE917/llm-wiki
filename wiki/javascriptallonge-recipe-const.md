---
page_id: javascriptallonge-recipe-const
page_kind: recipe
page_family: recipe-pattern
summary: const: reusable source-backed pattern with 11 statement(s) and 9 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: const
projection_coverage: recipe-javascriptallonge-recipe-const@9e1b54510f34508d628b73971360385e
---

# const

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-that-constant-coffee-craving-const-1d605a7f]].
- Evidence roles: decision, explanation, constraint, procedure, example, structured-state.

## Applicability And Rationale

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-7239e085-00415))_
- This differs from our example above in that there is only one environment, rather than two. _(javascriptallonge.pdf (source-range-7239e085-00419))_
- We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name. _(javascriptallonge.pdf (source-range-7239e085-00419))_
- JavaScript gives us a way to do that, the const keyword. _(javascriptallonge.pdf (source-range-7239e085-00420))_
- We'll learn a lot more about const in future chapters, but here's the most important thing we can do with const : _(javascriptallonge.pdf (source-range-7239e085-00420))_
- That's much better than what we were writing. _(javascriptallonge.pdf (source-range-7239e085-00422))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00416)_

```
(diameter, PI) => diameter * PI
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00418)_

```
((diameter, PI) => diameter * PI)(2, 3.14159265)
//=> 6.2831853
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00421)_

```
(diameter) => {
const PI = 3.14159265;
return diameter * PI
}
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00425)_

```
((diameter) =>
((PI) =>
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00426)_

```
diameter * PI)(3.14159265))(2)
Or:
((diameter, PI) => diameter * PI)(2, 3.14159265)
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00427)_

```
//=> 6.2831853
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-that-constant-coffee-craving-const-1d605a7f]]
