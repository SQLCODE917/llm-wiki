---
page_id: javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-f00edd2f
page_kind: source
page_family: section-reference
summary: And also: / Ah. I'd Like to Have an Argument, Please. 22: 64 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-f00edd2f@6476459164341fcfd68cd344f23bebfb
---

# And also: / Ah. I'd Like to Have an Argument, Please. 22

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-3f50274e]] - broader source section: And also:
- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-a-quick-summary-of-functions-and-bodies-7798619d]] - narrower source section: And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies
- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-sharing-96a55cff]] - narrower source section: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing
- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-call-by-value-ae929990]] - narrower source section: And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value
- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-variables-and-bindings-4f74d027]] - narrower source section: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

## Statements

- Up to now, we've looked at functions without arguments. We haven't even said what an argument is , only that our functions don't have any. _(javascriptallonge.pdf (source-range-7239e085-00270))_
- Most programmers are perfectly familiar with arguments (often called 'parameters'). Secondary school mathematics discusses this. So you know what they are, and I know that you know what they are, but please be patient with the explanation! _(javascriptallonge.pdf (source-range-7239e085-00271))_
- This function has one argument, room , and an empty body. Here's a function with two arguments and an empty body: _(javascriptallonge.pdf (source-range-7239e085-00274))_
- I'm sure you are perfectly comfortable with the idea that this function has two arguments, room , and board . What does one do with the arguments? Use them in the body, of course. What do you think this is? _(javascriptallonge.pdf (source-range-7239e085-00276))_
- It's a function for calculating the circumference of a circle given the diameter. I read that aloud as 'When applied to a value representing the diameter, this function returns the diameter times 3.14159265.' _(javascriptallonge.pdf (source-range-7239e085-00278))_
- You won't be surprised to see how to write and apply a function to two arguments: _(javascriptallonge.pdf (source-range-7239e085-00281))_
- We haven't even said what an argument is , only that our functions don't have any. _(javascriptallonge.pdf (source-range-7239e085-00270))_

## Statements by subsection

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / a quick summary of functions and bodies

- How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-7239e085-00286))_
- One of the important possible statements is a return statement. A return statement accepts any valid JavaScript expression. _(javascriptallonge.pdf (source-range-7239e085-00288))_
- How arguments are used in a body's expression is probably perfectly obvious to you from the examples, especially if you've used any programming language (except for the dialect of BASIC-which I recall from my secondary school-that didn't allow parameters when you called a procedure). _(javascriptallonge.pdf (source-range-7239e085-00286))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by value

- Like most contemporary programming languages, JavaScript uses the 'call by value' evaluation strategy 23 . That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-7239e085-00291))_
- What happened internally is that the expression 1 + 1 was evaluated first, resulting in 2 . Then our circumference function was applied to 2 . 24 _(javascriptallonge.pdf (source-range-7239e085-00295))_
- We'll see below that while JavaScript always calls by value, the notion of a 'value' has additional subtlety. But before we do, let's look at variables. _(javascriptallonge.pdf (source-range-7239e085-00296))_
- That means that when you write some code that appears to apply a function to an expression or expressions, JavaScript evaluates all of those expressions and applies the functions to the resulting value(s). _(javascriptallonge.pdf (source-range-7239e085-00291))_
- Then our circumference function was applied to 2 . _(javascriptallonge.pdf (source-range-7239e085-00295))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

- Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. And we're going to work our way up from (diameter) => diameter * 3.14159265 to functions like: (x) => (y) => x just looks crazy, as if we are learning English as a second language and the teacher promises us that soon we will be using words like antidisestablishmentarianism . Besides a desire to use long words to sound impressive, this is not going to seem attractive until we find ourselves wanting to discuss the role of the Church of England in 19th century British politics. _(javascriptallonge.pdf (source-range-7239e085-00298, source-range-7239e085-00300))_
- But there's another reason for learning the word antidisestablishmentarianism : We might learn how prefixes and postfixes work in English grammar. It's the same thing with (x) => (y) => x . It has a certain important meaning in its own right, and it's also an excellent excuse to learn about functions that make functions, environments, variables, and more. _(javascriptallonge.pdf (source-range-7239e085-00301))_
- In order to talk about how this works, we should agree on a few terms (you may already know them, but let's check-in together and 'synchronize our dictionaries'). The first x , the one in (x) => ... , is an argument . The y in function (y) ... is another argument. The second x , the one in => x , is not an argument, it's an expression referring to a variable . Arguments and variables work the same way whether we're talking about (x) => (y) => x or just plain (x) => x . _(javascriptallonge.pdf (source-range-7239e085-00302))_
- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. An environment is a (possibly empty) dictionary that maps variables to values by name. The x in the expression that we call a 'variable' is itself an expression that is evaluated by looking up the value in the environment. _(javascriptallonge.pdf (source-range-7239e085-00303))_
- 24 We said that you can't apply a function to an expression. You can apply a function to one or more functions. Functions are values! This has interesting applications, and they will be explored much more thoroughly in Functions That Are Applied to Functions. _(javascriptallonge.pdf (source-range-7239e085-00304))_
- How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write: _(javascriptallonge.pdf (source-range-7239e085-00305))_
- The value '2' is bound to the name 'x' in the environment. _(javascriptallonge.pdf (source-range-7239e085-00314))_
- The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-7239e085-00315))_
- The value of a variable when evaluated in an environment is the value bound to the variable's name in that environment, which is '2' _(javascriptallonge.pdf (source-range-7239e085-00316))_
- When we talk about environments, we'll use an unsurprising syntax 25 for showing their bindings: {x: 2, ...} . meaning, that the environment is a dictionary, and that the value 2 is bound to the name x , and that there might be other stuff in that dictionary we aren't discussing right now. _(javascriptallonge.pdf (source-range-7239e085-00318))_
- Every time a function is invoked ('invoked' means 'applied to zero or more arguments'), a new environment is created. _(javascriptallonge.pdf (source-range-7239e085-00303))_
- - The expression 'x' (the right side of the function) is evaluated within the environment we just created. _(javascriptallonge.pdf (source-range-7239e085-00315))_

### And also: / Ah. I'd Like to Have an Argument, Please. 22 / call by sharing

- Earlier, we distinguished JavaScript's value types from its reference types . At that time, we looked at how JavaScript distinguishes objects that are identical from objects that are not. Now it is time to take another look at the distinction between value and reference types. _(javascriptallonge.pdf (source-range-7239e085-00320))_
- There is a property that JavaScript strictly maintains: When a value-any value-is passed as an argument to a function, the value bound in the function's environment must be identical to the original. _(javascriptallonge.pdf (source-range-7239e085-00321))_
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. Now we can elaborate: When JavaScript binds a value-type to a name, it makes a copy of the value and places the copy in the environment. As you recall, value types like strings and numbers are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes. _(javascriptallonge.pdf (source-range-7239e085-00322))_
- Whatabout reference types? JavaScript does not place copies of reference values in any environment. JavaScript places references to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-7239e085-00324))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement 'call by sharing' semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types. _(javascriptallonge.pdf (source-range-7239e085-00325))_
- 26 Unless the argument is NaN , which isn't equal to anything, including itself . NaN in JavaScript behaves a lot like NULL in SQL. _(javascriptallonge.pdf (source-range-7239e085-00328))_
- We said that JavaScript binds names to values, but we didn't say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-7239e085-00322))_
- Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement 'call by sharing' semantics. _(javascriptallonge.pdf (source-range-7239e085-00325))_
- 26 Unless the argument is NaN , which isn't equal to anything, including itself . _(javascriptallonge.pdf (source-range-7239e085-00328))_
