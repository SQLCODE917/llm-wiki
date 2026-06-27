---
page_id: javascriptallonge-section-bonus-fb3c09bf
page_kind: source
summary: **bonus**: 10 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-bonus-fb3c09bf@38c30af73b140867b066289674957043
---

# **bonus**

From [[javascriptallonge]].

## Statements

- In Smalltalk, for example, they are known as collect, select, and detect. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- Many programmers coming to JavaScript from other languages are familiar with three “canonical” operations on collections: folding, filtering, and finding. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- In Smalltalk, for example, they are known as collect, select, and detect. _(javascriptallonge.pdf (source-range-83ecb080-02015))_
- This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-83ecb080-02020))_
- This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. _(javascriptallonge.pdf (source-range-83ecb080-02020))_
- And if fn had some sort of side-effect, the program could be buggy. _(javascriptallonge.pdf (source-range-83ecb080-02022))_
- JavaScript would apply fn to every element. _(javascriptallonge.pdf (source-range-83ecb080-02022))_
- If array was very large, and fn very slow, this would consume a lot of unnecessary time. _(javascriptallonge.pdf (source-range-83ecb080-02022))_

## Technical atoms

> Context: This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02020))_

> **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-02019))_

> Context: This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-02020))_

> **const** firstInArray = (fn, array) => array.filter(fn)[0];
_(source: javascriptallonge.pdf (source-range-83ecb080-02021))_
