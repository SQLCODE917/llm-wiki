---
page_id: javascriptallonge-section-call-by-sharing-50815870
page_kind: source
summary: **call by sharing**: 16 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-call-by-sharing-50815870@15d18c5de1b812e0dfaa2e4cd5d733fd
---

# **call by sharing**

From [[javascriptallonge]].

## Statements

- Now it is time to take another look at the distinction between value and reference types. _(javascriptallonge.pdf (source-range-83ecb080-00453))_
- At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. _(javascriptallonge.pdf (source-range-83ecb080-00453))_
- Earlier, we distinguished JavaScript’s _value types_ from its _reference types_ . _(javascriptallonge.pdf (source-range-83ecb080-00453))_
- There is a property that JavaScript strictly maintains: When a value–any value–is passed as an argument to a function, the value bound in the function’s environment must be identical to the original. _(javascriptallonge.pdf (source-range-83ecb080-00454))_
- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- JavaScript does not place copies of reference values in any environment. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. _(javascriptallonge.pdf (source-range-83ecb080-00461))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-83ecb080-00461))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-83ecb080-00461))_
- > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . _(javascriptallonge.pdf (source-range-83ecb080-00465))_
- > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . _(javascriptallonge.pdf (source-range-83ecb080-00465))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00461))_

> Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00459))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00462))_

> And with that, we’re ready to look at _closures_ . When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00464))_

> - ((ref1, ref2) => ref1 === ref2)(value, value)
