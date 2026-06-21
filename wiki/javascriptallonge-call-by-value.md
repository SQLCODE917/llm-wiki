---
page_id: javascriptallonge-call-by-value
page_kind: source
summary: Summary of the call by value evaluation strategy in JavaScript, based on the source 'javascriptallonge'.
sources: raw/javascriptallonge.pdf p.40-41
updated: 2026-06-20
source_id: javascriptallonge.pdf
---

## Source record

Like most contemporary programming languages, JavaScript uses the 'call by value' evaluation strategy. That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s).

## Key supported claims

- JavaScript uses the 'call by value' evaluation strategy. (raw/javascriptallonge.pdf p.40-41)
- In call by value, JavaScript evaluates expressions before applying functions to the resulting values. (raw/javascriptallonge.pdf p.40-41)
- Example: ((diameter) => diameter * 3.14159265)(1 + 1) evaluates 1 + 1 to 2 before applying the function. (raw/javascriptallonge.pdf p.40-41)
