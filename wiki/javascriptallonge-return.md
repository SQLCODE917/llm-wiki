---
page_id: javascriptallonge-return
page_kind: concept
summary: Return: 15 statement(s) and 23 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-return@2783a53e3626f6faf6bea41653179366
---

# Return

What [[javascriptallonge]] covers about return:

## Statements

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

- We've seen () => 0 . We know that (() => 0)() returns 0 , and this is unsurprising. Likewise, the following all ought to be obvious: _(javascriptallonge.pdf (source-range-7239e085-00188))_

### Or even: / the simplest possible block

- It returns the result of evaluating a block that has no statements. What would that be? Let's try it: _(javascriptallonge.pdf (source-range-7239e085-00213))_

### Or even: / back on the block

- We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21 _(javascriptallonge.pdf (source-range-7239e085-00236))_

### And also: / Combinators and Function Decorators / higher-order functions

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-7239e085-00557))_

### And also: / Building Blocks / partial application

- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-7239e085-00597))_

### Picking the Bean: Choice and Truthiness / truthiness and operators

- Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-7239e085-00777))_

### Composing and Decomposing Data / Self-Similarity / folding

- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-7239e085-00949))_

### Yes. Consider this variation: / Functional Iterators / iterating

- Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iteratorSum function iterates over the elements by calling the iterator function repeatedly until it returns { done: true } . _(javascriptallonge.pdf (source-range-7239e085-01294))_

### Yes. Consider this variation: / Making Data Out Of Functions / the vireo

- Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. For arrays, we'd write cons = (first, second) => [first, second] . For objects we'd write: cons = (first, second) => {first, second} . In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-7239e085-01364))_

### Like this: / operations on ordered collections

- For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. They are equivalent to destructuring arrays with [first, ...rest] : _(javascriptallonge.pdf (source-range-7239e085-01607))_

### We'll keep it simple: / javascript's generators

- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-7239e085-01671))_

### We'll keep it simple: / generators are coroutines

- The body of our generator runs until it returns, ends, or encounters the next yield statement. There are no more lines of code, so it ends. _(javascriptallonge.pdf (source-range-7239e085-01698))_

### We'll keep it simple: / more generators

- We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-7239e085-01725))_

### We'll keep it simple: / yielding iterables

- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-7239e085-01731))_

### We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

- This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-7239e085-01791))_


## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00190))_

> Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00189))_

```
(() => 1)()
//=> 1
(() => "Hello, JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity)()
//=> Infinity
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00193))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00192))_

```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```

### Technical frame 3: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00196))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00197))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical frame 4: Or even: / the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00213))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00212))_

```
() => {}
```

### Technical frame 5: Or even: / the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00213))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00214))_

```
(() => {})()
//=> undefined
```

### Technical frame 6: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00236))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00235))_

```
(() => {})()
//=> undefined
```

### Technical frame 7: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00241))_

> As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00240))_

```
() => { 2 + 2 }
() => { 1 + 1; 2 + 2 }
```

### Technical frame 8: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00248))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 9: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00249))_

```
(() => { return 0 })()
//=> 0
(() => { return 1 })()
//=> 1
(() => { return 'Hello ' + 'World' })()
// 'Hello World'
```

### Technical frame 10: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00251))_

```
(() => {
1 + 1;
return 2 + 2
})()
//=> 4
```

### Technical frame 11: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00599))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00598))_

```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

### Technical frame 12: Picking the Bean: Choice and Truthiness / truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00779))_

> Programmers often take advantage of this behaviour to observe that !!(someExpression) will always evaluate to true is someExpression is truthy, and to false if it is not. So in JavaScript (and other languages with similar semantics), when you see something like !!currentUser() , this is an idiom that means 'true if currentUser is truthy.' Thus, a function like currentUser() is free to return null , or undefined , or false if there is no current user.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00778))_

```
!5
//=> false
!undefined
//=> true
```

### Technical frame 13: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00949))_

