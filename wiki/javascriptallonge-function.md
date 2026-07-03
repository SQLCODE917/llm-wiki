---
page_id: javascriptallonge-function
page_kind: concept
page_family: broad-topic
summary: Function: 101 statement(s) and 164 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-function@7847cc5e5516845e832b39aabdecabae
---

# Function

What [[javascriptallonge]] covers about function:


## Related pages

### Source structure

- [[javascriptallonge-section-and-also-summary-functions-a3702d43]] - source section: And also: / Summary / Functions shares source evidence from And also: / Summary / Functions: Functions are values that can be part of expressions, returned from other functions, and so forth.; And also: / Summary / Functions shares technical table: combinators The word 'combinator' has a precise technical meaning in mathematics: 'A combinator is a higher-order function that uses only function application and ea ... [truncated] (12 shared statement(s), 7 shared atom(s))

### Shared technical atoms

- [[javascriptallonge-javascript]] - shared statements and technical atoms: Javascript shares source evidence from A Pull of the Lever: Prefaces / About JavaScript Allongé: It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or ... [truncated]; Javascript shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less: () => 0 (4 shared statement(s), 22 shared atom(s))
- [[javascriptallonge-argument]] - shared statements and technical atoms: Argument shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dicti ... [truncated]; Argument shares technical record from And also: / Ah. I'd Like to Have an Argument, Please. 22: (room) => {} (4 shared statement(s), 21 shared atom(s))
- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: The expression 'x' (the right side of the function) is evaluated within the environment we just created.; Expression shares technical record from Or even: / back on the block: () => { 2 + 2 } () => { 1 + 1; 2 + 2 } (2 shared statement(s), 17 shared atom(s))
- [[javascriptallonge-bind]] - shared statements and technical atoms: Bind shares source evidence from And also: / Naming Functions: It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an ... [truncated]; Bind shares technical record from And also: / That Constant Coffee Craving: ((PI) => // ???? )(3.14159265) (1 shared statement(s), 14 shared atom(s))
- [[javascriptallonge-return]] - shared statements and technical atoms: Return shares source evidence from Or even: / back on the block: We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21; Return shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (6 shared statement(s), 11 shared atom(s))
- [[javascriptallonge-length]] - shared statements and technical atoms: Length shares source evidence from Composing and Decomposing Data / Self-Similarity: Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to c ... [truncated]; Length shares technical record from Composing and Decomposing Data / Self-Similarity: const length = ([first, ...rest]) => first === undefined ? 0 : // ??? (3 shared statement(s), 12 shared atom(s))
- [[javascriptallonge-write]] - shared statements and technical atoms: Write shares source evidence from And also: / That Constant Coffee Craving / const: Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this:; Write shares technical record from Or even: / back on the block: So how do we get a function that evaluates a block to return a value when applied? (2 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-functional-iterator]] - shared statements and technical atoms: Functional Iterators shares source evidence from Yes. Consider this variation: / Functional Iterators: What we've done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array); . The sumFoldable function do ... [truncated]; Functional Iterators shares technical record from Yes. Consider this variation: / Functional Iterators / unfolding and laziness: const NumberIterator = (number = 0) => () => ({ done: false, value: number++ }) fromOne = NumberIterator(1); fromOne().value; //=> 1 fromOne().value; //=> 2 fromOne( ... [truncated] (5 shared statement(s), 7 shared atom(s))

### Topics

- [[javascriptallonge-function-keyword]] - narrower topic: the function keyword shares source evidence from And also: / Naming Functions / the function keyword: In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, b ... [truncated]; the function keyword shares technical record from And also: / Naming Functions / the function keyword: (str) => str + str (4 shared statement(s), 14 shared atom(s))
- [[javascriptallonge-function-return-value]] - narrower topic: Function Return Value shares source evidence from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: Yes we can! Functions can return the value of evaluating another function.; Function Return Value shares technical record from The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions: (() => 1 + 1)() //=> 2 (() => "Hello, " + "JavaScript")() //=> "Hello, JavaScript" (() => Infinity * Infinity)() //=> Infinity (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-function-decorator]] - narrower topic: Function Decorator shares source evidence from And also: / Combinators and Function Decorators / function decorators: not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorator ... [truncated]; Function Decorator shares technical record from And also: / Combinators and Function Decorators / function decorators: const nothing = not(something); (1 shared statement(s), 1 shared atom(s))
## Statements by source section

### A Pull of the Lever: Prefaces / About JavaScript Allongé

- It also provides recipes for using functions to write software that is simpler, cleaner, and less complicated than alternative approaches that are object-centric or code-centric. JavaScript idioms like function combinators and decorators leverage JavaScript's power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-7239e085-00018))_

### A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

- Likewise, many programming languages permit functions to have a variable number of arguments, and to collect the arguments into a single variable as an array. In Ruby, we can write: _(javascriptallonge.pdf (source-range-7239e085-00028))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-7239e085-00168))_

- What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else. _(javascriptallonge.pdf (source-range-7239e085-00172))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-7239e085-00196))_

### Or even: / back on the block

- We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21 _(javascriptallonge.pdf (source-range-7239e085-00236))_

### And also: / functions that evaluate to functions

- That's a function! It's a function that when applied, evaluates to a function that when applied, evaluates to 0 . So we have a function, that returns a function, that returns zero . Likewise: _(javascriptallonge.pdf (source-range-7239e085-00261))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22

- This function has one argument, room , and an empty body. Here's a function with two arguments and an empty body: _(javascriptallonge.pdf (source-range-7239e085-00274))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value

- What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . Then our circumference function was applied to 2 . 24 _(javascriptallonge.pdf (source-range-7239e085-00295))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary that maps variables to values by name. The x in the expression that we call a 'variable' is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-7239e085-00303))_

- How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write: _(javascriptallonge.pdf (source-range-7239e085-00305))_

- The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-7239e085-00315))_

### And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

- Functions containing no free variables are called pure functions . _(javascriptallonge.pdf (source-range-7239e085-00345))_

- Functions containing one or more free variables are called closures . _(javascriptallonge.pdf (source-range-7239e085-00346))_

- Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we've already seen: _(javascriptallonge.pdf (source-range-7239e085-00347))_

### And also: / Closures and Scope / it's always the environment

- To understand how closures are evaluated, we need to revisit environments. As we've said before, all functions are associated with an environment. We also hand-waved something when describing our environment. Remember that we said the environment for ((x) => (y) => x)(1) is {x: 1, ...} and that the environment for ((y) => x)(2) is {y: 2, ...} ? Let's fill in the blanks! _(javascriptallonge.pdf (source-range-7239e085-00355))_

- The first function is the result of currying a the second function. Calling a curried function with only some of its arguments is sometimes called partial application b . Some programming languages automatically curry and partially evaluate functions without the need to manually nest them. _(javascriptallonge.pdf (source-range-7239e085-00366))_

### And also: / Closures and Scope / which came first, the chicken or the egg?

- This behaviour of pure functions and closures has many, many consequences that can be exploited to write software. We are going to explore them in some detail as well as look at some of the other mechanisms JavaScript provides for working with variables and mutable state. _(javascriptallonge.pdf (source-range-7239e085-00378))_

### And also: / That Constant Coffee Craving

- This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 . _(javascriptallonge.pdf (source-range-7239e085-00392))_

### And also: / That Constant Coffee Craving / const

- Another way to write our 'circumference' function would be to pass PI along with the diameter argument, something like this: _(javascriptallonge.pdf (source-range-7239e085-00415))_

- Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30 _(javascriptallonge.pdf (source-range-7239e085-00432))_

- Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-7239e085-00433))_

### And also: / Naming Functions

- It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-7239e085-00501))_

### And also: / Naming Functions / the function keyword

- In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-7239e085-00523))_

- Now, the function's actual name has no effect on the environment in which it is used. To whit: _(javascriptallonge.pdf (source-range-7239e085-00529))_

- So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const : _(javascriptallonge.pdf (source-range-7239e085-00531))_

### And also: / Naming Functions / function declarations

- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-7239e085-00540))_

- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently: _(javascriptallonge.pdf (source-range-7239e085-00543))_

### And also: / Naming Functions / function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-7239e085-00548))_

- Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. _(javascriptallonge.pdf (source-range-7239e085-00551))_

### And also: / Combinators and Function Decorators / higher-order functions

- As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function. _(javascriptallonge.pdf (source-range-7239e085-00557))_

### And also: / Combinators and Function Decorators / function decorators

- not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators. _(javascriptallonge.pdf (source-range-7239e085-00578))_

### And also: / Building Blocks / partial application

- The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-7239e085-00597))_

### And also: / Magic Names

- When a function is applied to arguments (or 'called'), JavaScript binds the values of arguments to the function's argument names in an environment created for the function's execution. What we haven't discussed so far is that JavaScript also binds values to some 'magic' names in addition to any you put in the argument list. 42 _(javascriptallonge.pdf (source-range-7239e085-00605))_

### And also: / Magic Names / magic names and fat arrows

- For example, when this expression's inner function is defined with function , arguments[0] refers to its only argument, "inner" : _(javascriptallonge.pdf (source-range-7239e085-00620))_

- Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code. _(javascriptallonge.pdf (source-range-7239e085-00631))_

- But sometimes, a function is a small-f function. It's a simple representation of an expression to be computed. In our example above, row is a Big-F function, but (column) => column * arguments[0] is a small-f function, it exists just to give mapWith something to apply. _(javascriptallonge.pdf (source-range-7239e085-00632))_

### And also: / Summary / Functions

- Functions are values that can be part of expressions, returned from other functions, and so forth. _(javascriptallonge.pdf (source-range-7239e085-00637))_

- Functions are reference values . _(javascriptallonge.pdf (source-range-7239e085-00638))_

- Functions are applied to arguments. _(javascriptallonge.pdf (source-range-7239e085-00639))_


## Technical atoms

### Technical frame 1: A Pull of the Lever: Prefaces / About JavaScript Allongé / why the 'six' edition?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00030))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00029))_

<a id="atom-technical-atom-4cdaf7d079e7fa51"></a>

```
def foo (first, *rest)
# ...
end
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00170))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00169))_

<a id="atom-technical-atom-4ba993180602fa06"></a>

```
() => 0
```

### Technical frame 3: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00172))_

> What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a br

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00171))_

<a id="atom-technical-atom-4a550bf37c4d3c09"></a>

```
(() => 0)
//=> [Function]
```

### Technical frame 4: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00174))_

> I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00172))_

<a id="atom-technical-atom-20ea58105aebcc81"></a>

> If you try the same thing in a browser, you may see something else.

### Technical frame 5: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00174))_

> I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00173))_

<a id="atom-technical-atom-3bfee0f96693b040"></a>

> 16 The simplest possible function is () => {} , we'll see that later.

### Technical frame 6: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00176))_

> You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00178))_

<a id="atom-technical-atom-103065528fb20d67"></a>

```
(() => 0) === (() => 0)
//=> false
```

### Technical frame 7: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00184))_

> Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00183))_

<a id="atom-technical-atom-a7a196f63e97d3c4"></a>

```
fn_expr(args)
```

### Technical frame 8: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00193))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00192))_

<a id="atom-technical-atom-7673f47cd782cb73"></a>

```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```

### Technical frame 9: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00196))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00197))_

<a id="atom-technical-atom-89adc0ecfdaf7a9b"></a>

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical frame 10: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00204))_

<a id="atom-technical-atom-ead6c5c59b062746"></a>

```
(() => (1 + 1, 2 + 2))()
//=> 4
```

### Technical frame 11: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00201))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

<a id="atom-technical-atom-a037009faf63061c"></a>

> This is useful when trying to do things that might involve side-effects , but we'll get to that later.

### Technical frame 12: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00236))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00235))_

<a id="atom-technical-atom-b34f988478f326e7"></a>

```
(() => {})()
//=> undefined
```

### Technical frame 13: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00240))_

<a id="atom-technical-atom-f310a0c20a90f3f0"></a>

```
() => { 2 + 2 }
() => { 1 + 1; 2 + 2 }
```

### Technical frame 14: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00242))_

<a id="atom-technical-atom-1d9243789bdf2a74"></a>

```
() => {
1 + 1;
2 + 2
}
```

### Technical frame 15: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00248))_

<a id="atom-technical-atom-a3eff62ec638110d"></a>

> So how do we get a function that evaluates a block to return a value when applied?

### Technical frame 16: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00249))_

<a id="atom-technical-atom-60713ed93e461b84"></a>

```
(() => { return 0 })()
//=> 0
(() => { return 1 })()
//=> 1
(() => { return 'Hello ' + 'World' })()
// 'Hello World'
```

### Technical frame 17: Or even: / back on the block

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00246))_

> 21 You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there's a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it's part of the language's definition, it's fair game to write code that e

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00251))_

<a id="atom-technical-atom-2a6a94a2285075d4"></a>

```
(() => {
1 + 1;
return 2 + 2
})()
//=> 4
```

### Technical frame 18: And also: / functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00268))_

> Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00262))_

<a id="atom-technical-atom-3ca4240b2cedb80a"></a>

```
() => () => true
```

### Technical frame 19: And also: / functions that evaluate to functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00268))_

> Well. We've been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can't blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, 'I'd Like to Have an Argument, Please,' we'll see how to make functions practical.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00264))_

<a id="atom-technical-atom-7c3019347764a54f"></a>

```
(() => () => true)()()
//=> true
```

### Technical frame 20: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00274))_

> This function has one argument, room , and an empty body. Here's a function with two arguments and an empty body:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00273))_

<a id="atom-technical-atom-6a7b1c7102f82932"></a>

```
(room) => {}
```

### Technical frame 21: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00276))_

> I'm sure you are perfectly comfortable with the idea that this function has two arguments, room , and board . What does one do with the arguments? Use them in the body, of course. What do you think this is?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00275))_

<a id="atom-technical-atom-e3d6fc001ce32d0d"></a>

```
(room, board) => {}
```

### Technical frame 22: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00278))_

> It's a function for calculating the circumference of a circle given the diameter. I read that aloud as 'When applied to a value representing the diameter, this function returns the diameter times 3.14159265.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00277))_

<a id="atom-technical-atom-8b0b88078e233caf"></a>

```
(diameter) => diameter * 3.14159265
```

### Technical frame 23: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00281))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00280))_

<a id="atom-technical-atom-8b01b9d30a77b780"></a>

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
```

### Technical frame 24: And also: / Ah. I'd Like to Have an Argument, Please. 22

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00281))_

> You won't be surprised to see how to write and apply a function to two arguments:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00283))_

<a id="atom-technical-atom-ec0274d1c7132fae"></a>

```
((room, board) => room + board)(800, 150)
//=> 950
```

### Technical frame 25: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00301))_

> But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. It's the same thing with (x) => (y) => x . It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00299))_

<a id="atom-technical-atom-3aa4f4b69198f2f9"></a>

```
(x) => (y) => x
```

### Technical frame 26: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00314))_

> The value '2' is bound to the name 'x' in the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00306))_

<a id="atom-technical-atom-4a548db5b5a8be44"></a>

```
((x) => x)(2)
//=> 2
```

### Technical frame 27: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00328))_

> 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00327))_

<a id="atom-technical-atom-352494efef5d9591"></a>

```
(value) =>
((ref1, ref2) => ref1 === ref2)(value, value)
```

### Technical frame 28: And also: / Closures and Scope / if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00352))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00351))_

<a id="atom-technical-atom-022fdc90abb9f966"></a>

> If pure functions can contain closures, can a closure contain a pure function?

### Technical frame 29: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00358))_

> (x) => x is called the I Combinator, or the Identity Function . (x) => (y) => x is called the K Combinator, or Kestrel . Some people get so excited by this that they write entire books about them, some are great a , some-how shall I put this-are interesting b if you use Ruby. a http://www.amzn.com/0192801422?tag=raganwald001-20

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00356))_

<a id="atom-technical-atom-634e3513bd1b5d02"></a>

> So whenever a function is applied to arguments, its environment always has a reference to its parent environment.

### Technical frame 30: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00365))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00360))_

<a id="atom-technical-atom-25dfc322e92bb80d"></a>

```
bh
```

### Technical frame 31: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00365))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00362))_

<a id="atom-technical-atom-af55a2cd0e53b310"></a>

