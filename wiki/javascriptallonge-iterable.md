---
page_id: javascriptallonge-iterable
page_kind: concept
summary: Iterable: 9 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-iterable@d880c3418f8cdbf0f8cdafc028076c04
---

# Iterable

What [[javascriptallonge]] covers about iterable:

## Statements

### Iteration and Iterables

- 192

Served by the Pot: Collections As we can see, we can use for...of with linked lists just as easily as with stacks. And there’s one more thing: You recall that the spread operator (...) can spread the elements of an array in an array literal or as parameters in a function invocation.

Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal:

- ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_ And we can also spread the elements of an array literal into parameters: **const** firstAndSecondElement = (first, second) => ({first, second}) firstAndSecondElement(...stack) _//=> {"first":5,"second":10}_ This can be extremely useful.

One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

And if we have an infinite collection, spreading is going to fail outright as we’re about to see.

## **iterables out to infinity**

Iterables needn’t represent finite collections: **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } } There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them: _(javascriptallonge.pdf (source-range-83ecb080-00256))_

- 193

Served by the Pot: Collections ['all the numbers', ...Numbers] _//=> infinite loop!_

firstAndSecondElement(...Numbers) _//=> infinite loop!_

Attempting to spread an infinite iterable into an array is always going to fail.

## **ordered collections**

The iterables we’re discussing represent _ordered collections_ . One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning. For example: **const** abc = ["a", "b", "c"]; **for** ( **const** i **of** abc) { console.log(i) } _//=>_ a b c **for** ( **const** i **of** abc) { console.log(i) } _//=>_ a b c

This is accomplished with our own collections by returning a brand new iterator every time we call [Symbol.iterator], and ensuring that our iterators start at the beginning and work forward. Iterables needn’t represent ordered collections. We could make an infinite iterable representing random numbers: _(javascriptallonge.pdf (source-range-83ecb080-00257))_

- 194

Served by the Pot: Collections **const** RandomNumbers = { [Symbol.iterator]: () => ({ next () { **return** {value: Math.random()}; } }) } **for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.494052127469331 0.835459444206208 0.1408337657339871 ...

**for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.7845381607767195 0.4956772483419627 0.20259276474826038 ...

Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection.

Right now, we’re just looking at ordered collections. To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. Every time we get an iterator from an ordered collection, we start iterating from the beginning.

## **operations on ordered collections**

Let’s define some operations on ordered collections. Here’s mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original:[89] > 89Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-00258))_

- 196

Served by the Pot: Collections

Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens. Evens works just as if we’d written this: **const** Evens = { [Symbol.iterator] () { **const** iterator = Numbers[Symbol.iterator](); **return** { next () { **const** {done, value} = iterator.next(); **return** ({done, value: done ? **undefined** : 2 *value}); } } } };

Every time we write for (const i of Evens), JavaScript calls Evens[Symbol.iterator](). That in turns means it executes const iterator = Numbers[Symbol.iterator](); every time we write for (const i of Evens), and that means that iterator starts at the beginning of Numbers.

So, Evens is also an ordered collection, because it starts at the beginning each time we get a fresh iterator over it. Thus, mapWith has the property of preserving the collection semantics of the iterable we give it. So we call it a _collection operation_ .

Mind you, we can also map non-collection iterables, like RandomNumbers: **const** ZeroesToNines = mapWith((n) => Math.floor(10 * limit), RandomNumbers); **for** ( **const** i **of** ZeroesToNines) { console.log(i) } _//=>_ 5 1 9 ...

**for** ( **const** i **of** ZeroesToNines) { console.log(i) } _//=>_ 3 _(javascriptallonge.pdf (source-range-83ecb080-00260))_

- 198

Served by the Pot: Collections

Like mapWith, they preserve the ordered collection semantics of whatever you give them.

And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000: **const** Squares = mapWith((x) => x * x, Numbers); **const** EndWithOne = filterWith((x) => x % 10 === 1, Squares); **const** UpTo1000 = untilWith((x) => (x > 1000), EndWithOne);

[...UpTo1000] _//=>_ [1,81,121,361,441,841,961] [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] As we expect from an ordered collection, each time we iterate over UpTo1000, we begin at the beginning.

For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest]: **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **const** rest = (iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **return** iterator; } }); like our other operations, rest preserves the ordered collection semantics of its argument.

## **from**

Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function? No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-83ecb080-00262))_

- 199

Served by the Pot: Collections

One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in Array class already has one:

Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_ We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ]. And if we assign a function to a property, we’ve created a method.

So let’s do that:

Stack3.from = **function** (iterable) { **const** stack = **this** (); **for** ( **let** element **of** iterable) { stack.push(element); } **return** stack; } Pair1.from = (iterable) => ( **function** iterationToList (iteration) { **const** {done, value} = iteration.next(); **return** done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()) Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: **const** numberList = Pair1.from(untilWith((x) => x > 10, Numbers));

Pair1.from(Squares) _//=> {"first":0,_ "rest":{"first":1, "rest":{"first":4, "rest":{ ... _(javascriptallonge.pdf (source-range-83ecb080-00263))_


## Related pages

- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Iteration and Iterables: 198  Served by the Pot: Collections  Like mapWith, they preserve the ordered collection semantics of whatever you give them.  And here’s a computation performed usin ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Iteration and Iterables: 194  Served by the Pot: Collections **const** RandomNumbers = { [Symbol.iterator]: () => ({ next () { **return** {value: Math.random()}; } }) } **for** ( **const** i ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Iteration and Iterables: 196  Served by the Pot: Collections  Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens. Evens works just as if we’d written th ... [truncated] (1 shared statement(s))
- [[javascriptallonge-needn]] - shared statements: Needn shares source evidence from Iteration and Iterables: 193  Served by the Pot: Collections ['all the numbers', ...Numbers] _//=> infinite loop!_  firstAndSecondElement(...Numbers) _//=> infinite loop!_  Attempting to spr ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Iteration and Iterables: 198  Served by the Pot: Collections  Like mapWith, they preserve the ordered collection semantics of whatever you give them.  And here’s a computation performed usin ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
