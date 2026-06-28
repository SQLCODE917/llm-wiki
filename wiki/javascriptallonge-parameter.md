---
page_id: javascriptallonge-parameter
page_kind: concept
summary: Parameter: 4 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-parameter@39e6108923fd2b111ed05c375ba5c68c
---

# Parameter

What [[javascriptallonge]] covers about parameter:

## Statements

### That Constant Coffee Craving

- 34

The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => diameter * PI })() ) _//=> 6.2831853_

Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope.

## **are consts also from a shadowy planet?**

We just saw that values bound with const use lexical scope, just like values bound with parameters. They are looked up in the environment where they are declared. And we know that functions create environments. Parameters are declared when we create functions, so it makes sense that parameters are bound to environments created when we invoke functions.

But const statements can appear inside blocks, and we saw that blocks can appear inside of other blocks, including function bodies. So where are const variables bound? In the function environment? Or in an environment corresponding to the block?

We can test this by creating another conflict. But instead of binding two different variables to the same name in two different places, we’ll bind two different values to the same name, but one environment will be completely enclosed by the other.

Let’s start, as above, by doing this with parameters. We’ll start with:

((PI) => (diameter) => diameter * PI )(3.14159265) And gratuitously wrap it in another IIFE so that we can bind PI to something else: _(javascriptallonge.pdf (source-range-83ecb080-00070))_

- 36

The first sip: Basic Functions ((diameter) => { **const** PI = 3.14159265; (() => { **const** PI = 3; })(); **return** diameter * PI; })(2) _//=> 6.2831853_

Yes, names bound with const shadow enclosing bindings just like parameters. But wait! There’s more!!!

Parameters are only bound when we invoke a function. That’s why we made all these IIFEs. But const statements can appear inside blocks. What happens when we use a const inside of a block?

We’ll need a gratuitous block. We’ve seen if statements, what could be more gratuitous than: **if** ( **true** ) { _// an immediately invoked block statement (IIBS)_ } Let’s try it: ((diameter) => { **const** PI = 3; **if** ( **true** ) { **const** PI = 3.14159265; **return** diameter * PI; } })(2) _//=> 6.2831853_ ((diameter) => { **const** PI = 3.14159265; **if** ( **true** ) { **const** PI = 3; } **return** diameter * PI; _(javascriptallonge.pdf (source-range-83ecb080-00072))_

### Making Data Out Of Functions

- Composing and Decomposing Data

159

Our latin data structure is no longer a dumb data structure, it’s a function. And instead of passing latin to first or second, we pass first or second to latin. It’s _exactly backwards_ of the way we write functions that operate on data.

## **the vireo**

Given that our latin data is represented as the function (selector) => selector("primus")("secundus"), our obvious next step is to make a function that makes data. For arrays, we’d write cons = (first, second) => [first, second]. For objects we’d write: cons = (first, second) => {first, second}. In both cases, we take two parameters, and return the form of the data.

For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters: (first, second) => (selector) => selector(first)(second) For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: (first) => (second) => (selector) => selector(first)(second) Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default): **const** first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second); **const** latin = pair("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_

It works! Now what is this pair function? If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y). That’s the V combinator, the Vireo! So we can write:

78https://en.wikipedia.org/wiki/Currying _(javascriptallonge.pdf (source-range-83ecb080-00215))_


## Related pages

- [[javascriptallonge-bind]] - shared statements: Bind shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (1 shared statement(s))
- [[javascriptallonge-binding]] - shared statements: Binding shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (1 shared statement(s))
- [[javascriptallonge-const]] - shared statements: Const shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Making Data Out Of Functions: Composing and Decomposing Data  159  Our latin data structure is no longer a dumb data structure, it’s a function. And instead of passing latin to first or second, w ... [truncated] (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
