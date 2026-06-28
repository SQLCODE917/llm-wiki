---
page_id: javascriptallonge-follow
page_kind: concept
summary: Follow: 9 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-follow@bcd1240f2976fa10263af97f1d47e6e3
---

# Follow

What [[javascriptallonge]] covers about follow:

## Statements

### What JavaScript Allongé is. And isn't.

- vii

A Pull of the Lever: Prefaces

Following some of the chapters are a series of recipes designed to show the application of the chapter’s ideas in practical form. While the content of each chapter builds naturally on what was discussed in the previous chapter, the recipes may draw upon any aspect of the JavaScript programming language. _(javascriptallonge.pdf (source-range-83ecb080-00018))_

### Forewords to the First Edition

- ix

A Pull of the Lever: Prefaces

## **Forewords to the First Edition**

## **michael fogus**

As a life-long bibliophile and long-time follower of Reg’s online work, I was excited when he started writing books. However, I’m very conservative about books – let’s just say that if there was an aftershave scented to the essence of “Used Book Store” then I would be first in line to buy. So as you might imagine I was “skeptical” about the decision to release JavaScript Allongé as an ongoing ebook, with a pay-what-you-want model. However, Reg sent me a copy of his book and I was humbled. Not only was this a great book, but it was also a great way to write and distribute books. Having written books myself, I know the pain of soliciting and receiving feedback.

The act of writing is an iterative process with (very often) tight revision loops. However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. On more than one occasion I’ve found myself attempting to reify feedback with content that either no longer existed or was changed beyond recognition. However, with the Leanpub model the read-feedback-change process is extremely efficient, leaving in its wake a quality book that continues to get better as others likewise read and comment into infinitude.

In the case of JavaScript Allongé, you’ll find the Leanpub model a shining example of effectiveness. Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. No matter how much of an expert you think you are, JavaScript Allongé has something to teach you… about coffee. I kid.

As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you’ll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time.

Enjoy.

– Fogus, fogus.me[5]

## **matthew knox**

A different kind of language requires a different kind of book.

JavaScript holds surprising depths–its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many

5http://www.fogus.me _(javascriptallonge.pdf (source-range-83ecb080-00022))_

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

9

## **functions that return values and evaluate expressions**

We’ve seen () => 0. We know that (() => 0)() returns 0, and this is unsurprising. Likewise, the following all ought to be obvious: (() => 1)() _//=> 1_ (() => "Hello, JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** )() _//=> Infinity_

Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2. Can we put an expression to the right of the arrow?

(() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)()?

Let’s try it: (() => (() => 0)())() _//=> 0_

Yes we can! Functions can return the value of evaluating another function.

When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out. So we can also write: _(javascriptallonge.pdf (source-range-83ecb080-00046))_

- 13

The first sip: Basic Functions

## (() => {})()

_//=> undefined_

We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] Something like: { statement[1] ; statement[2] ; statement[3] ; ... ; statement[n] } We haven’t discussed these _statements_ . What’s a statement?

There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: () => { 1 + 1; 2 + 2 } But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: (() => { 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:

> 21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00050))_

### That Constant Coffee Craving

- 43

The first sip: Basic Functions

( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:

( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })() The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript’s design to facilitate a certain style of programming where you put the main logic up front, and the “helper functions” at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const) is essential for working with production code.

## **function declaration caveats**[34]

Function declarations are formally only supposed to be made at what we might call the “top level” of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea:

34 A number of the caveats discussed here were described in Jyrly Zaytsev’s excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-83ecb080-00079))_

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

### Making Data Out Of Functions

- Composing and Decomposing Data

163 But without building our way up to something insane like writing a JavaScript interpreter using JavaScript functions and no other data structures, let’s take things another step in a slightly different direction.

We used functions to replace arrays and POJOs, but we still use JavaScript’s built-in operators to test for equality (===) and to branch ?:.

## **say “please”**

We keep using the same pattern in our functions: aPair === EMPTY ? doSomething : doSomethingElse. This follows the philosophy we used with data structures: The function doing the work inspects the data structure.

We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here’s length again: **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest));

Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. Instead of writing length(list) and examining a list, we’ll write something like: **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(rest))) );

Now we’ll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. So let’s disambiguate our names: **const** pairFirst = K, pairRest = K(I), pair = V; **const** first = (list) => list( () => "ERROR: Can't take first of an empty list", (aPair) => aPair(pairFirst) ); **const** rest = (list) => list( _(javascriptallonge.pdf (source-range-83ecb080-00219))_


## Related pages

- [[javascriptallonge-code]] - shared statements: Code shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (3 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (2 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Mutation: Composing and Decomposing Data  120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsE ... [truncated] (2 shared statement(s))
- [[javascriptallonge-const]] - shared statements: Const shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from That Constant Coffee Craving: 43  The first sip: Basic Functions  ( **function** () { **return** fizzbuzz(); **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_ Althou ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))
- [[javascriptallonge-people]] - shared statements: People shares source evidence from Mutation: Composing and Decomposing Data  120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsE ... [truncated] (1 shared statement(s))
- [[javascriptallonge-rule]] - shared statements: Rule shares source evidence from As Little As Possible About Functions, But No Less: 13  The first sip: Basic Functions  ## (() => {})()  _//=> undefined_  We said that the function returns the result of evaluating a _block_ , and we said that a bloc ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Copy on Write: Composing and Decomposing Data  140  Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it shoul ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
