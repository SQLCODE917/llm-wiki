---
page_id: javascriptallonge-section-the-kestrel-and-the-idiot-9954fcbb
page_kind: source
summary: **the kestrel and the idiot**: 19 source-backed entries and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-kestrel-and-the-idiot-9954fcbb@0c67ab4b8f0ac3f4d2048f21d9d93194
---

# **the kestrel and the idiot**

From [[javascriptallonge]].

## Statements

- You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- The kestrel, or K, is a function that makes constant functions. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- A _constant function_ is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- The _identity function_ is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-83ecb080-02056))_
- Given two values, we can say that K always returns the _first_ value: K(x)(y) => x (that’s not valid JavaScript, but it’s essentially how it works). _(javascriptallonge.pdf (source-range-83ecb080-02060))_
- Given two values, we can say that K always returns the _first_ value, and given two values, K(I) always returns the _second_ value. _(javascriptallonge.pdf (source-range-83ecb080-02074))_

## Technical atoms

> **const** K = (x) => (y) => x; **const** fortyTwo = K(42);
_(source: javascriptallonge.pdf (source-range-83ecb080-02053))_

> fortyTwo(6) _//=> 42_
_(source: javascriptallonge.pdf (source-range-83ecb080-02054))_

> fortyTwo("Hello") _//=> 42_
_(source: javascriptallonge.pdf (source-range-83ecb080-02055))_

> K(6)(7) _//=> 6_
_(source: javascriptallonge.pdf (source-range-83ecb080-02058))_

> K(12)(24) _//=> 12_
_(source: javascriptallonge.pdf (source-range-83ecb080-02059))_

> Context: Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.
_(context: javascriptallonge.pdf (source-range-83ecb080-02061))_

> Therefore, K(I)(x)(y) => y:
_(source: javascriptallonge.pdf (source-range-83ecb080-02062))_

> K(I)(6)(7) _//=> 7_
_(source: javascriptallonge.pdf (source-range-83ecb080-02065))_

> K(I)(12)(24) _//=> 24_
_(source: javascriptallonge.pdf (source-range-83ecb080-02066))_

> K("primus")("secundus") _//=> "primus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02068))_

> K(I)("primus")("secundus") _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02069))_

> Context: If we are not feeling particularly academic, we can name our functions:
_(context: javascriptallonge.pdf (source-range-83ecb080-02070))_

> **const** first = K, second = K(I);
_(source: javascriptallonge.pdf (source-range-83ecb080-02071))_

> Context: If we are not feeling particularly academic, we can name our functions:
_(context: javascriptallonge.pdf (source-range-83ecb080-02070))_

> first("primus")("secundus") _//=> "primus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02072))_

> Context: If we are not feeling particularly academic, we can name our functions:
_(context: javascriptallonge.pdf (source-range-83ecb080-02070))_

> second("primus")("secundus") _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02073))_
