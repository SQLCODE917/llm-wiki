---
page_id: javascriptallonge-declaration
page_kind: concept
summary: Declaration: 4 statement(s) and 8 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-declaration@48ddbc0a4cd915cf7130a390780b302a
---

# Declaration

What [[javascriptallonge]] covers about declaration:

## Statements

### function declarations

- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-31a4cf47-00543))_

### function declaration caveats 34

- Function declarations are formally only supposed to be made at what we might call the 'top level' of a function. Although some JavaScript environments permit the following code, this example is technically illegal and definitely a bad idea: _(javascriptallonge.pdf (source-range-31a4cf47-00551))_

- Function declarations are not supposed to occur inside of blocks. The big trouble with expressions like this is that they may work just fine in your test environment but work a different way in production. Or it may work one way today and a different way when the JavaScript engine is updated, say with a new optimization. _(javascriptallonge.pdf (source-range-31a4cf47-00554))_

### var

- But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: _(javascriptallonge.pdf (source-range-31a4cf47-01194))_


## Technical atoms

### Technical frame 1: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00543))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00541))_

```
function someName () { // ... } This behaves a little like: const someName = function someName () // ... }
```

### Technical frame 2: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00543))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00542))_

```
{
```

### Technical frame 3: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00549))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00547))_

```
( function () { return fizzbuzz(); function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> 'FizzBuzz' Although fizzbuzz is declared later in the function, JavaScript behaves as if we'd written: ( function () { {
```

### Technical frame 4: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00549))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00548))_

```
const fizzbuzz = function fizzbuzz () return "Fizz" + "Buzz"; } return fizzbuzz(); })()
```

### Technical frame 5: function declaration caveats 34

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00557))_

> The parentheses make this an expression, not a function declaration.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00556))_

```
function trueDat () { return true } But this is not: ( function trueDat () { return true })
```

### Technical frame 6: var

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01193))_

> Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01192))_

```
(() => { var age = 49; if ( true ) { var age = 50; } return age; })() //=> 50
```

### Technical frame 7: var

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01195))_

```
const factorial = (n) => { return innerFactorial(n, 1); function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> 24
```

### Technical frame 8: var

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-01200))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-01199))_

```
const factorial = (n) => { let innerFactorial = undefined ; return innerFactorial(n, 1); innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from function declarations: In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of ... [truncated]; Function shares technical record from function declarations: function someName () { // ... } This behaves a little like: const someName = function someName () // ... } (4 shared statement(s), 7 shared atom(s))
- [[javascriptallonge-bound]] - shared technical atoms: Bound shares technical record from function declarations: ( function () { return fizzbuzz(); function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> 'FizzBuzz' Although fizzbuzz is declared later in the function, JavaScr ... [truncated] (2 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from var: const factorial = (n) => { return innerFactorial(n, 1); function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } fa ... [truncated] (2 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from function declarations: { (1 shared atom(s))
- [[javascriptallonge-expression]] - shared technical atoms: Expression shares technical record from function declaration caveats 34: function trueDat () { return true } But this is not: ( function trueDat () { return true }) (1 shared atom(s))

## Source

- [[javascriptallonge]]
