---
page_id: javascriptallonge-closures-and-scope
page_kind: source
summary: Closures and Scope from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.44-48
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on closures and scope from JavaScript Allongé.

## Key supported claims

- Functions that contain free variables are called closures (raw/javascriptallonge.pdf p.44-48).
- Pure functions are easiest to understand because they always mean the same thing (raw/javascriptallonge.pdf p.44-48).
- When a function is applied to arguments, its environment has a reference to its parent environment (raw/javascriptallonge.pdf p.44-48).
- Variables in a function's scope shadow variables in parent scopes if they have the same name (raw/javascriptallonge.pdf p.44-48).
- JavaScript has a global environment, and code can be wrapped in an IIFE to create a local environment (raw/javascriptallonge.pdf p.44-48).

## Technical details

### `technical-atom-11aaefbbc6b93bf3` code

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
The environment belonging to the function with signature (x) => ... becomes {x: 1, ...}, and the result of applying the function is another function value. It makes sense that the result value is a function, because the expression for (x) => ...’s body is:
```

### `technical-atom-0b09d56701da7fc0` code

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
So we seem to get a new environment {y: 2, ...}. How is the expression x going to be evaluated in that function’s environment? There is no x in its environment, it must come from somewhere else.
```

### `technical-atom-18f67c085760f2dd` code

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
lambda { |x| lambda { |y| x } }[1][2] #=> 1
```

### `technical-atom-58f9184c287b83f5` code

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
The function (y) => x is interesting. It contains a free variable, x.[27] A free variable is one that is not bound within the function. Up to now, we’ve only seen one way to “bind” a variable, namely by passing in an argument with the same name. Since the function (y) => x doesn’t have an argument named x, the variable x isn’t bound in this function, which makes it “free.”
```

### `technical-atom-bd2f4a6b2c266e9d` code

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
## () => {}
```

### `technical-atom-6ef9e0d67016949b` code

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => ....
```

### `technical-atom-6f035a06fb85b432` code

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.
```

### `technical-atom-1f3d003d4d7f3e47` code

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
To understand how closures are evaluated, we need to revisit environments. As we’ve said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...}? Let’s fill in the blanks!
```

## Related technical details

### From [[javascriptallonge-that-constant-coffee-craving]]: `technical-atom-e75668d22e5ff80b` code

Relation: nearby source page; matched terms `can`, `code`, `evaluated`, `function`, `functions`, `has`

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our “functions” are expressions. This one has a few more moving parts, that’s all. But we can use it just like (diameter) => diameter * 3.14159265.
```

### From [[javascriptallonge-ah-i-d-like-to-have-an-argument-please]]: `technical-atom-059258f79c64cecb` code

Relation: nearby source page; matched terms `can`, `code`, `contain`, `function`, `functions`, `have`

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
This loose definition is recursive, so we can intuit (or use our experience with other languages) that since a function can contain a return statement with an expression, we can write a function that returns a function, or an array that contains another array expression. Or a function that returns an array, an array of functions, a function that returns an array of functions, and so forth:
```

### From [[javascriptallonge-ah-i-d-like-to-have-an-argument-please]]: `technical-atom-07b4f982763531cb` code

Relation: nearby source page; matched terms `arguments`, `code`, `function`, `functions`, `have`

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
Expressions consist either of representations of values (like 3.14159265, true, and undefined), operators that combine expressions (like 3 + 2), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( arguments) { body-statements } for creating functions.
```

### From [[javascriptallonge-combinators-and-function-decorators]]: `technical-atom-4ec0e2f5cfc99090` code

Relation: nearby source page; matched terms `arguments`, `can`, `code`, `function`, `functions`, `javascript`

Citation: (raw/javascriptallonge.pdf p.68-70)

```javascript
As we’ve seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function.
```
