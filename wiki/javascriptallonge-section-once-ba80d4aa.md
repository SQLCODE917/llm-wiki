---
page_id: javascriptallonge-section-once-ba80d4aa
page_kind: source
summary: **Once**: 6 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-once-ba80d4aa@6aa9e3dc97eb1c640484d5949ae6bea6
---

# **Once**

From [[javascriptallonge]].

## Statements

- It ensures that a function can only be called, well, _once_ . _(javascriptallonge.pdf (source-range-83ecb080-01026))_
- once is an extremely helpful combinator. _(javascriptallonge.pdf (source-range-83ecb080-01026))_
- It ensures that a function can only be called, well, _once_ . _(javascriptallonge.pdf (source-range-83ecb080-01026))_
- (Note: There are some subtleties with decorators like once that involve the intersection of state with methods. _(javascriptallonge.pdf (source-range-83ecb080-01034))_

## Technical atoms

> Context: Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let’s try it:
_(context: javascriptallonge.pdf (source-range-83ecb080-01028))_

> **const** askedOnBlindDate = once( () => "sure, why not?" ); askedOnBlindDate() _//=> 'sure, why not?'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01029))_

> Context: Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let’s try it:
_(context: javascriptallonge.pdf (source-range-83ecb080-01028))_

> askedOnBlindDate() _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-01030))_
