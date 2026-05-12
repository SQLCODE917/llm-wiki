---
title: JavaScript Functions
type: concept
tags: []
status: draft
last_updated: 2026-05-12
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1069-L1069
  - js-allonge:normalized:L109-L110
  - js-allonge:normalized:L113-L113
  - js-allonge:normalized:L1137-L1137
  - js-allonge:normalized:L119-L119
  - js-allonge:normalized:L1455-L1455
  - js-allonge:normalized:L1477-L1482
  - js-allonge:normalized:L1485-L1485
  - js-allonge:normalized:L1493-L1497
  - js-allonge:normalized:L1533-L1535
  - js-allonge:normalized:L1545-L1545
  - js-allonge:normalized:L157-L157
  - js-allonge:normalized:L165-L167
  - js-allonge:normalized:L185-L185
  - js-allonge:normalized:L253-L265
  - js-allonge:normalized:L575-L577
  - js-allonge:normalized:L599-L600
  - js-allonge:normalized:L607-L607
  - js-allonge:normalized:L621-L621
  - js-allonge:normalized:L653-L657
  - js-allonge:normalized:L749-L749
  - js-allonge:normalized:L873-L873
  - js-allonge:normalized:L997-L997
  - js-allonge:normalized:L999-L999
---

# JavaScript Functions

## Summary

JavaScript functions are central to programming with functions, offering first-class support with lexical scope. They enable powerful programming techniques including closures, recursion, and functional mixins.

## Source-backed details

| Claim | Evidence |
| --- | --- |
| ECMAScript 2015 introduces significant enhancements to JavaScript, including destructuring, block-structured variables, iterables, generators, and the class keyword, making programming more... | [js-allonge:claim_js-allonge_c000_91756a08] |
| Modern JavaScript supports rest parameters in function definitions, allowing functions to collect remaining arguments efficiently. | [js-allonge:claim_js-allonge_c000_58060688] |
| ECMAScript 6 features are categorized into improved syntax for existing features, new standard library functionality, and completely new features like generators and proxies. | [js-allonge:claim_js-allonge_c000_214fe07b] |
| JavaScript allows for block-scoped variables using let, improving control flow and scoping behavior compared to traditional var declarations. | [js-allonge:claim_js-allonge_c000_029ab784] |
| JavaScript Allongé emphasizes programming with functions, leveraging JavaScript's first-class functions and lexical scope to write simpler and cleaner code. | [js-allonge:claim_js-allonge_c000_fd543f98] |
| Programming with functions leads to software that is simpler, cleaner, and less complicated than object-centric or code-centric approaches. | [js-allonge:claim_js-allonge_c000_fe732098] |
| The 'six' edition of JavaScript Allongé integrates classes, mixins, private properties with symbols, and iterators and generators, all based on functional programming principles. | [js-allonge:claim_js-allonge_c000_d5c0bd82] |
| Arrow functions in JavaScript can evaluate expressions directly, enabling concise function definitions. | [js-allonge:claim_js-allonge_c001_3ec3f59f] |
| Functions in JavaScript can be applied to arguments using the standard syntax fn_expr(args). | [js-allonge:claim_js-allonge_c001_58d96453] |
| Functions can return the result of evaluating another function, supporting higher-order function patterns. | [js-allonge:claim_js-allonge_c001_26084f35] |
| The comma operator in JavaScript evaluates both operands and returns the value of the right-hand operand. | [js-allonge:claim_js-allonge_c001_db28502f] |
| An empty function block evaluates to undefined when invoked. | [js-allonge:claim_js-allonge_c001_296bdec8] |
| To return a value from a function block, the return keyword must be used with an expression. | [js-allonge:claim_js-allonge_c001_323b0568] |
| JavaScript functions can be applied to arguments using function expressions, such as ((diameter) => diameter * 3.14159265)(1 + 1). | [js-allonge:claim_js-allonge_c002_fbeadf1f] |
| Functions containing free variables are known as closures, while those with no free variables are called pure functions. | [js-allonge:claim_js-allonge_c002_3b198538], [js-allonge:claim_js-allonge_c002_7a6263e3] |
| Variable shadowing occurs when a variable in a nested scope has the same name as one in an ancestor scope. | [js-allonge:claim_js-allonge_c002_7a71c2fa] |
| Variables can be bound in expressions by wrapping them in immediately invoked functions. | [js-allonge:claim_js-allonge_c002_3b815a11] |
| Named function expressions allow functions to be given internal names distinct from their binding names. | [js-allonge:claim_js-allonge_c003_27830237] |
| Recursive functions can be implemented using named function expressions, where the function name is available within its own body. | [js-allonge:claim_js-allonge_c003_400219f4] |
| In named function expressions, the function's actual name is not accessible in the outer environment. | [js-allonge:claim_js-allonge_c004_916f3fea] |
| Function declarations within other functions are not accessible outside of that function's scope. | [js-allonge:claim_js-allonge_c004_dbc733f9] |
| Functions can be defined inside other functions and accessed even if declared later in the same scope. | [js-allonge:claim_js-allonge_c004_9853e361] |
| Function declarations should ideally be placed at the top level of a function to avoid issues in certain JavaScript environments. | [js-allonge:claim_js-allonge_c004_93e1fb57] |

## Source pages

- [JavaScript Allongé](../sources/js-allonge.md)
