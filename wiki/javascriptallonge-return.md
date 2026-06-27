---
page_id: javascriptallonge-return
page_kind: concept
summary: Return: 15 statement(s) and 15 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-return@4b0f1068c9c1dd088aa04e247a722dee
---

# Return

What [[javascriptallonge]] covers about return:

## Statements

_Showing 14 of 15 statements selected for this topic._

- first returns the first element of an iterable (if it has one), and rest returns an iterable that iterates over all but the first element of an iterable. _(javascriptallonge.pdf (source-range-83ecb080-02501))_
- It works, but as we’ve just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object:[93] _(javascriptallonge.pdf (source-range-83ecb080-02689))_
- We know that (() => 0)() returns 0, and this is unsurprising. _(javascriptallonge.pdf (source-range-83ecb080-00283))_
- It returns the result of evaluating a block that has no statements. _(javascriptallonge.pdf (source-range-83ecb080-00314))_
- We said that the function returns the result of evaluating a _block_ , and we said that a block is a (possibly empty) list of JavaScript _statements_ separated by semicolons.[21] _(javascriptallonge.pdf (source-range-83ecb080-00346))_
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-83ecb080-01123))_
- And to return to our first example, our version of length can be written as a fold: _(javascriptallonge.pdf (source-range-83ecb080-01389))_
- The arrayIterator function takes an array and returns a function we can call repeatedly to obtain the elements of the array. _(javascriptallonge.pdf (source-range-83ecb080-01976))_
- In both cases, we take two parameters, and return the form of the data. _(javascriptallonge.pdf (source-range-83ecb080-02095))_
- Invoking only("you") returns an iterator that we can call with .next(), and it yields "you". _(javascriptallonge.pdf (source-range-83ecb080-02604))_
- The body of our generator runs until it returns, ends, or encounters the next yield statement. _(javascriptallonge.pdf (source-range-83ecb080-02638))_
- We’ve writing a function that returns an iterator, but we used a generator to do it. _(javascriptallonge.pdf (source-range-83ecb080-02681))_

## Technical atoms

_Showing 6 of 15 technical atoms selected for this topic._

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00285))_

> Well, the last one’s a doozy, but still, the general idea is this: We can make a function that returns a value by putting the value to the right of the arrow.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00287))_

> (() => 1 + 1)() _//=> 2_ (() => "Hello, " + "JavaScript")() _//=> "Hello, JavaScript"_ (() => **Infinity** * **Infinity** )() _//=> Infinity_

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00291))_

> Yes we can! Functions can return the value of evaluating another function.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00292))_

> When dealing with expressions that have a lot of the same characters (like parentheses), you may find it helpful to format the code to make things stand out.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00349, source-range-83ecb080-00351))_

> There are many kinds of JavaScript statements, but the first kind is one we’ve already met. An expression is a JavaScript statement. Although they aren’t very practical, these are valid JavaScript functions, and they return undefined when applied: As we saw with commas above, we can rearrange these functions onto multiple lines when we feel its more readable that way:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00350))_

> () => { 2 + 2 } () => { 1 + 1; 2 + 2 }

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00364))_

> The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00362))_

> So how do we get a function that evaluates a block to return a value when applied?

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00364))_

> The return keyword creates a _return statement_ that immediately terminates the function application and returns the result of evaluating its expression. For example:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00365))_

> (() => { 1 + 1; **return** 2 + 2 })() _//=> 4_

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00366, source-range-83ecb080-00368))_

> And also: The return statement is the first statement we’ve seen, and it behaves differently than an expression. For example, you can’t use one as the expression in a simple function, because it isn’t an expression:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00367))_

> (() => { **return** 1 + 1; 2 + 2 })() _//=> 2_


## Source

- [[javascriptallonge]]
