---
page_id: javascriptallonge-section-building-blocks-18fa4ba0
page_kind: source
page_family: section-reference
summary: Building Blocks: 27 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-building-blocks-18fa4ba0@96845a70965372be44dc74f179e5bb2c
---

# Building Blocks

From [[javascriptallonge]].

## Statements

- The first sip: Basic Functions 

48 

## **Building Blocks** 

When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. 

## **composition** 

: One of the most basic of these building blocks is _composition_ 

**const** cookAndEat = (food) => eat(cook(food)); 

It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators: 

**const** compose = (a, b) => (c) => a(b(c)); 

**const** cookAndEat = compose(eat, cook); 

If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways. 

In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument. 

Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit: 

- **const** actuallyTransfer= (from, to, amount) => _// do something_ 

**const** invokeTransfer = once(maybe(actuallyTransfer(...))); _(javascriptallonge.pdf (source-range-af806fb1-00082))_
- The first sip: Basic Functions 

49 

## **partial application** 

Another basic building block is _partial application_ . When a function takes multiple arguments, we “apply” the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can’t get the final value, but we can get a function that represents _part_ of our application. 

Code is easier than words for this. The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this: 

_.map([1, 2, 3], (n) => n * n) _//=> [1, 4, 9]_ 

We don’t want to fool around writing _., so we can use it by writing:[41] 

This code implements a partial application of the map function by applying the function (n) => n * n as its second argument: 

**const** squareAll = (array) => map(array, (n) => n * n); 

The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. 

**const** mapWith = (fn) => (array) => map(array, fn); 

**const** squareAll = mapWith((n) => n * n); 

squareAll([1, 2, 3]) _//=> [1, 4, 9]_ 

We’ll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: 

> 39http://underscorejs.org 

> 40Modern JavaScript implementations provide a map method for arrays, but Underscore’s implementation also works with older browsers if you are working with that headache. 

> 41If we don’t want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven’t discussed methods yet. const map = _.map; _(javascriptallonge.pdf (source-range-af806fb1-00083))_
- The first sip: Basic Functions 

50 

**const** safeSquareAll = mapWith(maybe((n) => n * n)); 

safeSquareAll([1, **null** , 2, 3]) 

_//=> [1, null, 4, 9]_ 

We generalized composition with the compose combinator. Partial application also has a combinator, which we’ll see in the partial recipe. _(javascriptallonge.pdf (source-range-af806fb1-00084))_
- In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-af806fb1-00082))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-af806fb1-00082))_
