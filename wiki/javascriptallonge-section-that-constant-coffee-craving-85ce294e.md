---
page_id: javascriptallonge-section-that-constant-coffee-craving-85ce294e
page_kind: source
summary: That Constant Coffee Craving: 13 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-that-constant-coffee-craving-85ce294e@4857b02149bc382cf5a9520cfa82ed64
---

# That Constant Coffee Craving

From [[javascriptallonge]].

## Statements

- Up to now, all we've really seen are anonymous functions , functions that don't have a name. This feels very different from programming in most other languages, where the focus is on naming functions, methods, and procedures. Naming things is a critical part of programming, but all we've seen so far is how to name arguments. _(javascriptallonge.pdf (source-range-8eb13d6b-00388))_
- In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . If we put our function expression in parentheses, we can apply it to the argument of 3.14159265 : _(javascriptallonge.pdf (source-range-8eb13d6b-00391))_
- This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 . _(javascriptallonge.pdf (source-range-8eb13d6b-00395))_
- That works! We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind. 29 _(javascriptallonge.pdf (source-range-8eb13d6b-00399))_

## Technical atoms

### Technical frame 1: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00391))_

> In order to bind 3.14159265 to the name PI , we'll need a function with a parameter of PI applied to an argument of 3.14159265 . If we put our function expression in parentheses, we can apply it to the argument of 3.14159265 :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00389))_

> There are other ways to name things in JavaScript, but before we learn some of those, let's see how to use what we already have to name things. Let's revisit a very simple example:

### Technical frame 2: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00395))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00392))_

```
((PI) => // ???? )(3.14159265)
```

### Technical frame 3: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00395))_

> This expression, when evaluated, returns a function that calculates circumferences. That sounds bad, but when we think about it, (diameter) => diameter * 3.14159265 is also an expression, that when evaluated, returns a function that calculates circumferences. All of our 'functions' are expressions. This one has a few more moving parts, that's all. But we can use it just like (diameter) => diameter * 3.14159265 .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00394))_

```
((PI) => (diameter) => diameter * PI )(3.14159265)
```

### Technical frame 4: That Constant Coffee Craving

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00399))_

> That works! We can bind anything we want in an expression by wrapping it in a function that is immediately invoked with the value we want to bind. 29

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00398))_

```
((diameter) => diameter * 3.14159265)(2) //=> 6.2831853 ((PI) => (diameter) => diameter * PI )(3.14159265)(2) //=> 6.2831853
```