> And to return to our first example, our version of length can be written as a fold:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00950))_

```
const length = (array) => foldWith((first, rest) => 1 + rest, 0, array);
length([1, 2, 3, 4, 5])
//=> 5
```

### Technical frame 14: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01590))_

> This illustrates the general pattern of working with ordered collections: We make them iterables , meaning that they have a [Symbol.iterator] method, that returns an iterator . An iterator is also an object, but with a .next() method that is invoked repeatedly to obtain the elements in order.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01589))_

```
const mapWith = (fn, collection) =>
({
[Symbol.iterator] () {
const iterator = collection[Symbol.iterator]();
return {
next () {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

### Technical frame 15: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01593))_

> Numbers is an ordered collection. We invoke mapWith((x) => 2 * x, Numbers) and get Evens . Evens works just as if we'd written this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01592))_

```
const Evens = mapWith((x) => 2 * x, Numbers);
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
for (const i of Evens) {
console.log(i)
}
//=>
0
2
4
...
```

### Technical frame 16: Like this: / operations on ordered collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01609))_

> like our other operations, rest preserves the ordered collection semantics of its argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01608))_

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
const rest = (iterable) =>
({
[Symbol.iterator] () {
const iterator = iterable[Symbol.iterator]();
iterator.next();
return iterator;
}
});
```

### Technical frame 17: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01667))_

> When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01666))_

```
function * empty () {};
empty().next()
//=>
{"done":true}
```

### Technical frame 18: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01668))_

> Generator functions can take an argument. Let's use that to illustrate yield :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01667))_

> When we invoke empty , we get an iterator with no elements.

### Technical frame 19: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01671))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01672))_

```
only("you").next()
//=>
{"done":false, value: "you"}
only("the lonely").next()
//=>
{"done":false, value: "the lonely"}
```

### Technical frame 20: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01731))_

> We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01730))_

```
const isIterable = (something) =>
!!something[Symbol.iterator];
const TreeIterable = (iterable) =>
({
[Symbol.iterator]: function * () {
for (const e of iterable) {
if (isIterable(e)) {
for (const ee of TreeIterable(e)) {
yield ee;
}
}
else {
yield e;
}
}
}
})
for (const i of TreeIterable([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
```

### Technical frame 21: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01734))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01732))_

> But if you can write it as a simple generator, write it as a simple generator.

