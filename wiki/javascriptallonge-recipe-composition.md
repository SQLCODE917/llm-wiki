---
page_id: javascriptallonge-recipe-composition
page_kind: recipe
page_family: recipe-pattern
summary: composition: reusable source-backed pattern with 7 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: composition
projection_coverage: recipe-javascriptallonge-recipe-composition@526a04dbff03d1a168af550f50c08a2a
---

# composition

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-building-blocks-composition-b915cf07]].
- Evidence roles: decision, constraint, procedure, explanation, example, structured-state.

## Applicability And Rationale

- It's really that simple: Whenever you are chaining two or more functions together, you're composing them. _(javascriptallonge.pdf (source-range-7239e085-00584))_
- You can compose them with explicit JavaScript code as we've just done. _(javascriptallonge.pdf (source-range-7239e085-00584))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-7239e085-00586))_
- If that was all there was to it, composition wouldn't matter much. _(javascriptallonge.pdf (source-range-7239e085-00586))_
- Thereafter, it does nothing. _(javascriptallonge.pdf (source-range-7239e085-00587))_
- Once is useful for ensuring that certain side effects are not repeated. _(javascriptallonge.pdf (source-range-7239e085-00587))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00583)_

```
const cookAndEat = (food) => eat(cook(food));
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00585)_

```
const compose = (a, b) => (c) => a(b(c));
const cookAndEat = compose(eat, cook);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00589)_

```
const actuallyTransfer= (from, to, amount) =>
// do something
const invokeTransfer = once(maybe(actuallyTransfer(...)));
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-building-blocks-composition-b915cf07]]
