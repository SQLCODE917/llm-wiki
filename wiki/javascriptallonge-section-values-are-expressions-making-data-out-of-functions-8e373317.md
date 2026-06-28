---
page_id: javascriptallonge-section-values-are-expressions-making-data-out-of-functions-8e373317
page_kind: source
summary: values are expressions / Making Data Out Of Functions: 76 source-backed entries and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-making-data-out-of-functions-8e373317@3c622080c8b73d21d0ee8bab05cd38ba
---

# values are expressions / Making Data Out Of Functions

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-4763e204]] - broader source section
- [[javascriptallonge-section-values-are-expressions-making-data-out-of-functions-the-kestrel-and-the-idiot-6e750175]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-making-data-out-of-functions-backwardness-ddef4f83]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-making-data-out-of-functions-the-vireo-a6abbaee]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-making-data-out-of-functions-lists-with-functions-as-data-15914c4a]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-making-data-out-of-functions-say-please-1c1db3a9]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-making-data-out-of-functions-functions-are-not-the-real-point-0fb8ff56]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-making-data-out-of-functions-a-return-to-backward-thinking-75b5fc78]] - narrower source section

## Statements

- In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case. _(javascriptallonge.pdf (source-range-83ecb080-01319))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-01320))_
- For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-01320))_
- They searched for a radically simpler set of tools that could accomplish all of the same things. _(javascriptallonge.pdf (source-range-83ecb080-01325))_
- We can model lists just using functions. _(javascriptallonge.pdf (source-range-83ecb080-01326))_
- They established that arbitrary computations could be represented a small set of axiomatic components. _(javascriptallonge.pdf (source-range-83ecb080-01326))_
- For example, we don’t need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-83ecb080-01326))_
- For example, we don’t need arrays to represent lists, or even POJOs to represent nodes in a linked list. _(javascriptallonge.pdf (source-range-83ecb080-01326))_
- The oscin.es[77] library contains code for all of the standard combinators and for experimenting using the standard notation. _(javascriptallonge.pdf (source-range-83ecb080-01328))_
- Let’s start with some of the building blocks of combinatory logic, the K, I, and V combinators, nicknamed the “Kestrel”, the “Idiot Bird”, and the “Vireo:” > 76http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 _(javascriptallonge.pdf (source-range-83ecb080-01329))_

## Statements by subsection

### values are expressions / Making Data Out Of Functions / the kestrel and the idiot

- The kestrel, or K, is a function that makes constant functions. _(javascriptallonge.pdf (source-range-83ecb080-01334))_
- You give it a value, and it returns a constant function that gives that value. _(javascriptallonge.pdf (source-range-83ecb080-01334))_
- A _constant function_ is a function that always returns the same thing, no matter what you give it. _(javascriptallonge.pdf (source-range-83ecb080-01334))_
- The _identity function_ is a function that evaluates to whatever parameter you pass it. _(javascriptallonge.pdf (source-range-83ecb080-01336))_
- Given two values, we can say that K always returns the _first_ value: K(x)(y) => x (that’s not valid JavaScript, but it’s essentially how it works). _(javascriptallonge.pdf (source-range-83ecb080-01340))_
- Given two values, we can say that K always returns the _first_ value, and given two values, K(I) always returns the _second_ value. _(javascriptallonge.pdf (source-range-83ecb080-01351))_

### values are expressions / Making Data Out Of Functions / backwardness

- Our first and second functions are a little different than what most people are used to when we talk about functions that access data. _(javascriptallonge.pdf (source-range-83ecb080-01353))_
- In both cases, the functions first and second know how the data is represented, whether it be an array or an object. _(javascriptallonge.pdf (source-range-83ecb080-01356))_
- So if we wanted to use them with a two-element array, we’d need to have a piece of code that calls some code. _(javascriptallonge.pdf (source-range-83ecb080-01357))_
- Our latin data structure is no longer a dumb data structure, it’s a function. _(javascriptallonge.pdf (source-range-83ecb080-01361))_

