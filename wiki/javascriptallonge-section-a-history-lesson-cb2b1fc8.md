---
page_id: javascriptallonge-section-a-history-lesson-cb2b1fc8
page_kind: source
summary: a history lesson: 5 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-a-history-lesson-cb2b1fc8@14d46201dac8eaa8e5b6e8b907197832
---

# a history lesson

From [[javascriptallonge]].

## Statements

- In 'Ye Olde Days,' 53 JavaScript could not gather parameters, and we had to either do backflips with arguments and .slice , or we wrote ourselves a variadic decorator that could gather arguments into the last declared parameter. Here it is in all of its ECMAScript-5 glory: _(javascriptallonge.pdf (source-range-31a4cf47-00725))_
- This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument. _(javascriptallonge.pdf (source-range-31a4cf47-00731))_

## Technical atoms

### Technical frame 1: a history lesson

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00726))_

```
var __slice = Array.prototype.slice; function rightVariadic (fn) { if (fn.length < 1) return fn; return function () { var ordinaryArgs = (1 <= arguments.length ? __slice.call(arguments, 0, fn.length - 1) : []), restOfTheArgsList = __slice.call(arguments, fn.length - 1), args = (fn.length <= arguments.length ? ordinaryArgs.concat([restOfTheArgsList]) : []); return fn.apply( this , args); } }; var firstAndButFirst = rightVariadic( function test (first, butFirst) { return [first, butFirst] }); firstAndButFirst('why', 'hello', 'there', 'little', 'droid') //=> ["why",["hello","there","little","droid"]]
```

### Technical frame 2: a history lesson

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00729))_

```
var firstAndButFirst = rightVariadic( function test (first, butFirst) { return [first, butFirst] }); We now simply write: const firstAndButFirst = (first, ...butFirst) [first, butFirst];
```

### Technical frame 3: a history lesson

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00731))_

> This is a right-variadic function , meaning that it has one or more fixed arguments, and the rest are gathered into the rightmost argument.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00730))_

```
=>
```
