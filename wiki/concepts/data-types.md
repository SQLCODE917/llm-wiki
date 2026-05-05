---
title: Data Types
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# Data Types

Data types in JavaScript distinguish between primitive and reference types, where primitives are identical if they have the same type and content, while reference types are unique even when appearing identical. JavaScript handles value types and reference types differently when passing arguments to functions, with value types creating copies and reference types placing references in environments. Objects serve as the primary data structure for representing collections of heterogeneous data, while arrays and linked lists differ in their handling of copying when taking the "rest" of a data structure.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| In JavaScript, all values are also expressions, but not all expressions are values | "All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, "I want one of these." The barista is no fool, she gives it straight back to you, and you get exactly what you want. Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista)." | normalized:L507 | [Source](../sources/js-allonge.md) |
| Primitive types in JavaScript are identical if they have the same type and content, whereas reference types are unique even if they appear identical | "Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far. ... But are they identical the same way that every value of 42 is identical to every other value of 42? Try these for yourself: [2-1, 2, 2+1] === [1,2,3]" | normalized:L590 | [Source](../sources/js-allonge.md) |
| JavaScript numbers are represented internally as double-precision floating-point values, which can lead to precision issues with decimal fractions | "Internally, both 042 and 34 have the same representation, as double-precision floating point numbers. A computer's internal representation for numbers is important to understand. The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing "under the hood." | normalized:L659 | [Source](../sources/js-allonge.md) |
| JavaScript distinguishes between value types and reference types when passing arguments to functions | "JavaScript binds names to values, but we didn't say what it means to bind a name to a value. When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments." | normalized:L1199 | [Source](../sources/js-allonge.md) |
| Linked lists are more efficient than arrays for certain operations like accessing the head element and getting the rest of the list | "In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed." | normalized:L4173 | [Source](../sources/js-allonge.md) |
| In JavaScript, objects are the primary data structure for representing collections of heterogeneous data | "Lists are not the only way to represent collections of things, but they are the "oldest" data structure in the history of high level languages, because they map very closely to the way the hardware is organized in a computer. Lists are obviously very handy for homogeneous collections of things, like a shopping list: const remember = ["the milk", "the coffee beans", "the biscotti"]; And they can be used to store heterogeneous things in various levels of structure: const user = [["Reginald", "Braithwaite"],[ "author", ["JavaScript Allongé", "JavaScript Spessore", "CoffeeScript Ristretto"]]]; Remembering that the name is the first item is error-prone, and being expected to look at user[0][1] and know that we are talking about a surname is unreasonable." | normalized:L4228 | [Source](../sources/js-allonge.md) |
| JavaScript allows reassignment of new values to existing bindings, including elements of arrays and objects | "JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects." | normalized:L4616 | [Source](../sources/js-allonge.md) |
| Arrays and linked lists differ in how they handle copying when taking the 'rest' of a data structure | "• When you take the rest of an array with destructuring ([first, ...rest]), you are given a copy of the elements of the array. • When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list." | normalized:L5139 | [Source](../sources/js-allonge.md) |
| A pair data structure can be created using the V combinator, which takes two values and applies them to a selector function | "const first = K, second = K(I), pair = V; const latin = pair("primus")("secundus"); latin(first) //=> "primus"" | normalized:L6006 | [Source](../sources/js-allonge.md) |
| Lists can be implemented using function-based representations that encapsulate both data and behavior | "const EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty() ... const node = (x) => (y) => (whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));" | normalized:L6168 | [Source](../sources/js-allonge.md) |
| Quasi-literal strings are evaluated at runtime when the code is executed | "Like any other expression, quasi-literals are evaluated late, when that line or lines of code is evaluated." | normalized:L6641 | [Source](../sources/js-allonge.md) |
| Sets in JavaScript can be used to efficiently track visited elements for cycle detection | "const visited = new Set();" | normalized:L9160 | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding data types in JavaScript is crucial for grasping how values are stored, compared, and passed around in programs. The distinction between primitive and reference types affects memory usage, performance, and program behavior. Knowing how different data structures like arrays, linked lists, and objects handle copying and access patterns helps developers make informed decisions about data manipulation and algorithm efficiency. Additionally, understanding how JavaScript represents numbers internally helps avoid common pitfalls related to floating-point arithmetic precision.

## Source pages

- [Source](../sources/js-allonge.md)