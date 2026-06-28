---
page_id: javascriptallonge-evaluate
page_kind: concept
summary: Evaluate: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-evaluate@8d68449542742585ff56c6d156dc0ebe
---

# Evaluate

What [[javascriptallonge]] covers about evaluate:

## Statements

### values and identity

- xviii

Prelude: Values and Expressions over Coffee

An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like:

[2-1, 2, 2+1] [1, 1+1, 1+1+1] Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42? Try these for yourself:

[2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other array also looks like [1, 2, 3]. It’s as if JavaScript is generating new cups of coffee with serial numbers on the bottom.

They look the same, but if you examine them with ===, you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. As we’ll see, this is true of many other kinds of values, including _functions_ , the main subject of this book. _(javascriptallonge.pdf (source-range-83ecb080-00035))_

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

11

## **the simplest possible block**

There’s another thing we can put to the right of an arrow, a _block_ . A block has zero or more _statements_ , separated by semicolons.[18] So, this is a valid function:

## () => {}

It returns the result of evaluating a block that has no statements. What would that be? Let’s try it: (() => {})() _//=> undefined_

What is this undefined?

## **undefined**

In JavaScript, the absence of a value is written undefined, and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type:

## **undefined**

_//=> undefined_

Like numbers, booleans and strings, JavaScript can print out the value undefined.

**undefined** === **undefined**

_//=> true_ (() => {})() === (() => {})() _//=> true_ (() => {})() === **undefined** _//=> true_

No matter how you evaluate undefined, you get an identical value back. undefined is a value that means “I don’t have a value.” But it’s still a value :-)

> 18Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it’s helpful to know it exists. _(javascriptallonge.pdf (source-range-83ecb080-00048))_

### Closures and Scope

- The first sip: Basic Functions

24

The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its arguments is sometimes called partial application _[b]_ . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them.

> _a_ https://en.wikipedia.org/wiki/Currying

> _b_ https://en.wikipedia.org/wiki/Partial_application

## **shadowy variables from a shadowy planet**

An interesting thing happens when a variable has the same name as an ancestor environment’s variable. Consider:

- (x) => (x, y) => x + y

The function (x, y) => x + y is a pure function, because its x is defined within its own environment. Although its parent also defines an x, it is ignored when evaluating x + y. JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one. The same is true of: (x) => (x, y) => (w, z) => (w) => x + y + z

When evaluating x + y + z, JavaScript will find x and y in the great-grandparent scope and z in the parent scope. The x in the great-great-grandparent scope is ignored, as are both ws. When a variable has the same name as an ancestor environment’s binding, it is said to _shadow_ the ancestor.

This is often a good thing.

## **which came first, the chicken or the egg?**

This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state.

But before we do so, there’s one final question: Where does the ancestry start? If there’s no other code in a file, what is (x) => x’s parent environment? _(javascriptallonge.pdf (source-range-83ecb080-00059))_

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

### A Warm Cup: Basic Strings and Quasi-Literals

- A Warm Cup: Basic Strings and Quasi-Literals

181

- 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They’re easier to read and it’s easier to avid errors like the following:

- 'A popular number for nerds is' + (40 + 2) - _//=> 'A popular number for nerds is42'_

## **evaluation time**

Like any other expression, quasi-literals are evaluated _late_ , when that line or lines of code is evaluated.

So for example, **const** name = "Harry"; **const** greeting = (name) => `Hello my name is **${** name **}** `; greeting('Arthur Dent') - _//=> 'Hello my name is Arthur Dent'_

JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function’s body is evaluated. Thus, name is not bound to "Harry", it is bound to 'Arthur Dent', the value of the parameter when the function is invoked.

This is exactly what we’d expect if we’d written it like this: **const** greeting = (name) => 'Hello my name is ' + name; greeting('Arthur Dent') - _//=> 'Hello my name is Arthur Dent'_ _(javascriptallonge.pdf (source-range-83ecb080-00243))_


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Closures and Scope: The first sip: Basic Functions  24  The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its argument ... [truncated] (2 shared statement(s))
- [[javascriptallonge-block]] - shared statements: Block shares source evidence from Summary: The first sip: Basic Functions  55  ## **Summary**  **==> picture [29 x 29] intentionally omitted <==**  ## **Functions**  - Functions are values that can be part of ... [truncated] (1 shared statement(s))
- [[javascriptallonge-expression]] - shared statements: Expression shares source evidence from values and identity: xviii  Prelude: Values and Expressions over Coffee  An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wil ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from Closures and Scope: The first sip: Basic Functions  24  The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its argument ... [truncated] (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements: Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-programming]] - shared statements: Programming shares source evidence from Closures and Scope: The first sip: Basic Functions  24  The first function is the result of currying _[a]_ the second function. Calling a curried function with only some of its argument ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-quasi-literal]] - shared statements: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: A Warm Cup: Basic Strings and Quasi-Literals  181  - 'A popular number for nerds is ' + (40 + 2) - _//=> 'A popular number for nerds is 42'_ However, there is a big ... [truncated] (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from values and identity: xviii  Prelude: Values and Expressions over Coffee  An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wil ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