### values are expressions / Making Data Out Of Functions / the vireo

- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-83ecb080-01363))_
- Let’s extract those into parameters: (first, second) => (selector) => selector(first)(second) For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: (first) => (second) => (selector) => selector(first)(second) Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default): **const** first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second); **const** latin = pair("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_ _(javascriptallonge.pdf (source-range-83ecb080-01364))_
- It says, “take these two values and apply them to this function.” There are other, similar combinators that apply values to functions. _(javascriptallonge.pdf (source-range-83ecb080-01368))_
- One notable example is the “thrush” or T combinator: It takes one value and applies it to a function. _(javascriptallonge.pdf (source-range-83ecb080-01368))_
- It is known to most programmers as .tap. _(javascriptallonge.pdf (source-range-83ecb080-01368))_

### values are expressions / Making Data Out Of Functions / lists with functions as data

- Here’s another look at linked lists using POJOs. _(javascriptallonge.pdf (source-range-83ecb080-01371))_
- We write them in a backwards way, but they seem to work. _(javascriptallonge.pdf (source-range-83ecb080-01378))_
- Presto, **we can use pure functions to represent a linked list** . _(javascriptallonge.pdf (source-range-83ecb080-01380))_
- And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-01380))_
- We used functions to replace arrays and POJOs, but we still use JavaScript’s built-in operators to test for equality (===) and to branch ?:. _(javascriptallonge.pdf (source-range-83ecb080-01383))_

### values are expressions / Making Data Out Of Functions / say “please”

- This follows the philosophy we used with data structures: The function doing the work inspects the data structure. _(javascriptallonge.pdf (source-range-83ecb080-01385))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-01386))_
- We can reverse this: Instead of asking a pair if it is empty and then deciding what to do, we can ask the pair to do it for us. _(javascriptallonge.pdf (source-range-83ecb080-01386))_
- Let’s presume we are working with a slightly higher abstraction, we’ll call it a list. _(javascriptallonge.pdf (source-range-83ecb080-01387))_
- Now we’ll need to write first and rest functions for a list, and those names will collide with the first and rest we wrote for pairs. _(javascriptallonge.pdf (source-range-83ecb080-01388))_
- We can write reverse and mapWith as well. _(javascriptallonge.pdf (source-range-83ecb080-01394))_
- We have managed to provide the exact same functionality that === and ?: provided, but using functions and nothing else. _(javascriptallonge.pdf (source-range-83ecb080-01397))_

### values are expressions / Making Data Out Of Functions / functions are not the real point

- You can establish that K and K(I) can represent true and false, model magnitudes with Church Numerals[79] or Surreal Numbers[80] , and build your way up to printing FizzBuzz. _(javascriptallonge.pdf (source-range-83ecb080-01399))_
- There are lots of similar texts explaining how to construct complex semantics out of functions. _(javascriptallonge.pdf (source-range-83ecb080-01399))_
- Functions are a fundamental building block of computation. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- They are “axioms” of combinatory logic, and can be used to compute anything that JavaScript can compute. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- Knowing how to make a linked list out of functions is not really necessary for the working programmer. _(javascriptallonge.pdf (source-range-83ecb080-01402))_
- Practically speaking, languages like JavaScript already provide arrays with mapping and folding methods, choice operations, and other rich constructs. _(javascriptallonge.pdf (source-range-83ecb080-01402))_
- However, that is not the interesting thing to note here. _(javascriptallonge.pdf (source-range-83ecb080-01402))_
- (Knowing that it can be done, on the other hand, is very important to understanding computer science.) Knowing how to make a list out of just functions is a little like knowing that photons are the Gauge Bosons[81] of the electromagnetic force. _(javascriptallonge.pdf (source-range-83ecb080-01402))_

### values are expressions / Making Data Out Of Functions / a return to backward thinking

