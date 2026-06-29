---
page_id: javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-83116d81
page_kind: source
summary: Composing and Decomposing Data / Garbage, Garbage Everywhere: 58 source-backed entries and 12 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-83116d81@507ba40ffd7dd6d863398355da86b4d4
---

# Composing and Decomposing Data / Garbage, Garbage Everywhere

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-6f7d7870]] - broader source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-some-history-1c77955f]] - narrower source section: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history
- [[javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-so-why-arrays-ecae5c27]] - narrower source section: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays
- [[javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-summary-71292497]] - narrower source section: Composing and Decomposing Data / Garbage, Garbage Everywhere / summary

## Statements

- We have now seen how to use Tail Calls to execute mapWith in constant space: _(javascriptallonge.pdf (source-range-7239e085-01017))_
- But when we try it on very large arrays, we discover that it is still very slow. Much slower than the built-in .map method for arrays. The right tool to discover why it's still slow is a memory profiler, but a simple inspection of the program will reveal the following: _(javascriptallonge.pdf (source-range-7239e085-01019))_
- Every time we call mapWith , we're calling [...prepend, fn(first)] . To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith . _(javascriptallonge.pdf (source-range-7239e085-01020))_
- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-7239e085-01022))_
- We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another. _(javascriptallonge.pdf (source-range-7239e085-01023))_
- Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-7239e085-01024))_
- 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript's built-in arrays work. _(javascriptallonge.pdf (source-range-7239e085-01026))_
- Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-7239e085-01022))_
- Key Point : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-7239e085-01024))_
- 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-7239e085-01026))_

## Statements by subsection

### Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word. _(javascriptallonge.pdf (source-range-7239e085-01031))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-7239e085-01032))_
- Lists were represented as linked lists of cons cells, with each cell's head pointing to an element and the tail pointing to another cons cell. _(javascriptallonge.pdf (source-range-7239e085-01033))_
- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today's standards. Although the 704 used core memory, it still used vacuum tubes for its logic. Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-7239e085-01034))_
- Here's the scheme in JavaScript, using two-element arrays to represent cons cells: _(javascriptallonge.pdf (source-range-7239e085-01035))_
- This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it: _(javascriptallonge.pdf (source-range-7239e085-01042))_
- car is very fast, it simply extracts the first element of the cons cell. _(javascriptallonge.pdf (source-range-7239e085-01044))_
- Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-7239e085-01047))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-7239e085-01048))_
- That being said, it is easy to understand and helps us grasp how literals and destructuring works, and how recursive algorithms ought to mirror the self-similarity of the data structures they manipulate. And so it is today that languages like JavaScript have arrays that are slow to split into the equivalent of a car / cdr pair, but instructional examples of recursive programs still have echoes of their Lisp origins. _(javascriptallonge.pdf (source-range-7239e085-01050))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-7239e085-01031))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-7239e085-01032))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-7239e085-01034))_
- This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . _(javascriptallonge.pdf (source-range-7239e085-01042))_
- In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-7239e085-01047))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-7239e085-01048))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

- Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it. _(javascriptallonge.pdf (source-range-7239e085-01055))_
- We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list. _(javascriptallonge.pdf (source-range-7239e085-01056))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-7239e085-01057))_
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. _(javascriptallonge.pdf (source-range-7239e085-01058))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / summary

- Although we showed how to use tail calls to map and fold over arrays with [first, ...rest] , in reality this is not how it ought to be done. But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-7239e085-01060))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-7239e085-01060))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01017))_

> We have now seen how to use Tail Calls to execute mapWith in constant space:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01015))_

> [Figure] (p.126)

### Technical frame 2: Composing and Decomposing Data / Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01019))_

> But when we try it on very large arrays, we discover that it is still very slow. Much slower than the built-in .map method for arrays. The right tool to discover why it's still slow is a memory profiler, but a simple inspection of the program will reveal the following:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01018))_

```
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 3: Composing and Decomposing Data / Garbage, Garbage Everywhere

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01026))_

> 64 It needn't always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. But this is not how JavaScript's built-in arrays work.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01027))_

> [Figure] (p.128)

### Technical frame 4: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01032))_

> Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01031))_

> If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.

### Technical frame 5: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01036))_

```
const cons = (a, d) => [a, d],
car
= ([a, d]) => a,
cdr
= ([a, d]) => d;
```

### Technical frame 6: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01038))_

```
const oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, null)))));
```

### Technical frame 7: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01039))_

```
oneToFive
//=> [1,[2,[3,[4,[5,null]]]]]
```

### Technical frame 8: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01041))_

```
const node5 = [5,null],
node4 = [4, node5],
node3 = [3, node4],
node2 = [2, node3],
node1 = [1, node2];
const oneToFive = node1;
```

### Technical frame 9: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01044))_

> car is very fast, it simply extracts the first element of the cons cell.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01043))_

```
car(oneToFive)
//=> 1
```

### Technical frame 10: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01047))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01046))_

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

### Technical frame 11: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01056))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01055))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

### Technical frame 12: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01057))_

> Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation).

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01056))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.
