---
page_id: javascriptallonge-collection
page_kind: concept
summary: Collection: 7 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-collection@d40dfeaf034ce8f41e744cfeaf114292
---

# Collection

What [[javascriptallonge]] covers about collection:

## Statements

### Iteration and Iterables

- Served by the Pot: Collections

183

## **Iteration and Iterables**

**==> picture [469 x 313] intentionally omitted <==**

**Coffee Labels at the Saltspring Coffee Processing Facility**

Many objects in JavaScript can model collections of things. A collection is like a box containing stuff. Sometimes you just want to move the box around. But sometimes you want to open it up and do things with its contents.

Things like “put a label on every bag of coffee in this box,” Or, “Open the box, take out the bags of decaf, and make a new box with just the decaf.” Or, “go through the bags in this box, and take out the first one marked ‘Espresso’ that contains at least 454 grams of beans.” All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called _iterating over the contents_ , and JavaScript has a standard way to iterate over the contents of collections.

## **a look back at functional iterators**

When discussing functions, we looked at the benefits of writing Functional Iterators. We can do the same thing for objects. Here’s a stack that has its own functional iterator method: _(javascriptallonge.pdf (source-range-83ecb080-00247))_

- 186

Served by the Pot: Collections **const** stack = Stack1(); stack.push(1); stack.push(2); stack.push(3); iteratorSum(stack.iterator()) _//=> 6_

We could save a step and write collectionSum, a function that folds over any object, provided that the object implements an .iterator method: **const** collectionSum = (collection) => { **const** iterator = collection.iterator(); **let** eachIteration, sum = 0; **while** ((eachIteration = iterator(), !eachIteration.done)) { sum += eachIteration.value; } **return** sum } collectionSum(stack) _//=> 6_

If we write a program with the presumption that “everything is an object,” we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don’t need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

This is a good thing.

## **iterator objects**

Iteration for functions and objects has been around for many, many decades. For simple linear collections like arrays, linked lists, stacks, and queues, functional iterators are the simplest and easiest way to implement iterators.

In programs involving large collections of objects, it can be handy to implement iterators as objects, rather than functions. The mechanics of iterating can then be factored using the same tools that are used to factor the mechanics of all other objects in the system. _(javascriptallonge.pdf (source-range-83ecb080-00250))_

- 192

Served by the Pot: Collections As we can see, we can use for...of with linked lists just as easily as with stacks. And there’s one more thing: You recall that the spread operator (...) can spread the elements of an array in an array literal or as parameters in a function invocation.

Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal:

- ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_ And we can also spread the elements of an array literal into parameters: **const** firstAndSecondElement = (first, second) => ({first, second}) firstAndSecondElement(...stack) _//=> {"first":5,"second":10}_ This can be extremely useful.

One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

And if we have an infinite collection, spreading is going to fail outright as we’re about to see.

## **iterables out to infinity**

Iterables needn’t represent finite collections: **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } } There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them: _(javascriptallonge.pdf (source-range-83ecb080-00256))_

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

- 233

Served by the Pot: Collections **const** Numbers = Object.assign({ [Symbol.iterator]: () => { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } }, LazyCollection); **const** firstCubeOver1234 = Numbers .map((x) => x * x * x) .filter((x) => x > 1234) .first() _//=> 1331_

Balanced against their flexibility, our “lazy collections” use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why “pure” functional languages like Haskell combine lazy semantics with immutable collections, and why even “impure” languages like Clojure emphasize the use of immutable collections.

## **eager collections**

An _eager_ collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is _gatherable_ , meaning it has a .from method: **const** extend = **function** (consumer, ...providers) { **for** ( **let** i = 0; i < providers.length; ++i) { **const** provider = providers[i]; **for** ( **let** key **in** provider) { **if** (provider.hasOwnProperty(key)) { consumer[key] = provider[key] } } } **return** consumer }; _(javascriptallonge.pdf (source-range-83ecb080-00297))_

### Interactive Generators

- Served by the Pot: Collections

260 } } **break** ; _// ..._ } } **const** aNaughtsAndCrossesGame = generatorNaughtsAndCrosses();

We can then get the first move by calling .next(). Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn’t started yet. If we wanted to pass some state to the generator before it begins, we’d do that with parameters.): aNaughtsAndCrossesGame.next().value

_//=> 0_ aNaughtsAndCrossesGame.next(1).value

_//=> 6_ aNaughtsAndCrossesGame.next(3).value

_//=> 8_ aNaughtsAndCrossesGame.next(7).value

_//=> 4_

Our generator function maintains state implicitly in its control flow, but returns an iterator that we call, it doesn’t call us. It isn’t a collection, it has no meaning if we try to spread it into parameters or as the subject of a for...of block.

But the generator function allows us to maintain state implicitly. And sometimes, we want to use implicit state instead of explicitly storing state in our data.

## **summary**

We have looked at generators as ways of making iterators over static collections, where state is modelled implicitly in control flow. But as we see here, it’s also possible to use a generator interactively, passing values in and receiving a value in return, just like an ordinary function.

Again, the salient difference is that an “interactive” generator is stateful, and it embodies its state in its control flow. _(javascriptallonge.pdf (source-range-83ecb080-00326))_


## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00273, source-range-83ecb080-00275))_

