---
page_id: javascriptallonge-section-that-constant-coffee-craving-cf333dea
page_kind: source
summary: **That Constant Coffee Craving**: 16 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-that-constant-coffee-craving-cf333dea@2b95fb970a2d5fe9e3c3ec9921bbabe6
---

# **That Constant Coffee Craving**

From [[javascriptallonge]].

## Statements

- Up to now, all we’ve really seen are _anonymous functions_ , functions that don’t have a name. _(javascriptallonge.pdf (source-range-83ecb080-00543))_
- This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. _(javascriptallonge.pdf (source-range-83ecb080-00543))_
- Naming things is a critical part of programming, but all we’ve seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-83ecb080-00543))_
- In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. _(javascriptallonge.pdf (source-range-83ecb080-00548))_
- This one has a few more moving parts, that’s all. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- But we can use it just like (diameter) => diameter * 3.14159265. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- This expression, when evaluated, returns a function that calculates circumferences. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- All of our “functions” are expressions. _(javascriptallonge.pdf (source-range-83ecb080-00552))_
- We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind.[29] _(javascriptallonge.pdf (source-range-83ecb080-00559))_

## Technical atoms

> There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. Let’s revisit a very simple example:
_(source: javascriptallonge.pdf (source-range-83ecb080-00544))_

> Context: There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. Let’s revisit a very simple example:
_(context: javascriptallonge.pdf (source-range-83ecb080-00544))_

> (diameter) => diameter * 3.14159265
_(source: javascriptallonge.pdf (source-range-83ecb080-00545))_

> Context: What is this “3.14159265” number? PI[28] , obviously. We’d like to name it so that we can write something like:
_(context: javascriptallonge.pdf (source-range-83ecb080-00546))_

> (diameter) => diameter * PI
_(source: javascriptallonge.pdf (source-range-83ecb080-00547))_

> Context: In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. If we put our function expression in parentheses, we can apply it to the argument of 3.14159265:
_(context: javascriptallonge.pdf (source-range-83ecb080-00548))_

> ((PI) => _// ????_ )(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00549))_

> Context: What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course:
_(context: javascriptallonge.pdf (source-range-83ecb080-00550))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)
_(source: javascriptallonge.pdf (source-range-83ecb080-00551))_

> ((diameter) => diameter * 3.14159265)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00557))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)(2) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00558))_
