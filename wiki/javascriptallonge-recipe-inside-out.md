---
page_id: javascriptallonge-recipe-inside-out
page_kind: recipe
page_family: recipe-pattern
summary: inside-out: reusable source-backed pattern with 11 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: inside-out
projection_coverage: recipe-javascriptallonge-recipe-inside-out@bad498db5000f488215d4213c0213348
---

# inside-out

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-that-constant-coffee-craving-inside-out-96a0dd3a]].
- Evidence roles: decision, constraint, procedure, explanation, example.

## Applicability And Rationale

- We can turn things inside-out by putting the binding inside our diameter calculating function, like this: _(javascriptallonge.pdf (source-range-7239e085-00398))_
- There's another way we can make a function that binds 3.14159265 to the name PI and then uses that in its expression. _(javascriptallonge.pdf (source-range-7239e085-00398))_
- Well, the first one seems simplest, but a half-century of experience has taught us that names matter. _(javascriptallonge.pdf (source-range-7239e085-00402))_
- A 'magic literal' like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-7239e085-00402))_
- The third one is easiest for most people to read. _(javascriptallonge.pdf (source-range-7239e085-00403))_
- 29 JavaScript programmers regularly use the idea of writing an expression that denotes a function and then immediately applying it to arguments. _(javascriptallonge.pdf (source-range-7239e085-00404))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00399)_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00401)_

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
((diameter) =>
((PI) =>
diameter * PI)(3.14159265))(2)
//=> 6.2831853
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00405)_

```
(diameter) =>
// ...
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00407)_

```
((PI) =>
// ...
)(3.14159265)
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00409)_

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00411)_

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-that-constant-coffee-craving-inside-out-96a0dd3a]]
