---
page_id: javascriptallonge-knowing
page_kind: concept
summary: Knowing: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-knowing@9572544697f7d1a804ec4c548a87577a
---

# Knowing

What [[javascriptallonge]] covers about knowing:

## Statements

### Functional Iterators

- Composing and Decomposing Data

146

## **iterating**

Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration.

JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: **const** arraySum = (array) => { **let** sum = 0; **for** ( **let** i = 0; i < array.length; ++i) { sum += array[i]; } **return** sum } arraySum([1, 4, 9, 16, 25]) _//=> 55_

Once again, we’re mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we’re getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0.

We can write this a slightly different way, using a while loop: **const** arraySum = (array) => { **let** done, sum = 0, i = 0; **while** ((done = i == array.length, !done)) { **const** value = array[i++]; sum += value; } **return** sum } arraySum([1, 4, 9, 16, 25]) _//=> 55_

Notice that buried inside our loop, we have bound the names done and value. We can put those into a POJO (a Plain Old JavaScript Object). It’ll be a little awkward, but we’ll be patient: _(javascriptallonge.pdf (source-range-83ecb080-00201))_

### Making Data Out Of Functions

- 165

Composing and Decomposing Data **const** reverse = (list, delayed = EMPTYLIST) => list( () => delayed, (aPair) => reverse(aPair(pairRest), node(aPair(pairFirst))(delayed)) ); print(reverse(l123)); _//=> 3 2 1_ **const** mapWith = (fn, list, delayed = EMPTYLIST) => list( () => reverse(delayed), (aPair) => mapWith(fn, aPair(pairRest), node(fn(aPair(pairFirst)))(delayed)) ); print(mapWith(x => x * x, reverse(l123))) _//=> 941_

We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else.

## **functions are not the real point**

There are lots of similar texts explaining how to construct complex semantics out of functions. You can establish that K and K(I) can represent true and false, model magnitudes with Church Numerals[79] or Surreal Numbers[80] , and build your way up to printing FizzBuzz.

The superficial conclusion reads something like this:

Functions are a fundamental building block of computation. They are “axioms” of combinatory logic, and can be used to compute anything that JavaScript can compute.

However, that is not the interesting thing to note here. Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. Knowing how to make a linked list out of functions is not really necessary for the working programmer. (Knowing that it can be done, on the other hand, is very important to understanding computer science.) Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons[81] of the electromagnetic force. It’s the QED of physics that underpins the Maxwell’s Equations of programming. Deeply important, but not practical when you’re building a bridge.

> 79https://en.wikipedia.org/wiki/Church_encoding

> 80https://en.wikipedia.org/wiki/Surreal_number

> 81https://en.wikipedia.org/wiki/Gauge_boson _(javascriptallonge.pdf (source-range-83ecb080-00221))_

### Lazy and Eager Collections

- Served by the Pot: Collections

223

## **Lazy and Eager Collections**

The operations on iterables are tremendously valuable, but let’s reiterate why we care: In JavaScript, we build single-responsibility objects, and single-responsibility functions, and we compose these together to build more full-featured objects and algorithms.

Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack in the older style of object-oriented programming, we built “fat” objects. Each collection knew how to map itself (.map), how to fold itself (.reduce), how to filter itself (.filter) and how to find one element within itself (.find). If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection.

Over time, this informal “interface” for collections grows by accretion. Some methods are only added to a few collections, some are added to all. But our objects grow fatter and fatter. We tell ourselves that, well, a collection ought to know how to map itself.

But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. Each one has its own variation, but the overall form is identical. That’s a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction.

This “fat object” style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don’t need for the collection to handle every single detail. That would be like saying that when we ask a bank teller for some cash, they personally print every bank note.

## **implementing methods with iteration**

Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith.

Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. And if we want to create convenience methods, we can reuse common pieces.

Here is LazyCollection, a mixin we can use with any ordered collection that is also an iterable: _(javascriptallonge.pdf (source-range-83ecb080-00287))_


## Related pages

- [[javascriptallonge-method]] - shared statements: Method shares source evidence from Lazy and Eager Collections: Served by the Pot: Collections  223  ## **Lazy and Eager Collections**  The operations on iterables are tremendously valuable, but let’s reiterate why we care: In Ja ... [truncated] (2 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Functional Iterators: Composing and Decomposing Data  146  ## **iterating**  Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplish ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
