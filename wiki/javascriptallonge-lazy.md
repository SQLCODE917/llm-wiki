---
page_id: javascriptallonge-lazy
page_kind: concept
page_family: topic-concept
summary: Lazy: 1 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-lazy@49c36f3d06b2d67405a010db04e98db3
---

# Lazy

What [[javascriptallonge]] covers about lazy:

## Statements

### We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

- Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-7239e085-01800))_


## Technical atoms

### Technical frame 1: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01800))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01799))_

<a id="atom-technical-atom-8672457350f9a8ff"></a>

```
const Numbers = Object.assign({
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}, LazyCollection);
const firstCubeOver1234 =
Numbers
.map((x) => x * x * x)
.filter((x) => x > 1234)
.first()
//=> 1331
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-collection]] - shared technical atoms: Collection shares technical record from We'll keep it simple: / Lazy and Eager Collections / lazy collection operations: const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false, value: n++}) } } }, LazyCollection); const firstCubeOver123 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from We'll keep it simple: / Lazy and Eager Collections / lazy collection operations: const Numbers = Object.assign({ [Symbol.iterator]: () => { let n = 0; return { next: () => ({done: false, value: n++}) } } }, LazyCollection); const firstCubeOver123 ... [truncated] (1 shared atom(s))

## Source

- [[javascriptallonge]]
