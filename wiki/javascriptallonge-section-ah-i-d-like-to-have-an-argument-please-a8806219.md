---
page_id: javascriptallonge-section-ah-i-d-like-to-have-an-argument-please-a8806219
page_kind: source
summary: Ah. I'd Like to Have an Argument, Please.: 62 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-ah-i-d-like-to-have-an-argument-please-a8806219@7570a65b6fa5d27cd7a33456c9a4274d
---

# Ah. I'd Like to Have an Argument, Please.

From [[javascriptallonge]].

## Statements

- We haven’t even said what an argument _is_ , only that our functions don’t have any. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- Up to now, we’ve looked at functions without arguments. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- We haven’t even said what an argument _is_ , only that our functions don’t have any. _(javascriptallonge.pdf (source-range-83ecb080-00391))_
- So you know what they are, and I know that you know what they are, but please be patient with the explanation! _(javascriptallonge.pdf (source-range-83ecb080-00392))_
- Most programmers are perfectly familiar with arguments (often called “parameters”). _(javascriptallonge.pdf (source-range-83ecb080-00392))_
- This function has one argument, room, and an empty body. _(javascriptallonge.pdf (source-range-83ecb080-00395))_
- I’m sure you are perfectly comfortable with the idea that this function has two arguments, room, and board. _(javascriptallonge.pdf (source-range-83ecb080-00397))_
- I read that aloud as “When applied to a value representing the diameter, this function _returns_ the diameter times 3.14159265.” _(javascriptallonge.pdf (source-range-83ecb080-00399))_
- To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this: _(javascriptallonge.pdf (source-range-83ecb080-00400))_
- You won’t be surprised to see how to write and apply a function to two arguments: _(javascriptallonge.pdf (source-range-83ecb080-00403))_
- How arguments are used in a body’s expression is probably perfectly obvious to you from the examples, especially if you’ve used any programming language (except for the dialect of BASIC–which I recall from my secondary school–that didn’t allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-83ecb080-00411))_
- How arguments are used in a body’s expression is probably perfectly obvious to you from the examples, especially if you’ve used any programming language (except for the dialect of BASIC–which I recall from my secondary school–that didn’t allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-83ecb080-00411))_
- One of the important possible statements is a return statement. _(javascriptallonge.pdf (source-range-83ecb080-00413))_
- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-83ecb080-00420))_
- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-83ecb080-00420))_
- We’ll see below that while JavaScript always calls by value, the notion of a “value” has additional subtlety. _(javascriptallonge.pdf (source-range-83ecb080-00427))_
- But before we do, let’s look at variables. _(javascriptallonge.pdf (source-range-83ecb080-00427))_
- But before we do, let’s look at variables. _(javascriptallonge.pdf (source-range-83ecb080-00427))_
- Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. _(javascriptallonge.pdf (source-range-83ecb080-00429))_
- Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics. _(javascriptallonge.pdf (source-range-83ecb080-00431))_
- But there’s another reason for learning the word _antidisestablishmentarianism_ : We might learn how prefixes and postfixes work in English grammar. _(javascriptallonge.pdf (source-range-83ecb080-00432))_
- It has a certain important meaning in its own right, and it’s also an excellent excuse to learn about functions that make functions, environments, variables, and more. _(javascriptallonge.pdf (source-range-83ecb080-00432))_
- In order to talk about how this works, we should agree on a few terms (you may already know them, but let’s check-in together and “synchronize our dictionaries”). _(javascriptallonge.pdf (source-range-83ecb080-00433))_
- The second x, the one in => x, is not an argument, _it’s an expression referring to a variable_ . _(javascriptallonge.pdf (source-range-83ecb080-00433))_
- The first x, the one in (x) => ..., is an _argument_ . _(javascriptallonge.pdf (source-range-83ecb080-00433))_
- The x in the expression that we call a “variable” is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- Every time a function is invoked (“invoked” means “applied to zero or more arguments”), a new _environment_ is created. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- An environment is a (possibly empty) dictionary that maps variables to values by name. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- Every time a function is invoked (“invoked” means “applied to zero or more arguments”), a new _environment_ is created. _(javascriptallonge.pdf (source-range-83ecb080-00434))_
- > 24 We said that you can’t apply a function to an expression. _(javascriptallonge.pdf (source-range-83ecb080-00435))_
- This has interesting applications, and they will be explored much more thoroughly in Functions That Are Applied to Functions. _(javascriptallonge.pdf (source-range-83ecb080-00435))_
- Well for arguments, that is very simple. _(javascriptallonge.pdf (source-range-83ecb080-00438))_
- When you apply the function to the arguments, an entry is placed in the dictionary for each argument. _(javascriptallonge.pdf (source-range-83ecb080-00438))_
- The value ‘2’ is bound to the name ‘x’ in the environment. _(javascriptallonge.pdf (source-range-83ecb080-00447))_
- The expression ‘x’ (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-83ecb080-00448))_
- The expression ‘x’ (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-83ecb080-00448))_
- The value of a variable when evaluated in an environment is the value bound to the variable’s name in that environment, which is ‘2’ _(javascriptallonge.pdf (source-range-83ecb080-00449))_
- meaning, that the environment is a dictionary, and that the value 2 is bound to the name x, and that there might be other stuff in that dictionary we aren’t discussing right now. _(javascriptallonge.pdf (source-range-83ecb080-00451))_
- Now it is time to take another look at the distinction between value and reference types. _(javascriptallonge.pdf (source-range-83ecb080-00453))_
- At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. _(javascriptallonge.pdf (source-range-83ecb080-00453))_
- Earlier, we distinguished JavaScript’s _value types_ from its _reference types_ . _(javascriptallonge.pdf (source-range-83ecb080-00453))_
- There is a property that JavaScript strictly maintains: When a value–any value–is passed as an argument to a function, the value bound in the function’s environment must be identical to the original. _(javascriptallonge.pdf (source-range-83ecb080-00454))_
- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- JavaScript does not place copies of reference values in any environment. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. _(javascriptallonge.pdf (source-range-83ecb080-00461))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-83ecb080-00461))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. _(javascriptallonge.pdf (source-range-83ecb080-00461))_
- > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . _(javascriptallonge.pdf (source-range-83ecb080-00465))_
- > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . _(javascriptallonge.pdf (source-range-83ecb080-00465))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00397))_

