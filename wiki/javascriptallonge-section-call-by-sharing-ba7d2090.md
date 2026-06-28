---
page_id: javascriptallonge-section-call-by-sharing-ba7d2090
page_kind: source
summary: call by sharing: 17 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-call-by-sharing-ba7d2090@6a377021ae46de9ac4bc1c87dbf54db6
---

# call by sharing

From [[javascriptallonge]].

## Statements

- Earlier, we distinguished JavaScript's value types from its reference types . At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. Now it is time to take another look at the distinction between value and reference types. _(javascriptallonge.pdf (source-range-31a4cf47-00323))_
- There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original. _(javascriptallonge.pdf (source-range-31a4cf47-00324))_
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-31a4cf47-00325))_
- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-31a4cf47-00327))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement 'call by sharing' semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. _(javascriptallonge.pdf (source-range-31a4cf47-00328))_
- 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL. _(javascriptallonge.pdf (source-range-31a4cf47-00331))_
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-31a4cf47-00325))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement 'call by sharing' semantics. _(javascriptallonge.pdf (source-range-31a4cf47-00328))_
- 26 Unless the argument is NaN , which isn't equal to anything, including itself . _(javascriptallonge.pdf (source-range-31a4cf47-00331))_

## Technical atoms

### Technical frame 1: call by sharing

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00327))_

> Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00325))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

### Technical frame 2: call by sharing

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00331))_

> 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00330))_

```
(value) => ((ref1, ref2) => ref1 === ref2)(value, value)
```
