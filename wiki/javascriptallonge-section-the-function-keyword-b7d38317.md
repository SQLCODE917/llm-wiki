---
page_id: javascriptallonge-section-the-function-keyword-b7d38317
page_kind: source
summary: **the function keyword**: 13 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-function-keyword-b7d38317@92ca8ab19d7b33a6369106d3e506bc60
---

# **the function keyword**

From [[javascriptallonge]].

## Statements

- There are two separate rules for these “magic” names, one for when you invoke a function using the function keyword, and another for functions defined with “fat arrows.” We’ll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-83ecb080-00865))_
- The second magic name is very interesting, it’s called arguments, and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-83ecb080-00866))_
- The first magic name is this, and it is bound to something called the function’s context. _(javascriptallonge.pdf (source-range-83ecb080-00866))_
- arguments always contains all of the arguments passed to a function, regardless of how many are declared. _(javascriptallonge.pdf (source-range-83ecb080-00870))_
- It is wise to treat them as read-only at all times. _(javascriptallonge.pdf (source-range-83ecb080-00871))_
- > 42You should never attempt to define your own bindings against “magic” names that JavaScript binds for you. _(javascriptallonge.pdf (source-range-83ecb080-00871))_
- It is wise to treat them as read-only at all times. _(javascriptallonge.pdf (source-range-83ecb080-00871))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. _(javascriptallonge.pdf (source-range-83ecb080-00878))_
- We’ll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-83ecb080-00878))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00866))_

> The first magic name is this, and it is bound to something called the function’s context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it’s called arguments, and the most interesting thing about it is that it contains a list of arguments passed to a function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00867))_

> **const** plus = **function** (a, b) { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00868, source-range-83ecb080-00870))_

> Although arguments looks like an array, it isn’t an array: It’s more like an object[43] that happens to bind some values to properties with names that look like integers starting with zero: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00869))_

> **const** args = **function** (a, b) { **return** arguments; } args(2,3) _//=> { '0': 2, '1': 3 }_

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00875))_

> **const** plus = **function** () { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00876))_

> When discussing objects, we’ll discuss properties in more depth. Here’s something interesting about arguments:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00877))_

> **const** howMany = **function** () { **return** arguments['length']; } howMany() _//=> 0_ howMany('hello') _//=> 1_ howMany('sharks', 'are', 'apex', 'predators') _//=> 4_
