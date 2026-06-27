---
page_id: javascriptallonge-section-as-little-as-possible-about-functions-but-no-less-dc8f76dc
page_kind: source
summary: As Little As Possible About Functions, But No Less: 91 source-backed entries and 21 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-as-little-as-possible-about-functions-but-no-less-dc8f76dc@502da78a6440cc7fb95a6d614900a06e
---

# As Little As Possible About Functions, But No Less

From [[javascriptallonge]].

## Statements

- Functions represent computations to be performed. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- Like numbers, strings, and arrays, they have a representation. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- In JavaScript, functions are values, but they are also much more than simple numbers, strings, or even complex data structures like trees or maps. _(javascriptallonge.pdf (source-range-83ecb080-00258))_
- This is a function that is applied to no values and returns 0. _(javascriptallonge.pdf (source-range-83ecb080-00260))_
- [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. _(javascriptallonge.pdf (source-range-83ecb080-00262))_
- But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. _(javascriptallonge.pdf (source-range-83ecb080-00266))_
- Reference types do not. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- You recall that we have two types of values with respect to identity: Value types and reference types. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- Value types share the same identity if they have the same contents. _(javascriptallonge.pdf (source-range-83ecb080-00268))_
- “Function” is a reference type. _(javascriptallonge.pdf (source-range-83ecb080-00272))_
- The way we use functions is to _apply_ them to zero or more values called _arguments_ . _(javascriptallonge.pdf (source-range-83ecb080-00274))_
- Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. _(javascriptallonge.pdf (source-range-83ecb080-00275))_
- Right now, we only know about one such expression: () => 0, so let’s use it. _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- We’ll put it in parentheses[17] to keep the parser happy, like we did above: (() => 0). _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- Since we aren’t giving it any arguments, we’ll simply write () after the expression. _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- Right now, we only know about one such expression: () => 0, so let’s use it. _(javascriptallonge.pdf (source-range-83ecb080-00277))_
- > 17If you’re used to other programming languages, you’ve probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. _(javascriptallonge.pdf (source-range-83ecb080-00279))_
- We know that (() => 0)() returns 0, and this is unsurprising. _(javascriptallonge.pdf (source-range-83ecb080-00283))_
- Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00285))_
- Values like 0 are expressions, as are things like 40 + 2. _(javascriptallonge.pdf (source-range-83ecb080-00286))_
- In the prelude, we looked at expressions. _(javascriptallonge.pdf (source-range-83ecb080-00286))_
- We can put any expression to the right of the arrow. _(javascriptallonge.pdf (source-range-83ecb080-00288))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00288))_
- For example, (() => 0)() is an expression. _(javascriptallonge.pdf (source-range-83ecb080-00288))_
- Functions can return the value of evaluating another function. _(javascriptallonge.pdf (source-range-83ecb080-00291))_
- The comma operator in JavaScript is interesting. _(javascriptallonge.pdf (source-range-83ecb080-00298))_
- In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00303))_
- There’s another thing we can put to the right of an arrow, a _block_ . _(javascriptallonge.pdf (source-range-83ecb080-00311))_
- It returns the result of evaluating a block that has no statements. _(javascriptallonge.pdf (source-range-83ecb080-00314))_
- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-83ecb080-00319))_
- It will crop up again. _(javascriptallonge.pdf (source-range-83ecb080-00319))_
- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-83ecb080-00319))_
- Like numbers, booleans and strings, JavaScript can print out the value undefined. _(javascriptallonge.pdf (source-range-83ecb080-00322))_
- No matter how you evaluate undefined, you get an identical value back. _(javascriptallonge.pdf (source-range-83ecb080-00325))_
- > 18Sometimes, you will find JavaScript that has statements that are separated by newlines without semi-colons. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- This works because JavaScript has a feature that can infer where the semi-colons should be most of the time. _(javascriptallonge.pdf (source-range-83ecb080-00326))_
- You might think that undefined in JavaScript is equivalent to NULL in SQL. _(javascriptallonge.pdf (source-range-83ecb080-00329))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can’t be equal. _(javascriptallonge.pdf (source-range-83ecb080-00329))_
- In JavaScript, every undefined is identical to every other undefined. _(javascriptallonge.pdf (source-range-83ecb080-00329))_
- In SQL, two things that are NULL are not equal to nor share the same identity, because two unknowns can’t be equal. _(javascriptallonge.pdf (source-range-83ecb080-00329))_
- We’ve seen that JavaScript represents an undefined value by typing undefined, and we’ve generated undefined values in two ways: _(javascriptallonge.pdf (source-range-83ecb080-00331))_
- void is an operator that takes any value and evaluates to undefined, always. _(javascriptallonge.pdf (source-range-83ecb080-00336))_
- So, when we deliberately want an undefined value, should we use the first, second, or third form?[19] The answer is, use void. _(javascriptallonge.pdf (source-range-83ecb080-00336))_
- The first form works but it’s cumbersome. _(javascriptallonge.pdf (source-range-83ecb080-00337))_
- The second form works most of the time, but it is possible to break it by reassigning undefined to a different value, something we’ll discuss in Reassignment and Mutation. _(javascriptallonge.pdf (source-range-83ecb080-00337))_
- > 19Experienced JavaScript programmers are aware that there’s a fourth way, using a function argument. _(javascriptallonge.pdf (source-range-83ecb080-00340))_
- This was actually the preferred mechanism until void became commonplace. _(javascriptallonge.pdf (source-range-83ecb080-00340))_
- > 20As an exercise for the reader, we suggest you ask your friendly neighbourhood programming language designer or human factors subjectmatter expert to explain why a keyword called void is used to generate an undefined value, instead of calling them both void or both undefined. _(javascriptallonge.pdf (source-range-83ecb080-00341))_
- We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] _(javascriptallonge.pdf (source-range-83ecb080-00346))_
- We haven’t discussed these _statements_ . _(javascriptallonge.pdf (source-range-83ecb080-00348))_
- An expression is a JavaScript statement. _(javascriptallonge.pdf (source-range-83ecb080-00349))_
- There are many kinds of JavaScript statements, but the first kind is one we’ve already met. _(javascriptallonge.pdf (source-range-83ecb080-00349))_
- Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: _(javascriptallonge.pdf (source-range-83ecb080-00349))_
- As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way: _(javascriptallonge.pdf (source-range-83ecb080-00351))_
- But no matter how we arrange them, a block with one or more expressions still evaluates to undefined: _(javascriptallonge.pdf (source-range-83ecb080-00353))_
- Some programmers argue that since it’s part of the language’s definition, it’s fair game to write code that exploits it, so they deliberately omit any semicolon that JavaScript will insert for them. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- This feature was originally created as a kind of helpful error-correction. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- > 21You can also separate statements with line breaks. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Basically, there’s a step where JavaScript looks at your code and follows some rules to guess where you meant to put semicolons in should you leave them out. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Readers who follow internet flame-fests may be aware of something called automatic semicolon insertion. _(javascriptallonge.pdf (source-range-83ecb080-00358))_
- Statements belong inside blocks and only inside blocks. _(javascriptallonge.pdf (source-range-83ecb080-00373))_
- So we have _a function, that returns a function, that returns zero_ . _(javascriptallonge.pdf (source-range-83ecb080-00378))_
- It’s a function that when applied, evaluates to a function that when applied, evaluates to 0. _(javascriptallonge.pdf (source-range-83ecb080-00378))_
- So… In the next chapter, “I’d Like to Have an Argument, Please,” we’ll see how to make functions practical. _(javascriptallonge.pdf (source-range-83ecb080-00386))_
- We’ve been very clever, but so far this all seems very abstract. _(javascriptallonge.pdf (source-range-83ecb080-00386))_
- Diffraction of a crystal is beautiful and interesting in its own right, but you can’t blame us for wanting to be shown a practical use for it, like being able to determine the composition of a star millions of light years away. _(javascriptallonge.pdf (source-range-83ecb080-00386))_

