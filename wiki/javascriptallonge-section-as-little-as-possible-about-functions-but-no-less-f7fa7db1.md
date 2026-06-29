---
page_id: javascriptallonge-section-as-little-as-possible-about-functions-but-no-less-f7fa7db1
page_kind: source
summary: As Little As Possible About Functions, But No Less: 13 source-backed entries and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-as-little-as-possible-about-functions-but-no-less-f7fa7db1@2eaead75b754f342510893a3b7645f4f
---

# As Little As Possible About Functions, But No Less

From [[javascriptallonge]].

## Statements

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-8eb13d6b-00172))_
- This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others: _(javascriptallonge.pdf (source-range-8eb13d6b-00174))_
- What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else. _(javascriptallonge.pdf (source-range-8eb13d6b-00176))_
- I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function. _(javascriptallonge.pdf (source-range-8eb13d6b-00178))_

## Technical atoms

### Technical frame 1: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00174))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00173))_

```
() => 0
```

### Technical frame 2: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00176))_

> What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a br

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00175))_

```
(() => 0) //=> [Function]
```

### Technical frame 3: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00178))_

> I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00176))_

> If you try the same thing in a browser, you may see something else.

### Technical frame 4: As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00178))_

> I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00177))_

> 16 The simplest possible function is () => {} , we'll see that later.
