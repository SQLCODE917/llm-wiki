---
page_id: javascriptallonge-element
page_kind: concept
summary: Element: 21 statement(s) and 17 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-element@7296ace86963b40b681616dbcbbfcfd1
---

# Element

What [[javascriptallonge]] covers about element:

## Statements

### element references

- Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: _(javascriptallonge.pdf (source-range-8eb13d6b-00834))_

### Self-Similarity

- Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list , [e, ...list] is a list. We can test this manually by building up a list: _(javascriptallonge.pdf (source-range-8eb13d6b-00890))_

### linear recursion

- The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our solutions are a little simpler in that we don't really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. _(javascriptallonge.pdf (source-range-8eb13d6b-00915))_

- Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions. _(javascriptallonge.pdf (source-range-8eb13d6b-00923))_

### Garbage, Garbage Everywhere

- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-8eb13d6b-01022))_

- Here's the scheme in JavaScript, using two-element arrays to represent cons cells: _(javascriptallonge.pdf (source-range-8eb13d6b-01034))_

- Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-8eb13d6b-01046))_

### so why arrays

- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-8eb13d6b-01056))_

### Copy on Write

- This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection. _(javascriptallonge.pdf (source-range-8eb13d6b-01231))_

### iterating

- Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 . _(javascriptallonge.pdf (source-range-8eb13d6b-01287))_

### Iteration and Iterables

- All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and JavaScript has a standard way to iterate over the contents of collections. _(javascriptallonge.pdf (source-range-8eb13d6b-01529))_

### iterator objects

- Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object with a .next() method. _(javascriptallonge.pdf (source-range-8eb13d6b-01547))_

### iterables

- One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly. _(javascriptallonge.pdf (source-range-8eb13d6b-01569))_

### operations on ordered collections

- For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest] : _(javascriptallonge.pdf (source-range-8eb13d6b-01606))_

### recursive iterators

- For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable. _(javascriptallonge.pdf (source-range-8eb13d6b-01637))_

### state machines

- The first element of the fibonacci sequence is zero. _(javascriptallonge.pdf (source-range-8eb13d6b-01646))_

- The second element of the fibonacci sequence is one. _(javascriptallonge.pdf (source-range-8eb13d6b-01647))_

- Every subsequent element of the fibonacci sequence is the sum of the previous two elements. _(javascriptallonge.pdf (source-range-8eb13d6b-01648))_

### yielding iterables

- Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-8eb13d6b-01733))_

### lazy collection operations

- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. _(javascriptallonge.pdf (source-range-8eb13d6b-01791))_


## Technical atoms

### Technical frame 1: element references

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00836))_

> As we can see, JavaScript Arrays are zero-based 56 .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00835))_

```
const oneTwoThree = ["one", "two", "three"]; oneTwoThree[0] //=> 'one' oneTwoThree[1] //=> 'two' oneTwoThree[2] //=> 'three'
```

### Technical frame 2: Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00892))_

> Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00891))_

```
[] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"]
```

### Technical frame 3: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01041))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01035))_

```
const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
```

### Technical frame 4: Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01046))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01045))_

```
cdr(oneToFive) //=> [2,[3,[4,[5,null]]]]
```

### Technical frame 5: so why arrays

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01056))_

> Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation).

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01055))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.

### Technical frame 6: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01231))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01227))_

> The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array.

### Technical frame 7: Copy on Write

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01231))_

> This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunch of bookkeeping to track references? We'll end up reinventing reference counting and garbage collection.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01228))_

> Whereas if you have a linked list, and you take it's 'rest,' your 'child' list shares its nodes with the 'parent' list.

### Technical frame 8: iterating

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01287))_

> Once again, we're mixing the code for iterating over an array with the code for calculating a sum. And worst of all, we're getting really low-level with details like knowing that the elements of an array are indexed with consecutive integers that begin with 0 .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01286))_

```
const arraySum = (array) => { let sum = 0; for ( let i = 0; i < array.length; ++i) { sum += array[i]; } return sum } arraySum([1, 4, 9, 16, 25]) //=> 55
```

### Technical frame 9: iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01569))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01565))_

```
['some squares', ...someSquares] //=> ["some squares", 1, 4, 9, 16, 25]
```

### Technical frame 10: iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01569))_

> One caveat of spreading iterables: JavaScript creates an array out of the elements of the iterable. That might be very wasteful for extremely large collections. For example, if we spread a large collection just to find an element in the collection, it might have been wiser to iterate over the element using its iterator directly.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01567))_

