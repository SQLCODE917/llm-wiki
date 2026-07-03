---
page_id: javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-e2a54ac1
page_kind: source
page_family: section-reference
summary: Composing and Decomposing Data / Tail Calls (and Default Arguments): 69 source-backed entries and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-e2a54ac1@5cb77e4ac46cd3474579236165eb1ef0
---

# Composing and Decomposing Data / Tail Calls (and Default Arguments)

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-composing-and-decomposing-data-6f7d7870]] - broader source section: Composing and Decomposing Data
- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-converting-non-tail-calls-to-tai-dc131bb9]] - narrower source section: Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls
- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-default-arguments-ec839e44]] - narrower source section: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments
- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-defaults-and-destructuring-483fccd5]] - narrower source section: Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring
- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-factorials-ca237dca]] - narrower source section: Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials
- [[javascriptallonge-section-composing-and-decomposing-data-tail-calls-and-default-arguments-tail-call-optimization-755a53cb]] - narrower source section: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

## Statements

- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not 'production-ready' implementations. One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. _(javascriptallonge.pdf (source-range-7239e085-00954))_
- Let's step through its execution. First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. first is not undefined , so it evaluates [fn(first), …mapWith(fn, rest)]. To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] . _(javascriptallonge.pdf (source-range-7239e085-00957))_
- Note that while evaluating mapWith(fn, rest) , JavaScript must retain the value first or fn(first) , plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result. JavaScript cannot throw first away. So we know that JavaScript is going to hang on to 1 . _(javascriptallonge.pdf (source-range-7239e085-00960))_
- Next, JavaScript invokes mapWith(fn, rest) , which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]) . And the same thing happens: JavaScript has to hang on to 2 (or 4 , or both, depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]) . _(javascriptallonge.pdf (source-range-7239e085-00961))_
- This keeps on happening, so that JavaScript collects the values 1 , 2 , 3 , 4 , and 5 plus housekeeping information by the time it calls mapWith((x) => x * x, []) . It can start assembling the resulting array and start discarding the information it is saving. _(javascriptallonge.pdf (source-range-7239e085-00962))_
- That information is saved on a call stack , and it is quite expensive. Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called call frames , and they include the place where the function was called, an environment, and so on). _(javascriptallonge.pdf (source-range-7239e085-00963))_
- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. _(javascriptallonge.pdf (source-range-7239e085-00964))_
- Is there a better way? Yes. In fact, there are several better ways. Making algorithms faster is a very highly studied field of computer science. The one we're going to look at here is called tail-call optimization , or 'TCO.' _(javascriptallonge.pdf (source-range-7239e085-00966))_
- To do that, it has to evaluate fn(first) and mapWith(fn, rest) , then evaluate [fn(first), ...mapWith(fn, rest)] . _(javascriptallonge.pdf (source-range-7239e085-00957))_

## Statements by subsection

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

- There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe -wrapped call. This is a very important characteristic of JavaScript: If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space. _(javascriptallonge.pdf (source-range-7239e085-00971))_
- That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length : _(javascriptallonge.pdf (source-range-7239e085-00972))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-7239e085-00974))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-7239e085-00975))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-7239e085-00970))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest) , not length(rest) . _(javascriptallonge.pdf (source-range-7239e085-00974))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length , the other happens after the recursive call. _(javascriptallonge.pdf (source-range-7239e085-00975))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / converting non-tail-calls to tail-calls

- The obvious solution is push the 1 + work into the call to length . Here's our first cut: _(javascriptallonge.pdf (source-range-7239e085-00978))_
- This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we've seen how it works, we can clean up the 0 + numberToBeAdded business. But while we're doing that, it's annoying to remember to call it with a zero. Let's fix that: _(javascriptallonge.pdf (source-range-7239e085-00980))_
- This version of length calls uses lengthDelaysWork , and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith : _(javascriptallonge.pdf (source-range-7239e085-00983))_
- Brilliant! We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-7239e085-00986))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-7239e085-00980))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / factorials

- In mathematics, the factorial of a non-negative integer n , denoted by n! , is the product of all positive integers less than or equal to n . For example: _(javascriptallonge.pdf (source-range-7239e085-00989))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n -1) . We can do the same conversion, pass in the work to be done: _(javascriptallonge.pdf (source-range-7239e085-00994))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-7239e085-00999))_
- Asbefore, we wrote a factorialWithDelayedWork function, then used partial application ( callLast ) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-7239e085-00999))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

- What we really want is this: We want to write something like factorial(6) , and have JavaScript automatically know that we really mean factorial(6, 1) . But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1) . _(javascriptallonge.pdf (source-range-7239e085-01004))_
- JavaScript provides this exact syntax, it's called a default argument , and it looks like this: _(javascriptallonge.pdf (source-range-7239e085-01005))_
- Now we don't need to use two functions. A default argument is concise and readable. _(javascriptallonge.pdf (source-range-7239e085-01009))_

### Composing and Decomposing Data / Tail Calls (and Default Arguments) / defaults and destructuring

- Wesawearlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment? _(javascriptallonge.pdf (source-range-7239e085-01011))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-7239e085-01013))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Tail Calls (and Default Arguments) / tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-7239e085-00970))_

> There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-00969))_

<a id="atom-technical-atom-a6d838fc3442cb2f"></a>

```
const maybe = (fn) =>
function (...args) {
if (args.length === 0) {
return;
}
else {
for (let arg of args) {
if (arg == null) return;
}
return fn.apply(this, args);
}
}
```

### Technical frame 2: Composing and Decomposing Data / Tail Calls (and Default Arguments) / default arguments

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01009))_

> Now we don't need to use two functions. A default argument is concise and readable.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01006))_

<a id="atom-technical-atom-0f7127662a9c065a"></a>

```
const factorial = (n, work = 1) =>
n === 1
? work
: factorial(n - 1, n * work);
factorial(1)
//=> 1
factorial(6)
//=> 720
```
