---
page_id: javascriptallonge-implementation
page_kind: concept
summary: Implementation: 7 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-implementation@adf5df11bf6fac3653738447fc80be5f
---

# Implementation

What [[javascriptallonge]] covers about implementation:

## Statements

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

### Building Blocks

- The first sip: Basic Functions

49

## **partial application**

Another basic building block is _partial application_ . When a function takes multiple arguments, we “apply” the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can’t get the final value, but we can get a function that represents _part_ of our application.

Code is easier than words for this. The Underscore[39] library provides a higher-order function called _map_ .[40] It applies another function to each element of an array, like this:

_.map([1, 2, 3], (n) => n * n) _//=> [1, 4, 9]_ We don’t want to fool around writing _., so we can use it by writing:[41] This code implements a partial application of the map function by applying the function (n) => n * n as its second argument: **const** squareAll = (array) => map(array, (n) => n * n);

The resulting function–squareAll–is still the map function, it’s just that we’ve applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**const** mapWith = (fn) => (array) => map(array, fn); **const** squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) _//=> [1, 4, 9]_ We’ll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

> 39http://underscorejs.org

> 40Modern JavaScript implementations provide a map method for arrays, but Underscore’s implementation also works with older browsers if you are working with that headache.

> 41If we don’t want to sort out Underscore, we can also write the following: const map = (a, fn) => a.map(fn);, and trust that it works even though we haven’t discussed methods yet. const map = _.map; _(javascriptallonge.pdf (source-range-83ecb080-00087))_

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

95 depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]).

This keeps on happening, so that JavaScript collects the values 1, 2, 3, 4, and 5 plus housekeeping information by the time it calls mapWith((x) => x * x, []). It can start assembling the resulting array and start discarding the information it is saving.

That information is saved on a _call stack_ , and it is quite expensive. Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called _call frames_ , and they include the place where the function was called, an environment, and so on).

In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error.

mapWith((x) => x * x, [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99 ]) _//=> ???_

Is there a better way? Yes. In fact, there are several better ways. Making algorithms faster is a very highly studied field of computer science. The one we’re going to look at here is called _tail-call optimization_ , or “TCO.” _(javascriptallonge.pdf (source-range-83ecb080-00142))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

105

**==> picture [469 x 372] intentionally omitted <==**

**The IBM 704**

## **some history**

Once upon a time, there was a programming language called Lisp[65] , an acronym for LISt Processing.[66] Lisp was one of the very first high-level languages, the very first implementation was written for the IBM 704[67] computer. (The very first FORTRAN implementation was also written for the 704).

The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. The CPU’s instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register.

> 65https://en.wikipedia.org/wiki/Lisp_

> 66Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. 67https://en.wikipedia.org/wiki/IBM_704 _(javascriptallonge.pdf (source-range-83ecb080-00154))_

### Plain Old JavaScript Objects

- Composing and Decomposing Data

114 **const** description = ({name: { first: given }, occupation: { title: title } }) => ` **${** given **}** is a **${** title **}** `; description(user) _//=> "Reginald is a Author"_

Terrible grammar and capitalization, but let’s move on. It is very common to write things like title: title when destructuring objects. When the label is a valid variable name, it’s often the most obvious variable name as well. So JavaScript supports a further syntactic optimization: **const** description = ({name: { first }, occupation: { title } }) => ` **${** first **}** is a **${** title **}** `; description(user) _//=> "Reginald is a Author"_ And that same syntax works for literals: **const** abbrev = ({name: { first, last }, occupation: { title } }) => { **return** { first, last, title}; } abbrev(user) _//=> {"first":"Reginald","last":"Braithwaite","title":"Author"}_

## **revisiting linked lists**

Earlier, we used two-element arrays as nodes in a linked list: **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;

In essence, this simple implementation used functions to create an abstraction with named elements. But now that we’ve looked at objects, we can use an object instead of a two-element array. While we’re at it, let’s use contemporary names. So our linked list nodes will be formed from { first, rest } In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } }.

We can then perform the equivalent of [first, ...rest] with direct property accessors: _(javascriptallonge.pdf (source-range-83ecb080-00164))_

### Making Data Out Of Functions

- Composing and Decomposing Data

166 So what _is_ interesting about this? What nags at our brain as we’re falling asleep after working our way through this?

## **a return to backward thinking**

To make pairs work, we did things _backwards_ , we passed the first and rest functions to the pair, and the pair called our function. As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y).

But we could have done something completely different. We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair.

The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it: **const** first = K, second = K(I), pair = (first) => (second) => { **const** pojo = {first, second}; **return** (selector) => selector(pojo.first)(pojo.second); }; **const** latin = pair("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_

This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. The same thing happens with our lists. Here’s length for lists: **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) );

We’re passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-00222))_

### Generating Iterables

- 204

Served by the Pot: Collections

_// Iteration_ **const** isIterable = (something) => !!something[Symbol.iterator]; **const** treeIterator = (iterable) => { **const** iterators = [ iterable[Symbol.iterator]() ]; **return** () => { **while** (!!iterators[0]) { **const** iterationResult = iterators[0].next(); **if** (iterationResult.done) { iterators.shift(); } **else if** (isIterable(iterationResult.value)) { iterators.unshift(iterationResult.value[Symbol.iterator]()); } **else** { **return** iterationResult.value; } } **return** ; } } **const** i = treeIterator([1, [2, [3, 4], 5]]); **let** n; **while** (n = i()) { console.log(n) } _//=>_ 1 2 3 4 5

If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next, we’re left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version’s stack is _implicit_ , while the iteration version’s stack is _explicit_ . _(javascriptallonge.pdf (source-range-83ecb080-00269))_


## Related pages

- [[javascriptallonge-combinator]] - shared statements: Combinator shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (1 shared statement(s))
- [[javascriptallonge-decorator]] - shared statements: Decorator shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function-decorator]] - shared statements: Function Decorator shares source evidence from Combinators and Function Decorators: The first sip: Basic Functions  46  In this book, we will be using a looser definition of “combinator:” Higher-order pure functions that take only functions as argum ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Building Blocks: The first sip: Basic Functions  49  ## **partial application**  Another basic building block is _partial application_ . When a function takes multiple arguments, we ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
