---
page_id: javascriptallonge-recipe-lazy-collection-operations
page_kind: recipe
page_family: recipe-pattern
summary: lazy collection operations: reusable source-backed pattern with 10 statement(s) and 5 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: lazy-collection-operations
projection_coverage: recipe-javascriptallonge-recipe-lazy-collection-operations@c0ebaa1fcaa7558d52df154b77bfd3c6
---

# lazy collection operations

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-lazy-collection-operations-547c7c28]].
- Evidence roles: decision, constraint, explanation, procedure, example, structured-state.

## Applicability And Rationale

- But it can be an excellent strategy for efficiency in algorithms. _(javascriptallonge.pdf (source-range-7239e085-01783))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-7239e085-01786))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-7239e085-01787))_
- They produce small iterable objects that refer back to the original iteration. _(javascriptallonge.pdf (source-range-7239e085-01788))_
- Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-7239e085-01791))_
- This expression begins with a stack containing 30 elements. _(javascriptallonge.pdf (source-range-7239e085-01791))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01785)_

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01790)_

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01794)_

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => {
console.log(`squaring ${x}`);
return x * x
})
.filter((x) => {
console.log(`filtering ${x}`);
return x % 2 == 0
})
.first()
//=>
squaring 29
filtering 841
squaring 28
filtering 784
784
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01796)_

```
[ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
.reverse()
.map((x) => {
console.log(`squaring ${x}`);
return x * x
})
.filter((x) => {
console.log(`filtering ${x}`);
return x % 2 == 0
})[0]
//=>
squaring 0
squaring 1
squaring 2
squaring 3
...
squaring 28
squaring 29
filtering 0
filtering 1
filtering 4
...
filtering 784
filtering 841
784
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01799)_

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

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-lazy-collection-operations-547c7c28]]
