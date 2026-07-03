---
page_id: javascriptallonge-section-we-ll-keep-it-simple-yielding-iterables-d9572ca8
page_kind: source
page_family: section-reference
summary: We'll keep it simple: / yielding iterables: 15 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-yielding-iterables-d9572ca8@db200a196b0a9b08049ccffff28a962d
---

# We'll keep it simple: / yielding iterables

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-ll-keep-it-simple-1104ef0d]] - broader source section: We'll keep it simple:

## Statements

- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-7239e085-01731))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. But if you can write it as a simple generator, write it as a simple generator. _(javascriptallonge.pdf (source-range-7239e085-01732))_
- Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-7239e085-01734))_
- JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping. _(javascriptallonge.pdf (source-range-7239e085-01735))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-7239e085-01732))_

## Technical atoms

### Technical frame 1: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01735))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01742))_

<a id="atom-technical-atom-3f887d1daf7a5385"></a>

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

### Technical frame 2: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01735))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01743))_

<a id="atom-technical-atom-a08bb83e790e552c"></a>

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

### Technical frame 3: We'll keep it simple: / yielding iterables

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01744))_

<a id="atom-technical-atom-aba6cb6873b1bd9a"></a>

```
const isIterable = (something) =>
!!something[Symbol.iterator];
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
yield * tree(e);
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4
console.log(i);
}
//=>
1
2
3
4
5
```
