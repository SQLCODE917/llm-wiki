---
page_id: javascriptallonge-truthiness-and-operators
page_kind: source
summary: truthiness and operators from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.96-97
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

This section covers truthiness and operators in JavaScript, including the behavior of !, &&, and || operators.

## Key supported claims

- Our logical operators !, &&, and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy (raw/javascriptallonge.pdf p.96-97).
- In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a, and the same goes for && (raw/javascriptallonge.pdf p.96-97).
- So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser(), this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user (raw/javascriptallonge.pdf p.96-97).

## Technical details

### `technical-atom-db1a2dfcc5799e60` code

Citation: (raw/javascriptallonge.pdf p.96-97)

```javascript
!5 //=> false ! undefined //=> true
```

### `technical-atom-0ca83b17a1275975` code

Citation: (raw/javascriptallonge.pdf p.96-97)

```javascript
1 || 2 //=> 1 null && undefined //=> null undefined && null //=> undefined
```

### `technical-atom-4242c29147b55336` requirement

Citation: (raw/javascriptallonge.pdf p.96-97)

It always returns false if its argument is truthy, and true is its argument is not truthy:

### `technical-atom-7a79b526d01dff95` requirement

Citation: (raw/javascriptallonge.pdf p.96-97)

Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not.

### `technical-atom-78ca85cfb1ead778` exception

Citation: (raw/javascriptallonge.pdf p.96-97)

-If its left-hand expression evaluates to something falsy, && returns the value of its lefthand expression without evaluating its right-hand expression.

### `technical-atom-519a764de8aeb061` exception

Citation: (raw/javascriptallonge.pdf p.96-97)

-If its left-hand expression evaluates to something truthy, || returns the value of its lefthand expression without evaluating its right-hand expression.

### `technical-atom-dbc76303af6bafa8` requirement

Citation: (raw/javascriptallonge.pdf p.96-97)

They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .
