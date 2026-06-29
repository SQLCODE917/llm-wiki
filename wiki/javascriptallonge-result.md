---
page_id: javascriptallonge-result
page_kind: concept
summary: Result: 5 statement(s) and 11 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-result@9032a4a5306c4eda0160461dba49fe54
---

# Result

What [[javascriptallonge]] covers about result:

## Statements

### the simplest possible block

- It returns the result of evaluating a block that has no statements. What would that be? Let's try it: _(javascriptallonge.pdf (source-range-8eb13d6b-00217))_

### void

- We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21 _(javascriptallonge.pdf (source-range-8eb13d6b-00239))_

### partial application

- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-8eb13d6b-00598))_

### destructuring is not pattern matching

- From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-8eb13d6b-00869))_

### How to run the examples

- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-8eb13d6b-01975))_


## Technical atoms

### Technical frame 1: the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00217))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00216))_

```
() => {}
```

### Technical frame 2: the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00217))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00218))_

```
(() => {})() //=> undefined
```

### Technical frame 3: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00239))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00238))_

```
(() => {})() //=> undefined
```

### Technical frame 4: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00251))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 5: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00252))_

```
(() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World'
```

### Technical frame 6: void

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00254))_

```
(() => { 1 + 1; return 2 + 2 })() //=> 4
```

### Technical frame 7: partial application

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00600))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00599))_

```
const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9]
```

### Technical frame 8: destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00869))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00867))_

```
const [...they] = []; they //=> [] const [which, what, they //=> []
```

### Technical frame 9: How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01975))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01973))_

```
100 101 http://babeljs.io/
```

### Technical frame 10: How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01975))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01974))_

```
const before = (decoration) => (method) => function (...args) { decoration.apply( this , args); return method.apply( this , args) }; And it would be 'transpiled' into: var before = function (decoration) { return function (method) { return function () { for ( let _len = arguments.length, args = Array(_len), _key = 0; _key < _le\ n; _key++) { args[_key] = arguments[_key]; } decoration.apply( this , args); return method.apply( this , args); }; }; };
```

### Technical atom 11

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00564))_

| entry | content |
| --- | --- |
| 35 | https://en.wikipedia.org/wiki/Combinatory_logic |
| 36 | http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20 |

<details>
<summary>Raw table text</summary>

```
combinators
The word 'combinator' has a precise technical meaning in mathematics:
'A combinator is a higher-order function that uses only function application and earlier defined combinators to define a result from its arguments.'-Wikipedia 35
If we were learning Combinatorial Logic, we'd start with the most basic combinators like S , K , and I , and work up from there to practical combinators. We'd learn that the fundamental combinators are named after birds following the example of Raymond Smullyan's famous book To Mock a Mockingbird 36 .
35 https://en.wikipedia.org/wiki/Combinatory_logic
36 http://www.amazon.com/gp/product/B00A1P096Y/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=B00A1P096Y& linkCode=as2&tag=raganwald001-20
```

</details>


## Related pages

- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Return shares technical record from the simplest possible block: () => {} (2 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-evaluating]] - shared statements and technical atoms: Evaluating shares source evidence from the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Evaluating shares technical record from the simplest possible block: () => {} (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from void: We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21; Function shares technical record from void: (() => {})() //=> undefined (2 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from How to run the examples: Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see t ... [truncated]; Expression shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Block shares technical record from the simplest possible block: () => {} (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-pass]] - shared statements and technical atoms: Pass shares source evidence from destructuring is not pattern matching: From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can ... [truncated]; Pass shares technical record from destructuring is not pattern matching: const [...they] = []; they //=> [] const [which, what, they //=> [] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from destructuring is not pattern matching: From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can ... [truncated]; Value shares technical record from destructuring is not pattern matching: const [...they] = []; they //=> [] const [which, what, they //=> [] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from void: (() => {})() //=> undefined (3 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (2 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from destructuring is not pattern matching: const [...they] = []; they //=> [] const [which, what, they //=> [] (1 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared technical atoms: Evaluate shares technical record from void: (() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World' (1 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-follow]] - shared technical atoms: Follow shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from partial application: const mapWith = (fn) => (array) => map(array, fn); const squareAll = mapWith((n) => n * n); squareAll([1, 2, 3]) //=> [1, 4, 9] (1 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: combinators The word 'combinator' has a precise technical meaning in mathematics: 'A combinator is a higher-order function that uses only function application and ea ... [truncated] (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))

## Source

- [[javascriptallonge]]