```
(x) =>
(y) =>
(z) => x + y + z
```

### Technical frame 32: And also: / Closures and Scope / it's always the environment

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00365))_

> Only you call it with (1)(2)(3) instead of (1, 2, 3) . The other big difference is that you can call it with (1) and get a function back that you can later call with (2)(3) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00364))_

<a id="atom-technical-atom-2bf197b4e3f33351"></a>

```
(x, y, z) => x + y + z
```

### Technical frame 33: And also: / Closures and Scope / which came first, the chicken or the egg?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00383))_

> The effect is to insert a new, empty environment in between the global environment and your own functions: {x: 1, '..': {'..': global environment }} . As we'll see when we discuss mutable state, this helps to prevent programmers from accidentally changing the global state that is shared by all code in the program.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00381))_

<a id="atom-technical-atom-ac56068d50c46aef"></a>

> If you don't want your code to operate directly within the global environment, what can you do?

### Technical frame 34: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00392))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00389))_

<a id="atom-technical-atom-115c32a1871b07e7"></a>

```
((PI) =>
// ????
)(3.14159265)
```

### Technical frame 35: And also: / That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00392))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00391))_

<a id="atom-technical-atom-cb937ee0cbf9e345"></a>

```
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
```

### Technical frame 36: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00402))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00399))_

<a id="atom-technical-atom-0b04a5eefd97d2db"></a>

```
(diameter) =>
((PI) =>
diameter * PI)(3.14159265)
```

### Technical frame 37: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00402))_

> Which one is better? Well, the first one seems simplest, but a half-century of experience has taught us that names matter. A 'magic literal' like 3.14159265 is anathema to sustainable software development.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00401))_

<a id="atom-technical-atom-bcfcee9cd8ad8fd7"></a>

```
((diameter) => diameter * 3.14159265)(2)
//=> 6.2831853
((PI) =>
(diameter) => diameter * PI
)(3.14159265)(2)
//=> 6.2831853
((diameter) =>
((PI) =>
diameter * PI)(3.14159265))(2)
//=> 6.2831853
```

### Technical frame 38: And also: / That Constant Coffee Craving / inside-out

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00406))_

> Everything else is encapsulated in its body. That's how it should be, naming PI is its concern, not ours. The other formulation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00405))_

<a id="atom-technical-atom-ddeb9767d36d61f0"></a>

```
(diameter) =>
// ...
```

### Technical frame 39: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00419))_

> This differs from our example above in that there is only one environment, rather than two. We have one binding in the environment representing our regular argument, and another our 'constant.' That's more efficient, and it's almost what we wanted all along: A way to bind 3.14159265 to a readable name.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00416))_

<a id="atom-technical-atom-9748fc02adddeb23"></a>

```
(diameter, PI) => diameter * PI
```

### Technical frame 40: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00432))_

> Notice calc(d) ? This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () . A name that's bound to a function is a valid expression evaluating to a function. 30

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00431))_

<a id="atom-technical-atom-21fe35262939d1dc"></a>

```
(d) => {
const calc = (diameter) => {
const PI = 3.14159265;
return diameter * PI
};
return "The circumference is " + calc(d)
}
```

### Technical frame 41: And also: / That Constant Coffee Craving / const

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00433))_

> Amazing how such an important idea-naming functions-can be explained en passant in just a few words. That emphasizes one of the things JavaScript gets really, really right: Functions as 'first class entities. ' Functions are values that can be bound to names like any other value, passed as arguments, returned from other functions, and so forth.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00432))_

<a id="atom-technical-atom-7cfbdf50ede10fea"></a>

> This underscores what we've said: if we have an expression that evaluates to a function, we apply it with () .

### Technical frame 42: And also: / That Constant Coffee Craving / nested blocks

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00442))_

> The if statement is a statement, not an expression (an unfortunate design choice), and its clauses are statements or blocks. So we could also write something like:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00439))_

<a id="atom-technical-atom-179dd365e9382c9f"></a>

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

### Technical frame 43: And also: / That Constant Coffee Craving / const and lexical scope

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00452))_

> It's more than a bit convoluted, but it binds ((PI) => (diameter) => diameter * PI)(3.14159265) to diameter_fn and evaluates the expression that we've elided. We can use any expression in there, and that expression can invoke diameter_fn . For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00451))_

<a id="atom-technical-atom-59fe384c5a8d5e2d"></a>

```
((diameter_fn) =>
// ...
)(
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)
```

### Technical frame 44: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00475))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00472))_

<a id="atom-technical-atom-cffdad27f95f7db7"></a>

```
((PI) =>
((PI) =>
(diameter) => diameter * PI
)(3.14159265)
)(3)(2)
//=> 6.2831853
```

### Technical frame 45: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00475))_

> Now we bind 3 to PI in an otherwise empty IIFE inside of our IIFE that binds 3.14159265 to PI . Does that binding 'overwrite' the outer one? Will our function return 6 or 6.2831853 ? This is a book, you've already scanned ahead, so you know that the answer is no , the inner binding does not overwrite the outer binding:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00474))_

