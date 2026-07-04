---
page_id: javascriptallonge-section-iteration-and-iterables-8f5e9b29
page_kind: source
page_family: section-reference
summary: Iteration and Iterables: 64 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-iteration-and-iterables-8f5e9b29@b3d40d6018ee5f8ae56cf9bca034aa9b
---

# Iteration and Iterables

From [[javascriptallonge]].

## Statements

- Served by the Pot: Collections 

183 

## **Iteration and Iterables** 

**==> picture [469 x 313] intentionally omitted <==**

**Coffee Labels at the Saltspring Coffee Processing Facility** 

Many objects in JavaScript can model collections of things. A collection is like a box containing stuff. Sometimes you just want to move the box around. But sometimes you want to open it up and do things with its contents. 

Things like “put a label on every bag of coffee in this box,” Or, “Open the box, take out the bags of decaf, and make a new box with just the decaf.” Or, “go through the bags in this box, and take out the first one marked ‘Espresso’ that contains at least 454 grams of beans.” 

All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections. 

## **a look back at functional iterators** 

When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here’s a stack that has its own functional iterator method: _(javascriptallonge.pdf (source-range-af806fb1-00238))_
- Served by the Pot: Collections 

185 

**const** iter = stack.iterator(); iter().value _//=> "you!"_ iter().value _//=> "to"_ 

The way we’ve written .iterator as a method, each object knows how to return an iterator for itself. 

The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is defined with a fat arrow () => { ... }. What is the value of this within that function? 

Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that’s where this is bound to the value of stack. 

Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). 

And here’s a sum function implemented as a fold over a functional iterator: 

**const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0; 

**while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } 

We can use it with our stack: _(javascriptallonge.pdf (source-range-af806fb1-00240))_
- 186 

Served by the Pot: Collections 

**const** stack = Stack1(); 

stack.push(1); stack.push(2); stack.push(3); 

iteratorSum(stack.iterator()) 

_//=> 6_ 

We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method: 

**const** collectionSum = (collection) => { **const** iterator = collection.iterator(); 

**let** eachIteration, sum = 0; 

**while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } 

collectionSum(stack) _//=> 6_ 

If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. 

This is a good thing. 

## **iterator objects** 

Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators. 

In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-af806fb1-00241))_
- 187 

Served by the Pot: Collections 

Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. Like this: 

**const** Stack2 = () => ({ array: [], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return** value }, isEmpty () { **return this** .index < 0 }, iterator () { **let** iterationIndex = **this** .index; **return** { next () { **if** (iterationIndex > **this** .index) { iterationIndex = **this** .index; } **if** (iterationIndex < 0) { **return** {done: **true** }; } **else** { **return** {done: **false** , value: **this** .array[iterationIndex--]} } } } } }); _(javascriptallonge.pdf (source-range-af806fb1-00242))_
- Served by the Pot: Collections 

188 

**const** stack = Stack2(); 

stack.push(2000); stack.push(10); stack.push(5) 

**const** collectionSum = (collection) => { **const** iterator = collection.iterator(); 

**let** eachIteration, sum = 0; 

**while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } 

collectionSum(stack) _//=> 2015_ 

Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object’s scaffolding. 

## **iterables** 

People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. 

So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. 

To ensure that the method would not conflict with any existing code, JavaScript provides a _symbol_ . Symbols are unique constants that are guaranteed not to conflict with existing strings. Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols.[88] 

The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. 

> 88 You can read more about JavaScript symbols in Axel Rauschmayer’s Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-af806fb1-00243))_
- 189 

Served by the Pot: Collections 

Our stack does, so instead of binding the existing iterator method to the name iterator, we bind it to the Symbol.iterator. We’ll do that using the [ ] syntax for using an expression as an object literal key: 

**const** Stack3 = () => ({ array: [], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return** value }, isEmpty () { **return this** .index < 0 }, [Symbol.iterator] () { **let** iterationIndex = **this** .index; **return** { next () { **if** (iterationIndex > **this** .index) { iterationIndex = **this** .index; } **if** (iterationIndex < 0) { **return** {done: **true** }; } **else** { **return** {done: **false** , value: **this** .array[iterationIndex--]} } } } } }); **const** stack = Stack3(); _(javascriptallonge.pdf (source-range-af806fb1-00244))_
- 190 

Served by the Pot: Collections 

stack.push(2000); stack.push(10); stack.push(5) 

