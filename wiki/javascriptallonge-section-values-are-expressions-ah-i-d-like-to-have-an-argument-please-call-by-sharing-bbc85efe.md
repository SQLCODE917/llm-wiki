---
page_id: javascriptallonge-section-values-are-expressions-ah-i-d-like-to-have-an-argument-please-call-by-sharing-bbc85efe
page_kind: source
summary: values are expressions / Ah. I'd Like to Have an Argument, Please. / call by sharing: 14 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-ah-i-d-like-to-have-an-argument-please-call-by-sharing-bbc85efe@1755920631a0c9378f3e4d5c908891ad
---

# values are expressions / Ah. I'd Like to Have an Argument, Please. / call by sharing

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-ah-i-d-like-to-have-an-argument-please-8d362ee7]] - broader source section

## Statements

- At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. _(javascriptallonge.pdf (source-range-83ecb080-00353))_
- Now it is time to take another look at the distinction between value and reference types. _(javascriptallonge.pdf (source-range-83ecb080-00353))_
- Earlier, we distinguished JavaScript’s _value types_ from its _reference types_ . _(javascriptallonge.pdf (source-range-83ecb080-00353))_
- There is a property that JavaScript strictly maintains: When a value–any value–is passed as an argument to a function, the value bound in the function’s environment must be identical to the original. _(javascriptallonge.pdf (source-range-83ecb080-00354))_
- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00355))_
- Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. _(javascriptallonge.pdf (source-range-83ecb080-00355))_
- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00355))_
- 20 are identical to each other if they have the same content. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- JavaScript does not place copies of reference values in any environment. _(javascriptallonge.pdf (source-range-83ecb080-00359))_
- JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-83ecb080-00359))_
- Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. _(javascriptallonge.pdf (source-range-83ecb080-00360))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-83ecb080-00360))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-83ecb080-00360))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00355, source-range-83ecb080-00360))_

> We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally unders

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00358))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.
