---
page_id: javascriptallonge-recipe-functions-that-evaluate-to-functions
page_kind: recipe
page_family: recipe-pattern
summary: functions that evaluate to functions: reusable source-backed pattern with 5 statement(s) and 4 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: functions-that-evaluate-to-functions
projection_coverage: recipe-javascriptallonge-recipe-functions-that-evaluate-to-functions@08d5de16fc0b68b04bc9318b078c745c
---

# functions that evaluate to functions

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-functions-that-evaluate-to-functions-0eac2f2e]].
- Evidence roles: decision, constraint, procedure, structured-state, example.

## Applicability And Rationale

- So we have a function, that returns a function, that returns zero . _(javascriptallonge.pdf (source-range-7239e085-00261))_
- It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . _(javascriptallonge.pdf (source-range-7239e085-00261))_
- Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. _(javascriptallonge.pdf (source-range-7239e085-00268))_
- So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical. _(javascriptallonge.pdf (source-range-7239e085-00268))_
- We've been very clever, but so far this all seems very abstract. _(javascriptallonge.pdf (source-range-7239e085-00268))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00260)_

```
() => () => 0
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00262)_

```
() => () => true
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00264)_

```
(() => () => true)()()
//=> true
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00266)_

```
() => () => { return true; }
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-functions-that-evaluate-to-functions-0eac2f2e]]
