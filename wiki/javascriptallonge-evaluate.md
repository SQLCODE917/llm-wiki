---
page_id: javascriptallonge-evaluate
page_kind: concept
summary: Evaluate: 9 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-evaluate@d4c9c60c2bf12c55214736d6c4767536
---

# Evaluate

What [[javascriptallonge]] covers about evaluate:

## Statements

### reference types

- They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. _(javascriptallonge.pdf (source-range-31a4cf47-00141))_

### undefined

- No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-) _(javascriptallonge.pdf (source-range-31a4cf47-00226))_

### void

- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-31a4cf47-00246))_

### it's always the environment

- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-31a4cf47-00369))_

### Functions

- Block bodies evaluate to whatever is returned with the return keyword, or to undefined . _(javascriptallonge.pdf (source-range-31a4cf47-00646))_

### truthiness and the ternary operator

- JavaScript inherited an operator from the C family of languages, the ternary operator. It's the only operator that takes three arguments. It looks like this: first ? second : third . It evaluates first , and if first is 'truthy', it evaluates second and that is its value. If first is not truthy, it evaluates third and that is its value. _(javascriptallonge.pdf (source-range-31a4cf47-00768))_

- Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true . _(javascriptallonge.pdf (source-range-31a4cf47-00775))_

### evaluation time

- JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" , it is bound to 'Arthur Dent' , the value of the parameter when the function is invoked. _(javascriptallonge.pdf (source-range-31a4cf47-01519))_

### iterables

- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-31a4cf47-01557))_


## Technical atoms

### Technical frame 1: undefined

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00226))_

> No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00225))_

```
undefined === undefined //=> true (() => {})() === (() => {})() //=> true (() => {})() === undefined //=> true
```

### Technical frame 2: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00235))_

> void is an operator that takes any value and evaluates to undefined , always. So, when we deliberately want an undefined value, should we use the first, second, or third form? 19 The answer is, use void . By convention, use void 0 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00234))_

```
void 0 //=> undefined void 1 //=> undefined void (2 + 2) //=> undefined
```

### Technical frame 3: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00247))_

```
(() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined
```

### Technical frame 4: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00252))_

```
(() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World'
```

### Technical frame 5: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00361))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00359))_

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical frame 6: it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00368))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00367))_

```
(x, y, z) => x + y + z
```

### Technical frame 7: truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00775))_

> Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00774))_

```
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den';
```

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00239))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00237))_

| entry | content |
| --- | --- |
| 19 | Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace. |
| 20 | As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea. |

<details>
<summary>Raw table text</summary>

```
back on the block
Back to our function. We evaluated this:
19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace.
20 As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea.
```

</details>


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from it's always the environment: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial applicatio ... [truncated]; Function shares technical record from void: (() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World' (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated]; Expression shares technical record from void: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from void: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :; Block shares technical record from void: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from truthiness and the ternary operator: Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .; Javascript shares technical record from void: void 0 //=> undefined void 1 //=> undefined void (2 + 2) //=> undefined (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-matter]] - shared statements and technical atoms: Matter shares source evidence from undefined: No matter how you evaluate undefined , you get an identical value back. undefined is a value that means 'I don't have a value.' But it's still a value :-); Matter shares technical record from undefined: undefined === undefined //=> true (() => {})() === (() => {})() //=> true (() => {})() === undefined //=> true (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-program]] - shared statements and technical atoms: Program shares source evidence from it's always the environment: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial applicatio ... [truncated]; Program shares technical record from it's always the environment: (x, y, z) => x + y + z (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-language]] - shared statements and technical atoms: Language shares source evidence from it's always the environment: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial applicatio ... [truncated]; Language shares technical record from it's always the environment: (x, y, z) => x + y + z (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-programming]] - shared statements and technical atoms: Programming shares source evidence from it's always the environment: The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial applicatio ... [truncated]; Programming shares technical record from it's always the environment: (x, y, z) => x + y + z (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated]; Value shares technical record from undefined: undefined === undefined //=> true (() => {})() === (() => {})() //=> true (() => {})() === undefined //=> true (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-second]] - shared technical atoms: Second shares technical record from void: void 0 //=> undefined void 1 //=> undefined void (2 + 2) //=> undefined (2 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (1 shared atom(s))
- [[javascriptallonge-evaluating]] - shared technical atoms: Evaluating shares technical record from void: (() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World' (1 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (1 shared atom(s))
- [[javascriptallonge-result]] - shared technical atoms: Result shares technical record from void: (() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World' (1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from void: (() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World' (1 shared atom(s))
- [[javascriptallonge-third]] - shared technical atoms: Third shares technical record from truthiness and the ternary operator: const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; (1 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (1 shared atom(s))
- [[javascriptallonge-array]] - shared statements: Array shares source evidence from reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated] (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))
- [[javascriptallonge-literal]] - shared statements: Literal shares source evidence from evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-method]] - shared statements: Method shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))
- [[javascriptallonge-quasi]] - shared statements: Quasi shares source evidence from evaluation time: JavaScript evaluates the quasi-literal when the function is invoked and the quasi-literal inside the function's body is evaluated. Thus, name is not bound to "Harry" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-symbol]] - shared statements: Symbol shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. (1 shared statement(s))

## Source

- [[javascriptallonge]]
