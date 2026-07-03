---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-d8796156
page_kind: source
page_family: section-reference
summary: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: 15 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-d8796156@f0eedc4eed2866b6b51fa990b69a2484
---

# Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-d45c6f89]] - broader source section: Picking the Bean: Choice and Truthiness

## Statements

- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-7239e085-00765))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-7239e085-00766))_
- JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-7239e085-00768))_
- This is a lot like the if statement, however it is an expression , not a statement, and that can be very valuable. It also doesn't introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements. _(javascriptallonge.pdf (source-range-7239e085-00770))_
- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example: _(javascriptallonge.pdf (source-range-7239e085-00773))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-7239e085-00775))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . _(javascriptallonge.pdf (source-range-7239e085-00766))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-7239e085-00775))_
