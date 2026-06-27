---
page_id: javascriptallonge-section-gathering-8df97cbb
page_kind: source
summary: **gathering**: 14 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-gathering-8df97cbb@dc3d2c5723762a2b65a8e5288b886cc6
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

> Context: Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:
_(context: javascriptallonge.pdf (source-range-83ecb080-01242))_

> **const** [car, ...cdr] = [1, 2, 3, 4, 5];
_(source: javascriptallonge.pdf (source-range-83ecb080-01243))_

> Context: Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array:
_(context: javascriptallonge.pdf (source-range-83ecb080-01242))_

> car _//=> 1_ cdr _//=> [2, 3, 4, 5]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01244))_

> **const** [...butLast, last] = [1, 2, 3, 4, 5]; _//=> ERROR_ **const** [first, ..., last] = [1, 2, 3, 4, 5]; _//=> ERROR_
_(source: javascriptallonge.pdf (source-range-83ecb080-01251))_

> **const** wrapped = [something];
_(source: javascriptallonge.pdf (source-range-83ecb080-01253))_

> **const** [unwrapped] = something;
_(source: javascriptallonge.pdf (source-range-83ecb080-01255))_

> Context: What is the reverse of gathering? We know that:
_(context: javascriptallonge.pdf (source-range-83ecb080-01256))_

> **const** [car, ...cdr] = [1, 2, 3, 4, 5];
_(source: javascriptallonge.pdf (source-range-83ecb080-01257))_

> Context: What is the reverse? It would be:
_(context: javascriptallonge.pdf (source-range-83ecb080-01258))_

> **const** cons = [car, ...cdr];
_(source: javascriptallonge.pdf (source-range-83ecb080-01259))_

> **const** oneTwoThree = ["one", "two", "three"]; ["zero", ...oneTwoThree] _//=> ["zero","one","two","three"]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01261))_
