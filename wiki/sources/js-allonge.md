---
title: JavaScript Allongé - Six Edition
type: source
source_id: js-allonge
source_type: pdf
raw_path: ../../raw/imported/js-allonge/
normalized_path: ../../raw/normalized/js-allonge/
status: draft
last_updated: 2026-05-05
tags: []
sources:
  - ../../raw/imported/js-allonge/original.pdf
---

# JavaScript Allongé - Six Edition

## Summary

JavaScript Allongé is a comprehensive guide to functional programming concepts in JavaScript, focusing on the evolution from basic functions to advanced patterns like closures, currying, and lazy evaluation. The book emphasizes understanding JavaScript's functional capabilities through practical examples and exercises, covering topics such as function composition, data structures, iteration, and recursive algorithms. It explores how JavaScript's unique features enable functional programming styles while maintaining compatibility with traditional imperative approaches.

## Key claims

| Claim | Evidence | Locator |
|---|---|---|
| JavaScript treats statements and expressions differently, with statements belonging inside blocks and only inside blocks. | "Statements belong inside blocks and only inside blocks. Some languages simplify this by making everything an expression, but JavaScript maintains this distinction, so when learning JavaScript we also learn about statements like function declarations, for loops, if statements, and so forth." | `normalized:L1024` |
| Function declarations are hoisted to the top of their enclosing scope, allowing helper functions to be defined after their usage. | "Although fizzbuzz is declared later in the function, JavaScript behaves as if we'd written: (function () { const fizzbuzz = function fizzbuzz () { return \"Fizz\" + \"Buzz\"; } return fizzbuzz(); })() The definition of the fizzbuzz is \"hoisted\" to the top of its enclosing scope (an IIFE in this case)." | `normalized:L2074` |
| The logical OR ( OR ) and AND ( AND ) operators have short-circuit semantics, evaluating expressions only when necessary. | " OR  and  AND  have short-cut semantics. In this case, if n === 0, JavaScript does not evaluate (n !== 1  AND  even(n - 2)). Likewise, if n === 1, JavaScript evaluates n !== 1  AND  even(n - 2) as false without ever evaluating even(n - 2). This is more than just an optimization. It's best to think of  OR  and  AND  as control-flow operators." | `normalized:L3043` |
| Function parameters are eagerly evaluated, unlike conditional operators which have short-circuit behavior. | "In contrast to the behaviour of the ternary operator,  OR , and  AND , function parameters are always eagerly evaluated:" | `normalized:L3065` |
| Destructuring assignments support default values similar to function parameters. | "How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters." | `normalized:L4042` |
| Iterables provide ordered collections where every iteration produces elements in the same sequence. | "The iterables we're discussing represent ordered collections. One of the semantic properties of an ordered collection is that every time you iterate over it, you get its elements in order, from the beginning." | `normalized:L7063` |
| Lazy evaluation allows for efficient processing of potentially infinite sequences without memory overflow. | "append iterates over a collection of iterables, one element at a time. Things like arrays can be easily catenated, but append iterates lazily, so there's no need to construct intermediary results." | `normalized:L8070` |
| Tail call optimization enables recursive functions to execute in constant space when properly implemented. | "We have now seen how to use Tail Calls to execute mapWith in constant space:" | `normalized:L4077` |
| JavaScript's function values allow for powerful closure-based programming patterns. | "Hey, remember that functions in JavaScript are values? Let's get fancy!" | `normalized:L5044` |

## Major concepts

- Functional programming in JavaScript
- Statements vs expressions
- Function hoisting and scope
- Logical operators and short-circuit evaluation
- Destructuring with defaults
- Iterables and lazy evaluation
- Tail call optimization
- Closures and function values
- Recursive algorithms
- Data structure manipulation

### Natural groupings

| Group | Scope | Evidence basis | Candidate page types |
|---|---|---|---|
| Basic Functions | Introduction to JavaScript functions and their behavior | function declarations, statements, expressions | concept |
| Control Flow Operators | Logical OR ( OR ) and AND ( AND ) operators with short-circuit behavior | short-circuit semantics, conditional evaluation | concept |
| Destructuring and Defaults | Pattern matching with default values for variables and parameters | destructuring assignments, default parameters | concept |
| Iteration and Collections | Working with iterables, lazy evaluation, and ordered collections | iterables, generators, append function | concept |
| Recursion and Tail Calls | Recursive algorithms and tail call optimization techniques | recursive functions, tail call elimination | concept |
| Closures and Function Values | Using functions as values and creating closures | closure examples, function values | concept |

## Entities

None.

## Procedures

None.

## References

None.

## Open questions

None.

## Related pages

| Candidate page | Intended path | Group | Priority | Evidence basis | Status |
|---|---|---|---|---|---|
| JavaScript Functions | `../concepts/js-functions.md` | Basic Functions | must create | function declarations, statements, expressions | not created yet |
| Short-Circuit Evaluation | `../concepts/short-circuit-evaluation.md` | Control Flow Operators | must create | logical operators  OR  and  AND  with short-circuit behavior | not created yet |
| Destructuring with Defaults | `../concepts/destructuring-defaults.md` | Destructuring and Defaults | must create | destructuring assignments with defaults | not created yet |
| Lazy Evaluation | `../concepts/lazy-evaluation.md` | Iteration and Collections | must create | iterables, lazy evaluation techniques | not created yet |
| Tail Call Optimization | `../concepts/tail-call-optimization.md` | Recursion and Tail Calls | must create | tail call elimination, recursive functions | not created yet |
| Closures | `../concepts/closures.md` | Closures and Function Values | must create | function values, closure examples | not created yet |
| Functional Programming in JavaScript | `../concepts/functional-programming-js.md` | Basic Functions | should create | overall functional programming approach | not created yet |
| Iterables and Generators | `../concepts/iterables-generators.md` | Iteration and Collections | should create | ordered collections, generators | not created yet |