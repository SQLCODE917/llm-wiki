---
page_id: javascriptallonge-section-picking-the-bean-choice-and-truthiness-d45c6f89
page_kind: source
summary: Picking the Bean: Choice and Truthiness: 47 source-backed entries and 11 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-picking-the-bean-choice-and-truthiness-d45c6f89@a96baf86d764acac92e678b27ae51c65
---

# Picking the Bean: Choice and Truthiness

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-the-ternary-operator-d8796156]] - narrower source section: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-truthiness-and-operators-f4c050bc]] - narrower source section: Picking the Bean: Choice and Truthiness / truthiness and operators
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-and-are-control-flow-operators-f37352da]] - narrower source section: Picking the Bean: Choice and Truthiness / || and && are control-flow operators
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-function-parameters-are-eager-77511990]] - narrower source section: Picking the Bean: Choice and Truthiness / function parameters are eager
- [[javascriptallonge-section-picking-the-bean-choice-and-truthiness-summary-7f12d5ad]] - narrower source section: Picking the Bean: Choice and Truthiness / summary

## Statements

- We've seen operators that act on numeric values, like + and % . In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. Is this array empty? Does this person have a middle name? Is this user logged in? _(javascriptallonge.pdf (source-range-7239e085-00753))_
- true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, ! , && , and || . To being with, ! is a unary prefix operator that negates its argument. So: _(javascriptallonge.pdf (source-range-7239e085-00759))_
- Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently. _(javascriptallonge.pdf (source-range-7239e085-00763))_

## Statements by subsection

### Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-7239e085-00765))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) _(javascriptallonge.pdf (source-range-7239e085-00766))_
- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This affects the way the ! , && , and || operators work. We'll look at them in a moment, but first, we'll look at one more operator. _(javascriptallonge.pdf (source-range-7239e085-00767))_
- JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-7239e085-00768))_
- This is a lot like the if statement, however it is an expression , not a statement, and that can be very valuable. It also doesn't introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements. _(javascriptallonge.pdf (source-range-7239e085-00770))_
- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example: _(javascriptallonge.pdf (source-range-7239e085-00773))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-7239e085-00775))_
- Every other value in JavaScript is 'truthy' except the aforementioned false , null , undefined , NaN , 0 , and '' . _(javascriptallonge.pdf (source-range-7239e085-00766))_
- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-7239e085-00775))_

### Picking the Bean: Choice and Truthiness / truthiness and operators

- Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-7239e085-00777))_
- Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user. _(javascriptallonge.pdf (source-range-7239e085-00779))_
- First, and unlike ! , && and || do not necessarily evaluate to true or false . To be precise: _(javascriptallonge.pdf (source-range-7239e085-00781))_
- If we look at our examples above, we see that when we pass true and false to && and || , we do indeed get true or false as a result. But when we pass other values, we no longer get true or false : _(javascriptallonge.pdf (source-range-7239e085-00788))_
- In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && . _(javascriptallonge.pdf (source-range-7239e085-00790))_
- This is not a subtle distinction. _(javascriptallonge.pdf (source-range-7239e085-00791))_

### Picking the Bean: Choice and Truthiness / || and && are control-flow operators

- We've seen the ternary operator: It is a control-flow operator, not a logical operator. The same is true of && and || . Consider this tail-recursive function that determines whether a positive integer is even: _(javascriptallonge.pdf (source-range-7239e085-00793))_
- This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-7239e085-00799))_

### Picking the Bean: Choice and Truthiness / function parameters are eager

- In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated : _(javascriptallonge.pdf (source-range-7239e085-00801))_
- If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique: _(javascriptallonge.pdf (source-range-7239e085-00804))_
- Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation. _(javascriptallonge.pdf (source-range-7239e085-00806))_
- In contrast to the behaviour of the ternary operator, || , and && , function parameters are always eagerly evaluated : _(javascriptallonge.pdf (source-range-7239e085-00801))_

### Picking the Bean: Choice and Truthiness / summary

- Logical operators are based on truthiness and falsiness, not the strict values true and false . _(javascriptallonge.pdf (source-range-7239e085-00808))_
- The ternary operator ( ?: ), || , and && are control flow operators, they do not always return true or false , and they have short-cut semantics. _(javascriptallonge.pdf (source-range-7239e085-00810))_
- Function invocation uses eager evaluation, so if we need to roll our own control-flow semantics, we pass it functions, not expressions. _(javascriptallonge.pdf (source-range-7239e085-00811))_

## Technical atoms

### Technical frame 1: Picking the Bean: Choice and Truthiness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00753))_

> We've seen operators that act on numeric values, like + and % . In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. Is this array empty? Does this person have a middle name? Is this user logged in?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00751))_

> [Figure] (p.94)

### Technical frame 2: Picking the Bean: Choice and Truthiness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00763))_

> Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00760))_

```
!true
//=> false
!false
//=> true
```

### Technical frame 3: Picking the Bean: Choice and Truthiness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00763))_

> Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00762))_

```
false && false //=> false
false && true
//=> false
true
&& false //=> false
true
&& true
//=> true
false || false //=> false
false || true
//=> true
true
|| false //=> true
true
|| true
//=> true
```

### Technical frame 4: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00773))_

> The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00772))_

```
true ? 'Hello' : 'Good bye'
//=> 'Hello'
0 ? 'Hello' : 'Good bye'
//=> 'Good bye'
[1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal'
//=> 'Pentatonic'
```

### Technical frame 5: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00775))_

> Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00774))_

```
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\
den';
```

### Technical frame 6: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00779))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00778))_

```
!5
//=> false
!undefined
//=> true
```

### Technical frame 7: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00790))_

> In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00788))_

> But when we pass other values, we no longer get true or false :

### Technical frame 8: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00790))_

> In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00789))_

```
1 || 2
//=> 1
null && undefined
//=> null
undefined && null
//=> undefined
```

### Technical frame 9: Picking the Bean: Choice and Truthiness / || and && are control-flow operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00799))_

> This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00795))_

```
const even = (n) =>
n === 0 || (n !== 1 && even(n - 2))
even(42)
//=> true
```

### Technical frame 10: Picking the Bean: Choice and Truthiness / function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00804))_

> If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00802))_

```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```

### Technical frame 11: Picking the Bean: Choice and Truthiness / function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00806))_

> Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00805))_

```
const or = (a, b) => a() || b()
const and = (a, b) => a() && b()
const even = (n) =>
or(() => n === 0, () => and(() => n !== 1, () => even(n - 2)))
even(7)
//=> false
```
