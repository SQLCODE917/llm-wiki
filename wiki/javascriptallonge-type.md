---
page_id: javascriptallonge-type
page_kind: concept
summary: Type: 9 statement(s) and 7 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-type@0ef86bc32f7cb9953a2426a4a927feb2
---

# Type

What [[javascriptallonge]] covers about type:

## Statements

- Third, some types of cups have no distinguishing marks on them. _(javascriptallonge.pdf (source-range-83ecb080-00194))_
- When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other array also looks like [1, 2, 3]. _(javascriptallonge.pdf (source-range-83ecb080-00209))_
- For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. _(javascriptallonge.pdf (source-range-83ecb080-00232))_
- Reference types do not. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- Value types share the same identity if they have the same contents. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- Lisp’s basic data type is often said to be the list, but in actuality it was the “cons cell,” the term used to describe two 15-bit values stored in one word. _(javascriptallonge.pdf (source-range-83ecb080-01534))_
- In JavaScript, almost every type of value can _mutate_ . _(javascriptallonge.pdf (source-range-83ecb080-01688))_
- This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics. _(javascriptallonge.pdf (source-range-83ecb080-02894))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00195))_

> - 2 + 2 === 4 _//=> true_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00196))_

> - (2 + 2 === 4) === (2 !== 5) _//=> true_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00197))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00198))_

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00232))_

> > 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00235))_

> 0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00461))_

> Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00459))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00462))_

> And with that, we’re ready to look at _closures_ . When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00464))_

> - ((ref1, ref2) => ref1 === ref2)(value, value)

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01688))_

> In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01689))_

> **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_


## Related pages

- [[javascriptallonge-value]] - shared statements and technical atoms (3 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms (1 shared atom(s))
- [[javascriptallonge-environment]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
