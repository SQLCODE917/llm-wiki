---
page_id: javascriptallonge-choice
page_kind: concept
summary: Choice: 4 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-choice@2a2e2d5abe64515549b87c58370be393
---

# Choice

What [[javascriptallonge]] covers about choice:

## Statements

### What JavaScript Allongé is. And isn't.

- A Pull of the Lever: Prefaces v

## **What JavaScript Allongé is. And isn’t.**

**==> picture [468 x 275] intentionally omitted <==**

**JavaScript Allongé is a book about thinking about programs**

JavaScript Allongé is a book about programming with functions. From functions flow many ideas, from decorators to methods to delegation to mixins, and onwards in so many fruitful directions.

The focus in this book on the underlying ideas, what we might call the fundamentals, and how they combine to form new ideas. The intention is to improve the way we think about programs. That’s a good thing.

But while JavaScript Allongé attempts to be provocative, it is not _prescriptive_ . There is absolutely no suggestion that any of the techniques shown here are the only way to do something, the best way, or even an acceptable way to write programs that are intended to be used, read, and maintained by others.

Software development is a complex field. Choices in development are often driven by social considerations. People often say that software should be written for people to read. Doesn’t that depend upon the people in question? Should code written by a small team of specialists use the same techniques and patterns as code maintained by a continuously changing cast of inexperienced interns?

Choices in software development are also often driven by requirements specific to the type of software being developed. For example, business software written in-house has a very different set of requirements than a library written to be publicly distributed as open-source. _(javascriptallonge.pdf (source-range-83ecb080-00016))_

- vi

A Pull of the Lever: Prefaces

Choices in software development must also consider the question of consistency. If a particular codebase is written with lots of helper functions that place the subject first, like this: **const** mapWith = (iterable, fn) => ({ [Symbol.iterator]: **function** * () { **for** ( **let** element **of** iterable) { **yield** fn(element); } } }); Then it can be jarring to add new helpers written that place the verb first, like this: **const** filterWith = (fn, iterable) => ({ [Symbol.iterator]: **function** * () { **for** ( **let** element **of** iterable) { **if** (!!fn(element)) **yield** element; } } });

There are reasons why the second form is more flexible, especially when used in combination with partial application, but does that outweigh the benefit of having an entire codebase do everything consistently the first way or the second way?

Finally, choices in software development cannot ignore the tooling that is used to create and maintain software. The use of source-code control systems with integrated diffing rewards making certain types of focused changes. The use of linters[1] makes checking for certain types of undesirable code very cheap. Debuggers encourage the use of functions with explicit or implicit names. Continuous integration encourages the creation of software in tandem with and factored to facilitate the creation of automated test suites.

JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn’t a book about practicing, it’s a book about thinking.

## **how this book is organized**

_JavaScript Allongé_ introduces new aspects of programming with functions in each chapter, explaining exactly how JavaScript works. Code examples within each chapter are small and emphasize exposition rather than serving as patterns for everyday use.

1https://en.wikipedia.org/wiki/Lint_ _(javascriptallonge.pdf (source-range-83ecb080-00017))_


## Technical atoms

### Technical atom 1

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00118))_

