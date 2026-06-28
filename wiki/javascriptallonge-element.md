---
page_id: javascriptallonge-element
page_kind: concept
summary: Element: 17 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-element@17a008fd102b1e1f97f426fcbffc7e43
---

# Element

What [[javascriptallonge]] covers about element:

## Statements

### Arrays and Destructuring Arguments

- Composing and Decomposing Data

79 **const** wrap = (something) => [something]; wrap("lunch") _//=> ["lunch"]_ Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: [] === [] _//=> false_ [2 + 2] === [2 + 2] _//=> false_ **const** array_of_one = () => [1]; array_of_one() === array_of_one() _//=> false_

## **element references**

Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: **const** oneTwoThree = ["one", "two", "three"]; oneTwoThree[0] _//=> 'one'_ oneTwoThree[1] _//=> 'two'_ oneTwoThree[2] _//=> 'three'_ As we can see, JavaScript Arrays are zero-based[56] .

We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind?

56https://en.wikipedia.org/wiki/Zero-based_numbering _(javascriptallonge.pdf (source-range-83ecb080-00125))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

104

Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious.[64] The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend.

We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another.

**Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded.

So here’s a question: If this is such a slow approach, why do some examples of “functional” algorithms work this exact way?

> 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript’s built-in arrays work. _(javascriptallonge.pdf (source-range-83ecb080-00153))_

- Composing and Decomposing Data

107 **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; **const** oneToFive = node1;

This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. But it works the same way: If we want the head of a list, we call car on it: car(oneToFive) _//=> 1_ car is very fast, it simply extracts the first element of the cons cell.

But what about the rest of the list? cdr does the trick: cdr(oneToFive) _//=> [2,[3,[4,[5,null]]]]_ Again, it’s just extracting a reference from a cons cell, it’s very fast. In Lisp, it’s blazingly fast because it happens in hardware. There’s no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements.

So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible.

Getting back to JavaScript now, when we write [first, ...rest] to gather or spread arrays, we’re emulating the semantics of car and cdr, but not the implementation. We’re doing something laborious and memory-inefficient compared to using a linked list as Lisp did and as we can still do if we choose.

That being said, it is easy to understand and helps us grasp how literals and destructuring works, and how recursive algorithms ought to mirror the self-similarity of the data structures they manipulate. And so it is today that languages like JavaScript have arrays that are slow to split into the equivalent of a car/cdr pair, but instructional examples of recursive programs still have echoes of their Lisp origins.

We’ll look at linked lists again when we look at Plain Old JavaScript Objects.

68https://en.wikipedia.org/wiki/Linked_list _(javascriptallonge.pdf (source-range-83ecb080-00156))_

- Composing and Decomposing Data

108

## **so why arrays**

If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation).

For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases.

## **summary**

Although we showed how to use tail calls to map and fold over arrays with [first, ...rest], in reality this is not how it ought to be done. But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-00157))_

### Copy on Write

- Composing and Decomposing Data

136

Whereas if you have a linked list, and you take it’s “rest,” your “child” list shares its nodes with the “parent” list. And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent.

Let’s confirm our understanding: **const** parentArray = [1, 2, 3]; **const** [aFirst, ...childArray] = parentArray; parentArray[2] = "three"; childArray[0] = "two"; parentArray _//=> [1,2,"three"]_ childArray _//=> ["two",3]_ **const** EMPTY = { first: {}, rest: {} }; **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = parentList.rest; parentList.rest.rest.first = "three"; childList.first = "two"; parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ This is remarkably unsafe. If we _know_ that a list doesn’t share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We’ll end up reinventing reference counting and garbage collection.

## **a few utilities**

before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-00189))_

### Functional Iterators

- Composing and Decomposing Data

146

## **iterating**

Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop. Nevertheless, there is some value in being able to express some algorithms as iteration.

JavaScript has a particularly low-level version of for loop that mimics the semantics of the C language. Summing the elements of an array can be accomplished with: **const** arraySum = (array) => { **let** sum = 0; **for** ( **let** i = 0; i < array.length; ++i) { sum += array[i]; } **return** sum } arraySum([1, 4, 9, 16, 25]) _//=> 55_

