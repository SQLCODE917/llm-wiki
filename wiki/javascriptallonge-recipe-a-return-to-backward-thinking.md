---
page_id: javascriptallonge-recipe-a-return-to-backward-thinking
page_kind: recipe
page_family: recipe-pattern
summary: a return to backward thinking: reusable source-backed pattern with 18 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: a-return-to-backward-thinking
projection_coverage: recipe-javascriptallonge-recipe-a-return-to-backward-thinking@901061cccc1509cd649fb05707ad0485
---

# a return to backward thinking

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-a-return-to-backward-thinking-b86dc74c]].
- Evidence roles: decision, constraint, procedure, explanation, example.

## Applicability And Rationale

- As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y) . _(javascriptallonge.pdf (source-range-7239e085-01409))_
- To make pairs work, we did things backwards , we passed the first and rest functions to the pair, and the pair called our function. _(javascriptallonge.pdf (source-range-7239e085-01409))_
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. _(javascriptallonge.pdf (source-range-7239e085-01410))_
- But we could have done something completely different. _(javascriptallonge.pdf (source-range-7239e085-01410))_
- All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-7239e085-01410))_
- The exact implementation of a pair is hidden from the code that uses a pair. _(javascriptallonge.pdf (source-range-7239e085-01411))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01412)_

```
const first = K,
second = K(I),
pair = (first) => (second) => {
const pojo = {first, second};
return (selector) => selector(pojo.first)(pojo.second);
};
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01415)_

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01418)_

```
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-yes-consider-this-variation-making-data-out-of-functions-a-return-to-backward-thinking-b86dc74c]]