## Technical atoms

> Context: This is a function that is applied to no values and returns 0. Let’s verify that our function is a value like all others:
_(context: javascriptallonge.pdf (source-range-83ecb080-00260))_

> If you try the same thing in a browser, you may see something else.
_(source: javascriptallonge.pdf (source-range-83ecb080-00262))_

> Context: What!? Why didn’t it type back () => 0 for us? This _seems_ to break our rule that if an expression is also a value, JavaScript will give the same value back to us. What’s going on? The simplest and easiest answer is that although the JavaScript interpreter does indeed return that value, displaying it on the screen is a slightly different matter. [Function] is a choice made by the people who wrote Node.js, the JavaScript environment that hosts the JavaScript REPL. If you try the same thing in a 
_(context: javascriptallonge.pdf (source-range-83ecb080-00262))_

> > 16 The simplest possible function is () => {}, we’ll see that later.
_(source: javascriptallonge.pdf (source-range-83ecb080-00263))_

> Context: Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.
_(context: javascriptallonge.pdf (source-range-83ecb080-00285))_

> (() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_
_(source: javascriptallonge.pdf (source-range-83ecb080-00287))_

> Context: Yes we can! Functions can return the value of evaluating another function.
_(context: javascriptallonge.pdf (source-range-83ecb080-00291))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.
_(source: javascriptallonge.pdf (source-range-83ecb080-00292))_

> Context: The comma operator in JavaScript is interesting. It takes two arguments, evaluates them both, and itself evaluates to the value of the right-hand argument. In other words:
_(context: javascriptallonge.pdf (source-range-83ecb080-00298))_

> (1 + 1, 2 + 2) _//=> 4_
_(source: javascriptallonge.pdf (source-range-83ecb080-00300))_

> Context: We can use commas with functions to create functions that evaluate multiple expressions:
_(context: javascriptallonge.pdf (source-range-83ecb080-00301))_

> (() => (1 + 1, 2 + 2))() _//=> 4_
_(source: javascriptallonge.pdf (source-range-83ecb080-00302))_

> Context: We can use commas with functions to create functions that evaluate multiple expressions:
_(context: javascriptallonge.pdf (source-range-83ecb080-00301))_

> This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later.
_(source: javascriptallonge.pdf (source-range-83ecb080-00303))_

> Context: This is useful when trying to do things that might involve _side-effects_ , but we’ll get to that later. In most cases, JavaScript does not care whether things are separated by spaces, tabs, or line breaks. So we can also write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00303))_

