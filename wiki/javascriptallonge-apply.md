---
page_id: javascriptallonge-apply
page_kind: concept
summary: Apply: 3 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-apply@832b30c0b699fa62439aaad3fa7443f4
---

# Apply

What [[javascriptallonge]] covers about apply:

## Statements

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

8

I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function.

## **functions and identities**

You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not.

Which kind are functions? Let’s try them out and see. For reasons of appeasing the JavaScript parser, we’ll enclose our functions in parentheses: (() => 0) === (() => 0) _//=> false_

Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. “Function” is a reference type.

## **applying functions**

Let’s put functions to work. The way we use functions is to _apply_ them to zero or more values called _arguments_ . Just as 2 + 2 produces a value (in this case 4), applying a function to zero or more arguments produces a value as well.

Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. Let’s call the arguments _args_ . Here’s how to apply a function to some arguments:

## _fn_expr_ ( _args_ )

Right now, we only know about one such expression: () => 0, so let’s use it. We’ll put it in parentheses[17] to keep the parser happy, like we did above: (() => 0). Since we aren’t giving it any arguments, we’ll simply write () after the expression. So we write: (() => 0)() _//=> 0_

> 17If you’re used to other programming languages, you’ve probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages! _(javascriptallonge.pdf (source-range-83ecb080-00045))_

### Magic Names

- The first sip: Basic Functions

54 **const** row = **function** () { **return** mapWith( **function** (column) { **return** column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) _//=> [1,4,9,16,25,36,49,64,81,100,121,144]_ Now our inner function binds arguments[0] every time it is invoked, so we get the same result as if we’d written function (column) { return column * column }.

Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it’s a first-class entity in the code.

But sometimes, a function is a small-f function. It’s a simple representation of an expression to be computed. In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply.

Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-00093))_

### Making Data Out Of Functions

- Composing and Decomposing Data

160 **const** first = K, second = K(I), pair = V; **const** latin = pair("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_ As an aside, the Vireo is a little like JavaScript’s .apply function. It says, “take these two values and apply them to this function.” There are other, similar combinators that apply values to functions. One notable example is the “thrush” or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap.

Armed with nothing more than K, I, and V, we can make a little data structure that holds two values, the cons cell of Lisp and the node of a linked list. Without arrays, and without objects, just with functions. We’d better try it out to check.

## **lists with functions as data**

Here’s another look at linked lists using POJOs. We use the term rest instead of second, but it’s otherwise identical to what we have above: **const** first = ({first, rest}) => first, rest = ({first, rest}) => rest, pair = (first, rest) => ({first, rest}), EMPTY = ({}); **const** l123 = pair(1, pair(2, pair(3, EMPTY))); first(l123) _//=> 1_ first(rest(l123)) _//=> 2_ first(rest(rest(l123))) _//=3_

We can write length and mapWith functions over it: _(javascriptallonge.pdf (source-range-83ecb080-00216))_


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  8  I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really count ... [truncated] (3 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  8  I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really count ... [truncated] (2 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  8  I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really count ... [truncated] (1 shared statement(s))
- [[javascriptallonge-variable]] - shared statements: Variable shares source evidence from Magic Names: The first sip: Basic Functions  54 **const** row = **function** () { **return** mapWith( **function** (column) { **return** column * arguments[0] }, [1, 2, 3, 4, 5, ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
