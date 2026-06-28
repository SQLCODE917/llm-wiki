---
page_id: javascriptallonge-operator
page_kind: concept
summary: Operator: 6 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-operator@a5a738550d2fcb42ea6af9acd0e73a25
---

# Operator

What [[javascriptallonge]] covers about operator:

## Statements

### values are expressions

- xv

Prelude: Values and Expressions over Coffee

Now we see that “strings” are values, and you can make an expression out of strings and an operator +. Since strings are values, they are also expressions by themselves. But strings with operators are not values, they are expressions. Now we know what was missing with our “coffee grounds plus hot water” example. The coffee grounds were a value, the boiling hot water was a value, and the “plus” operator between them made the whole thing an expression that was not a value. _(javascriptallonge.pdf (source-range-83ecb080-00031))_

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

### As Little As Possible About Functions, But No Less

- 10

The first sip: Basic Functions (() => (() => 0 )() )() _//=> 0_

It evaluates to the same thing, 0.

## **commas**

The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

(1, 2) _//=> 2_

(1 + 1, 2 + 2) _//=> 4_

We can use commas with functions to create functions that evaluate multiple expressions: (() => (1 + 1, 2 + 2))() _//=> 4_

This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write: () => (1 + 1, 2 + 2) Or even: () => ( 1 + 1, 2 + 2 ) _(javascriptallonge.pdf (source-range-83ecb080-00047))_

### Left-Variadic Functions

- 76

Picking the Bean: Choice and Truthiness **const** or = (a, b) => a() || b() **const** and = (a, b) => a() && b() **const** even = (n) => or(() => n === 0, () => and(() => n !== 1, () => even(n - 2))) even(7) _//=> false_

Here we’ve passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation.

## **summary**

- Logical operators are based on truthiness and falsiness, not the strict values true and false.

- ! is a logical operator, it always returns true or false.

- The ternary operator (?:), ||, and && are control flow operators, they do not always return true or false, and they have short-cut semantics.

- Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-83ecb080-00120))_

### Iteration and Iterables

- 192

Served by the Pot: Collections As we can see, we can use for...of with linked lists just as easily as with stacks. And there’s one more thing: You recall that the spread operator (...) can spread the elements of an array in an array literal or as parameters in a function invocation.

Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal:

- ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_ And we can also spread the elements of an array literal into parameters: **const** firstAndSecondElement = (first, second) => ({first, second}) firstAndSecondElement(...stack) _//=> {"first":5,"second":10}_ This can be extremely useful.

One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

And if we have an infinite collection, spreading is going to fail outright as we’re about to see.

## **iterables out to infinity**

Iterables needn’t represent finite collections: **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } } There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them: _(javascriptallonge.pdf (source-range-83ecb080-00256))_


## Related pages

- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from A Rich Aroma: Basic Numbers: A Rich Aroma: Basic Numbers  3  0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_  This kind of “inexactitude” can be ignored when perfo ... [truncated] (2 shared statement(s))
- [[javascriptallonge-recall]] - shared statements: Recall shares source evidence from Iteration and Iterables: 192  Served by the Pot: Collections As we can see, we can use for...of with linked lists just as easily as with stacks. And there’s one more thing: You recall that t ... [truncated] (1 shared statement(s))
- [[javascriptallonge-string]] - shared statements: String shares source evidence from values are expressions: xv  Prelude: Values and Expressions over Coffee  Now we see that “strings” are values, and you can make an expression out of strings and an operator +. Since strings ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
