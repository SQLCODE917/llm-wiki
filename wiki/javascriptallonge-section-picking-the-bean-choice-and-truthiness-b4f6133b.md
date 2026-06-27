---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-b4f6133b
page_kind: source
summary: Picking the Bean: Choice and Truthiness: 49 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-b4f6133b@363aae715d4bd17cc541efda76342be7
---

# Picking the Bean: Choice and Truthiness

From [[javascriptallonge]].

## Statements

- In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. _(javascriptallonge.pdf (source-range-83ecb080-01091))_
- All values of true are === all other values of true. _(javascriptallonge.pdf (source-range-83ecb080-01097))_
- We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. _(javascriptallonge.pdf (source-range-83ecb080-01097))_
- true and false are value types. _(javascriptallonge.pdf (source-range-83ecb080-01097))_
- Now, note well: We have said what happens if you pass boolean values to !, &&, and ||, but we’ve said nothing about expressions or about passing other values. _(javascriptallonge.pdf (source-range-83ecb080-01103))_
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
- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-83ecb080-01123))_
- Our logical operators !, &&, and || are a little more subtle than our examples above implied. _(javascriptallonge.pdf (source-range-83ecb080-01123))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. _(javascriptallonge.pdf (source-range-83ecb080-01128))_
- First, and unlike !, && and || do not necessarily evaluate to true or false. _(javascriptallonge.pdf (source-range-83ecb080-01133))_
- First, and unlike !, && and || do not necessarily evaluate to true or false. _(javascriptallonge.pdf (source-range-83ecb080-01133))_
- If we look at our examples above, we see that when we pass true and false to && and ||, we do indeed get true or false as a result. _(javascriptallonge.pdf (source-range-83ecb080-01140))_
- They don’t operate strictly on logical values, and they don’t commute: a || b is not always equal to b || a, and the same goes for &&. _(javascriptallonge.pdf (source-range-83ecb080-01146))_
- This is not a subtle distinction. _(javascriptallonge.pdf (source-range-83ecb080-01147))_
- We’ve seen the ternary operator: It is a _control-flow_ operator, not a logical operator. _(javascriptallonge.pdf (source-range-83ecb080-01149))_
- The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-83ecb080-01159))_
- This is more than just an optimization. _(javascriptallonge.pdf (source-range-83ecb080-01159))_
- In contrast to the behaviour of the ternary operator, ||, and &&, function parameters are always : _eagerly evaluated_ _(javascriptallonge.pdf (source-range-83ecb080-01161))_
- In contrast to the behaviour of the ternary operator, ||, and &&, function parameters are always : _eagerly evaluated_ _(javascriptallonge.pdf (source-range-83ecb080-01161))_
- This leads to the infinite recursion we fear. _(javascriptallonge.pdf (source-range-83ecb080-01166))_
- If we need to have functions with control-flow semantics, we can pass anonymous functions. _(javascriptallonge.pdf (source-range-83ecb080-01167))_
- Here we’ve passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-83ecb080-01171))_
- - Logical operators are based on truthiness and falsiness, not the strict values true and false. _(javascriptallonge.pdf (source-range-83ecb080-01173))_
- - The ternary operator (?:), ||, and && are control flow operators, they do not always return true or false, and they have short-cut semantics. _(javascriptallonge.pdf (source-range-83ecb080-01175))_
- - Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-83ecb080-01176))_

## Technical atoms

> Context: true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. To being with, ! is a unary prefix operator that negates its argument. So:
_(context: javascriptallonge.pdf (source-range-83ecb080-01097))_

> ! **true** _//=> false_ ! **false** _//=> true_
_(source: javascriptallonge.pdf (source-range-83ecb080-01100))_

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

> But when we pass other values, we no longer get true or false:
_(source: javascriptallonge.pdf (source-range-83ecb080-01140))_

> **const** even = (n) => n === 0 || (n !== 1 && even(n - 2))
_(source: javascriptallonge.pdf (source-range-83ecb080-01153))_

> **const** or = (a, b) => a || b
_(source: javascriptallonge.pdf (source-range-83ecb080-01162))_

> **const** and = (a, b) => a && b
_(source: javascriptallonge.pdf (source-range-83ecb080-01163))_

> **const** even = (n) => or(n === 0, and(n !== 1, even(n - 2)))
_(source: javascriptallonge.pdf (source-range-83ecb080-01164))_

> even(42) _//=> Maximum call stack size exceeded._
_(source: javascriptallonge.pdf (source-range-83ecb080-01165))_
