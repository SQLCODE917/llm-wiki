---
page_id: javascriptallonge-functions-that-return-values-and-evaluate-expressions
page_kind: source
summary: functions that return values and evaluate expressions from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf p.32-33
updated: 2026-06-23
source_id: javascriptallonge.pdf
---

## Source record

Chapter on functions that return values and evaluate expressions from JavaScript Allongé.

## Key supported claims

- We can make a function that returns a value by putting the value to the right of the arrow, as seen with (() => 0)() returning 0. (raw/javascriptallonge.pdf p.32-33)
- Values like 0 are expressions, as are things like 40 + 2, and we can put any expression to the right of the arrow. (raw/javascriptallonge.pdf p.32-33)
- Functions can return the value of evaluating another function, such as with (() => (() => 0)())() returning 0. (raw/javascriptallonge.pdf p.32-33)
- When dealing with expressions that have a lot of the same characters, formatting the code can help make things stand out. (raw/javascriptallonge.pdf p.32-33)
- It evaluates to the same thing, 0. (raw/javascriptallonge.pdf p.32-33)

## Technical details

### `technical-atom-053e216a0ba143de` code

Citation: (raw/javascriptallonge.pdf p.32-33)

```javascript
(() => 1)() //=> 1 (() => "Hello, JavaScript")() //=> "Hello, JavaScript" (() => Infinity )() //=> Infinity
```

### `technical-atom-b5a28ac67439659d` code

Citation: (raw/javascriptallonge.pdf p.32-33)

```javascript
(() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity )() //=> Infinity
```

### `technical-atom-1172baccc0a24ff7` code

Citation: (raw/javascriptallonge.pdf p.32-33)

```javascript
(() => (() => 0)())() //=> 0
```

### `technical-atom-be7839225be60f3a` code

Citation: (raw/javascriptallonge.pdf p.32-33)

```javascript
(() => (() => 0 )() )() //=> 0
```

### `technical-atom-3ac7bed3402992a5` worked-example

Citation: (raw/javascriptallonge.pdf p.32-33)

For example, (() => 0)() is an expression.

## Related technical details

### From [[javascriptallonge-void]]: `technical-atom-69ffa4ccd5f774da` code

Relation: nearby source page; matched terms `code`, `evaluating`, `function`, `return`, `value`

Citation: (raw/javascriptallonge.pdf p.35)

```
- By evaluating a function that doesn't return a value (() => {})() , and;
```

### From [[javascriptallonge-applying-functions]]: `technical-atom-b0a12df78d1155e0` exception

Relation: nearby source page; matched terms `expression`, `functions`, `one`, `right`, `such`

Citation: (raw/javascriptallonge.pdf p.31)

Right now, we only know about one such expression: () => 0 , so let's use it.

### From [[javascriptallonge-applying-functions]]: `technical-atom-a16c68b137f59cbe` requirement

Relation: nearby source page; matched terms `function`, `functions`, `have`

Citation: (raw/javascriptallonge.pdf p.31)

- function keyword functions always have blocks as their bodies.

### From [[javascriptallonge-as-little-as-possible-about-functions-but-no-less]]: `technical-atom-d5ce0404744a426c` code

Relation: nearby source page; matched terms `code`, `function`, `functions`

Citation: (raw/javascriptallonge.pdf p.30-31)

```javascript
(() => 0) //=> [Function]
```