<a id="atom-technical-atom-bd9435d4a2d0ab5a"></a>

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)
```

### Technical frame 46: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00477))_

> We say that when we bind a variable using a parameter inside another binding, the inner binding shadows the outer binding. It has effect inside its own scope, but does not affect the binding in the enclosing scope.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00476))_

<a id="atom-technical-atom-5ee3571022440691"></a>

```
((PI) => {
((PI) => {})(3);
return (diameter) => diameter * PI;
})(3.14159265)(2)
//=> 6.2831853
```

### Technical frame 47: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00482))_

<a id="atom-technical-atom-2dde6743679c8a4b"></a>

```
if (true) {
// an immediately invoked block statement (IIBS)
}
Let’s try it:
((diameter) => {
const PI = 3;
if (true) {
const PI = 3.14159265;
return diameter * PI;
}
})(2)
//=> 6.2831853
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
```

### Technical frame 48: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00483))_

<a id="atom-technical-atom-bdd5dd7c22cb3cef"></a>

```
})(2)
//=> 6.2831853
```

### Technical frame 49: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00486))_

<a id="atom-technical-atom-d1848416f5b4149d"></a>

```
((diameter) => {
const PI = 3.14159265;
if (true) {
const PI = 3;
}
return diameter * PI;
})(2)
//=> would return 6 if const had function scope
```

### Technical frame 50: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00487))_

<a id="atom-technical-atom-cfed28fee17d44c4"></a>

> If const always bound its value to the name defined in the function's environment, placing a const statement inside of a block would merely rebind the existing name, overwriting its old contents.

### Technical frame 51: And also: / That Constant Coffee Craving / are consts also from a shadowy planet?

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00489))_

> Again, confusing. Typically, we want to bind our names as close to where we need them as possible. This design rule is called the Principle of Least Privilege 32 , and it has both quality and security implications. Being able to bind a name inside of a block means that if the name is only needed in the block, we are not 'leaking' its binding to other parts of the code that do not need to interact with it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00488))_

<a id="atom-technical-atom-0c5d98acca1d8c87"></a>

```
((diameter) => {
if (true) {
const PI = 3.14159265;
}
return diameter * PI;
})(2)
//=> would return 6.2831853 if const had function scope
```

### Technical frame 52: And also: / Naming Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00501))_

> It doesn't name the function 'repeat' for the same reason that const answer = 42 doesn't name the number 42 . This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00500))_

<a id="atom-technical-atom-c6844fc1ab0f403a"></a>

```
const repeat = (str) => str + str
```

### Technical frame 53: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00510))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00505))_

<a id="atom-technical-atom-5678cd19e7fe129e"></a>

```
(str) => str + str
```

### Technical frame 54: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00510))_

> Something else we're about to discuss is optional.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00507))_

<a id="atom-technical-atom-4892b44040deaa12"></a>

```
function (str) { return str + str }
```

### Technical frame 55: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00523))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00515))_

<a id="atom-technical-atom-263a35e1362152b8"></a>

```
(n) => (1.618**n - -1.618**-n) / 2.236
```

### Technical frame 56: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00523))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00517))_

<a id="atom-technical-atom-4988f07d229ed38d"></a>

```
function (n) {
return (1.618**n - -1.618**-n) / 2.236;
}
```

### Technical frame 57: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00523))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00520))_

<a id="atom-technical-atom-3b77ebe4e9b354d7"></a>

```
const repeat = function repeat (str) {
return str + str;
};
const fib = function fib (n) {
return (1.618**n - -1.618**-n) / 2.236;
};
```

### Technical frame 58: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00523))_

> In this expression, double is the name in the environment, but repeat is the function's actual name. This is a named function expression . That may seem confusing, but think of the binding names as properties of the environment, not of the function. While the name of the function is a property of the function, not of the environment.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00522))_

<a id="atom-technical-atom-81cb3037dd7ae143"></a>

```
const double = function repeat (str) {
return str + str;
}
```

### Technical frame 59: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00529))_

> Now, the function's actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00528))_

<a id="atom-technical-atom-8b9017e39b6579b1"></a>

```
someBackboneView.on('click', function clickHandler () {
//...
});
```

### Technical frame 60: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00531))_

> So 'actualName' isn't bound in the environment where we use the named function expression. Is it bound anywhere else? Yes it is. Here's a function that determines whether a positive integer is even or not. We'll use it in an IIFE so that we don't have to bind it to a name with const :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00530))_

<a id="atom-technical-atom-1b4e65ac7feab271"></a>

```
const bindingName = function actualName () {
//...
};
bindingName
//=> [Function: actualName]
actualName
//=> ReferenceError: actualName is not defined
```

### Technical frame 61: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00533))_

> Clearly, the name even is bound to the function within the function's body . Is it bound to the function outside of the function's body?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00532))_

<a id="atom-technical-atom-8a664fe5bf8ee9c2"></a>

```
(function even (n) {
if (n === 0) {
return true
}
else return !even(n - 1)
})(5)
//=> false
(function even (n) {
if (n === 0) {
return true
}
else return !even(n - 1)
})(2)
//=> true
```

### Technical frame 62: And also: / Naming Functions / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00535))_

> even is bound within the function itself, but not outside it. This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don't need to name it anywhere else, you needn't.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00534))_

<a id="atom-technical-atom-1e163547ee6c3eac"></a>

```
even
//=> Can't find variable: even
```

### Technical frame 63: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00540))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00538))_

<a id="atom-technical-atom-642381d95ff4831d"></a>

```
function someName () {
// ...
}
This behaves a little like:
const someName = function someName ()
// ...
}
```

### Technical frame 64: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00540))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00539))_

<a id="atom-technical-atom-93530060e3dbc4f9"></a>

```
{
```

### Technical frame 65: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00543))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00542))_

<a id="atom-technical-atom-1a6edd33946284bd"></a>

```
(function () {
return fizzbuzz();
const fizzbuzz = function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> undefined is not a function (evaluating 'fizzbuzz()')
```

### Technical frame 66: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00546))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00544))_

<a id="atom-technical-atom-66980774291bd9f4"></a>

```
(function () {
return fizzbuzz();
function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> 'FizzBuzz'
Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:
(function () {
const fizzbuzz = function fizzbuzz () {
```

### Technical frame 67: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00546))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00545))_

<a id="atom-technical-atom-fe1368760c002c91"></a>

```
const fizzbuzz = function fizzbuzz ()
return "Fizz" + "Buzz";
}
return fizzbuzz();
})()
```

### Technical frame 68: And also: / Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00551))_

> Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00550))_

<a id="atom-technical-atom-8efe555506c14cf1"></a>

```
(function (camelCase) {
return fizzbuzz();
if (camelCase) {
function fizzbuzz () {
return "Fizz" + "Buzz";
}
}
else {
function fizzbuzz () {
return "Fizz" + "Buzz";
}
}
})(true)
//=> 'FizzBuzz'? Or ERROR: Can't find variable: fizzbuzz?
```

### Technical frame 69: And also: / Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00552))_

> Another caveat is that a function declaration cannot exist inside of any expression, otherwise it's a function expression. So this is a function declaration:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00551))_

<a id="atom-technical-atom-8524e5547711bd2a"></a>

> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.

### Technical frame 70: And also: / Naming Functions / function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00554))_

> The parentheses make this an expression, not a function declaration.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00553))_

<a id="atom-technical-atom-29b2a5bf49007ce5"></a>

```
function trueDat () { return true }
But this is not:
(function trueDat () { return true })
```

### Technical frame 71: And also: / Combinators and Function Decorators / higher-order functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00557))_

> As we've seen, JavaScript functions take values as arguments and return values. JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a 'higher-order' function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00559))_

<a id="atom-technical-atom-7193eeef1bd53156"></a>

```
const repeat = (num, fn) =>
(num > 0)
? (repeat(num - 1, fn), fn(num))
: undefined
repeat(3, function (n) {
console.log(`Hello ${n}`)
})
//=>
'Hello 1'
'Hello 2'
'Hello 3'
undefined
```

### Technical frame 72: And also: / Combinators and Function Decorators / function decorators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00578))_

> not is a function decorator because it modifies a function while remaining strongly related to the original function's semantics. You'll see other function decorators in the recipes, like once and maybe. Function decorators aren't strict about being pure functions, so there's more latitude for making decorators than combinators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00577))_

<a id="atom-technical-atom-16403f5e9983b595"></a>

```
const nothing = not(something);
```

### Technical frame 73: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00593))_

<a id="atom-technical-atom-d58c104eac1daf94"></a>

```
_.map([1, 2, 3], (n) => n * n)
//=> [1, 4, 9]
```

### Technical frame 74: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00597))_

> The resulting functionsquareAll -is still the map function, it's just that we've applied one of its two arguments already. squareAll is nice, but why write one function every time we want to partially apply a function to a map? We can abstract this one level higher. mapWith takes any function as an argument and returns a partially applied map function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00596))_

<a id="atom-technical-atom-7e2e343bb8d0ba90"></a>

```
const squareAll = (array) => map(array,
(n) => n * n);
```

### Technical frame 75: And also: / Building Blocks / partial application

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00599))_

> We'll discuss mapWith again. The important thing to see is that partial application is orthogonal to composition, and that they both work together nicely:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00598))_

<a id="atom-technical-atom-d427b13c540a373d"></a>

```
const mapWith = (fn) =>
(array) => map(array, fn);
const squareAll = mapWith((n) => n * n);
squareAll([1, 2, 3])
//=> [1, 4, 9]
```

### Technical frame 76: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00617))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00609))_

<a id="atom-technical-atom-013351b465690d3d"></a>

```
const plus = function (a, b) {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Technical frame 77: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00617))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00611))_

<a id="atom-technical-atom-73008766944bbb48"></a>

```
const args = function (a, b) {
return arguments;
}
args(2,3)
//=> { '0': 2, '1': 3 }
```

### Technical frame 78: And also: / Magic Names / the function keyword

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00617))_

> The most common use of the arguments binding is to build functions that can take a variable number of arguments. We'll see it used in many of the recipes, starting off with partial application and ellipses.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00614))_

<a id="atom-technical-atom-8fe93a73e437ee03"></a>

```
const plus = function () {
return arguments[0] + arguments[1];
}
plus(2,3)
//=> 5
```

### Technical frame 79: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00625))_

> To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00621))_

<a id="atom-technical-atom-243e812c5a716d94"></a>

```
(function () {
return (function () { return arguments[0]; })('inner');
})('outer')
//=> "inner"
```

### Technical frame 80: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00625))_

> To give a contrived example, this function takes a number and returns an array representing a row in a hypothetical multiplication table. It uses mapWith , which we discussed in Building Blocks. 44 We'll use arguments just to show the difference between using a fat arrow and the function keyword:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00623))_

<a id="atom-technical-atom-733056f2f6551e51"></a>

```
(function () {
return (() => arguments[0])('inner');
})('outer')
//=> "outer"
```

### Technical frame 81: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00627))_

> This works just fine, because arguments[0] refers to the 3 we passed to the function row . Our 'fat arrow' function (column) => column * arguments[0] doesn't bind arguments when it's invoked. But if we rewrite row to use the function keyword, it stops working:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00626))_

<a id="atom-technical-atom-f66c3ed611303c0d"></a>

