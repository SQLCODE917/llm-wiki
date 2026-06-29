---
page_id: javascriptallonge-reference
page_kind: concept
summary: Reference: 5 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-reference@1c16ea19bf6c93c44960fd88f4787190
---

# Reference

What [[javascriptallonge]] covers about reference:

## Statements

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

- You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not. _(javascriptallonge.pdf (source-range-7239e085-00176))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-7239e085-00324))_

- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement 'call by sharing' semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. _(javascriptallonge.pdf (source-range-7239e085-00325))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

- Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements. _(javascriptallonge.pdf (source-range-7239e085-01047))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-7239e085-01057))_


## Technical atoms

### Technical frame 1: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00328))_

> 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00327))_

```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

### Technical frame 2: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01042))_

> This is a Linked List 68 , it's just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference . But it works the same way: If we want the head of a list, we call car on it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01041))_

```
const node5 = [5,null],
node4 = [4, node5],
node3 = [3, node4],
node2 = [2, node3],
node1 = [1, node2];
const oneToFive = node1;
```

### Technical frame 3: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01044))_

> car is very fast, it simply extracts the first element of the cons cell.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01043))_

```
car(oneToFive)
//=> 1
```

### Technical frame 4: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01047))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01046))_

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```


## Related pages

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated]; Javascript shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: const node5 = [5,null], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1; (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-type]] - shared statements and technical atoms: Type shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities: You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same cont ... [truncated]; Type shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-copy]] - shared statements and technical atoms: Copy shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated]; Copy shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated]; Element shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-structure]] - shared statements and technical atoms: Structure shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of ar ... [truncated]; Structure shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated]; Value shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: const node5 = [5,null], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; const oneToFive = node1; (3 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (1 shared atom(s))
- [[javascriptallonge-data]] - shared technical atoms: Data shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: car(oneToFive) //=> 1 (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: (value) => ((ref1, ref2) => ref1 === ref2)(value, value) (1 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing: Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, ... [truncated] (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
