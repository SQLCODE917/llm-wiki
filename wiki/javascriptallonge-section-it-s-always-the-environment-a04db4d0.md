---
page_id: javascriptallonge-section-it-s-always-the-environment-a04db4d0
page_kind: source
summary: it's always the environment: 15 source-backed entries and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-it-s-always-the-environment-a04db4d0@98a6bf7a8f21c16b64a6442a6d59e127
---

# it's always the environment

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-environment]] - topic hub: opens the topic page for Environment

## Statements

- To understand how closures are evaluated, we need to revisit environments. As we've said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...} ? Let's fill in the blanks! _(javascriptallonge.pdf (source-range-8eb13d6b-00358))_
- (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20 _(javascriptallonge.pdf (source-range-8eb13d6b-00361))_
- Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) . _(javascriptallonge.pdf (source-range-8eb13d6b-00368))_
- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-8eb13d6b-00369))_
- As we've said before, all functions are associated with an environment. _(javascriptallonge.pdf (source-range-8eb13d6b-00358))_
- Calling a curried function with only some of its arguments is sometimes called partial application b . _(javascriptallonge.pdf (source-range-8eb13d6b-00369))_

## Technical atoms

### Technical frame 1: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00361))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00359))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical frame 2: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00368))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00363))_

```
b
```

### Technical frame 3: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00368))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00365))_

```
(x) => (y) => (z) => x + y + z
```

### Technical frame 4: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00368))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00367))_

```
(x, y, z) => x + y + z
```

### Technical frame 5: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00369))_

> The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00370))_

```
a b
```
