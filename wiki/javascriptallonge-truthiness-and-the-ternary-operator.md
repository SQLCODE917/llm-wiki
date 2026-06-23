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

### `technical-atom-bb41af449e0cdc69` exception

Citation: (raw/javascriptallonge.pdf p.95-96)

Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' .

### `technical-atom-7f475abc0c10c679` worked-example

Citation: (raw/javascriptallonge.pdf p.95-96)

(Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!)

### `technical-atom-ce4e1fdf33c4d740` procedure

Citation: (raw/javascriptallonge.pdf p.95-96)

We'll look at them in a moment, but first, we'll look at one more operator.

### `technical-atom-4949693f4290a4cd` exception

Citation: (raw/javascriptallonge.pdf p.95-96)

It's the only operator that takes three arguments.

### `technical-atom-8ccbfb59d500ba84` code

Citation: (raw/javascriptallonge.pdf p.95-96)

```
'Hello' : 'Good bye' //=> 'Good bye' [1, 2, 3, 4, 5].length === 5 ?
```

### `technical-atom-8df6859e9fc1caf2` worked-example

Citation: (raw/javascriptallonge.pdf p.95-96)

Consider this hypothetical example:
