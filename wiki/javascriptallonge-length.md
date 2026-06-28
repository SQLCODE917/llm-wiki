---
page_id: javascriptallonge-length
page_kind: concept
summary: Length: 6 statement(s) and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-length@a00551cc7566075f04b821d07fc915e5
---

# Length

What [[javascriptallonge]] covers about length:

## Statements

### Arrays and Destructuring Arguments

- Composing and Decomposing Data

88 its .length. But as an exercise, how would we write a length function using just what we have already?

First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0: **const** length = ([first, ...rest]) => first === **undefined** ? 0 : _// ???_

We need something for when the array isn’t empty. If an array is not empty, and we break it into two pieces, first and rest, the length of our array is going to be length(first) + length(rest). Well, the length of first is 1, there’s just one element at the front. But we don’t know the length of rest. If only there was a function we could call… Like length!

**const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

Let’s try it!

length([]) _//=> 0_ length(["foo"]) _//=> 1_ length(["foo", "bar", "baz"]) _//=> 3_

Our length function is _recursive_ , it calls itself. This makes sense because our definition of a list is recursive, and if a list is self-similar, it is natural to create an algorithm that is also self-similar.

## **linear recursion**

“Recursion” sometimes seems like an elaborate party trick. There’s even a joke about this:

When promising students are trying to choose between pure mathematics and applied engineering, they are given a two-part aptitude test. In the first part, they are led to a laboratory bench and told to follow the instructions printed on the card. They find a bunsen burner, a sparker, a tap, an empty beaker, a stand, and a card with the instructions “boil water.” _(javascriptallonge.pdf (source-range-83ecb080-00134))_

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

96

## **tail-call optimization**

A “tail-call” occurs when a function’s last act is to invoke another function, and then return whatever the other function returns. For example, consider the maybe function decorator: **const** maybe = (fn) => **function** (...args) { **if** (args.length === 0) { **return** ; } **else** { **for** ( **let** arg **of** args) { **if** (arg == **null** ) **return** ; } **return** fn.apply( **this** , args); } } There are three places it returns. The first two don’t return anything, they don’t matter. But the third is fn.apply(this, args). This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. It isn’t going to do any more work, so it can throw its existing stack frame away.

And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe-wrapped call. This is a very important characteristic of JavaScript: **If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space.**

That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length: **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);

The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest).

The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call.

The obvious solution? _(javascriptallonge.pdf (source-range-83ecb080-00143))_

- Composing and Decomposing Data

97

## **converting non-tail-calls to tail-calls**

The obvious solution is push the 1 + work into the call to length. Here’s our first cut: **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

? 0 + numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) lengthDelaysWork(["foo", "bar", "baz"], 0) _//=> 3_

This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that: **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**

? numberToBeAdded : lengthDelaysWork(rest, 1 + numberToBeAdded) **const** length = (n) => lengthDelaysWork(n, 0); Or we could use partial application: **const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** length = callLast(lengthDelaysWork, 0); length(["foo", "bar", "baz"]) _//=> 3_

This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith: _(javascriptallonge.pdf (source-range-83ecb080-00144))_

### Plain Old JavaScript Objects

- 117

Composing and Decomposing Data

Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away.

Mind you, this is still much, much faster than making partial copies of arrays. For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-00167))_

### Making Data Out Of Functions

- Composing and Decomposing Data

154

## **Making Data Out Of Functions**

**==> picture [469 x 352] intentionally omitted <==**

**Coffee served at the CERN particle accelerator**

In our code so far, we have used arrays and objects to represent the structure of data, and we have extensively used the ternary operator to write algorithms that terminate when we reach a base case.

For example, this length function uses a functions to bind values to names, POJOs to structure nodes, and the ternary function to detect the base case, the empty list. _(javascriptallonge.pdf (source-range-83ecb080-00210))_


## Technical atoms

### Technical frame 1: Tail Calls (and Default Arguments)

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00149))_

> Composing and Decomposing Data

101 **const** factorial = (n, work = 1) => n === 1 ? work : factorial(n - 1, n * work); factorial(1) _//=> 1_ factorial(6) _//=> 720_

By writing our parameter list as (n, work = 1) =>, we’re stating that if a second parameter is not provided, work is to be bound to 1. We can do similar things with our other tail-recursive functions: **const** length = ([first, ...rest], numberToBeAdded = 0) => first === **undefined** ? numberToBeAdded : length(rest, 1 + numberToB

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00150))_

> 102 **const** [first, second = "two"] = ["one"];


## Related pages

- [[javascriptallonge-function]] - shared statements and technical atoms: Function shares source evidence from Arrays and Destructuring Arguments: Composing and Decomposing Data  88 its .length. But as an exercise, how would we write a length function using just what we have already?  First, we pick what we cal ... [truncated]; Function shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (3 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-learn]] - shared technical atoms: Learn shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-mapwith]] - shared technical atoms: Mapwith shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Tail Calls (and Default Arguments): 102 **const** [first, second = "two"] = ["one"]; (1 shared atom(s))
- [[javascriptallonge-list]] - shared statements: List shares source evidence from Plain Old JavaScript Objects: 117  Composing and Decomposing Data  Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, a ... [truncated] (1 shared statement(s))
- [[javascriptallonge-version]] - shared statements: Version shares source evidence from Tail Calls (and Default Arguments): Composing and Decomposing Data  97  ## **converting non-tail-calls to tail-calls**  The obvious solution is push the 1 + work into the call to length. Here’s our fir ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
