---
page_id: javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-e91633ac
page_kind: source
summary: values are expressions / As Little As Possible About Functions, But No Less: 77 source-backed entries and 12 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-e91633ac@457933fa68dfced76f332cd40c2ddb51
---

# values are expressions / As Little As Possible About Functions, But No Less

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-values-are-expressions-4763e204]] - broader source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-0-ea5573e4]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-functions-and-identitie-eff6f784]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-applying-functions-912900c1]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-fnexpr-args-f89f653e]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-functions-that-return-v-ab68fb84]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-commas-49c0b74b]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-the-simplest-possible-b-86d186d5]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-cb5dd629]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-undefined-c6b467fa]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-undefined-125f50a5]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-void-a81e28f2]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-back-on-the-block-2e4f02ef]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-1d1453ee]] - narrower source section
- [[javascriptallonge-section-values-are-expressions-as-little-as-possible-about-functions-but-no-less-functions-that-evaluate-466a3da3]] - narrower source section

## Statements

- Like numbers, strings, and arrays, they have a representation. _(javascriptallonge.pdf (source-range-83ecb080-00218))_
- Functions represent computations to be performed. _(javascriptallonge.pdf (source-range-83ecb080-00218))_
- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. _(javascriptallonge.pdf (source-range-83ecb080-00218))_

## Statements by subsection

### values are expressions / As Little As Possible About Functions, But No Less / () => 0

- This is a function that is applied to no values and returns 0. _(javascriptallonge.pdf (source-range-83ecb080-00220))_
- [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. _(javascriptallonge.pdf (source-range-83ecb080-00221))_
- But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function. _(javascriptallonge.pdf (source-range-83ecb080-00225))_
- I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. _(javascriptallonge.pdf (source-range-83ecb080-00225))_

### values are expressions / As Little As Possible About Functions, But No Less / functions and identities

- Reference types do not. _(javascriptallonge.pdf (source-range-83ecb080-00227))_
- Value types share the same identity if they have the same contents. _(javascriptallonge.pdf (source-range-83ecb080-00227))_
- You recall that we have two types of values with respect to identity: Value types and reference types. _(javascriptallonge.pdf (source-range-83ecb080-00227))_
- “Function” is a reference type. _(javascriptallonge.pdf (source-range-83ecb080-00229))_

### values are expressions / As Little As Possible About Functions, But No Less / applying functions

- The way we use functions is to _apply_ them to zero or more values called _arguments_ . _(javascriptallonge.pdf (source-range-83ecb080-00231))_
- Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. _(javascriptallonge.pdf (source-range-83ecb080-00232))_

### values are expressions / As Little As Possible About Functions, But No Less / fnexpr ( args )

- We’ll put it in parentheses[17] to keep the parser happy, like we did above: (() => 0). _(javascriptallonge.pdf (source-range-83ecb080-00234))_
- Right now, we only know about one such expression: () => 0, so let’s use it. _(javascriptallonge.pdf (source-range-83ecb080-00234))_
- Right now, we only know about one such expression: () => 0, so let’s use it. _(javascriptallonge.pdf (source-range-83ecb080-00234))_
- > 17If you’re used to other programming languages, you’ve probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00235))_

### values are expressions / As Little As Possible About Functions, But No Less / functions that return values and evaluate expressions

- Likewise, the following all ought to be obvious: (() => 1)() _//=> 1_ (() => "Hello, JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** )() _//=> Infinity_ _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- We know that (() => 0)() returns 0, and this is unsurprising. _(javascriptallonge.pdf (source-range-83ecb080-00239))_
- Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00240))_
- In the prelude, we looked at expressions. _(javascriptallonge.pdf (source-range-83ecb080-00241))_
- Values like 0 are expressions, as are things like 40 + 2. _(javascriptallonge.pdf (source-range-83ecb080-00241))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- We can put any expression to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00243))_
- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-83ecb080-00245))_

### values are expressions / As Little As Possible About Functions, But No Less / commas

- The comma operator in JavaScript is interesting. _(javascriptallonge.pdf (source-range-83ecb080-00251))_
- In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00255))_

### values are expressions / As Little As Possible About Functions, But No Less / the simplest possible block

- A block has zero or more _statements_ , separated by semicolons.[18] So, this is a valid function: _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- There’s another thing we can put to the right of an arrow, a _block_ . _(javascriptallonge.pdf (source-range-83ecb080-00258))_

### values are expressions / As Little As Possible About Functions, But No Less / () => {}

- It returns the result of evaluating a block that has no statements. _(javascriptallonge.pdf (source-range-83ecb080-00260))_

### values are expressions / As Little As Possible About Functions, But No Less / undefined

- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-83ecb080-00263))_
- It will crop up again. _(javascriptallonge.pdf (source-range-83ecb080-00263))_
- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-83ecb080-00263))_

### values are expressions / As Little As Possible About Functions, But No Less / undefined

