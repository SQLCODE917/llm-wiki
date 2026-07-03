---
page_id: javascriptallonge-recipe-floating
page_kind: recipe
page_family: recipe-pattern
summary: floating: reusable source-backed pattern with 7 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: floating
projection_coverage: recipe-javascriptallonge-recipe-floating@b593e5089a4d481854030012aa6acb38
---

# floating

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-a-rich-aroma-basic-numbers-floating-ebe9399e]].
- Evidence roles: decision, constraint, explanation, example, structured-state.

## Applicability And Rationale

- But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. _(javascriptallonge.pdf (source-range-7239e085-00147))_
- We can, for example, write 1.5 or 33.33 , and JavaScript represents these literals as floating point numbers. _(javascriptallonge.pdf (source-range-7239e085-00147))_
- It's tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, 'Nooooooooooooooooooooo.' A computer's internal representation for a floating point number is binary, while our literal number was in base ten. _(javascriptallonge.pdf (source-range-7239e085-00148))_
- This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2. _(javascriptallonge.pdf (source-range-7239e085-00148))_
- But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic 15 . _(javascriptallonge.pdf (source-range-7239e085-00155))_
- For example, '$43.21' will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21 . _(javascriptallonge.pdf (source-range-7239e085-00155))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00150)_

```
1.0
//=> 1
1.0 + 1.0
//=> 2
1.0 + 1.0 + 1.0
//=> 3
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00153)_

```
0.1
//=> 0.1
0.1 + 0.1
//=> 0.2
0.1 + 0.1 + 0.1
//=> 0.30000000000000004
```

### Atom 3: `worked-example`

_Source: javascriptallonge.pdf (source-range-7239e085-00154)_

```
This kind of 'inexactitude' can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript's calculation is less than a pixel, there is no observable error.
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-a-rich-aroma-basic-numbers-floating-ebe9399e]]
