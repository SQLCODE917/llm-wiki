---
title: Recursion
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# Recursion

Recursion is a programming technique where a function calls itself to solve problems that exhibit self-similar structures, such as lists and trees. This approach aligns naturally with the recursive definition of data structures, enabling elegant solutions for operations like mapping, folding, and enumeration. Tail-call optimization allows recursive functions to execute efficiently without growing the call stack, making them suitable for processing large datasets.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Recursive functions can be defined using self-similar data structures like arrays. | "Our length function is recursive, it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar." | `normalized:L3451` | [Source](../sources/js-allonge.md) |
| Linear recursion is a fundamental approach for working with self-similar data structures like lists. | "Linear recursion is a basic building block of algorithms. Its basic form parallels the way linear data structures like lists are constructed" | `normalized:L3617` | [Source](../sources/js-allonge.md) |
| Recursive functions can be implemented using pattern matching on array destructuring. | "const flatten = ([first, ...rest]) => { if (first === undefined) { return []; } else if (!Array.isArray(first)) { return [first, ...flatten(rest)]; } else { return [...flatten(first), ...flatten(rest)]; } }" | `normalized:L3510` | [Source](../sources/js-allonge.md) |
| Folding is a generalization of mapping that can be used to implement various operations including mapping and length calculation. | "Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code" | `normalized:L3593` | [Source](../sources/js-allonge.md) |
| Tail-call optimization allows recursive functions to avoid consuming memory proportional to input size. | "In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error" | `normalized:L3677` | [Source](../sources/js-allonge.md) |
| A tail-call occurs when a function's last action is to invoke another function and return its result. | "A "tail-call" occurs when a function's last act is to invoke another function, and then return whatever the other function returns" | `normalized:L3731` | [Source](../sources/js-allonge.md) |
| Converting recursive calls to tail-calls enables tail-call optimization for better memory usage. | "The obvious solution is push the 1 + work into the call to length. Here's our first cut: const lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === undefined ? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded)" | `normalized:L3775` | [Source](../sources/js-allonge.md) |
| Tail recursion can be used to implement functions like factorial without causing stack overflow issues. | "const factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work);" | `normalized:L4006` | [Source](../sources/js-allonge.md) |
| Default arguments in functions allow for cleaner tail-recursive implementations by providing initial values automatically. | "By writing our parameter list as (n, work = 1) =>, we're stating that if a second parameter is not provided, work is to be bound to 1." | `normalized:L4014` | [Source](../sources/js-allonge.md) |
| Tail-call optimization allows recursive functions to execute without growing the call stack, improving performance. | "Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls." | `normalized:L3920` | [Source](../sources/js-allonge.md) |
| Recursive enumeration of nested structures is easier to express with generators than with explicit iterative stacks. | "One of those cases is when we have to recursively enumerate something. For example, iterating over a tree." | `normalized:L7402` | [Source](../sources/js-allonge.md) |

## Why it matters

Recursion provides a natural way to work with self-similar data structures like lists and trees, aligning with their inherent recursive definitions. It enables powerful abstractions such as folding and mapping, and when combined with tail-call optimization, allows efficient processing of large datasets without stack overflow issues. Understanding recursion is essential for functional programming and for writing clean, expressive code that mirrors the structure of the data being processed.

## Source pages

- [Source](../sources/js-allonge.md)