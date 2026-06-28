---
page_id: javascriptallonge-iterator
page_kind: concept
summary: Iterator: 17 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iterator@f399f55678121ae91277888cd51121ea
---

# Iterator

What [[javascriptallonge]] covers about iterator:

## Statements

### Functional Iterators

- Composing and Decomposing Data

153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);

This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: **const** firstInArray = (fn, array) => array.filter(fn)[0];

JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy.

## **caveat**

Please note that unlike most of the other functions discussed in this book, iterators are _stateful_ . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you’re changing the state of the original!

For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-00208))_

### Iteration and Iterables

- Served by the Pot: Collections

185 **const** iter = stack.iterator(); iter().value _//=> "you!"_ iter().value _//=> "to"_ The way we’ve written .iterator as a method, each object knows how to return an iterator for itself.

The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is defined with a fat arrow () => { ... }. What is the value of this within that function?

Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that’s where this is bound to the value of stack.

Therefore, the iterator function returned by the .iterator() method has this bound to the stack object, even though we call it with iter().

And here’s a sum function implemented as a fold over a functional iterator: **const** iteratorSum = (iterator) => { **let** eachIteration, sum = 0; **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } We can use it with our stack: _(javascriptallonge.pdf (source-range-83ecb080-00249))_

- 187

Served by the Pot: Collections

Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. Like this: **const** Stack2 = () => ({ array: [], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return** value }, isEmpty () { **return this** .index < 0 }, iterator () { **let** iterationIndex = **this** .index; **return** { next () { **if** (iterationIndex > **this** .index) { iterationIndex = **this** .index; } **if** (iterationIndex < 0) { **return** {done: **true** }; } **else** { **return** {done: **false** , value: **this** .array[iterationIndex--]} } } } } }); _(javascriptallonge.pdf (source-range-83ecb080-00251))_

- Served by the Pot: Collections

188 **const** stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) **const** collectionSum = (collection) => { **const** iterator = collection.iterator(); **let** eachIteration, sum = 0; **while** ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 2015_

Now our .iterator() method is returning an iterator object. When working with objects, we do things the object way. But having started by building functional iterators, we understand what is happening underneath the object’s scaffolding.

## **iterables**

People have been writing iterators since JavaScript was first released in the late 1990s. Since there was no particular standard way to do it, people used all sorts of methods, and their methods returned all sorts of things: Objects with various interfaces, functional iterators, you name it.

So, when a standard way to write iterators was added to the JavaScript language, it didn’t make sense to use a method like .iterator() for it: That would conflict with existing code. Instead, the language encourages new code to be written with a different name for the method that a collection object uses to return its iterator.

To ensure that the method would not conflict with any existing code, JavaScript provides a _symbol_ . Symbols are unique constants that are guaranteed not to conflict with existing strings. Symbols are a longstanding technique in programming going back to Lisp, where the GENSYM function generated… You guessed it… Symbols.[88] The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.

> 88 You can read more about JavaScript symbols in Axel Rauschmayer’s Symbols in ECMAScript 2015. _(javascriptallonge.pdf (source-range-83ecb080-00252))_

- 194

Served by the Pot: Collections **const** RandomNumbers = { [Symbol.iterator]: () => ({ next () { **return** {value: Math.random()}; } }) } **for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.494052127469331 0.835459444206208 0.1408337657339871 ...

**for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.7845381607767195 0.4956772483419627 0.20259276474826038 ...

Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection.

Right now, we’re just looking at ordered collections. To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. Every time we get an iterator from an ordered collection, we start iterating from the beginning.

## **operations on ordered collections**

Let’s define some operations on ordered collections. Here’s mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original:[89] > 89Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-00258))_

- 195

Served by the Pot: Collections **const** mapWith = (fn, collection) => ({ [Symbol.iterator] () { **const** iterator = collection[Symbol.iterator](); **return** { next () { **const** {done, value} = iterator.next(); **return** ({done, value: done ? **undefined** : fn(value)}); } } } });

This illustrates the general pattern of working with ordered collections: We make them _iterables_ , meaning that they have a [Symbol.iterator] method, that returns an _iterator_ . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith: **const** Evens = mapWith((x) => 2 * x, Numbers); **for** ( **const** i **of** Evens) { console.log(i) } _//=>_ 0 2 4 ... **for** ( **const** i **of** Evens) { console.log(i) } _//=>_ 0 2 4 ... _(javascriptallonge.pdf (source-range-83ecb080-00259))_

- Served by the Pot: Collections

200

## **summary**

Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. _Iterable_ ordered collections can be iterated over or gathered into another collection.

Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-00264))_

### Generating Iterables

- Served by the Pot: Collections

201

## **Generating Iterables**

**==> picture [469 x 314] intentionally omitted <==**

**Banco do Café**

Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. What is there they don’t do well?

Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.

Iterators have to arrange its own state such that when you call them, they compute and return the next item. This seems blindingly obvious and simple. If, for example, you want numbers, you write: _(javascriptallonge.pdf (source-range-83ecb080-00266))_