> I’m sure you are perfectly comfortable with the idea that this function has two arguments, room, and board. What does one do with the arguments? Use them in the body, of course. What do you think this is?

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00398))_

> (diameter) => diameter * 3.14159265

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00400))_

> Remember that to apply a function with no arguments, we wrote (() => {})(). To apply a function with an argument (or arguments), we put the argument (or arguments) within the parentheses, like this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00401))_

> ((diameter) => diameter * 3.14159265)(2)

### Technical atom 3

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00407))_

> ((room, board) => room + board)(800, 150)

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00424))_

> So when you write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00425))_

> - ((diameter) => diameter * 3.14159265)(1 + 1) _//=> 6.2831853_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00424))_

> So when you write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00426))_

> What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2. Then our circumference function was applied to 2.[24]

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00429))_

> Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. And we’re going to work our way up from (diameter) => diameter * 3.14159265 to functions like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00430))_

> - (x) => (y) => x

### Technical atom 7

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00438))_

> How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00439))_

> ((x) => x)(2) _//=> 2_

### Technical atom 8

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00440))_

> What happens is this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00443))_

> 3. One sub-expression, (x) => x evaluates to a function.

### Technical atom 9

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00461))_

> Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00459))_

> So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

### Technical atom 10

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00462))_

> And with that, we’re ready to look at _closures_ . When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00464))_

> - ((ref1, ref2) => ref1 === ref2)(value, value)
