---
page_id: javascriptallonge-section-backwardness-9f328804
page_kind: source
summary: **backwardness**: 12 source-backed entries and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-backwardness-9f328804@1ae2ee5c3290f27fb67c100cebe00d91
---

# **backwardness**

From [[javascriptallonge]].

## Statements

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-83ecb080-02076))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-83ecb080-02085))_
- So if we wanted to use them with a two-element array, we’d need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-83ecb080-02086))_
- Our latin data structure is no longer a dumb data structure, it’s a function. _(javascriptallonge.pdf (source-range-83ecb080-02093))_

## Technical atoms

> Context: Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we’d write them like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02076))_

> **const** first = ([first, second]) => first, second = ([first, second]) => second;
_(source: javascriptallonge.pdf (source-range-83ecb080-02079))_

> **const** latin = ["primus", "secundus"];
_(source: javascriptallonge.pdf (source-range-83ecb080-02080))_

> first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02081))_

> Context: Or if we were using a POJO, we’d write them like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02082))_

> **const** first = ({first, second}) => first, second = ({first, second}) => second; **const** latin = {first: "primus", second: "secundus"};
_(source: javascriptallonge.pdf (source-range-83ecb080-02083))_

> Context: Or if we were using a POJO, we’d write them like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-02082))_

> first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02084))_

> **const** first = K, second = K(I);
_(source: javascriptallonge.pdf (source-range-83ecb080-02088))_

> **const** latin = (selector) => selector("primus")("secundus");
_(source: javascriptallonge.pdf (source-range-83ecb080-02089))_

> latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02090))_
