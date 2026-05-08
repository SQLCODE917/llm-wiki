---
title: Arrays
type: concept
tags: []
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
---

# Arrays

Arrays in JavaScript are ordered collections that store references to objects rather than copies, and their literal syntax creates distinct instances even with identical content. They support destructuring techniques for flexible value extraction and assignment, though certain operations like spreading during recursion can lead to performance concerns.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| Array literals create new, distinct arrays even when containing identical elements. | "Array literals are expressions, and arrays are _reference types_ . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:" | normalized:L2397-L2397 | [Source](../sources/js-allonge.md) |
| Array elements are stored as references to the original objects rather than copies. | "a[0] === x" | normalized:L2425-L2425 | [Source](../sources/js-allonge.md) |
| Using destructuring with default values allows providing fallbacks for array elements during assignment. | "**const** [first, second = "two"] = ["one"];" | normalized:L2985-L2985 | [Source](../sources/js-allonge.md) |
| Creating new arrays via spread operations during recursion leads to performance issues due to copying elements. | "Every time we call mapWith, we're calling [...prepend, fn(first)]. To do that, we take the array in prepend and push fn(first) onto the end, creating a new array that will be passed to the next..." | normalized:L3017-L3017 | [Source](../sources/js-allonge.md) |
| The author can be contacted via Twitter at @raganwald or by email at reg@braythwayt.com. | "Twitter: @raganwald[224] Email: reg@braythwayt.com[225]" | normalized:L6483-L6483 | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding how arrays work in JavaScript is crucial for effective programming because array literals always produce new instances, which affects equality checks and object identity. Since elements are stored as references, modifications to referenced objects will be visible across all references. Additionally, knowing about destructuring with defaults helps in writing more robust code that handles missing or undefined values gracefully. Performance considerations around spreading arrays during recursive operations also inform optimization strategies in algorithms involving arrays.

## Source pages

- [Source](../sources/js-allonge.md)
```