```
const row = function () {
return mapWith(
(column) => column * arguments[0],
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [3,6,9,12,15,18,21,24,27,30,33,36]
```

### Technical frame 82: And also: / Magic Names / magic names and fat arrows

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00631))_

> Although this example is clearly unrealistic, there is a general design principle that deserves attention. Sometimes, a function is meant to be used as a Big-F function. It has a name, it is called by different pieces of code, it's a first-class entity in the code.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00629))_

<a id="atom-technical-atom-aeb7942534341524"></a>

```
const row = function () {
return mapWith(
function (column) { return column * arguments[0] },
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)
}
row(3)
//=> [1,4,9,16,25,36,49,64,81,100,121,144]
```

### Technical frame 83: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00674))_

> If you pass in a function taking only one argument, it simply ignores the additional arguments. But some functions have optional second or even third arguments. For example:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00670))_

<a id="atom-technical-atom-234622016e944e78"></a>

```
['1', '2', '3'].map(parseFloat)
//=> [1, 2, 3]
```

### Technical frame 84: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00674))_

<a id="atom-technical-atom-e63879039d2b786d"></a>

> If you pass in a function taking only one argument, it simply ignores the additional arguments.

### Technical frame 85: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00675))_

<a id="atom-technical-atom-39444c72b711b290"></a>

```
['1', '2', '3'].map(parseInt)
//=> [1, NaN, NaN]
```

### Technical frame 86: Recipes with Basic Functions / Unary

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00676))_

> This doesn't work because parseInt is defined as parseInt(string[, radix]) . It takes an optional radix argument. And when you call parseInt with map , the index is interpreted as a radix. Not good! What we want is to convert parseInt into a function taking only one argument.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00677))_

<a id="atom-technical-atom-c6eb6eaeb3b33791"></a>

> Wecould write ['1', '2', '3'].map((s) => parseInt(s)) , or we could come up with a decorator to do the job for us:

### Technical frame 87: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00698))_

> Alternately, the function may be intended to work with any value, but the code calling the function wishes to emulate the behaviour of doing nothing by design when given nothing:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00697))_

<a id="atom-technical-atom-0050ec8e3fdf9f53"></a>

```
const isSomething = (value) =>
value !== null && value !== void 0;
const checksForSomething = (value) => {
if (isSomething(value)) {
// function's true logic
}
}
```

### Technical frame 88: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00700))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00699))_

<a id="atom-technical-atom-6e43ace583e3f4ed"></a>

```
var something =
isSomething(value)
? doesntCheckForSomething(value)
: value;
```

### Technical frame 89: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00701))_

<a id="atom-technical-atom-8066787a4a683125"></a>

```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return
}
else {
for (let arg of args) {
if (arg == null) return;
}
```

### Technical frame 90: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00703))_

<a id="atom-technical-atom-76ebbf2990753f8d"></a>

```
return fn.apply(this, args)
}
}
```

### Technical frame 91: Recipes with Basic Functions / Maybe

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00708))_

> If some code ever tries to call model.setSomething with nothing, the operation will be skipped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00705))_

<a id="atom-technical-atom-e759bf9ba4f40ec3"></a>

```
maybe((a, b, c) => a + b + c)(1, 2, 3)
//=> 6
maybe((a, b, c) => a + b + c)(1, null, 3)
//=> undefined
```

### Technical frame 92: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00711))_

<a id="atom-technical-atom-2388b6615c013cfa"></a>

```
const once = (fn) => {
let done = false;
return function () {
return done ? void 0 : ((done = true), fn.apply(this, arguments))
}
}
```

### Technical frame 93: Recipes with Basic Functions / Once

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00710))_

> once is an extremely helpful combinator. It ensures that a function can only be called, well, once . Here's the recipe:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00713))_

<a id="atom-technical-atom-4a54ace1417283a8"></a>

```
const askedOnBlindDate = once(
() => "sure, why not?"
);
askedOnBlindDate()
//=> 'sure, why not?'
askedOnBlindDate()
//=> undefined
askedOnBlindDate()
//=> undefined
```

### Technical frame 94: Recipes with Basic Functions / Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00719))_

> This can be useful when writing certain kinds of destructuring algorithms. For example, we might want to have a function that builds some kind of team record. It accepts a coach, a captain, and an arbitrary number of players. Easy in ECMAScript 2015:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00718))_

<a id="atom-technical-atom-2cf7e32d0c999fe7"></a>

```
const abccc = (a, b, ...c) => {
console.log(a);
console.log(b);
console.log(c);
};
abccc(1, 2, 3, 4, 5)
1
2
[3,4,5]
```

### Technical frame 95: Recipes with Basic Functions / Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00721))_

> 52 English is about as inconsistent as JavaScript: Functions with a fixed number of arguments can be unary, binary, ternary, and so forth. But can they be 'variary?' No! They have to be 'variadic.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00720))_

<a id="atom-technical-atom-f601b03ee56b156a"></a>

```
function team(coach, captain, ...players) {
console.log(`${captain} (captain)`);
for (let player of players) {
console.log(player);
}
console.log(`squad coached by ${coach}`);
}
team('Luis Enrique', 'Xavi Hernández', 'Marc-André ter Stegen',
'Martín Montoya', 'Gerard Piqué')
//=>
Xavi Hernández (captain)
Marc-André ter Stegen
Martín Montoya
Gerard Piqué
squad coached by Luis Enrique
But we can’t go the other way around:
```

### Technical frame 96: Recipes with Basic Functions / Left-Variadic Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00723))_

> ECMAScript 2015 only permits gathering parameters from the end of the parameter list. Not the beginning. What to do?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00722))_

<a id="atom-technical-atom-99a0f4a090bc346d"></a>

```
function team2(...players, captain, coach) {
console.log(`${captain} (captain)`);
for (let player of players) {
console.log(player);
}
console.log(`squad coached by ${coach}`);
}
//=> Unexpected token
```

### Technical frame 97: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00749))_

> With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00742))_

<a id="atom-technical-atom-eb3ab57c56a2f7dd"></a>

```
const [first, ...butFirst] = ['why', 'hello', 'there', 'little', 'droid'];
first
//=> 'why'
butFirst
//=> ["hello","there","little","droid"]
```

### Technical frame 98: Recipes with Basic Functions / Left-Variadic Functions / left-variadic destructuring

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00749))_

> With leftGather , we have to supply the length of the array we wish to use as the result, and it gathers excess arguments into it from the left, just like leftVariadic gathers excess parameters for a function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00748))_

<a id="atom-technical-atom-fcb9efdca6bc6168"></a>

```
const leftGather = (outputArrayLength) => {
return function (inputArray) {
return [inputArray.slice(0, inputArray.length - outputArrayLength + 1)].conc\
at(
inputArray.slice(inputArray.length - outputArrayLength + 1)
)
}
};
const [butLast, last] = leftGather(2)(['why', 'hello', 'there', 'little', 'droid\
']);
butLast
//=> ['why', 'hello', 'there', 'little']
last
//=> 'droid'
```

### Technical frame 99: Picking the Bean: Choice and Truthiness / function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00804))_

> If we need to have functions with control-flow semantics, we can pass anonymous functions. We obviously don't need anything like this for or and and , but to demonstrate the technique:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00802))_

<a id="atom-technical-atom-f6692ca904d56bf1"></a>

```
const or = (a, b) => a || b
const and = (a, b) => a && b
const even = (n) =>
or(n === 0, and(n !== 1, even(n - 2)))
even(42)
//=> Maximum call stack size exceeded.
```

### Technical frame 100: Picking the Bean: Choice and Truthiness / function parameters are eager

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00806))_

> Here we've passed functions that contain the expressions we want to evaluate, and now we can write our own functions that can delay evaluation.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00805))_

<a id="atom-technical-atom-85184dcfdb4ac959"></a>

```
const or = (a, b) => a() || b()
const and = (a, b) => a() && b()
const even = (n) =>
or(() => n === 0, () => and(() => n !== 1, () => even(n - 2)))
even(7)
//=> false
```

### Technical frame 101: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00901))_

> We need something for when the array isn't empty. If an array is not empty, and we break it into two pieces, first and rest , the length of our array is going to be length(first) + length(rest) . Well, the length of first is 1 , there's just one element at the front. But we don't know the length of rest . If only there was a function we could call… Like length !

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00900))_

