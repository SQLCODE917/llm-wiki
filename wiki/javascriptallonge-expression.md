---
page_id: javascriptallonge-expression
page_kind: concept
summary: Expression: 14 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-expression@3280c42d42710cedcd1185470120cb3c
---

# Expression

What [[javascriptallonge]] covers about expression:

## Statements

### values are expressions

- xiv

Prelude: Values and Expressions over Coffee

## **values are expressions**

All values are expressions. Say you hand the barista a café Cubano. Yup, you hand over a cup with some coffee infused through partially caramelized sugar. You say, “I want one of these.” The barista is no fool, she gives it straight back to you, and you get exactly what you want. Thus, a café Cubano is an expression (you can use it to place an order) and a value (you get it back from the barista).

Let’s try this with something the computer understands easily:

## 42

Is this an expression? A value? Neither? Or both?

The answer is, this is both an expression _and_ a value.[10] The way you can tell that it’s both is very easy: When you type it into JavaScript, you get the same thing back, just like our café Cubano:

## 42

_//=> 42_

All values are expressions. That’s easy! Are there any other kinds of expressions? Sure! let’s go back to the coffee shop. Instead of handing over the finished coffee, we can hand over the ingredients. Let’s hand over some ground coffee plus some boiling water.

Astute readers will realize we’re omitting something. Congratulations! Take a sip of espresso. We’ll get to that in a moment.

Now the barista gives us back an espresso. And if we hand over the espresso, we get the espresso right back. So, boiling water plus ground coffee is an expression, but it isn’t a value.[11] Boiling water is a value. Ground coffee is a value. Espresso is a value. Boiling water plus ground coffee is an expression.

Let’s try this as well with something else the computer understands easily:

> "JavaScript" + " " + "Allonge"

> _//=> "JavaScript Allonge"_

> 10Technically, it’s a _representation_ of a value using Base10 notation, but we needn’t worry about that in this book. You and I both understand that this means “42,” and so does the computer.

> 11In some languages, expressions are a kind of value unto themselves and can be manipulated. The grandfather of such languages is Lisp. JavaScript is not such a language, expressions in and of themselves are not values. _(javascriptallonge.pdf (source-range-83ecb080-00030))_

### values and identity

- xviii

Prelude: Values and Expressions over Coffee

An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like:

[2-1, 2, 2+1] [1, 1+1, 1+1+1] Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42? Try these for yourself:

[2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other array also looks like [1, 2, 3]. It’s as if JavaScript is generating new cups of coffee with serial numbers on the bottom.

They look the same, but if you examine them with ===, you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. As we’ll see, this is true of many other kinds of values, including _functions_ , the main subject of this book. _(javascriptallonge.pdf (source-range-83ecb080-00035))_

### A Rich Aroma: Basic Numbers

- ## **A Rich Aroma: Basic Numbers**

**==> picture [469 x 352] intentionally omitted <==**

**Mathematics and Coffee**

In computer science, a literal is a notation for representing a fixed value in source code. Almost all programming languages have notations for atomic values such as integers, floating-point numbers, and strings, and usually for booleans and characters; some also have notations for elements of enumerated types and compound values such as arrays, records, and objects. An anonymous function is a literal for the function type.— Wikipedia[12] JavaScript, like most languages, has a collection of literals. We saw that an expression consisting solely of numbers, like 42, is a literal. It represents the number forty-two, which is 42 base 10. Not

> 12https://en.wikipedia.org/wiki/Literal_(computer_programming) _(javascriptallonge.pdf (source-range-83ecb080-00037))_

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

7

## **As Little As Possible About Functions, But No Less**

In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let’s start with the second simplest possible function.[16] In JavaScript, it looks like this:

## () => 0

This is a function that is applied to no values and returns 0. Let’s verify that our function is a value like all others:

- (() => 0) _//=> [Function]_ What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else.

> 16 The simplest possible function is () => {}, we’ll see that later. _(javascriptallonge.pdf (source-range-83ecb080-00044))_

- The first sip: Basic Functions

8

I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function.

## **functions and identities**

You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not.

Which kind are functions? Let’s try them out and see. For reasons of appeasing the JavaScript parser, we’ll enclose our functions in parentheses: (() => 0) === (() => 0) _//=> false_

Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. “Function” is a reference type.

## **applying functions**

Let’s put functions to work. The way we use functions is to _apply_ them to zero or more values called _arguments_ . Just as 2 + 2 produces a value (in this case 4), applying a function to zero or more arguments produces a value as well.

Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. Let’s call the arguments _args_ . Here’s how to apply a function to some arguments:

## _fn_expr_ ( _args_ )

Right now, we only know about one such expression: () => 0, so let’s use it. We’ll put it in parentheses[17] to keep the parser happy, like we did above: (() => 0). Since we aren’t giving it any arguments, we’ll simply write () after the expression. So we write: (() => 0)() _//=> 0_

> 17If you’re used to other programming languages, you’ve probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages! _(javascriptallonge.pdf (source-range-83ecb080-00045))_

- The first sip: Basic Functions

9

## **functions that return values and evaluate expressions**

We’ve seen () => 0. We know that (() => 0)() returns 0, and this is unsurprising. Likewise, the following all ought to be obvious: (() => 1)() _//=> 1_ (() => "Hello, JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** )() _//=> Infinity_

Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2. Can we put an expression to the right of the arrow?

(() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)()?

Let’s try it: (() => (() => 0)())() _//=> 0_

Yes we can! Functions can return the value of evaluating another function.

When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out. So we can also write: _(javascriptallonge.pdf (source-range-83ecb080-00046))_

- 13

The first sip: Basic Functions

## (() => {})()

_//=> undefined_

We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] Something like: { statement[1] ; statement[2] ; statement[3] ; ... ; statement[n] } We haven’t discussed these _statements_ . What’s a statement?

