---
page_id: javascriptallonge-second
page_kind: concept
summary: Second: 4 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-second@288fa4c238ed5bfef12ac61aa6ffad00
---

# Second

What [[javascriptallonge]] covers about second:

## Statements

### Closures and Scope

- The first sip: Basic Functions

22

## **if functions without free variables are pure, are closures impure?**

The function (y) => x is interesting. It contains a _free variable_ , x.[27] A free variable is one that is not bound within the function. Up to now, we’ve only seen one way to “bind” a variable, namely by passing in an argument with the same name. Since the function (y) => x doesn’t have an argument named x, the variable x isn’t bound in this function, which makes it “free.” Now that we know that variables used in a function are either bound or free, we can bifurcate functions into those with free variables and those without:

- Functions containing no free variables are called _pure functions_ .

- Functions containing one or more free variables are called _closures_ .

Pure functions are easiest to understand. They always mean the same thing wherever you use them. Here are some pure functions we’ve already seen:

## () => {}

## (x) => x

- (x) => (y) => x

The first function doesn’t have any variables, therefore doesn’t have any free variables. The second doesn’t have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ..., and it doesn’t have a free variable: The only variable anywhere in its body is x, which is certainly bound within (x) => ....

From this, we learn something: A pure function can contain a closure.

**==> picture [29 x 30] intentionally omitted <==**

If pure functions can contain closures, can a closure contain a pure function? Using only what we’ve learned so far, attempt to compose a closure that contains a pure function. If you can’t, give your reasoning for why it’s impossible.

Pure functions always mean the same thing because all of their “inputs” are fully defined by their arguments. Not so with a closure. If I present to you this pure function (x, y) => x + y, we know exactly what it does with (2, 2). But what about this closure: (y) => x + y? We can’t say what it will do with argument (2) without understanding the magic for evaluating the free variable x.

27You may also hear the term “non-local variable.” Both are correct. _(javascriptallonge.pdf (source-range-83ecb080-00057))_

### Making Data Out Of Functions

- Composing and Decomposing Data

157

K(I)(6)(7) _//=> 7_

K(I)(12)(24) _//=> 24_

Aha! Given two values, K(I) always returns the _second_ value.

K("primus")("secundus") _//=> "primus"_

K(I)("primus")("secundus") _//=> "secundus"_

If we are not feeling particularly academic, we can name our functions: **const** first = K, second = K(I); first("primus")("secundus") _//=> "primus"_ second("primus")("secundus") _//=> "secundus"_

This is very interesting. Given two values, we can say that K always returns the _first_ value, and given two values, K(I) always returns the _second_ value.

## **backwardness**

Our first and second functions are a little different than what most people are used to when we talk about functions that access data. If we represented a pair of values as an array, we’d write them like this: _(javascriptallonge.pdf (source-range-83ecb080-00213))_

- Composing and Decomposing Data

158 **const** first = ([first, second]) => first, second = ([first, second]) => second; **const** latin = ["primus", "secundus"]; first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_ Or if we were using a POJO, we’d write them like this: **const** first = ({first, second}) => first, second = ({first, second}) => second; **const** latin = {first: "primus", second: "secundus"}; first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_

In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

But the first and second we built out of K and I don’t work that way. You call them and pass them the bits, and they choose what to return. So if we wanted to use them with a two-element array, we’d need to have a piece of code that calls some code.

Here’s the first cut: **const** first = K, second = K(I); **const** latin = (selector) => selector("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_ _(javascriptallonge.pdf (source-range-83ecb080-00214))_

### Generating Iterables

- Served by the Pot: Collections

205

A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re reinventing the use of a stack to manage recursion, because writing our code to respond to a function call makes us turn a simple recursive algorithm inside-out.

## **state machines**

Some iterables can be modelled as state machines. Let’s revisit the Fibonacci sequence. Again. One way to define it is:

- The first element of the fibonacci sequence is zero.

- The second element of the fibonacci sequence is one.

- Every subsequent element of the fibonacci sequence is the sum of the previous two elements.

Let’s write a generator:

_// Generation_ **const** fibonacci = () => { **let** a, b; console.log(a = 0); console.log(b = 1); **while** ( **true** ) { [a, b] = [b, a + b]; console.log(b); } } fibonacci() _//=>_

0 1 1 2

3 5 8 13

21

34 _(javascriptallonge.pdf (source-range-83ecb080-00270))_


## Related pages

- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Making Data Out Of Functions: Composing and Decomposing Data  157  K(I)(6)(7) _//=> 7_  K(I)(12)(24) _//=> 24_  Aha! Given two values, K(I) always returns the _second_ value.  K("primus")("secund ... [truncated] (2 shared statement(s))
- [[javascriptallonge-data]] - shared statements: Data shares source evidence from Making Data Out Of Functions: Composing and Decomposing Data  158 **const** first = ([first, second]) => first, second = ([first, second]) => second; **const** latin = ["primus", "secundus"]; fir ... [truncated] (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Generating Iterables: Served by the Pot: Collections  205  A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re re ... [truncated] (1 shared statement(s))
- [[javascriptallonge-sequence]] - shared statements: Sequence shares source evidence from Generating Iterables: Served by the Pot: Collections  205  A less kind way to put it is that the iteration version is greenspunning something built into our programming language: We’re re ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