- Like numbers, booleans and strings, JavaScript can print out the value undefined. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- No matter how you evaluate undefined, you get an identical value back. _(javascriptallonge.pdf (source-range-83ecb080-00269))_
- > 18Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. _(javascriptallonge.pdf (source-range-83ecb080-00270))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-83ecb080-00270))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-83ecb080-00270))_
- In JavaScript, every undefined is identical to every other undefined. _(javascriptallonge.pdf (source-range-83ecb080-00273))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. _(javascriptallonge.pdf (source-range-83ecb080-00273))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can’t be equal. _(javascriptallonge.pdf (source-range-83ecb080-00273))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can’t be equal. _(javascriptallonge.pdf (source-range-83ecb080-00273))_

### values are expressions / As Little As Possible About Functions, But No Less / void

- We’ve seen that JavaScript represents an undefined value by typing undefined, and we’ve generated undefined values in two ways: _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- So, when we deliberately want an undefined value, should we use the first, second, or third form?[19] The answer is, use void. _(javascriptallonge.pdf (source-range-83ecb080-00278))_
- Behold: **void** 0 _//=> undefined_ **void** 1 _//=> undefined_ **void** (2 + 2) _//=> undefined_ void is an operator that takes any value and evaluates to undefined, always. _(javascriptallonge.pdf (source-range-83ecb080-00278))_
- The first form works but it’s cumbersome. _(javascriptallonge.pdf (source-range-83ecb080-00279))_
- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we’ll discuss in Reassignment and Mutation. _(javascriptallonge.pdf (source-range-83ecb080-00279))_

### values are expressions / As Little As Possible About Functions, But No Less / back on the block

- This was actually the preferred mechanism until void became commonplace. _(javascriptallonge.pdf (source-range-83ecb080-00282))_
- > 19Experienced JavaScript programmers are aware that there’s a fourth way, using a function argument. _(javascriptallonge.pdf (source-range-83ecb080-00282))_
- > 20As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined. _(javascriptallonge.pdf (source-range-83ecb080-00283))_

### values are expressions / As Little As Possible About Functions, But No Less / (() => {})()

- There are many kinds of JavaScript statements, but the first kind is one we’ve already met. _(javascriptallonge.pdf (source-range-83ecb080-00289))_
- An expression is a JavaScript statement. _(javascriptallonge.pdf (source-range-83ecb080-00289))_
- Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- > 21You can also separate statements with line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. _(javascriptallonge.pdf (source-range-83ecb080-00290))_
- This feature was originally created as a kind of helpful error-correction. _(javascriptallonge.pdf (source-range-83ecb080-00290))_

### values are expressions / As Little As Possible About Functions, But No Less / functions that evaluate to functions

- So we have _a function, that returns a function, that returns zero_ . _(javascriptallonge.pdf (source-range-83ecb080-00301))_
- It’s a function that when applied, evaluates to a function that when applied, evaluates to 0. _(javascriptallonge.pdf (source-range-83ecb080-00301))_
- We’ve been very clever, but so far this all seems very abstract. _(javascriptallonge.pdf (source-range-83ecb080-00303))_
- So… In the next chapter, “I’d Like to Have an Argument, Please,” we’ll see how to make functions practical. _(javascriptallonge.pdf (source-range-83ecb080-00303))_
- Diffraction of a crystal is beautiful and interesting in its own right, but you can’t blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. _(javascriptallonge.pdf (source-range-83ecb080-00303))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00220))_

> This is a function that is applied to no values and returns 0. Let’s verify that our function is a value like all others:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00221))_

> If you try the same thing in a browser, you may see something else.

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00221))_

> (() => 0) _//=> [Function]_ What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00222))_

> > 16 The simplest possible function is () => {}, we’ll see that later.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00240))_

> Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00242))_

> (() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00243))_

> Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)()?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00244))_

> Let’s try it: (() => (() => 0)())() _//=> 0_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00245))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00246))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00246))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out. So we can also write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00248))_

> The first sip: Basic Functions (() => (() => 0 )() )() _//=> 0_

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00251))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00253))_

> (1 + 1, 2 + 2) _//=> 4_

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00251))_

> The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00254))_

> We can use commas with functions to create functions that evaluate multiple expressions: (() => (1 + 1, 2 + 2))() _//=> 4_

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00254))_

> We can use commas with functions to create functions that evaluate multiple expressions: (() => (1 + 1, 2 + 2))() _//=> 4_

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00255))_

> This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later.

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00269))_

> No matter how you evaluate undefined, you get an identical value back. undefined is a value that means “I don’t have a value.” But it’s still a value :-)

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00267))_

> **undefined** === **undefined**

### Technical atom 11

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00293))_

> The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example: (() => { 1 + 1; **return** 2 + 2 })() _//=> 4_ And also: (() => { **return** 1 + 1; 2 + 2 })() _//=> 2_

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00294))_

> The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression:

### Technical atom 12

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00300))_

> If an expression that evaluates to a function is, well, an expression, and if a return statement can have any expression on its right side… _Can we put an expression that evaluates to a function on the right side of a function expression?_