There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: () => { 1 + 1; 2 + 2 } But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: (() => { 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator:

> 21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00050))_

### That Constant Coffee Craving

- 44

The first sip: Basic Functions

( **function** (camelCase) { **return** fizzbuzz(); **if** (camelCase) { **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } } **else** { **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } } })( **true** ) _//=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?_

Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. So this is a function declaration: **function** trueDat () { **return true** } But this is not:

( **function** trueDat () { **return true** }) The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-83ecb080-00080))_

### Magic Names

- 52

The first sip: Basic Functions **const** plus = **function** () { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_

When discussing objects, we’ll discuss properties in more depth. Here’s something interesting about arguments: **const** howMany = **function** () { **return** arguments['length']; } howMany() _//=> 0_ howMany('hello') _//=> 1_ howMany('sharks', 'are', 'apex', 'predators') _//=> 4_

The most common use of the arguments binding is to build functions that can take a variable number of arguments. We’ll see it used in many of the recipes, starting off with partial application and ellipses.

## **magic names and fat arrows**

The magic names this and arguments have a different behaviour when you invoke a function that was defined with a fat arrow: Instead of being bound when the function is invoked, the fat arrow function always acquires the bindings for this and arguments from its enclosing scope, just like any other binding.

For example, when this expression’s inner function is defined with function, arguments[0] refers to its only argument, "inner": _(javascriptallonge.pdf (source-range-83ecb080-00091))_

- The first sip: Basic Functions

54 **const** row = **function** () { **return** mapWith( **function** (column) { **return** column * arguments[0] }, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] ) } row(3) _//=> [1,4,9,16,25,36,49,64,81,100,121,144]_ Now our inner function binds arguments[0] every time it is invoked, so we get the same result as if we’d written function (column) { return column * column }.

Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it’s a first-class entity in the code.

But sometimes, a function is a small-f function. It’s a simple representation of an expression to be computed. In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply.

Having magic variables apply to Big-F functions but not to small-G functions makes it much easier to use small-F functions as syntax, treating them as expressions or blocks that can be passed to functions like mapWith. _(javascriptallonge.pdf (source-range-83ecb080-00093))_

### Left-Variadic Functions

- 75

Picking the Bean: Choice and Truthiness **const** even = (n) => n === 0 || (n !== 1 && even(n - 2)) even(42) _//=> true_

If n === 0, JavaScript does not evaluate (n !== 1 && even(n - 2)). This is very important! Imagine that JavaScript evaluated both sides of the || operator before determining its value. n === 0 would be true. What about (n !== 1 && even(n - 2))? Well, it would evaluate even(n - 2), or even(-2) This leads us to evaluate n === 0 || (n !== 1 && even(n - 2)) all over again, and this time we end up evaluating even(-4). And then even(-6). and so on and so forth until JavaScript throws up its hands and runs out of stack space.

But that’s not what happens. || and && have _short-cut semantics_ . In this case, if n === 0, JavaScript does not evaluate (n !== 1 && even(n - 2)). Likewise, if n === 1, JavaScript evaluates n !== 1 && even(n - 2) as false without ever evaluating even(n - 2).

This is more than just an optimization. It’s best to think of || and && as control-flow operators. The expression on the left is always evaluated, and its value determines whether the expression on the right is evaluated or not.

## **function parameters are eager**

In contrast to the behaviour of the ternary operator, ||, and &&, function parameters are always : _eagerly evaluated_ **const** or = (a, b) => a || b **const** and = (a, b) => a && b **const** even = (n) => or(n === 0, and(n !== 1, even(n - 2))) even(42) _//=> Maximum call stack size exceeded._

Now our expression or(n === 0, and(n !== 1, even(n - 2))) is calling functions, and JavaScript always evaluates the expressions for parameters before passing the values to a function to invoke. This leads to the infinite recursion we fear.

If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don’t need anything like this for or and and, but to demonstrate the technique: _(javascriptallonge.pdf (source-range-83ecb080-00119))_

### Plain Old JavaScript Objects

- Composing and Decomposing Data

