---
page_id: javascriptallonge-pattern
page_kind: concept
summary: Pattern: 6 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-pattern@0f3350bebb2718fdff9de6b17ac33f41
---

# Pattern

What [[javascriptallonge]] covers about pattern:

## Statements

### Building Blocks

- The first sip: Basic Functions

48

## **Building Blocks**

When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it. The strength of JavaScript is that you can do anything. The weakness is that you will. There are ifs, fors, returns, everything thrown higgledy piggledy together. Although you needn’t restrict yourself to a small number of simple patterns, it can be helpful to understand the patterns so that you can structure your code around some basic building blocks.

## **composition**

: One of the most basic of these building blocks is _composition_ **const** cookAndEat = (food) => eat(cook(food));

It’s really that simple: Whenever you are chaining two or more functions together, you’re composing them. You can compose them with explicit JavaScript code as we’ve just done. You can also generalize composition with the B Combinator or “compose” that we saw in Combinators and Decorators: **const** compose = (a, b) => (c) => a(b(c)); **const** cookAndEat = compose(eat, cook);

If that was all there was to it, composition wouldn’t matter much. But like many patterns, using it when it applies is only 20% of the benefit. The other 80% comes from organizing your code such that you can use it: Writing functions that can be composed in various ways.

In the recipes, we’ll look at a decorator called once: It ensures that a function can only be executed once. Thereafter, it does nothing. Once is useful for ensuring that certain side effects are not repeated. We’ll also look at maybe: It ensures that a function does nothing if it is given nothing (like null or undefined) as an argument.

Of course, you needn’t use combinators to implement either of these ideas, you can use if statements. But once and maybe compose, so you can chain them together as you see fit:

- **const** actuallyTransfer= (from, to, amount) => _// do something_ **const** invokeTransfer = once(maybe(actuallyTransfer(...))); _(javascriptallonge.pdf (source-range-83ecb080-00086))_

### Mutation

- Composing and Decomposing Data

120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsEve _//=> [2012, 10, 31]_ The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we _mutate_ the value in the inner environment?

**const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween[0] = 2013; })(allHallowsEve); allHallowsEve _//=> [2013, 10, 31]_ This is different. We haven’t rebound the inner name to a different variable, we’ve mutated the value that both bindings share. Now that we’ve finished with mutation and aliases, let’s have a look at it.

**==> picture [29 x 29] intentionally omitted <==**

JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value.

**==> picture [29 x 29] intentionally omitted <==**

Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction.

## **mutation and data structures**

Mutation is a surprisingly complex subject. It is possible to compute anything without ever mutating an existing entity. Languages like Haskell[70] don’t permit mutation at all. In general, mutation makes some algorithms shorter to write and possibly faster, but harder to reason about.

One pattern many people follow is to be liberal with mutation when constructing data, but conservative with mutation when consuming data. Let’s recall linked lists from Plain Old JavaScript Objects. While we’re executing the mapWith function, we’re constructing a new linked list. By this pattern, we would be happy to use mutation to construct the list while running mapWith.

But after returning the new list, we then become conservative about mutation. This also makes sense: Linked lists often use structure sharing. For example:

70https://en.wikipedia.org/wiki/Haskell_ _(javascriptallonge.pdf (source-range-83ecb080-00171))_

### Copy on Write

- Composing and Decomposing Data

140

Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.— Wikipedia[73] Like all strategies, it makes a tradeoff: It’s much cheaper than pessimistically copying structures when you make an infrequent number of small changes, but if you tend to make a lot of changes to some that you aren’t sharing, it’s more expensive.

Looking at the code again, you see that the copy function doesn’t copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we’re done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write.

> 73https://en.wikipedia.org/wiki/Copy-on-write _(javascriptallonge.pdf (source-range-83ecb080-00193))_

### Iteration and Iterables

- 195

Served by the Pot: Collections **const** mapWith = (fn, collection) => ({ [Symbol.iterator] () { **const** iterator = collection[Symbol.iterator](); **return** { next () { **const** {done, value} = iterator.next(); **return** ({done, value: done ? **undefined** : fn(value)}); } } } });

This illustrates the general pattern of working with ordered collections: We make them _iterables_ , meaning that they have a [Symbol.iterator] method, that returns an _iterator_ . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

Many operations on ordered collections return another ordered collection. They do so by taking care to iterate over a result freshly every time we get an iterator for them. Consider this example for mapWith: **const** Evens = mapWith((x) => 2 * x, Numbers); **for** ( **const** i **of** Evens) { console.log(i) } _//=>_ 0 2 4 ... **for** ( **const** i **of** Evens) { console.log(i) } _//=>_ 0 2 4 ... _(javascriptallonge.pdf (source-range-83ecb080-00259))_

### Generating Iterables

- 212

Served by the Pot: Collections **const** ThreeNumbers = { [Symbol.iterator]: **function** * () { **yield** 1; **yield** 2; **yield** 3 } } **for** ( **const** i **of** ThreeNumbers) { console.log(i); } _//=>_ 1 2 3 [...ThreeNumbers] _//=>_ [1,2,3] **const** iterator = ThreeNumbers[Symbol.iterator](); iterator.next() _//=>_ {"done": **false** , value: 1} iterator.next() _//=>_ {"done": **false** , value: 2} iterator.next() _//=>_ {"done": **false** , value: 3} iterator.next() _//=>_ {"done": **true** } Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method.

This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing _(javascriptallonge.pdf (source-range-83ecb080-00276))_


## Related pages

- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from Mutation: Composing and Decomposing Data  120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsE ... [truncated] (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-const]] - shared statements: Const shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-needn]] - shared statements: Needn shares source evidence from Building Blocks: The first sip: Basic Functions  48  ## **Building Blocks**  When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-people]] - shared statements: People shares source evidence from Mutation: Composing and Decomposing Data  120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsE ... [truncated] (1 shared statement(s))
- [[javascriptallonge-rest]] - shared statements: Rest shares source evidence from Building Blocks: The first sip: Basic Functions  48  ## **Building Blocks**  When you look at functions within functions in JavaScript, there’s a bit of a “spaghetti code” look to it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
