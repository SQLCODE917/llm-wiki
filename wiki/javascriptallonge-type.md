---
page_id: javascriptallonge-type
page_kind: concept
summary: Type: 9 statement(s) and 5 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-type@a08d15f693f275916be8e662c5a4462b
---

# Type

What [[javascriptallonge]] covers about type:

## Statements

### Prelude: Values and Expressions over Coffee / values and identity / value types

- Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far. _(javascriptallonge.pdf (source-range-7239e085-00124))_

### Prelude: Values and Expressions over Coffee / values and identity / reference types

- How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own unique array that is not identical to any other array, even if that other array also looks like [1, 2, 3] . It's as if JavaScript is generating new cups of coffee with serial numbers on the bottom. _(javascriptallonge.pdf (source-range-7239e085-00136))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

- You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not. _(javascriptallonge.pdf (source-range-7239e085-00176))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-7239e085-00322))_

- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-7239e085-00324))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

- Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the 'cons cell,' the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells. _(javascriptallonge.pdf (source-range-7239e085-01032))_

### Composing and Decomposing Data / Mutation

- In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = : _(javascriptallonge.pdf (source-range-7239e085-01121))_

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the aftermath

- The Carpenter sat down and waited. This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics. _(javascriptallonge.pdf (source-range-7239e085-01853))_


## Technical atoms

### Technical frame 1: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00126))_

> Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same 'content.' Strings, numbers, and booleans are examples of what JavaScript calls 'value' or 'primitive' types. We'll use both terms interchangeably.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00125))_

```
2 + 2 === 4
//=> true
(2 + 2 === 4) === (2 !== 5)
//=> true
```

### Technical frame 2: Prelude: Values and Expressions over Coffee / values and identity / value types

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00129))_

> Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d'Italia

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00127))_

> So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

### Technical frame 3: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00328))_

> 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00327))_

```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

### Technical frame 4: Composing and Decomposing Data / Mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01127))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01122))_

```
const oneTwoThree = [1, 2, 3];
oneTwoThree[0] = 'one';
oneTwoThree
//=> [ 'one', 2, 3 ]
```

### Technical atom 5

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00152))_

| entry | content |
| --- | --- |
| 13 | http://en.wikipedia.org/wiki/Double-precision_floating-point_format |
| 14 | Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 . But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. |

<details>
<summary>Raw table text</summary>

```
13 http://en.wikipedia.org/wiki/Double-precision_floating-point_format
14 Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js , it will happily report that the answer is 18014398509481982 . But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.
```

</details>


## Related pages

- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same cont ... [truncated]; Value shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (4 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated]; Javascript shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-string]] - shared statements and technical atoms: String shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to ... [truncated]; String shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-reference]] - shared statements and technical atoms: Reference shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same cont ... [truncated]; Reference shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-note]] - shared technical atoms: Note shares technical record from Prelude: Values and Expressions over Coffee / values and identity / value types: 2 + 2 === 4 //=> true (2 + 2 === 4) === (2 !== 5) //=> true (2 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (1 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical table: 13 http://en.wikipedia.org/wiki/Double-precision_floating-point_format 14 Implementations of JavaScript are free to handle larger numbers. For example, if you type 9 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (1 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from Composing and Decomposing Data / Mutation: const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ] (1 shared atom(s))
- [[javascriptallonge-data]] - shared statements: Data shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp's basic data type is often said to be the list, but in actuality it was the ... [truncated] (1 shared statement(s))
- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
