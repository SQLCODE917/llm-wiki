---
page_id: javascriptallonge-garbage-everywhere
page_kind: concept
summary: Garbage, Garbage Everywhere: 41 statement(s) and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-garbage-everywhere@1b5bd5444e1b0f2fd976a3f78c94fbbc
---

# Garbage, Garbage Everywhere

What [[javascriptallonge]] covers about garbage, garbage everywhere:

## Statements

- In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. _(javascriptallonge.pdf (source-range-83ecb080-01533))_
- But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-01570))_
- We have now seen how to use Tail Calls to execute mapWith in constant space: _(javascriptallonge.pdf (source-range-83ecb080-01507))_
- But when we try it on very large arrays, we discover that it is _still_ very slow. _(javascriptallonge.pdf (source-range-83ecb080-01512))_
- The right tool to discover why it’s still slow is a memory profiler, but a simple inspection of the program will reveal the following: _(javascriptallonge.pdf (source-range-83ecb080-01512))_
- To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next invocation of mapWith. _(javascriptallonge.pdf (source-range-83ecb080-01513))_
- The array we had in prepend is no longer used. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- Lather, rinse, repeat: Ever time we call mapWith, we’re creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend. _(javascriptallonge.pdf (source-range-83ecb080-01517))_
- Although the maximum amount of memory does not grow, the thrashing as we create short-lived arrays is very bad, and we do a lot of work copying elements from one array to another. _(javascriptallonge.pdf (source-range-83ecb080-01518))_
- We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. _(javascriptallonge.pdf (source-range-83ecb080-01518))_
- **Key Point** : Our [first, ...rest] approach to recursion is slow because that it creates a lot of temporary arrays, and it spends an enormous amount of time copying elements into arrays that end up being discarded. _(javascriptallonge.pdf (source-range-83ecb080-01519))_
- > 64It needn’t always be so: Programmers have developed specialized data structures that make operations like this cheap, often by arranging for structures to share common elements by default, and only making copies when changes are made. _(javascriptallonge.pdf (source-range-83ecb080-01521))_
- But this is not how JavaScript’s built-in arrays work. _(javascriptallonge.pdf (source-range-83ecb080-01521))_

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


## Source

- [[javascriptallonge]]
