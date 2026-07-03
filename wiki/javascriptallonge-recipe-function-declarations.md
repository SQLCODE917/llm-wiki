---
page_id: javascriptallonge-recipe-function-declarations
page_kind: recipe
page_family: recipe-pattern
summary: function declarations: reusable source-backed pattern with 7 statement(s) and 6 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: function-declarations
projection_coverage: recipe-javascriptallonge-recipe-function-declarations@c46329f16f6383cbe28edbcfff730efe
---

# function declarations

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-and-also-naming-functions-function-declarations-25fc9c63]].
- Evidence roles: decision, procedure, explanation, example.

## Applicability And Rationale

- There is another syntax for naming and/or defining a function. _(javascriptallonge.pdf (source-range-7239e085-00537))_
- First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-7239e085-00540))_
- However, there are two important differences. _(javascriptallonge.pdf (source-range-7239e085-00540))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-7239e085-00543))_
- The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). _(javascriptallonge.pdf (source-range-7239e085-00546))_
- This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. _(javascriptallonge.pdf (source-range-7239e085-00546))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00538)_

```
function someName () {
// ...
}
This behaves a little like:
const someName = function someName ()
// ...
}
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00539)_

```
{
```

### Atom 3: `worked-example`

_Source: javascriptallonge.pdf (source-range-7239e085-00541)_

```
Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const :
```

### Atom 4: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00542)_

```
(function () {
return fizzbuzz();
const fizzbuzz = function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> undefined is not a function (evaluating 'fizzbuzz()')
```

### Atom 5: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00544)_

```
(function () {
return fizzbuzz();
function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> 'FizzBuzz'
Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:
(function () {
const fizzbuzz = function fizzbuzz () {
```

### Atom 6: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00545)_

```
const fizzbuzz = function fizzbuzz ()
return "Fizz" + "Buzz";
}
return fizzbuzz();
})()
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-and-also-naming-functions-function-declarations-25fc9c63]]
