---
page_id: javascriptallonge-recall
page_kind: concept
summary: Recall: 6 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-recall@e52db6ccc482de39a53b660ef9ccb8fd
---

# Recall

What [[javascriptallonge]] covers about recall:

## Statements

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

8

I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function.

## **functions and identities**

You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not.

Which kind are functions? Let’s try them out and see. For reasons of appeasing the JavaScript parser, we’ll enclose our functions in parentheses: (() => 0) === (() => 0) _//=> false_

Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. “Function” is a reference type.

## **applying functions**

Let’s put functions to work. The way we use functions is to _apply_ them to zero or more values called _arguments_ . Just as 2 + 2 produces a value (in this case 4), applying a function to zero or more arguments produces a value as well.

Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. Let’s call the arguments _args_ . Here’s how to apply a function to some arguments:

## _fn_expr_ ( _args_ )

Right now, we only know about one such expression: () => 0, so let’s use it. We’ll put it in parentheses[17] to keep the parser happy, like we did above: (() => 0). Since we aren’t giving it any arguments, we’ll simply write () after the expression. So we write: (() => 0)() _//=> 0_

> 17If you’re used to other programming languages, you’ve probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages! _(javascriptallonge.pdf (source-range-83ecb080-00045))_

### Mutation

- Composing and Decomposing Data

118

## **Mutation**

**==> picture [240 x 321] intentionally omitted <==**

**Cupping Grinds**

In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =: **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_ You can even add a value: _(javascriptallonge.pdf (source-range-83ecb080-00169))_

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

### Iteration and Iterables

- 192

Served by the Pot: Collections As we can see, we can use for...of with linked lists just as easily as with stacks. And there’s one more thing: You recall that the spread operator (...) can spread the elements of an array in an array literal or as parameters in a function invocation.

Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal:

- ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_ And we can also spread the elements of an array literal into parameters: **const** firstAndSecondElement = (first, second) => ({first, second}) firstAndSecondElement(...stack) _//=> {"first":5,"second":10}_ This can be extremely useful.

One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

And if we have an infinite collection, spreading is going to fail outright as we’re about to see.

## **iterables out to infinity**

Iterables needn’t represent finite collections: **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } } There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them: _(javascriptallonge.pdf (source-range-83ecb080-00256))_

- 199

Served by the Pot: Collections

One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in Array class already has one:

Array.from(UpTo1000) _//=> [1,81,121,361,441,841,961]_ We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ]. And if we assign a function to a property, we’ve created a method.

So let’s do that:

Stack3.from = **function** (iterable) { **const** stack = **this** (); **for** ( **let** element **of** iterable) { stack.push(element); } **return** stack; } Pair1.from = (iterable) => ( **function** iterationToList (iteration) { **const** {done, value} = iteration.next(); **return** done ? EMPTY : Pair1(value, iterationToList(iteration)); })(iterable[Symbol.iterator]()) Now we can go “end to end,” If we want to map a linked list of numbers to a linked list of the squares of some numbers, we can do that: **const** numberList = Pair1.from(untilWith((x) => x > 10, Numbers));

Pair1.from(Squares) _//=> {"first":0,_ "rest":{"first":1, "rest":{"first":4, "rest":{ ... _(javascriptallonge.pdf (source-range-83ecb080-00263))_

### Generating Iterables

- Served by the Pot: Collections

211 it “suspends” and the producer starts running. When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next().

Of course, generators need not be implemented exactly as coroutines. For example, a “transpiler” might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we’ll see that later): **const** oneTwoThree = **function** () { **let** state = 'newborn'; **return** { next () { **switch** (state) { **case** 'newborn': state = 1; **return** {value: 1}; **case** 1: state = 2; **return** {value: 2} **case** 2: state = 3; **return** {value: 3} **case** 3: **return** {done: **true** }; } } } }; But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next(), it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded.

## **generators and iterables**

Our generator function oneTwoThree is not an iterator. It’s a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call.

If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3. Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-83ecb080-00275))_


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Iteration and Iterables: 199  Served by the Pot: Collections  One useful thing is to write a .from function that gathers an iterable into a particular collection type. JavaScript’s built-in ... [truncated] (1 shared statement(s))
- [[javascriptallonge-operator]] - shared statements: Operator shares source evidence from Iteration and Iterables: 192  Served by the Pot: Collections As we can see, we can use for...of with linked lists just as easily as with stacks. And there’s one more thing: You recall that t ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
