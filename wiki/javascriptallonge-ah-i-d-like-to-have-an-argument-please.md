---
page_id: javascriptallonge-ah-i-d-like-to-have-an-argument-please
page_kind: source
summary: Ah. I'd Like to Have an Argument, Please. from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.39-43
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

This chapter discusses functions with arguments and evaluation strategies in JavaScript, including call by value and call by sharing.

## Key supported claims

- Functions can have arguments, such as (room) => {} or (room, board) => {} (raw/javascriptallonge.pdf p.39-43).
- JavaScript uses call by value evaluation strategy, where expressions are evaluated before being passed to functions (raw/javascriptallonge.pdf p.39-43).
- Functions can return other functions, and arguments and variables work similarly in nested functions (raw/javascriptallonge.pdf p.39-43).

## Technical details

### `technical-atom-fc1c8a714e491c05` code

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
(room) => {}
```

### `technical-atom-8359bd4539950c44` code

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
(room, board) => {}
```

### `technical-atom-81a9f5130a4963ab` code

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
(diameter) => diameter * 3.14159265
```

### `technical-atom-e6905bb92a6660b7` code

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
Remember that to apply a function with no arguments, we wrote (() => {})(). To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this:
```

### `technical-atom-b25868d951dcbf46` code

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
((diameter) => diameter * 3.14159265)(2)
```

### `technical-atom-becfdb70c59dc94b` code

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
((room, board) => room + board)(800, 150)
```

### `technical-atom-07b4f982763531cb` code

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
Expressions consist either of representations of values (like 3.14159265, true, and undefined), operators that combine expressions (like 3 + 2), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( arguments) { body-statements } for creating functions.
```

### `technical-atom-059258f79c64cecb` code

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
This loose definition is recursive, so we can intuit (or use our experience with other languages) that since a function can contain a return statement with an expression, we can write a function that returns a function, or an array that contains another array expression. Or a function that returns an array, an array of functions, a function that returns an array of functions, and so forth:
```

## Related technical details

### From [[javascriptallonge-combinators-and-function-decorators]]: `technical-atom-4ec0e2f5cfc99090` code

Relation: nearby source page; matched terms `arguments`, `can`, `function`, `functions`, `javascript`, `return`

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
As we’ve seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function.
```

### From [[javascriptallonge-that-constant-coffee-craving]]: `technical-atom-e75668d22e5ff80b` code

Relation: nearby source page; matched terms `can`, `evaluated`, `expressions`, `function`, `functions`, `like`

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our “functions” are expressions. This one has a few more moving parts, that’s all. But we can use it just like (diameter) => diameter * 3.14159265.
```

### From [[javascriptallonge-closures-and-scope]]: `technical-atom-58f9184c287b83f5` code

Relation: nearby source page; matched terms `argument`, `function`, `have`

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
The function (y) => x is interesting. It contains a free variable, x.[27] A free variable is one that is not bound within the function. Up to now, we’ve only seen one way to “bind” a variable, namely by passing in an argument with the same name. Since the function (y) => x doesn’t have an argument named x, the variable x isn’t bound in this function, which makes it “free.”
```

### From [[javascriptallonge-closures-and-scope]]: `technical-atom-6ef9e0d67016949b` code

Relation: nearby source page; matched terms `function`, `functions`, `have`, `other`, `variables`

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => ....
```