**const** collectionSum = (collection) => { **const** iterator = collection[Symbol.iterator](); 

**let** eachIteration, sum = 0; 

**while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 2015_ 

Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? 

Indeed we do. Behold the for...of loop: 

**const** iterableSum = (iterable) => { **let** sum = 0; 

**for** ( **const** num **of** iterable) { sum += num; } **return** sum } iterableSum(stack) _//=> 2015_ 

The for...of loop works directly with any object that is _iterable_ , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here’s another linked list, this one is iterable: _(javascriptallonge.pdf (source-range-af806fb1-00245))_
- 192 

Served by the Pot: Collections 

As we can see, we can use for...of with linked lists just as easily as with stacks. And there’s one more thing: You recall that the spread operator (...) can spread the elements of an array in an array literal or as parameters in a function invocation. 

Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal: 

- ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_ 

And we can also spread the elements of an array literal into parameters: 

**const** firstAndSecondElement = (first, second) => ({first, second}) 

firstAndSecondElement(...stack) _//=> {"first":5,"second":10}_ 

This can be extremely useful. 

One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. 

And if we have an infinite collection, spreading is going to fail outright as we’re about to see. 

## **iterables out to infinity** 

Iterables needn’t represent finite collections: 

**const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } } 

There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them: _(javascriptallonge.pdf (source-range-af806fb1-00247))_
- 193 

Served by the Pot: Collections 

['all the numbers', ...Numbers] _//=> infinite loop!_ 

firstAndSecondElement(...Numbers) 

_//=> infinite loop!_ 

Attempting to spread an infinite iterable into an array is always going to fail. 

## **ordered collections** 

The iterables we’re discussing represent _ordered collections_ . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example: 

**const** abc = ["a", "b", "c"]; 

**for** ( **const** i **of** abc) { console.log(i) } _//=>_ a b c 

**for** ( **const** i **of** abc) { console.log(i) } _//=>_ a b c 

This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator], and ensuring that our iterators start at the beginning and work forward. Iterables needn’t represent ordered collections. We could make an infinite iterable representing random numbers: _(javascriptallonge.pdf (source-range-af806fb1-00248))_
- 194 

Served by the Pot: Collections 

**const** RandomNumbers = { [Symbol.iterator]: () => ({ next () { **return** {value: Math.random()}; } }) } **for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.494052127469331 0.835459444206208 0.1408337657339871 ... 

**for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.7845381607767195 0.4956772483419627 0.20259276474826038 ... 

Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection. 

Right now, we’re just looking at ordered collections. To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. Every time we get an iterator from an ordered collection, we start iterating from the beginning. 

## **operations on ordered collections** 

Let’s define some operations on ordered collections. Here’s mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original:[89] 

> 89Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. _(javascriptallonge.pdf (source-range-af806fb1-00249))_
- 195 

Served by the Pot: Collections 

**const** mapWith = (fn, collection) => ({ [Symbol.iterator] () { **const** iterator = collection[Symbol.iterator](); **return** { next () { **const** {done, value} = iterator.next(); **return** ({done, value: done ? **undefined** : fn(value)}); } } } }); 

This illustrates the general pattern of working with ordered collections: We make them _iterables_ , meaning that they have a [Symbol.iterator] method, that returns an _iterator_ . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. 

Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith: 

**const** Evens = mapWith((x) => 2 * x, Numbers); 

**for** ( **const** i **of** Evens) { console.log(i) } _//=>_ 0 2 4 ... **for** ( **const** i **of** Evens) { console.log(i) } _//=>_ 0 2 4 ... _(javascriptallonge.pdf (source-range-af806fb1-00250))_
- 196 

Served by the Pot: Collections 

Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens. Evens works just as if we’d written this: 

**const** Evens = { [Symbol.iterator] () { **const** iterator = Numbers[Symbol.iterator](); **return** { next () { **const** {done, value} = iterator.next(); **return** ({done, value: done ? **undefined** : 2 *value}); } } } }; 

Every time we write for (const i of Evens), JavaScript calls Evens[Symbol.iterator](). That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens), and that means that iterator starts at the beginning of Numbers. 

So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a _collection operation_ . 

Mind you, we can also map non-collection iterables, like RandomNumbers: 

**const** ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers); 

**for** ( **const** i **of** ZeroesToNines) { console.log(i) } _//=>_ 5 1 9 ... 

**for** ( **const** i **of** ZeroesToNines) { console.log(i) } _//=>_ 3 _(javascriptallonge.pdf (source-range-af806fb1-00251))_
- 198 

Served by the Pot: Collections 

Like mapWith, they preserve the ordered collection semantics of whatever you give them. 

And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000: 

**const** Squares = mapWith((x) => x * x, Numbers); **const** EndWithOne = filterWith((x) => x % 10 === 1, Squares); **const** UpTo1000 = untilWith((x) => (x > 1000), EndWithOne); 

[...UpTo1000] _//=>_ [1,81,121,361,441,841,961] [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] 

As we expect from an ordered collection, each time we iterate over UpTo1000, we begin at the beginning. 

For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest]: 

**const** first = (iterable) => iterable[Symbol.iterator]().next().value; **const** rest = (iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **return** iterator; } }); 

like our other operations, rest preserves the ordered collection semantics of its argument. 

## **from** 

Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function? No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-af806fb1-00253))_
- Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-af806fb1-00238))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-af806fb1-00240))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-af806fb1-00241))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-af806fb1-00247))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-af806fb1-00249))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-af806fb1-00251))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-af806fb1-00251))_
