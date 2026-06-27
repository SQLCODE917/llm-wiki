---
page_id: javascriptallonge-argument-please
page_kind: concept
summary: Ah. I'd Like to Have an Argument, Please.: 42 statement(s) and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-argument-please@9aac372202289459f6d84bcb97493a65
---

# Ah. I'd Like to Have an Argument, Please.

What [[javascriptallonge]] covers about ah. i'd like to have an argument, please.:

## Statements

- Every time a function is invoked (“invoked” means “applied to zero or more arguments”), a new _environment_ is created. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- When you apply the function to the arguments, an entry is placed in the dictionary for each argument. _(javascriptallonge.pdf (source-range-83ecb080-00438))_
- We haven’t even said what an argument _is_ , only that our functions don’t have any. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- How arguments are used in a body’s expression is probably perfectly obvious to you from the examples, especially if you’ve used any programming language (except for the dialect of BASIC–which I recall from my secondary school–that didn’t allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-83ecb080-00411))_
- Well for arguments, that is very simple. _(javascriptallonge.pdf (source-range-83ecb080-00438))_
- > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . _(javascriptallonge.pdf (source-range-83ecb080-00465))_
- Up to now, we’ve looked at functions without arguments. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- So you know what they are, and I know that you know what they are, but please be patient with the explanation! _(javascriptallonge.pdf (source-range-83ecb080-00392))_
- Most programmers are perfectly familiar with arguments (often called “parameters”). _(javascriptallonge.pdf (source-range-83ecb080-00392))_
- This function has one argument, room, and an empty body. _(javascriptallonge.pdf (source-range-83ecb080-00395))_
- I’m sure you are perfectly comfortable with the idea that this function has two arguments, room, and board. _(javascriptallonge.pdf (source-range-83ecb080-00397))_
- You won’t be surprised to see how to write and apply a function to two arguments: _(javascriptallonge.pdf (source-range-83ecb080-00403))_
- Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. _(javascriptallonge.pdf (source-range-83ecb080-00429))_
- The second x, the one in => x, is not an argument, _it’s an expression referring to a variable_ . _(javascriptallonge.pdf (source-range-83ecb080-00433))_

## Technical atoms

> Context: I’m sure you are perfectly comfortable with the idea that this function has two arguments, room, and board. What does one do with the arguments? Use them in the body, of course. What do you think this is?
_(context: javascriptallonge.pdf (source-range-83ecb080-00397))_

> (diameter) => diameter * 3.14159265
_(source: javascriptallonge.pdf (source-range-83ecb080-00398))_

> Context: Remember that to apply a function with no arguments, we wrote (() => {})(). To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this:
_(context: javascriptallonge.pdf (source-range-83ecb080-00400))_

> ((diameter) => diameter * 3.14159265)(2)
_(source: javascriptallonge.pdf (source-range-83ecb080-00401))_

> ((room, board) => room + board)(800, 150)
_(source: javascriptallonge.pdf (source-range-83ecb080-00407))_

> Context: So when you write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00424))_

> - ((diameter) => diameter * 3.14159265)(1 + 1) _//=> 6.2831853_
_(source: javascriptallonge.pdf (source-range-83ecb080-00425))_

> Context: So when you write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00424))_

> What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2. Then our circumference function was applied to 2.[24]
_(source: javascriptallonge.pdf (source-range-83ecb080-00426))_

> Context: Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. And we’re going to work our way up from (diameter) => diameter * 3.14159265 to functions like:
_(context: javascriptallonge.pdf (source-range-83ecb080-00429))_

> - (x) => (y) => x
_(source: javascriptallonge.pdf (source-range-83ecb080-00430))_


## Source

- [[javascriptallonge]]