> () => (1 + 1, 2 + 2)
_(source: javascriptallonge.pdf (source-range-83ecb080-00304))_

> () => ( 1 + 1, 2 + 2
_(source: javascriptallonge.pdf (source-range-83ecb080-00306))_

> Context: No matter how you evaluate undefined, you get an identical value back. undefined is a value that means “I don’t have a value.” But it’s still a value :-)
_(context: javascriptallonge.pdf (source-range-83ecb080-00325))_

> **undefined** === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-00323))_

> Context: There’s a third way, with JavaScript’s void operator. Behold: void is an operator that takes any value and evaluates to undefined, always. So, when we deliberately want an undefined value, should we use the first, second, or third form?[19] The answer is, use void. By convention, use void 0.
_(context: javascriptallonge.pdf (source-range-83ecb080-00334, source-range-83ecb080-00336))_

> **void** 0 _//=> undefined_ **void** 1 _//=> undefined_ **void** (2 + 2) _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00335))_

> Context: There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:
_(context: javascriptallonge.pdf (source-range-83ecb080-00349, source-range-83ecb080-00351))_

> () => { 2 + 2 } () => { 1 + 1; 2 + 2 }
_(source: javascriptallonge.pdf (source-range-83ecb080-00350))_

> Context: As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:
_(context: javascriptallonge.pdf (source-range-83ecb080-00351))_

> () => { 1 + 1; 2 + 2 }
_(source: javascriptallonge.pdf (source-range-83ecb080-00352))_

> Context: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:
_(context: javascriptallonge.pdf (source-range-83ecb080-00353))_

> (() => { 2 + 2 })() _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00354))_

> Context: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:
_(context: javascriptallonge.pdf (source-range-83ecb080-00353))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00355))_

> Context: But no matter how we arrange them, a block with one or more expressions still evaluates to undefined:
_(context: javascriptallonge.pdf (source-range-83ecb080-00353))_

> (() => { 1 + 1; 2 + 2 })() _//=> undefined_
_(source: javascriptallonge.pdf (source-range-83ecb080-00356))_

> Context: The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-00364))_

> So how do we get a function that evaluates a block to return a value when applied?
_(source: javascriptallonge.pdf (source-range-83ecb080-00362))_

> Context: The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-00364))_

> (() => { 1 + 1; **return** 2 + 2 })() _//=> 4_
_(source: javascriptallonge.pdf (source-range-83ecb080-00365))_

> Context: And also: The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression:
_(context: javascriptallonge.pdf (source-range-83ecb080-00366, source-range-83ecb080-00368))_

> (() => { **return** 1 + 1; 2 + 2 })() _//=> 2_
_(source: javascriptallonge.pdf (source-range-83ecb080-00367))_

> The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression:
_(source: javascriptallonge.pdf (source-range-83ecb080-00368))_

> If an expression that evaluates to a function is, well, an expression, and if a return statement can have any expression on its right side… _Can we put an expression that evaluates to a function on the right side of a function expression?_
_(source: javascriptallonge.pdf (source-range-83ecb080-00375))_
