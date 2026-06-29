---
page_id: javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-0ed59777
page_kind: source
summary: The first sip: Basic Functions / As Little As Possible About Functions, But No Less: 41 source-backed entries and 16 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-0ed59777@2039db37f19b4935fa12c143d0752a79
---

# The first sip: Basic Functions / As Little As Possible About Functions, But No Less

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-the-first-sip-basic-functions-310a8867]] - broader source section: The first sip: Basic Functions
- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-and-id-04ebbc48]] - narrower source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities
- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-applying-functio-9dc686e6]] - narrower source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions
- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-functions-that-r-953101e3]] - narrower source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions
- [[javascriptallonge-section-the-first-sip-basic-functions-as-little-as-possible-about-functions-but-no-less-commas-613f6e9a]] - narrower source section: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

## Statements

- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let's start with the second simplest possible function. 16 In JavaScript, it looks like this: _(javascriptallonge.pdf (source-range-7239e085-00168))_
- This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others: _(javascriptallonge.pdf (source-range-7239e085-00170))_
- What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else. _(javascriptallonge.pdf (source-range-7239e085-00172))_
- I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function. _(javascriptallonge.pdf (source-range-7239e085-00174))_

## Statements by subsection

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

- You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not. _(javascriptallonge.pdf (source-range-7239e085-00176))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions

- Let's put functions to work. The way we use functions is to apply them to zero or more values called arguments . Just as 2 + 2 produces a value (in this case 4 ), applying a function to zero or more arguments produces a value as well. _(javascriptallonge.pdf (source-range-7239e085-00181))_
- Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write: _(javascriptallonge.pdf (source-range-7239e085-00184))_
- 17 If you're used to other programming languages, you've probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages! _(javascriptallonge.pdf (source-range-7239e085-00186))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

- We've seen () => 0 . We know that (() => 0)() returns 0 , and this is unsurprising. Likewise, the following all ought to be obvious: _(javascriptallonge.pdf (source-range-7239e085-00188))_
- Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-7239e085-00190))_
- In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2 . Can we put an expression to the right of the arrow? _(javascriptallonge.pdf (source-range-7239e085-00191))_
- Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ? _(javascriptallonge.pdf (source-range-7239e085-00193))_
- Yes we can! Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-7239e085-00196))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-7239e085-00193))_

### The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

- The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: _(javascriptallonge.pdf (source-range-7239e085-00201))_
- This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write: _(javascriptallonge.pdf (source-range-7239e085-00205))_

## Technical atoms

### Technical frame 1: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00170))_

> This is a function that is applied to no values and returns 0 . Let's verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00169))_

```
() => 0
```

### Technical frame 2: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00172))_

> What!? Why didn't it type back () => 0 for us? This seems to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What's going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a br

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00171))_

```
(() => 0)
//=> [Function]
```

### Technical frame 3: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00174))_

> I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00172))_

> If you try the same thing in a browser, you may see something else.

### Technical frame 4: The first sip: Basic Functions / As Little As Possible About Functions, But No Less

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00174))_

> I'd prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0 , internally JavaScript has a full and proper function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00173))_

> 16 The simplest possible function is () => {} , we'll see that later.

### Technical frame 5: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions and identities

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00176))_

> You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00178))_

```
(() => 0) === (() => 0)
//=> false
```

### Technical frame 6: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00184))_

> Right now, we only know about one such expression: () => 0 , so let's use it. We'll put it in parentheses 17 to keep the parser happy, like we did above: (() => 0) . Since we aren't giving it any arguments, we'll simply write () after the expression. So we write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00183))_

```
fn_expr(args)
```

### Technical frame 7: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / applying functions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00186))_

> 17 If you're used to other programming languages, you've probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages!

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00185))_

```
(() => 0)()
//=> 0
```

### Technical frame 8: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00190))_

> Well, the last one's a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00189))_

```
(() => 1)()
//=> 1
(() => "Hello, JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity)()
//=> Infinity
```

### Technical frame 9: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00193))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)() ?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00192))_

```
(() => 1 + 1)()
//=> 2
(() => "Hello, " + "JavaScript")()
//=> "Hello, JavaScript"
(() => Infinity * Infinity)()
//=> Infinity
```

### Technical frame 10: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00196))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00195))_

```
(() => (() => 0)())()
//=> 0
```

### Technical frame 11: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00196))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00197))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical frame 12: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00196))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00198))_

```
(() =>
(() => 0
)()
)()
//=> 0
```

### Technical frame 13: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00202))_

```
//=> 2
(1 + 1, 2 + 2)
```

### Technical frame 14: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00204))_

```
(() => (1 + 1, 2 + 2))()
//=> 4
```

### Technical frame 15: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00201))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later.

### Technical frame 16: The first sip: Basic Functions / As Little As Possible About Functions, But No Less / commas

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00205))_

> This is useful when trying to do things that might involve side-effects , but we'll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00206))_

```
() =>
(1 + 1, 2 + 2)
```
