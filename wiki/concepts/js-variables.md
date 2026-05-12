---
title: JavaScript Variables
type: concept
tags: [javascript, variables, bindings, const, scope]
status: draft
last_updated: 2026-05-12
sources:
  - ../sources/js-allonge.md
source_ranges:
  - js-allonge:normalized:L1199-L1201
  - js-allonge:normalized:L1355-L1355
  - js-allonge:normalized:L1389-L1389
  - js-allonge:normalized:L1393-L1393
---

# JavaScript Variables

## Summary

JavaScript variables are used to store data values. They can be declared using 'const', 'let', or 'var'. The 'const' keyword creates a variable that cannot be reassigned after initialization, while 'let' and 'var' allow reassignment. Variables in JavaScript have scope rules that determine where they can be accessed within code blocks.

## Source-backed details

| Claim | Evidence |
| --- | --- |
| Variables declared with 'const' in JavaScript cannot be reassigned after their initial assignment, which helps enforce immutability for values that should remain constant. | [js-allonge:claim_js-allonge_c003_798d1a81], [js-allonge:claim_js-allonge_c003_317ca4e4], [js-allonge:claim_js-allonge_c003_d42471f5] |
| JavaScript's block scoping allows variables declared with 'const' to be redeclared in nested scopes without conflict, enabling localized redefinition of identifiers. | [js-allonge:claim_js-allonge_c003_1445a17d], [js-allonge:claim_js-allonge_c003_80c9d02f], [js-allonge:claim_js-allonge_c003_b5ede1aa] |
| Attempting to reassign a value to a variable declared with 'const' results in an error, demonstrating that such variables are truly read-only once initialized. | [js-allonge:claim_js-allonge_c003_79b1486f] |

## Why it matters

Understanding how variables work in JavaScript is fundamental to writing correct and maintainable code. Using 'const' appropriately helps prevent accidental reassignments and makes code behavior more predictable. Proper scoping with 'const' and 'let' prevents issues like variable hoisting and unintended global pollution.

## Related pages

- [JavaScript Data Types](../concepts/js-data-types.md)
- [JavaScript Functions](../concepts/js-functions.md)
- [JavaScript Control Flow](../concepts/js-control-flow.md)
- [JavaScript Objects](../concepts/js-objects.md)
- [JavaScript Arrays](../concepts/js-arrays.md)
- [JavaScript Iterables](../concepts/js-iterables.md)
- [JavaScript Functional Programming](../concepts/js-functional-programming.md)
- [JavaScript Data Structures](../concepts/js-data-structures.md)

## Source pages

- [Js Allonge](../sources/js-allonge.md)
