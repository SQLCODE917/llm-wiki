---
page_id: javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-variables-and-bindings-4f74d027
page_kind: source
page_family: section-reference
summary: And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings: 22 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-variables-and-bindings-4f74d027@a6cd5dcb53d17b73aef1024d16f8bcce
---

# And also: / Ah. I'd Like to Have an Argument, Please. 22 / variables and bindings

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-and-also-ah-i-d-like-to-have-an-argument-please-22-f00edd2f]] - broader source section: And also: / Ah. I'd Like to Have an Argument, Please. 22

## Statements

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
