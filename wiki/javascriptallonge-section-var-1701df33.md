---
page_id: javascriptallonge-section-var-1701df33
page_kind: source
summary: var: 15 source-backed entries and 6 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-var-1701df33@4be23fa1a7982120c9bf5792bf93e0a9
---

# var

From [[javascriptallonge]].

## Statements

- JavaScript has one more way to bind a name to a value, var . 71 var looks a lot like let : _(javascriptallonge.pdf (source-range-8eb13d6b-01186))_
- But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations: _(javascriptallonge.pdf (source-range-8eb13d6b-01190))_
- Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations. _(javascriptallonge.pdf (source-range-8eb13d6b-01192))_
- But, again, it is unwise to expect consistency. A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. Note this example of a function that uses a helper: _(javascriptallonge.pdf (source-range-8eb13d6b-01193))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped. _(javascriptallonge.pdf (source-range-8eb13d6b-01199))_
- A function declaration can appear anywhere within a function, but the declaration and the definition are hoisted. _(javascriptallonge.pdf (source-range-8eb13d6b-01193))_
- In that way, var is a little like const and let , we should always declare and bind names before using them. _(javascriptallonge.pdf (source-range-8eb13d6b-01199))_

## Technical atoms

### Technical frame 1: var

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01190))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01187))_

```
const factorial = (n) => { let x = n; if (x === 1) { return 1; } else { --x; return n * factorial(x); } } factorial(5) //=> 120 const factorial2 = (n) => { var x = n; if (x === 1) { return 1; } else { --x;
```

### Technical frame 2: var

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01190))_

> But of course, it's not exactly like let . It's just different enough to present a source of confusion. First, var is not block scoped, it's function scoped, just like function declarations:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01189))_

```
return n * factorial2(x); } } factorial2(5) //=> 120
```

### Technical frame 3: var

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01192))_

> Declaring age twice does not cause an error(!), and the inner declaration does not shadow the outer declaration. All var declarations behave as if they were hoisted to the top of the function, a little like function declarations.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01191))_

```
(() => { var age = 49; if ( true ) { var age = 50; } return age; })() //=> 50
```

### Technical frame 4: var

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01199))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01194))_

```
const factorial = (n) => { return innerFactorial(n, 1); function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> 24
```

### Technical frame 5: var

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01199))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01196))_

```
const factorial = (n) => { let innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } return innerFactorial(n, 1); } JavaScript hoists the let and the assignment. But not so with var : const factorial = (n) => { return innerFactorial(n, 1); var innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```

### Technical frame 6: var

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01199))_

> In that way, var is a little like const and let , we should always declare and bind names before using them. But it's not like const and let in that it's function scoped, not block scoped.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01198))_

```
const factorial = (n) => { let innerFactorial = undefined ; return innerFactorial(n, 1); innerFactorial = function innerFactorial (x, y) { if (x == 1) { return y; } else { return innerFactorial(x-1, x * y); } } } factorial(4) //=> undefined is not a function (evaluating 'innerFactorial(n, 1)')
```
