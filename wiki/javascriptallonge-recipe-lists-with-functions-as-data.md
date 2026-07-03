---
page_id: javascriptallonge-recipe-lists-with-functions-as-data
page_kind: recipe
page_family: recipe-pattern
summary: lists with functions as data: reusable source-backed pattern with 4 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: lists-with-functions-as-data
projection_coverage: recipe-javascriptallonge-recipe-lists-with-functions-as-data@b67de53d4f638f10046db9344751cf0e
---

# lists with functions as data

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-lists-with-functions-as-data-6f298a2f]].
- Evidence roles: decision, procedure, constraint, example.

## Applicability And Rationale

- Here's another look at linked lists using POJOs. _(javascriptallonge.pdf (source-range-7239e085-01377))_
- And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-7239e085-01385))_
- Presto, we can use pure functions to represent a linked list . _(javascriptallonge.pdf (source-range-7239e085-01385))_
- We used functions to replace arrays and POJOs, but we still use JavaScript's built-in operators to test for equality ( === ) and to branch ?: . _(javascriptallonge.pdf (source-range-7239e085-01387))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01378)_

```
const first = ({first, rest}) => first,
rest
= ({first, rest}) => rest,
pair = (first, rest) => ({first, rest}),
EMPTY = ({});
const l123 = pair(1, pair(2, pair(3, EMPTY)));
first(l123)
//=> 1
first(rest(l123))
//=> 2
first(rest(rest(l123)))
//=3
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01380)_

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(rest(aPair));
length(l123)
//=> 3
const reverse = (aPair, delayed = EMPTY) =>
aPair === EMPTY
? delayed
: reverse(rest(aPair), pair(first(aPair), delayed));
const mapWith = (fn, aPair, delayed = EMPTY) =>
aPair === EMPTY
? reverse(delayed)
: mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed));
const doubled = mapWith((x) => x * 2, l123);
first(doubled)
//=> 2
first(rest(doubled))
//=> 4
first(rest(rest(doubled)))
//=> 6
Can we do the same with the linked lists we build out of functions? Yes:
const first = K,
rest
= K(I),
pair = V,
EMPTY = (() => {});
const l123 = pair(1)(pair(2)(pair(3)(EMPTY)));
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01381)_

```
rest
= K(I),
pair = V,
EMPTY = (() => {});
const l123 = pair(1)(pair(
l123(first)
//=> 1
l123(rest)(first)
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01382)_

```
//=> 2
return l123(rest)(rest)(first)
//=> 3
We write them in a backwards way, but they seem to work. How about
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01384)_

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(aPair(rest));
length(l123)
//=> 3
And mapWith?
const reverse = (aPair, delayed = EMPTY) =>
aPair === EMPTY
? delayed
: reverse(aPair(rest), pair(aPair(first))(delayed));
const mapWith = (fn, aPair, delayed = EMPTY) =>
aPair === EMPTY
? reverse(delayed)
: mapWith(fn, aPair(rest), pair(fn(aPair(first)))(delayed));
const doubled = mapWith((x) => x * 2, l123)
doubled(first)
//=> 2
doubled(rest)(first)
//=> 4
doubled(rest)(rest)(first)
//=> 6
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-lists-with-functions-as-data-6f298a2f]]
