---
page_id: javascriptallonge-section-and-also-naming-functions-function-declarations-25fc9c63
page_kind: source
summary: And also: / Naming Functions / function declarations: 15 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-naming-functions-function-declarations-25fc9c63@157a97eff81eed6cdd19e04fb6c7c0b4
---

# And also: / Naming Functions / function declarations

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-and-also-naming-functions-37c9be8d]] - broader source section: And also: / Naming Functions

## Statements

- There is another syntax for naming and/or defining a function. It's called a function declaration statement , and it looks a lot like a named function expression, only we use it as a statement: _(javascriptallonge.pdf (source-range-7239e085-00537))_
- In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur. _(javascriptallonge.pdf (source-range-7239e085-00540))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently: _(javascriptallonge.pdf (source-range-7239e085-00543))_
- The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code. _(javascriptallonge.pdf (source-range-7239e085-00546))_
- We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. _(javascriptallonge.pdf (source-range-7239e085-00543))_

## Technical atoms

### Technical frame 1: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00540))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00538))_

```
function someName () {
// ...
}
This behaves a little like:
const someName = function someName ()
// ...
}
```

### Technical frame 2: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00540))_

> In that it binds a name in the environment to a named function. However, there are two important differences. First, function declarations are hoisted to the top of the function in which they occur.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00539))_

```
{
```

### Technical frame 3: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00543))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00541))_

> Consider this example where we try to use the variable fizzbuzz as a function before we bind a function to it with const :

### Technical frame 4: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00543))_

> We haven't actually bound a function to the name fizzbuzz before we try to use it, so we get an error. But a function declaration works differently:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00542))_

```
(function () {
return fizzbuzz();
const fizzbuzz = function fizzbuzz () {
return "Fizz" + "Buzz";
}
})()
//=> undefined is not a function (evaluating 'fizzbuzz()')
```

### Technical frame 5: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00546))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00544))_

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

### Technical frame 6: And also: / Naming Functions / function declarations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00546))_

> The definition of the fizzbuzz is 'hoisted' to the top of its enclosing scope (an IIFE in this case). This behaviour is intentional on the part of JavaScript's design to facilitate a certain style of programming where you put the main logic up front, and the 'helper functions' at the bottom. It is not necessary to declare functions in this way in JavaScript, but understanding the syntax and its behaviour (especially the way it differs from const ) is essential for working with production code.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00545))_

```
const fizzbuzz = function fizzbuzz ()
return "Fizz" + "Buzz";
}
return fizzbuzz();
})()
```
