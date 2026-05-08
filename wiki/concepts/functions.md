---
title: Functions
type: concept
tags: []
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
---

# Functions

Functions are fundamental building blocks in JavaScript that enable the composition of complex programs. They can be invoked with zero or more arguments to produce values, and support various mechanisms for managing state, scope, and control flow. In functional programming paradigms, functions serve not only as procedures but also as representations of data, allowing for encapsulation and abstraction.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| JavaScript Allongé is a book about programming with functions, focusing on how functions compose to make larger programs. | "JavaScript Allongé is a first and foremost, a book about _programming with functions_ . It's written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of..." | normalized:L109-L110 | [Source](../sources/js-allonge.md) |
| Functions can be applied to zero or more arguments to produce a value. | "Let's put functions to work. The way we use functions is to _apply_ them to zero or more values called _arguments_ . Just as 2 + 2 produces a value (in this case 4), applying a function to zero or..." | normalized:L573-L573 | [Source](../sources/js-allonge.md) |
| Functions can be applied to multiple arguments by listing them within parentheses separated by commas. | "((room, board) => room + board)(800, 150)" | normalized:L837-L837 | [Source](../sources/js-allonge.md) |
| Binding values to names with const works just like binding values to names with parameter invocations, using lexical scope. | "Yes. Binding values to names with const works just like binding values to names with parameter invocations, it uses lexical scope." | normalized:L1303-L1303 | [Source](../sources/js-allonge.md) |
| The name of a function defined with the function keyword is a property of the function itself, not of the environment binding. | "In this expression, double is the name in the environment, but repeat is the function's actual name. This is a _named function expression_ . That may seem confusing, but think of the binding names..." | normalized:L1457-L1457 | [Source](../sources/js-allonge.md) |
| JavaScript binds values to 'magic' names in addition to function argument names during function execution. | "When a function is applied to arguments (or "called"), JavaScript binds the values of arguments to the function's argument names in an environment created for the function's execution. What we..." | normalized:L1737-L1737 | [Source](../sources/js-allonge.md) |
| The 'arguments' magic name is commonly used to build functions that accept a variable number of arguments. | "The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and..." | normalized:L1767-L1767 | [Source](../sources/js-allonge.md) |
| JavaScript optimizes away function call overhead and stack space when a function makes a call in tail position. | "And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe-wrapped call. This is a very important characteristic of JavaScript: **If a..." | normalized:L2827-L2827 | [Source](../sources/js-allonge.md) |
| Copy-on-write is a strategy where copies are made only when modifications are about to occur, improving performance by avoiding unnecessary copying. | "This strategy of waiting to copy until you are writing is called copy-on-write, or "COW:"" | normalized:L3773-L3773 | [Source](../sources/js-allonge.md) |
| Using functions to represent data allows for hiding implementation details from code that uses the data, as the data structure controls how its internal values are accessed. | "The exact implementation of a pair is hidden from the code that uses a pair. Here, we'll prove it:" | normalized:L4333-L4333 | [Source](../sources/js-allonge.md) |
| Generator functions are declared using the function * syntax and use yield to produce values instead of return. | "We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a _generator_ . To write a generator, we write a function, but we make two..." | normalized:L5141-L5146 | [Source](../sources/js-allonge.md) |
| An interactive generator function can receive values from the caller via the .next() method and yield values back to the caller. | "_//=> 0_ aNaughtsAndCrossesGame.next(1).value _//=> 6_ aNaughtsAndCrossesGame.next(3).value _//=> 8_ aNaughtsAndCrossesGame.next(7).value _//=> 4_" | normalized:L6024-L6038 | [Source](../sources/js-allonge.md) |

## Why it matters

Functions form the core of program logic in JavaScript, enabling modular design and reusable code. Understanding their behavior--such as argument handling, scope management, and optimization--is essential for writing efficient and maintainable programs. Concepts like generators and copy-on-write further extend the expressive power of functions, supporting advanced patterns in functional programming and performance-sensitive applications.

## Source pages

- [Source](../sources/js-allonge.md)
```