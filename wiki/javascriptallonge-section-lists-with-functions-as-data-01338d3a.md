---
page_id: javascriptallonge-section-lists-with-functions-as-data-01338d3a
page_kind: source
summary: **lists with functions as data**: 10 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-lists-with-functions-as-data-01338d3a@6cb729b495c9067ea29a262a9f23aaec
---

# **lists with functions as data**

From [[javascriptallonge]].

## Statements

- Here’s another look at linked lists using POJOs. _(javascriptallonge.pdf (source-range-83ecb080-02117))_
- reverse(delayed) : mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed)); _(javascriptallonge.pdf (source-range-83ecb080-02124))_
- We write them in a backwards way, but they seem to work. _(javascriptallonge.pdf (source-range-83ecb080-02131))_
- And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-02133))_
- Presto, **we can use pure functions to represent a linked list** . _(javascriptallonge.pdf (source-range-83ecb080-02133))_
- We used functions to replace arrays and POJOs, but we still use JavaScript’s built-in operators to test for equality (===) and to branch ?:. _(javascriptallonge.pdf (source-range-83ecb080-02137))_

## Technical atoms

> Context: We can write length and mapWith functions over it:
_(context: javascriptallonge.pdf (source-range-83ecb080-02119))_

> **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair));
_(source: javascriptallonge.pdf (source-range-83ecb080-02122))_

> length(l123) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-02123))_

> **const** doubled = mapWith((x) => x * 2, l123); first(doubled) _//=> 2_ first(rest(doubled)) _//=> 4_ first(rest(rest(doubled))) _//=> 6_
_(source: javascriptallonge.pdf (source-range-83ecb080-02125))_

> Context: Can we do the same with the linked lists we build out of functions? Yes:
_(context: javascriptallonge.pdf (source-range-83ecb080-02126))_

> **const** first = K, rest = K(I), pair = V, EMPTY = (() => {}); **const** l123 = pair(1)(pair(2)(pair(3)(EMPTY))); l123(first) _//=> 1_ l123(rest)(first)
_(source: javascriptallonge.pdf (source-range-83ecb080-02127))_
