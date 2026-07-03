---
page_id: javascriptallonge-recipe-yielding-iterables
page_kind: recipe
page_family: recipe-pattern
summary: yielding iterables: reusable source-backed pattern with 5 statement(s) and 8 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: yielding-iterables
projection_coverage: recipe-javascriptallonge-recipe-yielding-iterables@e929e8188128584084c31c1f369f32ee
---

# yielding iterables

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-we-ll-keep-it-simple-yielding-iterables-d9572ca8]].
- Evidence roles: decision, constraint, explanation, example, structured-state.

## Applicability And Rationale

- It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-7239e085-01731))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-7239e085-01732))_
- Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. _(javascriptallonge.pdf (source-range-7239e085-01734))_
- If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-7239e085-01734))_
- This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping. _(javascriptallonge.pdf (source-range-7239e085-01735))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01730)_

```
const isIterable = (something) =>
!!something[Symbol.iterator];
const TreeIterable = (iterable) =>
({
[Symbol.iterator]: function * () {
for (const e of iterable) {
if (isIterable(e)) {
for (const ee of TreeIterable(e)) {
yield ee;
}
}
else {
yield e;
}
}
}
})
for (const i of TreeIterable([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01733)_

```
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
for (const ee of tree(e)) {
yield ee;
}
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01737)_

```
for (const ee of tree(e)) {
yield ee;
}
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01739)_

```
function * append (...iterables) {
for (const iterable of iterables) {
for (const element of iterable) {
yield element;
}
}
}
const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\
"]);
for (const word of lyrics) {
console.log(word);
}
//=>
a
b
c
one
two
three
do
re
me
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01742)_

```
function * append (...iterables) {
for (const iterable of iterables) {
yield * iterable;
}
}
const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\
"]);
for (const word of lyrics) {
console.log(word);
}
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-01743)_

```
//=>
a
b
c
one
two
thre
do
re
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-we-ll-keep-it-simple-yielding-iterables-d9572ca8]]
