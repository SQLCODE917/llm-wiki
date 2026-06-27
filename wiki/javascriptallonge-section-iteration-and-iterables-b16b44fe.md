---
page_id: javascriptallonge-section-iteration-and-iterables-b16b44fe
page_kind: source
summary: Iteration and Iterables: 115 source-backed entries and 33 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-iteration-and-iterables-b16b44fe@aa5315ffabd08d20bb34d041a03a0af2
---

# Iteration and Iterables

From [[javascriptallonge]].

## Statements

- Many objects in JavaScript can model collections of things. _(javascriptallonge.pdf (source-range-83ecb080-02363))_
- But sometimes you want to open it up and do things with its contents. _(javascriptallonge.pdf (source-range-83ecb080-02363))_
- Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-83ecb080-02365))_
- Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-83ecb080-02365))_
- We can do the same thing for objects. _(javascriptallonge.pdf (source-range-83ecb080-02367))_
- Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-02375))_
- } function, and that’s where this is bound to the value of stack. _(javascriptallonge.pdf (source-range-83ecb080-02376))_
- Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. _(javascriptallonge.pdf (source-range-83ecb080-02376))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-02377))_
- Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter(). _(javascriptallonge.pdf (source-range-83ecb080-02377))_
- We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method: _(javascriptallonge.pdf (source-range-83ecb080-02388))_
- If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. _(javascriptallonge.pdf (source-range-83ecb080-02393))_
- Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects. _(javascriptallonge.pdf (source-range-83ecb080-02393))_
- Iteration for functions and objects has been around for many, many decades. _(javascriptallonge.pdf (source-range-83ecb080-02396))_
- In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-02397))_
- Fortunately, an iterator object is almost as simple as an iterator function. _(javascriptallonge.pdf (source-range-83ecb080-02400))_
- Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-83ecb080-02400))_
- When working with objects, we do things the object way. _(javascriptallonge.pdf (source-range-83ecb080-02410))_
- But having started by building functional iterators, we understand what is happening underneath the object’s scaffolding. _(javascriptallonge.pdf (source-range-83ecb080-02410))_
- Now our .iterator() method is returning an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02410))_
- Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it. _(javascriptallonge.pdf (source-range-83ecb080-02412))_
- People have been writing iterators since JavaScript was first released in the late 1990s. _(javascriptallonge.pdf (source-range-83ecb080-02412))_
- So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. _(javascriptallonge.pdf (source-range-83ecb080-02413))_
- Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator. _(javascriptallonge.pdf (source-range-83ecb080-02413))_
- Symbols are unique constants that are guaranteed not to conflict with existing strings. _(javascriptallonge.pdf (source-range-83ecb080-02414))_
- Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols.[88] _(javascriptallonge.pdf (source-range-83ecb080-02414))_
- To ensure that the method would not conflict with any existing code, JavaScript provides a _symbol_ . _(javascriptallonge.pdf (source-range-83ecb080-02414))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02415))_
- > 88 You can read more about JavaScript symbols in Axel Rauschmayer’s Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-83ecb080-02416))_
- Our stack does, so instead of binding the existing iterator method to the name iterator, we bind it to the Symbol.iterator. _(javascriptallonge.pdf (source-range-83ecb080-02419))_
- The for...of loop works directly with any object that is _iterable_ , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. _(javascriptallonge.pdf (source-range-83ecb080-02431))_
- And there’s one more thing: You recall that the spread operator (...) can spread the elements of an array in an array literal or as parameters in a function invocation. _(javascriptallonge.pdf (source-range-83ecb080-02437))_
- Now is the time to note that we can spread any iterable. _(javascriptallonge.pdf (source-range-83ecb080-02438))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- That might be very wasteful for extremely large collections. _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-83ecb080-02444))_
- And if we have an infinite collection, spreading is going to fail outright as we’re about to see. _(javascriptallonge.pdf (source-range-83ecb080-02445))_
- There are useful things we can do with iterables representing an infinitely large collection. _(javascriptallonge.pdf (source-range-83ecb080-02449))_
- Attempting to spread an infinite iterable into an array is always going to fail. _(javascriptallonge.pdf (source-range-83ecb080-02455))_
- The iterables we’re discussing represent _ordered collections_ . _(javascriptallonge.pdf (source-range-83ecb080-02457))_
- One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. _(javascriptallonge.pdf (source-range-83ecb080-02457))_
- Iterables needn’t represent ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-02461))_
- This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator], and ensuring that our iterators start at the beginning and work forward. _(javascriptallonge.pdf (source-range-83ecb080-02461))_
- Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- Therefore, RandomNumbers is not an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02466))_
- To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. _(javascriptallonge.pdf (source-range-83ecb080-02467))_
- Every time we get an iterator from an ordered collection, we start iterating from the beginning. _(javascriptallonge.pdf (source-range-83ecb080-02467))_
- Right now, we’re just looking at ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-02467))_
- Here’s mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original:[89] _(javascriptallonge.pdf (source-range-83ecb080-02469))_
- Let’s define some operations on ordered collections. _(javascriptallonge.pdf (source-range-83ecb080-02469))_
- > 89Yes, we also used the name mapWith for working with ordinary collections elsewhere. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- But for the purposes of discussing ideas, we can use the same name twice in two different contexts. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-02470))_
- This illustrates the general pattern of working with ordered collections: We make them _iterables_ , meaning that they have a [Symbol.iterator] method, that returns an _iterator_ . _(javascriptallonge.pdf (source-range-83ecb080-02474))_
- An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order. _(javascriptallonge.pdf (source-range-83ecb080-02474))_
- Many operations on ordered collections return another ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02475))_
- They do so by taking care to iterate over a result freshly every time we get an iterator for them. _(javascriptallonge.pdf (source-range-83ecb080-02475))_
- Numbers is an ordered collection. _(javascriptallonge.pdf (source-range-83ecb080-02480))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. _(javascriptallonge.pdf (source-range-83ecb080-02483))_
- Like mapWith, they preserve the ordered collection semantics of whatever you give them. _(javascriptallonge.pdf (source-range-83ecb080-02496))_
- And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000: _(javascriptallonge.pdf (source-range-83ecb080-02497))_
- As we expect from an ordered collection, each time we iterate over UpTo1000, we begin at the beginning. _(javascriptallonge.pdf (source-range-83ecb080-02500))_
- For completeness, here are two more handy iterable functions. _(javascriptallonge.pdf (source-range-83ecb080-02501))_
- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-02501))_
- like our other operations, rest preserves the ordered collection semantics of its argument. _(javascriptallonge.pdf (source-range-83ecb080-02503))_
- No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-83ecb080-02505))_
- One useful thing is to write a .from function that gathers an iterable into a particular collection type. _(javascriptallonge.pdf (source-range-83ecb080-02508))_
- And we can assign properties to functions with a . _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- We can do the same with our own collections. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- And if we assign a function to a property, we’ve created a method. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- As you recall, functions are mutable objects. _(javascriptallonge.pdf (source-range-83ecb080-02510))_
- Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: _(javascriptallonge.pdf (source-range-83ecb080-02516))_
- _Iterable_ ordered collections can be iterated over or gathered into another collection. _(javascriptallonge.pdf (source-range-83ecb080-02522))_
- Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. _(javascriptallonge.pdf (source-range-83ecb080-02522))_
- Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-02523))_

