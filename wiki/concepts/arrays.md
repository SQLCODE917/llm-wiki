---
title: Arrays
type: concept
tags: [javascript, data-structures, destructuring]
status: draft
last_updated: 2026-05-11
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2397-L2397
  - js-allonge:normalized:L2465-L2469
  - js-allonge:normalized:L2475-L2477
  - js-allonge:normalized:L2517-L2531
  - js-allonge:normalized:L2569-L2570
---

# Arrays

## Summary

Arrays in JavaScript are ordered collections of values that can hold elements of any type. They are reference types, meaning each array literal creates a new object, and they support various operations including indexing, destructuring, and functional iteration patterns.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Arrays in JavaScript are reference types, so evaluating an array literal produces a new distinct object each time, even when containing identical elements. | "Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:" | `normalized:L2397-L2397` | [Source](../sources/js-allonge.md) |
| Array destructuring allows for flexible extraction and manipulation of elements, including nested structures and rest patterns, enabling powerful functional programming techniques. | "Destructuring can nest: **const** description = (nameAndOccupation) => { **const** [[first, last], occupation] = nameAndOccupation; **return** ` **${** first **}** is a **${** occupation **}** `;..." | `normalized:L2465-L2469` | [Source](../sources/js-allonge.md) |
| Array destructuring allows for flexible extraction and manipulation of elements, including nested structures and rest patterns, enabling powerful functional programming techniques. | "**const** numbers = (...nums) => nums; numbers(1, 2, 3, 4, 5) _//=> [1,2,3,4,5]_ **const** headAndTail = (head, ...tail) => [head, tail]; headAndTail(1, 2, 3, 4, 5) _//=> [1,[2,3,4,5]]_" | `normalized:L2569-L2570` | [Source](../sources/js-allonge.md) |
| Array destructuring allows for flexible extraction and manipulation of elements, including nested structures and rest patterns, enabling powerful functional programming techniques. | "**const** [car, ...cdr] = [1, 2, 3, 4, 5]; car _//=> 1_ cdr _//=> [2, 3, 4, 5]_" | `normalized:L2475-L2477` | [Source](../sources/js-allonge.md) |
| JavaScript's array destructuring behaves differently from pattern matching in other languages, as it does not fail on mismatch but rather assigns values based on available elements. | "Some other languages have something called _pattern matching_ , where you can write something like a destructuring assignment, and the language decides whether the "patterns" matches at all. If it..." | `normalized:L2517-L2531` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
