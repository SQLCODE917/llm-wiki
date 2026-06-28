---
page_id: javascriptallonge-section-once-60aa50ef
page_kind: source
summary: Once: 3 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-once-60aa50ef@312c80630f10c2640ecac17f9b9f26cc
---

# Once

From [[javascriptallonge]].

## Statements

- Recipes with Basic Functions

65

## **Once**

once is an extremely helpful combinator. It ensures that a function can only be called, well, _once_ . Here’s the recipe: **const** once = (fn) => { **let** done = **false** ; **return function** () { **return** done ? **void** 0 : ((done = **true** ), fn.apply( **this** , arguments)) } } Very simple! You pass it a function, and you get a function back. That function will call your function once, and thereafter will return undefined whenever it is called. Let’s try it: **const** askedOnBlindDate = once( () => "sure, why not?" ); askedOnBlindDate() _//=> 'sure, why not?'_

askedOnBlindDate() _//=> undefined_ askedOnBlindDate() _//=> undefined_

It seems some people will only try blind dating once.

(Note: There are some subtleties with decorators like once that involve the intersection of state with methods. We’ll look at that again in stateful method decorators.) _(javascriptallonge.pdf (source-range-83ecb080-00111))_
- It ensures that a function can only be called, well, _once_ . _(javascriptallonge.pdf (source-range-83ecb080-00111))_
