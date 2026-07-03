---
page_id: javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-sharing-96a55cff
page_kind: source
page_family: section-reference
summary: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: 17 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-sharing-96a55cff@ac00d5985f2b61c5b66fc262ca382454
---

# And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-f00edd2f]] - broader source section: And also: / Ah. I'd Like to Have an Argument, Please. 22

## Statements

- Earlier, we distinguished JavaScript's value types from its reference types . At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. Now it is time to take another look at the distinction between value and reference types. _(javascriptallonge.pdf (source-range-7239e085-00320))_
- There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original. _(javascriptallonge.pdf (source-range-7239e085-00321))_
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-7239e085-00322))_
- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-7239e085-00324))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement 'call by sharing' semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. _(javascriptallonge.pdf (source-range-7239e085-00325))_
- 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL. _(javascriptallonge.pdf (source-range-7239e085-00328))_
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-7239e085-00322))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement 'call by sharing' semantics. _(javascriptallonge.pdf (source-range-7239e085-00325))_
- 26 Unless the argument is NaN , which isn't equal to anything, including itself . _(javascriptallonge.pdf (source-range-7239e085-00328))_
