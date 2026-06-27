---
page_id: javascriptallonge-section-making-data-out-of-functions-654f2c10
page_kind: source
summary: Making Data Out Of Functions: 120 source-backed entries and 52 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-making-data-out-of-functions-654f2c10@60268739a9cd1b2ae2e78cf02639707a
---

# Making Data Out Of Functions

From [[javascriptallonge]].

## Statements

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. _(javascriptallonge.pdf (source-range-83ecb080-02032))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-02033))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-02033))_
- They searched for a radically simpler set of tools that could accomplish all of the same things. _(javascriptallonge.pdf (source-range-83ecb080-02040))_
- We can model lists just using functions. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- They established that arbitrary computations could be represented a small set of axiomatic components. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- For example, we don’t need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- For example, we don’t need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-83ecb080-02041))_
- The oscin.es[77] library contains code for all of the standard combinators and for experimenting using the standard notation. _(javascriptallonge.pdf (source-range-83ecb080-02043))_
- Let’s start with some of the building blocks of combinatory logic, the K, I, and V combinators, nicknamed the “Kestrel”, the “Idiot Bird”, and the “Vireo:” _(javascriptallonge.pdf (source-range-83ecb080-02044))_
- You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- The kestrel, or K, is a function that makes constant functions. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- A _constant function_ is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-83ecb080-02051))_
- The _identity function_ is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-83ecb080-02056))_
- Given two values, we can say that K always returns the _first_ value: K(x)(y) => x (that’s not valid JavaScript, but it’s essentially how it works). _(javascriptallonge.pdf (source-range-83ecb080-02060))_
- Given two values, we can say that K always returns the _first_ value, and given two values, K(I) always returns the _second_ value. _(javascriptallonge.pdf (source-range-83ecb080-02074))_
- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-83ecb080-02076))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-83ecb080-02085))_
- So if we wanted to use them with a two-element array, we’d need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-83ecb080-02086))_
- Our latin data structure is no longer a dumb data structure, it’s a function. _(javascriptallonge.pdf (source-range-83ecb080-02093))_
- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-83ecb080-02095))_
- For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: _(javascriptallonge.pdf (source-range-83ecb080-02098))_
- Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default): _(javascriptallonge.pdf (source-range-83ecb080-02100))_
- It is known to most programmers as .tap. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- It says, “take these two values and apply them to this function.” There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- One notable example is the “thrush” or T combinator: It takes one value and applies it to a function. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- As an aside, the Vireo is a little like JavaScript’s .apply function. _(javascriptallonge.pdf (source-range-83ecb080-02114))_
- Here’s another look at linked lists using POJOs. _(javascriptallonge.pdf (source-range-83ecb080-02117))_
- reverse(delayed) : mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed)); _(javascriptallonge.pdf (source-range-83ecb080-02124))_
- We write them in a backwards way, but they seem to work. _(javascriptallonge.pdf (source-range-83ecb080-02131))_
- And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-02133))_
- Presto, **we can use pure functions to represent a linked list** . _(javascriptallonge.pdf (source-range-83ecb080-02133))_
- We used functions to replace arrays and POJOs, but we still use JavaScript’s built-in operators to test for equality (===) and to branch ?:. _(javascriptallonge.pdf (source-range-83ecb080-02137))_
- This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-83ecb080-02139))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-02140))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-02140))_
- Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. _(javascriptallonge.pdf (source-range-83ecb080-02142))_
- Now we’ll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. _(javascriptallonge.pdf (source-range-83ecb080-02144))_
- We can write reverse and mapWith as well. _(javascriptallonge.pdf (source-range-83ecb080-02158))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-02162))_
- There are lots of similar texts explaining how to construct complex semantics out of functions. _(javascriptallonge.pdf (source-range-83ecb080-02164))_
- You can establish that K and K(I) can represent true and false, model magnitudes with Church Numerals[79] or Surreal Numbers[80] , and build your way up to printing FizzBuzz. _(javascriptallonge.pdf (source-range-83ecb080-02164))_
- Functions are a fundamental building block of computation. _(javascriptallonge.pdf (source-range-83ecb080-02166))_
- They are “axioms” of combinatory logic, and can be used to compute anything that JavaScript can compute. _(javascriptallonge.pdf (source-range-83ecb080-02166))_
- Knowing how to make a linked list out of functions is not really necessary for the working programmer. _(javascriptallonge.pdf (source-range-83ecb080-02167))_
- However, that is not the interesting thing to note here. _(javascriptallonge.pdf (source-range-83ecb080-02167))_
- (Knowing that it can be done, on the other hand, is very important to understanding computer science.) _(javascriptallonge.pdf (source-range-83ecb080-02167))_
- Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. _(javascriptallonge.pdf (source-range-83ecb080-02167))_
- Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons[81] of the electromagnetic force. _(javascriptallonge.pdf (source-range-83ecb080-02168))_
- As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y). _(javascriptallonge.pdf (source-range-83ecb080-02176))_
- To make pairs work, we did things _backwards_ , we passed the first and rest functions to the pair, and the pair called our function. _(javascriptallonge.pdf (source-range-83ecb080-02176))_
- All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-83ecb080-02177))_
- But we could have done something completely different. _(javascriptallonge.pdf (source-range-83ecb080-02177))_
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. _(javascriptallonge.pdf (source-range-83ecb080-02177))_
- The exact implementation of a pair is hidden from the code that uses a pair. _(javascriptallonge.pdf (source-range-83ecb080-02178))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-83ecb080-02185))_
- We’re passing list what we want done with an empty list, and what we want done with a list that has at least one element. _(javascriptallonge.pdf (source-range-83ecb080-02187))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-02187))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-02187))_
- This is fundamentally _not_ the same thing as this code for the length of a linked list: _(javascriptallonge.pdf (source-range-83ecb080-02190))_
- It presumes there is one canonical empty list value. _(javascriptallonge.pdf (source-range-83ecb080-02195))_
- We can fix this with an isEmpty function, but now we’re pushing even more knowledge about the structure of lists into the code that uses them. _(javascriptallonge.pdf (source-range-83ecb080-02195))_
- It presumes you can compare these things with the === operator. _(javascriptallonge.pdf (source-range-83ecb080-02195))_
- This is a fundamental principle of good design. _(javascriptallonge.pdf (source-range-83ecb080-02196))_
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. _(javascriptallonge.pdf (source-range-83ecb080-02196))_
- It is a tenet of Object-Oriented Programming, but it is **not** exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. _(javascriptallonge.pdf (source-range-83ecb080-02196))_
- There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns: _(javascriptallonge.pdf (source-range-83ecb080-02197))_
- - Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-83ecb080-02198))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02033))_

