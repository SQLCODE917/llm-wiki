---
page_id: javascriptallonge-section-tap-ab5bb031
page_kind: source
page_family: section-reference
summary: Tap: 3 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-tap-ab5bb031@7d0742c2cb56c041b3c70c3d435e389c
---

# Tap

From [[javascriptallonge]].

## Statements

- Recipes with Basic Functions 

61 

## **Tap** 

One of the most basic combinators is the “K Combinator,” nicknamed the “Kestrel:” 

**const** K = (x) => (y) => x; 

It has some surprising applications. One is when you want to do something with a value for sideeffects, but keep the value around. Behold: 

**const** tap = (value) => (fn) => ( **typeof** (fn) === 'function' && fn(value), value ) 

tap is a traditional name borrowed from various Unix shell commands. It takes a value and returns a function that always returns the value, but if you pass it a function, it executes the function for side-effects. Let’s see it in action as a poor-man’s debugger: 

tap('espresso')((it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso' 

It’s easy to turn off: 

tap('espresso')(); _//=> 'espresso'_ 

Libraries like Underscore[49] use a version of tap that is “uncurried:” 

_.tap('espresso', (it) => console.log(`Our drink is ' **${** it **}** '`) ); _//=> Our drink is 'espresso'_ 'espresso' 

Let’s enhance our recipe so that it works both ways: 

> 49http://underscorejs.org _(javascriptallonge.pdf (source-range-af806fb1-00101))_
- Recipes with Basic Functions 

62 

**const** tap = (value, fn) => { **const** curried = (fn) => ( **typeof** (fn) === 'function' && fn(value), value ); **return** fn === **undefined** ? curried : curried(fn); } 

Now we can write: 

tap('espresso')((it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso' 

Or: 

tap('espresso', (it) => { console.log(`Our drink is ' **${** it **}** '`) }); _//=> Our drink is 'espresso'_ 'espresso' And if we wish it to do nothing at all, We can write either tap('espresso')() or tap('espresso', null) 

p.s. tap can do more than just act as a debugging aid. It’s also useful for working with object and instance methods. _(javascriptallonge.pdf (source-range-af806fb1-00102))_
