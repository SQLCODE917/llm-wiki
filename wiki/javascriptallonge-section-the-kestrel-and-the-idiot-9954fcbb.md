---
page_id: javascriptallonge-section-the-kestrel-and-the-idiot-9954fcbb
page_kind: source
summary: **the kestrel and the idiot**: 19 source-backed entries and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-kestrel-and-the-idiot-9954fcbb@2102d613e836436f46edcb631029fe12
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

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02053))_

> **const** K = (x) => (y) => x; **const** fortyTwo = K(42);

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02054))_

> fortyTwo(6) _//=> 42_

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02055))_

> fortyTwo("Hello") _//=> 42_

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02058))_

> K(6)(7) _//=> 6_

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02059))_

> K(12)(24) _//=> 12_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02061))_

> Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02062))_

> Therefore, K(I)(x)(y) => y:

### Technical atom 7

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02065))_

> K(I)(6)(7) _//=> 7_

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02066))_

> K(I)(12)(24) _//=> 24_

### Technical atom 9

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02068))_

> K("primus")("secundus") _//=> "primus"_

### Technical atom 10

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02069))_

> K(I)("primus")("secundus") _//=> "secundus"_

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02070))_

> If we are not feeling particularly academic, we can name our functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02071))_

> **const** first = K, second = K(I);

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02070))_

> If we are not feeling particularly academic, we can name our functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02072))_

> first("primus")("secundus") _//=> "primus"_

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02070))_

> If we are not feeling particularly academic, we can name our functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02073))_

> second("primus")("secundus") _//=> "secundus"_
