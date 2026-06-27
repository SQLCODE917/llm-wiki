---
page_id: javascriptallonge-picking-bean-choice-and-truthiness
page_kind: concept
summary: Picking the Bean: Choice and Truthiness: 32 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-picking-bean-choice-and-truthiness@03db8a26293244f0d70de926f878cff2
---

# Picking the Bean: Choice and Truthiness

What [[javascriptallonge]] covers about picking the bean: choice and truthiness:

## Statements

_Showing 14 of 32 statements selected for this topic._

- and if first is “truthy”, it evaluates second and that is its value. _(javascriptallonge.pdf (source-range-83ecb080-01112))_
- They don’t operate strictly on logical values, and they don’t commute: a || b is not always equal to b || a, and the same goes for &&. _(javascriptallonge.pdf (source-range-83ecb080-01146))_
- The ternary operator (?:), ||, and && are control flow operators, they do not always return true or false, and they have short-cut semantics. _(javascriptallonge.pdf (source-range-83ecb080-01175))_
- true and false are value types. _(javascriptallonge.pdf (source-range-83ecb080-01097))_
- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on _truthiness_ , not on boolean values. _(javascriptallonge.pdf (source-range-83ecb080-01107))_
- It also doesn’t introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements. _(javascriptallonge.pdf (source-range-83ecb080-01113))_
- Our logical operators !, &&, and || are a little more subtle than our examples above implied. _(javascriptallonge.pdf (source-range-83ecb080-01123))_
- First, and unlike !, && and || do not necessarily evaluate to true or false. _(javascriptallonge.pdf (source-range-83ecb080-01133))_
- If we look at our examples above, we see that when we pass true and false to && and ||, we do indeed get true or false as a result. _(javascriptallonge.pdf (source-range-83ecb080-01140))_
- In contrast to the behaviour of the ternary operator, ||, and &&, function parameters are always : _eagerly evaluated_ _(javascriptallonge.pdf (source-range-83ecb080-01161))_
- We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. _(javascriptallonge.pdf (source-range-83ecb080-01097))_
- Now, note well: We have said what happens if you pass boolean values to !, &&, and ||, but we’ve said nothing about expressions or about passing other values. _(javascriptallonge.pdf (source-range-83ecb080-01103))_
- In JavaScript, there is a notion of “truthiness.” Every value is either “truthy” or “falsy.” Obviously, false is falsy. _(javascriptallonge.pdf (source-range-83ecb080-01105))_
- Every other value in JavaScript is “truthy” except the aforementioned false, null, undefined, NaN, 0, and ''. _(javascriptallonge.pdf (source-range-83ecb080-01106))_

## Technical atoms

_Showing 6 of 10 technical atoms selected for this topic._

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01097))_

> true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. To being with, ! is a unary prefix operator that negates its argument. So:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01100))_

> ! **true** _//=> false_ ! **false** _//=> true_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01114))_

> Here’re some simple examples of the ternary operator:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01117))_

> - 0 ? 'Hello' : 'Good bye' _//=> 'Good bye'_

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01118))_

> - [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' _//=> 'Pentatonic'_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01119))_

> The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01120))_

> **const** status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den';

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01140))_

> But when we pass other values, we no longer get true or false:

### Technical atom 6

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01153))_

> **const** even = (n) => n === 0 || (n !== 1 && even(n - 2))


## Source

- [[javascriptallonge]]
