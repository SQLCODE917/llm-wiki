---
page_id: javascriptallonge-section-ah-i-d-like-to-have-an-argument-please-428fd20a
page_kind: source
page_family: section-reference
summary: Ah. I'd Like to Have an Argument, Please.: 6 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-ah-i-d-like-to-have-an-argument-please-428fd20a@16e50879d0f7028c98024235d970dfda
---

# Ah. I'd Like to Have an Argument, Please.

From [[javascriptallonge]].

## Statements

- The first sip: Basic Functions 

20 

are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. 

What about reference types? JavaScript does not place copies of reference values in any environment. JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. 

Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. 

And with that, we’re ready to look at _closures_ . When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to: 

(value) => 

- ((ref1, ref2) => ref1 === ref2)(value, value) 

> 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . NaN in JavaScript behaves a lot like NULL in SQL. _(javascriptallonge.pdf (source-range-af806fb1-00053))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-af806fb1-00053))_
