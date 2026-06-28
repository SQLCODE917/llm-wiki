---
page_id: javascriptallonge-expression
page_kind: concept
summary: Expression: 20 statement(s) and 30 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-expression@a72ad302acb36771f36fa03af74a9dec
---

# Expression

What [[javascriptallonge]] covers about expression:

## Statements

### reference types

- They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you're creating a new, distinct value even if it appears to be the same as some other array value. As we'll see, this is true of many other kinds of values, including functions , the main subject of this book. _(javascriptallonge.pdf (source-range-31a4cf47-00141))_

### A Rich Aroma: Basic Numbers

- JavaScript, like most languages, has a collection of literals. We saw that an expression consisting solely of numbers, like 42 , is a literal. It represents the number forty-two, which is 42 base 10. Not all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actually 34 base 10. _(javascriptallonge.pdf (source-range-31a4cf47-00146))_

### void

- There are many kinds of JavaScript statements, but the first kind is one we've already met. An expression is a JavaScript statement. Although they aren't very practical, these are valid JavaScript functions, and they return undefined when applied: _(javascriptallonge.pdf (source-range-31a4cf47-00242))_

- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined : _(javascriptallonge.pdf (source-range-31a4cf47-00246))_

### variables and bindings

- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary that maps variables to values by name. The x in the expression that we call a 'variable' is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-31a4cf47-00306))_

- The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-31a4cf47-00318))_

### That Constant Coffee Craving

- This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 . _(javascriptallonge.pdf (source-range-31a4cf47-00395))_

### the function keyword

- In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-31a4cf47-00526))_

### function declaration caveats 34

- Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. _(javascriptallonge.pdf (source-range-31a4cf47-00554))_

### magic names and fat arrows

- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-31a4cf47-00621))_

- But sometimes, a function is a small-f function. It's a simple representation of an expression to be computed. In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. _(javascriptallonge.pdf (source-range-31a4cf47-00633))_

### truthiness and the ternary operator

- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example: _(javascriptallonge.pdf (source-range-31a4cf47-00773))_

### || and && are control-flow operators

- This is more than just an optimization. It's best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not. _(javascriptallonge.pdf (source-range-31a4cf47-00799))_

### Self-Similarity

- We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-31a4cf47-00885))_

### literal object syntax

- Expressions can be used for keys as well. The syntax is to enclose the key's expression in [ and ] : _(javascriptallonge.pdf (source-range-31a4cf47-01082))_

### A Warm Cup: Basic Strings and Quasi-Literals

- Coffee and a Book An expression is any valid unit of code that resolves to a value.-Mozilla Development Network: Expressions and operators 87 _(javascriptallonge.pdf (source-range-31a4cf47-01499))_

### quasi-literals

- Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string. _(javascriptallonge.pdf (source-range-31a4cf47-01507))_

### iterables

- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-31a4cf47-01557))_

### lazy collection operations

- This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-31a4cf47-01792))_

### How to run the examples

- Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser. _(javascriptallonge.pdf (source-range-31a4cf47-01977))_


## Technical atoms

### Technical frame 1: reference types

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00138))_

> Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42 ? Try these for yourself:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00137))_

```
[2-1, 2, 2+1] [1, 1+1, 1+1+1]
```

### Technical frame 2: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00244))_

> As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00243))_

