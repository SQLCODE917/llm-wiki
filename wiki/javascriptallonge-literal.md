---
page_id: javascriptallonge-literal
page_kind: concept
page_family: broad-topic
summary: Literal: 12 statement(s) and 9 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-literal@1b020f1ba1b6bbc8875b2ed3fd0f8c30
---

# Literal

What [[javascriptallonge]] covers about literal:


## Related pages

### Shared technical atoms

- [[javascriptallonge-quasi]] - shared statements and technical atoms: Quasi shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Quasi shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (4 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from Composing and Decomposing Data / Self-Similarity: We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment.; Expression shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it co ... [truncated]; Array shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: [] //=> [] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-list]] - shared technical atoms: List shares technical record from Composing and Decomposing Data / Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (2 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from Composing and Decomposing Data / Self-Similarity: [] //=> [] ["baz", ...[]] //=> ["baz"] ["bar", ...["baz"]] //=> ["bar","baz"] ["foo", ...["bar", "baz"]] //=> ["foo","bar","baz"] (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated]; Javascript shares technical record from Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals: [] //=> [] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-rest]] - shared statements and technical atoms: Rest shares source evidence from Composing and Decomposing Data / Self-Similarity: Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:; Rest shares technical record from Composing and Decomposing Data / Self-Similarity: const [first, ...rest] = []; first //=> undefined rest //=> []: const [first, ...rest] = ["foo"]; first //=> "foo" rest //=> [] const [first, ...rest] = ["foo", "bar ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-string]] - shared statements and technical atoms: String shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; String shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 1 shared atom(s))

### Shared claims

- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-idea]] - shared statements: Idea shares source evidence from Composing and Decomposing Data / Self-Similarity: We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. (1 shared statement(s))

### Topics

- [[javascriptallonge-quasi-literal]] - narrower topic: Quasi Literal shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a str ... [truncated]; Quasi Literal shares technical record from A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (4 shared statement(s), 3 shared atom(s))
## Statements by source section

### A Rich Aroma: Basic Numbers

- In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.Wikipedia 12 _(javascriptallonge.pdf (source-range-7239e085-00141))_

- JavaScript, like most languages, has a collection of literals. We saw that an expression consisting solely of numbers, like 42 , is a literal. It represents the number forty-two, which is 42 base 10. Not all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actually 34 base 10. _(javascriptallonge.pdf (source-range-7239e085-00142))_

### And also: / That Constant Coffee Craving / inside-out

- Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development. _(javascriptallonge.pdf (source-range-7239e085-00402))_

### Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

- Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements: _(javascriptallonge.pdf (source-range-7239e085-00831))_

### Composing and Decomposing Data / Self-Similarity

- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-7239e085-00885))_

- Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists: _(javascriptallonge.pdf (source-range-7239e085-00892))_

### A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

- JavaScript supports quasi-literal strings , a/k/a 'Template Strings' or 'String Interpolation Expressions.' A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g. _(javascriptallonge.pdf (source-range-7239e085-01505))_

- Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-7239e085-01507))_

- Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written: _(javascriptallonge.pdf (source-range-7239e085-01510))_

### A Warm Cup: Basic Strings and Quasi-Literals / evaluation time

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-7239e085-01519))_


## Technical atoms

### Technical frame 1: A Rich Aroma: Basic Numbers

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00145))_

> For example, the largest integer JavaScript can safely 14 handle is 9007199254740991 , or 2 '53' - 1 . Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00144))_

<a id="atom-technical-atom-a93f6fecaab38822"></a>

> The machine's representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer's behaviour surprises us if we don't know a little about what it's doing 'under the hood.'

### Technical frame 2: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00822))_

> We can create an array with one or more elements by placing them between the brackets and separating the items with commas. Whitespace is optional:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00821))_

<a id="atom-technical-atom-7fab0563ec943d7c"></a>

```
[]
//=> []
```

### Technical frame 3: Composing and Decomposing Data / Arrays and Destructuring Arguments / array literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00831))_

> Array literals are expressions, and arrays are reference types . We can see that each time an array literal is evaluated, we get a new, distinct array, even if it contains the exact same elements:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00832))_

<a id="atom-technical-atom-61efb6f3893fcfdd"></a>

```
[] === []
//=> false
[2 + 2] === [2 + 2]
//=> false
const array_of_one = () => [1];
array_of_one() === array_of_one()
//=> false
```

### Technical frame 4: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00892))_

> Thanks to the parallel between array literals + spreads with destructuring + rests, we can also use the same rules to decompose lists:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00891))_

<a id="atom-technical-atom-9d3e365c447e4d34"></a>

```
[]
//=> []
["baz", ...[]]
//=> ["baz"]
["bar", ...["baz"]]
//=> ["bar","baz"]
["foo", ...["bar", "baz"]]
//=> ["foo","bar","baz"]
```

### Technical frame 5: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00897))_

> Armed with our definition of an empty list and with what we've already learned, we can build a great many functions that operate on arrays. We know that we can get the length of an array using its .length . But as an exercise, how would we write a length function using just what we have already?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00895))_

<a id="atom-technical-atom-ab90397824182d0e"></a>

```
const [first, ...rest] = [];
first
//=> undefined
rest
//=> []:
const [first, ...rest] = ["foo"];
first
//=> "foo"
rest
//=> []
const [first, ...rest] = ["foo", "bar"];
first
//=> "foo"
rest
//=> ["bar"]
const [first, ...rest] = ["foo", "bar", "baz"];
first
//=> "foo"
rest
//=> ["bar","baz"]
For the purpose of this exploration, we will presume the following:61
const isEmpty = ([first, ...rest]) => first === undefined;
```

### Technical frame 6: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01507))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01506))_

<a id="atom-technical-atom-d1c1badbce303be3"></a>

```
`foobar`
//=> 'foobar'
`fizz` + `buzz`
//=> 'fizzbuzz'
```

### Technical frame 7: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01510))_

> Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01509))_

<a id="atom-technical-atom-a2109321f385f002"></a>

```
`A popular number for nerds is ${40 + 2}`
//=> 'A popular number for nerds is 42'
```

### Technical frame 8: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01512))_

<a id="atom-technical-atom-53001ff2df5804aa"></a>

```
'A popular number for nerds is ' + (40 + 2)
//=> 'A popular number for nerds is 42'
```

### Technical frame 9: A Warm Cup: Basic Strings and Quasi-Literals / quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01514))_

<a id="atom-technical-atom-9826aa7ca28708d6"></a>

```
'A popular number for nerds is' + (40 + 2)
//=> 'A popular number for nerds is42'
```


## Source

- [[javascriptallonge]]
