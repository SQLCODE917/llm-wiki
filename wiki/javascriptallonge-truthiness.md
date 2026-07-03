---
page_id: javascriptallonge-truthiness
page_kind: concept
page_family: topic-concept
summary: Truthiness: 2 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-truthiness@a966e37d01cb51aeed823b00fc180046
---

# Truthiness

What [[javascriptallonge]] covers about truthiness:

## Statements

### Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-7239e085-00765))_

### Picking the Bean: Choice and Truthiness / summary

- Logical operators are based on truthiness and falsiness, not the strict values true and false . _(javascriptallonge.pdf (source-range-7239e085-00808))_


## Technical atoms

### Technical frame 1: Picking the Bean: Choice and Truthiness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00763))_

> Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00760))_

<a id="atom-technical-atom-843bd04c4cf702f8"></a>

```
!true
//=> false
!false
//=> true
```

### Technical frame 2: Picking the Bean: Choice and Truthiness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00763))_

> Now, note well: We have said what happens if you pass boolean values to ! , && , and || , but we've said nothing about expressions or about passing other values. We'll look at those presently.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00762))_

<a id="atom-technical-atom-799c16e09c3689d4"></a>

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

### Technical frame 3: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00773))_

> The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00772))_

<a id="atom-technical-atom-47ab3b5bdc155cff"></a>

```
true ? 'Hello' : 'Good bye'
//=> 'Hello'
0 ? 'Hello' : 'Good bye'
//=> 'Good bye'
[1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal'
//=> 'Pentatonic'
```

### Technical frame 4: Picking the Bean: Choice and Truthiness / truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00775))_

> Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00774))_

<a id="atom-technical-atom-146014ea05c20f9f"></a>

```
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\
den';
```

### Technical frame 5: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00779))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00778))_

<a id="atom-technical-atom-e4e2b300bef7f5ba"></a>

```
!5
//=> false
!undefined
//=> true
```

### Technical frame 6: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00790))_

> In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00788))_

<a id="atom-technical-atom-f7360fc878cd62ac"></a>

> But when we pass other values, we no longer get true or false :

### Technical frame 7: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00790))_

> In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00789))_

<a id="atom-technical-atom-18deb0cfe93967e8"></a>

```
1 || 2
//=> 1
null && undefined
//=> null
undefined && null
//=> undefined
```

### Technical frame 8: Picking the Bean: Choice and Truthiness / || and && are control-flow operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00799))_

> This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00795))_

<a id="atom-technical-atom-d27aeaad056c2ea9"></a>

```
const even = (n) =>
n === 0 || (n !== 1 && even(n - 2))
even(42)
//=> true
```

### Technical frame 9: Picking the Bean: Choice and Truthiness / function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00804))_

> If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00802))_

<a id="atom-technical-atom-f6692ca904d56bf1"></a>

```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```

### Technical frame 10: Picking the Bean: Choice and Truthiness / function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00806))_

> Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00805))_

<a id="atom-technical-atom-85184dcfdb4ac959"></a>

```
const or = (a, b) => a() || b()
const and = (a, b) => a() && b()
const even = (n) =>
or(() => n === 0, () => and(() => n !== 1, () => even(n - 2)))
even(7)
//=> false
```


## Related pages

### Shared technical atoms

- [[javascriptallonge-behaviour]] - shared technical atoms: Behaviour shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (2 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from Picking the Bean: Choice and Truthiness / function parameters are eager: const or = (a, b) => a || b const and = (a, b) => a && b const even = (n) => or(n === 0, and(n !== 1, even(n - 2))) even(42) //=> Maximum call stack size exceeded. (2 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from Picking the Bean: Choice and Truthiness: !true //=> false !false //=> true (2 shared atom(s))
- [[javascriptallonge-alway]] - shared technical atoms: Alway shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; (1 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from Picking the Bean: Choice and Truthiness / function parameters are eager: const or = (a, b) => a || b const and = (a, b) => a && b const even = (n) => or(n === 0, and(n !== 1, even(n - 2))) even(42) //=> Maximum call stack size exceeded. (1 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))

### Shared claims

- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and the ternary operator: In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that seman ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
