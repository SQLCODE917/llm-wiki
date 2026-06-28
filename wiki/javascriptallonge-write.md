---
page_id: javascriptallonge-write
page_kind: concept
summary: Write: 10 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-write@6421416b9096f58a87f0bea855802d9e
---

# Write

What [[javascriptallonge]] covers about write:

## Statements

### As Little As Possible About Functions, But No Less

- 13

The first sip: Basic Functions

## (() => {})()

_//=> undefined_

We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] Something like: { statement[1] ; statement[2] ; statement[3] ; ... ; statement[n] } We haven’t discussed these _statements_ . What’s a statement?

There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: () => { 1 + 1; 2 + 2 } But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: (() => { 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:

> 21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00050))_

### Copy on Write

- Composing and Decomposing Data

136

Whereas if you have a linked list, and you take it’s “rest,” your “child” list shares its nodes with the “parent” list. And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent.

Let’s confirm our understanding: **const** parentArray = [1, 2, 3]; **const** [aFirst, ...childArray] = parentArray; parentArray[2] = "three"; childArray[0] = "two"; parentArray _//=> [1,2,"three"]_ childArray _//=> ["two",3]_ **const** EMPTY = { first: {}, rest: {} }; **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = parentList.rest; parentList.rest.rest.first = "three"; childList.first = "two"; parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ This is remarkably unsafe. If we _know_ that a list doesn’t share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We’ll end up reinventing reference counting and garbage collection.

## **a few utilities**

before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-00189))_

- Composing and Decomposing Data

140

Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.— Wikipedia[73] Like all strategies, it makes a tradeoff: It’s much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren’t sharing, it’s more expensive.

Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we’re done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write.

> 73https://en.wikipedia.org/wiki/Copy-on-write _(javascriptallonge.pdf (source-range-83ecb080-00193))_

### Functional Iterators

- Composing and Decomposing Data

150 **const** FibonacciIterator = () => { **let** previous = 0, current = 1; **return** () => { **const** value = current; [previous, current] = [current, current + previous]; **return** {done: **false** , value}; }; }; **const** fib = FibonacciIterator() fib().value _//=> 1_ fib().value _//=> 1_ fib().value _//=> 2_ fib().value _//=> 3_ fib().value _//=> 5_

A function that starts with a seed and expands it into a data structure is called an _unfold_ . It’s the opposite of a fold. It’s possible to write a generic unfold mechanism, but let’s pass on to what we can do with unfolded iterators.

For starters, we can map an iterator, just like we map a collection: **const** mapIteratorWith = (fn, iterator) => () => { **const** {done, value} = iterator(); **return** ({done, value: done ? **undefined** : fn(value)}); } **const** squares = mapIteratorWith((x) => x * x, NumberIterator(1)); squares().value _//=> 1_ squares().value _(javascriptallonge.pdf (source-range-83ecb080-00205))_

### Making Data Out Of Functions

- 162

Composing and Decomposing Data

_//=> 2_ **return** l123(rest)(rest)(first) _//=> 3_

We write them in a backwards way, but they seem to work. How about length?

**const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest)); length(l123) _//=> 3_ And mapWith? **const** reverse = (aPair, delayed = EMPTY) => aPair === EMPTY ? delayed : reverse(aPair(rest), pair(aPair(first))(delayed)); **const** mapWith = (fn, aPair, delayed = EMPTY) => aPair === EMPTY ? reverse(delayed) : mapWith(fn, aPair(rest), pair(fn(aPair(first)))(delayed)); **const** doubled = mapWith((x) => x * 2, l123) doubled(first) _//=> 2_ doubled(rest)(first) _//=> 4_ doubled(rest)(rest)(first) _//=> 6_

Presto, **we can use pure functions to represent a linked list** . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-00218))_

### Flip

- Recipes with Data

173 **const** flipAndCurry = (fn) => (first) => (second) => fn(second, first);

Sometimes you want to flip, but not curry: **const** flip = (fn) => (first, second) => fn(second, first);

This is gold. Consider how we define mapWith now: **var** mapWith = flipAndCurry(map);