- To make pairs work, we did things _backwards_ , we passed the first and rest functions to the pair, and the pair called our function. _(javascriptallonge.pdf (source-range-83ecb080-01409))_
- As it happened, the pair was composed by the vireo (or V combinator): (x) => (y) => (z) => z(x)(y). _(javascriptallonge.pdf (source-range-83ecb080-01409))_
- We could have written a pair that stored its elements in an array, or a pair that stored its elements in a POJO. _(javascriptallonge.pdf (source-range-83ecb080-01410))_
- All we know is that we can pass the pair function a function of our own, at it will be called with the elements of the pair. _(javascriptallonge.pdf (source-range-83ecb080-01410))_
- But we could have done something completely different. _(javascriptallonge.pdf (source-range-83ecb080-01410))_
- The exact implementation of a pair is hidden from the code that uses a pair. _(javascriptallonge.pdf (source-range-83ecb080-01411))_
- This is a little gratuitous, but it makes the point: The code that uses the data doesn’t reach in and touch it: The code that uses the data provides some code and asks the data to do something with it. _(javascriptallonge.pdf (source-range-83ecb080-01412))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-01413))_
- We’re passing list what we want done with an empty list, and what we want done with a list that has at least one element. _(javascriptallonge.pdf (source-range-83ecb080-01413))_
- We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-83ecb080-01413))_
- It presumes you can compare these things with the === operator. _(javascriptallonge.pdf (source-range-83ecb080-01419))_
- We can fix this with an isEmpty function, but now we’re pushing even more knowledge about the structure of lists into the code that uses them. _(javascriptallonge.pdf (source-range-83ecb080-01419))_
- It presumes there is one canonical empty list value. _(javascriptallonge.pdf (source-range-83ecb080-01419))_
- It is a tenet of Object-Oriented Programming, but it is **not** exclusive to OOP: We can and should design data structures to hide implementation information from the code that use them, whether we are working with functions, objects, or both. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- Having a list know itself whether it is empty hides implementation information from the code that uses lists. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is a fundamental principle of good design. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- There are many tools for hiding implementation information, and we have now seen two particularly powerful patterns: _(javascriptallonge.pdf (source-range-83ecb080-01421))_
- - Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-83ecb080-01422))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01320))_

> For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01323))_

> OneTwoThree.first _//=> 1_ OneTwoThree.rest.first _//=> 2_

### Technical atom 2

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01324))_

> OneTwoThree.rest.rest.first _//=> 3_ **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) _//=> 3_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01334))_

> A _constant function_ is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K, is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01335))_

> For example: **const** K = (x) => (y) => x; **const** fortyTwo = K(42); fortyTwo(6) _//=> 42_ fortyTwo("Hello") _//=> 42_

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01338))_

> K(6)(7) _//=> 6_

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01339))_

> K(12)(24) _//=> 12_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01341))_

> Now, an interesting thing happens when we pass functions to each other. Consider K(I). From what we just wrote, K(x)(y) => x So K(I)(x) => I. Makes sense. Now let’s tack one more invocation on: What is K(I)(x)(y)? If K(I)(x) => I, then K(I)(x)(y) === I(y) which is y.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01342))_

> Therefore, K(I)(x)(y) => y:

### Technical atom 7

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01345))_

> K(I)(6)(7) _//=> 7_

### Technical atom 8

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01346))_

> K(I)(12)(24) _//=> 24_

### Technical atom 9

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01348))_

> K("primus")("secundus") _//=> "primus"_

### Technical atom 10

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01349))_

> K(I)("primus")("secundus") _//=> "secundus"_

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01364))_

> For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters: (first, second) => (selector) => selector(first)(second) For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: (first) => (second) => (selector) => selector(first)(second) Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specifi

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01365))_

> If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y).

### Technical atom 12

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01390))_

> How would all this work? Let’s start with the obvious. What is an empty list?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01391))_

> **const** EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty() And what is a node of a list?

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01391))_

> **const** EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty() And what is a node of a list?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01392))_

> **const** node = (x) => (y) => (whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));
