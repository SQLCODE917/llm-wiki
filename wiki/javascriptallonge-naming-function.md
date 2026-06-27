---
page_id: javascriptallonge-naming-function
page_kind: concept
summary: Naming Functions: 33 statement(s) and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-naming-function@f779724a41ed630fb44b6e95699512e6
---

# Naming Functions

What [[javascriptallonge]] covers about naming functions:

## Statements

_Showing 14 of 33 statements selected for this topic._

- This means that if we want our functions to return a value, we always need to use the return keyword _(javascriptallonge.pdf (source-range-83ecb080-00708))_
- While the name of the function is a property of the function, not of the environment. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- First, function declarations are _hoisted_ to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-83ecb080-00750))_
- Function declarations are formally only supposed to be made at what we might call the “top level” of a function. _(javascriptallonge.pdf (source-range-83ecb080-00764))_
- This syntax binds an anonymous function to a name in an environment, but the function itself remains anonymous. _(javascriptallonge.pdf (source-range-83ecb080-00696))_
- Now, the function’s actual name has no effect on the environment in which it is used. _(javascriptallonge.pdf (source-range-83ecb080-00729))_
- Here’s a function that determines whether a positive integer is even or not. _(javascriptallonge.pdf (source-range-83ecb080-00733))_
- We haven’t actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-83ecb080-00755))_
- Function declarations are not supposed to occur inside of blocks. _(javascriptallonge.pdf (source-range-83ecb080-00770))_
- Until ECMAScript 2015 was created, function was the usual syntax for writing functions. _(javascriptallonge.pdf (source-range-83ecb080-00698))_
- JavaScript _does_ have a syntax for naming a function, we use the function keyword. _(javascriptallonge.pdf (source-range-83ecb080-00698))_
- We have arguments in parentheses, just like fat arrow functions. _(javascriptallonge.pdf (source-range-83ecb080-00706))_
- That may seem confusing, but think of the binding names as properties of the environment, not of the function. _(javascriptallonge.pdf (source-range-83ecb080-00720))_
- This is a _named function expression_ . _(javascriptallonge.pdf (source-range-83ecb080-00720))_

## Technical atoms

_Showing 6 of 13 technical atoms selected for this topic._

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

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00709))_

> If we leave out the “something optional” that comes after the function keyword, we can translate all of the fat arrow functions that we’ve seen into function keyword functions, e.g.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00710))_

> (n) => (1.618**n - -1.618**-n) / 2.236

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00718))_

> Placing a name between the function keyword and the argument list names the function. Confusingly, the name of the function is not exactly the same thing as the name we may choose to bind to the value of the function. For example, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00719))_

> **const double** = **function** repeat (str) { **return** str + str; }

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00729))_

> Now, the function’s actual name has no effect on the environment in which it is used. To whit:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00730))_

> **const** bindingName = **function** actualName () { _//..._


## Source

- [[javascriptallonge]]
