---
page_id: javascriptallonge-section-garbage-garbage-everywhere-8f6e0d08
page_kind: source
summary: Garbage, Garbage Everywhere: 61 source-backed entries and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-garbage-garbage-everywhere-8f6e0d08@7032bf17f5a77032fe33a084308d480c
---

# Garbage, Garbage Everywhere

From [[javascriptallonge]].

## Statements

- We have now seen how to use Tail Calls to execute mapWith in constant space: _(javascriptallonge.pdf (source-range-83ecb080-01507))_
- But when we try it on very large arrays, we discover that it is _still_ very slow. _(javascriptallonge.pdf (source-range-83ecb080-01512))_
- The right tool to discover why it’s still slow is a memory profiler, but a simple inspection of the program will reveal the following: _(javascriptallonge.pdf (source-range-83ecb080-01512))_
- To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith. _(javascriptallonge.pdf (source-range-83ecb080-01513))_
- The array we had in prepend is no longer used. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another. _(javascriptallonge.pdf (source-range-83ecb080-01518))_
- We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. _(javascriptallonge.pdf (source-range-83ecb080-01518))_
- **Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-83ecb080-01519))_
- **Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-83ecb080-01519))_
- > 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-83ecb080-01521))_
- But this is not how JavaScript’s built-in arrays work. _(javascriptallonge.pdf (source-range-83ecb080-01521))_
- > 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-83ecb080-01521))_
- (The very first FORTRAN implementation was also written for the 704). _(javascriptallonge.pdf (source-range-83ecb080-01527))_
- The CPU’s instruction set featured two important macros: CAR would fetch 15 bits representing the Contents of the Address part of the Register, while CDR would fetch the Contents of the Decrement part of the Register. _(javascriptallonge.pdf (source-range-83ecb080-01528))_
- The 704 had a 36-bit word, meaning that it was very fast to store and retrieve 36-bit values. _(javascriptallonge.pdf (source-range-83ecb080-01528))_
- > 66Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-01530))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-83ecb080-01533))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-83ecb080-01533))_
- The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Lisp’s basic data type is often said to be the list, but in actuality it was the “cons cell,” the term used to describe two 15-bit values stored in one word. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- Lists were represented as linked lists of cons cells, with each cell’s head pointing to an element and the tail pointing to another cons cell. _(javascriptallonge.pdf (source-range-83ecb080-01535))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today’s standards. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Although the 704 used core memory, it still used vacuum tubes for its logic. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance. _(javascriptallonge.pdf (source-range-83ecb080-01536))_
- Here’s the scheme in JavaScript, using two-element arrays to represent cons cells: _(javascriptallonge.pdf (source-range-83ecb080-01537))_
- This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. _(javascriptallonge.pdf (source-range-83ecb080-01548))_
- This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. _(javascriptallonge.pdf (source-range-83ecb080-01548))_
- car is very fast, it simply extracts the first element of the cons cell. _(javascriptallonge.pdf (source-range-83ecb080-01551))_
- In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- There’s no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- In Lisp, it’s blazingly fast because it happens in hardware. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. _(javascriptallonge.pdf (source-range-83ecb080-01555))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-83ecb080-01556))_
- So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible. _(javascriptallonge.pdf (source-range-83ecb080-01556))_
- That being said, it is easy to understand and helps us grasp how literals and destructuring works, and how recursive algorithms ought to mirror the self-similarity of the data structures they manipulate. _(javascriptallonge.pdf (source-range-83ecb080-01558))_
- And so it is today that languages like JavaScript have arrays that are slow to split into the equivalent of a car/cdr pair, but instructional examples of recursive programs still have echoes of their Lisp origins. _(javascriptallonge.pdf (source-range-83ecb080-01558))_
- We’ll look at linked lists again when we look at Plain Old JavaScript Objects. _(javascriptallonge.pdf (source-range-83ecb080-01559))_
- But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. _(javascriptallonge.pdf (source-range-83ecb080-01565))_
- Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. _(javascriptallonge.pdf (source-range-83ecb080-01565))_
- If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list. _(javascriptallonge.pdf (source-range-83ecb080-01566))_
- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-83ecb080-01567))_
- For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases. _(javascriptallonge.pdf (source-range-83ecb080-01568))_
- Although we showed how to use tail calls to map and fold over arrays with [first, ...rest], in reality this is not how it ought to be done. _(javascriptallonge.pdf (source-range-83ecb080-01570))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-01570))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-01570))_

## Technical atoms

> Context: We have now seen how to use Tail Calls to execute mapWith in constant space:
_(context: javascriptallonge.pdf (source-range-83ecb080-01507))_

> **const** mapWith = (fn, [first, ...rest], prepend = []) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01508))_

> mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01511))_

> Context: > 66Lisp is still very much alive, and one of the most interesting and exciting programming languages in use today is Clojure, a Lisp dialect that runs on the JVM, along with its sibling ClojureScript, Clojure that transpiles to JavaScript. 67https://en.wikipedia.org/wiki/IBM_704
_(context: javascriptallonge.pdf (source-range-83ecb080-01530))_

> If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.
_(source: javascriptallonge.pdf (source-range-83ecb080-01533))_

> Context: Here’s the scheme in JavaScript, using two-element arrays to represent cons cells:
_(context: javascriptallonge.pdf (source-range-83ecb080-01537))_

> **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;
_(source: javascriptallonge.pdf (source-range-83ecb080-01538))_

> Context: We can make a list by calling cons repeatedly, and terminating it with null:
_(context: javascriptallonge.pdf (source-range-83ecb080-01539))_

> **const** oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, **null** )))));
_(source: javascriptallonge.pdf (source-range-83ecb080-01540))_

> Context: Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like:
_(context: javascriptallonge.pdf (source-range-83ecb080-01543))_

> **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2];
_(source: javascriptallonge.pdf (source-range-83ecb080-01546))_

> **const** oneToFive = node1;
_(source: javascriptallonge.pdf (source-range-83ecb080-01547))_

> Context: If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?
_(context: javascriptallonge.pdf (source-range-83ecb080-01564))_

> And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.
_(source: javascriptallonge.pdf (source-range-83ecb080-01565))_

> Context: Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.
_(context: javascriptallonge.pdf (source-range-83ecb080-01565))_

> We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements.
_(source: javascriptallonge.pdf (source-range-83ecb080-01566))_
