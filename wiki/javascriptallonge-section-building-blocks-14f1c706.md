---
page_id: javascriptallonge-section-building-blocks-14f1c706
page_kind: source
summary: Building Blocks: 40 source-backed entries and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-building-blocks-14f1c706@0784b7831729a9ed3d5c43011f459641
---

# Building Blocks

From [[javascriptallonge]].

## Statements

- The weakness is that you will. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- There are ifs, fors, returns, everything thrown higgledy piggledy together. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- The strength of JavaScript is that you can do anything. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it. _(javascriptallonge.pdf (source-range-83ecb080-00824))_
- You can compose them with explicit JavaScript code as we’ve just done. _(javascriptallonge.pdf (source-range-83ecb080-00828))_
- It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. _(javascriptallonge.pdf (source-range-83ecb080-00828))_
- If that was all there was to it, composition wouldn’t matter much. _(javascriptallonge.pdf (source-range-83ecb080-00831))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-83ecb080-00831))_
- But like many patterns, using it when it applies is only 20% of the benefit. _(javascriptallonge.pdf (source-range-83ecb080-00831))_
- In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Once is useful for ensuring that certain side effects are not repeated. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- Thereafter, it does nothing. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. _(javascriptallonge.pdf (source-range-83ecb080-00832))_
- But once and maybe compose, so you can chain them together as you see fit: _(javascriptallonge.pdf (source-range-83ecb080-00833))_
- Another basic building block is _partial application_ . _(javascriptallonge.pdf (source-range-83ecb080-00839))_
- In that case, we can’t get the final value, but we can get a function that represents _part_ of our application. _(javascriptallonge.pdf (source-range-83ecb080-00839))_
- The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this: _(javascriptallonge.pdf (source-range-83ecb080-00840))_
- Code is easier than words for this. _(javascriptallonge.pdf (source-range-83ecb080-00840))_
- The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- We can abstract this one level higher. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely: _(javascriptallonge.pdf (source-range-83ecb080-00849))_
- > 40Modern JavaScript implementations provide a map method for arrays, but Underscore’s implementation also works with older browsers if you are working with that headache. _(javascriptallonge.pdf (source-range-83ecb080-00851))_
- Partial application also has a combinator, which we’ll see in the partial recipe. _(javascriptallonge.pdf (source-range-83ecb080-00858))_
- We generalized composition with the compose combinator. _(javascriptallonge.pdf (source-range-83ecb080-00858))_

## Technical atoms

> **const** cookAndEat = (food) => eat(cook(food));
_(source: javascriptallonge.pdf (source-range-83ecb080-00827))_

> Context: It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:
_(context: javascriptallonge.pdf (source-range-83ecb080-00828))_

> **const** compose = (a, b) => (c) => a(b(c));
_(source: javascriptallonge.pdf (source-range-83ecb080-00829))_

> Context: It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:
_(context: javascriptallonge.pdf (source-range-83ecb080-00828))_

> **const** cookAndEat = compose(eat, cook);
_(source: javascriptallonge.pdf (source-range-83ecb080-00830))_

> Context: It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators:
_(context: javascriptallonge.pdf (source-range-83ecb080-00828))_

> The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.
_(source: javascriptallonge.pdf (source-range-83ecb080-00831))_

> Context: If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.
_(context: javascriptallonge.pdf (source-range-83ecb080-00831))_

> Of course, you needn’t use combinators to implement either of these ideas, you can use if statements.
_(source: javascriptallonge.pdf (source-range-83ecb080-00833))_

> Context: Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00833))_

> - **const** actuallyTransfer= (from, to, amount) => _// do something_
_(source: javascriptallonge.pdf (source-range-83ecb080-00834))_

> Context: Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:
_(context: javascriptallonge.pdf (source-range-83ecb080-00833))_

> **const** invokeTransfer = once(maybe(actuallyTransfer(...)));
_(source: javascriptallonge.pdf (source-range-83ecb080-00835))_

> Context: Code is easier than words for this. The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this: This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:
_(context: javascriptallonge.pdf (source-range-83ecb080-00840, source-range-83ecb080-00843))_

> _.map([1, 2, 3], (n) => n * n) _//=> [1, 4, 9]_
_(source: javascriptallonge.pdf (source-range-83ecb080-00841))_

> Context: This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:
_(context: javascriptallonge.pdf (source-range-83ecb080-00843))_

> **const** squareAll = (array) => map(array, (n) => n * n);
_(source: javascriptallonge.pdf (source-range-83ecb080-00844))_

> Context: The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.
_(context: javascriptallonge.pdf (source-range-83ecb080-00845))_

> **const** mapWith = (fn) => (array) => map(array, fn);
_(source: javascriptallonge.pdf (source-range-83ecb080-00846))_

> Context: The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.
_(context: javascriptallonge.pdf (source-range-83ecb080-00845))_

> **const** squareAll = mapWith((n) => n * n);
_(source: javascriptallonge.pdf (source-range-83ecb080-00847))_

> Context: The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.
_(context: javascriptallonge.pdf (source-range-83ecb080-00845))_

> squareAll([1, 2, 3]) _//=> [1, 4, 9]_
_(source: javascriptallonge.pdf (source-range-83ecb080-00848))_

> Context: > 41If we don’t want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven’t discussed methods yet. const map = _.map;
_(context: javascriptallonge.pdf (source-range-83ecb080-00852))_

> **const** safeSquareAll = mapWith(maybe((n) => n * n));
_(source: javascriptallonge.pdf (source-range-83ecb080-00855))_
