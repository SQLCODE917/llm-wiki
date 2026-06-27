---
page_id: javascriptallonge-magic
page_kind: concept
summary: Magic Names: 26 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-magic@ea6f319a111e5d68705792fe9ef3eb12
---

# Magic Names

What [[javascriptallonge]] covers about magic names:

## Statements

- The second magic name is very interesting, it’s called arguments, and the most interesting thing about it is that it contains a list of arguments passed to a function: _(javascriptallonge.pdf (source-range-83ecb080-00866))_
- The first magic name is this, and it is bound to something called the function’s context. _(javascriptallonge.pdf (source-range-83ecb080-00866))_
- Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-00898))_
- What we haven’t discussed so far is that JavaScript also binds values to some “magic” names in addition to any you put in the argument list.[42] _(javascriptallonge.pdf (source-range-83ecb080-00863))_
- There are two separate rules for these “magic” names, one for when you invoke a function using the function keyword, and another for functions defined with “fat arrows.” We’ll begin with how things work for functions defined with the function keyword. _(javascriptallonge.pdf (source-range-83ecb080-00865))_
- > 42You should never attempt to define your own bindings against “magic” names that JavaScript binds for you. _(javascriptallonge.pdf (source-range-83ecb080-00871))_
- This works just fine, because arguments[0] refers to the 3 we passed to the function row. _(javascriptallonge.pdf (source-range-83ecb080-00890))_
- For example, when this expression’s inner function is defined with function, arguments[0] refers to its only argument, "inner": _(javascriptallonge.pdf (source-range-83ecb080-00881))_
- When a function is applied to arguments (or “called”), JavaScript binds the values of arguments to the function’s argument names in an environment created for the function’s execution. _(javascriptallonge.pdf (source-range-83ecb080-00863))_
- arguments always contains all of the arguments passed to a function, regardless of how many are declared. _(javascriptallonge.pdf (source-range-83ecb080-00870))_
- It is wise to treat them as read-only at all times. _(javascriptallonge.pdf (source-range-83ecb080-00871))_
- The most common use of the arguments binding is to build functions that can take a variable number of arguments. _(javascriptallonge.pdf (source-range-83ecb080-00878))_
- We’ll see it used in many of the recipes, starting off with partial application and ellipses. _(javascriptallonge.pdf (source-range-83ecb080-00878))_
- But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function. _(javascriptallonge.pdf (source-range-83ecb080-00885))_

## Technical atoms

> Context: The first magic name is this, and it is bound to something called the function’s context. We will explore this in more detail when we start discussing objects and classes. The second magic name is very interesting, it’s called arguments, and the most interesting thing about it is that it contains a list of arguments passed to a function:
_(context: javascriptallonge.pdf (source-range-83ecb080-00866))_

> **const** plus = **function** (a, b) { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_
_(source: javascriptallonge.pdf (source-range-83ecb080-00867))_

> Context: Although arguments looks like an array, it isn’t an array: It’s more like an object[43] that happens to bind some values to properties with names that look like integers starting with zero: arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00868, source-range-83ecb080-00870))_

> **const** args = **function** (a, b) { **return** arguments; } args(2,3) _//=> { '0': 2, '1': 3 }_
_(source: javascriptallonge.pdf (source-range-83ecb080-00869))_

> **const** plus = **function** () { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_
_(source: javascriptallonge.pdf (source-range-83ecb080-00875))_

> Context: When discussing objects, we’ll discuss properties in more depth. Here’s something interesting about arguments:
_(context: javascriptallonge.pdf (source-range-83ecb080-00876))_

> **const** howMany = **function** () { **return** arguments['length']; } howMany() _//=> 0_ howMany('hello') _//=> 1_ howMany('sharks', 'are', 'apex', 'predators') _//=> 4_
_(source: javascriptallonge.pdf (source-range-83ecb080-00877))_

> Context: But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function. And thus arguments[0] will refer to "outer", not to "inner":
_(context: javascriptallonge.pdf (source-range-83ecb080-00885))_

> ( **function** () { **return** (() => arguments[0])('inner'); })('outer') _//=> "outer"_
_(source: javascriptallonge.pdf (source-range-83ecb080-00886))_


## Source

- [[javascriptallonge]]
