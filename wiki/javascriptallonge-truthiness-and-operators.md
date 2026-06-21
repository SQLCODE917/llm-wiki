---
page_id: javascriptallonge-truthiness-and-operators
page_kind: source
summary: Summary of the truthiness and operators section from JavaScript Allongé.
sources: raw/javascriptallonge.pdf p.96-97
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

This section covers truthiness and operators in JavaScript, including the behavior of !, &&, and || operators.

## Key supported claims

- Our logical operators !, &&, and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy (raw/javascriptallonge.pdf p.96-97).
- In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a, and the same goes for && (raw/javascriptallonge.pdf p.96-97).
- So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser(), this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user (raw/javascriptallonge.pdf p.96-97).
