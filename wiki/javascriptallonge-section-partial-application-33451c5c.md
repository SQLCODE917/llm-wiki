---
page_id: javascriptallonge-section-partial-application-33451c5c
page_kind: source
summary: **partial application**: 17 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-partial-application-33451c5c@e0d1a1b3c104a4bfbe47e82ab0e2154d
---

# **partial application**

From [[javascriptallonge]].

## Statements

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
