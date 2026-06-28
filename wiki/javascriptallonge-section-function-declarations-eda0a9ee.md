---
page_id: javascriptallonge-section-function-declarations-eda0a9ee
page_kind: source
summary: function declarations: 15 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-function-declarations-eda0a9ee@568ecdfca001ea77829fa24fe1783472
---

# function declarations

From [[javascriptallonge]].

## Statements

- There is another syntax for naming and/or defining a function. It's called a function declaration statement , and it looks a lot like a named function expression, only we use it as a statement: _(javascriptallonge.pdf (source-range-31a4cf47-00540))_
- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-31a4cf47-00543))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently: _(javascriptallonge.pdf (source-range-31a4cf47-00546))_
- The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code. _(javascriptallonge.pdf (source-range-31a4cf47-00549))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-31a4cf47-00546))_

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

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00546))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00544))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const :

### Technical frame 4: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00546))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00545))_

```
( function () { return fizzbuzz(); const fizzbuzz = function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> undefined is not a function (evaluating 'fizzbuzz()')
```

### Technical frame 5: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00549))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00547))_

```
( function () { return fizzbuzz(); function fizzbuzz () { return "Fizz" + "Buzz"; } })() //=> 'FizzBuzz' Although fizzbuzz is declared later in the function, JavaScript behaves as if we'd written: ( function () { {
```

### Technical frame 6: function declarations

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00549))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00548))_

```
const fizzbuzz = function fizzbuzz () return "Fizz" + "Buzz"; } return fizzbuzz(); })()
```
