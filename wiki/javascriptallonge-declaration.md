---
page_id: javascriptallonge-declaration
page_kind: concept
summary: Declaration: 4 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-declaration@072a0892f4fcca9e1a78df70c96841f0
---

# Declaration

What [[javascriptallonge]] covers about declaration:

## Statements

### That Constant Coffee Craving

- 43

The first sip: Basic Functions

( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:

( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })() The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript’s design to facilitate a certain style of programming where you put the main logic up front, and the “helper functions” at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const) is essential for working with production code.

## **function declaration caveats**[34]

Function declarations are formally only supposed to be made at what we might call the “top level” of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea:

34 A number of the caveats discussed here were described in Jyrly Zaytsev’s excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-83ecb080-00079))_

- 44

The first sip: Basic Functions

( **function** (camelCase) { **return** fizzbuzz(); **if** (camelCase) { **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } } **else** { **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } } })( **true** ) _//=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?_

Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. So this is a function declaration: **function** trueDat () { **return true** } But this is not:

( **function** trueDat () { **return true** }) The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-83ecb080-00080))_

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

### Reassignment

- Composing and Decomposing Data

129 **return** n * factorial2(x); } } factorial2(5) _//=> 120_ But of course, it’s not exactly like let. It’s just different enough to present a source of confusion. First, var is not block scoped, it’s function scoped, just like function declarations: (() => { **var** age = 49; **if** ( **true** ) { **var** age = 50; } **return** age; })() _//=> 50_

Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration _and_ the definition are hoisted. Note this example of a function that uses a helper: **const** factorial = (n) => { **return** innerFactorial(n, 1); **function** innerFactorial (x, y) { **if** (x == 1) { **return** y; } **else** { **return** innerFactorial(x-1, x * y); } } } factorial(4) _//=> 24_ _(javascriptallonge.pdf (source-range-83ecb080-00181))_


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from That Constant Coffee Craving: 43  The first sip: Basic Functions  ( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Althou ... [truncated] (4 shared statement(s))

## Source

- [[javascriptallonge]]
