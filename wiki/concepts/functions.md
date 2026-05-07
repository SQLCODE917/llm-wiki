---
title: Functions
type: concept
tags: [javascript, programming, functions]
status: draft
last_updated: 2026-05-07
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1039-L1042
  - js-allonge:normalized:L1067-L1068
  - js-allonge:normalized:L1079-L1082
  - js-allonge:normalized:L1120-L1120
  - js-allonge:normalized:L169-L172
  - js-allonge:normalized:L293-L295
  - js-allonge:normalized:L343-L345
  - js-allonge:normalized:L760-L761
  - js-allonge:normalized:L761-L765
  - js-allonge:normalized:L794-L796
---

# Functions

## Summary

Functions are fundamental constructs in JavaScript that serve as first-class citizens, enabling powerful programming paradigms such as functional programming. They encapsulate reusable blocks of code that can be invoked with arguments to perform computations.

## Source-backed details

| Claim | Evidence | Locator | Source |
| --- | --- | --- | --- |
| In JavaScript, functions are treated as first-class values that can be assigned to variables, passed as arguments, and returned from other functions. | "The second simplest possible function.16 In JavaScript, it looks like this: () => 0" | `normalized:L760-L761` | [Source](../sources/js-allonge.md) |
| In JavaScript, functions are treated as first-class values that can be assigned to variables, passed as arguments, and returned from other functions. | "(() => 0) //=> [Function]" | `normalized:L761-L765` | [Source](../sources/js-allonge.md) |
| JavaScript Allongé emphasizes the foundational role of functions in programming, focusing on how core concepts combine to form new ideas rather than just teaching syntax. | "JavaScript Allongé is a first and foremost, a book about programming with functions. It's written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of..." | `normalized:L169-L172` | [Source](../sources/js-allonge.md) |
| JavaScript Allongé emphasizes the foundational role of functions in programming, focusing on how core concepts combine to form new ideas rather than just teaching syntax. | "The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. The intention is to improve the way we think about programs." | `normalized:L293-L295` | [Source](../sources/js-allonge.md) |
| JavaScript Allongé emphasizes the foundational role of functions in programming, focusing on how core concepts combine to form new ideas rather than just teaching syntax. | "JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn't a book about practicing,..." | `normalized:L343-L345` | [Source](../sources/js-allonge.md) |
| Functions in JavaScript support various application patterns including those with arguments, nested function returns, and evaluation strategies like 'call by value'. | "Let's put functions to work. The way we use functions is to apply them to zero or more values called arguments." | `normalized:L794-L796` | [Source](../sources/js-allonge.md) |
| Functions in JavaScript support various application patterns including those with arguments, nested function returns, and evaluation strategies like 'call by value'. | "Yes: () => () => 0 That's a function! It's a function that when applied, evaluates to a function that when applied, evaluates to 0." | `normalized:L1039-L1042` | [Source](../sources/js-allonge.md) |
| Functions in JavaScript support various application patterns including those with arguments, nested function returns, and evaluation strategies like 'call by value'. | "Let's make a function with an argument: (room) => {}" | `normalized:L1067-L1068` | [Source](../sources/js-allonge.md) |
| Functions in JavaScript support various application patterns including those with arguments, nested function returns, and evaluation strategies like 'call by value'. | "To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this: ((diameter) => diameter * 3.14159265)(2)" | `normalized:L1079-L1082` | [Source](../sources/js-allonge.md) |
| Functions in JavaScript support various application patterns including those with arguments, nested function returns, and evaluation strategies like 'call by value'. | "Like most contemporary programming languages, JavaScript uses the "call by value" evaluation strategy." | `normalized:L1120-L1120` | [Source](../sources/js-allonge.md) |

## Why it matters

Understanding functions is crucial for mastering JavaScript and adopting functional programming principles. Functions allow for modular, reusable, and composable code, which leads to cleaner and more maintainable software designs.

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
