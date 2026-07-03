---
page_id: javascriptallonge-element
page_kind: concept
page_family: broad-topic
summary: Element: 21 statement(s) and 18 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-element@12965a12028dd8a35d2b644c174f433c
---

# Element

What [[javascriptallonge]] covers about element:


## Related pages

### Shared technical atoms

- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Composing and Decomposing Data / Self-Similarity: Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e ... [truncated]; List shares technical record from Composing and Decomposing Data / Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (3 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: Here's the scheme in JavaScript, using two-element arrays to represent cons cells:; Javascript shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d; (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (3 shared atom(s))
- [[javascriptallonge-copy-write]] - shared statements and technical atoms: Copy on Write shares source evidence from Yes. Consider this variation: / Copy on Write: This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunc ... [truncated]; Copy on Write shares technical record from Yes. Consider this variation: / Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from Like this: / operations on ordered collections: For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that itera ... [truncated]; Return shares technical record from Like this: / operations on ordered collections: const first = (iterable) => iterable[Symbol.iterator]().next().value; const rest = (iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator] ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / element references: Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:; Array shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / element references: const oneTwoThree = ["one", "two", "three"]; oneTwoThree[0] //=> 'one' oneTwoThree[1] //=> 'two' oneTwoThree[2] //=> 'three' (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-copy]] - shared statements and technical atoms: Copy shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of ar ... [truncated]; Copy shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Yes. Consider this variation: / Functional Iterators / iterating: Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like ... [truncated]; Functional Iterators shares technical record from Yes. Consider this variation: / Functional Iterators / iterating: const arraySum = (array) => { let sum = 0; for (let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55 (1 shared statement(s), 1 shared atom(s))

### Shared claims

- [[javascriptallonge-collection]] - shared statements: Collection shares source evidence from Served by the Pot: Collections / Iteration and Iterables: All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and ... [truncated] (2 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from Composing and Decomposing Data / Self-Similarity / linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (2 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object w ... [truncated] (1 shared statement(s))
- [[javascriptallonge-important]] - shared statements: Important shares source evidence from Composing and Decomposing Data / Self-Similarity / linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from Served by the Pot: Collections / Iteration and Iterables / iterator objects: Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object w ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-second]] - shared statements: Second shares source evidence from Like this: / Generating Iterables / state machines: The second element of the fibonacci sequence is one. (1 shared statement(s))
## Statements by source section

### Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

- Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: _(javascriptallonge.pdf (source-range-7239e085-00834))_

### Composing and Decomposing Data / Self-Similarity

- Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list , [e, ...list] is a list. We can test this manually by building up a list: _(javascriptallonge.pdf (source-range-7239e085-00890))_

### Composing and Decomposing Data / Self-Similarity / linear recursion

- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-7239e085-00915))_

- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-7239e085-00923))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere

- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-7239e085-01022))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

- Here's the scheme in JavaScript, using two-element arrays to represent cons cells: _(javascriptallonge.pdf (source-range-7239e085-01035))_

- Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-7239e085-01047))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-7239e085-01057))_

### Yes. Consider this variation: / Copy on Write

- This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-7239e085-01232))_

### Yes. Consider this variation: / Functional Iterators / iterating

- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-7239e085-01288))_

### Served by the Pot: Collections / Iteration and Iterables

- All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-7239e085-01530))_

### Served by the Pot: Collections / Iteration and Iterables / iterator objects

- Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-7239e085-01548))_

### Like this: / iterables

- One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-7239e085-01570))_

### Like this: / operations on ordered collections

- For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest] : _(javascriptallonge.pdf (source-range-7239e085-01607))_

### Like this: / Generating Iterables / recursive iterators

- For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-7239e085-01638))_

### Like this: / Generating Iterables / state machines

- The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-7239e085-01647))_

- The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-7239e085-01648))_

- Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-7239e085-01649))_

### We'll keep it simple: / yielding iterables

- Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-7239e085-01734))_

### We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. _(javascriptallonge.pdf (source-range-7239e085-01792))_


## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00837))_

> We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00835))_

<a id="atom-technical-atom-6a9b189a9c39fb74"></a>

```
const oneTwoThree = ["one", "two", "three"];
oneTwoThree[0]
//=> 'one'
oneTwoThree[1]
//=> 'two'
oneTwoThree[2]
//=> 'three'
```

### Technical frame 2: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00892))_

> Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00891))_

<a id="atom-technical-atom-9d3e365c447e4d34"></a>

```
[]
//=> []
["baz", ...[]]
//=> ["baz"]
["bar", ...["baz"]]
//=> ["bar","baz"]
["foo", ...["bar", "baz"]]
//=> ["foo","bar","baz"]
```

