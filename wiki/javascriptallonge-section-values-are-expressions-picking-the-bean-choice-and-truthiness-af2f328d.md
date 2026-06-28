---
page_id: javascriptallonge-section-values-are-expressions-picking-the-bean-choice-and-truthiness-af2f328d
page_kind: source
summary: values are expressions / Picking the Bean: Choice and Truthiness: 39 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-picking-the-bean-choice-and-truthiness-af2f328d@3261f46d4d8c1e7374d507644194c138
---

# values are expressions / Picking the Bean: Choice and Truthiness

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-4763e204]] - broader source section
- [[javascriptallonge-section-values-are-expressions-picking-the-bean-choice-and-truthiness-false-0d7e61ee]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operato-f8408ac8]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-picking-the-bean-choice-and-truthiness-truthiness-and-operators-a024af20]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-700863fb]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-4c2540f8]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-picking-the-bean-choice-and-truthiness-summary-23f8bae2]] - narrower source section

## Statements

- In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. _(javascriptallonge.pdf (source-range-83ecb080-00756))_

## Statements by subsection

### values are expressions / Picking the Bean: Choice and Truthiness / false

- We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. _(javascriptallonge.pdf (source-range-83ecb080-00761))_
- All values of true are === all other values of true. _(javascriptallonge.pdf (source-range-83ecb080-00761))_
- _//=> false_ true and false are value types. _(javascriptallonge.pdf (source-range-83ecb080-00761))_
- The && and || operators are binary infix operators that perform “logical and” and “logical or” respectively: **false** && **false** _//=> false_ **false** && **true** _//=> false_ **true** && **false** _//=> false_ **true** && **true** _//=> true_ **false** || **false** _//=> false_ **false** || **true** _//=> true_ **true** || **false** _//=> true_ **true** || **true** _//=> true_ _(javascriptallonge.pdf (source-range-83ecb080-00765))_
- Now, note well: We have said what happens if you pass boolean values to !, &&, and ||, but we’ve said nothing about expressions or about passing other values. _(javascriptallonge.pdf (source-range-83ecb080-00766))_

### values are expressions / Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

- So are null and undefined, values that semantically represent “no value.” NaN is falsy, a value representing the result of a calculation that is not a number.[54] And there are more: 0 is falsy, a value representing “none of something.” The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-83ecb080-00768))_
- In JavaScript, there is a notion of “truthiness.” Every value is either “truthy” or “falsy.” Obviously, false is falsy. _(javascriptallonge.pdf (source-range-83ecb080-00768))_
- Every other value in JavaScript is “truthy” except the aforementioned false, null, undefined, NaN, 0, and ''. _(javascriptallonge.pdf (source-range-83ecb080-00769))_
- (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on _truthiness_ , not on boolean values. _(javascriptallonge.pdf (source-range-83ecb080-00769))_
- Every other value in JavaScript is “truthy” except the aforementioned false, null, undefined, NaN, 0, and ''. _(javascriptallonge.pdf (source-range-83ecb080-00769))_
- JavaScript inherited an operator from the C family of languages, the _ternary_ operator. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- Picking the Bean: Choice and Truthiness and if first is “truthy”, it evaluates second and that is its value. _(javascriptallonge.pdf (source-range-83ecb080-00772))_
- If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-83ecb080-00772))_
- It also doesn’t introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements. _(javascriptallonge.pdf (source-range-83ecb080-00773))_
- This is a lot like the if statement, however it is an _expression_ , not a statement, and that can be very valuable. _(javascriptallonge.pdf (source-range-83ecb080-00773))_
- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. _(javascriptallonge.pdf (source-range-83ecb080-00778))_
- We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. _(javascriptallonge.pdf (source-range-83ecb080-00779))_
- We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. _(javascriptallonge.pdf (source-range-83ecb080-00779))_

### values are expressions / Picking the Bean: Choice and Truthiness / truthiness and operators

- Our logical operators !, &&, and || are a little more subtle than our examples above implied. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. _(javascriptallonge.pdf (source-range-83ecb080-00786))_
- First, and unlike !, && and || do not necessarily evaluate to true or false. _(javascriptallonge.pdf (source-range-83ecb080-00790))_
- First, and unlike !, && and || do not necessarily evaluate to true or false. _(javascriptallonge.pdf (source-range-83ecb080-00790))_
- If we look at our examples above, we see that when we pass true and false to && and ||, we do indeed get true or false as a result. _(javascriptallonge.pdf (source-range-83ecb080-00797))_
- They don’t operate strictly on logical values, and they don’t commute: a || b is not always equal to b || a, and the same goes for &&. _(javascriptallonge.pdf (source-range-83ecb080-00801))_
- This is not a subtle distinction. _(javascriptallonge.pdf (source-range-83ecb080-00802))_

### values are expressions / Picking the Bean: Choice and Truthiness / || and && are control-flow operators

- We’ve seen the ternary operator: It is a _control-flow_ operator, not a logical operator. _(javascriptallonge.pdf (source-range-83ecb080-00804))_
- This is more than just an optimization. _(javascriptallonge.pdf (source-range-83ecb080-00810))_
- The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-83ecb080-00810))_

### values are expressions / Picking the Bean: Choice and Truthiness / function parameters are eager

- If we need to have functions with control-flow semantics, we can pass anonymous functions. _(javascriptallonge.pdf (source-range-83ecb080-00814))_
- Here we’ve passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-83ecb080-00817))_

### values are expressions / Picking the Bean: Choice and Truthiness / summary

- - Logical operators are based on truthiness and falsiness, not the strict values true and false. _(javascriptallonge.pdf (source-range-83ecb080-00819))_
- - The ternary operator (?:), ||, and && are control flow operators, they do not always return true or false, and they have short-cut semantics. _(javascriptallonge.pdf (source-range-83ecb080-00821))_
- - Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-83ecb080-00822))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00761))_

> _//=> false_ true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. To being with, ! is a unary prefix operator that negates its argument. So:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00764))_

> ! **true** _//=> false_ ! **false** _//=> true_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00773))_

> This is a lot like the if statement, however it is an _expression_ , not a statement, and that can be very valuable. It also doesn’t introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00776))_

> - 0 ? 'Hello' : 'Good bye' _//=> 'Good bye'_

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00777))_

> - [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' _//=> 'Pentatonic'_

### Technical atom 4

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00797))_

> But when we pass other values, we no longer get true or false:
