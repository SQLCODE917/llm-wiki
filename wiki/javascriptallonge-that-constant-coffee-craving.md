---
page_id: javascriptallonge-that-constant-coffee-craving
page_kind: source
summary: That Constant Coffee Craving from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.49-61
updated: 2026-06-25
source_id: javascriptallonge.pdf
---

## Source record

Chapter on naming functions and lexical scoping in JavaScript, introducing const and IIFEs.

## Key supported claims

- IIFEs bind values in expressions, like ((PI) => (diameter) => diameter * PI )(3.14159265) (raw/javascriptallonge.pdf p.49-61).
- The const keyword binds names in blocks without invocation cost, such as (diameter) => { const PI = 3.14159265; return diameter * PI } (raw/javascriptallonge.pdf p.49-61).
- Const names use lexical scoping, shadowing outer bindings in nested scopes (raw/javascriptallonge.pdf p.49-61).
- Magic literals like 3.14159265 are anathema to sustainable development (raw/javascriptallonge.pdf p.49-61).
- Names bound with const are only ever seen in their lexical scope (raw/javascriptallonge.pdf p.49-61).

## Technical details

### `technical-atom-f3d4ec8fd778fe12` code

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
(diameter) => diameter * 3.14159265
```

### `technical-atom-8844e7fc14cbe5ea` code

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
(diameter) => diameter * PI
```

### `technical-atom-89c425d2c3cd45d9` code

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
((PI) => // ????)(3.14159265)
```

### `technical-atom-1e78c3033caab42f` code

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
((PI) => (diameter) => diameter * PI)(3.14159265)
```

### `technical-atom-e75668d22e5ff80b` code

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our “functions” are expressions. This one has a few more moving parts, that’s all. But we can use it just like (diameter) => diameter * 3.14159265.
```

### `technical-atom-d27cd2f7548a48fd` code

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
((diameter) => diameter * 3.14159265)(2) //=> 6.2831853
```

### `technical-atom-557b2640917f78cc` code

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
((PI) => (diameter) => diameter * PI)(3.14159265)(2) //=> 6.2831853
```

### `technical-atom-30ece2f7b2390b03` code

Citation: (raw/javascriptallonge.pdf p.49-61)

```javascript
(diameter) => ((PI) => diameter * PI)(3.14159265)
```

## Related technical details

### From [[javascriptallonge-closures-and-scope]]: `technical-atom-58f9184c287b83f5` code

Relation: nearby source page; matched terms `bind`, `bound`, `function`, `name`, `now`, `one`

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
The function (y) => x is interesting. It contains a free variable, x.[27] A free variable is one that is not bound within the function. Up to now, we’ve only seen one way to “bind” a variable, namely by passing in an argument with the same name. Since the function (y) => x doesn’t have an argument named x, the variable x isn’t bound in this function, which makes it “free.”
```

### From [[javascriptallonge-ah-i-d-like-to-have-an-argument-please]]: `technical-atom-07b4f982763531cb` code

Relation: nearby source page; matched terms `expressions`, `function`, `functions`, `like`, `values`

Citation: (raw/javascriptallonge.pdf p.39-43)

```javascript
Expressions consist either of representations of values (like 3.14159265, true, and undefined), operators that combine expressions (like 3 + 2), some special forms like [1, 2, 3] for creating arrays out of expressions, or function ( arguments) { body-statements } for creating functions.
```

### From [[javascriptallonge-closures-and-scope]]: `technical-atom-6ef9e0d67016949b` code

Relation: nearby source page; matched terms `bound`, `function`, `functions`, `one`, `only`, `other`

Citation: (raw/javascriptallonge.pdf p.44-48)

```javascript
The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => ....
```

### From [[javascriptallonge-naming-functions]]: `technical-atom-e6e76a5e6be15c59` code

Relation: nearby source page; matched terms `function`, `functions`, `keyword`, `naming`, `our`, `return`

Citation: (raw/javascriptallonge.pdf p.62-67)

```javascript
5. We always use a block, we cannot write function (str) str + str. This means that if we want our functions to return a value, we always need to use the return keyword
```
