---
page_id: javascriptallonge-block
page_kind: concept
summary: Block: 10 statement(s) and 18 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-block@17ac927af9b4944a7cb9579eb4aab01e
---

# Block

What [[javascriptallonge]] covers about block:

## Statements

### A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

- ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful components and combine them into larger, fully featured programs. Features like destructuring, block-structured variables, iterables, generators, and the class keyword are poised to make JavaScript programming more expressive. _(javascriptallonge.pdf (source-range-7239e085-00021))_

### Or even: / the simplest possible block

- There's another thing we can put to the right of an arrow, a block . A block has zero or more statements , separated by semicolons. 18 _(javascriptallonge.pdf (source-range-7239e085-00210))_

- It returns the result of evaluating a block that has no statements. What would that be? Let's try it: _(javascriptallonge.pdf (source-range-7239e085-00213))_

### Or even: / back on the block

- We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21 _(javascriptallonge.pdf (source-range-7239e085-00236))_

- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-7239e085-00243))_

### And also: / That Constant Coffee Craving / nested blocks

- Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statement. In JavaScript, an if statement looks like this: _(javascriptallonge.pdf (source-range-7239e085-00438))_

### And also: / Building Blocks / partial application

- Another basic building block is partial application . When a function takes multiple arguments, we 'apply' the function to the arguments by evaluating it with all of the arguments, producing a value. But what if we only supply some of the arguments? In that case, we can't get the final value, but we can get a function that represents part of our application. _(javascriptallonge.pdf (source-range-7239e085-00591))_

### And also: / Summary / Functions

- Block bodies evaluate to whatever is returned with the return keyword, or to undefined . _(javascriptallonge.pdf (source-range-7239e085-00645))_

- Blocks also create scopes if const statements are within them. _(javascriptallonge.pdf (source-range-7239e085-00649))_

### Composing and Decomposing Data / Reassignment

- Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from: _(javascriptallonge.pdf (source-range-7239e085-01173))_


## Technical atoms

### Technical frame 1: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00025))_

> And the variable i is scoped locally to the code within the braces. Prior to ECMAScript 2015, JavaScript did not support block-structuring, so programmers borrowed a trick from the Scheme programming language, and would write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00024))_

```
for (int i = 0; i < array.length; ++i) {
// ...
}
```

### Technical frame 2: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00028))_

> Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00026))_

```
var i;
for (i = 0; i < array.length; ++i) {
(function (i) {
// ...
})(i)
}
```

### Technical frame 3: Or even: / the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00213))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00212))_

```
() => {}
```

### Technical frame 4: Or even: / the simplest possible block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00213))_

> It returns the result of evaluating a block that has no statements. What would that be? Let's try it:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00214))_

```
(() => {})()
//=> undefined
```

### Technical frame 5: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00236))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00235))_

```
(() => {})()
//=> undefined
```

### Technical frame 6: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00244))_

```
(() => { 2 + 2 })()
//=> undefined
(() => { 1 + 1; 2 + 2 })()
//=> undefined
(() => {
1 + 1;
2 + 2
})()
//=> undefined
```

### Technical frame 7: Or even: / back on the block

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

