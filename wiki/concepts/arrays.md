---
title: Arrays
type: concept
tags: [javascript, data-structures, destructuring, arrays]
status: draft
last_updated: 2024-07-15
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2397-L2397
  - js-allonge:normalized:L2425-L2427
  - js-allonge:normalized:L2445-L2449
  - js-allonge:normalized:L2465-L2469
  - js-allonge:normalized:L2473-L2477
  - js-allonge:normalized:L2513-L2513
  - js-allonge:normalized:L2517-L2527
  - js-allonge:normalized:L2539-L2541
  - js-allonge:normalized:L2569-L2571
  - js-allonge:normalized:L2589-L2593
  - js-allonge:normalized:L2591-L2593
  - js-allonge:normalized:L2593-L2593
  - js-allonge:normalized:L2595-L2597
  - js-allonge:normalized:L2607-L2607
  - js-allonge:normalized:L2611-L2611
  - js-allonge:normalized:L3017-L3018
  - js-allonge:normalized:L3027-L3028
  - js-allonge:normalized:L5887-L5887
  - js-allonge:normalized:L5899-L5899
---

# Arrays

## Summary

Arrays in JavaScript are reference types created through array literals. They store references to elements rather than the elements themselves. Destructuring allows extracting values from arrays, including nested patterns and gathering remaining elements with the spread operator.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Array literals produce reference types, generating a new distinct array instance upon each evaluation regardless of identical contents. | "Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:" | `normalized:L2397-L2397` | [Source](../sources/js-allonge.md) |
| Arrays maintain references to their contained elements, allowing modification of referenced objects to affect the array's contents. | "a[0] === x _//=> true, arrays store references to the things you put in them._" | `normalized:L2425-L2427` | [Source](../sources/js-allonge.md) |
| JavaScript enables reverse assignment by placing the destructuring template on the left-hand side of an assignment expression. | "In JavaScript, we can actually _reverse_ the statement and place the template on the left and a value on the right: **const** unwrap = (wrapped) => { **const** [something] = wrapped; **return**..." | `normalized:L2445-L2449` | [Source](../sources/js-allonge.md) |
| Destructuring supports nested patterns, enabling extraction of elements from deeply structured arrays. | "Destructuring can nest: **const** description = (nameAndOccupation) => { **const** [[first, last], occupation] = nameAndOccupation; **return** ` **${** first **}** is a **${** occupation **}** `;..." | `normalized:L2465-L2469` | [Source](../sources/js-allonge.md) |
| The gathering pattern with the spread operator facilitates extraction of the head and collection of the remainder of an array's elements. | "Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array: **const** [car, ...cdr] = [1, 2, 3, 4,..." | `normalized:L2473-L2477` | [Source](../sources/js-allonge.md) |
| The spread operator allows insertion of array elements within another array, distinguishing this operation from destructuring. | "It works! We can use ... to place the elements of an array inside another array. We say that using ... to destructure is gathering, and using it in a literal to insert elements is called "spreading."" | `normalized:L2513-L2513` | [Source](../sources/js-allonge.md) |
| Unlike languages with pattern matching, JavaScript's destructuring does not fail when attempting to match an empty array against a pattern requiring elements. | "Some other languages have something called _pattern matching_ , where you can write something like a destructuring assignment, and the language decides whether the "patterns" matches at all. If it..." | `normalized:L2517-L2527` | [Source](../sources/js-allonge.md) |
| Destructuring can emulate multiple return values from functions, providing a clean syntax for unpacking results. | "## **destructuring and return values** Some languages support multiple return values: A function can return several things at once, like a value and an error code. This can easily be emulated in..." | `normalized:L2539-L2541` | [Source](../sources/js-allonge.md) |
| Gathering works with function parameters, allowing flexible handling of variable argument counts. | "**const** numbers = (...nums) => nums; numbers(1, 2, 3, 4, 5) _//=> [1,2,3,4,5]_ **const** headAndTail = (head, ...tail) => [head, tail]; headAndTail(1, 2, 3, 4, 5) _//=> [1,[2,3,4,5]]_ Gathering..." | `normalized:L2569-L2571` | [Source](../sources/js-allonge.md) |
| Lists can be defined recursively using two rules: being empty or consisting of an element concatenated with another list. | "But we can also define a list by describing a rule for building lists. One of the simplest, and longeststanding in computer science, is to say that a list is: 1. Empty, or; 2. Consists of an..." | `normalized:L2589-L2593` | [Source](../sources/js-allonge.md) |
| Array literals and the spread operator mirror the recursive definition of lists, enabling both construction and decomposition. | "Let's convert our rules to array literals. The first rule is simple: [] is a list. How about the second rule? We can express that using a spread. Given an element e and a list list, [e, ...list]..." | `normalized:L2595-L2597` | [Source](../sources/js-allonge.md) |
| A list is either empty or consists of an element concatenated with another list. | "1. Empty, or; 2. Consists of an element concatenated with a list ." | `normalized:L2591-L2593` | [Source](../sources/js-allonge.md) |
| The second rule of list definition states that a list consists of an element concatenated with another list. | "2. Consists of an element concatenated with a list ." | `normalized:L2593-L2593` | [Source](../sources/js-allonge.md) |
| Destructuring with the spread operator can extract the first element and collect the rest, even from empty arrays. | "**const** [first, ...rest] = []; first _//=> undefined_ rest _//=> []:_ **const** [first, ...rest] = ["foo"]; first _//=> "foo"_ rest _//=> []_ **const** [first, ...rest] = ["foo", "bar"]; first..." | `normalized:L2607-L2607` | [Source](../sources/js-allonge.md) |
| An empty array is identified by checking if the first element is undefined after destructuring. | "**const** isEmpty = ([first, ...rest]) => first === **undefined** ;" | `normalized:L2611-L2611` | [Source](../sources/js-allonge.md) |
| Recursive mapping functions create new arrays during each step, leading to performance issues due to repeated element copying. | "Every time we call mapWith, we're calling [...prepend, fn(first)]. To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next..." | `normalized:L3017-L3018` | [Source](../sources/js-allonge.md) |
| Repeated array creation and copying during recursion causes significant overhead, making such approaches inefficient for large datasets. | "We may not be creating 3,000 stack frames, but we are creating three thousand new arrays and copying elements into each and every one of them. Although the maximum amount of memory does not grow,..." | `normalized:L3027-L3028` | [Source](../sources/js-allonge.md) |
| A game board state can be represented as an array containing character elements. | "[ 'o', 'x', ' ', ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ]" | `normalized:L5887-L5887` | [Source](../sources/js-allonge.md) |
| A specific game board configuration is encoded as an array of characters. | "[ 'o', 'x', ' ', 'x', ' ', ' ', 'o', ' ', ' ' ]" | `normalized:L5899-L5899` | [Source](../sources/js-allonge.md) |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
