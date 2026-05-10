---
title: Arrays
type: concept
tags: [data structures, javascript]
status: draft
last_updated: 2026-05-09
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2397-L2397
  - js-allonge:normalized:L2407-L2407
  - js-allonge:normalized:L2413-L2413
  - js-allonge:normalized:L2425-L2427
  - js-allonge:normalized:L2429-L2431
  - js-allonge:normalized:L2475-L2477
  - js-allonge:normalized:L2511-L2511
  - js-allonge:normalized:L2517-L2527
  - js-allonge:normalized:L2539-L2539
  - js-allonge:normalized:L2569-L2569
  - js-allonge:normalized:L2591-L2593
  - js-allonge:normalized:L2595-L2595
  - js-allonge:normalized:L2599-L2599
---

# Arrays

## Summary

Arrays in JavaScript are ordered collections of values that can hold elements of any type. They are reference types, meaning each array literal creates a new object, and elements are accessed via zero-based indices. Arrays support destructuring and spreading, enabling flexible manipulation and decomposition of data.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Array literals in JavaScript produce new, distinct objects each time they are evaluated, even when containing identical elements. | "Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:" | `normalized:L2397-L2397` | [Source](../sources/js-allonge.md) |
| Array elements are accessed using bracket notation with zero-based integer indices, and the elements themselves are stored as references to their original values. | "a[0] === x _//=> true, arrays store references to the things you put in them._" | `normalized:L2425-L2427` | [Source](../sources/js-allonge.md) |
| Array elements are accessed using bracket notation with zero-based integer indices, and the elements themselves are stored as references to their original values. | "Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:" | `normalized:L2407-L2407` | [Source](../sources/js-allonge.md) |
| Array elements are accessed using bracket notation with zero-based integer indices, and the elements themselves are stored as references to their original values. | "As we can see, JavaScript Arrays are zero-based[56] ." | `normalized:L2413-L2413` | [Source](../sources/js-allonge.md) |
| JavaScript arrays support destructuring and spreading, which allow for extracting elements and combining arrays in flexible ways, such as using rest patterns to capture remaining elements. | "## **destructuring arrays** There is another way to extract elements from arrays: _Destructuring_ , a feature going back to Common Lisp, if not before. We saw how to construct an array literal..." | `normalized:L2429-L2431` | [Source](../sources/js-allonge.md) |
| JavaScript arrays support destructuring and spreading, which allow for extracting elements and combining arrays in flexible ways, such as using rest patterns to capture remaining elements. | "**const** [car, ...cdr] = [1, 2, 3, 4, 5]; car _//=> 1_ cdr _//=> [2, 3, 4, 5]_" | `normalized:L2475-L2477` | [Source](../sources/js-allonge.md) |
| JavaScript arrays support destructuring and spreading, which allow for extracting elements and combining arrays in flexible ways, such as using rest patterns to capture remaining elements. | "**const** oneTwoThree = ["one", "two", "three"]; ["zero", ...oneTwoThree] _//=> ["zero","one","two","three"]_" | `normalized:L2511-L2511` | [Source](../sources/js-allonge.md) |
| JavaScript arrays support destructuring and spreading, which allow for extracting elements and combining arrays in flexible ways, such as using rest patterns to capture remaining elements. | "Some other languages have something called _pattern matching_ , where you can write something like a destructuring assignment, and the language decides whether the "patterns" matches at all. If it..." | `normalized:L2517-L2527` | [Source](../sources/js-allonge.md) |
| JavaScript arrays support destructuring and spreading, which allow for extracting elements and combining arrays in flexible ways, such as using rest patterns to capture remaining elements. | "## **destructuring and return values**" | `normalized:L2539-L2539` | [Source](../sources/js-allonge.md) |
| JavaScript arrays support destructuring and spreading, which allow for extracting elements and combining arrays in flexible ways, such as using rest patterns to capture remaining elements. | "**const** numbers = (...nums) => nums; numbers(1, 2, 3, 4, 5) _//=> [1,2,3,4,5]_ **const** headAndTail = (head, ...tail) => [head, tail]; headAndTail(1, 2, 3, 4, 5) _//=> [1,[2,3,4,5]]_" | `normalized:L2569-L2569` | [Source](../sources/js-allonge.md) |
| JavaScript arrays support destructuring and spreading, which allow for extracting elements and combining arrays in flexible ways, such as using rest patterns to capture remaining elements. | "1. Empty, or; 2. Consists of an element concatenated with a list ." | `normalized:L2591-L2593` | [Source](../sources/js-allonge.md) |
| JavaScript arrays support destructuring and spreading, which allow for extracting elements and combining arrays in flexible ways, such as using rest patterns to capture remaining elements. | "Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list, [e, ...list]..." | `normalized:L2595-L2595` | [Source](../sources/js-allonge.md) |
| JavaScript arrays support destructuring and spreading, which allow for extracting elements and combining arrays in flexible ways, such as using rest patterns to capture remaining elements. | "Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:" | `normalized:L2599-L2599` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