### Technical frame 3: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00930))_

> This specific case of linear recursion is called 'mapping,' and it is not necessary to constantly write out the same pattern again and again. Functions can take functions as arguments, so let's 'extract' the thing to do to each element and separate it from the business of taking an array apart, doing the thing, and putting the array back together.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00929))_

<a id="atom-technical-atom-28f08e1ff8b916bb"></a>

```
const truthyAll = ([first, ...rest]) => first === undefined
? []
: [!!first, ...truthyAll(rest)];
truthyAll([null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

### Technical frame 4: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01036))_

<a id="atom-technical-atom-9ce8c8bbddbd25dd"></a>

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Technical frame 5: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01047))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01046))_

<a id="atom-technical-atom-507de994e6577937"></a>

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

### Technical frame 6: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01057))_

> Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation).

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01056))_

<a id="atom-technical-atom-e101f7e8ac776af8"></a>

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.

### Technical frame 7: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01228))_

<a id="atom-technical-atom-bba78c8b3994a437"></a>

> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

### Technical frame 8: Yes. Consider this variation: / Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01232))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01229))_

<a id="atom-technical-atom-107209144ad81087"></a>

> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

### Technical frame 9: Yes. Consider this variation: / Functional Iterators / iterating

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01288))_

> Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01287))_

<a id="atom-technical-atom-61ae9b6a12610202"></a>

```
const arraySum = (array) => {
let sum = 0;
for (let i = 0; i < array.length; ++i) {
sum += array[i];
}
return sum
}
arraySum([1, 4, 9, 16, 25])
//=> 55
```

### Technical frame 10: Like this: / iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01570))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01566))_

<a id="atom-technical-atom-df54c8166a1c51e0"></a>

```
['some squares', ...someSquares]
//=> ["some squares", 1, 4, 9, 16, 25]
```

### Technical frame 11: Like this: / iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01570))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01568))_

<a id="atom-technical-atom-bc5647c8475105f4"></a>

```
const firstAndSecondElement = (first, second) =>
({first, second})
firstAndSecondElement(...stack)
//=> {"first":5,"second":10}
```

### Technical frame 12: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01607))_

> For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest] :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01608))_

<a id="atom-technical-atom-d81d89fc363898dc"></a>

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
const rest = (iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
iterator.next();
return iterator;
}
});
```

### Technical frame 13: Like this: / Generating Iterables / recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01643))_

> If you peel off isIterable and ignore the way that the iteration version uses [Symbol.iterator] and .next , we're left with the fact that the generating version calls itself recursively, and the iteration version maintains an explicit stack. In essence, both the generation and iteration implementations have stacks, but the generation version's stack is implicit , while the iteration version's stack is explicit .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01639))_

<a id="atom-technical-atom-d14c6a73cd2e1891"></a>

```
// Generation
const isIterable = (something) =>
!!something[Symbol.iterator];
const generate = (iterable) => {
for (let element of iterable) {
if (isIterable(element)) {
generate(element)
}
else {
console.log(element)
}
}
}
generate([1, [2, [3, 4], 5]])
//=>
1
2
3
4
5
```

### Technical frame 14: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01735))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01739))_

<a id="atom-technical-atom-06bb02d698b5a335"></a>

```
function * append (...iterables) {
for (const iterable of iterables) {
for (const element of iterable) {
yield element;
}
}
}
const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\
"]);
for (const word of lyrics) {
console.log(word);
}
//=>
a
b
c
one
two
three
do
re
me
```

### Technical frame 15: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01735))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01742))_

<a id="atom-technical-atom-3f887d1daf7a5385"></a>

```
function * append (...iterables) {
for (const iterable of iterables) {
yield * iterable;
}
}
const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\
"]);
for (const word of lyrics) {
console.log(word);
}
```

### Technical frame 16: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01735))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01743))_

<a id="atom-technical-atom-a08bb83e790e552c"></a>

```
//=>
a
b
c
one
two
thre
do
re
```

### Technical frame 17: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01791))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01790))_

<a id="atom-technical-atom-e10108dd925b5dd3"></a>

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
```

### Technical atom 18

<a id="atom-technical-atom-aba6cb6873b1bd9a"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01741))_

> Tucked inside of it is the same three-line idiom for yielding each element of an iterable. There is an abbreviation for this, we can use yield * to yield all the elements of an iterable:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01744))_

```
const isIterable = (something) =>
!!something[Symbol.iterator];
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
yield * tree(e);
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4
console.log(i);
}
//=>
1
2
3
4
5
```


## Source

- [[javascriptallonge]]
