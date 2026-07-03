---
page_id: javascriptallonge-recipe-variables-and-bindings
page_kind: recipe
page_family: recipe-pattern
summary: variables and bindings: reusable source-backed pattern with 17 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: variables-and-bindings
projection_coverage: recipe-javascriptallonge-recipe-variables-and-bindings@f735fb92a3c36b13eb6e2b31e4c6cec5
---

# variables and bindings

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-variables-and-bindings-4f74d027]].
- Evidence roles: decision, constraint, explanation, definition, procedure, example, structured-state.

## Applicability And Rationale

- Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. _(javascriptallonge.pdf (source-range-7239e085-00298))_
- Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics. _(javascriptallonge.pdf (source-range-7239e085-00300))_
- It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more. _(javascriptallonge.pdf (source-range-7239e085-00301))_
- But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. _(javascriptallonge.pdf (source-range-7239e085-00301))_
- The second x , the one in => x , is not an argument, it's an expression referring to a variable . _(javascriptallonge.pdf (source-range-7239e085-00302))_
- The x in the expression that we call a 'variable' is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-7239e085-00303))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00299)_

```
(x) => (y) => x
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00306)_

```
((x) => x)(2)
//=> 2
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-variables-and-bindings-4f74d027]]
