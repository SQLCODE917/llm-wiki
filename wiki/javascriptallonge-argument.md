---
page_id: javascriptallonge-argument
page_kind: concept
summary: Argument: 13 statement(s) and 21 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-argument@88a961a13d03d982c08334f484e79b58
---

# Argument

What [[javascriptallonge]] covers about argument:

## Statements

- This works just fine, because arguments[0] refers to the 3 we passed to the function row. _(javascriptallonge.pdf (source-range-83ecb080-00890))_
- When you apply the function to the arguments, an entry is placed in the dictionary for each argument. _(javascriptallonge.pdf (source-range-83ecb080-00438))_
- arguments always contains all of the arguments passed to a function, regardless of how many are declared. _(javascriptallonge.pdf (source-range-83ecb080-00870))_
- It always returns false if its argument is truthy, and true is its argument is not truthy: _(javascriptallonge.pdf (source-range-83ecb080-01123))_
- We haven’t even said what an argument _is_ , only that our functions don’t have any. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- How arguments are used in a body’s expression is probably perfectly obvious to you from the examples, especially if you’ve used any programming language (except for the dialect of BASIC–which I recall from my secondary school–that didn’t allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-83ecb080-00411))_
- Well for arguments, that is very simple. _(javascriptallonge.pdf (source-range-83ecb080-00438))_
- > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . _(javascriptallonge.pdf (source-range-83ecb080-00465))_
- Generally speaking, a function that either takes functions as arguments, or returns a function, or both, is referred to as a “higher-order” function. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- mapWith takes any function as an argument and returns a partially applied map function. _(javascriptallonge.pdf (source-range-83ecb080-00845))_
- Gathering arguments for functions is one of the ways JavaScript can _destructure_ arrays. _(javascriptallonge.pdf (source-range-83ecb080-01074))_
- In Arrays and Destructuring Arguments, we worked with the basic idea that putting an array together with a literal array expression was the reverse or opposite of taking it apart with a destructuring assignment. _(javascriptallonge.pdf (source-range-83ecb080-01298))_
- A default argument is concise and readable. _(javascriptallonge.pdf (source-range-83ecb080-01491))_

## Technical atoms

> Context: I’m sure you are perfectly comfortable with the idea that this function has two arguments, room, and board. What does one do with the arguments? Use them in the body, of course. What do you think this is?
_(context: javascriptallonge.pdf (source-range-83ecb080-00397))_

> (diameter) => diameter * 3.14159265
_(source: javascriptallonge.pdf (source-range-83ecb080-00398))_

> Context: Remember that to apply a function with no arguments, we wrote (() => {})(). To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00400))_

> ((diameter) => diameter * 3.14159265)(2)
_(source: javascriptallonge.pdf (source-range-83ecb080-00401))_

> Context: Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. And we’re going to work our way up from (diameter) => diameter * 3.14159265 to functions like:
_(context: javascriptallonge.pdf (source-range-83ecb080-00429))_

> - (x) => (y) => x
_(source: javascriptallonge.pdf (source-range-83ecb080-00430))_

> Context: How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00438))_

> ((x) => x)(2) _//=> 2_
_(source: javascriptallonge.pdf (source-range-83ecb080-00439))_

> Context: Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types.
_(context: javascriptallonge.pdf (source-range-83ecb080-00461))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.
_(source: javascriptallonge.pdf (source-range-83ecb080-00459))_

> Context: And with that, we’re ready to look at _closures_ . When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to:
_(context: javascriptallonge.pdf (source-range-83ecb080-00462))_

> - ((ref1, ref2) => ref1 === ref2)(value, value)
_(source: javascriptallonge.pdf (source-range-83ecb080-00464))_


## Source

- [[javascriptallonge]]
