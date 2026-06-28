---
page_id: javascriptallonge-version
page_kind: concept
summary: Version: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-version@b8daa493649de17626ff2e9660c0c1df
---

# Version

What [[javascriptallonge]] covers about version:

## Statements

### Foreword to the Six'' edition

- viii

A Pull of the Lever: Prefaces

## **Foreword to the “Six” edition**

ECMAScript 6 (short name: ES6; official name: ECMAScript 2015) was ratified as a standard on June 17. Getting there took a while – in a way, the origins of ES6 date back to the year 2000: After ECMAScript 3 was finished, TC39 (the committee evolving JavaScript) started to work on ECMAScript 4. That version was planned to have numerous new features (interfaces, namespaces, packages, multimethods, etc.), which would have turned JavaScript into a completely new language. After internal conflict, a settlement was reached in July 2008 and a new plan was made – to abandon ECMAScript 4 and to replace it with two upgrades:

- A smaller upgrade would bring a few minor enhancements to ECMAScript 3. This upgrade became ECMAScript 5.

- A larger upgrade would substantially improve JavaScript, but without being as radical as ECMAScript 4. This upgrade became ECMAScript 6 (some features that were initially discussed will show up later, in upcoming ECMAScript versions).

ECMAScript 6 has three major groups of features:

- Better syntax for features that already exist (e.g. via libraries). For example: classes and modules.

- New functionality in the standard library. For example:

- New methods for strings and arrays

- Promises (for asynchronous programming) - Maps and sets

- Completely new features. For example: Generators, proxies and WeakMaps.

With ECMAScript 6, JavaScript has become much larger as a language. _JavaScript Allongé, the “Six” Edition_ is both a comprehensive tour of its features and a rich collection of techniques for making better use of them. You will learn much about functional programming and object-oriented programming. And you’ll do so via ES6 code, handed to you in small, easily digestible pieces.

- Axel Rauschmayer Blogger[2] , trainer[3] and author of “Exploring ES6[4] ” > 2http://www.2ality.com

> 3http://ecmanauten.de

> 4http://exploringjs.com _(javascriptallonge.pdf (source-range-83ecb080-00020))_

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

97

## **converting non-tail-calls to tail-calls**

The obvious solution is push the 1 + work into the call to length. Here’s our first cut: **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysWork(["foo", "bar", "baz"], 0) _//=> 3_

This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that: **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

? numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) **const** length = (n) => lengthDelaysWork(n, 0); Or we could use partial application: **const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** length = callLast(lengthDelaysWork, 0); length(["foo", "bar", "baz"]) _//=> 3_

This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith: _(javascriptallonge.pdf (source-range-83ecb080-00144))_

### Generating Iterables

- 204

Served by the Pot: Collections

_// Iteration_ **const** isIterable = (something) => !!something[Symbol.iterator]; **const** treeIterator = (iterable) => { **const** iterators = [ iterable[Symbol.iterator]() ]; **return** () => { **while** (!!iterators[0]) { **const** iterationResult = iterators[0].next(); **if** (iterationResult.done) { iterators.shift(); } **else if** (isIterable(iterationResult.value)) { iterators.unshift(iterationResult.value[Symbol.iterator]()); } **else** { **return** iterationResult.value; } } **return** ; } } **const** i = treeIterator([1, [2, [3, 4], 5]]); **let** n; **while** (n = i()) { console.log(n) } _//=>_ 1 2 3 4 5

If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next, we’re left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version’s stack is _implicit_ , while the iteration version’s stack is _explicit_ . _(javascriptallonge.pdf (source-range-83ecb080-00269))_

- Served by the Pot: Collections

207

21 34 55 89 144

...

Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspunning the natural linear state. In a generator, we write “do this, then this, then this.” In an iterator, we have to wrap that up and explicitly keep track of what step we’re on.

So we see the same thing: The generation version has state, but it’s implicit in JavaScript’s linear control flow. Whereas the iteration version must make that state explicit.

## **javascript’s generators**

It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript makes this possible.

We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a _generator_ . To write a generator, we write a function, but we make two changes:

1. We declare the function using the function * syntax. Not a fat arrow. Not a plain function.

2. We don’t return values or output them to console.log. We “yield” values using the yield keyword.

When we invoke the function, we get an iterator object back. Let’s start with the degenerate example, the empty iterator:[91] **function** * empty () {}; empty().next() _//=>_ {"done": **true** } When we invoke empty, we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it’s done immediately.

Generator functions can take an argument. Let’s use that to illustrate yield:

> 91We wrote a _generator declaration_ . We can also write const empty = function * () {} to bind an anonymous generator to the empty keyword, but we don’t need to do that here. _(javascriptallonge.pdf (source-range-83ecb080-00272))_


## Related pages

- [[javascriptallonge-length]] - shared statements: Length shares source evidence from Tail Calls (and Default Arguments): Composing and Decomposing Data  97  ## **converting non-tail-calls to tail-calls**  The obvious solution is push the 1 + work into the call to length. Here’s our fir ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
