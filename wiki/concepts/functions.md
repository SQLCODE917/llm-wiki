---
title: Functions
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# Functions

In JavaScript, functions are first-class values that can be applied to zero or more arguments to produce a result, serving as fundamental building blocks for programming with functional techniques.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| In JavaScript, functions are values that can be applied to zero or more arguments to produce a result | "Let's put functions to work. The way we use functions is to apply them to zero or more values called arguments. Just as 2 + 2 produces a value (in this case 4), applying a function to zero or more arguments produces a value as well." | `normalized:L794` | [JavaScript Allongé](../sources/js-allonge.md) |
| Functions with arguments are applied by placing the argument values within parentheses | "To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this: ((diameter) => diameter * 3.14159265)(2)" | `normalized:L1079` | [JavaScript Allongé](../sources/js-allonge.md) |
| Functions in JavaScript can be bound to names using IIFEs which allow for encapsulation of values and creation of reusable function expressions | "((PI) => (diameter) => diameter * PI)(3.14159265) This expression, when evaluated, returns a function that calculates circumferences." | `normalized:L1413` | [JavaScript Allongé](../sources/js-allonge.md) |
| Function declarations should generally be placed at the top level of a function, not inside blocks or conditional statements | "Function declarations are formally only supposed to be made at what we might call the "top level" of a function." | `normalized:L2048` | [JavaScript Allongé](../sources/js-allonge.md) |
| Partial application is a technique where a function is applied to some of its arguments, returning a new function | "Another basic building block is partial application. When a function takes multiple arguments, we apply the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can't get the final value, but we can get a function that represents part of our application." | `normalized:L2219` | [JavaScript Allongé](../sources/js-allonge.md) |
| The maybe decorator prevents a function from executing if any of its arguments are null or undefined | "const maybe = (fn) => function (...args) { if (args.length === 0) { return } else { for (let arg of args) { if (arg == null) return; } return fn.apply(this, args) } }" | `normalized:L2640` | [JavaScript Allongé](../sources/js-allonge.md) |
| Mapping and folding are specialized cases of linear recursion that are particularly useful for building other functions | "Its specialized cases of mapping and folding are especially useful and can be used to build other functions" | `normalized:L3618` | [JavaScript Allongé](../sources/js-allonge.md) |
| Folding is a universal operation that can express any task achievable with traditional loops | "Folding is a universal operation, and with care we can accomplish any task with folds that could be accomplished with that stalwart of structured programming, the for loop." | `normalized:L5522` | [JavaScript Allongé](../sources/js-allonge.md) |
| Functions can encapsulate behavior and hide implementation details from code that uses them | "The exact implementation of a pair is hidden from the code that uses a pair. Here, we'll prove it: ... This is a little gratuitous, but it makes the point: The code that uses the data doesn't reach in and touch it: The code that uses the data provides some code and asks the data to do something with it." | `normalized:L6234` | [JavaScript Allongé](../sources/js-allonge.md) |
| Functions can be used to create closures that maintain state | "const Stack1 = () => ({ array:[], index: -1, push (value) { return this.array[this.index += 1] = value; }, pop () { const value = this.array[this.index]; this.array[this.index] = undefined; if (this.index >= 0) { this.index -= 1 } return value }, isEmpty () { return this.index < 0 }, iterator () { let iterationIndex = this.index; return () => { if (iterationIndex > this.index) { iterationIndex = this.index; } if (iterationIndex < 0) { return {done: true}; } else { return {done: false, value: this.array[iterationIndex--]} } } } });" | `normalized:L6690` | [JavaScript Allongé](../sources/js-allonge.md) |
| Lazy collections can be combined with immutable data structures to ensure predictable behavior | "Balanced against their flexibility, our "lazy collections" use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why "pure" functional languages like Haskell combine lazy semantics with immutable collections." | `normalized:L8648` | [JavaScript Allongé](../sources/js-allonge.md) |

## Why it matters

Functions are central to functional programming in JavaScript, enabling powerful patterns like partial application, decorators such as the maybe wrapper, and higher-order functions that manipulate data through mapping and folding operations. They support encapsulation, state management through closures, and can be composed to build complex behaviors while maintaining predictable outcomes when combined with immutable data structures and lazy evaluation techniques.

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)