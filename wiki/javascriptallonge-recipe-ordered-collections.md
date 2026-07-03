---
page_id: javascriptallonge-recipe-ordered-collections
page_kind: recipe
page_family: recipe-pattern
summary: ordered collections: reusable source-backed pattern with 9 statement(s) and 2 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: ordered-collections
projection_coverage: recipe-javascriptallonge-recipe-ordered-collections@d598580bbb74b087e967d22a1bc17027
---

# ordered collections

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-like-this-ordered-collections-a2e8339c]].
- Evidence roles: decision, explanation, example.

## Applicability And Rationale

- One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. _(javascriptallonge.pdf (source-range-7239e085-01579))_
- The iterables we're discussing represent ordered collections . _(javascriptallonge.pdf (source-range-7239e085-01579))_
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator] , and ensuring that our iterators start at the beginning and work forward. _(javascriptallonge.pdf (source-range-7239e085-01581))_
- Iterables needn't represent ordered collections. _(javascriptallonge.pdf (source-range-7239e085-01582))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-7239e085-01584))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-7239e085-01584))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01580)_

```
const abc = ["a", "b", "c"];
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
for (const i of abc) {
console.log(i)
}
//=>
a
b
c
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01583)_

```
const RandomNumbers = {
[Symbol.iterator]: () =>
({
next () {
return {value: Math.random()};
}
})
}
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.494052127469331
0.835459444206208
0.1408337657339871
...
for (const i of RandomNumbers) {
console.log(i)
}
//=>
0.7845381607767195
0.4956772483419627
0.20259276474826038
...
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-like-this-ordered-collections-a2e8339c]]
