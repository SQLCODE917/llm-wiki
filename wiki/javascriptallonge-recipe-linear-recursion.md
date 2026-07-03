---
page_id: javascriptallonge-recipe-linear-recursion
page_kind: recipe
page_family: recipe-pattern
summary: linear recursion: reusable source-backed pattern with 12 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: linear-recursion
projection_coverage: recipe-javascriptallonge-recipe-linear-recursion@e4c840090dc3f6f8530377b48821f8ca
---

# linear recursion

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-linear-recursion-4c0b6367]].
- Evidence roles: decision, constraint, definition, procedure, explanation, example.

## Applicability And Rationale

- There is more to recursive solutions that simply functions that invoke themselves. _(javascriptallonge.pdf (source-range-7239e085-00910))_
- - When all small problems have been solved, compose the solutions into one big solution _(javascriptallonge.pdf (source-range-7239e085-00914))_
- Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-7239e085-00915))_
- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. _(javascriptallonge.pdf (source-range-7239e085-00915))_
- This simpler form of 'divide and conquer' is called linear recursion . _(javascriptallonge.pdf (source-range-7239e085-00916))_
- Sometimes we want to flatten an array, that is, an array of arrays needs to be turned into one array of elements that aren't arrays. _(javascriptallonge.pdf (source-range-7239e085-00916))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00918)_

```
Array.isArray("foo")
//=> false
Array.isArray(["foo"])
//=> true
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00922)_

```
const flatten = ([first, ...rest]) => {
if (first === undefined) {
return [];
}
else if (!Array.isArray(first)) {
return [first, ...flatten(rest)];
}
else {
return [...flatten(first), ...flatten(rest)];
}
}
flatten(["foo", [3, 4, []]])
//=> ["foo",3,4]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-composing-and-decomposing-data-self-similarity-linear-recursion-4c0b6367]]
