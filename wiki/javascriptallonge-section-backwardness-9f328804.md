---
page_id: javascriptallonge-section-backwardness-9f328804
page_kind: source
summary: **backwardness**: 12 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-backwardness-9f328804@c48e2bec644643da0d2126d12dde7978
---

# **backwardness**

From [[javascriptallonge]].

## Statements

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-83ecb080-02076))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-83ecb080-02085))_
- So if we wanted to use them with a two-element array, we’d need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-83ecb080-02086))_
- Our latin data structure is no longer a dumb data structure, it’s a function. _(javascriptallonge.pdf (source-range-83ecb080-02093))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02076))_

> Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we’d write them like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02079))_

> **const** first = ([first, second]) => first, second = ([first, second]) => second;

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02080))_

> **const** latin = ["primus", "secundus"];

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02081))_

> first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02082))_

> Or if we were using a POJO, we’d write them like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02083))_

> **const** first = ({first, second}) => first, second = ({first, second}) => second; **const** latin = {first: "primus", second: "secundus"};

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02082))_

> Or if we were using a POJO, we’d write them like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02084))_

> first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02088))_

> **const** first = K, second = K(I);

### Technical atom 7

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02089))_

> **const** latin = (selector) => selector("primus")("secundus");

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02090))_

> latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_