Much nicer!

## **self-currying flip**

Sometimes we’ll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We _could_ make that into flip: **const** flip = (fn) => **function** (first, second) { **if** (arguments.length === 2) { **return** fn(second, first); } **else** { **return function** (second) { **return** fn(second, first); }; }; };

Now if we write mapWith = flip(map), we can call mapWith(fn, list) or mapWith(fn)(list), our choice.

## **flipping methods**

When we learn about context and methods, we’ll see that flip throws the current context away, so it can’t be used to flip methods. A small alteration gets the job done: _(javascriptallonge.pdf (source-range-83ecb080-00232))_

### Iteration and Iterables

- 186

Served by the Pot: Collections **const** stack = Stack1(); stack.push(1); stack.push(2); stack.push(3); iteratorSum(stack.iterator()) _//=> 6_

We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method: **const** collectionSum = (collection) => { **const** iterator = collection.iterator(); **let** eachIteration, sum = 0; **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 6_

If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

This is a good thing.

## **iterator objects**

Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators.

In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-00250))_

- Served by the Pot: Collections

188 **const** stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) **const** collectionSum = (collection) => { **const** iterator = collection.iterator(); **let** eachIteration, sum = 0; **while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 2015_

Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object’s scaffolding.

## **iterables**

People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it.

So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator.

To ensure that the method would not conflict with any existing code, JavaScript provides a _symbol_ . Symbols are unique constants that are guaranteed not to conflict with existing strings. Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols.[88] The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.

> 88 You can read more about JavaScript symbols in Axel Rauschmayer’s Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-83ecb080-00252))_

### Generating Iterables

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

### Interlude: The Carpenter Interviews for a Job

- Served by the Pot: Collections

239

**==> picture [476 x 314] intentionally omitted <==**

**----- Start of picture text -----**<br> 94<br>**----- End of picture text -----**<br>

Christine intoned the question, as if by rote:

Consider a finite checkerboard of unknown size. On each square, we randomly place an arrow pointing to one of its four sides. A chequer is placed randomly on the checkerboard. Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. If the arrow should cause the chequer to move off the edge of the board, the game halts.

The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. “↑, →, ↑, ↓, ↑, →…” Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space.

“So,” The Carpenter asked, “I am to write an algorithm that takes a possibly infinite stream of…” Christine interrupted. “To save time, we have written a template of the solution for you in ECMASCript 2015 notation. Fill in the blanks. Your code should not presume anything about the > 94https://www.flickr.com/photos/stigrudeholm/6710684795 _(javascriptallonge.pdf (source-range-83ecb080-00304))_


## Related pages

- [[javascriptallonge-code]] - shared statements: Code shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (2 shared statement(s))
- [[javascriptallonge-algorithm]] - shared statements: Algorithm shares source evidence from Interlude: The Carpenter Interviews for a Job: Served by the Pot: Collections  239  **==> picture [476 x 314] intentionally omitted <==**  **----- Start of picture text -----**<br> 94<br>**----- End of picture te ... [truncated] (1 shared statement(s))
- [[javascriptallonge-const]] - shared statements: Const shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-game]] - shared statements: Game shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-generator]] - shared statements: Generator shares source evidence from Generating Iterables: Served by the Pot: Collections  207  21 34 55 89 144  ...  Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspunning ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Iteration and Iterables: Served by the Pot: Collections  188 **const** stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) **const** collectionSum = (collection) => { **const** ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-list]] - shared statements: List shares source evidence from Copy on Write: Composing and Decomposing Data  136  Whereas if you have a linked list, and you take it’s “rest,” your “child” list shares its nodes with the “parent” list. And ther ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Flip: Recipes with Data  173 **const** flipAndCurry = (fn) => (first) => (second) => fn(second, first);  Sometimes you want to flip, but not curry: **const** flip = (fn) = ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pass]] - shared statements: Pass shares source evidence from Functional Iterators: Composing and Decomposing Data  150 **const** FibonacciIterator = () => { **let** previous = 0, current = 1; **return** () => { **const** value = current; [previous, ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-programmer]] - shared statements: Programmer shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
