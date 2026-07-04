---
page_id: javascriptallonge-section-as-little-as-possible-about-functions-but-no-less-e6b12881
page_kind: source
page_family: section-reference
summary: As Little As Possible About Functions, But No Less: 57 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-03
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-as-little-as-possible-about-functions-but-no-less-e6b12881@ace05e555b0e9dc2ea411d067eb71a89
---

# As Little As Possible About Functions, But No Less

From [[javascriptallonge]].

## Statements

- The first sip: Basic Functions 

7 

## **As Little As Possible About Functions, But No Less** 

In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. Functions represent computations to be performed. Like numbers, strings, and arrays, they have a representation. Let’s start with the second simplest possible function.[16] In JavaScript, it looks like this: 

## () => 0 

This is a function that is applied to no values and returns 0. Let’s verify that our function is a value like all others: 

- (() => 0) _//=> [Function]_ 

What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a browser, you may see something else. 

> 16 The simplest possible function is () => {}, we’ll see that later. _(javascriptallonge.pdf (source-range-af806fb1-00042))_
- The first sip: Basic Functions 

8 

I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function. 

## **functions and identities** 

You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not. 

Which kind are functions? Let’s try them out and see. For reasons of appeasing the JavaScript parser, we’ll enclose our functions in parentheses: 

(() => 0) === (() => 0) 

_//=> false_ 

Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. “Function” is a reference type. 

## **applying functions** 

Let’s put functions to work. The way we use functions is to _apply_ them to zero or more values called _arguments_ . Just as 2 + 2 produces a value (in this case 4), applying a function to zero or more arguments produces a value as well. 

Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. Let’s call the arguments _args_ . Here’s how to apply a function to some arguments: 

## _fn_expr_ ( _args_ ) 

Right now, we only know about one such expression: () => 0, so let’s use it. We’ll put it in parentheses[17] to keep the parser happy, like we did above: (() => 0). Since we aren’t giving it any arguments, we’ll simply write () after the expression. So we write: 

(() => 0)() _//=> 0_ 

> 17If you’re used to other programming languages, you’ve probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages! _(javascriptallonge.pdf (source-range-af806fb1-00043))_
- The first sip: Basic Functions 

9 

## **functions that return values and evaluate expressions** 

We’ve seen () => 0. We know that (() => 0)() returns 0, and this is unsurprising. Likewise, the following all ought to be obvious: 

(() => 1)() _//=> 1_ (() => "Hello, JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** )() _//=> Infinity_ 

Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. 

In the prelude, we looked at expressions. Values like 0 are expressions, as are things like 40 + 2. Can we put an expression to the right of the arrow? 

(() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_ 

Yes we can. We can put any expression to the right of the arrow. For example, (() => 0)() is an expression. Can we put it to the right of an arrow, like this: () => (() => 0)()? 

Let’s try it: 

(() => (() => 0)())() _//=> 0_ 

Yes we can! Functions can return the value of evaluating another function. 

When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out. So we can also write: _(javascriptallonge.pdf (source-range-af806fb1-00044))_
- 10 

The first sip: Basic Functions 

(() => (() => 0 )() )() _//=> 0_ 

It evaluates to the same thing, 0. 

## **commas** 

The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words: 

(1, 2) _//=> 2_ 

(1 + 1, 2 + 2) _//=> 4_ 

We can use commas with functions to create functions that evaluate multiple expressions: 

(() => (1 + 1, 2 + 2))() _//=> 4_ 

This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write: 

() => (1 + 1, 2 + 2) 

Or even: 

() => ( 1 + 1, 2 + 2 

) _(javascriptallonge.pdf (source-range-af806fb1-00045))_
- The first sip: Basic Functions 

11 

## **the simplest possible block** 

There’s another thing we can put to the right of an arrow, a _block_ . A block has zero or more _statements_ , separated by semicolons.[18] 

So, this is a valid function: 

## () => {} 

It returns the result of evaluating a block that has no statements. What would that be? Let’s try it: 

(() => {})() 

_//=> undefined_ 

What is this undefined? 

## **undefined** 

In JavaScript, the absence of a value is written undefined, and it means there is no value. It will crop up again. undefined is its own type of value, and it acts like a value type: 

## **undefined** 

_//=> undefined_ 

Like numbers, booleans and strings, JavaScript can print out the value undefined. 

**undefined** === **undefined** 

_//=> true_ (() => {})() === (() => {})() _//=> true_ (() => {})() === **undefined** _//=> true_ 

No matter how you evaluate undefined, you get an identical value back. undefined is a value that means “I don’t have a value.” But it’s still a value :-) 