> For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02036))_

> **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02037))_

> OneTwoThree.first _//=> 1_ OneTwoThree.rest.first _//=> 2_

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02038))_

> OneTwoThree.rest.rest.first _//=> 3_ **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1);

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02039))_

> length(OneTwoThree) _//=> 3_

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02049))_

> **const** K = (x) => (y) => x; **const** I = (x) => (x); **const** V = (x) => (y) => (z) => z(x)(y);

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02053))_

> **const** K = (x) => (y) => x; **const** fortyTwo = K(42);

### Technical atom 7

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02054))_

> fortyTwo(6) _//=> 42_

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02055))_

> fortyTwo("Hello") _//=> 42_

### Technical atom 9

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02058))_

> K(6)(7) _//=> 6_

### Technical atom 10

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02059))_

> K(12)(24) _//=> 12_

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02061))_

> Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02062))_

> Therefore, K(I)(x)(y) => y:

### Technical atom 12

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02065))_

> K(I)(6)(7) _//=> 7_

### Technical atom 13

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02066))_

> K(I)(12)(24) _//=> 24_

### Technical atom 14

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02068))_

> K("primus")("secundus") _//=> "primus"_

### Technical atom 15

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02069))_

> K(I)("primus")("secundus") _//=> "secundus"_

### Technical atom 16

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02070))_

> If we are not feeling particularly academic, we can name our functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02071))_

> **const** first = K, second = K(I);

### Technical atom 17

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02070))_

> If we are not feeling particularly academic, we can name our functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02072))_

> first("primus")("secundus") _//=> "primus"_

### Technical atom 18

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02070))_

> If we are not feeling particularly academic, we can name our functions:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02073))_

> second("primus")("secundus") _//=> "secundus"_

### Technical atom 19

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02076))_

> Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we’d write them like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02079))_

> **const** first = ([first, second]) => first, second = ([first, second]) => second;

