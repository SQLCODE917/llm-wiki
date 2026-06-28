---
page_id: javascriptallonge-seen
page_kind: concept
summary: Seen: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-seen@cb5fce0c2dbd1d683b06561e49333970
---

# Seen

What [[javascriptallonge]] covers about seen:

## Statements

### A Rich Aroma: Basic Numbers

- A Rich Aroma: Basic Numbers

3

0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_

This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.

But as a rule, if you need to work with real numbers, you should have more than a nodding acquaintance with the IEEE Standard for Floating-Point Arithmetic[15] . Professional programmers almost never use floating point numbers to represent monetary amounts. For example, “$43.21” will nearly always be presented as two numbers: 43 for dollars and 21 for cents, not 43.21. In this book, we need not think about such details, but outside of this book, we must.

## **operations on numbers**

As we’ve seen, JavaScript has many common arithmetic operators. We can create expressions that look very much like mathematical expressions, for example we can write 1 + 1 or 2 * 3 or 42 - 34 or even 6 / 2. These can be combined to make more complex expressions, like 2 * 5 + 1.

In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So:

2 * 5 + 1 _//=> 11_ 1 + 5 * 2 _//=> 11_

JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2), because the * operator has a _higher precedence_ than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus, of course).

In addition to the common +, -, *, and /, JavaScript also supports modulus, %, and unary negation, -:

15https://en.wikipedia.org/wiki/IEEE_floating_point _(javascriptallonge.pdf (source-range-83ecb080-00039))_

### That Constant Coffee Craving

- The first sip: Basic Functions

26

## **That Constant Coffee Craving**

Up to now, all we’ve really seen are _anonymous functions_ , functions that don’t have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we’ve seen so far is how to name arguments.

There are other ways to name things in JavaScript, but before we learn some of those, let’s see how to use what we already have to name things. Let’s revisit a very simple example: (diameter) => diameter * 3.14159265

What is this “3.14159265” number? PI[28] , obviously. We’d like to name it so that we can write something like: (diameter) => diameter * PI

In order to bind 3.14159265 to the name PI, we’ll need a function with a parameter of PI applied to an argument of 3.14159265. If we put our function expression in parentheses, we can apply it to the argument of 3.14159265:

((PI) => _// ????_ )(3.14159265) What do we put inside our new function that binds 3.14159265 to the name PI when evaluated? Our circumference function, of course:

((PI) => (diameter) => diameter * PI )(3.14159265) This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our “functions” are expressions. This one has a few more moving parts, that’s all. But we can use it just like (diameter) => diameter * 3.14159265.

Let’s test it:

28https://en.wikipedia.org/wiki/Pi _(javascriptallonge.pdf (source-range-83ecb080-00062))_

- The first sip: Basic Functions

31

## **nested blocks**

Up to now, we’ve only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this: (n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else return** !even(x - 1); } **return** even(n) } And it works for fairly small numbers: ((n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else return** !even(x - 1); } **return** even(n) })(13) _//=> false_

The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like: (n) => { **const** even = (x) => { **if** (x === 0) **return true** ; **else** { **const** odd = (y) => !even(y); **return** odd(x - 1); } _(javascriptallonge.pdf (source-range-83ecb080-00067))_

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

97

## **converting non-tail-calls to tail-calls**

The obvious solution is push the 1 + work into the call to length. Here’s our first cut: **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysWork(["foo", "bar", "baz"], 0) _//=> 3_

This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that: **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

? numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) **const** length = (n) => lengthDelaysWork(n, 0); Or we could use partial application: **const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** length = callLast(lengthDelaysWork, 0); length(["foo", "bar", "baz"]) _//=> 3_

This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith: _(javascriptallonge.pdf (source-range-83ecb080-00144))_

### Copy on Write

- Composing and Decomposing Data

135

## **Copy on Write**

**==> picture [469 x 364] intentionally omitted <==**

**The Coffee Cow**

We’ve seen how to build lists with arrays and with linked lists. We’ve touched on an important difference between them:

- When you take the rest of an array with destructuring ([first, ...rest]), you are given a _copy_ of the elements of the array.

- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list.

The consequence of this is that if you have an array, and you take it’s “rest,” your “child” array is a copy of the elements of the parent array. And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-00188))_


## Related pages

- [[javascriptallonge-block]] - shared statements: Block shares source evidence from That Constant Coffee Craving: The first sip: Basic Functions  31  ## **nested blocks**  Up to now, we’ve only ever seen blocks we use as the body of functions. But there are other kinds of blocks ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from A Rich Aroma: Basic Numbers: A Rich Aroma: Basic Numbers  3  0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_  This kind of “inexactitude” can be ignored when perfo ... [truncated] (1 shared statement(s))
- [[javascriptallonge-list]] - shared statements: List shares source evidence from Copy on Write: Composing and Decomposing Data  135  ## **Copy on Write**  **==> picture [469 x 364] intentionally omitted <==**  **The Coffee Cow**  We’ve seen how to build lists w ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
