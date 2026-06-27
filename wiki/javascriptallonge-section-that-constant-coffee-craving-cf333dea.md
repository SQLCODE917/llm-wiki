---
page_id: javascriptallonge-section-that-constant-coffee-craving-cf333dea
page_kind: source
summary: **That Constant Coffee Craving**: 16 source-backed entries and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-that-constant-coffee-craving-cf333dea@88ae285f55206e2d505bc9fc1ac8540e
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

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00544))_

> There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. Let’s revisit a very simple example:

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00544))_

> There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. Let’s revisit a very simple example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00545))_

> (diameter) => diameter * 3.14159265

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00546))_

> What is this “3.14159265” number? PI[28] , obviously. We’d like to name it so that we can write something like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00547))_

> (diameter) => diameter * PI

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00548))_

> In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. If we put our function expression in parentheses, we can apply it to the argument of 3.14159265:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00549))_

> ((PI) => _// ????_ )(3.14159265)

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00550))_

> What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00551))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00557))_

> ((diameter) => diameter * 3.14159265)(2) _//=> 6.2831853_

### Technical atom 7

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00558))_

> ((PI) => (diameter) => diameter * PI )(3.14159265)(2) _//=> 6.2831853_