111 **const** date = { year: 2012, month: 6, day: 14 }; date['day'] === date.day _//=> true_

Expressions can be used for keys as well. The syntax is to enclose the key’s expression in [ and ]:

{ ["p" + "i"]: 3.14159265 } _//=> {"pi":3.14159265}_ All containers can contain any value, including functions or other containers, like a fat arrow function: **const** Mathematics = { abs: (a) => a < 0 ? -a : a }; Mathematics.abs(-5) _//=> 5_ Or proper functions: **const** SecretDecoderRing = { encode: **function** (plaintext) { **return** plaintext .split('') .map( **char** => **char** .charCodeAt() ) .map( code => code + 1 ) .map( code => String.fromCharCode(code) ) .join(''); }, decode: **function** (cyphertext) { **return** cyphertext .split('') .map( **char** => **char** .charCodeAt() ) .map( code => code - 1 ) .map( code => String.fromCharCode(code) ) .join(''); } } Or named function expressions: _(javascriptallonge.pdf (source-range-83ecb080-00161))_

### A Warm Cup: Basic Strings and Quasi-Literals

- A Warm Cup: Basic Strings and Quasi-Literals

180

An expression is any valid unit of code that resolves to a value.—Mozilla Development Network: Expressions and operators[87] Like most programming languages, JavaScript also has string literals, like 'fubar' or 'fizzbuzz'. Special characters can be included in a string literal by means of an _escape sequence_ . For example, the escape sequence \n inserts a newline character in a string literal, like this: 'first line\nsecond line'.

There are operators that can be used on strings. The most common is +, it _concatenates_ : 'fu' + 'bar' _//=> 'fubar'_

String manipulation is extremely common in programming. Writing is a big part of what makes us human, and strings are how JavaScript and most other languages represent writing.

## **quasi-literals**

JavaScript supports _quasi-literal strings_ , a/k/a “Template Strings” or “String Interpolation Expressions.” A quasi-literal string is something that looks like a string literal, but is actually an expression. Quasi-literal strings are denoted with back quotes, and most strings that can be expressed as literals have the exact same meaning as quasi-literals, e.g.

`foobar` _//=> 'foobar'_ `fizz` + `buzz` _//=> 'fizzbuzz'_

Quasi-literals go much further. A quasi-literal can contain an expression to be evaluated. Old-school lispers call this “unquoting,” the more contemporary term is “interpolation.” An unquoted expression is inserted in a quasi-literal with ${expression}. The expression is evaluated, and the result is coerced to a string, then inserted in the quasi-string.

For example:

- `A popular number for nerds is **${** 40 + 2 **}** `

- _//=> 'A popular number for nerds is 42'_

A quasi-literal is computationally equivalent to an expression using +. So the above expression could also be written:

> 87https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators _(javascriptallonge.pdf (source-range-83ecb080-00242))_

### How to run the examples

- The Golden Crema: Appendices and Afterwords

267 **const** before = (decoration) => (method) => **function** (...args) { decoration.apply( **this** , args); **return** method.apply( **this** , args) }; And it would be “transpiled” into: **var** before = **function** (decoration) { **return function** (method) { **return function** () { **for** ( **let** _len = arguments.length, args = Array(_len), _key = 0; _key < _le\ n; _key++) { args[_key] = arguments[_key]; } decoration.apply( **this** , args); **return** method.apply( **this** , args); }; }; };

Both tools offer an online area where you can type ECMAScript code into a web browser and see the ECMAScript-5 equivalent, and you can run the code as well. To see the result of your expressions, you may have to use the console in your web browser.

So instead of just writing: (() => 2 + 2)() And having 4 displayed, you’d need to write: console.log( (() => 2 + 2)() ) And 4 would appear in your browser’s development console.

You can also install the transpilers on your development system and use them with Node[102] on the command line[103] . The care and feeding of node and npm are beyond the scope of this book, but both tools offer clear instructions for those who have already installed node.

> 102http://nodejs.org/

> 103https://en.wikipedia.org/wiki/REPL _(javascriptallonge.pdf (source-range-83ecb080-00336))_


## Related pages

- [[javascriptallonge-evaluate]] - shared statements: Evaluate shares source evidence from values and identity: xviii  Prelude: Values and Expressions over Coffee  An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wil ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Magic Names: 52  The first sip: Basic Functions **const** plus = **function** () { **return** arguments[0] + arguments[1]; } plus(2,3) _//=> 5_  When discussing objects, we’ll di ... [truncated] (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from values are expressions: xiv  Prelude: Values and Expressions over Coffee  ## **values are expressions**  All values are expressions. Say you hand the barista a café Cubano. Yup, you hand ov ... [truncated] (1 shared statement(s))
- [[javascriptallonge-rule]] - shared statements: Rule shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  7  ## **As Little As Possible About Functions, But No Less**  In JavaScript, functions are values, but they are also much more than s ... [truncated] (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from values and identity: xviii  Prelude: Values and Expressions over Coffee  An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wil ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