```
() => { 2 + 2 } () => { 1 + 1; 2 + 2 }
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

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00251))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 5: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00252))_

```
(() => { return 0 })() //=> 0 (() => { return 1 })() //=> 1 (() => { return 'Hello ' + 'World' })() // 'Hello World'
```

### Technical frame 6: void

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00249))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00254))_

```
(() => { 1 + 1; return 2 + 2 })() //=> 4
```

### Technical frame 7: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00395))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00392))_

```
((PI) => // ???? )(3.14159265)
```

### Technical frame 8: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00536))_

> Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body?

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00535))_

```
( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false ( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(2) //=> true
```

### Technical frame 9: the function keyword

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00538))_

> even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00537))_

```
even //=> Can't find variable: even
```

### Technical frame 10: function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00554))_

> Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00553))_

```
( function (camelCase) { return fizzbuzz(); if (camelCase) { function fizzbuzz () { return "Fizz" + "Buzz"; } } else { function fizzbuzz () { return "Fizz" + "Buzz"; } } })( true ) //=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?
```

### Technical frame 11: function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00555))_

> Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00554))_

> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

### Technical frame 12: function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00557))_

> The parentheses make this an expression, not a function declaration.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00556))_

```
function trueDat () { return true } But this is not: ( function trueDat () { return true })
```

### Technical frame 13: magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00623))_

> But if we use a fat arrow, arguments will be defined in the outer environment, the one defined with function . And thus arguments[0] will refer to "outer" , not to "inner" :

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00622))_

```
( function () { return ( function () { return arguments[0]; })('inner'); })('outer') //=> "inner"
```

### Technical frame 14: truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00775))_

> Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00774))_

```
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den';
```

### Technical frame 15: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01090))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01083))_

```
{ ["p" + "i"]: 3.14159265 } //=> {"pi":3.14159265}
```

### Technical frame 16: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01090))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01089))_

```
const SecretDecoderRing = { encode: function encode (plaintext) { return plaintext .split('') .map( char => char .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); }, decode: function decode (cyphertext) { return cyphertext .split('') .map( char => char .charCodeAt() ) .map( code => code - 1 ) .map( code => String.fromCharCode(code) ) .join(''); } }
```

### Technical frame 17: literal object syntax

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01090))_

> It is very common to associate named function expressions with keys in objects, and there is a 'compact method syntax' for binding named function expressions to keywords:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01091))_

```
const SecretDecoderRing = { encode (plaintext) { return plaintext .split('') .map( char => char .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); }, decode (cyphertext) { return cyphertext .split('') .map( char => char .charCodeAt() ) .map( code => code - 1 ) .map( code => String.fromCharCode(code) ) .join(''); } }
```

### Technical frame 18: quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01507))_

> Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this 'unquoting,' the more contemporary term is 'interpolation.' An unquoted expression is inserted in a quasi-literal with ${expression} . The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01506))_

```
`foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz'
```

### Technical frame 19: quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01510))_

> Aquasi-literal is computationally equivalent to an expression using + . So the above expression could also be written:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01509))_

```
`A popular number for nerds is ${ 40 + 2 } ` //=> 'A popular number for nerds is 42'
```

### Technical frame 20: quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01512))_

```
'A popular number for nerds is ' + (40 + 2) //=> 'A popular number for nerds is 42'
```

### Technical frame 21: quasi-literals

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01513))_

> However, there is a big semantic difference between a quasi-literal and an expression. Quasi-literals are expressions that resemble their result. They're easier to read and it's easier to avid errors like the following:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01514))_

```
'A popular number for nerds is' + (40 + 2) //=> 'A popular number for nerds is42'
```

### Technical frame 22: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01562))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01560))_

```
const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this .array[ this .index] = undefined ; if ( this .index >= 0) { this .index -= 1 } return value }, isEmpty () { return this .index < 0 }, [Symbol.iterator] () { let iterationIndex = this .index; return { next () { if (iterationIndex > this .index) { iterationIndex = this .index; } if (iterationIndex < 0) { return {done: true }; } else { return {done: false , value: this .array[iterationIndex--]} } } } } }); const stack = Stack3();
```

### Technical frame 23: iterables

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01562))_

> The for...of loop works directly with any object that is iterable , meaning it works with any object that has a Symbol.iterator method that returns an object iterator. Here's another linked list, this one is iterable:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01561))_

```
stack.push(2000); stack.push(10); stack.push(5) const collectionSum = (collection) => { const iterator = collection[Symbol.iterator](); let eachIteration, sum = 0; while ((eachIteration = iterator.next(), !eachIteration.done)) { sum += eachIteration.value; } return sum } collectionSum(stack) //=> 2015 Using [Symbol.iterator] instead of .iterator seems like adding an extra moving part for nothing. Do we get anything in return? Indeed we do. Behold the for...of loop: const iterableSum = (iterable) => { let sum = 0; for ( const num of iterable) { sum += num; } return sum } iterableSum(stack) //=> 2015
```