### Technical atom 20

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02080))_

> **const** latin = ["primus", "secundus"];

### Technical atom 21

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02081))_

> first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_

### Technical atom 22

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02082))_

> Or if we were using a POJO, we’d write them like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02083))_

> **const** first = ({first, second}) => first, second = ({first, second}) => second; **const** latin = {first: "primus", second: "secundus"};

### Technical atom 23

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02082))_

> Or if we were using a POJO, we’d write them like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02084))_

> first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_

### Technical atom 24

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02088))_

> **const** first = K, second = K(I);

### Technical atom 25

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02089))_

> **const** latin = (selector) => selector("primus")("secundus");

### Technical atom 26

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02090))_

> latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_

### Technical atom 27

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02096))_

> For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02097))_

> (first, second) => (selector) => selector(first)(second)

### Technical atom 28

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02098))_

> For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02099))_

> (first) => (second) => (selector) => selector(first)(second)

### Technical atom 29

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02100))_

> Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default):

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02101))_

> **const** first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second);

### Technical atom 30

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02100))_

> Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default):

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02102))_

> **const** latin = pair("primus")("secundus");

### Technical atom 31

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02107))_

> If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y).

### Technical atom 32

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02111))_

> **const** first = K, second = K(I), pair = V;

### Technical atom 33

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02112))_

> **const** latin = pair("primus")("secundus");

### Technical atom 34

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02113))_

> latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_

### Technical atom 35

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02119))_

> We can write length and mapWith functions over it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02122))_

> **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(rest(aPair));

### Technical atom 36

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02123))_

> length(l123) _//=> 3_

### Technical atom 37

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02125))_

> **const** doubled = mapWith((x) => x * 2, l123); first(doubled) _//=> 2_ first(rest(doubled)) _//=> 4_ first(rest(rest(doubled))) _//=> 6_

### Technical atom 38

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02126))_

> Can we do the same with the linked lists we build out of functions? Yes:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02127))_

> **const** first = K, rest = K(I), pair = V, EMPTY = (() => {}); **const** l123 = pair(1)(pair(2)(pair(3)(EMPTY))); l123(first) _//=> 1_ l123(rest)(first)

### Technical atom 39

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02140))_

> We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. Here’s length again:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02141))_

> **const** length = (aPair) => aPair === EMPTY ? 0 : 1 + length(aPair(rest));

### Technical atom 40

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02142))_

> Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. Instead of writing length(list) and examining a list, we’ll write something like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02143))_

> **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(rest))) );

### Technical atom 41

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02149))_

> We’ll also write a handy list printer:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02150))_

> **const** print = (list) => list( () => "", (aPair) => ` **${** aPair(pairFirst) **} ${** print(aPair(pairRest)) **}** ` );

### Technical atom 42

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02151))_

> How would all this work? Let’s start with the obvious. What is an empty list?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02152))_

> **const** EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty()

### Technical atom 43

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02153))_

> And what is a node of a list?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02154))_

> **const** node = (x) => (y) => (whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));

### Technical atom 44

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02156))_

> **const** l123 = node(1)(node(2)(node(3)(EMPTYLIST)));

### Technical atom 45

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02157))_

> print(l123) _//=> 1 2 3_

### Technical atom 46

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02178))_

> The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02179))_

> **const** first = K, second = K(I), pair = (first) => (second) => { **const** pojo = {first, second};

### Technical atom 47

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02178))_

> The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02180))_

> **return** (selector) => selector(pojo.first)(pojo.second); };

### Technical atom 48

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02178))_

> The exact implementation of a pair is hidden from the code that uses a pair. Here, we’ll prove it:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02181))_

> **const** latin = pair("primus")("secundus");

### Technical atom 49

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02184))_

> latin(second) _//=> "secundus"_

### Technical atom 50

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02185))_

> This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. The same thing happens with our lists. Here’s length for lists:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02186))_

> **const** length = (list) => list( () => 0, (aPair) => 1 + length(aPair(pairRest))) );

### Technical atom 51

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02190))_

> We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02191))_

> **const** length = (node, delayed = 0) =>

### Technical atom 52

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02190))_

> We won’t bother here, but it’s easy to see how to swap our functions out and replace them with an array. Or a column in a database. This is fundamentally _not_ the same thing as this code for the length of a linked list:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02192))_

> node === EMPTY