| entry | content |
| --- | --- |
| 0 | ? 'Hello' : 'Good bye' _//=> 'Good bye'_ The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example: We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. Our logical operators !, &&, and \|\| are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser(), this is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user. Thus, !! is the way we write “is truthy” in JavaScript. How about && and \|\|? What haven’t we discussed? First, and unlike !, && and \|\| do not necessarily evaluate to true or false. To be precise: - && evaluates its left-hand expression. - If its left-hand expression evaluates to something falsy, && returns the value of its lefthand expression without evaluating its right-hand expression. - If its left-hand expression evaluates to something truthy, && evaluates its right-hand expression and returns the value of the right-hand expression. - \|\| evaluates its left-hand expression. - If its left-hand expression evaluates to something truthy, \|\| returns the value of its lefthand expression without evaluating its right-hand expression. - If its left-hand expression evaluates to something false, \|\| evaluates its right-hand expression and returns the value of the right-hand expression. If we look at our examples above, we see that when we pass true and false to && and \|\|, we do indeed get true or false as a result. But when we pass other values, we no longer get true or false: |
| 1 | - [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' _//=> 'Pentatonic'_ **const** status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; ## **truthiness and operators** !5 _//=> false_ ! **undefined** _//=> true_ Picking the Bean: Choice and Truthiness 74 \|\| 2 _//=> 1_ In JavaScript, && and \|\| aren’t boolean logical operators in the logical sense. They don’t operate strictly on logical values, and they don’t commute: a \|\| b is not always equal to b \|\| a, and the same goes for &&. This is not a subtle distinction. We’ve seen the ternary operator: It is a _control-flow_ operator, not a logical operator. The same is true of && and \|\|. Consider this tail-recursive function that determines whether a positive integer is even: |

<details>
<summary>Raw table text</summary>

```
Picking the Bean: Choice and Truthiness
## **Picking the Bean: Choice and Truthiness** 

**==> picture [469 x 264] intentionally omitted <==**

**Decaf and the Antidote** 

We’ve seen operators that act on numeric values, like + and %. In addition to numbers, we often need to represent a much more basic idea of truth or falsehood. Is this array empty? Does this person have a middle name? Is this user logged in? 

JavaScript does have “boolean” values, they’re written true and false: 

## **true** 

_//=> true_ 

## **false** 

_//=> false_ 

true and false are value types. All values of true are === all other values of true. We can see that is the case by looking at some operators we can perform on boolean values, !, &&, and ||. To being with, ! is a unary prefix operator that negates its argument. So:
Picking the Bean: Choice and Truthiness 

72 

! **true** _//=> false_ ! **false** _//=> true_ 

The && and || operators are binary infix operators that perform “logical and” and “logical or” respectively: 

**false** && **false** _//=> false_ **false** && **true** _//=> false_ **true** && **false** _//=> false_ **true** && **true** _//=> true_ **false** || **false** _//=> false_ **false** || **true** _//=> true_ **true** || **false** _//=> true_ **true** || **true** _//=> true_ 

Now, note well: We have said what happens if you pass boolean values to !, &&, and ||, but we’ve said nothing about expressions or about passing other values. We’ll look at those presently. 

## **truthiness and the ternary operator** 

In JavaScript, there is a notion of “truthiness.” Every value is either “truthy” or “falsy.” Obviously, false is falsy. So are null and undefined, values that semantically represent “no value.” NaN is falsy, a value representing the result of a calculation that is not a number.[54] And there are more: 0 is falsy, a value representing “none of something.” The empty string, '' is falsy, a value representing having no characters. 

Every other value in JavaScript is “truthy” except the aforementioned false, null, undefined, NaN, 0, and ''. (Many other languages that have a notion of truthiness consider zero and the empty string to be truthy, not falsy, so beware of blindly transliterating code from one language to another!) 

The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on _truthiness_ , not on boolean values. This affects the way the !, &&, and || operators work. We’ll look at them in a moment, but first, we’ll look at one more operator. 

JavaScript inherited an operator from the C family of languages, the _ternary_ operator. It’s the only operator that takes _three_ arguments. It looks like this: first ? second : third. It evaluates first, 

> 54We will not discuss JavaScript’s numeric behaviour in much depth in this book, but the most important thing to know is that it implements the IEEE Standard for Floating-Point Arithmetic (IEEE 754), a technical standard for floating-point computation established in 1985 by the Institute of Electrical and Electronics Engineers (IEEE).
73 

Picking the Bean: Choice and Truthiness 

and if first is “truthy”, it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. 

This is a lot like the if statement, however it is an _expression_ , not a statement, and that can be very valuable. It also doesn’t introduce braces, and that can be a help or a hindrance if we want to introduce a new scope or use statements. 

Here’re some simple examples of the ternary operator: 

**true** ? 'Hello' : 'Good bye' 

_//=> 'Hello'_ 

- 0 ? 'Hello' : 'Good bye' _//=> 'Good bye'_ 

- [1, 2, 3, 4, 5].length === 5 ? 'Pentatonic' : 'Quasimodal' _//=> 'Pentatonic'_ 

The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example: 

**const** status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; 

We certainly don’t want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true. 

## **truthiness and operators** 

Our logical operators !, &&, and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: 

!5 

_//=> false_ 

! **undefined** 

_//=> true_ 

Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser(), this
Picking the Bean: Choice and Truthiness 

74 

is an idiom that means “true if currentUser is truthy.” Thus, a function like currentUser() is free to return null, or undefined, or false if there is no current user. 

Thus, !! is the way we write “is truthy” in JavaScript. How about && and ||? What haven’t we discussed? 

First, and unlike !, && and || do not necessarily evaluate to true or false. To be precise: 

- && evaluates its left-hand expression. 

   - If its left-hand expression evaluates to something falsy, && returns the value of its lefthand expression without evaluating its right-hand expression. 

   - If its left-hand expression evaluates to something truthy, && evaluates its right-hand expression and returns the value of the right-hand expression. 

- || evaluates its left-hand expression. 

   - If its left-hand expression evaluates to something truthy, || returns the value of its lefthand expression without evaluating its right-hand expression. 

   - If its left-hand expression evaluates to something false, || evaluates its right-hand expression and returns the value of the right-hand expression. 

If we look at our examples above, we see that when we pass true and false to && and ||, we do indeed get true or false as a result. But when we pass other values, we no longer get true or false: 

1 || 2 _//=> 1_ 

**null** && **undefined** 

_//=> null_ 

**undefined** && **null** 

_//=> undefined_ 

In JavaScript, && and || aren’t boolean logical operators in the logical sense. They don’t operate strictly on logical values, and they don’t commute: a || b is not always equal to b || a, and the same goes for &&. 

This is not a subtle distinction. 

## **|| and && are control-flow operators** 

We’ve seen the ternary operator: It is a _control-flow_ operator, not a logical operator. The same is true of && and ||. Consider this tail-recursive function that determines whether a positive integer is even: 

For example:
```

</details>


## Related pages

- [[javascriptallonge-function]] - shared technical atoms: Function shares technical table: Picking the Bean: Choice and Truthiness ## **Picking the Bean: Choice and Truthiness**  **==> picture [469 x 264] intentionally omitted <==**  **Decaf and the Antido ... [truncated] (1 shared atom(s))
- [[javascriptallonge-development]] - shared statements: Development shares source evidence from What JavaScript Allongé is. And isn't.: A Pull of the Lever: Prefaces v  ## **What JavaScript Allongé is. And isn’t.**  **==> picture [468 x 275] intentionally omitted <==**  **JavaScript Allongé is a book ... [truncated] (4 shared statement(s))
- [[javascriptallonge-software]] - shared statements: Software shares source evidence from What JavaScript Allongé is. And isn't.: A Pull of the Lever: Prefaces v  ## **What JavaScript Allongé is. And isn’t.**  **==> picture [468 x 275] intentionally omitted <==**  **JavaScript Allongé is a book ... [truncated] (3 shared statement(s))

## Source

- [[javascriptallonge]]
