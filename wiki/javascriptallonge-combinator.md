---
page_id: javascriptallonge-combinator
page_kind: concept
summary: Combinator: 8 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-combinator@4f611919ef3b405805fc7597014fc8d4
---

# Combinator

What [[javascriptallonge]] covers about combinator:

## Statements

### Combinators and Function Decorators

- The first sip: Basic Functions

45

## **Combinators and Function Decorators**

## **higher-order functions**

As we’ve seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function.

Here’s a very simple higher-order function that takes a function as an argument: **const** repeat = (num, fn) => (num > 0) ? (repeat(num - 1, fn), fn(num)) : **undefined** repeat(3, **function** (n) { console.log(`Hello **${** n **}** `) }) _//=>_ 'Hello 1' 'Hello 2' 'Hello 3' **undefined**

Higher-order functions dominate _JavaScript Allongé_ . But before we go on, we’ll talk about some specific types of higher-order functions.

## **combinators**

The word “combinator” has a precise technical meaning in mathematics:

“A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.”–Wikipedia[35] If we were learning Combinatorial Logic, we’d start with the most basic combinators like S, K, and I, and work up from there to practical combinators. We’d learn that the fundamental combinators are named after birds following the example of Raymond Smullyan’s famous book To Mock a Mockingbird[36] .

> 35https://en.wikipedia.org/wiki/Combinatory_logic

> 36http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 _(javascriptallonge.pdf (source-range-83ecb080-00082))_

- The first sip: Basic Functions

46

In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as arguments and return a function. We won’t be strict about using only previously defined combinators in their construction.

Let’s start with a useful combinator: Most programmers call it _Compose_ , although the logicians call it the B combinator or “Bluebird.” Here is the typical[37] programming implementation:

- **const** compose = (a, b) => (c) => a(b(c)) Let’s say we have: **const** addOne = (number) => number + 1; **const** doubleOf = (number) => number * 2;

With compose, anywhere you would write **const** doubleOfAddOne = (number) => doubleOf(addOne(number));

You could also write: **const** doubleOfAddOne = compose(doubleOf, addOne);

This is, of course, just one example of many. You’ll find lots more perusing the recipes in this book. While some programmers believe “There Should Only Be One Way To Do It,” having combinators available as well as explicitly writing things out with lots of symbols and keywords has some advantages when used judiciously.

## **a balanced statement about combinators**

Code that uses a lot of combinators tends to name the verbs and adverbs (like doubleOf, addOne, and compose) while avoiding language keywords and the names of nouns (like number). So one perspective is that combinators are useful when you want to emphasize what you’re doing and how it fits together, and more explicit code is useful when you want to emphasize what you’re working with.

## **function decorators**

A _function decorator_ is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here’s a ridiculously simple decorator:[38] > 37As we’ll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.

> 38 We’ll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) _(javascriptallonge.pdf (source-range-83ecb080-00083))_

- The first sip: Basic Functions

47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress. But like compose, we could write either: **const** something = (x) => x != **null** ; And elsewhere, write: **const** nothing = (x) => !something(x); Or we could write: **const** nothing = not(something); not is a function decorator because it modifies a function while remaining strongly related to the original function’s semantics. You’ll see other function decorators in the recipes, like once and maybe. Function decorators aren’t strict about being pure functions, so there’s more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-83ecb080-00084))_


## Related pages

- [[javascriptallonge-decorator]] - shared statements: Decorator shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (2 shared statement(s))
- [[javascriptallonge-function-decorator]] - shared statements: Function Decorator shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (2 shared statement(s))
- [[javascriptallonge-programmer]] - shared statements: Programmer shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  47 **const** not = (fn) => (x) => !fn(x) So instead of writing !someFunction(42), we can write not(someFunction)(42). Hardly progress ... [truncated] (1 shared statement(s))
- [[javascriptallonge-implementation]] - shared statements: Implementation shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (1 shared statement(s))
- [[javascriptallonge-learn]] - shared statements: Learn shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  45  ## **Combinators and Function Decorators**  ## **higher-order functions**  As we’ve seen, JavaScript functions take values as arg ... [truncated] (1 shared statement(s))
- [[javascriptallonge-start]] - shared statements: Start shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