### Technical frame 8: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00442))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00439))_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else
return !even(x - 1);
}
return even(n)
}
```

### Technical frame 9: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00443))_

```
(n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
```

### Technical frame 10: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00444))_

```
}
return even(n)
}
And this also works:
((n) => {
const even = (x) => {
if (x === 0)
return true;
else {
const odd = (y) => !even(y);
return odd(x - 1);
}
}
return even(n)
})(42)
```

### Technical frame 11: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00446))_

> We've used a block as the else clause, and since it's a block, we've placed a const statement inside it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00445))_

```
//=> true
```

### Technical frame 12: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01173))_

> Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding of age in the outer environment, just like const . We go from:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01172))_

```
(() => {
let age = 49;
if (true) {
let age = 50;
}
return age;
})()
//=> 49
```

### Technical frame 13: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01174))_

```
{age: 49, '..': global-environment}
To:
{age: 50, '..': {age: 49, '..': global-environment}}
Then back to:
```

### Technical frame 14: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01175))_

```
{age: 49, '..': global-environment}
```

### Technical frame 15: Composing and Decomposing Data / Reassignment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01178))_

> Like evaluating variable labels, when a binding is rebound, JavaScript searches for the binding in the current environment and then each ancestor in turn until it finds one. It then rebinds the name in that environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01177))_

```
(() => {
let age = 49;
if (true) {
age = 50;
}
return age;
})()
//=> 50
```

### Technical frame 16: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01193))_

> Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01192))_

```
(() => {
var age = 49;
if (true) {
var age = 50;
}
return age;
})()
//=> 50
```

### Technical atom 17

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00236))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00234))_

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

### Technical atom 18

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00659))_

| entry | content |
| --- | --- |
| 45 | from Michael Fogus, Functional JavaScript |
| 46 | from Oliver Steele and the terse but handy node-ap |
| 47 | from James Halliday. |

<details>
<summary>Raw table text</summary>

```
Partial Application
In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libraries provide some form of partial application. You'll find examples in Lemonad 45 from Michael Fogus, Functional JavaScript 46 from Oliver Steele and the terse but handy node-ap 47 from James Halliday.
```

</details>


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Or even: / back on the block: We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21; Function shares technical record from Or even: / back on the block: (() => {})() //=> undefined (1 shared statement(s), 6 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from Or even: / back on the block: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :; Expression shares technical record from Or even: / back on the block: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-evaluating]] - shared statements and technical atoms: Evaluating shares source evidence from Or even: / the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Evaluating shares technical record from Or even: / the simplest possible block: () => {} (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-result]] - shared statements and technical atoms: Result shares source evidence from Or even: / the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Result shares technical record from Or even: / the simplest possible block: () => {} (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from Or even: / the simplest possible block: It returns the result of evaluating a block that has no statements. What would that be? Let's try it:; Return shares technical record from Or even: / the simplest possible block: () => {} (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-statement]] - shared statements and technical atoms: Statement shares source evidence from And also: / Summary / Functions: Blocks also create scopes if const statements are within them.; Statement shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else return !even(x - 1); } return even(n) } (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from Or even: / back on the block: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :; Evaluate shares technical record from Or even: / back on the block: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (2 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from Composing and Decomposing Data / Reassignment: Using let to bind 50 to age within the block does not change the binding of age in the outer environment because the binding of age in the block shadows the binding ... [truncated]; Bind shares technical record from Composing and Decomposing Data / Reassignment: (() => { let age = 49; if (true) { let age = 50; } return age; })() //=> 49 (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-matter]] - shared statements and technical atoms: Matter shares source evidence from Or even: / back on the block: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :; Matter shares technical record from Or even: / back on the block: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-partial-application]] - shared statements and technical atoms: partial application shares source evidence from And also: / Building Blocks / partial application: Another basic building block is partial application . When a function takes multiple arguments, we 'apply' the function to the arguments by evaluating it with all of ... [truncated]; partial application shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-seen]] - shared statements and technical atoms: Seen shares source evidence from And also: / That Constant Coffee Craving / nested blocks: Up to now, we've only ever seen blocks we use as the body of functions. But there are other kinds of blocks. One of the places you can find blocks is in an if statem ... [truncated]; Seen shares technical record from And also: / That Constant Coffee Craving / nested blocks: (n) => { const even = (x) => { if (x === 0) return true; else return !even(x - 1); } return even(n) } (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (4 shared atom(s))
- [[javascriptallonge-binding]] - shared technical atoms: Binding shares technical record from Composing and Decomposing Data / Reassignment: (() => { let age = 49; if (true) { let age = 50; } return age; })() //=> 49 (3 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: for (int i = 0; i < array.length; ++i) { // ... } (2 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (2 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (2 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (1 shared atom(s))
- [[javascriptallonge-declaration]] - shared technical atoms: Declaration shares technical record from Composing and Decomposing Data / Reassignment / mixing let and const / var: (() => { var age = 49; if (true) { var age = 50; } return age; })() //=> 50 (1 shared atom(s))
- [[javascriptallonge-ecmascript]] - shared technical atoms: Ecmascript shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (1 shared atom(s))
- [[javascriptallonge-functional]] - shared technical atoms: Functional shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-programming]] - shared technical atoms: Programming shares technical record from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: var i; for (i = 0; i < array.length; ++i) { (function (i) { // ... })(i) } (1 shared atom(s))
- [[javascriptallonge-recipe]] - shared technical atoms: Recipe shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-works-just-fine-because-arguments]] - shared technical atoms: Works Just Fine, Because Arguments[0 shares technical table: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical table: Partial Application In Building Blocks, we discussed partial application, but we didn't write a generalized recipe for it. This is such a common tool that many libra ... [truncated] (1 shared atom(s))
- [[javascriptallonge-feature]] - shared statements: Feature shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?: ECMAScript 2015 (formerly called ECMAScript 6 or 'ES6'), is ushering in a very large number of improvements to the way programmers can write small, powerful componen ... [truncated] (1 shared statement(s))
- [[javascriptallonge-section-or-even-back-on-the-block-b9587c98]] - source section: Or even: / back on the block shares source evidence from Or even: / back on the block: We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21; Or even: / back on the block shares technical record from Or even: / back on the block: back on the block Back to our function. We evaluated this: 19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This ... [truncated] (12 shared statement(s), 9 shared atom(s))

## Source

- [[javascriptallonge]]
