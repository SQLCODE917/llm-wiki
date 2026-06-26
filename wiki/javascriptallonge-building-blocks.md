---
page_id: javascriptallonge-building-blocks
page_kind: source
summary: Building Blocks from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.71-73
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter covers basic building blocks in JavaScript, focusing on composition and partial application.

## Key supported claims

- JavaScript functions can be composed by chaining them together, as shown with cookAndEat = (food) => eat(cook(food)) (raw/javascriptallonge.pdf p.71-73).
- Composition can be generalized using a compose combinator, like compose = (a, b) => (c) => a(b(c)) (raw/javascriptallonge.pdf p.71-73).
- Partial application is a building block where a function is applied to some, but not all, of its arguments, resulting in a new function (raw/javascriptallonge.pdf p.71-73).

## Technical details

### `technical-atom-91311a5ace51742a` code

Citation: (raw/javascriptallonge.pdf p.71-73)

```javascript
const cookAndEat = (food) => eat(cook(food));
```

### `technical-atom-e9b4c964109aba6c` code

Citation: (raw/javascriptallonge.pdf p.71-73)

```javascript
const compose = (a, b) => (c) => a(b(c));
```

### `technical-atom-9c2016aadbdfddbf` code

Citation: (raw/javascriptallonge.pdf p.71-73)

```javascript
const cookAndEat = compose(eat, cook);
```

### `technical-atom-4793a64cb9af7a48` code

Citation: (raw/javascriptallonge.pdf p.71-73)

```javascript
const invokeTransfer = once(maybe(actuallyTransfer(...)));
```

### `technical-atom-cc7f0e20542b4dff` code

Citation: (raw/javascriptallonge.pdf p.71-73)

```javascript
This code implements a partial application of the map function by applying the function (n) => n * n as its second argument:
```

### `technical-atom-b2c8a2ee6fc47ae0` code

Citation: (raw/javascriptallonge.pdf p.71-73)

```javascript
const squareAll = (array) => map(array, (n) => n * n);
```

### `technical-atom-a8de28c0caf59533` code

Citation: (raw/javascriptallonge.pdf p.71-73)

```javascript
const mapWith = (fn) => (array) => map(array, fn);
```

### `technical-atom-d603aa51bcdad457` code

Citation: (raw/javascriptallonge.pdf p.71-73)

```javascript
const squareAll = mapWith((n) => n * n);
```

## Related technical details

### From [[javascriptallonge-combinators-and-function-decorators]]: `technical-atom-4ec0e2f5cfc99090` code

Relation: nearby source page; matched terms `arguments`, `can`, `function`, `functions`, `javascript`

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
As we’ve seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function.
```

### From [[javascriptallonge-closures-and-scope]]: `technical-atom-6f035a06fb85b432` code

Relation: nearby source page; matched terms `all`, `arguments`, `but`, `can`, `function`, `functions`

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.
```

### From [[javascriptallonge-partial-application]]: `technical-atom-a4e2222067936b67` procedure

Relation: nearby source page; matched terms `application`, `can`, `partial`

Citation: (raw/javascriptallonge.pdf p.80-81)

We take it a step further, and can use gathering and spreading to allow for partial application with more than one argument:

### From [[javascriptallonge-that-constant-coffee-craving]]: `technical-atom-e75668d22e5ff80b` code

Relation: nearby source page; matched terms `all`, `but`, `can`, `function`, `functions`, `like`

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our “functions” are expressions. This one has a few more moving parts, that’s all. But we can use it just like (diameter) => diameter * 3.14159265.
```
