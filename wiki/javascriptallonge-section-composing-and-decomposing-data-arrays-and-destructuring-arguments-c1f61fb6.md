---
page_id: javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-c1f61fb6
page_kind: source
summary: Composing and Decomposing Data / Arrays and Destructuring Arguments: 62 source-backed entries and 24 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-c1f61fb6@0f7ca8791688aefc469eb08f25a56133
---

# Composing and Decomposing Data / Arrays and Destructuring Arguments

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-6f7d7870]] - broader source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-array-literals-2857d963]] - narrower source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-element-references-a8dcb708]] - narrower source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-arrays-6ab61a91]] - narrower source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-gathering-91ed37bf]] - narrower source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-is-not-pattern-m-d5383046]] - narrower source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-and-return-value-ec61c56d]] - narrower source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values
- [[javascriptallonge-section-composing-and-decomposing-data-arrays-and-destructuring-arguments-destructuring-parameters-6cd226a5]] - narrower source section: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

## Statements

- While we have mentioned arrays briefly, we haven't had a close look at them. Arrays are JavaScript's 'native' representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-7239e085-00818))_
- Strings are important because they represent writing. _(javascriptallonge.pdf (source-range-7239e085-00818))_
- Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-7239e085-00818))_

## Statements by subsection

### Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

- JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: _(javascriptallonge.pdf (source-range-7239e085-00820))_
- We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional: _(javascriptallonge.pdf (source-range-7239e085-00822))_
- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-7239e085-00828))_
- Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-7239e085-00831))_
- Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-7239e085-00828))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

- Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: _(javascriptallonge.pdf (source-range-7239e085-00834))_
- As we can see, JavaScript Arrays are zero-based 56 . _(javascriptallonge.pdf (source-range-7239e085-00836))_
- We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind? _(javascriptallonge.pdf (source-range-7239e085-00837))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [ , expressions, , and ] . Here's an example of an array literal that uses a name: _(javascriptallonge.pdf (source-range-7239e085-00841))_
- The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string. _(javascriptallonge.pdf (source-range-7239e085-00844))_
- In JavaScript, we can actually reverse the statement and place the template on the left and a value on the right: _(javascriptallonge.pdf (source-range-7239e085-00845))_
- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-7239e085-00847))_
- We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style. _(javascriptallonge.pdf (source-range-7239e085-00849))_
- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. _(javascriptallonge.pdf (source-range-7239e085-00841))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

- Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-7239e085-00853))_
- car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. Some other languages call them first and butFirst , or head and tail . We will use a common convention and call variables we gather rest , but refer to the ... operation as a 'gather,' following Kyle Simpson's example. 58 _(javascriptallonge.pdf (source-range-7239e085-00855))_
- Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write _(javascriptallonge.pdf (source-range-7239e085-00856))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

- Some other languages have something called pattern matching , where you can write something like a destructuring assignment, and the language decides whether the 'patterns' matches at all. If it does, assignments are made where appropriate. _(javascriptallonge.pdf (source-range-7239e085-00862))_
- That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore: _(javascriptallonge.pdf (source-range-7239e085-00865))_
- From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-7239e085-00869))_
- That match would fail because the array doesn't have an element to assign to what . _(javascriptallonge.pdf (source-range-7239e085-00865))_
- This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-7239e085-00869))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

- It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that: _(javascriptallonge.pdf (source-range-7239e085-00878))_
- Gathering works with parameters! This is very useful indeed, and we'll see more of it in a moment. 59 _(javascriptallonge.pdf (source-range-7239e085-00880))_
- 59 Gathering in parameters has a long history, and the usual terms are to call gathering 'pattern matching' and to call a name that is bound to gathered values a 'rest parameter.' The term 'rest' is perfectly compatible with gather: 'Rest' is the noun, and 'gather' is the verb. We gather the rest of the parameters. _(javascriptallonge.pdf (source-range-7239e085-00881))_
- There is only one difference: We have not tried gathering. _(javascriptallonge.pdf (source-range-7239e085-00878))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00822))_

> We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00821))_

```
[]
//=> []
```

### Technical frame 2: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00823))_

```
[1]
//=> [1]
[2, 3, 4]
//=> [2,3,4]
```

### Technical frame 3: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00825))_

```
[ 2,
3,
2 + 2
]
//=> [2,3,4]
```

### Technical frame 4: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00828))_

> This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00827))_

```
[[[[[]]]]]
```

### Technical frame 5: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00831))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00830))_

```
const wrap = (something) => [something];
wrap("lunch")
//=> ["lunch"]
```

### Technical frame 6: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00831))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00832))_

```
[] === []
//=> false
[2 + 2] === [2 + 2]
//=> false
const array_of_one = () => [1];
array_of_one() === array_of_one()
//=> false
```

### Technical frame 7: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00836))_

> As we can see, JavaScript Arrays are zero-based 56 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00835))_

