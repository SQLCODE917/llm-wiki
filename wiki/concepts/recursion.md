---
title: Recursion
type: concept
tags: [programming, functions, algorithm]
status: draft
last_updated: 2026-05-11
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L2625-L2625
  - js-allonge:normalized:L2629-L2629
  - js-allonge:normalized:L2637-L2637
  - js-allonge:normalized:L2663-L2663
  - js-allonge:normalized:L3005-L3005
---

# Recursion

## Summary

Recursion is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| A recursive approach to solving problems involves decomposing the problem into smaller instances of the same problem, solving those recursively, and combining their results. | "The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our..." | `normalized:L2663-L2663` | [Source](../sources/js-allonge.md) |
| A recursive function typically includes a base case to terminate the recursion and a recursive case that calls the function on a smaller portion of the input. | "Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is..." | `normalized:L2637-L2637` | [Source](../sources/js-allonge.md) |
| A recursive function typically includes a base case to terminate the recursion and a recursive case that calls the function on a smaller portion of the input. | "First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let's start our function with the observation that if an array is empty, the length is 0:" | `normalized:L2625-L2625` | [Source](../sources/js-allonge.md) |
| When implementing a recursive function like calculating the length of a list, the solution often relies on breaking the input into parts (like first and rest) and applying the function to the... | "We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest, the length of our array is going to be length(first) + length(rest)...." | `normalized:L2629-L2629` | [Source](../sources/js-allonge.md) |
| Tail call optimization can be used to make recursive functions more memory-efficient by reusing the current stack frame. | "We have now seen how to use Tail Calls to execute mapWith in constant space:" | `normalized:L3005-L3005` | [Source](../sources/js-allonge.md) |

## Why it matters

Recursion allows for elegant solutions to problems that exhibit self-similarity, such as traversing nested data structures or implementing divide-and-conquer algorithms. It aligns well with mathematical definitions and can lead to more readable code for certain problems.

## Related pages

- [Functions](../concepts/functions.md)
- [Functional Programming](../concepts/functional-programming.md)
- [Control Flow](../concepts/control-flow.md)
- [Iterators](../concepts/iterators.md)
- [Arrays](../concepts/arrays.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
