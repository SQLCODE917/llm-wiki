---
page_id: javascriptallonge-recipe-mapwith
page_kind: recipe
page_family: recipe-pattern
summary: mapWith: reusable source-backed pattern with 6 statement(s) and 7 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: mapwith
projection_coverage: recipe-javascriptallonge-recipe-mapwith@06c019d6a2b17401e5f29863505b6e34
---

# mapWith

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-data-mapwith-588e9415]].
- Evidence roles: decision, constraint, definition, explanation, procedure, example.

## Applicability And Rationale

- That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. _(javascriptallonge.pdf (source-range-7239e085-01437))_
- 82 Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-7239e085-01440))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-7239e085-01440))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-7239e085-01440))_
- If we didn't use mapWith , we'd could have also used callRight with map to accomplish the same result: _(javascriptallonge.pdf (source-range-7239e085-01442))_
- mapWith is a very convenient abstraction for a very common pattern. _(javascriptallonge.pdf (source-range-7239e085-01444))_

## Technical Atoms

### Atom 1: `worked-example`

_Source: javascriptallonge.pdf (source-range-7239e085-01430)_

```
In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01431)_

```
[1, 2, 3, 4, 5].map(x => x * x)
//=> [1, 4, 9, 16, 25]
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01433)_

```
const map = (list, fn) =>
list.map(fn);
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01435)_

```
const mapWith = (fn) => (list) => list.map(fn);
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01438)_

```
const squaresOf = (list) =>
list.map(x => x * x);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01441)_

```
const squaresOf = mapWith(n => n * n);
squaresOf([1, 2, 3, 4, 5])
//=> [1, 4, 9, 16, 25]
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-data-mapwith-588e9415]]
