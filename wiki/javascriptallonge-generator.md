---
page_id: javascriptallonge-generator
page_kind: concept
summary: Generator: 8 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-generator@70bce34f28ff0d624f2421d59081da31
---

# Generator

What [[javascriptallonge]] covers about generator:

## Statements

### Generating Iterables

- 203

Served by the Pot: Collections

They’re of approximately equal complexity. So why bring up generation? Well, there are some collections that are much easier to generate than to iterate over. Let’s look at one:

## **recursive iterators**

Iterators maintain state, that’s what they do. Generators have to manage the exact same amount of state, but sometimes, it’s much easier to manage that state in a generator. One of those cases is when we have to recursively enumerate something.

For example, iterating over a tree. Given an array that might contain arrays, let’s say we want to generate all the “leaf” elements, i.e. elements that are not, themselves, iterable.

_// Generation_ **const** isIterable = (something) => !!something[Symbol.iterator]; **const** generate = (iterable) => { **for** ( **let** element **of** iterable) { **if** (isIterable(element)) { generate(element) } **else** { console.log(element) } } } generate([1, [2, [3, 4], 5]]) _//=>_ 1 2 3 4 5

Very simple. Now for the iteration version. We’ll write a functional iterator to keep things simple, but it’s easy to see the shape of the basic problem: _(javascriptallonge.pdf (source-range-83ecb080-00268))_

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

- Served by the Pot: Collections

211 it “suspends” and the producer starts running. When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next().

Of course, generators need not be implemented exactly as coroutines. For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): **const** oneTwoThree = **function** () { **let** state = 'newborn'; **return** { next () { **switch** (state) { **case** 'newborn': state = 1; **return** {value: 1}; **case** 1: state = 2; **return** {value: 2} **case** 2: state = 3; **return** {value: 3} **case** 3: **return** {done: **true** }; } } } }; But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next(), it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded.

## **generators and iterables**

Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.

If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3. Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-83ecb080-00275))_

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


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Generating Iterables: Served by the Pot: Collections  207  21 34 55 89 144  ...  Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspunning ... [truncated] (3 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from Generating Iterables: Served by the Pot: Collections  222 **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Generating Iterables: Served by the Pot: Collections  222 **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield ... [truncated] (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Generating Iterables: Served by the Pot: Collections  222 **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Generating Iterables: Served by the Pot: Collections  207  21 34 55 89 144  ...  Again, this is not particularly horrendous, but like the recursive example, we’re explicitly greenspunning ... [truncated] (1 shared statement(s))
- [[javascriptallonge-writing]] - shared statements: Writing shares source evidence from Generating Iterables: Served by the Pot: Collections  222 **function** * untilWith (fn, iterable) { **for** ( **const** element **of** iterable) { **if** (fn(element)) **break** ; **yield ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