- 203

Served by the Pot: Collections

They’re of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let’s look at one:

## **recursive iterators**

Iterators maintain state, that’s what they do. Generators have to manage the exact same amount of state, but sometimes, it’s much easier to manage that state in a generator. One of those cases is when we have to recursively enumerate something.

For example, iterating over a tree. Given an array that might contain arrays, let’s say we want to generate all the “leaf” elements, i.e. elements that are not, themselves, iterable.

_// Generation_ **const** isIterable = (something) => !!something[Symbol.iterator]; **const** generate = (iterable) => { **for** ( **let** element **of** iterable) { **if** (isIterable(element)) { generate(element) } **else** { console.log(element) } } } generate([1, [2, [3, 4], 5]]) _//=>_ 1 2 3 4 5

Very simple. Now for the iteration version. We’ll write a functional iterator to keep things simple, but it’s easy to see the shape of the basic problem: _(javascriptallonge.pdf (source-range-83ecb080-00268))_

- Served by the Pot: Collections

206

55 89 144 ...

The thing to note here is that our fibonacci generator has three states: generating 0, generating 1, and generating everything after that. This isn’t a good fit for an iterator, because iterators have one functional entry point and therefore, we’d have to represent our three states explicitly, perhaps using a state pattern[90] :

We’ll keep it simple:

_// Iteration_ **let** a, b, state = 0; **const** fibonacci = () => { **switch** (state) { **case** 0: state = 1; **return** a = 0; **case** 1: state = 2; **return** b = 1; **case** 2: [a, b] = [b, a + b]; **return** b } }; **while** ( **true** ) { console.log(fibonacci()); } _//=>_ 0 1 1 2 3 5 8 13

90https://en.wikipedia.org/wiki/State_pattern _(javascriptallonge.pdf (source-range-83ecb080-00271))_

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

- 216

Served by the Pot: Collections

We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use JavaScript’s natural management of state instead of constantly rolling our own.

Of course, we could just as easily write a generator function for Fibonacci numbers: **function** * fibonacci () { **let** a, b; **yield** a = 0; **yield** b = 1; **while** ( **true** ) { [a, b] = [b, a + b] **yield** b; } } **for** ( **const** i **of** fibonacci()) { console.log(i); } _//=>_ 0 1 1 2 3 5 8 13 21 34 55 89 144 ...

## **yielding iterables**

Here’s a first crack at a function that returns an iterable object for iterating over trees: _(javascriptallonge.pdf (source-range-83ecb080-00279))_

- Served by the Pot: Collections

222 **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield** fn(element); } } first works directly with iterators and remains unchanged, but rest can be rewritten as a generator: **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **function** * rest (iterable) { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **yield** * iterator; }

## **Summary**

A generator is a function that is defined with function * and uses yield (or yield *) to generate values. Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. And we don’t need to worry about wrapping our values in an object with .done and .value properties.

This is especially useful for making iterables. _(javascriptallonge.pdf (source-range-83ecb080-00285))_


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (5 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Iteration and Iterables: 187  Served by the Pot: Collections  Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get t ... [truncated] (3 shared statement(s))
- [[javascriptallonge-functional]] - shared statements: Functional shares source evidence from Iteration and Iterables: Served by the Pot: Collections  200  ## **summary**  Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection fr ... [truncated] (2 shared statement(s))
- [[javascriptallonge-method]] - shared statements: Method shares source evidence from Iteration and Iterables: Served by the Pot: Collections  188 **const** stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) **const** collectionSum = (collection) => { **const** ... [truncated] (2 shared statement(s))
- [[javascriptallonge-writing]] - shared statements: Writing shares source evidence from Generating Iterables: 216  Served by the Pot: Collections  We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use ... [truncated] (2 shared statement(s))
- [[javascriptallonge-generator]] - shared statements: Generator shares source evidence from Generating Iterables: Served by the Pot: Collections  222 **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from Generating Iterables: Served by the Pot: Collections  222 **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterable]] - shared statements: Iterable shares source evidence from Iteration and Iterables: 194  Served by the Pot: Collections **const** RandomNumbers = { [Symbol.iterator]: () => ({ next () { **return** {value: Math.random()}; } }) } **for** ( **const** i ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Iteration and Iterables: Served by the Pot: Collections  200  ## **summary**  Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection fr ... [truncated] (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from Iteration and Iterables: Served by the Pot: Collections  200  ## **summary**  Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection fr ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pass]] - shared statements: Pass shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (1 shared statement(s))
- [[javascriptallonge-purpose]] - shared statements: Purpose shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Generating Iterables: 216  Served by the Pot: Collections  We’ve writing a function that returns an iterator, but we used a generator to do it. And the generator’s syntax allows us to use ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Iteration and Iterables: Served by the Pot: Collections  188 **const** stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) **const** collectionSum = (collection) => { **const** ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
