---
page_id: javascriptallonge-recipe-say-please
page_kind: recipe
page_family: recipe-pattern
summary: say 'please': reusable source-backed pattern with 5 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: say-please
projection_coverage: recipe-javascriptallonge-recipe-say-please@c3cdc85cecca613344bcdfb7e3c7c819
---

# say 'please'

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-say-please-4edc5a79]].
- Evidence roles: decision, procedure, constraint, explanation, example.

## Applicability And Rationale

- This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-7239e085-01389))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-7239e085-01390))_
- Now we'll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. _(javascriptallonge.pdf (source-range-7239e085-01394))_
- We can write reverse and mapWith as well. _(javascriptallonge.pdf (source-range-7239e085-01397))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-7239e085-01399))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01391)_

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(aPair(rest));
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01393)_

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(rest)))
);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01395)_

```
const pairFirst = K,
pairRest
= K(I),
pair = V;
const first = (list) => list(
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairFirst)
);
const rest = (list) => list(
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01396)_

```
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairRest)
);
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
We’ll also write a handy list printer:
const print = (list) => list(
() => "",
(aPair) => `${aPair(pairFirst)} ${print(aPair(pairRest))}`
);
How would all this work? Let’s start with the obvious. What is an empty list?
const EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty()
And what is a node of a list?
const node = (x) => (y) =>
(whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));
Let’s try it:
const l123 = node(1)(node(2)(node(3)(EMPTYLIST)));
print(l123)
//=> 1 2 3
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01398)_

```
const reverse = (list, delayed = EMPTYLIST) => list(
() => delayed,
(aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed))
);
print(reverse(l123));
//=> 3 2 1
const mapWith = (fn, list, delayed = EMPTYLIST) =>
list(
() => reverse(delayed),
(aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed))
);
print(mapWith(x => x * x, reverse(l123)))
//=> 941
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-say-please-4edc5a79]]
