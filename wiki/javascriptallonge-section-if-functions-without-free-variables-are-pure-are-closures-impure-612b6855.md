---
page_id: javascriptallonge-section-if-functions-without-free-variables-are-pure-are-closures-impure-612b6855
page_kind: source
summary: if functions without free variables are pure, are closures impure?: 26 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-if-functions-without-free-variables-are-pure-are-closures-impure-612b6855@7b2623a257fe00595ba305b9234b3746
---

# if functions without free variables are pure, are closures impure?

From [[javascriptallonge]].

## Statements

- The function (y) => x is interesting. It contains a free variable , x . 27 A free variable is one that is not bound within the function. Up to now, we've only seen one way to 'bind' a variable, namely by passing in an argument with the same name. Since the function (y) => x doesn't have an argument named x , the variable x isn't bound in this function, which makes it 'free.' _(javascriptallonge.pdf (source-range-8eb13d6b-00346))_
- Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without: _(javascriptallonge.pdf (source-range-8eb13d6b-00347))_
- Functions containing no free variables are called pure functions . _(javascriptallonge.pdf (source-range-8eb13d6b-00348))_
- Functions containing one or more free variables are called closures . _(javascriptallonge.pdf (source-range-8eb13d6b-00349))_
- Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we've already seen: _(javascriptallonge.pdf (source-range-8eb13d6b-00350))_
- The first function doesn't have any variables, therefore doesn't have any free variables. The second doesn't have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ... , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... . _(javascriptallonge.pdf (source-range-8eb13d6b-00351))_
- From this, we learn something: A pure function can contain a closure. _(javascriptallonge.pdf (source-range-8eb13d6b-00352))_
- If pure functions can contain closures, can a closure contain a pure function? Using only what we've learned so far, attempt to compose a closure that contains a pure function. If you can't, give your reasoning for why it's impossible. _(javascriptallonge.pdf (source-range-8eb13d6b-00354))_
- Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x . _(javascriptallonge.pdf (source-range-8eb13d6b-00355))_
- 27 You may also hear the term 'non-local variable.' Both are correct. _(javascriptallonge.pdf (source-range-8eb13d6b-00356))_
- 27 A free variable is one that is not bound within the function. _(javascriptallonge.pdf (source-range-8eb13d6b-00346))_
- The second doesn't have any free variables, because its only variable is bound. _(javascriptallonge.pdf (source-range-8eb13d6b-00351))_
- , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... _(javascriptallonge.pdf (source-range-8eb13d6b-00351))_
- The third one is actually two functions, one inside the other. _(javascriptallonge.pdf (source-range-8eb13d6b-00351))_
- The first function doesn't have any variables, therefore doesn't have any free variables. _(javascriptallonge.pdf (source-range-8eb13d6b-00351))_
- Using only what we've learned so far, attempt to compose a closure that contains a pure function. _(javascriptallonge.pdf (source-range-8eb13d6b-00354))_
- Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. _(javascriptallonge.pdf (source-range-8eb13d6b-00355))_

## Technical atoms

### Technical frame 1: if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00354))_

> If pure functions can contain closures, can a closure contain a pure function? Using only what we've learned so far, attempt to compose a closure that contains a pure function. If you can't, give your reasoning for why it's impossible.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00353))_

> [Figure] (p.45)

### Technical frame 2: if functions without free variables are pure, are closures impure?

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00355))_

> Pure functions always mean the same thing because all of their 'inputs' are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y , we know exactly what it does with (2, 2) . But what about this closure: (y) => x + y ? We can't say what it will do with argument (2) without understanding the magic for evaluating the free variable x .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00354))_

> If pure functions can contain closures, can a closure contain a pure function?
