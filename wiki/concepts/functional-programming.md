---
title: Functional Programming
type: concept
tags: [programming-paradigm, functions, combinators, higher-order-functions]
status: draft
last_updated: 2026-05-11
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1587-L1589
  - js-allonge:normalized:L1605-L1605
  - js-allonge:normalized:L1627-L1629
  - js-allonge:normalized:L1691-L1693
  - js-allonge:normalized:L185-L185
  - js-allonge:normalized:L1871-L1871
  - js-allonge:normalized:L201-L201
  - js-allonge:normalized:L2945-L2945
  - js-allonge:normalized:L3005-L3005
  - js-allonge:normalized:L3131-L3132
  - js-allonge:normalized:L3333-L3335
  - js-allonge:normalized:L4059-L4059
  - js-allonge:normalized:L4075-L4075
  - js-allonge:normalized:L4435-L4435
  - js-allonge:normalized:L5955-L5963
---

# Functional Programming

## Summary

Functional programming is a paradigm centered on the use of functions, emphasizing immutability, pure functions, and the composition of functions to build complex behaviors. It leverages concepts like higher-order functions, combinators, and function decorators to create flexible and modular code.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| JavaScript's evolution includes features like classes, mixins, and iterators that are fundamentally built upon simple objects and functions, allowing programmers to apply functional programming... | "Thus, the "six" edition introduces classes and mixins. It introduces the notion of implementing private properties with symbols. It introduces iterators and generators. But the common thread that..." | `normalized:L185-L185` | [Source](../sources/js-allonge.md) |
| The core philosophy of JavaScript Allongé is to explore programming with functions, where fundamental concepts like decorators, methods, and delegation stem from functional principles. | "JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions." | `normalized:L201-L201` | [Source](../sources/js-allonge.md) |
| In functional programming, a combinator is a higher-order function that constructs results using only function application and previously defined combinators, providing a rigorous mathematical... | "The word "combinator" has a precise technical meaning in mathematics: "A combinator is a higher-order function that uses only function application and earlier defined combinators to define a..." | `normalized:L1587-L1589` | [Source](../sources/js-allonge.md) |
| Function composition is a key technique in functional programming, exemplified by a compose function that takes two functions and returns their sequential application. | "- **const** compose = (a, b) => (c) => a(b(c))" | `normalized:L1605-L1605` | [Source](../sources/js-allonge.md) |
| Function decorators are higher-order functions that modify or enhance other functions, creating variations of the original function while preserving its core behavior. | "## **function decorators** A _function decorator_ is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the..." | `normalized:L1627-L1629` | [Source](../sources/js-allonge.md) |
| Partial application allows a function to be applied to some of its arguments, returning a new function that expects the remaining arguments, enabling flexible function reuse. | "Another basic building block is _partial application_ . When a function takes multiple arguments, we "apply" the function to the arguments by evaluating it with all of the arguments, producing a..." | `normalized:L1691-L1693` | [Source](../sources/js-allonge.md) |
| Utility functions like callFirst and callLast can be created to partially apply arguments to a given function, facilitating the construction of specialized function variants. | "**const** callFirst = (fn, larg) => **function** (...rest) { **return** fn.call( **this** , larg, ...rest); } **const** callLast = (fn, rarg) => **function** (...rest) { **return** fn.call(..." | `normalized:L1871-L1871` | [Source](../sources/js-allonge.md) |
| Tail call optimization enables recursive functions to operate efficiently in constant space, which is crucial for implementing operations like mapping over large data structures without stack... | "We have now seen how to use Tail Calls to execute mapWith in constant space:" | `normalized:L3005-L3005` | [Source](../sources/js-allonge.md) |
| While recursive patterns like mapWith using destructuring are illustrative of recursion, they are not the most idiomatic way to perform such operations in practice. | "Although we showed how to use tail calls to map and fold over arrays with [first, ...rest], in reality this is not how it ought to be done. But it is an extremely simple illustration of how..." | `normalized:L3131-L3132` | [Source](../sources/js-allonge.md) |
| Recursive functions can be implemented to process data structures like linked lists in a tail-recursive manner, accumulating results to avoid growing the call stack. | "**const** reverseMapWith = (fn, node, delayed = EMPTY) => node === EMPTY ? delayed : reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed }); reverseMapWith((x) => x * x,..." | `normalized:L3333-L3335` | [Source](../sources/js-allonge.md) |
| Higher-order functions such as callLast can be expressed using rest parameters to prepend arguments to a function call, demonstrating functional composition patterns. | "**const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);" | `normalized:L2945-L2945` | [Source](../sources/js-allonge.md) |
| Fundamental data structures like lists can be modeled purely using functions, showing that complex behaviors can emerge from simple functional primitives. | "They established that arbitrary computations could be represented a small set of axiomatic components. For example, we don't need arrays to represent lists, or even POJOs to represent nodes in a..." | `normalized:L4059-L4059` | [Source](../sources/js-allonge.md) |
| Basic combinators like K (constant), I (identity), and V (application) are foundational elements in lambda calculus and functional programming, representing core computational operations. | "**const** K = (x) => (y) => x; **const** I = (x) => (x); **const** V = (x) => (y) => (z) => z(x)(y);" | `normalized:L4075-L4075` | [Source](../sources/js-allonge.md) |
| Both mapWith and similar recursive patterns demonstrate how functional programming encourages building abstractions from common, reusable components rather than crafting each operation from scratch. | "Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common..." | `normalized:L4435-L4435` | [Source](../sources/js-allonge.md) |
| Functional programming emphasizes the ability to construct complex systems by combining simpler functions, leading to more modular and composable code. | "Both patterns take us to the same destination: Composing functions out of common pieces, rather than building them entirely from scratch. mapWith is a very convenient abstraction for a very common..." | `normalized:L4435-L4435` | [Source](../sources/js-allonge.md) |
| Stateful behaviors can be constructed using closures and functional techniques, allowing for encapsulation of state within function scopes while maintaining functional purity. | "We can build this out of our statelessNaughtsAndCrosses function: **const** statefulNaughtsAndCrosses = () => { **const** state = [ ' ' ' ' ' ' , , , ' ' ' ' ' ' , , , ' ' ' ' ' ' , , ];..." | `normalized:L5955-L5963` | [Source](../sources/js-allonge.md) |

## Why it matters

Functional programming techniques enable developers to write more predictable, testable, and maintainable code by focusing on the application of functions rather than changing state. It promotes composability and reusability of code elements, making large systems easier to reason about.

## Related pages

- [Functions](../concepts/functions.md)
- [Higher-Order Functions](../concepts/functions.md)
- [Combinators](../concepts/functions.md)
- [Iterators](../concepts/iterators.md)
- [Objects](../concepts/objects.md)
- [Control Flow](../concepts/control-flow.md)
- [Arrays](../concepts/arrays.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
