---
page_id: javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-a-history-lesson-7dceb2fe
page_kind: source
summary: Recipes with Basic Functions / Left-Variadic Functions / a history lesson: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-a-history-lesson-7dceb2fe@a3fec3e7a67f25d172f06b8fecd921ae
---

# Recipes with Basic Functions / Left-Variadic Functions / a history lesson

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-recipes-with-basic-functions-left-variadic-functions-d00f2bc0]] - broader source section: Recipes with Basic Functions / Left-Variadic Functions

## Statements

- In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory: _(javascriptallonge.pdf (source-range-7239e085-00725))_
- This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument. _(javascriptallonge.pdf (source-range-7239e085-00731))_

## Technical atoms

### Technical frame 1: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00726))_

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

### Technical frame 2: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00729))_

```
var firstAndButFirst = rightVariadic(
function test (first, butFirst) {
return [first, butFirst]
});
We now simply write:
const firstAndButFirst = (first, ...butFirst)
[first, butFirst];
```

### Technical frame 3: Recipes with Basic Functions / Left-Variadic Functions / a history lesson

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00730))_

```
=>
```
