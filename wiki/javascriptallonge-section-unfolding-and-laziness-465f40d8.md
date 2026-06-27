---
page_id: javascriptallonge-section-unfolding-and-laziness-465f40d8
page_kind: source
summary: **unfolding and laziness**: 17 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-unfolding-and-laziness-465f40d8@d38ae391c0e8f8190766f018b0c0e3f1
---

# **unfolding and laziness**

From [[javascriptallonge]].

## Statements

- When they iterate over an array or linked list, they are traversing something that is already there. _(javascriptallonge.pdf (source-range-83ecb080-01987))_
- A function that starts with a seed and expands it into a data structure is called an _unfold_ . _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- It’s possible to write a generic unfold mechanism, but let’s pass on to what we can do with unfolded iterators. _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- A function that starts with a seed and expands it into a data structure is called an _unfold_ . _(javascriptallonge.pdf (source-range-83ecb080-01995))_
- This business of going on forever has some drawbacks. _(javascriptallonge.pdf (source-range-83ecb080-02001))_
- We can start with take, an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-83ecb080-02001))_
- We can start with take, an easy function that returns an iterator that only returns a fixed number of elements: _(javascriptallonge.pdf (source-range-83ecb080-02001))_
- We’ll need an iterator that produces odd numbers. _(javascriptallonge.pdf (source-range-83ecb080-02003))_
- We could also write a filter for iterators to accompany our mapping function: _(javascriptallonge.pdf (source-range-83ecb080-02009))_
- Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions. _(javascriptallonge.pdf (source-range-83ecb080-02013))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01987))_

> Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01988))_

> **const** NumberIterator = (number = 0) => () => ({ done: **false** , value: number++ })

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01987))_

> Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01989))_

> fromOne = NumberIterator(1);

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01987))_

> Iterators are functions. When they iterate over an array or linked list, they are traversing something that is already there. But they could just as easily manufacture the data as they go. Let’s consider the simplest example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01990))_

> fromOne().value; _//=> 1_ fromOne().value; _//=> 2_ fromOne().value; _//=> 3_ fromOne().value; _//=> 4_ fromOne().value; _//=> 5_

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02007))_

> **const** squareOf = callLeft(mapIteratorWith, (x) => x * x)

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02008))_

> toArray(take(squareOf(odds()), 5)) _//=> [1, 9, 25, 49, 81]_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02009))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02011))_

> **const** oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02009))_

> We could also write a filter for iterators to accompany our mapping function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02012))_

> toArray(take(squareOf(oddsOf(NumberIterator(1))), 5)) _//=> [1, 9, 25, 49, 81]_
