---
page_id: javascriptallonge-statement
page_kind: concept
summary: Statement: 6 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-statement@64a9fb055ea0da4dd808ae17af8eb4bd
---

# Statement

What [[javascriptallonge]] covers about statement:

## Statements

### As Little As Possible About Functions, But No Less

- 14

The first sip: Basic Functions (() => 2 + 2)() _//=> 4_ (() => { 2 + 2 })() _//=> undefined_ (() => (1 + 1, 2 + 2))() _//=> 4_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ So how do we get a function that evaluates a block to return a value when applied? With the return keyword and any expression: (() => { **return** 0 })() _//=> 0_ (() => { **return** 1 })() _//=> 1_ (() => { **return** 'Hello ' + 'World' })() _// 'Hello World'_

The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example: (() => { 1 + 1; **return** 2 + 2 })() _//=> 4_ And also: (() => { **return** 1 + 1; 2 + 2 })() _//=> 2_

The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression: _(javascriptallonge.pdf (source-range-83ecb080-00051))_

### That Constant Coffee Craving

- The first sip: Basic Functions

31

## **nested blocks**

Up to now, we’ve only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this: (n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else return** !even(x - 1); } **return** even(n) } And it works for fairly small numbers: ((n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else return** !even(x - 1); } **return** even(n) })(13) _//=> false_

The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: (n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else** { **const** odd = (y) => !even(y); **return** odd(x - 1); } _(javascriptallonge.pdf (source-range-83ecb080-00067))_

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

### Summary

- The first sip: Basic Functions

55

## **Summary**

**==> picture [29 x 29] intentionally omitted <==**

## **Functions**

- Functions are values that can be part of expressions, returned from other functions, and so forth.

- Functions are _reference values_ .

- Functions are applied to arguments.

- The arguments are passed by sharing, which is also called “pass by value.” - Fat arrow functions have expressions or blocks as their bodies.

- function keyword functions always have blocks as their bodies.

- Function bodies have zero or more statements.

- Expression bodies evaluate to the value of the expression.

- Block bodies evaluate to whatever is returned with the return keyword, or to undefined.

- JavaScript uses const to bind values to names within block scope.

- JavaScript uses function declarations to bind functions to names within function scope. Function declarations are “hoisted.” - Function application creates a scope.

- Blocks also create scopes if const statements are within them.

- Scopes are nested and free variable references closed over.

- Variables can shadow variables in an enclosing scope. _(javascriptallonge.pdf (source-range-83ecb080-00095))_

### Arrays and Destructuring Arguments

- Composing and Decomposing Data

80 **const** x = [], a = [x]; a[0] === x

_//=> true, arrays store references to the things you put in them._

## **destructuring arrays**

There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [, expressions, , and ]. Here’s an example of an array literal that uses a name: **const** wrap = (something) => [something];

Let’s expand it to use a block and an extra name: **const** wrap = (something) => { **const** wrapped = [something]; **return** wrapped; } wrap("package") _//=> ["package"]_ The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right: **const** unwrap = (wrapped) => { **const** [something] = wrapped; **return** something; } unwrap(["present"]) _//=> "present"_

The statement const [something] = wrapped; _destructures_ the array represented by wrapped, binding the value of its single element to the name something. We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-83ecb080-00126))_


## Related pages

- [[javascriptallonge-const]] - shared statements: Const shares source evidence from That Constant Coffee Craving: 34  The first sip: Basic Functions ((diameter_fn) => { **const** PI = 3; **return** diameter_fn(2) })( (() => { **const** PI = 3.14159265; **return** (diameter) => d ... [truncated] (4 shared statement(s))
- [[javascriptallonge-array]] - shared statements: Array shares source evidence from Arrays and Destructuring Arguments: Composing and Decomposing Data  80 **const** x = [], a = [x]; a[0] === x  _//=> true, arrays store references to the things you put in them._  ## **destructuring arr ... [truncated] (1 shared statement(s))
- [[javascriptallonge-block]] - shared statements: Block shares source evidence from Summary: The first sip: Basic Functions  55  ## **Summary**  **==> picture [29 x 29] intentionally omitted <==**  ## **Functions**  - Functions are values that can be part of ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from As Little As Possible About Functions, But No Less: 14  The first sip: Basic Functions (() => 2 + 2)() _//=> 4_ (() => { 2 + 2 })() _//=> undefined_ (() => (1 + 1, 2 + 2))() _//=> 4_ (() => { 1 + 1; 2 + 2 })() _//=> u ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