### Technical frame 24: lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01787))_

> Both expressions evaluate to 220 . And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01786))_

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0) Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) .map((x) => x * x) .filter((x) => x % 2 == 0) .reduce((seed, element) => seed + element, 0)
```

### Technical frame 25: lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01792))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01789))_

> When working with very large collections and many operations, this can be important.

### Technical frame 26: lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01792))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01790))_

> The effect is even more pronounced when we use methods like first , until , or take :

### Technical frame 27: How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01977))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01975))_

```
100 101 http://babeljs.io/
```

### Technical frame 28: How to run the examples

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01977))_

> Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01976))_

```
const before = (decoration) => (method) => function (...args) { decoration.apply( this , args); return method.apply( this , args) }; And it would be 'transpiled' into: var before = function (decoration) { return function (method) { return function () { for ( let _len = arguments.length, args = Array(_len), _key = 0; _key < _le\ n; _key++) { args[_key] = arguments[_key]; } decoration.apply( this , args); return method.apply( this , args); }; }; };
```

### Technical atom 29

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00103))_

| entry | content |
| --- | --- |
| 8 | https://en.wikipedia.org/wiki/Expression_ |
| 9 | https://en.wikipedia.org/wiki/Value_ |

<details>
<summary>Raw table text</summary>

```
Prelude: Values and Expressions over Coffee
The following material is extremely basic, however like most stories, the best way to begin is to start at the very beginning.
Imagine we are visiting our favourite coffee shop. They will make for you just about any drink you desire, from a short, intense espresso ristretto through a dry cappuccino, up to those coffee-flavoured desert concoctions featuring various concentrated syrups and milks. (You tolerate the existence of sugary drinks because they provide a sufficient profit margin to the establishment to finance your hanging out there all day using their WiFi and ordering a $3 drink every few hours.)
You express your order at one end of their counter, the folks behind the counter perform their magic, and deliver the coffee you value at the other end. This is exactly how the JavaScript environment works for the purpose of this book. We are going to dispense with web servers, browsers and other complexities and deal with this simple model: You give the computer an expression 8 , and it returns a value 9 , just as you express your wishes to a barista and receive a coffee in return.
8 https://en.wikipedia.org/wiki/Expression_
9 https://en.wikipedia.org/wiki/Value_
```

</details>

### Technical atom 30

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00114))_

> Let's try this as well with something else the computer understands easily:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00116))_

| entry | content |
| --- | --- |
| 10 | Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer. |
| 11 | In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. |

<details>
<summary>Raw table text</summary>

```
10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' and so does the computer.
11 In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values.
```

</details>


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from variables and bindings: The expression 'x' (the right side of the function) is evaluated within the environment we just created.; Function shares technical record from void: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } (2 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-result]] - shared statements and technical atoms: Result shares source evidence from How to run the examples: Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see t ... [truncated]; Result shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared statement(s), 5 shared atom(s))
- [[javascriptallonge-array]] - shared statements and technical atoms: Array shares source evidence from reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated]; Array shares technical record from reference types: [2-1, 2, 2+1] [1, 1+1, 1+1+1] (2 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements and technical atoms: Evaluate shares source evidence from reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated]; Evaluate shares technical record from void: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-literal]] - shared statements and technical atoms: Literal shares source evidence from Self-Similarity: We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment.; Literal shares technical record from quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared statement(s), 4 shared atom(s))
- [[javascriptallonge-block]] - shared statements and technical atoms: Block shares source evidence from void: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :; Block shares technical record from void: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-function-keyword]] - shared statements and technical atoms: the function keyword shares source evidence from the function keyword: In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, b ... [truncated]; the function keyword shares technical record from the function keyword: ( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false ( function even (n) { if (n === 0) { return true } else return !even(n - ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-iterator]] - shared statements and technical atoms: Iterator shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Iterator shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-method]] - shared statements and technical atoms: Method shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Method shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms: Object shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Object shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-symbol]] - shared statements and technical atoms: Symbol shares source evidence from iterables: The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object.; Symbol shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from reference types: They look the same, but if you examine them with === , you see that they are different. Every time you evaluate an expression (including typing something in) to crea ... [truncated]; Value shares technical table: Prelude: Values and Expressions over Coffee The following material is extremely basic, however like most stories, the best way to begin is to start at the very begin ... [truncated] (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-coffee]] - shared statements and technical atoms: Coffee shares source evidence from A Warm Cup: Basic Strings and Quasi-Literals: Coffee and a Book An expression is any valid unit of code that resolves to a value.-Mozilla Development Network: Expressions and operators 87; Coffee shares technical table: Prelude: Values and Expressions over Coffee The following material is extremely basic, however like most stories, the best way to begin is to start at the very begin ... [truncated] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-matter]] - shared statements and technical atoms: Matter shares source evidence from void: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined :; Matter shares technical record from void: (() => { 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (() => { 1 + 1; 2 + 2 })() //=> undefined (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-second]] - shared statements and technical atoms: Second shares source evidence from truthiness and the ternary operator: The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:; Second shares technical record from truthiness and the ternary operator: const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-third]] - shared statements and technical atoms: Third shares source evidence from truthiness and the ternary operator: The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:; Third shares technical record from truthiness and the ternary operator: const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-return]] - shared technical atoms: Return shares technical record from void: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } (4 shared atom(s))
- [[javascriptallonge-evaluating]] - shared technical atoms: Evaluating shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (3 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from void: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } (3 shared atom(s))
- [[javascriptallonge-quasi]] - shared technical atoms: Quasi shares technical record from quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (3 shared atom(s))
- [[javascriptallonge-bound]] - shared technical atoms: Bound shares technical record from the function keyword: ( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false ( function even (n) { if (n === 0) { return true } else return !even(n - ... [truncated] (2 shared atom(s))
- [[javascriptallonge-environment]] - shared technical atoms: Environment shares technical record from the function keyword: ( function even (n) { if (n === 0) { return true } else return !even(n - 1) })(5) //=> false ( function even (n) { if (n === 0) { return true } else return !even(n - ... [truncated] (2 shared atom(s))
- [[javascriptallonge-follow]] - shared technical atoms: Follow shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-instead]] - shared technical atoms: Instead shares technical record from iterables: const Stack3 = () => ({ array: [], index: -1, push (value) { return this .array[ this .index += 1] = value; }, pop () { const value = this .array[ this .index]; this ... [truncated] (2 shared atom(s))
- [[javascriptallonge-language]] - shared technical atoms: Language shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (2 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from magic names and fat arrows: ( function () { return ( function () { return arguments[0]; })('inner'); })('outer') //=> "inner" (1 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from That Constant Coffee Craving: ((PI) => // ???? )(3.14159265) (1 shared atom(s))
- [[javascriptallonge-code]] - shared technical atoms: Code shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-declaration]] - shared technical atoms: Declaration shares technical record from function declaration caveats 34: function trueDat () { return true } But this is not: ( function trueDat () { return true }) (1 shared atom(s))
- [[javascriptallonge-feature]] - shared technical atoms: Feature shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-needn]] - shared technical atoms: Needn shares technical table: 10 Technically, it's a representation of a value using Base10 notation, but we needn't worry about that in this book. You and I both understand that this means '42,' ... [truncated] (1 shared atom(s))
- [[javascriptallonge-program]] - shared technical atoms: Program shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-programmer]] - shared technical atoms: Programmer shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-rule]] - shared technical atoms: Rule shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-string]] - shared technical atoms: String shares technical record from quasi-literals: `foobar` //=> 'foobar' `fizz` + `buzz` //=> 'fizzbuzz' (1 shared atom(s))
- [[javascriptallonge-write]] - shared technical atoms: Write shares technical record from void: So how do we get a function that evaluates a block to return a value when applied? (1 shared atom(s))
- [[javascriptallonge-idea]] - shared statements: Idea shares source evidence from Self-Similarity: We saw that the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. (1 shared statement(s))
- [[javascriptallonge-variable]] - shared statements: Variable shares source evidence from variables and bindings: Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
