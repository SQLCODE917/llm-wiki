---
page_id: javascriptallonge-why
page_kind: source
summary: Why? from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.201-201
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter 47 of JavaScript Allongé, 'Why?', covering the Y Combinator and its role in functional programming.

## Key supported claims

- The Y Combinator enables recursive functions without binding to names in JavaScript, useful in combinatory logic (raw/javascriptallonge.pdf p.201-201).
- The Y Combinator has practical applications and is useful for understanding combinatory logic (raw/javascriptallonge.pdf p.201-201).
- The joy of working things out is emphasized when learning the Y Combinator (raw/javascriptallonge.pdf p.201-201).

## Technical details

### `technical-atom-4b3d2141ac2db208` code

Citation: (raw/javascriptallonge.pdf p.201)

```javascript
const Y = (f) => ( x => f(v => x(x)(v)))( x => f(v => x(x)(v)));
```

### `technical-atom-1131be1317bdb5fe` code

Citation: (raw/javascriptallonge.pdf p.201)

```javascript
const factorial = Y( function (fac) { return function (n) { return (n == 0 ? 1: n * fac(n - 1)); } }); factorial(5) //=> 120
```

### `technical-atom-bbb8ada0d2cf8387` code

Citation: (raw/javascriptallonge.pdf p.201)

```javascript
const Y = (f) => { const something = x => f(v => x(x)(v));
```

### `technical-atom-e733b0e7333b4559` code

Citation: (raw/javascriptallonge.pdf p.201)

```
return something(something); };
```

### `technical-atom-0ed67642d112bed9` code

Citation: (raw/javascriptallonge.pdf p.201)

```javascript
const factorial = Y( function (fac) { return function (n) { return (n == 0 ?
```

### `technical-atom-e050bf725570ce45` exception

Citation: (raw/javascriptallonge.pdf p.201)

It enables you to make recursive functions without needing to bind a function to a name in an environment.

### `technical-atom-dff96b94ef792fdf` exception

Citation: (raw/javascriptallonge.pdf p.201)

This has little practical utility in JavaScript, but in combinatory logic it’s essential: With fixed-point combinators it’s possible to compute everything computable without binding names.

### `technical-atom-fb389bc6a4c37326` worked-example

Citation: (raw/javascriptallonge.pdf p.201)

For example, you could start by writing:

## Related technical details

### From [[javascriptallonge-iteration-and-iterables]]: `technical-atom-d3b675be6d62eed9` code

Relation: nearby source page; matched terms `function`, `has`, `its`, `javascript`

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
Since JavaScript doesn’t bind this within a fat arrow function, we follow the same rules of variable scoping as any other variable name: We check in the environment enclosing the function. Although the .iterator() method has returned, its environment is the one that encloses our () => { ... } function, and that’s where this is bound to the value of stack.
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-cd36d849b171aa54` code

Relation: nearby source page; matched terms `function`, `functions`, `identity`, `out`, `useful`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
The identity function is a function that evaluates to whatever parameter you pass it. So I(42) => 42. Very simple, but useful. Now we’ll take it one more step forward: Passing a value to K gets a function back, and passing a value to that function gets us a value.
```

### From [[javascriptallonge-iteration-and-iterables]]: `technical-atom-be126e6eb38ca51a` code

Relation: nearby source page; matched terms `function`, `javascript`, `when`

Citation: (raw/javascriptallonge.pdf p.206-223)

```javascript
The .iterator() method is defined with shorthand equivalent to iterator: function iterator() { ... }. Note that it uses the function keyword, so when we invoke it with stack.iterator(), JavaScript sets this to the value of stack. But what about the function .iterator() returns? It is defined with a fat arrow () => { ... }. What is the value of this within that function?
```

### From [[javascriptallonge-making-data-out-of-functions]]: `technical-atom-aea76708de48efca` code

Relation: nearby source page; matched terms `function`, `functions`, `out`

Citation: (raw/javascriptallonge.pdf p.177-190)

```javascript
A constant function is a function that always returns the same thing, no matter what you give it. For example, (x) => 42 is a constant function that always evaluates to 42. The kestrel, or K, is a function that makes constant functions. You give it a value, and it returns a constant function that gives that value.
```