Once again, we’re mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we’re getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0.

We can write this a slightly different way, using a while loop: **const** arraySum = (array) => { **let** done, sum = 0, i = 0; **while** ((done = i == array.length, !done)) { **const** value = array[i++]; sum += value; } **return** sum } arraySum([1, 4, 9, 16, 25]) _//=> 55_

Notice that buried inside our loop, we have bound the names done and value. We can put those into a POJO (a Plain Old JavaScript Object). It’ll be a little awkward, but we’ll be patient: _(javascriptallonge.pdf (source-range-83ecb080-00201))_

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

- 187

Served by the Pot: Collections

Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. Like this: **const** Stack2 = () => ({ array: [], index: -1, push (value) { **return this** .array[ **this** .index += 1] = value; }, pop () { **const** value = **this** .array[ **this** .index]; **this** .array[ **this** .index] = **undefined** ; **if** ( **this** .index >= 0) { **this** .index -= 1 } **return** value }, isEmpty () { **return this** .index < 0 }, iterator () { **let** iterationIndex = **this** .index; **return** { next () { **if** (iterationIndex > **this** .index) { iterationIndex = **this** .index; } **if** (iterationIndex < 0) { **return** {done: **true** }; } **else** { **return** {done: **false** , value: **this** .array[iterationIndex--]} } } } } }); _(javascriptallonge.pdf (source-range-83ecb080-00251))_

- 192

Served by the Pot: Collections As we can see, we can use for...of with linked lists just as easily as with stacks. And there’s one more thing: You recall that the spread operator (...) can spread the elements of an array in an array literal or as parameters in a function invocation.

Now is the time to note that we can spread any iterable. So we can spread the elements of an iterable into an array literal:

- ['some squares', ...someSquares] _//=> ["some squares", 1, 4, 9, 16, 25]_ And we can also spread the elements of an array literal into parameters: **const** firstAndSecondElement = (first, second) => ({first, second}) firstAndSecondElement(...stack) _//=> {"first":5,"second":10}_ This can be extremely useful.

One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

And if we have an infinite collection, spreading is going to fail outright as we’re about to see.

## **iterables out to infinity**

Iterables needn’t represent finite collections: **const** Numbers = { [Symbol.iterator] () { **let** n = 0; **return** { next: () => ({done: **false** , value: n++}) } } } There are useful things we can do with iterables representing an infinitely large collection. But let’s point out what we can’t do with them: _(javascriptallonge.pdf (source-range-83ecb080-00256))_

- 198

Served by the Pot: Collections

Like mapWith, they preserve the ordered collection semantics of whatever you give them.

And here’s a computation performed using operations on ordered collections: We’ll create an ordered collection of square numbers that end in one and are less than 1,000: **const** Squares = mapWith((x) => x * x, Numbers); **const** EndWithOne = filterWith((x) => x % 10 === 1, Squares); **const** UpTo1000 = untilWith((x) => (x > 1000), EndWithOne);

[...UpTo1000] _//=>_ [1,81,121,361,441,841,961] [...UpTo1000] _//=>_ [1,81,121,361,441,841,961] As we expect from an ordered collection, each time we iterate over UpTo1000, we begin at the beginning.

For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest]: **const** first = (iterable) => iterable[Symbol.iterator]().next().value; **const** rest = (iterable) => ({ [Symbol.iterator] () { **const** iterator = iterable[Symbol.iterator](); iterator.next(); **return** iterator; } }); like our other operations, rest preserves the ordered collection semantics of its argument.

## **from**

Having iterated over a collection, are we limited to for..do and/or gathering the elements in an array literal and/or gathering the elements into the parameters of a function? No, of course not, we can do anything we like with them. _(javascriptallonge.pdf (source-range-83ecb080-00262))_

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

205

A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out.

## **state machines**

Some iterables can be modelled as state machines. Let’s revisit the Fibonacci sequence. Again. One way to define it is:

- The first element of the fibonacci sequence is zero.

- The second element of the fibonacci sequence is one.