<a id="atom-technical-atom-e298cdaa6ee5e32b"></a>

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: // ???
```

### Technical frame 102: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00902))_

<a id="atom-technical-atom-dce776a77328aa08"></a>

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
Let’s try it!
length([])
//=> 0
length(["foo"])
//=> 1
length(["foo", "bar", "baz"])
```

### Technical frame 103: Composing and Decomposing Data / Self-Similarity

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00904))_

> Our length function is recursive , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00903))_

<a id="atom-technical-atom-65ebfed4d2b01ae4"></a>

```
//=> 3
```

### Technical frame 104: Composing and Decomposing Data / Self-Similarity / linear recursion

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00923))_

> Once again, the solution directly displays the important elements: Dividing a problem into subproblems, detecting terminal cases, solving the terminal cases, and composing a solution from the solved portions.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00922))_

<a id="atom-technical-atom-e2cf71b057b0a93b"></a>

```
const flatten = ([first, ...rest]) => {
if (first === undefined) {
return [];
}
else if (!Array.isArray(first)) {
return [first, ...flatten(rest)];
}
else {
return [...flatten(first), ...flatten(rest)];
}
}
flatten(["foo", [3, 4, []]])
//=> ["foo",3,4]
```

### Technical frame 105: Composing and Decomposing Data / Self-Similarity / mapping

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00933))_

> Wecanwrite it out using a ternary operator. Even in this small function, we can identify the terminal condition, the piece being broken off, and recomposing the solution.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00934))_

<a id="atom-technical-atom-829e3201ad2e303b"></a>

```
const mapWith = (fn, [first, ...rest]) =>
first === undefined
? []
: [fn(first), ...mapWith(fn, rest)];
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
mapWith((x) => !!x, [null, true, 25, false, "foo"])
//=> [false,true,true,false,true]
```

### Technical frame 106: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00945))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00937))_

<a id="atom-technical-atom-9feefbdde8f3ed2c"></a>

```
const sumSquares = ([first, ...rest]) => first === undefined
? 0
: first * first + sumSquares(rest);
sumSquares([1, 2, 3, 4, 5])
//=> 55
```

### Technical frame 107: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00945))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00944))_

<a id="atom-technical-atom-50945a3512f71e5d"></a>

```
foldWith((number, rest) => number * number + rest, 0, [1, 2, 3, 4, 5])
//=> 55
```

### Technical frame 108: Composing and Decomposing Data / Self-Similarity / folding

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00945))_

> Our foldWith function is a generalization of our mapWith function. We can represent a map as a fold, we just need to supply the array rebuilding code:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00946))_

<a id="atom-technical-atom-5f6feca38471ebf3"></a>

```
const squareAll = (array) => foldWith((first, rest) => [first * first, ...rest],\
[], array);
squareAll([1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 109: Composing and Decomposing Data / Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00957))_

> Let's step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00956))_

<a id="atom-technical-atom-75e4f35af8eeaf3f"></a>

```
const mapWith = (fn, [first, ...rest]) =>
first === undefined
? []
: [fn(first), ...mapWith(fn, rest)];
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 110: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00970))_

> There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00969))_

<a id="atom-technical-atom-a6d838fc3442cb2f"></a>

```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return;
}
else {
for (let arg of args) {
if (arg == null) return;
}
return fn.apply(this, args);
}
}
```

### Technical frame 111: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00974))_

> The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00973))_

<a id="atom-technical-atom-2634a0aa2029afd4"></a>

```
const length = ([first, ...rest]) =>
first === undefined
? 0
: 1 + length(rest);
```

### Technical frame 112: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00980))_

> This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00979))_

<a id="atom-technical-atom-d0492cb61af780f2"></a>

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? 0 + numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
lengthDelaysWork(["foo", "bar", "baz"], 0)
//=> 3
```

### Technical frame 113: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00981))_

<a id="atom-technical-atom-04ddfbb646c44eec"></a>

```
const lengthDelaysWork = ([first, ...rest], numberToBeAdded) =>
first === undefined
? numberToBeAdded
: lengthDelaysWork(rest, 1 + numberToBeAdded)
const length = (n) =>
lengthDelaysWork(n, 0);
```

### Technical frame 114: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00983))_

> This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00982))_

<a id="atom-technical-atom-fb0a210bf03406d6"></a>

```
Or we could use partial application:
const callLast = (fn, ...args) =>
(...remainingArgs) =>
fn(...remainingArgs, ...args);
const length = callLast(lengthDelaysWork, 0);
length(["foo", "bar", "baz"])
//=> 3
```

### Technical frame 115: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00994))_

> Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00992))_

<a id="atom-technical-atom-2b5a4752af84217f"></a>

```
const factorial = (n) =>
n == 1
? n
: n * factorial(n - 1);
factorial(1)
//=> 1
factorial(5)
//=> 120
```

### Technical frame 116: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01009))_

> Now we don't need to use two functions. A default argument is concise and readable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01008))_

<a id="atom-technical-atom-e841272be520e519"></a>

```
const length = ([first, ...rest], numberToBeAdded = 0) =>
first === undefined
? numberToBeAdded
: length(rest, 1 + numberToBeAdded)
length(["foo", "bar", "baz"])
//=> 3
const mapWith = (fn, [first, ...rest], prepend = []) =>
first === undefined
? prepend
: mapWith(fn, rest, [...prepend, fn(first)]);
mapWith((x) => x * x, [1, 2, 3, 4, 5])
//=> [1,4,9,16,25]
```

### Technical frame 117: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01193))_

> Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01192))_

<a id="atom-technical-atom-63d61c60ed87d9a8"></a>

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

### Technical frame 118: Composing and Decomposing Data / Reassignment / mixing let and const / var

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01195))_

<a id="atom-technical-atom-1a419a25617e5303"></a>

```
const factorial = (n) => {
return innerFactorial(n, 1);
function innerFactorial (x, y) {
if (x == 1) {
return y;
}
else {
return innerFactorial(x-1, x * y);
}
}
}
factorial(4)
//=> 24
```

### Technical frame 119: Yes. Consider this variation:

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01213))_

> What went wrong? Why didn't it give us 'Hello, Raganwald, my name is Friedrich'? The answer is that pesky var i . Remember that i is bound in the surrounding environment, so it's as if we wrote:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01212))_

<a id="atom-technical-atom-1a0a0e203beae22d"></a>

```
introductions[1]('Raganwald')
//=> 'Hello, Raganwald, my name is undefined'
```

### Technical frame 120: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01303))_

> A function that starts with a seed and expands it into a data structure is called an unfold . It's the opposite of a fold. It's possible to write a generic unfold mechanism, but let's pass on to what we can do with unfolded iterators.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01300))_

<a id="atom-technical-atom-0ec5247e8a0095b9"></a>

```
const NumberIterator = (number = 0) =>
() => ({ done: false, value: number++ })
fromOne = NumberIterator(1);
fromOne().value;
//=> 1
fromOne().value;
//=> 2
fromOne().value;
//=> 3
fromOne().value;
//=> 4
fromOne().value;
//=> 5
```

### Technical frame 121: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01309))_

> How about the squares of the first five odd numbers? We'll need an iterator that produces odd numbers. We can write that directly:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01308))_

<a id="atom-technical-atom-b6c7b5f8c2b10650"></a>

```
const take = (iterator, numberToTake) => {
let count = 0;
return () => {
if (++count <= numberToTake) {
return iterator();
} else {
return {done: true};
}
};
};
const toArray = (iterator) => {
let eachIteration,
array = [];
while ((eachIteration = iterator(), !eachIteration.done)) {
array.push(eachIteration.value);
}
return array;
}
toArray(take(FibonacciIterator(), 5))
//=> [1, 1, 2, 3, 5]
toArray(take(squares, 5))
//=> [1, 4, 9, 16, 25]
```

### Technical frame 122: Yes. Consider this variation: / Functional Iterators / unfolding and laziness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01314))_

> Mapping and filtering iterators allows us to compose the parts we already have, rather than writing a tricky bit of code with ifs and whiles and boundary conditions.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01313))_

<a id="atom-technical-atom-4efea8fa4b4f428a"></a>

```
const filterIteratorWith = (fn, iterator) =>
() => {
do {
const {done, value} = iterator();
} while (!done && !fn(value));
return {done, value};
}
const oddsOf = callLeft(filterIteratorWith, (n) => n % 2 === 1);
toArray(take(squareOf(oddsOf(NumberIterator(1))), 5))
//=> [1, 9, 25, 49, 81]
```

### Technical frame 123: Yes. Consider this variation: / Making Data Out Of Functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01330))_

> A very long time ago, mathematicians like Alonzo Church, Moses Schönfinkel, Alan Turning, and Haskell Curry and asked themselves if we really needed all these features to perform computations. They searched for a radically simpler set of tools that could accomplish all of the same things.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01329))_

<a id="atom-technical-atom-8099f5b267d8f12e"></a>

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest.first
//=> 2
OneTwoThree.rest.rest.first
//=> 3
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

### Technical frame 124: Yes. Consider this variation: / Making Data Out Of Functions / the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01352))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01346))_

<a id="atom-technical-atom-150ac9277cfd9a5b"></a>

```
Therefore, K(I)(x)(y) => y:
```

### Technical frame 125: Yes. Consider this variation: / Making Data Out Of Functions / the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01352))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01347))_

<a id="atom-technical-atom-61793a1442767bc8"></a>

```
K(I)(6)(7)
//=> 7
K(I)(12)(24)
//=> 24
```

### Technical frame 126: Yes. Consider this variation: / Making Data Out Of Functions / the kestrel and the idiot

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01352))_

> This is very interesting. Given two values, we can say that K always returns the first value, and given two values, K(I) always returns the second value.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01351))_

<a id="atom-technical-atom-18db0560e38997a6"></a>

```
const first = K,
second = K(I);
first("primus")("secundus")
//=> "primus"
second("primus")("secundus")
//=> "secundus"
```

### Technical frame 127: Yes. Consider this variation: / Making Data Out Of Functions / backwardness

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01358))_

> In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01355))_

<a id="atom-technical-atom-a507715e23aece58"></a>

```
const first = ([first, second]) => first,
second = ([first, second]) => second;
const latin = ["primus", "secundus"];
first(latin)
//=> "primus"
second(latin)
//=> "secundus"
```

### Technical frame 128: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01367))_

> For consistency with the way combinators are written as functions taking just one parameter, we'll curry 78 the function:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01366))_

<a id="atom-technical-atom-33d508801ab09389"></a>

```
(first, second) => (selector) => selector(first)(second)
```

### Technical frame 129: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01368))_

<a id="atom-technical-atom-d239a09115d21f68"></a>

```
(first) => (second) => (selector) => selector(first)(second)
```

### Technical frame 130: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01370))_

<a id="atom-technical-atom-f5a74a636a28bf0f"></a>

```
const first = K,
second = K(I),
pair = (first) => (second) => (selector) => selector(first)(second);
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Technical frame 131: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01371))_

