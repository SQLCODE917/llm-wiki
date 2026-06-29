---
page_id: javascriptallonge-section-bonus-534c91a7
page_kind: source
summary: bonus: 10 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-bonus-534c91a7@c682e3b0391ae6798068904648c1e228
---

# bonus

From [[javascriptallonge]].

## Statements

- Many programmers coming to JavaScript from other languages are familiar with three 'canonical' operations on collections: folding, filtering, and finding. In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-8eb13d6b-01315))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: _(javascriptallonge.pdf (source-range-8eb13d6b-01318))_
- JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-8eb13d6b-01320))_
- In Smalltalk, for example, they are known as collect , select , and detect . _(javascriptallonge.pdf (source-range-8eb13d6b-01315))_
- This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-8eb13d6b-01318))_

## Technical atoms

### Technical frame 1: bonus

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01318))_

> This is interesting, because it is lazy: It doesn't apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01317))_

```
const firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);
```

### Technical frame 2: bonus

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01320))_

> JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01319))_

```
const firstInArray = (fn, array) => array.filter(fn)[0];
```
