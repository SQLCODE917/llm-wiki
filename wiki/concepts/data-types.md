---
title: Data Types
type: concept
tags: []
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
---

# Data Types

JavaScript's data type system includes both primitive and reference types, with distinct behaviors for equality, copying, and evaluation. Primitive types like strings, numbers, and booleans are compared by value, while arrays and functions are reference types that are unique instances. The language supports functional programming paradigms through first-class functions and evaluates expressions using a call-by-value strategy. Special operators such as `!` and `!!` provide explicit conversion between values and boolean representations.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| JavaScript has proper first-class functions with lexical scope, making it suitable for functional programming. | normalized:L110-L110 | [Source](../sources/js-allonge.md) |
| All values are expressions in JavaScript, meaning they can be used to place an order and are returned as-is by the system. | "All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, "I want one of these." The..." | normalized:L355-L355 | [Source](../sources/js-allonge.md) |
| The number 42 is both an expression and a value in JavaScript, returning the same value when evaluated. | "The answer is, this is both an expression _and_ a value.[10] The way you can tell that it's both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano:" | normalized:L363-L363 | [Source](../sources/js-allonge.md) |
| Strings, numbers, and booleans are primitive types in JavaScript that are identical if they have the same content. | "Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with..." | normalized:L425-L425 | [Source](../sources/js-allonge.md) |
| Arrays and functions in JavaScript are reference types, meaning each instance is unique even if they appear identical. | "How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other..." | normalized:L449-L451 | [Source](../sources/js-allonge.md) |
| The undefined value in JavaScript represents the absence of a value and is identical to every other undefined value. | "In JavaScript, the absence of a value is written undefined, and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type:" | normalized:L663-L663 | [Source](../sources/js-allonge.md) |
| JavaScript uses call by value evaluation strategy where expressions are evaluated before being passed to functions. | "Like most contemporary programming languages, JavaScript uses the "call by value" evaluation strategy[23] . That means that when you write some code that appears to apply a function to an..." | normalized:L863-L863 | [Source](../sources/js-allonge.md) |
| The ! operator converts any value to a boolean and returns the opposite truthiness. | "Our logical operators !, &&, and \|\| are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not..." | normalized:L2239-L2239 | [Source](../sources/js-allonge.md) |
| The !! operator is used to explicitly convert any value to its boolean equivalent. | "Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and..." | normalized:L2249-L2249 | [Source](../sources/js-allonge.md) |
| Arrays in JavaScript are copied when using destructuring to extract elements, allowing modifications to the original array without affecting the copy. | "- When you take the rest of an array with destructuring ([first, ...rest]), you are given a _copy_ of the elements of the array. - When you take the rest of a linked list with its reference, you..." | normalized:L3689-L3693 | [Source](../sources/js-allonge.md) |
| Linked lists share nodes with their parent when accessing the rest of the list, causing modifications to affect both parent and child lists. | "- When you take the rest of a linked list with its reference, you are given the exact same nodes of the elements of the original list. The consequence of this is that if you have an array, and you..." | normalized:L3691-L3694 | [Source](../sources/js-allonge.md) |
| The author has written libraries for JavaScript, Ruby, CoffeeScript, and Java programming. | "When he's not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg "Raganwald" Braithwaite has authored libraries[221] for JavaScript, CoffeeScript,..." | normalized:L6477-L6477 | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding JavaScript's data types is crucial for predicting program behavior, especially regarding equality comparisons, mutability, and function parameter passing. Knowing which types are primitives versus reference types helps developers avoid common pitfalls such as unintended shared state in arrays and objects. The distinction between call-by-value and reference semantics affects how data flows through programs, particularly when working with complex data structures like linked lists or when using destructuring syntax.

## Source pages

- [Source](../sources/js-allonge.md)
```