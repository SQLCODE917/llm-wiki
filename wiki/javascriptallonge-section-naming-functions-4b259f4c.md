---
page_id: javascriptallonge-section-naming-functions-4b259f4c
page_kind: source
summary: Naming Functions: 55 source-backed entries and 16 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-naming-functions-4b259f4c@593e8bd90fc3ad81aeefa8f264326c42
---

# Naming Functions

From [[javascriptallonge]].

## Statements

- This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-83ecb080-00696))_
- JavaScript _does_ have a syntax for naming a function, we use the function keyword. _(javascriptallonge.pdf (source-range-83ecb080-00698))_
- Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-83ecb080-00698))_
- Something else we’re about to discuss is optional. _(javascriptallonge.pdf (source-range-83ecb080-00705))_
- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-83ecb080-00706))_
- We do not have a fat arrow, we go directly to the body. _(javascriptallonge.pdf (source-range-83ecb080-00707))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-83ecb080-00708))_
- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-83ecb080-00708))_
- While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- That may seem confusing, but think of the binding names as properties of the environment, not of the function. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- This is a _named function expression_ . _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- In this expression, double is the name in the environment, but repeat is the function’s actual name. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- > 33“Yes of course?” Well, in chapter of a book dedicated to naming functions, it is not surprising that feature we mention has something to do with naming functions. _(javascriptallonge.pdf (source-range-83ecb080-00725))_
- Now, the function’s actual name has no effect on the environment in which it is used. _(javascriptallonge.pdf (source-range-83ecb080-00729))_
- So “actualName” isn’t bound in the environment where we use the named function expression. _(javascriptallonge.pdf (source-range-83ecb080-00733))_
- Here’s a function that determines whether a positive integer is even or not. _(javascriptallonge.pdf (source-range-83ecb080-00733))_
- Clearly, the name even is bound to the function _within the function’s body_ . _(javascriptallonge.pdf (source-range-83ecb080-00735))_
- This is useful for making recursive functions as we see above, and it speaks to the principle of least privilege: If you don’t _need_ to name it anywhere else, you needn’t. _(javascriptallonge.pdf (source-range-83ecb080-00740))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-83ecb080-00740))_
- even is bound within the function itself, but not outside it. _(javascriptallonge.pdf (source-range-83ecb080-00740))_
- There is another syntax for naming and/or defining a function. _(javascriptallonge.pdf (source-range-83ecb080-00742))_
- However, there are two important differences. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- First, function declarations are _hoisted_ to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- In that it binds a name in the environment to a named function. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- We haven’t actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-83ecb080-00755))_
- We haven’t actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-83ecb080-00755))_
- This behaviour is intentional on the part of JavaScript’s design to facilitate a certain style of programming where you put the main logic up front, and the “helper functions” at the bottom. _(javascriptallonge.pdf (source-range-83ecb080-00762))_
- The definition of the fizzbuzz is “hoisted” to the top of its enclosing scope (an IIFE in this case). _(javascriptallonge.pdf (source-range-83ecb080-00762))_
- It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const) is essential for working with production code. _(javascriptallonge.pdf (source-range-83ecb080-00762))_
- Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- Function declarations are formally only supposed to be made at what we might call the “top level” of a function. _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- Function declarations are formally only supposed to be made at what we might call the “top level” of a function. _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- 34 A number of the caveats discussed here were described in Jyrly Zaytsev’s excellent article Named function expressions demystified. _(javascriptallonge.pdf (source-range-83ecb080-00765))_
- The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. _(javascriptallonge.pdf (source-range-83ecb080-00771))_
- Another caveat is that a function declaration cannot exist inside of _any_ expression, otherwise it’s a function expression. _(javascriptallonge.pdf (source-range-83ecb080-00771))_
- The parentheses make this an expression, not a function declaration. _(javascriptallonge.pdf (source-range-83ecb080-00775))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00694, source-range-83ecb080-00696))_

> Let’s get right to it. This code does _not_ name a function: It doesn’t name the function “repeat” for the same reason that const answer = 42 doesn’t name the number 42. This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00695))_

> **const** repeat = (str) => str + str

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00699))_

> Here’s our repeat function written using a “fat arrow”

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00700))_

> (str) => str + str

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00708))_

> We always use a block, we cannot write function (str) str + str.

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00708))_

> 5. We always use a block, we cannot write function (str) str + str. This means that if we want our functions to return a value, we always need to use the return keyword

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00709))_

> If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g.

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00709))_

> If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00710))_

> (n) => (1.618**n - -1.618**-n) / 2.236

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00716))_

> Here are our example functions written with names:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00718))_

> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00718))_

> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00719))_

> **const double** = **function** repeat (str) { **return** str + str; }

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00729))_

> Now, the function’s actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00730))_

> **const** bindingName = **function** actualName () { _//..._

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00729))_

> Now, the function’s actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00731))_

> }; bindingName _//=> [Function: actualName]_

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00729))_

> Now, the function’s actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00732))_

> actualName _//=> ReferenceError: actualName is not defined_

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00746))_

> This behaves a _little_ like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00747))_

> **const** someName = **function** someName () {

### Technical atom 12

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00751))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const:

### Technical atom 13

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00751))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00754))_

> **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> undefined is not a function (evaluating 'fizzbuzz()')_

### Technical atom 14

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00759))_

> **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } })() _//=> 'FizzBuzz'_

### Technical atom 15

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00760))_

> Although fizzbuzz is declared later in the function, JavaScript behaves as if we’d written:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00761))_

> ( **function** () { **const** fizzbuzz = **function** fizzbuzz () { **return** "Fizz" + "Buzz"; } **return** fizzbuzz(); })()

### Technical atom 16

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00770))_

> Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization.