<a id="atom-technical-atom-efdd17c1e988c898"></a>

> If we change the names to x , y , and z , we get: (x) => (y) => (z) => z(x)(y) .

### Technical frame 132: Yes. Consider this variation: / Making Data Out Of Functions / the vireo

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01374))_

> As an aside, the Vireo is a little like JavaScript's .apply function. It says, 'take these two values and apply them to this function.' There are other, similar combinators that apply values to functions. One notable example is the 'thrush' or T combinator: It takes one value and applies it to a function. It is known to most programmers as .tap .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01373))_

<a id="atom-technical-atom-848abd9361a0c2c5"></a>

```
const first = K,
second = K(I),
pair = V;
const latin = pair("primus")("secundus");
latin(first)
//=> "primus"
latin(second)
//=> "secundus"
```

### Technical frame 133: Yes. Consider this variation: / Making Data Out Of Functions / lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01385))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01380))_

<a id="atom-technical-atom-0911e44845c5a8dc"></a>

```
const length = (aPair) =>
aPair === EMPTY
? 0
: 1 + length(rest(aPair));
length(l123)
//=> 3
const reverse = (aPair, delayed = EMPTY) =>
aPair === EMPTY
? delayed
: reverse(rest(aPair), pair(first(aPair), delayed));
const mapWith = (fn, aPair, delayed = EMPTY) =>
aPair === EMPTY
? reverse(delayed)
: mapWith(fn, rest(aPair), pair(fn(first(aPair)), delayed));
const doubled = mapWith((x) => x * 2, l123);
first(doubled)
//=> 2
first(rest(doubled))
//=> 4
first(rest(rest(doubled)))
//=> 6
Can we do the same with the linked lists we build out of functions? Yes:
const first = K,
rest
= K(I),
pair = V,
EMPTY = (() => {});
const l123 = pair(1)(pair(2)(pair(3)(EMPTY)));
```

### Technical frame 134: Yes. Consider this variation: / Making Data Out Of Functions / lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01385))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01381))_

<a id="atom-technical-atom-0231efcf9de2fb7c"></a>

```
rest
= K(I),
pair = V,
EMPTY = (() => {});
const l123 = pair(1)(pair(
l123(first)
//=> 1
l123(rest)(first)
```

### Technical frame 135: Yes. Consider this variation: / Making Data Out Of Functions / lists with functions as data

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01385))_

> Presto, we can use pure functions to represent a linked list . And with care, we can do amazing things like use functions to represent numbers, build more complex data structures like trees, and in fact, anything that can be computed can be computed using just functions and nothing else.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01382))_

<a id="atom-technical-atom-ad481489b3763dce"></a>

```
//=> 2
return l123(rest)(rest)(first)
//=> 3
We write them in a backwards way, but they seem to work. How about
```

### Technical frame 136: Yes. Consider this variation: / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01397))_

> We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01395))_

<a id="atom-technical-atom-f83abdf8e28a311c"></a>

```
const pairFirst = K,
pairRest
= K(I),
pair = V;
const first = (list) => list(
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairFirst)
);
const rest = (list) => list(
```

### Technical frame 137: Yes. Consider this variation: / Making Data Out Of Functions / say 'please'

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01397))_

> We can write reverse and mapWith as well. We aren't being super-strict about emulating combinatory logic, we'll use default parameters:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01396))_

<a id="atom-technical-atom-6a8000d81ef5c081"></a>

```
() => "ERROR: Can't take first of an empty list",
(aPair) => aPair(pairRest)
);
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
We’ll also write a handy list printer:
const print = (list) => list(
() => "",
(aPair) => `${aPair(pairFirst)} ${print(aPair(pairRest))}`
);
How would all this work? Let’s start with the obvious. What is an empty list?
const EMPTYLIST = (whenEmpty, unlessEmpty) => whenEmpty()
And what is a node of a list?
const node = (x) => (y) =>
(whenEmpty, unlessEmpty) => unlessEmpty(pair(x)(y));
Let’s try it:
const l123 = node(1)(node(2)(node(3)(EMPTYLIST)));
print(l123)
//=> 1 2 3
```

### Technical frame 138: Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01416))_

> We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01415))_

<a id="atom-technical-atom-7584d0bd3f95e295"></a>

```
const length = (list) => list(
() => 0,
(aPair) => 1 + length(aPair(pairRest)))
);
```

### Technical frame 139: Yes. Consider this variation: / Making Data Out Of Functions / a return to backward thinking

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01419))_

> The line node === EMPTY presumes a lot of things. It presumes there is one canonical empty list value. It presumes you can compare these things with the === operator. We can fix this with an isEmpty function, but now we're pushing even more knowledge about the structure of lists into the code that uses them.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01418))_

<a id="atom-technical-atom-f6632ca1ca20da83"></a>

```
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
```

### Technical frame 140: Recipes with Data / Flip / self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01467))_

<a id="atom-technical-atom-c08628393adc0e69"></a>

```
const flip = (fn) =>
function (first, second) {
if (arguments.length === 2) {
return fn(second, first);
}
else {
return function (second) {
return fn(second, first);
};
};
};
```

### Technical frame 141: Recipes with Data / Flip / self-currying flip

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01466))_

> Sometimes we'll want to flip a function, but retain the flexibility to call it in its curried form (pass one parameter) or non-curried form (pass both). We could make that into flip :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01468))_

