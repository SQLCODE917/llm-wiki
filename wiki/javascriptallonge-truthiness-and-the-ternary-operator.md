---
page_id: javascriptallonge-truthiness-and-the-ternary-operator
page_kind: source
summary: Chapter on truthiness and the ternary operator from JavaScript Allongé.
sources: raw/javascriptallonge.pdf p.95-96
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined, values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. Every other value in JavaScript is 'truthy' except the aforementioned false, null, undefined, NaN, 0, and ''.

## Key supported claims

- False is falsy in JavaScript. (raw/javascriptallonge.pdf p.95-96)
- Truthiness affects how logical operators and if statements work. (raw/javascriptallonge.pdf p.95-96)
- JavaScript inherited the ternary operator from C. It takes three arguments. (raw/javascriptallonge.pdf p.95-96)
- The ternary operator is an expression, not a statement. (raw/javascriptallonge.pdf p.95-96)
