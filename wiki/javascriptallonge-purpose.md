---
page_id: javascriptallonge-purpose
page_kind: concept
summary: Purpose: 4 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-purpose@6225377f88f9f5a386f292f92d8abdeb
---

# Purpose

What [[javascriptallonge]] covers about purpose:

## Statements

### Reassignment

- 134

Composing and Decomposing Data

Now we’re creating a new inner parameter, i and binding it to the value of the outer i. This works, but let is so much simpler and cleaner that it was added to the language in the ECMAScript 2015 specification.

In this book, we will use function declarations sparingly, and not use var at all. That does not mean that you should follow the exact same practice in your own code: The purpose of this book is to illustrate certain principles of programming. The purpose of your own code is to get things done. The two goals are often, but not always, aligned. _(javascriptallonge.pdf (source-range-83ecb080-00186))_

### Functional Iterators

- Composing and Decomposing Data

153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);

This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: **const** firstInArray = (fn, array) => array.filter(fn)[0];

JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy.

## **caveat**

Please note that unlike most of the other functions discussed in this book, iterators are _stateful_ . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you’re changing the state of the original!

For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-00208))_

### mapWith

- Recipes with Data

170

## **mapWith**

In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the array, then returns the results in another array. For example:

[1, 2, 3, 4, 5].map(x => x * x) _//=> [1, 4, 9, 16, 25]_ We could write a function that behaves like the .map method if we wanted: **const** map = (list, fn) => list.map(fn);

This recipe isn’t for map: It’s for mapWith, a function that wraps around map and turns any other function into a mapper. mapWith is very simple:[82] **const** mapWith = (fn) => (list) => list.map(fn); mapWith differs from map in two ways. It reverses the arguments, taking the function first and the list second. It also “curries” the function: Instead of taking two arguments, it takes one argument and returns a function that takes another argument.

That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map: **const** squaresOf = (list) => list.map(x => x * x); squaresOf([1, 2, 3, 4, 5]) _//=> [1, 4, 9, 16, 25]_ We can call mapWith in one step:

> 82Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-00228))_

### Iteration and Iterables

- 194

Served by the Pot: Collections **const** RandomNumbers = { [Symbol.iterator]: () => ({ next () { **return** {value: Math.random()}; } }) } **for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.494052127469331 0.835459444206208 0.1408337657339871 ...

**for** ( **const** i **of** RandomNumbers) { console.log(i) } _//=>_ 0.7845381607767195 0.4956772483419627 0.20259276474826038 ...

Whether you work with the same iterator over and over, or get a fresh iterable every time, you are always going to get fresh random numbers. Therefore, RandomNumbers is not an ordered collection.

Right now, we’re just looking at ordered collections. To reiterate (hah), an ordered collection represents a (possibly infinite) collection of elements that are in some order. Every time we get an iterator from an ordered collection, we start iterating from the beginning.

## **operations on ordered collections**

Let’s define some operations on ordered collections. Here’s mapWith, it takes an ordered collection, and returns another ordered collection representing a mapping over the original:[89] > 89Yes, we also used the name mapWith for working with ordinary collections elsewhere. If we were writing a library of functions, we would have to disambiguate the two kinds of mapping functions with special names, namespaces, or modules. But for the purposes of discussing ideas, we can use the same name twice in two different contexts. It’s the same idea, after all. _(javascriptallonge.pdf (source-range-83ecb080-00258))_


## Related pages

- [[javascriptallonge-idea]] - shared statements: Idea shares source evidence from mapWith: Recipes with Data  170  ## **mapWith**  In JavaScript, arrays have a .map method. Map takes a function as an argument, and applies it to each of the elements of the ... [truncated] (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Reassignment: 134  Composing and Decomposing Data  Now we’re creating a new inner parameter, i and binding it to the value of the outer i. This works, but let is so much simpler a ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pass]] - shared statements: Pass shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