```
const oneTwoThree = ["one", "two", "three"];
oneTwoThree[0]
//=> 'one'
oneTwoThree[1]
//=> 'two'
oneTwoThree[2]
//=> 'three'
```

### Technical frame 8: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00837))_

> We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00839))_

```
const x = [],
a = [x];
a[0] === x
//=> true, arrays store references to the things you put in them.
```

### Technical frame 9: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00844))_

> The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00842))_

```
const wrap = (something) => [something];
Let’s expand it to use a block and an extra name:
const wrap = (something) => {
const wrapped = [something];
```

### Technical frame 10: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00844))_

> The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00843))_

```
const wrap = (something) => {
const wrapped = [something]
return wrapped;
}
wrap("package")
//=> ["package"]
```

### Technical frame 11: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00847))_

> The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00846))_

```
const unwrap = (wrapped) => {
const [something] = wrapped;
return something;
}
unwrap(["present"])
//=> "present"
```

### Technical frame 12: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00849))_

> We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00848))_

```
const surname = (name) => {
const [first, last] = name;
return last;
}
surname(["Reginald", "Braithwaite"])
//=> "Braithwaite"
```

### Technical frame 13: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00849))_

> We could do the same thing with (name) => name[1] , but destructuring is code that resembles the data it consumes, a valuable coding style.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00851))_

```
const description = (nameAndOccupation) => {
const [[first, last], occupation] = nameAndOccupation;
return `${first} is a ${occupation}`;
}
description([["Reginald", "Braithwaite"], "programmer"])
//=> "Reginald is a programmer"
```

### Technical frame 14: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00855))_

> car and cdr 57 are archaic terms that go back to an implementation of Lisp running on the IBM 704 computer. Some other languages call them first and butFirst , or head and tail . We will use a common convention and call variables we gather rest , but refer to the ... operation as a 'gather,' following Kyle Simpson's example. 58

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00854))_

```
const [car, ...cdr] = [1, 2, 3, 4, 5];
car
//=> 1
cdr
//=> [2, 3, 4, 5]
```

### Technical frame 15: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00858))_

```
const [...butLast, last] = [1, 2, 3, 4, 5];
//=> ERROR
const [first, ..., last] = [1, 2, 3, 4, 5];
//=> ERROR
Now, when we introduced destructuring, we saw that it is kind-of-sort-of the reverse of array literals.
So if
const wrapped = [something];
Then:
const [unwrapped] = something;
What is the reverse of gathering? We know that:
const [car, ...cdr] = [1, 2, 3, 4, 5];
What is the reverse? It would be:
const cons = [car, ...cdr];
Let’s try it:
const oneTwoThree = ["one", "two", "three"];
```

### Technical frame 16: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00859))_

```
Let’s try it:
const oneTwoThree = ["one", "two", "
["zero", ...oneTwoThree]
//=> ["zero","one","two","three"]
```

### Technical frame 17: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00865))_

> That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00864))_

```
const [what] = [];
```

### Technical frame 18: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00869))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00866))_

```
const [what] = [];
what
//=> undefined
const [which, what,
who
//=> undefined
```

### Technical frame 19: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00869))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00867))_

```
const [...they] = [];
they
//=> []
const [which, what, .
they
//=> []
```

### Technical frame 20: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring and return values

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00872))_

```
const description = (nameAndOccupation) => {
if (nameAndOccupation.length < 2) {
return ["", "occupation missing"]
}
else {
const [[first, last], occupation] = nameAndOccupation;
return [`${first} is a ${occupation}`, "ok"];
}
}
const [reg, status] = description([["Reginald", "Braithwaite"], "programmer"]);
reg
//=> "Reginald is a programmer"
status
//=> "ok"
```

### Technical frame 21: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00878))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00875))_

```
foo()
bar("smaug")
baz(1, 2, 3)
```

### Technical frame 22: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00878))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00877))_

```
const foo = () => ...
const bar = (name) => ...
const baz = (a, b, c) => ...
```

### Technical frame 23: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00880))_

> Gathering works with parameters! This is very useful indeed, and we'll see more of it in a moment. 59

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00879))_

```
const numbers = (...nums) => nums;
numbers(1, 2, 3, 4, 5)
//=> [1,2,3,4,5]
const headAndTail = (head, ...tail) => [head, tail];
headAndTail(1, 2, 3, 4, 5)
//=> [1,[2,3,4,5]]
```

### Technical atom 24

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00856))_

> Alas, the ... notation does not provide a universal patten-matching capability. For example, we cannot write

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00857))_

| entry | content |
| --- | --- |
| 57 | https://en.wikipedia.org/wiki/CAR_and_CDR |
| 58 | Kyle Simpson is the author of You Don't Know JS, available here |

<details>
<summary>Raw table text</summary>

```
57 https://en.wikipedia.org/wiki/CAR_and_CDR
58 Kyle Simpson is the author of You Don't Know JS, available here
```

</details>
