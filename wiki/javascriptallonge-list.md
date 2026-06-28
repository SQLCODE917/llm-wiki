---
page_id: javascriptallonge-list
page_kind: concept
summary: List: 19 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-list@c36b5bb3d44ca304cf15af40b2e84e7d
---

# List

What [[javascriptallonge]] covers about list:

## Statements

### Arrays and Destructuring Arguments

- Composing and Decomposing Data

78

## **Arrays and Destructuring Arguments**

While we have mentioned arrays briefly, we haven’t had a close look at them. Arrays are JavaScript’s “native” representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality.

## **array literals**

JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: [] _//=> []_ We can create an array with one or more _elements_ by placing them between the brackets and separating the items with commas. Whitespace is optional:

[1] _//=> [1]_ [2, 3, 4] _//=> [2,3,4]_ Any expression will work:

[ 2, 3, 2 + 2 ] _//=> [2,3,4]_ Including an expression denoting another array: [[[[[]]]]] This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

Any expression will do, including names: _(javascriptallonge.pdf (source-range-83ecb080-00124))_

- Composing and Decomposing Data

91 **const** truthyAll = ([first, ...rest]) => first === **undefined**

? [] : [!!first, ...truthyAll(rest)]; truthyAll([ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_ This specific case of linear recursion is called “mapping,” and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let’s “extract” the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

Given the signature: **const** mapWith = (fn, array) => _// ..._

We can write it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**const** mapWith = (fn, [first, ...rest]) => first === **undefined** ? [] : [fn(first), ...mapWith(fn, rest)]; mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_ mapWith((x) => !!x, [ **null** , **true** , 25, **false** , "foo"]) _//=> [false,true,true,false,true]_

## **folding**

With the exception of the length example at the beginning, our examples so far all involve rebuilding a solution using spreads. But they needn’t. A function to compute the sum of the squares of a list of numbers might look like this: _(javascriptallonge.pdf (source-range-83ecb080-00137))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

106

In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.

Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp’s basic data type is often said to be the list, but in actuality it was the “cons cell,” the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells.

Lists were represented as linked lists of cons cells, with each cell’s head pointing to an element and the tail pointing to another cons cell.

Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today’s standards. Although the 704 used core memory, it still used vacuum tubes for its logic. Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance.

Here’s the scheme in JavaScript, using two-element arrays to represent cons cells: **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;

We can make a list by calling cons repeatedly, and terminating it with null: **const** oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, **null** )))));

## oneToFive

_//=> [1,[2,[3,[4,[5,null]]]]]_ Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like: _(javascriptallonge.pdf (source-range-83ecb080-00155))_

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

### Plain Old JavaScript Objects

- Composing and Decomposing Data

109

## **Plain Old JavaScript Objects**

Lists are not the only way to represent collections of things, but they are the “oldest” data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list: **const** remember = ["the milk", "the coffee beans", "the biscotti"]; And they can be used to store heterogeneous things in various levels of structure: **const** user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];

Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable. So back when lists were the only things available, programmers would introduce constants to make things easier on themselves: **const** NAME = 0, FIRST = 0, LAST = 1, OCCUPATION = 1, TITLE = 0, RESPONSIBILITIES = 1; **const** user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "Ja\ vaScript Spessore", "CoffeeScript Ristretto"]]];

Now they could write user[NAME][LAST] or user[OCCUPATION][TITLE] instead of user[0][1] or user[1][0]. Over time, this need to build heterogeneous data structures with access to members by name evolved into the Dictionary[69] data type, a mapping from a unique set of objects to another set of objects.

Dictionaries store key-value pairs, so instead of binding NAME to 0 and then storing a name in an array at index 0, we can bind a name directly to name in a dictionary, and we let JavaScript sort out whether the implementation is a list of key-value pairs, a hashed collection, a tree of some sort, or anything else.

JavaScript has dictionaries, and it calls them “objects.” The word “object” is loaded in programming circles, due to the widespread use of the term “object-oriented programming” that was coined by Alan Kay but has since come to mean many, many things to many different people.

In JavaScript, an object is a map from string keys to values.

> 69https://en.wikipedia.org/wiki/Associative_array _(javascriptallonge.pdf (source-range-83ecb080-00159))_

- 115

Composing and Decomposing Data **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };

OneTwoThree.first _//=> 1_ OneTwoThree.rest _//=> {"first":2,"rest":{"first":3,"rest":{}}}_ OneTwoThree.rest.rest.first _//=> 3_

Taking the length of a linked list is easy: **const** length = (node, delayed = 0) => node === EMPTY ? delayed : length(node.rest, delayed + 1); length(OneTwoThree) _//=> 3_

What about mapping? Well, let’s start with the simplest possible thing, making a _copy_ of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn’t fast is naïvely copying a list: **const** slowcopy = (node) => node === EMPTY ? EMPTY : { first: node.first, rest: slowcopy(node.rest)}; slowcopy(OneTwoThree) _//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{}}}}_ The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return.

We could follow the strategy of delaying the work. Let’s write that naively: _(javascriptallonge.pdf (source-range-83ecb080-00165))_

- 117

Composing and Decomposing Data

Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away.

Mind you, this is still much, much faster than making partial copies of arrays. For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-00167))_

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

- 123

Composing and Decomposing Data **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first, rest }; **return** copy(rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first, rest }; tail.rest = newNode; **return** copy(node.rest, head, newNode); } } This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we’re in the midst of creating a brand new list, we aren’t sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

