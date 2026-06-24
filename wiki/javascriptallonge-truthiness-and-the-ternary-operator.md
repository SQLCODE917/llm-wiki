---
page_id: javascriptallonge-truthiness-and-the-ternary-operator
page_kind: source
summary: truthiness and the ternary operator from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.95-96
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined, values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. Every other value in JavaScript is 'truthy' except the aforementioned false, null, undefined, NaN, 0, and ''.

## Key supported claims

- False is falsy in JavaScript. (raw/javascriptallonge.pdf p.95-96)
- Truthiness affects how logical operators and if statements work. (raw/javascriptallonge.pdf p.95-96)
- JavaScript inherited the ternary operator from C. It takes three arguments. (raw/javascriptallonge.pdf p.95-96)
- The ternary operator is an expression, not a statement. (raw/javascriptallonge.pdf p.95-96)

## Technical details

### `technical-atom-28dd8b450cc4ea1e` code

Citation: (raw/javascriptallonge.pdf p.95-96)

```javascript
true ? 'Hello' : 'Good bye' //=> 'Hello' 0 ? 'Hello' : 'Good bye' //=> 'Good bye' [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' //=> 'Pentatonic'
```

### `technical-atom-b10dc3555d085eff` code

Citation: (raw/javascriptallonge.pdf p.95-96)

```javascript
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den';
```

### `technical-atom-8ccbfb59d500ba84` code

Citation: (raw/javascriptallonge.pdf p.95-96)

```
'Hello' : 'Good bye' //=> 'Good bye' [1, 2, 3, 4, 5].length === 5 ?
```

### `technical-atom-ce4e1fdf33c4d740` procedure

Citation: (raw/javascriptallonge.pdf p.95-96)

We'll look at them in a moment, but first, we'll look at one more operator.

### `technical-atom-bb41af449e0cdc69` exception

Citation: (raw/javascriptallonge.pdf p.95-96)

Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' .

### `technical-atom-4949693f4290a4cd` exception

Citation: (raw/javascriptallonge.pdf p.95-96)

It's the only operator that takes three arguments.

### `technical-atom-7f475abc0c10c679` worked-example

Citation: (raw/javascriptallonge.pdf p.95-96)

(Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!)

### `technical-atom-8df6859e9fc1caf2` worked-example

Citation: (raw/javascriptallonge.pdf p.95-96)

Consider this hypothetical example:

## Related technical details

### From [[javascriptallonge-truthiness-and-operators]]: `technical-atom-0ca83b17a1275975` code

Relation: nearby source page; matched terms `null`, `operators`, `truthiness`, `undefined`

Citation: (raw/javascriptallonge.pdf p.96-97)

```javascript
1 || 2 //=> 1 null && undefined //=> null undefined && null //=> undefined
```

### From [[javascriptallonge-truthiness-and-operators]]: `technical-atom-78ca85cfb1ead778` exception

Relation: nearby source page; matched terms `expression`, `falsy`, `operators`, `something`, `truthiness`, `value`

Citation: (raw/javascriptallonge.pdf p.96-97)

-If its left-hand expression evaluates to something falsy, && returns the value of its lefthand expression without evaluating its right-hand expression.

### From [[javascriptallonge-truthiness-and-operators]]: `technical-atom-519a764de8aeb061` exception

Relation: nearby source page; matched terms `expression`, `operators`, `something`, `truthiness`, `truthy`, `value`

Citation: (raw/javascriptallonge.pdf p.96-97)

-If its left-hand expression evaluates to something truthy, || returns the value of its lefthand expression without evaluating its right-hand expression.

### From [[javascriptallonge-truthiness-and-operators]]: `technical-atom-4242c29147b55336` requirement

Relation: nearby source page; matched terms `false`, `not`, `operators`, `truthiness`, `truthy`

Citation: (raw/javascriptallonge.pdf p.96-97)

It always returns false if its argument is truthy, and true is its argument is not truthy:
