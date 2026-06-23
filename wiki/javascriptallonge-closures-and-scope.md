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

### `technical-atom-6e3151115dfb385f` procedure

Citation: (raw/javascriptallonge.pdf p.44)

Then we're going to take the value of that function and apply it to the argument 2 , something like this:

### `technical-atom-026e41457ce3d8a0` code

Citation: (raw/javascriptallonge.pdf p.44)

```
So we seem to get a new environment {y: 2, ...} .
```
