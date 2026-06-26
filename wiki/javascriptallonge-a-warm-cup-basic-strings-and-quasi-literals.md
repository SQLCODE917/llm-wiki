---
page_id: javascriptallonge-a-warm-cup-basic-strings-and-quasi-literals
page_kind: source
summary: A Warm Cup: Basic Strings and Quasi-Literals from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.202-204
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter 'A Warm Cup: Basic Strings and Quasi-Literals' from 'JavaScript Allongé' covers basic string literals, escape sequences, concatenation, and quasi-literal strings with expression interpolation.

## Key supported claims

- JavaScript has string literals like 'fubar' or 'fizzbuzz' with escape sequences for special characters such as \n for newline (raw/javascriptallonge.pdf p.202-204).
- The + operator concatenates strings, e.g., 'fu' + 'bar' evaluates to 'fubar' (raw/javascriptallonge.pdf p.202-204).
- String manipulation is extremely common in programming, and writing is a big part of what makes us human (raw/javascriptallonge.pdf p.202-204).
- JavaScript supports quasi-literal strings denoted with back quotes, which can include expressions using ${expression} (raw/javascriptallonge.pdf p.202-204).
- Quasi-literals are evaluated late, when the code is executed, making them easier to read and less error-prone than concatenation (raw/javascriptallonge.pdf p.202-204).

## Technical details

### `technical-atom-f23cad1b7f7aa532` code

Citation: (raw/javascriptallonge.pdf p.202-204)

```
Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.
```

### `technical-atom-af799f408a4345ac` code

Citation: (raw/javascriptallonge.pdf p.202-204)

```
- `A popular number for nerds is ${ 40 + 2 } `
```

### `technical-atom-39e7cdcc65fdfad1` code

Citation: (raw/javascriptallonge.pdf p.202-204)

```javascript
const name = "Harry";
```

### `technical-atom-6f1d22740b2fdf1a` code

Citation: (raw/javascriptallonge.pdf p.202-204)

```javascript
const greeting = (name) => `Hello my name is ${ name } `;
```

### `technical-atom-a32be0775921071c` code

Citation: (raw/javascriptallonge.pdf p.202-204)

```javascript
const greeting = (name) => 'Hello my name is ' + name;
```

### `technical-atom-299193afddbc36a1` code

Citation: (raw/javascriptallonge.pdf p.202-204)

```
Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}.
```

### `technical-atom-ef64506ba69ec339` procedure

Citation: (raw/javascriptallonge.pdf p.202-204)

The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

### `technical-atom-141514acb8272695` worked-example

Citation: (raw/javascriptallonge.pdf p.202-204)

For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line'.

## Related technical details

### From [[javascriptallonge-iteration-and-iterables]]: `technical-atom-be126e6eb38ca51a` code

Relation: nearby source page; matched terms `code`, `function`, `javascript`, `method`, `what`, `when`

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is defined with a fat arrow () => { ... }. What is the value of this within that function?
```

### From [[javascriptallonge-iteration-and-iterables]]: `technical-atom-d3b675be6d62eed9` code

Relation: nearby source page; matched terms `code`, `function`, `has`, `javascript`, `method`

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that’s where this is bound to the value of stack.
```

### From [[javascriptallonge-why]]: `technical-atom-dff96b94ef792fdf` exception

Relation: nearby source page; matched terms `has`, `javascript`

Citation: (raw/javascriptallonge.pdf p.201)

This has little practical utility in JavaScript, but in combinatory logic it’s essential: With fixed-point combinators it’s possible to compute everything computable without binding names.

### From [[javascriptallonge-mapwith]]: `technical-atom-49f118af13215ae0` code

Relation: nearby source page; matched terms `back`, `can`, `code`, `function`, `writing`

Citation: (raw/javascriptallonge.pdf p.193-194)

```javascript
That means that you can pass a function to mapWith and get back a function that applies that mapping to any array. For example, we might need a function to return the squares of an array. Instead of writing a a wrapper around .map:
```