```
const firstAndSecondElement = (first, second) => ({first, second}) firstAndSecondElement(...stack) //=> {"first":5,"second":10}
```

### Technical frame 11: operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01608))_

> like our other operations, rest preserves the ordered collection semantics of its argument.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01607))_

```
const first = (iterable) => iterable[Symbol.iterator]().next().value; const rest = (iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator](); iterator.next(); return iterator; } });
```

### Technical frame 12: recursive iterators

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01637))_

> For example, iterating over a tree. Given an array that might contain arrays, let's say we want to generate all the 'leaf' elements, i.e. elements that are not, themselves, iterable.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01638))_

```
// Generation const isIterable = (something) => !!something[Symbol.iterator]; const generate = (iterable) => { for ( let element of iterable) { if (isIterable(element)) { generate(element) } else { console.log(element) } } } generate([1, [2, [3, 4], 5]]) //=> 1 2 3 4 5
```

### Technical frame 13: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01745))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01738))_

```
function * append (...iterables) { for ( const iterable of iterables) { for ( const element of iterable) { yield element; } } } const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\ "]); for ( const word of lyrics) { console.log(word); } //=> a b c one two three do re me
```

### Technical frame 14: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01745))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01741))_

```
function * append (...iterables) { for ( const iterable of iterables) { yield * iterable; } } const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\ "]); for ( const word of lyrics) { console.log(word); }
```

### Technical frame 15: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01745))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01742))_

```
//=> a b c one two do re
```

### Technical frame 16: yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01745))_

> yield* is handy when writing generator functions that operate on or create iterables.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01743))_

```
const isIterable = (something) => !!something[Symbol.iterator]; function * tree (iterable) { for ( const e of iterable) { if (isIterable(e)) { yield * tree(e); } else { yield e; } } }; for ( const i of console.log(i); } //=> 1 2 3 4 5
```

### Technical frame 17: lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01790))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01789))_

```
Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first()
```


## Related pages

- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from element references: Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:; Array shares technical record from element references: const oneTwoThree = ["one", "two", "three"]; oneTwoThree[0] //=> 'one' oneTwoThree[1] //=> 'two' oneTwoThree[2] //=> 'three' (6 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Self-Similarity: Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e ... [truncated]; List shares technical record from Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (3 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Garbage, Garbage Everywhere: Here's the scheme in JavaScript, using two-element arrays to represent cons cells:; Javascript shares technical record from Garbage, Garbage Everywhere: const cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d; (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-copy-write]] - shared statements and technical atoms: Copy on Write shares source evidence from Copy on Write: This is remarkably unsafe. If we know that a list doesn't share any elements with another list, we can safely modify it. But how do we keep track of that? Add a bunc ... [truncated]; Copy on Write shares technical record from Copy on Write: The consequence of this is that if you have an array, and you take it's 'rest,' your 'child' array is a copy of the elements of the parent array. (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from operations on ordered collections: For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that itera ... [truncated]; Return shares technical record from operations on ordered collections: const first = (iterable) => iterable[Symbol.iterator]().next().value; const rest = (iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator] ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-copy]] - shared statements and technical atoms: Copy shares source evidence from Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated]; Copy shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-reference]] - shared statements and technical atoms: Reference shares source evidence from so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated]; Reference shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Garbage, Garbage Everywhere: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (4 shared atom(s))
- [[javascriptallonge-literal]] - shared technical atoms: Literal shares technical record from Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (1 shared atom(s))
- [[javascriptallonge-note]] - shared technical atoms: Note shares technical record from iterables: ['some squares', ...someSquares] //=> ["some squares", 1, 4, 9, 16, 25] (1 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (1 shared atom(s))
- [[javascriptallonge-collection]] - shared statements: Collection shares source evidence from Iteration and Iterables: All of these actions involve going through the contents one by one. Acting on the elements of a collection one at a time is called iterating over the contents , and ... [truncated] (2 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (2 shared statement(s))
- [[javascriptallonge-directly]] - shared statements: Directly shares source evidence from linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from iterator objects: Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object w ... [truncated] (1 shared statement(s))
- [[javascriptallonge-important]] - shared statements: Important shares source evidence from linear recursion: Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and com ... [truncated] (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from iterator objects: Fortunately, an iterator object is almost as simple as an iterator function. Instead of having a function that you call to get the next element, you have an object w ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-second]] - shared statements: Second shares source evidence from state machines: The second element of the fibonacci sequence is one. (1 shared statement(s))

## Source

- [[javascriptallonge]]
