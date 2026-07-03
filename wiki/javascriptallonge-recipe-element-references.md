---
page_id: javascriptallonge-recipe-element-references
page_kind: recipe
page_family: recipe-pattern
summary: element references: reusable source-backed pattern with 2 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: element-references
projection_coverage: recipe-javascriptallonge-recipe-element-references@e9b51965f934c3396474d3da1a3b86eb
---

# element references

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-element-references-a8dcb708]].
- Evidence roles: decision, constraint, procedure, example.

## Applicability And Rationale

- Array elements can be extracted using [ and ] as postfix operators. _(javascriptallonge.pdf (source-range-7239e085-00834))_
- We know that every array is its own unique entity, with its own unique reference. _(javascriptallonge.pdf (source-range-7239e085-00837))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00835)_

```
const oneTwoThree = ["one", "two", "three"];
oneTwoThree[0]
//=> 'one'
oneTwoThree[1]
//=> 'two'
oneTwoThree[2]
//=> 'three'
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00839)_

```
const x = [],
a = [x];
a[0] === x
//=> true, arrays store references to the things you put in them.
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-element-references-a8dcb708]]
