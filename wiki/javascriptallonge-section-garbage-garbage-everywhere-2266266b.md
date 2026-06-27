---
page_id: javascriptallonge-section-garbage-garbage-everywhere-2266266b
page_kind: source
summary: **Garbage, Garbage Everywhere**: 17 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-garbage-garbage-everywhere-2266266b@bd504c7544e8d8c4d4eb2dc03750cabb
---

# **Garbage, Garbage Everywhere**

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

## Technical atoms

> Context: We have now seen how to use Tail Calls to execute mapWith in constant space:
_(context: javascriptallonge.pdf (source-range-83ecb080-01507))_

> **const** mapWith = (fn, [first, ...rest], prepend = []) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01508))_

> mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01511))_
