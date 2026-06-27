---
page_id: javascriptallonge-section-variables-and-bindings-62ca1c8e
page_kind: source
summary: **variables and bindings**: 23 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-variables-and-bindings-62ca1c8e@14c1200d69263cf70747d6a4ebf4ecc2
---

# **variables and bindings**

From [[javascriptallonge]].

## Statements

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

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00429))_

> Right now everything looks simple and straightforward, and we can move on to talk about arguments in more detail. And we’re going to work our way up from (diameter) => diameter * 3.14159265 to functions like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00430))_

> - (x) => (y) => x

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00438))_

> How does the value get put in the environment? Well for arguments, that is very simple. When you apply the function to the arguments, an entry is placed in the dictionary for each argument. So when we write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00439))_

> ((x) => x)(2) _//=> 2_

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00440))_

> What happens is this:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00443))_

> 3. One sub-expression, (x) => x evaluates to a function.