## Technical atoms

> **const** iter = stack.iterator(); iter().value _//=> "you!"_ iter().value _//=> "to"_
_(source: javascriptallonge.pdf (source-range-83ecb080-02373))_

> Context: And here’s a sum function implemented as a fold over a functional iterator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02378))_

> **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02379))_

> Context: And here’s a sum function implemented as a fold over a functional iterator:
_(context: javascriptallonge.pdf (source-range-83ecb080-02378))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-02380))_

> Context: We can use it with our stack:
_(context: javascriptallonge.pdf (source-range-83ecb080-02381))_

> **const** stack = Stack1();
_(source: javascriptallonge.pdf (source-range-83ecb080-02384))_

> Context: We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02388))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();
_(source: javascriptallonge.pdf (source-range-83ecb080-02389))_

> Context: We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02388))_

> **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02390))_

> Context: We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method:
_(context: javascriptallonge.pdf (source-range-83ecb080-02388))_

> **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-02391))_

> collectionSum(stack) _//=> 6_
_(source: javascriptallonge.pdf (source-range-83ecb080-02392))_

> **const** stack = Stack2();
_(source: javascriptallonge.pdf (source-range-83ecb080-02404))_

> **const** collectionSum = (collection) => { **const** iterator = collection.iterator();
_(source: javascriptallonge.pdf (source-range-83ecb080-02406))_

> **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02407))_

> **while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum }
_(source: javascriptallonge.pdf (source-range-83ecb080-02408))_

