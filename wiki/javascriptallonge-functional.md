---
page_id: javascriptallonge-functional
page_kind: concept
summary: Functional: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-functional@baa03772785cfee47ffb5983cb0fd316
---

# Functional

What [[javascriptallonge]] covers about functional:

## Statements

### Forewords to the First Edition

- ix

A Pull of the Lever: Prefaces

## **Forewords to the First Edition**

## **michael fogus**

As a life-long bibliophile and long-time follower of Reg’s online work, I was excited when he started writing books. However, I’m very conservative about books – let’s just say that if there was an aftershave scented to the essence of “Used Book Store” then I would be first in line to buy. So as you might imagine I was “skeptical” about the decision to release JavaScript Allongé as an ongoing ebook, with a pay-what-you-want model. However, Reg sent me a copy of his book and I was humbled. Not only was this a great book, but it was also a great way to write and distribute books. Having written books myself, I know the pain of soliciting and receiving feedback.

The act of writing is an iterative process with (very often) tight revision loops. However, the process of soliciting feedback, gathering responses, sending out copies, waiting for people to actually read it (if they ever do), receiving feedback and then ultimately making sense out of how to use it takes weeks and sometimes months. On more than one occasion I’ve found myself attempting to reify feedback with content that either no longer existed or was changed beyond recognition. However, with the Leanpub model the read-feedback-change process is extremely efficient, leaving in its wake a quality book that continues to get better as others likewise read and comment into infinitude.

In the case of JavaScript Allongé, you’ll find the Leanpub model a shining example of effectiveness. Reg has crafted (and continues to craft) not only an interesting book from the perspective of a connoisseur, but also an entertaining exploration into some of the most interesting aspects of his art. No matter how much of an expert you think you are, JavaScript Allongé has something to teach you… about coffee. I kid.

As a staunch advocate of functional programming, much of what Reg has written rings true to me. While not exclusively a book about functional programming, JavaScript Allongé will provide a solid foundation for functional techniques. However, you’ll not be beaten about the head and neck with dogma. Instead, every section is motivated by relevant dialog and fortified with compelling source examples. As an author of programming books I admire what Reg has managed to accomplish and I envy the fine reader who finds JavaScript Allongé via some darkened channel in the Internet sprawl and reads it for the first time.

Enjoy.

– Fogus, fogus.me[5]

## **matthew knox**

A different kind of language requires a different kind of book.

JavaScript holds surprising depths–its scoping rules are neither strictly lexical nor strictly dynamic, and it supports procedural, object-oriented (in several flavors!), and functional programming. Many

5http://www.fogus.me _(javascriptallonge.pdf (source-range-83ecb080-00022))_

### Reassignment

- Composing and Decomposing Data

131 **const** factorial = (n) => { **let** innerFactorial = **undefined** ; **return** innerFactorial(n, 1); innerFactorial = **function** innerFactorial (x, y) { **if** (x == 1) { **return** y; } **else** { **return** innerFactorial(x-1, x * y); } } } factorial(4) _//=> undefined is not a function (evaluating 'innerFactorial(n, 1)')_ In that way, var is a little like const and let, we should always declare and bind names before using them. But it’s not like const and let in that it’s function scoped, not block scoped.

## **why const and let were invented**

const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). However, its functional scope was a problem.

We haven’t looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with var: **var** sum = 0; **for** ( **var** i = 1; i <= 100; i++) { sum = sum + i } sum #=> 5050

Hopefully, you can think of a faster way to calculate this sum.[72] And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?

> 72There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + . . . . + 99 + 100 = ? But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . . . . + (50 + 51) = ? If you notice every pair of numbers adds up to 101. There are 50 pairs of numbers, so the answer is 50*101 = 5050. Of course Gauss came up with the answer about 20 times faster than the other kids. _(javascriptallonge.pdf (source-range-83ecb080-00183))_

### Iteration and Iterables

- Served by the Pot: Collections

200

## **summary**

Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection from what we want to do with the elements of a collection. _Iterable_ ordered collections can be iterated over or gathered into another collection.

Separating concerns with iterators speaks to JavaScript’s fundamental nature: It’s a language that _wants_ to compose functionality out of small, singe-responsibility pieces, whether those pieces are functions or objects built out of functions. _(javascriptallonge.pdf (source-range-83ecb080-00264))_

### Generating Iterables

- Served by the Pot: Collections

201

## **Generating Iterables**

**==> picture [469 x 314] intentionally omitted <==**

**Banco do Café**

Iterables look cool, but then again, everything looks amazing when you’re given cherry-picked examples. What is there they don’t do well?

Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.

Iterators have to arrange its own state such that when you call them, they compute and return the next item. This seems blindingly obvious and simple. If, for example, you want numbers, you write: _(javascriptallonge.pdf (source-range-83ecb080-00266))_


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (5 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from Iteration and Iterables: Served by the Pot: Collections  200  ## **summary**  Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection fr ... [truncated] (2 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (2 shared statement(s))
- [[javascriptallonge-programming]] - shared statements: Programming shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (2 shared statement(s))
- [[javascriptallonge-allong]] - shared statements: Allong shares source evidence from Forewords to the First Edition: ix  A Pull of the Lever: Prefaces  ## **Forewords to the First Edition**  ## **michael fogus**  As a life-long bibliophile and long-time follower of Reg’s online wor ... [truncated] (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from Iteration and Iterables: Served by the Pot: Collections  200  ## **summary**  Iterators are a JavaScript feature that allow us to separate the concerns of how to iterate over a collection fr ... [truncated] (1 shared statement(s))
- [[javascriptallonge-method]] - shared statements: Method shares source evidence from Generating Iterables: Served by the Pot: Collections  201  ## **Generating Iterables**  **==> picture [469 x 314] intentionally omitted <==**  **Banco do Café**  Iterables look cool, but ... [truncated] (1 shared statement(s))
- [[javascriptallonge-object]] - shared statements: Object shares source evidence from Generating Iterables: Served by the Pot: Collections  201  ## **Generating Iterables**  **==> picture [469 x 314] intentionally omitted <==**  **Banco do Café**  Iterables look cool, but ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
