---
page_id: javascriptallonge-difference
page_kind: concept
summary: Difference: 4 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-difference@4aa4016f1617afa630d64101911a04bd
---

# Difference

What [[javascriptallonge]] covers about difference:

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

### Closures and Scope

- The first sip: Basic Functions

23

## **it’s always the environment**

To understand how closures are evaluated, we need to revisit environments. As we’ve said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let’s fill in the blanks!

The environment for ((y) => x)(2) is _actually_ {y: 2, '..': {x: 1, ...}}. '..' means something like “parent” or “enclosure” or “super-environment.” It’s (x) => ...’s environment, because the function (y) => x is within (x) => ...’s body. So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

And now you can guess how we evaluate ((y) => x)(2) in the environment {y: 2, '..': {x: 1, ...}}. The variable x isn’t in (y) => ...’s immediate environment, but it is in its parent’s environment, so it evaluates to 1 and that’s what ((y) => x)(2) returns even though it ended up ignoring its own argument.

(x) => x is called the I Combinator, or the _Identity Function_ . (x) => (y) => x is called the K Combinator, or _Kestrel_ . Some people get so excited by this that they write entire books about them, some are great _[a]_ , some–how shall I put this–are interesting _[b]_ if you use Ruby.

> _a_ http://www.amzn.com/0192801422?tag=raganwald001-20

> _b_ https://leanpub.com/combinators

Functions can have grandparents too: (x) => (y) => (z) => x + y + z

This function does much the same thing as: (x, y, z) => x + y + z

Only you call it with (1)(2)(3) instead of (1, 2, 3). The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3). _(javascriptallonge.pdf (source-range-83ecb080-00058))_

### Copy on Write

- Composing and Decomposing Data

138 **const** childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ Our new at and set functions behave similarly to array[index] and array[index] = value. The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list.

## **copy-on-read**

So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.

**const** rest = ({first, rest}) => copy(rest); **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = rest(parentList); **const** newParentList = set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}} This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don’t need to make a copy because we won’t be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node).

There’s also a bug: What happens when we modify the first element of a list? But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-00191))_

### Interactive Generators

- Served by the Pot: Collections

260 } } **break** ; _// ..._ } } **const** aNaughtsAndCrossesGame = generatorNaughtsAndCrosses();

We can then get the first move by calling .next(). Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. If we wanted to pass some state to the generator before it begins, we’d do that with parameters.): aNaughtsAndCrossesGame.next().value

_//=> 0_ aNaughtsAndCrossesGame.next(1).value

_//=> 6_ aNaughtsAndCrossesGame.next(3).value

_//=> 8_ aNaughtsAndCrossesGame.next(7).value

_//=> 4_

Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn’t call us. It isn’t a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block.

But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data.

## **summary**

We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. But as we see here, it’s also possible to use a generator interactively, passing values in and receiving a value in return, just like an ordinary function.

Again, the salient difference is that an “interactive” generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-83ecb080-00326))_


## Source

- [[javascriptallonge]]
