---
page_id: javascriptallonge-function-but
page_kind: concept
summary: As Little As Possible About Functions, But No Less: 63 statement(s) and 20 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function-but@6074bdc4df4565d788248f9d36a43b97
---

# As Little As Possible About Functions, But No Less

What [[javascriptallonge]] covers about as little as possible about functions, but no less:

## Statements

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00285))_
- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-83ecb080-00291))_
- It’s a function that when applied, evaluates to a function that when applied, evaluates to 0. _(javascriptallonge.pdf (source-range-83ecb080-00378))_
- Functions represent computations to be performed. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- “Function” is a reference type. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] _(javascriptallonge.pdf (source-range-83ecb080-00346))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: _(javascriptallonge.pdf (source-range-83ecb080-00353))_
- This is a function that is applied to no values and returns 0. _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- The way we use functions is to _apply_ them to zero or more values called _arguments_ . _(javascriptallonge.pdf (source-range-83ecb080-00274))_

## Technical atoms

> Context: This is a function that is applied to no values and returns 0. Let’s verify that our function is a value like all others:
_(context: javascriptallonge.pdf (source-range-83ecb080-00260))_

> If you try the same thing in a browser, you may see something else.
_(source: javascriptallonge.pdf (source-range-83ecb080-00262))_

> Context: What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else.
_(context: javascriptallonge.pdf (source-range-83ecb080-00262))_

> > 16 The simplest possible function is () => {}, we’ll see that later.
_(source: javascriptallonge.pdf (source-range-83ecb080-00263))_

> Context: Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.
_(context: javascriptallonge.pdf (source-range-83ecb080-00285))_

> (() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_
_(source: javascriptallonge.pdf (source-range-83ecb080-00287))_

> Context: Yes we can! Functions can return the value of evaluating another function.
_(context: javascriptallonge.pdf (source-range-83ecb080-00291))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.
_(source: javascriptallonge.pdf (source-range-83ecb080-00292))_

> Context: The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:
_(context: javascriptallonge.pdf (source-range-83ecb080-00298))_

> (1 + 1, 2 + 2) _//=> 4_
_(source: javascriptallonge.pdf (source-range-83ecb080-00300))_

> Context: We can use commas with functions to create functions that evaluate multiple expressions:
_(context: javascriptallonge.pdf (source-range-83ecb080-00301))_

> (() => (1 + 1, 2 + 2))() _//=> 4_
_(source: javascriptallonge.pdf (source-range-83ecb080-00302))_


## Source

- [[javascriptallonge]]
