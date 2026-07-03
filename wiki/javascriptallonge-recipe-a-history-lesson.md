---
page_id: javascriptallonge-recipe-a-history-lesson
page_kind: recipe
page_family: recipe-pattern
summary: a history lesson: reusable source-backed pattern with 2 statement(s) and 3 technical atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: recipes/javascriptallonge
source_id: javascriptallonge.pdf
aliases: a-history-lesson
projection_coverage: recipe-javascriptallonge-recipe-a-history-lesson@f499282dcd3f5edcfb434ce21e019772
---

# a history lesson

From [[javascriptallonge]].

## Pattern

- Use the source-backed pattern described in [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-a-history-lesson-7dceb2fe]].
- Evidence roles: decision, constraint, example.

## Applicability And Rationale

- In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. _(javascriptallonge.pdf (source-range-7239e085-00725))_
- This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument. _(javascriptallonge.pdf (source-range-7239e085-00731))_

## Technical Atoms

### Atom 1: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00726)_

```
var __slice = Array.prototype.slice;
function rightVariadic (fn) {
if (fn.length < 1) return fn;
return function () {
var ordinaryArgs = (1 <= arguments.length ?
__slice.call(arguments, 0, fn.length - 1) : []),
restOfTheArgsList = __slice.call(arguments, fn.length - 1),
args = (fn.length <= arguments.length ?
ordinaryArgs.concat([restOfTheArgsList]) : []);
return fn.apply(this, args);
}
};
var firstAndButFirst = rightVariadic(function test (first, butFirst) {
return [first, butFirst]
});
firstAndButFirst('why', 'hello', 'there', 'little', 'droid')
//=> ["why",["hello","there","little","droid"]]
```

### Atom 2: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00729)_

```
var firstAndButFirst = rightVariadic(
function test (first, butFirst) {
return [first, butFirst]
});
We now simply write:
const firstAndButFirst = (first, ...butFirst)
[first, butFirst];
```

### Atom 3: `code-block`

_Source: javascriptallonge.pdf (source-range-7239e085-00730)_

```
=>
```

## Source Trail

- Source manifest: [[javascriptallonge]]
- Source section: [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-a-history-lesson-7dceb2fe]]
