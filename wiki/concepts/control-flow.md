---
title: Control Flow
type: concept
tags: []
status: draft
last_updated: 2026-05-05
sources:
  - ../sources/js-allonge.md
---

# Control Flow

Control flow refers to the order in which individual statements, instructions, or function calls are executed or evaluated in a program. In JavaScript, control flow is managed through various mechanisms including block scoping, operator precedence, the comma operator, logical operators, function parameter evaluation, loop constructs, cycle detection algorithms, generator functions for interactive programs, and switch statements for decision-making.

## Source-backed details

| Claim | Evidence | Locator | Source |
|---|---|---|---|
| Block-structured variables in ES6 allow for cleaner scoping of variables within loops and other code blocks | "With ECMAScript 2015, we can write: for (let i = 0; i < array.length; ++i) { // ... } And i is scoped to the for loop." | normalized:L234 | [Source](../sources/js-allonge.md) |
| JavaScript uses operator precedence to determine the order of operations in arithmetic expressions | "JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2), because the * operator has a higher precedence than the + operator." | normalized:L721 | [Source](../sources/js-allonge.md) |
| The comma operator in JavaScript evaluates both operands and returns the value of the right-hand operand | "The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: (1, 2) //=> 2" | normalized:L856 | [Source](../sources/js-allonge.md) |
| Logical operators in JavaScript operate on truthiness rather than strict boolean values | "In JavaScript, there is a notion of "truthiness." Every value is either "truthy" or "falsy." Obviously, false is falsy." | normalized:L2931 | [Source](../sources/js-allonge.md) |
| The logical operators !, &&, and || are control-flow operators that don't always return true or false | "The ternary operator (?:), ||, and && are control flow operators, they do not always return true or false, and they have short-cut semantics." | normalized:L2977 | [Source](../sources/js-allonge.md) |
| Function parameters are eagerly evaluated, which can cause issues with control-flow semantics | "function parameters are always eagerly evaluated: const or = (a, b) => a || b" | normalized:L3046 | [Source](../sources/js-allonge.md) |
| To implement control-flow semantics in functions, pass functions instead of expressions to delay evaluation | "If we need to have functions with control-flow semantics, we can pass anonymous functions." | normalized:L3057 | [Source](../sources/js-allonge.md) |
| Using var in for loops can cause issues with closures capturing the loop variable instead of its value at loop iteration time | "var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?" | normalized:L5029 | [Source](../sources/js-allonge.md) |
| The tortoise and hare algorithm can be used to detect cycles in a sequence by using two iterators moving at different speeds | "This is, of course, the most common solution, it is Floyd's cycle-finding algorithm, although there is some academic dispute as to whether Robert Floyd actually discovered it or was misattributed by Knuth." | normalized:L9052 | [Source](../sources/js-allonge.md) |
| A cycle detection algorithm can be implemented using a teleporting tortoise that moves at increasing distances | "const hasCycle = (iterable) => { let iterator = iterable[Symbol.iterator](), teleportDistance = 1; while (true) { let {value, done} = iterator.next(), tortoise = value; if (done) return false; for (let i = 0; i < teleportDistance; ++i) { let {value, done} = iterator.next(), hare = value; if (done) return false; if (tortoise === hare) return true; } teleportDistance *= 2; } return false; };" | normalized:L9132 | [Source](../sources/js-allonge.md) |
| Interactive programs can be modeled using generators that yield values and receive inputs during execution | "Can we do the same thing here? At first glance, no. How do we get the player's moves to the generator function? But the first glance is deceptive, because we only see what we've seen so far. Let's see how it would actually work." | normalized:L9534 | [Source](../sources/js-allonge.md) |
| Switch statements can be used to implement decision trees for game logic | "switch (x1) { case 1: const x2 = parseInt(prompt('o plays 6, where does x play?')); switch (x2) { case 2:" | normalized:L9493 | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding control flow is essential for writing predictable and maintainable JavaScript code. It helps developers manage variable scoping, understand operator behavior, implement conditional logic correctly, avoid common pitfalls with closures and loop variables, detect cycles in data structures, model interactive programs, and build complex decision-making systems. Mastery of these concepts enables more robust and efficient programming practices.

## Source pages

- [Source](../sources/js-allonge.md)