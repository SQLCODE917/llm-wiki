---
page_id: javascriptallonge-problem
page_kind: concept
summary: Problem: 6 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-problem@9b595a15503e1ec14e1e774dd9cffdbf
---

# Problem

What [[javascriptallonge]] covers about problem:

## Statements

### Maybe

- Recipes with Basic Functions

63

## **Maybe**

A common problem in programming is checking for null or undefined (hereafter called “nothing,” while all other values including 0, [] and false will be called “something”). Languages like JavaScript do not strongly enforce the notion that a particular variable or particular property be something, so programs are often written to account for values that may be nothing.

This recipe concerns a pattern that is very common: A function fn takes a value as a parameter, and its behaviour by design is to do nothing if the parameter is nothing: **const** isSomething = (value) => value !== **null** && value !== **void** 0; **const** checksForSomething = (value) => { **if** (isSomething(value)) { _// function's true logic_ } } Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing: **var** something = isSomething(value) ? doesntCheckForSomething(value) : value;

Naturally, there’s a function decorator recipe for that, borrowed from Haskell’s maybe monad[50] , Ruby’s andand[51] , and CoffeeScript’s existential method invocation: **const** maybe = (fn) => **function** (...args) { **if** (args.length === 0) { **return** } **else** { **for** ( **let** arg **of** args) { **if** (arg == **null** ) **return** ; } > 50https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad > 51https://github.com/raganwald/andand _(javascriptallonge.pdf (source-range-83ecb080-00108))_

### Arrays and Destructuring Arguments

- 90

Composing and Decomposing Data **const** flatten = ([first, ...rest]) => { **if** (first === **undefined** ) { **return** []; } **else if** (!Array.isArray(first)) { **return** [first, ...flatten(rest)]; } **else** { **return** [...flatten(first), ...flatten(rest)]; } } flatten(["foo", [3, 4, []]]) _//=> ["foo",3,4]_ Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions.

## **mapping**

Another common problem is applying a function to every element of an array. JavaScript has a built-in function for this, but let’s write our own using linear recursion.

If we want to square each number in a list, we could write: **const** squareAll = ([first, ...rest]) => first === **undefined** ? [] : [first * first, ...squareAll(rest)\ ]; squareAll([1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ And if we wanted to “truthify” each element in a list, we could write: _(javascriptallonge.pdf (source-range-83ecb080-00136))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

108

## **so why arrays**

If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation).

For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases.

## **summary**

Although we showed how to use tail calls to map and fold over arrays with [first, ...rest], in reality this is not how it ought to be done. But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-00157))_

### Copy on Write

- Composing and Decomposing Data

138 **const** childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ Our new at and set functions behave similarly to array[index] and array[index] = value. The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list.

## **copy-on-read**

So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.

**const** rest = ({first, rest}) => copy(rest); **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = rest(parentList); **const** newParentList = set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}} This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don’t need to make a copy because we won’t be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node).

There’s also a bug: What happens when we modify the first element of a list? But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-00191))_

### Interlude: The Carpenter Interviews for a Job

- Served by the Pot: Collections

239

**==> picture [476 x 314] intentionally omitted <==**

**----- Start of picture text -----**<br> 94<br>**----- End of picture text -----**<br>

Christine intoned the question, as if by rote:

Consider a finite checkerboard of unknown size. On each square, we randomly place an arrow pointing to one of its four sides. A chequer is placed randomly on the checkerboard. Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. If the arrow should cause the chequer to move off the edge of the board, the game halts.

The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. “↑, →, ↑, ↓, ↑, →…” Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space.

“So,” The Carpenter asked, “I am to write an algorithm that takes a possibly infinite stream of…” Christine interrupted. “To save time, we have written a template of the solution for you in ECMASCript 2015 notation. Fill in the blanks. Your code should not presume anything about the > 94https://www.flickr.com/photos/stigrudeholm/6710684795 _(javascriptallonge.pdf (source-range-83ecb080-00304))_

- Served by the Pot: Collections

248

“I worked at Thing, and Christine told us about your solution. I had a look at the code you left on the whiteboard. Of course, white-boarding in an interview situation is notoriously unreliable, so small defects are not important. But I couldn’t help but notice that your solution doesn’t actually meet the stated requirements for a different reason:” “The hasCycle function, a/k/a Tortoise and Hare, requires two separate iterators to do its job. Whereas the problem as stated involves a single stream of directions. You’re essentially calling for the player to clone themselves and call out the directions in parallel.” The Carpenter thought about this for a moment. “Kidu, you’re right, that’s a fantastic observation. I should have used a Teleporting Tortoise!” _// implements Teleporting Tortoise // cycle detection algorithm._ **const** hasCycle = (iterable) => { **let** iterator = iterable[Symbol.iterator](), teleportDistance = 1; **while** ( **true** ) { **let** {value, done} = iterator.next(), tortoise = value; **if** (done) **return false** ; **for** ( **let** i = 0; i < teleportDistance; ++i) { **let** {value, done} = iterator.next(), hare = value; **if** (done) **return false** ; **if** (tortoise === hare) **return true** ; } teleportDistance *= 2; } **return false** ; };

Kidu shrugged. “You know, the requirement asked for a finite space algorithm, not a constant state algorithm. Doesn’t it make sense to go with a faster finite space algorithm? There’s no benefit to constant space if finite space is sufficient.” _(javascriptallonge.pdf (source-range-83ecb080-00313))_


## Related pages

- [[javascriptallonge-array]] - shared statements: Array shares source evidence from Arrays and Destructuring Arguments: 90  Composing and Decomposing Data **const** flatten = ([first, ...rest]) => { **if** (first === **undefined** ) { **return** []; } **else if** (!Array.isArray(first ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-programming]] - shared statements: Programming shares source evidence from Maybe: Recipes with Basic Functions  63  ## **Maybe**  A common problem in programming is checking for null or undefined (hereafter called “nothing,” while all other values ... [truncated] (1 shared statement(s))
- [[javascriptallonge-reference]] - shared statements: Reference shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-sequence]] - shared statements: Sequence shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-whenever]] - shared statements: Whenever shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
