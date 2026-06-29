---
page_id: javascriptallonge-array
page_kind: concept
summary: Array: 15 statement(s) and 14 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-array@cbfc725ac0e4149327596ae0a3f283b6
---

# Array

What [[javascriptallonge]] covers about array:

## Statements

### Composing and Decomposing Data / Arrays and Destructuring Arguments

- While we have mentioned arrays briefly, we haven't had a close look at them. Arrays are JavaScript's 'native' representation of lists. Strings are important because they represent writing. Lists are important because they represent ordered collections of things, and ordered collections are a fundamental abstraction for making sense of reality. _(javascriptallonge.pdf (source-range-7239e085-00818))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

- JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array: _(javascriptallonge.pdf (source-range-7239e085-00820))_

- We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional: _(javascriptallonge.pdf (source-range-7239e085-00822))_

- This is an array with one element that is an array with one element that is an array with one element that is an array with one element that is an empty array. Although that seems like something nobody would ever construct, many students have worked with almost the exact same thing when they explored various means of constructing arithmetic from Set Theory. _(javascriptallonge.pdf (source-range-7239e085-00828))_

- Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-7239e085-00831))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

- Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract: _(javascriptallonge.pdf (source-range-7239e085-00834))_

- As we can see, JavaScript Arrays are zero-based 56 . _(javascriptallonge.pdf (source-range-7239e085-00836))_

- We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind? _(javascriptallonge.pdf (source-range-7239e085-00837))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

- There is another way to extract elements from arrays: Destructuring , a feature going back to Common Lisp, if not before. We saw how to construct an array literal using [ , expressions, , and ] . Here's an example of an array literal that uses a name: _(javascriptallonge.pdf (source-range-7239e085-00841))_

- The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do the same thing with more than one element: _(javascriptallonge.pdf (source-range-7239e085-00847))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

- Sometimes we need to extract arrays from arrays. Here is the most common pattern: Extracting the head and gathering everything but the head from an array: _(javascriptallonge.pdf (source-range-7239e085-00853))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

- That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore: _(javascriptallonge.pdf (source-range-7239e085-00865))_


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

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00827))_

```
[[[[[]]]]]
```

### Technical frame 4: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

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

### Technical frame 5: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

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

### Technical frame 6: Composing and Decomposing Data / Arrays and Destructuring Arguments / element references

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00837))_

> We know that every array is its own unique entity, with its own unique reference. What about the contents of an array? Does it store references to the things we give it? Or copies of some kind?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00839))_

```
const x = [],
a = [x];
a[0] === x
//=> true, arrays store references to the things you put in them.
```

### Technical frame 7: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00844))_

> The line const wrapped = [something]; is interesting. On the left hand is a name to be bound, and on the right hand is an array literal, a template for constructing an array, very much like a quasi-literal string.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00842))_

```
const wrap = (something) => [something];
Let’s expand it to use a block and an extra name:
const wrap = (something) => {
const wrapped = [something];
```

### Technical frame 8: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

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

### Technical frame 9: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays

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

### Technical frame 10: Composing and Decomposing Data / Arrays and Destructuring Arguments / gathering

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

### Technical frame 11: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00865))_

> That match would fail because the array doesn't have an element to assign to what . But this is not how JavaScript works. JavaScript tries its best to assign things, and if there isn't something that fits, JavaScript binds undefined to the name. Therefore:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00864))_

```
const [what] = [];
```

### Technical frame 12: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

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

### Technical frame 13: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching

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

### Technical frame 14: Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00878))_

> It looks like destructuring. It acts like destructuring. There is only one difference: We have not tried gathering. Let's do that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00877))_

```
const foo = () => ...
const bar = (name) => ...
const baz = (a, b, c) => ...
```


## Related pages

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: JavaScript has a literal syntax for creating an array: The [ and ] characters. We can create an empty array:; Javascript shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: [] //=> [] (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it co ... [truncated]; Literal shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: [] //=> [] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / element references: Array elements can be extracted using [ and ] as postfix operators. We pass an integer as an index of the element to extract:; Element shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / element references: const oneTwoThree = ["one", "two", "three"]; oneTwoThree[0] //=> 'one' oneTwoThree[1] //=> 'two' oneTwoThree[2] //=> 'three' (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-statement]] - shared statements and technical atoms: Statement shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays: The statement const [something] = wrapped; destructures the array represented by wrapped , binding the value of its single element to the name something . We can do ... [truncated]; Statement shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring arrays: const surname = (name) => { const [first, last] = name; return last; } surname(["Reginald", "Braithwaite"]) //=> "Braithwaite" (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching: const [what] = []; (3 shared atom(s))
- [[javascriptallonge-parameter]] - shared technical atoms: Parameter shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring parameters: const foo = () => ... const bar = (name) => ... const baz = (a, b, c) => ... (1 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching: const [...they] = []; they //=> [] const [which, what, . they //=> [] (1 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / destructuring is not pattern matching: const [...they] = []; they //=> [] const [which, what, . they //=> [] (1 shared atom(s))
- [[javascriptallonge-section-composing-and-decomposing-data-garbage-garbage-everywhere-so-why-arrays-ecae5c27]] - source section: Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays: Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointe ... [truncated]; Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays: And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it. (5 shared statement(s), 2 shared atom(s))

## Source

- [[javascriptallonge]]
