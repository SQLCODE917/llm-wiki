---
page_id: javascriptallonge-section-yielding-iterables-c38f7cd6
page_kind: source
summary: yielding iterables: 16 source-backed entries and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yielding-iterables-c38f7cd6@d578f810cd5ce023e5a3622c7315783c
---

# yielding iterables

From [[javascriptallonge]].

## Statements

- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-31a4cf47-01732))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. But if you can write it as a simple generator, write it as a simple generator. _(javascriptallonge.pdf (source-range-31a4cf47-01733))_
- Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-31a4cf47-01735))_
- JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping. _(javascriptallonge.pdf (source-range-31a4cf47-01736))_
- yield* is handy when writing generator functions that operate on or create iterables. _(javascriptallonge.pdf (source-range-31a4cf47-01747))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-31a4cf47-01733))_

## Technical atoms

### Technical frame 1: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01732))_

> We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01731))_

```
const isIterable = (something) => !!something[Symbol.iterator]; const TreeIterable = (iterable) => ({ [Symbol.iterator]: function * () { for ( const e of iterable) { if (isIterable(e)) { for ( const ee of TreeIterable(e)) { yield ee; } } else { yield e; } } } }) for ( const i of TreeIterable([1, [2, [3, 4], 5]])) { console.log(i); } //=> 1 2 3 4 5
```

### Technical frame 2: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01735))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01733))_

> But if you can write it as a simple generator, write it as a simple generator.

### Technical frame 3: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01735))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01734))_

```
function * tree (iterable) { for ( const e of iterable) { if (isIterable(e)) { for ( const ee of tree(e)) { yield ee; } } else { yield e; } } }; for ( const i of tree([1, [2, [3, 4], 5]])) { console.log(i); } //=> 1 2 3 4 5
```

### Technical frame 4: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01736))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01738))_

```
for ( const ee of tree(e)) { yield ee; }
```

### Technical frame 5: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01747))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01740))_

```
function * append (...iterables) { for ( const iterable of iterables) { for ( const element of iterable) { yield element; } } } const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\ "]); for ( const word of lyrics) { console.log(word); } //=> a b c one two three do re me
```

### Technical frame 6: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01747))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01743))_

```
function * append (...iterables) { for ( const iterable of iterables) { yield * iterable; } } const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\ "]); for ( const word of lyrics) { console.log(word); }
```

### Technical frame 7: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01747))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01744))_

```
//=> a b c one two do re
```

### Technical frame 8: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01747))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01745))_

```
const isIterable = (something) => !!something[Symbol.iterator]; function * tree (iterable) { for ( const e of iterable) { if (isIterable(e)) { yield * tree(e); } else { yield e; } } }; for ( const i of console.log(i); } //=> 1 2 3 4 5
```

### Technical frame 9: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01747))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01746))_

```
three me yield * yields all of the elements of an iterable, in order. We can use it in tree , too: tree([1, [2, [3, 4], 5]])) {
```
