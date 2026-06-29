---
page_id: javascriptallonge-section-truthiness-and-the-ternary-operator-6520cd73
page_kind: source
summary: truthiness and the ternary operator: 16 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-truthiness-and-the-ternary-operator-6520cd73@5aa76e68cd2e66e7afd8dc217208dc67
---

# truthiness and the ternary operator

From [[javascriptallonge]].

## Statements

- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-8eb13d6b-00765))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-8eb13d6b-00766))_
- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This affects the way the ! , && , and || operators work. We'll look at them in a moment, but first, we'll look at one more operator. _(javascriptallonge.pdf (source-range-8eb13d6b-00767))_
- JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-8eb13d6b-00768))_
- This is a lot like the if statement, however it is an expression , not a statement, and that can be very valuable. It also doesn't introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements. _(javascriptallonge.pdf (source-range-8eb13d6b-00770))_
- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example: _(javascriptallonge.pdf (source-range-8eb13d6b-00773))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-8eb13d6b-00775))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . _(javascriptallonge.pdf (source-range-8eb13d6b-00766))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-8eb13d6b-00775))_

## Technical atoms

### Technical frame 1: truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00773))_

> The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00772))_

```
true ? 'Hello' : 'Good bye' //=> 'Hello' 0 ? 'Hello' : 'Good bye' //=> 'Good bye' [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' //=> 'Pentatonic'
```

### Technical frame 2: truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00775))_

> Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00774))_

```
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den';
```
