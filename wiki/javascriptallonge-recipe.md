---
page_id: javascriptallonge-recipe
page_kind: concept
summary: Recipe: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-recipe@009b99c778f782e06d9221f7581b043e
---

# Recipe

What [[javascriptallonge]] covers about recipe:

## Statements

### Building Blocks

- The first sip: Basic Functions

48

## **Building Blocks**

When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks.

## **composition**

: One of the most basic of these building blocks is _composition_ **const** cookAndEat = (food) => eat(cook(food));

It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators: **const** compose = (a, b) => (c) => a(b(c)); **const** cookAndEat = compose(eat, cook);

If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument.

Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

- **const** actuallyTransfer= (from, to, amount) => _// do something_ **const** invokeTransfer = once(maybe(actuallyTransfer(...))); _(javascriptallonge.pdf (source-range-83ecb080-00086))_

### Recipes with Basic Functions

- ## **Recipes with Basic Functions**

**==> picture [384 x 289] intentionally omitted <==**

**Before combining ingredients, begin with implements so clean, they gleam.**

Having looked at basic pure functions and closures, we’re going to see some practical recipes that focus on the premise of functions that return functions.

## **Disclaimer**

The recipes are written for practicality, and their implementation may introduce JavaScript features that haven’t been discussed in the text to this point, such as methods and/or prototypes. The overall _use_ of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-83ecb080-00097))_

### Recipes with Data

- Recipes with Data

169

## **Disclaimer**

The recipes are written for practicality, and their implementation may introduce JavaScript features that haven’t been discussed in the text to this point, such as methods and/or prototypes. The overall _use_ of each recipe will fit within the spirit of the language discussed so far, even if the implementations may not. _(javascriptallonge.pdf (source-range-83ecb080-00226))_


## Related pages

- [[javascriptallonge-decorator]] - shared statements: Decorator shares source evidence from Building Blocks: The first sip: Basic Functions  48  ## **Building Blocks**  When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
