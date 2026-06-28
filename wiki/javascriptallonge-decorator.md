---
page_id: javascriptallonge-decorator
page_kind: concept
summary: Decorator: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-decorator@64fb4232fa6e49c872e97f1ee0454ad5
---

# Decorator

What [[javascriptallonge]] covers about decorator:

## Statements

### About JavaScript Allongé

- ii

A Pull of the Lever: Prefaces

## **About JavaScript Allongé**

JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. If those terms seem unfamiliar, don’t worry: JavaScript Allongé takes great delight in explaining what they mean and why they matter.

_JavaScript Allongé_ begins at the beginning, with values and expressions, and builds from there to discuss types, identity, functions, closures, scopes, collections, iterators, and many more subjects up to working with classes and instances.

It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms like function combinators and decorators leverage JavaScript’s power to make code easier to read, modify, debug and refactor.

_JavaScript Allongé_ teaches you how to handle complex code, and it also teaches you how to simplify code without dumbing it down. As a result, _JavaScript Allongé_ is a rich read releasing many of JavaScript’s subtleties, much like the Café Allongé beloved by coffee enthusiasts everywhere.

## **why the “six” edition?**

ECMAScript 2015 (formerly called ECMAScript 6 or “ES6”), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive.

Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. For example, JavaScript did not include block-structured variables. Over time, programmers discovered ways to roll their own versions of important features.

For example, block-structured languages allow us to write: **for** ( **int** i = 0; i < array.length; ++i) { _// ..._ } And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write: _(javascriptallonge.pdf (source-range-83ecb080-00012))_

### Combinators and Function Decorators

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


## Related pages

- [[javascriptallonge-function-decorator]] - narrower topic: Function Decorator shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (3 shared statement(s))
- [[javascriptallonge-combinator]] - shared statements: Combinator shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (2 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from About JavaScript Allongé: ii  A Pull of the Lever: Prefaces  ## **About JavaScript Allongé**  JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s writ ... [truncated] (2 shared statement(s))
- [[javascriptallonge-implementation]] - shared statements: Implementation shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from About JavaScript Allongé: ii  A Pull of the Lever: Prefaces  ## **About JavaScript Allongé**  JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It’s writ ... [truncated] (1 shared statement(s))
- [[javascriptallonge-recipe]] - shared statements: Recipe shares source evidence from Building Blocks: The first sip: Basic Functions  48  ## **Building Blocks**  When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