- Every subsequent element of the fibonacci sequence is the sum of the previous two elements.

Let’s write a generator:

_// Generation_ **const** fibonacci = () => { **let** a, b; console.log(a = 0); console.log(b = 1); **while** ( **true** ) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() _//=>_

0 1 1 2

3 5 8 13

21

34 _(javascriptallonge.pdf (source-range-83ecb080-00270))_

- 218

Served by the Pot: Collections **function** * tree (iterable) { **for** ( **const** e **of** iterable) { **if** (isIterable(e)) { **for** ( **const** ee **of** tree(e)) { **yield** ee; } } **else** { **yield** e; } } }; **for** ( **const** i **of** tree([1, [2, [3, 4], 5]])) { console.log(i); } _//=>_ 1 2 3 4 5

We take advantage of the for...of loop in a plain and direct way: For each element e, if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e.

JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

But while we’re here, let’s look at one bit of this code: **for** ( **const** ee **of** tree(e)) { **yield** ee; } These three lines say, in essence, “yield all the elements of TreeIterable(e), in order.” This comes up quite often when we have collections that are compounds, collections made from other collections. Consider this operation on iterables: _(javascriptallonge.pdf (source-range-83ecb080-00281))_

### Lazy and Eager Collections

- Served by the Pot: Collections

231

Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() This expression begins with a stack containing 30 elements. The top two are 29 and 28. It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter, we get an iterable that can iterate over the even squares, but not an actual stack or array.

Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack’s elements, and it only needs to square two of those elements, 29 and 28, to return the answer.

We can confirm this:

Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => { console.log(`squaring **${** x **}** `); **return** x * x }) .filter((x) => { console.log(`filtering **${** x **}** `); **return** x % 2 == 0 }) .first() _//=>_ squaring 29 filtering 841 squaring 28 filtering 784 784

If we write the almost identical thing with an array, we get a different behaviour: _(javascriptallonge.pdf (source-range-83ecb080-00295))_


## Related pages

- [[javascriptallonge-sequence]] - shared statements: Sequence shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (4 shared statement(s))
- [[javascriptallonge-collection]] - shared statements: Collection shares source evidence from Iteration and Iterables: Served by the Pot: Collections  183  ## **Iteration and Iterables**  **==> picture [469 x 313] intentionally omitted <==**  **Coffee Labels at the Saltspring Coffee ... [truncated] (2 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  104  Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious. ... [truncated] (2 shared statement(s))
- [[javascriptallonge-list]] - shared statements: List shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  107 **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; **const** oneTo ... [truncated] (2 shared statement(s))
- [[javascriptallonge-array]] - shared statements: Array shares source evidence from Arrays and Destructuring Arguments: Composing and Decomposing Data  79 **const** wrap = (something) => [something]; wrap("lunch") _//=> ["lunch"]_ Array literals are expressions, and arrays are _refere ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Iteration and Iterables: 187  Served by the Pot: Collections  Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get t ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from Iteration and Iterables: 187  Served by the Pot: Collections  Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get t ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterable]] - shared statements: Iterable shares source evidence from Iteration and Iterables: 198  Served by the Pot: Collections  Like mapWith, they preserve the ordered collection semantics of whatever you give them.  And here’s a computation performed usin ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  107 **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; **const** oneTo ... [truncated] (1 shared statement(s))
- [[javascriptallonge-knowing]] - shared statements: Knowing shares source evidence from Functional Iterators: Composing and Decomposing Data  146  ## **iterating**  Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplish ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  104  Worse, the JavaScript Engine actually copies the elements from prepend into the new array one at a time. That is very laborious. ... [truncated] (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-reference]] - shared statements: Reference shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Iteration and Iterables: 198  Served by the Pot: Collections  Like mapWith, they preserve the ordered collection semantics of whatever you give them.  And here’s a computation performed usin ... [truncated] (1 shared statement(s))
- [[javascriptallonge-second]] - shared statements: Second shares source evidence from Generating Iterables: Served by the Pot: Collections  205  A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re re ... [truncated] (1 shared statement(s))
- [[javascriptallonge-whenever]] - shared statements: Whenever shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
