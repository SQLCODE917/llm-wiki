---
page_id: javascriptallonge-method
page_kind: concept
summary: Method: 10 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-method@1992b2a354fc11d8b895f3ae27766bca
---

# Method

What [[javascriptallonge]] covers about method:

## Statements

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

95 depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]).

This keeps on happening, so that JavaScript collects the values 1, 2, 3, 4, and 5 plus housekeeping information by the time it calls mapWith((x) => x * x, []). It can start assembling the resulting array and start discarding the information it is saving.

That information is saved on a _call stack_ , and it is quite expensive. Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called _call frames_ , and they include the place where the function was called, an environment, and so on).

In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error.

mapWith((x) => x * x, [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99 ]) _//=> ???_

Is there a better way? Yes. In fact, there are several better ways. Making algorithms faster is a very highly studied field of computer science. The one we’re going to look at here is called _tail-call optimization_ , or “TCO.” _(javascriptallonge.pdf (source-range-83ecb080-00142))_

### Plain Old JavaScript Objects

- Composing and Decomposing Data

113 compact method syntax, but they are not relevant here. We will generally prefer compact method syntax whenever we can.)

## **destructuring objects**

Just as we saw with arrays, we can write destructuring assignments with literal object syntax. So, we can write: **const** user = { name: { first: "Reginald", last: "Braithwaite" }, occupation: { title: "Author", responsibilities: [ "JavaScript Allongé", "JavaScript Spessore", "CoffeeScript Ristretto" ] } }; user.name.last _//=> "Braithwaite"_ user.occupation.title _//=> "Author"_ And we can also write: **const** {name: { first: given, last: surname}, occupation: { title: title } } = us\ er; surname _//=> "Braithwaite"_ title _//=> "Author"_ And of course, we destructure parameters: _(javascriptallonge.pdf (source-range-83ecb080-00163))_

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

201

## **Generating Iterables**

**==> picture [469 x 314] intentionally omitted <==**

**Banco do Café**

Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. What is there they don’t do well?

Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.

Iterators have to arrange its own state such that when you call them, they compute and return the next item. This seems blindingly obvious and simple. If, for example, you want numbers, you write: _(javascriptallonge.pdf (source-range-83ecb080-00266))_

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

- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Iteration and Iterables: Served by the Pot: Collections  188 **const** stack = Stack2(); stack.push(2000); stack.push(10); stack.push(5) **const** collectionSum = (collection) => { **const** ... [truncated] (2 shared statement(s))
- [[javascriptallonge-knowing]] - shared statements: Knowing shares source evidence from Lazy and Eager Collections: Served by the Pot: Collections  223  ## **Lazy and Eager Collections**  The operations on iterables are tremendously valuable, but let’s reiterate why we care: In Ja ... [truncated] (2 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Generating Iterables: Served by the Pot: Collections  201  ## **Generating Iterables**  **==> picture [469 x 314] intentionally omitted <==**  **Banco do Café**  Iterables look cool, but ... [truncated] (1 shared statement(s))
- [[javascriptallonge-functional]] - shared statements: Functional shares source evidence from Generating Iterables: Served by the Pot: Collections  201  ## **Generating Iterables**  **==> picture [469 x 314] intentionally omitted <==**  **Banco do Café**  Iterables look cool, but ... [truncated] (1 shared statement(s))
- [[javascriptallonge-learn]] - shared statements: Learn shares source evidence from Flip: Recipes with Data  173 **const** flipAndCurry = (fn) => (first) => (second) => fn(second, first);  Sometimes you want to flip, but not curry: **const** flip = (fn) = ... [truncated] (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Generating Iterables: Served by the Pot: Collections  201  ## **Generating Iterables**  **==> picture [469 x 314] intentionally omitted <==**  **Banco do Café**  Iterables look cool, but ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
