---
page_id: javascriptallonge-recipe-gathering
page_kind: recipe
page_family: recipe-pattern
summary: gathering: reusable source-backed pattern with 3 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: gathering
projection_coverage: recipe-javascriptallonge-recipe-gathering@c522176563d714f0af1a24b426dbd139
---

# gathering

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-gathering-91ed37bf]].
- Evidence roles: decision, example, structured-state.

## Applicability And Rationale

- Sometimes we need to extract arrays from arrays. _(javascriptallonge.pdf (source-range-7239e085-00853))_
- Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-7239e085-00853))_
- notation does not provide a universal patten-matching capability. _(javascriptallonge.pdf (source-range-7239e085-00856))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00854)_

```
const [car, ...cdr] = [1, 2, 3, 4, 5];
car
//=> 1
cdr
//=> [2, 3, 4, 5]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00858)_

```
const [...butLast, last] = [1, 2, 3, 4, 5];
//=> ERROR
const [first, ..., last] = [1, 2, 3, 4, 5];
//=> ERROR
Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals.
So if
const wrapped = [something];
Then:
const [unwrapped] = something;
What is the reverse of gathering? We know that:
const [car, ...cdr] = [1, 2, 3, 4, 5];
What is the reverse? It would be:
const cons = [car, ...cdr];
Let’s try it:
const oneTwoThree = ["one", "two", "three"];
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00859)_

```
Let’s try it:
const oneTwoThree = ["one", "two", "
["zero", ...oneTwoThree]
//=> ["zero","one","two","three"]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-gathering-91ed37bf]]