> 208 Served by the Pot: Collections **function** * only (something) { **yield** something; }; only("you").next() _//=>_ {"done": **false** , value: "you"} Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". Invoking only more than once gives us fresh iterators each time: only("you").next() _//=>_ {"done": **false** , value: "you"} only("the lonely").next() _//=>_ {"done": **false** , value: "the lonely"} We can invoke the same iterator twice: **const** six

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00274))_

| entry | content |
| --- | --- |
| 1 | We call oneTwoThree() and get an iterator. |
| 2 | The iterator is in a nascent or “newborn” state. |
| 3 | When we call interator.next(), the body of our generator begins to be evaluated. |
| 4 | Served by the Pot: Collections 210 The body of our generator runs until it returns, ends, or encounters a yield statement, which is yield 1;. - The iterator _suspends its execution_ . - The iterator wraps 1 in {done: false, value: 1} and returns that from the call to .next(). - The rest of the program continues along its way until it makes another call to iterator.next(). - The iterator _resumes execution_ from the point where it yielded the last value. |
| 5 | The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 2;. - The iterator _suspends its execution_ . - The iterator wraps 2 in {done: false, value: 2} and returns that from the call to .next(). - The rest of the program continues along its way until it makes another call to iterator.next(). - The iterator _resumes execution_ from the point where it yielded the last value. |
| 6 | The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 3;. - The iterator _suspends its execution_ . - The iterator wraps 3 in {done: false, value: 3} and returns that from the call to .next(). - The rest of the program continues along its way until it makes another call to iterator.next(). - The iterator _resumes execution_ from the point where it yielded the last value. |
| 7 | The body of our generator runs until it returns, ends, or encounters the next yield statement. There are no more lines of code, so it ends. - The iterator returns {done: true} from the call to .next(), and every call to this iterator’s .next() method will return {done: true} from now on. Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. Instead of thinking of there being on execution context, we can imagine that there are two execution contexts. With an iterator, we can call them the _producer_ and the _consumer_ . The iterator is the producer, and the code that iterates over it is the consumer. When the consumer calls .next(), |

<details>
<summary>Raw table text</summary>

```
209 

Served by the Pot: Collections 

**const** oneTwoThree = **function** * () { **yield** 1; **yield** 2; **yield** 3; }; 

oneTwoThree().next() _//=>_ {"done": **false** , value: 1} oneTwoThree().next() _//=>_ {"done": **false** , value: 1} oneTwoThree().next() _//=>_ {"done": **false** , value: 1} 

**const** iterator = oneTwoThree(); 

iterator.next() _//=>_ {"done": **false** , value: 1} iterator.next() _//=>_ {"done": **false** , value: 2} iterator.next() _//=>_ {"done": **false** , value: 3} iterator.next() _//=>_ {"done": **true** } 

This is where generators behave very, very differently from ordinary functions. What happens _semantically_ ? 

1. We call oneTwoThree() and get an iterator. 

2. The iterator is in a nascent or “newborn” state. 

3. When we call interator.next(), the body of our generator begins to be evaluated.
Served by the Pot: Collections 

210 

4. The body of our generator runs until it returns, ends, or encounters a yield statement, which is yield 1;. 

   - The iterator _suspends its execution_ . 

   - The iterator wraps 1 in {done: false, value: 1} and returns that from the call to .next(). 

   - The rest of the program continues along its way until it makes another call to iterator.next(). 

   - The iterator _resumes execution_ from the point where it yielded the last value. 

5. The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 2;. 

   - The iterator _suspends its execution_ . 

   - The iterator wraps 2 in {done: false, value: 2} and returns that from the call to .next(). 

   - The rest of the program continues along its way until it makes another call to iterator.next(). 

   - The iterator _resumes execution_ from the point where it yielded the last value. 

6. The body of our generator runs until it returns, ends, or encounters the next yield statement, which is yield 3;. 

   - The iterator _suspends its execution_ . 

   - The iterator wraps 3 in {done: false, value: 3} and returns that from the call to .next(). 

   - The rest of the program continues along its way until it makes another call to iterator.next(). 

   - The iterator _resumes execution_ from the point where it yielded the last value. 

7. The body of our generator runs until it returns, ends, or encounters the next yield statement. There are no more lines of code, so it ends. 

   - The iterator returns {done: true} from the call to .next(), and every call to this iterator’s .next() method will return {done: true} from now on. 

This behaviour is not unique to JavaScript, generators are called coroutines[92] in other languages: 

Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. 

Instead of thinking of there being on execution context, we can imagine that there are two execution contexts. With an iterator, we can call them the _producer_ and the _consumer_ . The iterator is the producer, and the code that iterates over it is the consumer. When the consumer calls .next(), 

92https://en.wikipedia.org/wiki/Coroutine
```

</details>


## Related pages

- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Iteration and Iterables: Served by the Pot: Collections  183  ## **Iteration and Iterables**  **==> picture [469 x 313] intentionally omitted <==**  **Coffee Labels at the Saltspring Coffee ... [truncated] (2 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Iteration and Iterables: 186  Served by the Pot: Collections **const** stack = Stack1(); stack.push(1); stack.push(2); stack.push(3); iteratorSum(stack.iterator()) _//=> 6_  We could save a ... [truncated] (2 shared statement(s))

## Source

- [[javascriptallonge]]