> collectionSum(stack) _//=> 2015_
_(source: javascriptallonge.pdf (source-range-83ecb080-02409))_

> **const** collectionSum = (collection) => { **const** iterator = collection[Symbol.iterator]();
_(source: javascriptallonge.pdf (source-range-83ecb080-02424))_

> **let** eachIteration, sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02425))_

> **while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 2015_
_(source: javascriptallonge.pdf (source-range-83ecb080-02426))_

> Context: Indeed we do. Behold the for...of loop:
_(context: javascriptallonge.pdf (source-range-83ecb080-02428))_

> **const** iterableSum = (iterable) => { **let** sum = 0;
_(source: javascriptallonge.pdf (source-range-83ecb080-02429))_

> Context: Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal:
_(context: javascriptallonge.pdf (source-range-83ecb080-02438))_

> - ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02439))_

> Context: And we can also spread the elements of an array literal into parameters:
_(context: javascriptallonge.pdf (source-range-83ecb080-02440))_

> **const** firstAndSecondElement = (first, second) => ({first, second})
_(source: javascriptallonge.pdf (source-range-83ecb080-02441))_

> Context: And we can also spread the elements of an array literal into parameters:
_(context: javascriptallonge.pdf (source-range-83ecb080-02440))_

> firstAndSecondElement(...stack) _//=> {"first":5,"second":10}_
_(source: javascriptallonge.pdf (source-range-83ecb080-02442))_

> Context: Iterables needn’t represent finite collections:
_(context: javascriptallonge.pdf (source-range-83ecb080-02447))_

> **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }
_(source: javascriptallonge.pdf (source-range-83ecb080-02448))_

> Context: There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them:
_(context: javascriptallonge.pdf (source-range-83ecb080-02449))_

> ['all the numbers', ...Numbers] _//=> infinite loop!_
_(source: javascriptallonge.pdf (source-range-83ecb080-02452))_

> Context: The iterables we’re discussing represent _ordered collections_ . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-02457))_

> **const** abc = ["a", "b", "c"];
_(source: javascriptallonge.pdf (source-range-83ecb080-02458))_

> Context: Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith:
_(context: javascriptallonge.pdf (source-range-83ecb080-02475))_

> **const** Evens = mapWith((x) => 2 * x, Numbers);
_(source: javascriptallonge.pdf (source-range-83ecb080-02476))_

> Context: Mind you, we can also map non-collection iterables, like RandomNumbers:
_(context: javascriptallonge.pdf (source-range-83ecb080-02484))_

> **const** ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers);
_(source: javascriptallonge.pdf (source-range-83ecb080-02485))_

> mapWith can get a new iterator from RandomNumbers each time we iterate over ZeroesToNines, but if RandomNumbers doesn’t behave like an ordered collection, that’s not mapWith’s fault.
_(source: javascriptallonge.pdf (source-range-83ecb080-02491))_

> Context: And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000:
_(context: javascriptallonge.pdf (source-range-83ecb080-02497))_

> [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] [...UpTo1000] _//=>_ [1,81,121,361,441,841,961]
_(source: javascriptallonge.pdf (source-range-83ecb080-02499))_

> Context: For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest]:
_(context: javascriptallonge.pdf (source-range-83ecb080-02501))_

> **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **const** rest = (iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **return** iterator; } });
_(source: javascriptallonge.pdf (source-range-83ecb080-02502))_

> Context: One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in Array class already has one:
_(context: javascriptallonge.pdf (source-range-83ecb080-02508))_

> Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_
_(source: javascriptallonge.pdf (source-range-83ecb080-02509))_

> Stack3.from = **function** (iterable) { **const** stack = **this** ();
_(source: javascriptallonge.pdf (source-range-83ecb080-02512))_

> Pair1.from = (iterable) => ( **function** iterationToList (iteration) { **const** {done, value} = iteration.next();
_(source: javascriptallonge.pdf (source-range-83ecb080-02514))_

> Context: Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:
_(context: javascriptallonge.pdf (source-range-83ecb080-02516))_

> **const** numberList = Pair1.from(untilWith((x) => x > 10, Numbers));
_(source: javascriptallonge.pdf (source-range-83ecb080-02517))_

> Context: Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that:
_(context: javascriptallonge.pdf (source-range-83ecb080-02516))_

> Pair1.from(Squares) _//=> {"first":0,_ "rest":{"first":1, "rest":{"first":4, "rest":{ ...
_(source: javascriptallonge.pdf (source-range-83ecb080-02518))_
