---
page_id: javascriptallonge-section-truthiness-and-the-ternary-operator-f442a22e
page_kind: source
summary: **truthiness and the ternary operator**: 18 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-truthiness-and-the-ternary-operator-f442a22e@786ee5070f8d594557b9f57338fba8dc
---

# **truthiness and the ternary operator**

From [[javascriptallonge]].

## Statements

- So are null and undefined, values that semantically represent “no value.” NaN is falsy, a value representing the result of a calculation that is not a number.[54] And there are more: 0 is falsy, a value representing “none of something.” The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-83ecb080-01105))_
- In JavaScript, there is a notion of “truthiness.” Every value is either “truthy” or “falsy.” Obviously, false is falsy. _(javascriptallonge.pdf (source-range-83ecb080-01105))_
- Every other value in JavaScript is “truthy” except the aforementioned false, null, undefined, NaN, 0, and ''. _(javascriptallonge.pdf (source-range-83ecb080-01106))_
- (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-83ecb080-01106))_
- Every other value in JavaScript is “truthy” except the aforementioned false, null, undefined, NaN, 0, and ''. _(javascriptallonge.pdf (source-range-83ecb080-01106))_
- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on _truthiness_ , not on boolean values. _(javascriptallonge.pdf (source-range-83ecb080-01107))_
- JavaScript inherited an operator from the C family of languages, the _ternary_ operator. _(javascriptallonge.pdf (source-range-83ecb080-01108))_
- It’s the only operator that takes _three_ arguments. _(javascriptallonge.pdf (source-range-83ecb080-01108))_
- and if first is “truthy”, it evaluates second and that is its value. _(javascriptallonge.pdf (source-range-83ecb080-01112))_
- If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-83ecb080-01112))_
- This is a lot like the if statement, however it is an _expression_ , not a statement, and that can be very valuable. _(javascriptallonge.pdf (source-range-83ecb080-01113))_
- It also doesn’t introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements. _(javascriptallonge.pdf (source-range-83ecb080-01113))_
- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. _(javascriptallonge.pdf (source-range-83ecb080-01119))_
- We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. _(javascriptallonge.pdf (source-range-83ecb080-01121))_
- We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. _(javascriptallonge.pdf (source-range-83ecb080-01121))_

## Technical atoms

> Context: Here’re some simple examples of the ternary operator:
_(context: javascriptallonge.pdf (source-range-83ecb080-01114))_

> - 0 ? 'Hello' : 'Good bye' _//=> 'Good bye'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01117))_

> - [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' _//=> 'Pentatonic'_
_(source: javascriptallonge.pdf (source-range-83ecb080-01118))_

> Context: The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01119))_

> **const** status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den';
_(source: javascriptallonge.pdf (source-range-83ecb080-01120))_
