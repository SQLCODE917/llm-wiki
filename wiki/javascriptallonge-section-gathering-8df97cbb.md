---
page_id: javascriptallonge-section-gathering-8df97cbb
page_kind: source
summary: **gathering**: 14 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-gathering-8df97cbb@02751cf846ede00f056dcc671c4b744a
---

# **gathering**

From [[javascriptallonge]].

## Statements

- Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-83ecb080-01242))_
- Sometimes we need to extract arrays from arrays. _(javascriptallonge.pdf (source-range-83ecb080-01242))_
- car and cdr[57] are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. _(javascriptallonge.pdf (source-range-83ecb080-01245))_
- notation does not provide a universal patten-matching capability. _(javascriptallonge.pdf (source-range-83ecb080-01246))_
- Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals. _(javascriptallonge.pdf (source-range-83ecb080-01252))_
- to place the elements of an array inside another array. _(javascriptallonge.pdf (source-range-83ecb080-01262))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01242))_

> Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01243))_

> **const** [car, ...cdr] = [1, 2, 3, 4, 5];

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01242))_

> Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01244))_

> car _//=> 1_ cdr _//=> [2, 3, 4, 5]_

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01251))_

> **const** [...butLast, last] = [1, 2, 3, 4, 5]; _//=> ERROR_ **const** [first, ..., last] = [1, 2, 3, 4, 5]; _//=> ERROR_

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01253))_

> **const** wrapped = [something];

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01255))_

> **const** [unwrapped] = something;

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01256))_

> What is the reverse of gathering? We know that:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01257))_

> **const** [car, ...cdr] = [1, 2, 3, 4, 5];

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01258))_

> What is the reverse? It would be:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01259))_

> **const** cons = [car, ...cdr];

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01261))_

> **const** oneTwoThree = ["one", "two", "three"]; ["zero", ...oneTwoThree] _//=> ["zero","one","two","three"]_
