---
page_id: javascriptallonge-closures-and-scope
page_kind: source
summary: Closures and Scope from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.44-44
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Summary of closures and scope concepts from JavaScript Allongé, covering free variables, closures, and environments.

## Key supported claims

- JavaScript allows functions to nest inside each other, and handles variables from 'outside' of a function that are referenced inside a function (raw/javascriptallonge.pdf p.44-44)
- The result of applying a function is a function when the expression body is another function (raw/javascriptallonge.pdf p.44-44)
- A value representing a function is created when a function is applied (raw/javascriptallonge.pdf p.44-44)

## Technical details

### `technical-atom-cf47f677a69883d2` code

Citation: (raw/javascriptallonge.pdf p.44)

```javascript
((x) => (y) => x)(1)(2) //=> 1
```

### `technical-atom-3901b4e4086be335` code

Citation: (raw/javascriptallonge.pdf p.44)

```javascript
((x) => (y) => x)(1) //=> [Function]
```

### `technical-atom-8836aeccf0c6bdd2` code

Citation: (raw/javascriptallonge.pdf p.44)

```javascript
(y) => x
```

### `technical-atom-d7f1182c8b1a42ac` code

Citation: (raw/javascriptallonge.pdf p.44)

```javascript
((y) => x)(2)
```

### `technical-atom-0dd7b0535b6b9710` code

Citation: (raw/javascriptallonge.pdf p.44)

```javascript
lambda { |x| lambda { |y| x } }[1][2] #=> 1
```

### `technical-atom-ab8524c9d5fcc7c0` code

Citation: (raw/javascriptallonge.pdf p.44)

```
becomes {x: 1, ...} , and the result of applying the function is another function value.
```

### `technical-atom-026e41457ce3d8a0` code

Citation: (raw/javascriptallonge.pdf p.44)

```
So we seem to get a new environment {y: 2, ...} .
```

### `technical-atom-6e3151115dfb385f` procedure

Citation: (raw/javascriptallonge.pdf p.44)

Then we're going to take the value of that function and apply it to the argument 2 , something like this:

## Related technical details

### From [[javascriptallonge-call-by-sharing]]: `technical-atom-247ce19e93a86869` requirement

Relation: nearby source page; matched terms `function`, `javascript`, `value`, `when`

Citation: (raw/javascriptallonge.pdf p.42-43)

There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original.

### From [[javascriptallonge-it-s-always-the-environment]]: `technical-atom-6582cc9837c81ff3` requirement

Relation: nearby source page; matched terms `applied`, `function`

Citation: (raw/javascriptallonge.pdf p.46-47)

So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### From [[javascriptallonge-call-by-sharing]]: `technical-atom-e8199c3947c572cb` requirement

Relation: nearby source page; matched terms `closures`, `function`, `value`, `when`

Citation: (raw/javascriptallonge.pdf p.42-43)

When we combine our knowledge of value types, reference types, arguments, and closures, we'll understand why this function always evaluates to true no matter what argument 26 you apply it to:

### From [[javascriptallonge-shadowy-variables-from-a-shadowy-planet]]: `technical-atom-592864b8cc8594c9` procedure

Relation: nearby source page; matched terms `each`, `functions`, `javascript`, `variables`

Citation: (raw/javascriptallonge.pdf p.47)

JavaScript always searches for a binding starting with the functions own environment and then each parent in turn until it finds one.