> 18Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. We will not take advantage of this feature, but it’s helpful to know it exists. _(javascriptallonge.pdf (source-range-af806fb1-00046))_
- 13 

The first sip: Basic Functions 

## (() => {})() 

_//=> undefined_ 

We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] 

Something like: { statement[1] ; statement[2] ; statement[3] ; ... ; statement[n] } 

We haven’t discussed these _statements_ . What’s a statement? 

There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: 

() => { 2 + 2 } () => { 1 + 1; 2 + 2 } 

As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: 

() => { 1 + 1; 2 + 2 } 

But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: 

(() => { 2 + 2 })() _//=> undefined_ 

(() => { 1 + 1; 2 + 2 })() _//=> undefined_ 

(() => { 1 + 1; 2 + 2 })() _//=> undefined_ 

As you can see, a block with one expression does not behave like an expression, and a block with more than one expression does not behave like an expression constructed with the comma operator: 

> 21You can also separate statements with line breaks. Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. This feature was originally created as a kind of helpful error-correction. Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-af806fb1-00048))_
- 14 

The first sip: Basic Functions 

(() => 2 + 2)() _//=> 4_ (() => { 2 + 2 })() _//=> undefined_ (() => (1 + 1, 2 + 2))() _//=> 4_ (() => { 1 + 1; 2 + 2 })() _//=> undefined_ 

So how do we get a function that evaluates a block to return a value when applied? With the return keyword and any expression: 

(() => { **return** 0 })() _//=> 0_ (() => { **return** 1 })() _//=> 1_ (() => { **return** 'Hello ' + 'World' })() _// 'Hello World'_ 

The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example: 

(() => { 1 + 1; **return** 2 + 2 })() _//=> 4_ 

And also: 

(() => { **return** 1 + 1; 2 + 2 })() _//=> 2_ 

The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression: _(javascriptallonge.pdf (source-range-af806fb1-00049))_
- The first sip: Basic Functions 

15 

- (() => **return** 0)() 

 - _//=> ERROR_ 

Statements belong inside blocks and only inside blocks. Some languages simplify this by making everything an expression, but JavaScript maintains this distinction, so when learning JavaScript we also learn about statements like function declarations, for loops, if statements, and so forth. We’ll see a few more of these later. 

## **functions that evaluate to functions** 

If an expression that evaluates to a function is, well, an expression, and if a return statement can have any expression on its right side… _Can we put an expression that evaluates to a function on the right side of a function expression?_ 

Yes: 

() => () => 0 

That’s a function! It’s a function that when applied, evaluates to a function that when applied, evaluates to 0. So we have _a function, that returns a function, that returns zero_ . Likewise: 

() => () => **true** 

That’s a function, that returns a function, that returns true: 

(() => () => **true** )()() 

- _//=> true_ 

We could, of course, do the same thing with a block if we wanted: 

() => () => { **return true** ; } 

But we generally don’t. 

Well. We’ve been very clever, but so far this all seems very abstract. Diffraction of a crystal is beautiful and interesting in its own right, but you can’t blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. So… In the next chapter, “I’d Like to Have an Argument, Please,” we’ll see how to make functions practical. _(javascriptallonge.pdf (source-range-af806fb1-00050))_
- Right now, we only know about one such expression: () => 0, so let’s use it. _(javascriptallonge.pdf (source-range-af806fb1-00043))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-af806fb1-00044))_
- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-af806fb1-00046))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-af806fb1-00046))_
- For example, you can’t use one as the expression in a simple function, because it isn’t an expression: _(javascriptallonge.pdf (source-range-af806fb1-00049))_
