---
page_id: javascriptallonge-method
page_kind: concept
summary: Method: 10 statement(s) and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-method@43ac31b43cb36674901c96eb089f3a85
---

# Method

What [[javascriptallonge]] covers about method:

## Statements

### Tail Calls (and Default Arguments)

- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. _(javascriptallonge.pdf (source-range-31a4cf47-00964))_

### flipping methods

- When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done: _(javascriptallonge.pdf (source-range-31a4cf47-01470))_

### Like this:

- Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object's scaffolding. _(javascriptallonge.pdf (source-range-31a4cf47-01552))_

### iterables

- To ensure that the method would not conflict with any existing code, JavaScript provides a symbol . Symbols are unique constants that are guaranteed not to conflict with existing strings. Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols. 88 _(javascriptallonge.pdf (source-range-31a4cf47-01556))_

- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-31a4cf47-01557))_

### Generating Iterables

- Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it's done. _(javascriptallonge.pdf (source-range-31a4cf47-01626))_

### Lazy and Eager Collections

- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack _(javascriptallonge.pdf (source-range-31a4cf47-01764))_

- Over time, this informal 'interface' for collections grows by accretion. Some methods are only added to a few collections, some are added to all. But our objects grow fatter and fatter. We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-31a4cf47-01766))_

### implementing methods with iteration

- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-31a4cf47-01771))_


## Technical atoms

### Technical frame 1: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00966))_

> Is there a better way? Yes. In fact, there are several better ways. Making algorithms faster is a very highly studied field of computer science. The one we're going to look at here is called tail-call optimization , or 'TCO.'

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00965))_

```
mapWith((x) => x * x, [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99 ]) //=> ???
```

### Technical frame 2: flipping methods

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01470))_

> When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01471))_

```
const flipAndCurry = (fn) => (first) => function (second) { return fn.call( this , second, first); } const flip = (fn) => function (first, second) { return fn.call( this , second, first); } const flip = (fn) => function (first, second) { if (arguments.length === 2) { return fn.call( this , second, first); } else { return function (second) { return fn.call( this , second, first); }; }; };
```

### Technical frame 3: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01562))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01560))_

```
const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, [Symbol.iterator] () { let iterationIndex = this .index; return { next () { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } }); const stack = Stack3();
```

### Technical frame 4: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01562))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01561))_

```
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```

### Technical frame 5: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01564))_

> As we can see, we can use for...of with linked lists just as easily as with stacks. And there's one more thing: You recall that the spread operator ( ... ) can spread the elements of an array in an array literal or as parameters in a function invocation.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01563))_

```
const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, [Symbol.iterator] () { let currentPair = this ; return { next () { if (currentPair.isEmpty()) { return {done: true } } else { const value = currentPair.first; currentPair = currentPair.rest; return {done: false , value} } } } } }); const list = (...elements) => { const [first, ...rest] = elements; return elements.length === 0 ? EMPTY : Pair1(first, list(...rest)) } const someSquares = list(1, 4, 9, 16, 25); iterableSum(someSquares) //=> 55
```

### Technical frame 6: Generating Iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01630))_

> Well, we've written our iterator as a server . It waits until given a request, and then it returns exactly one item. Then it waits for the next request. There is no concept of pushing numbers out from the iterator, just waiting until a number is pulled out of the iterator by whatever code consumes numbers.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01627))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.


## Related pages

- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from Like this:: Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterato ... [truncated]; Iterator shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (3 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Object shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-symbol]] - shared statements and technical atoms: Symbol shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Symbol shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Expression shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Tail Calls (and Default Arguments): In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error.; Array shares technical record from Tail Calls (and Default Arguments): mapWith((x) => x * x, [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated]; Function shares technical record from Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-functional]] - shared statements and technical atoms: Functional shares source evidence from Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated]; Functional shares technical record from Generating Iterables: Iterators have to arrange its own state such that when you call them, they compute and return the next item. (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-learn]] - shared statements and technical atoms: Learn shares source evidence from flipping methods: When we learn about context and methods, we'll see that flip throws the current context away, so it can't be used to flip methods. A small alteration gets the job done:; Learn shares technical record from flipping methods: const flipAndCurry = (fn) => (first) => function (second) { return fn.call( this , second, first); } const flip = (fn) => function (first, second) { return fn.call( ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-instead]] - shared technical atoms: Instead shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (2 shared atom(s))
- [[javascriptallonge-directly]] - shared technical atoms: Directly shares technical record from iterables: const EMPTY = { isEmpty: () => true }; const isEmpty = (node) => node === EMPTY; const Pair1 = (first, rest = EMPTY) => ({ first, rest, isEmpty () { return false }, ... [truncated] (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))
- [[javascriptallonge-functional-iterator]] - shared statements: Functional Iterators shares source evidence from Generating Iterables: Let's consider how they work. Whether it's a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly unt ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