<a id="atom-technical-atom-b23695ce3f4989e7"></a>

> Nowif we write mapWith = flip(map) , we can call mapWith(fn, list) or mapWith(fn)(list) , our choice.

### Technical frame 142: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01533))_

<a id="atom-technical-atom-0494f9669763f688"></a>

```
const Stack1 = () =>
({
array:[],
index: -1,
push (value) {
return this.array[this.index += 1] = value;
},
pop () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty () {
return this.index < 0
},
iterator () {
let iterationIndex = this.index;
return () => {
if (iterationIndex > this.index) {
iterationIndex = this.index;
}
if (iterationIndex < 0) {
return {done: true};
}
else {
return {done: false, value: this.array[iterationIndex--]}
}
}
}
});
const stack = Stack1();
stack.push("Greetings");
stack.push("to");
stack.push("you!")
```

### Technical frame 143: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01534))_

<a id="atom-technical-atom-977c2f6172e80243"></a>

```
const iter = stack.iterator();
iter().value
//=> "you!"
iter().value
//=> "to"
```

### Technical frame 144: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01541))_

> We could save a step and write collectionSum , a function that folds over any object, provided that the object implements an .iterator method:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01538))_

<a id="atom-technical-atom-ef867f51aa5d4e3b"></a>

```
const iteratorSum = (iterator) => {
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
```

### Technical frame 145: Served by the Pot: Collections / Iteration and Iterables / a look back at functional iterators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01543))_

> If we write a program with the presumption that 'everything is an object,' we can write maps, folds, and filters that work on objects. We just ask the object for an iterator, and work on the iterator. Our functions don't need to know anything about how an object implements iteration, and we get the benefit of lazily traversing our objects.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01542))_

<a id="atom-technical-atom-bc96f54b184676fd"></a>

```
const collectionSum = (collection) => {
const iterator = collection.iterator();
let eachIteration,
sum = 0;
while ((eachIteration = iterator(), !eachIteration.done)) {
sum += eachIteration.value;
}
return sum
}
collectionSum(stack)
//=> 6
```

### Technical frame 146: Like this: / from

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01614))_

> We can do the same with our own collections. As you recall, functions are mutable objects. And we can assign properties to functions with a . or even [ and ] . And if we assign a function to a property, we've created a method.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01613))_

<a id="atom-technical-atom-519518765b459b83"></a>

```
Array.from(UpTo1000)
//=> [1,81,121,361,441,841,961]
```

### Technical frame 147: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01671))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01670))_

<a id="atom-technical-atom-f8e039c42865fbe9"></a>

```
function * only (something) {
yield something;
};
only("you").next()
//=>
{"done":false, value: "you"}
```

### Technical frame 148: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01712))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01709))_

<a id="atom-technical-atom-f851858a3f0a60d5"></a>

> If we call our generator function more than once, we get new iterators.

### Technical frame 149: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01712))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01710))_

<a id="atom-technical-atom-df68b9aee54b4fac"></a>

```
const ThreeNumbers = {
[Symbol.iterator]: function * () {
yield 1;
yield 2;
yield 3
}
}
for (const i of ThreeNumbers) {
console.log(i);
}
//=>
1
2
3
[...ThreeNumbers]
//=>
[1,2,3]
const iterator = ThreeNumbers[Symbol.iterator]();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
```

### Technical frame 150: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01714))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01713))_

<a id="atom-technical-atom-08b3d4cd0486cddf"></a>

```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```

### Technical frame 151: We'll keep it simple: / more generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01725))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01727))_

<a id="atom-technical-atom-10237a444786ad38"></a>

```
function * fibonacci () {
let a, b;
yield a = 0;
yield b = 1;
while (true) {
[a, b] = [b, a + b]
yield b;
}
}
for (const i of fibonacci()) {
console.log(i);
}
//=>
0
1
1
2
3
5
8
13
21
34
55
89
144
...
```

### Technical frame 152: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01731))_

> We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01730))_

<a id="atom-technical-atom-c3426fdb123a0599"></a>

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

### Technical frame 153: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01734))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01732))_

<a id="atom-technical-atom-aa5a13c431df832a"></a>

> But if you can write it as a simple generator, write it as a simple generator.

### Technical frame 154: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01734))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01733))_

<a id="atom-technical-atom-79c4ba4c0edddbb5"></a>

```
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
for (const ee of tree(e)) {
yield ee;
}
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
```

### Technical frame 155: We get: / interactive generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01941))_

> Served by the Pot: Collections 260 } } break ; // ... } } const aNaughtsAndCrossesGame = generatorNaughtsAndCrosses(); We can then get the first move by calling .next() . Thereafter, we call .next(...) and pass in our moves (The very first call has to be .next() without any arguments, because the generator hasn't started yet. If we wanted to pass some state to the generator before it begins, we'd do that with parameters.): aNaughtsAndCrossesGame.next().value //=> 0 aNaughtsAndCrossesGame.next(1)

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01940))_

<a id="atom-technical-atom-c587d1518ea98f21"></a>

```
function* generatorNaughtsAndCrosses () {
const x1 = yield 0;
switch (x1) {
case 1:
const x2 = yield 6;
switch (x2) {
case 2:
case 4:
case 5:
case 7:
case 8:
yield 3;
break;
case 3:
const x3 = yield 8;
switch (x3) {
case 2:
case 5:
case 7:
yield 4;
break;
case 4:
yield 7;
break;
```

### Technical atom 156

<a id="atom-technical-atom-6eea21698f698a20"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00236))_

> We said that the function returns the result of evaluating a block , and we said that a block is a (possibly empty) list of JavaScript statements separated by semicolons. 21

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00234))_

```text
back on the block
Back to our function. We evaluated this:
19 Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace.
20 As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined . We have no idea.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 19 | Experienced JavaScript programmers are aware that there's a fourth way, using a function argument. This was actually the preferred mechanism until void became commonplace. |
| 20 | As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined. We have no idea. |

</details>

### Technical atom 157

<a id="atom-technical-atom-40032b1d8caeb152"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00612))_

> arguments always contains all of the arguments passed to a function, regardless of how many are declared. Therefore, we can write plus like this:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00613))_

```text
42 You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times.
43 We'll look at arrays and plain old javascript objects in depth later.
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 42 | You should never attempt to define your own bindings against 'magic' names that JavaScript binds for you. It is wise to treat them as read-only at all times. |
| 43 | We'll look at arrays and plain old javascript objects in depth later. |

</details>

### Technical atom 158

<a id="atom-technical-atom-5fc857e371a9ac51"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00660))_

> These two recipes are for quickly and simply applying a single argument, either the leftmost or rightmost. 48 If you want to bind more than one argument, or you want to leave a 'hole' in the argument list, you will need to either use a generalized partial recipe, or you will need to repeatedly apply arguments. They are context-agnostic.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00663))_

```text
45 https://github.com/fogus/lemonad 46 http://osteele.com/sources/javascript/functional/ 47 https://github.com/substack/node-ap 48
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 45 | https://github.com/fogus/lemonad |
| 46 | http://osteele.com/sources/javascript/functional/ |
| 47 | https://github.com/substack/node-ap 48 |

</details>

### Technical atom 159

<a id="atom-technical-atom-1f79a4f59b7f455a"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00700))_

> Naturally, there's a function decorator recipe for that, borrowed from Haskell's maybe monad 50 , Ruby's andand 51 , and CoffeeScript's existential method invocation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00702))_

```text
50 https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad
51 https://github.com/raganwald/andand
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 50 | https://en.wikipedia.org/wiki/Monad_(functional_programming)#The_Maybe_monad |
| 51 | https://github.com/raganwald/andand |

</details>

### Technical atom 160

<a id="atom-technical-atom-281a1ae07258b1dc"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01333))_

> The oscin.es 77 library contains code for all of the standard combinators and for experimenting using the standard notation.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01335))_

```text
76 http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422
77 http://oscin.es
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 76 | http://www.amazon.com/gp/product/0192801422/ref=as_li_ss_tl?ie=UTF8&tag=raganwald001-20&linkCode=as2&camp=1789&creative= 390957&creativeASIN=0192801422 |
| 77 | http://oscin.es |

</details>


## Source

- [[javascriptallonge]]