### Technical frame 22: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01791))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01790))_

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
```

### Technical atom 23

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00570))_

| entry | content |
| --- | --- |
| 37 | As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context. |
| 38 | We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args) |

<details>
<summary>Raw table text</summary>

```
function decorators
A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a variation of the argument function. Here's a ridiculously simple decorator: 38
37 As we'll discuss later, this implementation of the B Combinator is correct in languages like Scheme, but for truly general-purpose use in JavaScript, it needs to correctly manage the function context.
38 We'll see later why an even more useful version would be written (fn) => (...args) => !fn(...args)
```

</details>


## Related pages

- [[javascriptallonge-function-return-value]] - narrower topic: Function Return Value shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (2 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Or even: / back on the block: We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21; Function shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (6 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-result]] - shared statements and technical atoms: Result shares source evidence from Or even: / the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Result shares technical record from Or even: / the simplest possible block: () => {} (2 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-evaluating]] - shared statements and technical atoms: Evaluating shares source evidence from Or even: / the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Evaluating shares technical record from Or even: / the simplest possible block: () => {} (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from Or even: / the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Block shares technical record from Or even: / the simplest possible block: () => {} (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from We'll keep it simple: / javascript's generators: Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:; Iterator shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from And also: / Combinators and Function Decorators / higher-order functions: As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as argume ... [truncated]; Argument shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-mapwith]] - shared statements and technical atoms: Mapwith shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; Mapwith shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Like this: / operations on ordered collections: For completeness, here are two more handy iterable functions. first returns the first element of an iterable (if it has one), and rest returns an iterable that itera ... [truncated]; Element shares technical record from Like this: / operations on ordered collections: const first = (iterable) => iterable[Symbol.iterator]().next().value; const rest = (iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator] ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-alway]] - shared statements and technical atoms: Alway shares source evidence from Picking the Bean: Choice and Truthiness / truthiness and operators: Our logical operators ! , && , and || are a little more subtle than our examples above implied. ! is the simplest. It always returns false if its argument is truthy, ... [truncated]; Alway shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-code]] - shared statements and technical atoms: Code shares source evidence from We'll keep it simple: / Lazy and Eager Collections / lazy collection operations: This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iterati ... [truncated]; Code shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-length]] - shared statements and technical atoms: Length shares source evidence from Composing and Decomposing Data / Self-Similarity / folding: And to return to our first example, our version of length can be written as a fold:; Length shares technical record from Composing and Decomposing Data / Self-Similarity / folding: const length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) //=> 5 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from And also: / Building Blocks / partial application: The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one funct ... [truncated]; partial application shares technical record from And also: / Building Blocks / partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-version]] - shared statements and technical atoms: Version shares source evidence from Composing and Decomposing Data / Self-Similarity / folding: And to return to our first example, our version of length can be written as a fold:; Version shares technical record from Composing and Decomposing Data / Self-Similarity / folding: const length = (array) => foldWith((first, rest) => 1 + rest, 0, array); length([1, 2, 3, 4, 5]) //=> 5 (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from Or even: / back on the block: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } (4 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Or even: / back on the block: (() => {})() //=> undefined (4 shared atom(s))
- [[javascriptallonge-idea]] - shared technical atoms: Idea shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (2 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-operation]] - shared technical atoms: Operation shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-purpose]] - shared technical atoms: Purpose shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (2 shared atom(s))
- [[javascriptallonge-value]] - shared technical atoms: Value shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (2 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-behaviour]] - shared technical atoms: Behaviour shares technical record from Picking the Bean: Choice and Truthiness / truthiness and operators: !5 //=> false !undefined //=> true (1 shared atom(s))
- [[javascriptallonge-discussing]] - shared technical atoms: Discussing shares technical record from Like this: / operations on ordered collections: const mapWith = (fn, collection) => ({ [Symbol.iterator] () { const iterator = collection[Symbol.iterator](); return { next () { const {done, value} = iterator.next( ... [truncated] (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared technical atoms: Evaluate shares technical record from Or even: / back on the block: (() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World' (1 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-follow]] - shared technical atoms: Follow shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-method]] - shared technical atoms: Method shares technical record from We'll keep it simple: / Lazy and Eager Collections / lazy collection operations: Stack.from([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) .map((x) => x * x) .filter((x) => x % 2 == 0) .first() (1 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Like this: / operations on ordered collections: const first = (iterable) => iterable[Symbol.iterator]().next().value; const rest = (iterable) => ({ [Symbol.iterator] () { const iterator = iterable[Symbol.iterator] ... [truncated] (1 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: function decorators A function decorator is a higher-order function that takes one function as an argument, returns another function, and the returned function is a ... [truncated] (1 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements: Functional Iterators shares source evidence from Yes. Consider this variation: / Functional Iterators / iterating: Now this is something else. The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. The iterator ... [truncated] (1 shared statement(s))
- [[javascriptallonge-parameter]] - shared statements: Parameter shares source evidence from Yes. Consider this variation: / Making Data Out Of Functions / the vireo: Given that our latin data is represented as the function (selector) => selector("primus")("secundus") , our obvious next step is to make a function that makes data. ... [truncated] (1 shared statement(s))
- [[javascriptallonge-seen]] - shared statements: Seen shares source evidence from We'll keep it simple: / yielding iterables: We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function tha ... [truncated] (1 shared statement(s))
- [[javascriptallonge-writing]] - shared statements: Writing shares source evidence from We'll keep it simple: / more generators: We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of s ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
