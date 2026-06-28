---
page_id: javascriptallonge-rest
page_kind: concept
summary: Rest: 7 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-rest@570db58ef3279fc89fa006c3f4d17c2e
---

# Rest

What [[javascriptallonge]] covers about rest:

## Statements

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

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

94

## **Tail Calls (and Default Arguments)**

The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not “production-ready” implementations. One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded.

Let’s look at how. Here’s our extremely simple mapWith function again: **const** mapWith = (fn, [first, ...rest]) => first === **undefined** ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ Let’s step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined, so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest), then evaluate [fn(first), ...mapWith(fn, rest)].

This is roughly equivalent to writing: **const** mapWith = **function** (fn, [first, ...rest]) { **if** (first === **undefined** ) { **return** []; } **else** { **const** _temp1 = fn(first), _temp2 = mapWith(fn, rest), _temp3 = [_temp1, ..._temp2]; **return** _temp3; } } Note that while evaluating mapWith(fn, rest), JavaScript must retain the value first or fn(first), plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1.

Next, JavaScript invokes mapWith(fn, rest), which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]). And the same thing happens: JavaScript has to hang on to 2 (or 4, or both, _(javascriptallonge.pdf (source-range-83ecb080-00141))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

104

Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious.[64] The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend.

We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

**Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded.

So here’s a question: If this is such a slow approach, why do some examples of “functional” algorithms work this exact way?

> 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript’s built-in arrays work. _(javascriptallonge.pdf (source-range-83ecb080-00153))_

### Mutation

- Composing and Decomposing Data

121 **const** EMPTY = {}; **const** OneToFive = { first: 1, rest: { first: 2, rest: { first: 3, rest: { first: 4, rest: { first: 5, rest: EMPTY } } } } };

OneToFive

_//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\_ r","rest":{"first":"five","rest":{}}}}}} const ThreeToFive = OneToFive.rest.rest;

ThreeToFive

//=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}} ThreeToFive.first = "three"; ThreeToFive.rest.first = "four"; ThreeToFive.rest.rest.first = "five";

## ThreeToFive

//=> {"first":"three","rest":{"first":"four","rest":{"first":"five","rest":{}}\ }} OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}} Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes.

Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so: _(javascriptallonge.pdf (source-range-83ecb080-00172))_

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

- Composing and Decomposing Data

138 **const** childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ Our new at and set functions behave similarly to array[index] and array[index] = value. The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list.

## **copy-on-read**

So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.

**const** rest = ({first, rest}) => copy(rest); **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = rest(parentList); **const** newParentList = set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}} This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don’t need to make a copy because we won’t be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node).

There’s also a bug: What happens when we modify the first element of a list? But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-00191))_


## Technical atoms

### Technical frame 1: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00147))_

> Composing and Decomposing Data

99

5! = 5 x 4 x 3 x 2 x 1 = 120.

The naïve function for calcuating the factorial of a positive integer follows directly from the definition: **const** factorial = (n) => n == 1 ? n : n * factorial(n - 1); factorial(1) _//=> 1_ factorial(5) _//=> 120_ While this is mathematically elegant, it is computational filigree[63] .

Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n *

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00146))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |
```

</details>

### Technical frame 2: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00149))_

> Composing and Decomposing Data

101 **const** factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) _//=> 1_ factorial(6) _//=> 720_

By writing our parameter list as (n, work = 1) =>, we’re stating that if a second parameter is not provided, work is to be bound to 1. We can do similar things with our other tail-recursive functions: **const** length = ([first, ...rest], numberToBeAdded = 0) => first === **undefined** ? numberToBeAdded : length(rest, 1 + numberToB

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00150))_

> 102 **const** [first, second = "two"] = ["one"];


## Related pages

- [[javascriptallonge-mapwith]] - shared statements and technical atoms: Mapwith shares source evidence from Tail Calls (and Default Arguments): Composing and Decomposing Data  94  ## **Tail Calls (and Default Arguments)**  The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustra ... [truncated]; Mapwith shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-recursion]] - shared statements and technical atoms: Recursion shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  104  Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious. ... [truncated]; Recursion shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from Tail Calls (and Default Arguments): | 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 1 ... [truncated] (2 shared atom(s))
- [[javascriptallonge-learn]] - shared technical atoms: Learn shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-length]] - shared technical atoms: Length shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Mutation: Composing and Decomposing Data  121 **const** EMPTY = {}; **const** OneToFive = { first: 1, rest: { first: 2, rest: { first: 3, rest: { first: 4, rest: { first: 5, r ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Tail Calls (and Default Arguments): Composing and Decomposing Data  94  ## **Tail Calls (and Default Arguments)**  The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustra ... [truncated] (1 shared statement(s))
- [[javascriptallonge-list]] - shared statements: List shares source evidence from Copy on Write: Composing and Decomposing Data  138 **const** childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-needn]] - shared statements: Needn shares source evidence from Building Blocks: The first sip: Basic Functions  48  ## **Building Blocks**  When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Building Blocks: The first sip: Basic Functions  48  ## **Building Blocks**  When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-whenever]] - shared statements: Whenever shares source evidence from Copy on Write: Composing and Decomposing Data  138 **const** childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest" ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
