---
page_id: javascriptallonge-pass
page_kind: concept
summary: Pass: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-pass@cd56f4d300a992c360aa81ce80fe8289
---

# Pass

What [[javascriptallonge]] covers about pass:

## Statements

### Arrays and Destructuring Arguments

- Composing and Decomposing Data

83 **const** [what] = []; That match would fail because the array doesn’t have an element to assign to what. But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn’t something that fits, JavaScript binds undefined to the name. Therefore: **const** [what] = []; what _//=> undefined_ **const** [which, what, who] = ["duck feet", "tiger tail"]; who _//=> undefined_ And if there aren’t any items to assign with ..., JavaScript assigns an empty array: **const** [...they] = []; they _//=> []_ **const** [which, what, ...they] = ["duck feet", "tiger tail"]; they _//=> []_ From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

## **destructuring and return values**

Some languages support multiple return values: A function can return several things at once, like a value and an error code. This can easily be emulated in JavaScript with destructuring: _(javascriptallonge.pdf (source-range-83ecb080-00129))_

### Functional Iterators

- Composing and Decomposing Data

150 **const** FibonacciIterator = () => { **let** previous = 0, current = 1; **return** () => { **const** value = current; [previous, current] = [current, current + previous]; **return** {done: **false** , value}; }; }; **const** fib = FibonacciIterator() fib().value _//=> 1_ fib().value _//=> 1_ fib().value _//=> 2_ fib().value _//=> 3_ fib().value _//=> 5_

A function that starts with a seed and expands it into a data structure is called an _unfold_ . It’s the opposite of a fold. It’s possible to write a generic unfold mechanism, but let’s pass on to what we can do with unfolded iterators.

For starters, we can map an iterator, just like we map a collection: **const** mapIteratorWith = (fn, iterator) => () => { **const** {done, value} = iterator(); **return** ({done, value: done ? **undefined** : fn(value)}); } **const** squares = mapIteratorWith((x) => x * x, NumberIterator(1)); squares().value _//=> 1_ squares().value _(javascriptallonge.pdf (source-range-83ecb080-00205))_

- Composing and Decomposing Data

153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);

This is interesting, because it is lazy: It doesn’t apply fn to every element in an iteration, just enough to find the first that passes the test. Whereas if we wrote something like: **const** firstInArray = (fn, array) => array.filter(fn)[0];

JavaScript would apply fn to every element. If array was very large, and fn very slow, this would consume a lot of unnecessary time. And if fn had some sort of side-effect, the program could be buggy.

## **caveat**

Please note that unlike most of the other functions discussed in this book, iterators are _stateful_ . There are some important implications of stateful functions. One is that while functions like take(...) appear to create an entirely new iterator, in reality they return a decorated reference to the original iterator. So as you traverse the new decorator, you’re changing the state of the original!

For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer “own” that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-83ecb080-00208))_

### Making Data Out Of Functions

- Composing and Decomposing Data

166 So what _is_ interesting about this? What nags at our brain as we’re falling asleep after working our way through this?

## **a return to backward thinking**

To make pairs work, we did things _backwards_ , we passed the first and rest functions to the pair, and the pair called our function. As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y).

But we could have done something completely different. We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair.

The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it: **const** first = K, second = K(I), pair = (first) => (second) => { **const** pojo = {first, second}; **return** (selector) => selector(pojo.first)(pojo.second); }; **const** latin = pair("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_

This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. The same thing happens with our lists. Here’s length for lists: **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) );

We’re passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-00222))_

- Composing and Decomposing Data

167

We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list: **const** length = (node, delayed = 0) => node === EMPTY

- ? delayed

- : length(node.rest, delayed + 1);

The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we’re pushing even more knowledge about the structure of lists into the code that uses them.

Having a list know itself whether it is empty hides implementation information from the code that uses lists. This is a fundamental principle of good design. It is a tenet of Object-Oriented Programming, but it is **not** exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both.

There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns:

- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want.

- And instead of testing some property of an entity and making a choice of our own with ?: (or if), pass the entity the work we want done for each case and let it test itself. _(javascriptallonge.pdf (source-range-83ecb080-00223))_


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (2 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from Making Data Out Of Functions: Composing and Decomposing Data  167  We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a databa ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (1 shared statement(s))
- [[javascriptallonge-list]] - shared statements: List shares source evidence from Making Data Out Of Functions: Composing and Decomposing Data  166 So what _is_ interesting about this? What nags at our brain as we’re falling asleep after working our way through this?  ## **a r ... [truncated] (1 shared statement(s))
- [[javascriptallonge-purpose]] - shared statements: Purpose shares source evidence from Functional Iterators: Composing and Decomposing Data  153 **const** firstInIteration = (fn, iterator) => take(filterIteratorWith(fn, iterator), 1);  This is interesting, because it is laz ... [truncated] (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from Arrays and Destructuring Arguments: Composing and Decomposing Data  83 **const** [what] = []; That match would fail because the array doesn’t have an element to assign to what. But this is not how Java ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Functional Iterators: Composing and Decomposing Data  150 **const** FibonacciIterator = () => { **let** previous = 0, current = 1; **return** () => { **const** value = current; [previous, ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
