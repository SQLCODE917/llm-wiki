---
page_id: javascriptallonge-recipe-values-are-expressions
page_kind: recipe
page_family: recipe-pattern
summary: values are expressions: reusable source-backed pattern with 11 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: values-are-expressions
projection_coverage: recipe-javascriptallonge-recipe-values-are-expressions@3b32545d0327b626b7fa57dca3bcb2ad
---

# values are expressions

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-are-expressions-439d7791]].
- Evidence roles: decision, constraint, explanation, structured-state, example.

## Applicability And Rationale

- All values are expressions. _(javascriptallonge.pdf (source-range-7239e085-00101))_
- Yup, you hand over a cup with some coffee infused through partially caramelized sugar. _(javascriptallonge.pdf (source-range-7239e085-00101))_
- Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista). _(javascriptallonge.pdf (source-range-7239e085-00101))_
- You say, 'I want one of these.' The barista is no fool, she gives it straight back to you, and you get exactly what you want. _(javascriptallonge.pdf (source-range-7239e085-00101))_
- The answer is, this is both an expression and a value. _(javascriptallonge.pdf (source-range-7239e085-00105))_
- Instead of handing over the finished coffee, we can hand over the ingredients. _(javascriptallonge.pdf (source-range-7239e085-00107))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00106)_

```
42
//=> 42
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00111)_

```
"JavaScript" + " " + "Allonge"
//=> "JavaScript Allonge"
```

### Atom 3: `worked-example`

_Source: javascriptallonge.pdf (source-range-7239e085-00113)_

```
Nowwesee that 'strings' are values, and you can make an expression out of strings and an operator + . Since strings are values, they are also expressions by themselves. But strings with operators are not values, they are expressions. Now we know what was missing with our 'coffee grounds plus hot water' example. The coffee grounds were a value, the boiling hot water was a value, and the 'plus' operator between them made the whole thing an expression that was not a value.
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-prelude-values-and-expressions-over-coffee-values-are-expressions-439d7791]]