Armed with this basic copy implementation, we can write mapWith: **const** mapWith = (fn, node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail === **null** ) { **const** { first, rest } = node; **const** newNode = { first: fn(first), rest }; **return** mapWith(fn, rest, newNode, newNode); } **else** { **const** { first, rest } = node; **const** newNode = { first: fn(first), rest }; tail.rest = newNode; **return** mapWith(fn, node.rest, head, newNode); } } mapWith((x) => 1.0 / x, OneToFive) _(javascriptallonge.pdf (source-range-83ecb080-00174))_

### Copy on Write

- Composing and Decomposing Data

135

## **Copy on Write**

**==> picture [469 x 364] intentionally omitted <==**

**The Coffee Cow**

We’ve seen how to build lists with arrays and with linked lists. We’ve touched on an important difference between them:

- When you take the rest of an array with destructuring ([first, ...rest]), you are given a _copy_ of the elements of the array.

- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list.

The consequence of this is that if you have an array, and you take it’s “rest,” your “child” array is a copy of the elements of the parent array. And therefore, modifications to the parent do not affect the child, and modifications to the child do not affect the parent. _(javascriptallonge.pdf (source-range-83ecb080-00188))_

- Composing and Decomposing Data

136

Whereas if you have a linked list, and you take it’s “rest,” your “child” list shares its nodes with the “parent” list. And therefore, modifications to the parent also modify the child, and modifications to the child also modify the parent.

Let’s confirm our understanding: **const** parentArray = [1, 2, 3]; **const** [aFirst, ...childArray] = parentArray; parentArray[2] = "three"; childArray[0] = "two"; parentArray _//=> [1,2,"three"]_ childArray _//=> ["two",3]_ **const** EMPTY = { first: {}, rest: {} }; **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = parentList.rest; parentList.rest.rest.first = "three"; childList.first = "two"; parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ This is remarkably unsafe. If we _know_ that a list doesn’t share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We’ll end up reinventing reference counting and garbage collection.

## **a few utilities**

before we go any further, let’s write a few naïve list utilities so that we can work at a slightly higher level of abstraction: _(javascriptallonge.pdf (source-range-83ecb080-00189))_

- Composing and Decomposing Data

138 **const** childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":"two","rest":{"first":"three","rest":{"first":\_ {},"rest":{}}}}} childList _//=> {"first":"two","rest":{"first":"three","rest":{"first":{},"rest":{}}}}_ Our new at and set functions behave similarly to array[index] and array[index] = value. The main difference is that array[index] = value evaluates to value, while set(index, value, list) evaluates to the modified list.

## **copy-on-read**

So back to the problem of structure sharing. One strategy for avoiding problems is to be _pessimistic_ . Whenever we take the rest of a list, make a copy.

**const** rest = ({first, rest}) => copy(rest); **const** parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\ }}; **const** childList = rest(parentList); **const** newParentList = set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\_ rest":{}}}}} childList //=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}} This strategy is called “copy-on-read”, because when we attempt the parent to “read” the value of a child of the list, we make a copy and read the copy of the child. Thereafter, we can write to the parent or the copy of the child freely.

As we expected, making a copy lets us modify the copy without interfering with the original. This is, however, expensive. Sometimes we don’t need to make a copy because we won’t be modifying the list. Our mapWith function would be very expensive if we make a copy every time we call rest(node).

There’s also a bug: What happens when we modify the first element of a list? But before we fix that, let’s try being lazy about copying. _(javascriptallonge.pdf (source-range-83ecb080-00191))_

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

- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  107 **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; **const** oneTo ... [truncated] (2 shared statement(s))
- [[javascriptallonge-node]] - shared statements: Node shares source evidence from Mutation: 123  Composing and Decomposing Data **const** copy = (node, head = **null** , tail = **null** ) => { **if** (node === EMPTY) { **return** head; } **else if** (tail = ... [truncated] (2 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Plain Old JavaScript Objects: 115  Composing and Decomposing Data **const** EMPTY = {}; **const** OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \ } } };  OneTwoThree.f ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Arrays and Destructuring Arguments: Composing and Decomposing Data  91 **const** truthyAll = ([first, ...rest]) => first === **undefined**  ? [] : [!!first, ...truthyAll(rest)]; truthyAll([ **null** , ... [truncated] (1 shared statement(s))
- [[javascriptallonge-length]] - shared statements: Length shares source evidence from Plain Old JavaScript Objects: 117  Composing and Decomposing Data  Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, a ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pass]] - shared statements: Pass shares source evidence from Making Data Out Of Functions: Composing and Decomposing Data  166 So what _is_ interesting about this? What nags at our brain as we’re falling asleep after working our way through this?  ## **a r ... [truncated] (1 shared statement(s))
- [[javascriptallonge-rest]] - shared statements: Rest shares source evidence from Copy on Write: Composing and Decomposing Data  138 **const** childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-return]] - shared statements: Return shares source evidence from Mutation: Composing and Decomposing Data  120 **const** allHallowsEve = [2012, 10, 31]; ( **function** (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsE ... [truncated] (1 shared statement(s))
- [[javascriptallonge-seen]] - shared statements: Seen shares source evidence from Copy on Write: Composing and Decomposing Data  135  ## **Copy on Write**  **==> picture [469 x 364] intentionally omitted <==**  **The Coffee Cow**  We’ve seen how to build lists w ... [truncated] (1 shared statement(s))
- [[javascriptallonge-whenever]] - shared statements: Whenever shares source evidence from Copy on Write: Composing and Decomposing Data  138 **const** childList = rest(parentList); set(2, "three", parentList); set(0, "two", childList); parentList _//=> {"first":1,"rest" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Copy on Write: Composing and Decomposing Data  136  Whereas if you have a linked list, and you take it’s “rest,” your “child” list shares its nodes with the “parent” list. And ther ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
