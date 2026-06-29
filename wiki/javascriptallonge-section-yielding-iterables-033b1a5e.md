---
page_id: javascriptallonge-section-yielding-iterables-033b1a5e
page_kind: source
summary: yielding iterables: 16 source-backed entries and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yielding-iterables-033b1a5e@e528fcacea88ba9554e9a14768ed3cac
---

# yielding iterables

From [[javascriptallonge]].

## Statements

- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-8eb13d6b-01730))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. But if you can write it as a simple generator, write it as a simple generator. _(javascriptallonge.pdf (source-range-8eb13d6b-01731))_
- Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-8eb13d6b-01733))_
- JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping. _(javascriptallonge.pdf (source-range-8eb13d6b-01734))_
- yield* is handy when writing generator functions that operate on or create iterables. _(javascriptallonge.pdf (source-range-8eb13d6b-01745))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-8eb13d6b-01731))_

## Technical atoms

### Technical frame 1: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01730))_

> We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01729))_

```
const isIterable = (something) => !!something[Symbol.iterator]; const TreeIterable = (iterable) => ({ [Symbol.iterator]: function * () { for ( const e of iterable) { if (isIterable(e)) { for ( const ee of TreeIterable(e)) { yield ee; } } else { yield e; } } } }) for ( const i of TreeIterable([1, [2, [3, 4], 5]])) { console.log(i); } //=> 1 2 3 4 5
```

### Technical frame 2: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01733))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01731))_

> But if you can write it as a simple generator, write it as a simple generator.

### Technical frame 3: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01733))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01732))_

```
function * tree (iterable) { for ( const e of iterable) { if (isIterable(e)) { for ( const ee of tree(e)) { yield ee; } } else { yield e; } } }; for ( const i of tree([1, [2, [3, 4], 5]])) { console.log(i); } //=> 1 2 3 4 5
```

### Technical frame 4: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01734))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01736))_

```
for ( const ee of tree(e)) { yield ee; }
```

### Technical frame 5: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01745))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01738))_

```
function * append (...iterables) { for ( const iterable of iterables) { for ( const element of iterable) { yield element; } } } const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\ "]); for ( const word of lyrics) { console.log(word); } //=> a b c one two three do re me
```

### Technical frame 6: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01745))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01741))_

```
function * append (...iterables) { for ( const iterable of iterables) { yield * iterable; } } const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\ "]); for ( const word of lyrics) { console.log(word); }
```

### Technical frame 7: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01745))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01742))_

```
//=> a b c one two do re
```

### Technical frame 8: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01745))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01743))_

```
const isIterable = (something) => !!something[Symbol.iterator]; function * tree (iterable) { for ( const e of iterable) { if (isIterable(e)) { yield * tree(e); } else { yield e; } } }; for ( const i of console.log(i); } //=> 1 2 3 4 5
```

### Technical frame 9: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01745))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01744))_

```
three me yield * yields all of the elements of an iterable, in order. We can use it in tree , too: tree([1, [2, [3, 4], 5]])) {
```
