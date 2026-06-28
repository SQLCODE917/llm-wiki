---
page_id: javascriptallonge-section-tap-e0f40210
page_kind: source
summary: Tap: 3 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-tap-e0f40210@f6ec9f1797ab7b429f5c93faff383a2b
---

# Tap

From [[javascriptallonge]].

## Statements

- Recipes with Basic Functions

61

## **Tap**

One of the most basic combinators is the “K Combinator,” nicknamed the “Kestrel:” **const** K = (x) => (y) => x;

It has some surprising applications. One is when you want to do something with a value for sideeffects, but keep the value around. Behold: **const** tap = (value) => (fn) => ( **typeof** (fn) === 'function' && fn(value), value ) tap is a traditional name borrowed from various Unix shell commands. It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. Let’s see it in action as a poor-man’s debugger: tap('espresso')((it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso'

It’s easy to turn off: tap('espresso')(); _//=> 'espresso'_

Libraries like Underscore[49] use a version of tap that is “uncurried:” _.tap('espresso', (it) => console.log(`Our drink is ' **${** it **}** '`) ); _//=> Our drink is 'espresso'_ 'espresso'

Let’s enhance our recipe so that it works both ways:

> 49http://underscorejs.org _(javascriptallonge.pdf (source-range-83ecb080-00105))_
- Recipes with Basic Functions

62 **const** tap = (value, fn) => { **const** curried = (fn) => ( **typeof** (fn) === 'function' && fn(value), value ); **return** fn === **undefined** ? curried : curried(fn); } Now we can write: tap('espresso')((it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso' Or: tap('espresso', (it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso' And if we wish it to do nothing at all, We can write either tap('espresso')() or tap('espresso', null) p.s. tap can do more than just act as a debugging aid. It’s also useful for working with object and instance methods. _(javascriptallonge.pdf (source-range-83ecb080-00106))_
