---
page_id: javascriptallonge-section-tail-calls-and-default-arguments-37b86659
page_kind: source
summary: Tail Calls (and Default Arguments): 74 source-backed entries and 25 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-tail-calls-and-default-arguments-37b86659@9bad2013225dd83cc0a1535428eb0084
---

# Tail Calls (and Default Arguments)

From [[javascriptallonge]].

## Statements

- The mapWith and foldWith functions we wrote in Self-Similarity are useful for illustrating the basic principles behind using recursion to work with self-similar data structures, but they are not “production-ready” implementations. _(javascriptallonge.pdf (source-range-83ecb080-01398))_
- One of the reasons they are not production-ready is that they consume memory proportional to the size of the array being folded. _(javascriptallonge.pdf (source-range-83ecb080-01398))_
- First, mapWith((x) => x * x, [1, 2, 3, 4, 5]) is invoked. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- To do that, it has to evaluate fn(first) and mapWith(fn, rest), then evaluate [fn(first), ...mapWith(fn, rest)]. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- first is not undefined, so it evaluates [fn(first), …mapWith(fn, rest)]. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- To do that, it has to evaluate fn(first) and mapWith(fn, rest), then evaluate [fn(first), ...mapWith(fn, rest)]. _(javascriptallonge.pdf (source-range-83ecb080-01401))_
- So we know that JavaScript is going to hang on to 1. _(javascriptallonge.pdf (source-range-83ecb080-01404))_
- JavaScript cannot throw first away. _(javascriptallonge.pdf (source-range-83ecb080-01404))_
- Next, JavaScript invokes mapWith(fn, rest), which is semantically equivalent to mapWith((x) => x * x, [2, 3, 4, 5]). _(javascriptallonge.pdf (source-range-83ecb080-01405))_
- depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]). _(javascriptallonge.pdf (source-range-83ecb080-01408))_
- It can start assembling the resulting array and start discarding the information it is saving. _(javascriptallonge.pdf (source-range-83ecb080-01409))_
- Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called _call frames_ , and they include the place where the function was called, an environment, and so on). _(javascriptallonge.pdf (source-range-83ecb080-01410))_
- That information is saved on a _call stack_ , and it is quite expensive. _(javascriptallonge.pdf (source-range-83ecb080-01410))_
- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. _(javascriptallonge.pdf (source-range-83ecb080-01411))_
- Making algorithms faster is a very highly studied field of computer science. _(javascriptallonge.pdf (source-range-83ecb080-01414))_
- In fact, there are several better ways. _(javascriptallonge.pdf (source-range-83ecb080-01414))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- It isn’t going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- There are three places it returns. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- But the third is fn.apply(this, args). _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is interesting, because after sorting out what to supply as arguments (this, args), JavaScript can throw away everything in its current stack frame. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is a tail-call, because it invokes another function and returns its result. _(javascriptallonge.pdf (source-range-83ecb080-01420))_
- This is a very important characteristic of JavaScript: **If a function makes a call in tail position, JavaScript optimizes away the function call overhead and stack space.** _(javascriptallonge.pdf (source-range-83ecb080-01421))_
- And in fact, it does exactly that: It throws the stack frame away, and does not consume extra memory when making a maybe-wrapped call. _(javascriptallonge.pdf (source-range-83ecb080-01421))_
- That is excellent, but one wrapping is not a big deal. _(javascriptallonge.pdf (source-range-83ecb080-01422))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). _(javascriptallonge.pdf (source-range-83ecb080-01424))_
- The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest). _(javascriptallonge.pdf (source-range-83ecb080-01424))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call. _(javascriptallonge.pdf (source-range-83ecb080-01425))_
- The problem can be stated in such a way that the answer is obvious: length does not call itself in tail position, because it has to do two pieces of work, and while one of them is in the recursive call to length, the other happens after the recursive call. _(javascriptallonge.pdf (source-range-83ecb080-01425))_
- The obvious solution is push the 1 + work into the call to length. _(javascriptallonge.pdf (source-range-83ecb080-01430))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-83ecb080-01436))_
- Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. _(javascriptallonge.pdf (source-range-83ecb080-01436))_
- The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. _(javascriptallonge.pdf (source-range-83ecb080-01436))_
- This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. _(javascriptallonge.pdf (source-range-83ecb080-01444))_
- We can map over large arrays without incurring all the memory and performance overhead of non-tail-calls. _(javascriptallonge.pdf (source-range-83ecb080-01459))_
- And this basic transformation from a recursive function that does not make a tail call, into a recursive function that calls itself in tail position, is a bread-and-butter pattern for programmers using a language that incorporates tail-call optimization. _(javascriptallonge.pdf (source-range-83ecb080-01459))_
- In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. _(javascriptallonge.pdf (source-range-83ecb080-01462))_
- While this is mathematically elegant, it is computational filigree[63] . _(javascriptallonge.pdf (source-range-83ecb080-01469))_
- Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n - 1). _(javascriptallonge.pdf (source-range-83ecb080-01470))_
- As before, we wrote a factorialWithDelayedWork function, then used partial application (callLast) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-83ecb080-01479))_
- As before, we wrote a factorialWithDelayedWork function, then used partial application (callLast) to make a factorial function that took just the one argument and supplied the initial work value. _(javascriptallonge.pdf (source-range-83ecb080-01479))_
- But when it calls itself, it will call factorial(5, 6) and that will not mean factorial(5, 1). _(javascriptallonge.pdf (source-range-83ecb080-01484))_
- What we really want is this: We want to write something like factorial(6), and have JavaScript automatically know that we really mean factorial(6, 1). _(javascriptallonge.pdf (source-range-83ecb080-01484))_
- JavaScript provides this exact syntax, it’s called a _default argument_ , and it looks like this: _(javascriptallonge.pdf (source-range-83ecb080-01485))_
- A default argument is concise and readable. _(javascriptallonge.pdf (source-range-83ecb080-01491))_
- Now we don’t need to use two functions. _(javascriptallonge.pdf (source-range-83ecb080-01491))_
- Now we learn that we can create a default parameter argument. _(javascriptallonge.pdf (source-range-83ecb080-01493))_
- How very useful: defaults can be supplied for destructuring assignments, just like defaults for parameters. _(javascriptallonge.pdf (source-range-83ecb080-01500))_

## Technical atoms

> Context: This is roughly equivalent to writing:
_(context: javascriptallonge.pdf (source-range-83ecb080-01402))_

> Note that while evaluating mapWith(fn, rest), JavaScript must retain the value first or fn(first), plus some housekeeping information so it remembers what to do with mapWith(fn, rest) when it has a result.
_(source: javascriptallonge.pdf (source-range-83ecb080-01404))_

> Context: In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error.
_(context: javascriptallonge.pdf (source-range-83ecb080-01411))_

> mapWith((x) => x * x, [
_(source: javascriptallonge.pdf (source-range-83ecb080-01412))_

> Context: That is excellent, but one wrapping is not a big deal. When would we really care? Consider this implementation of length: The length function calls itself, but it is not a tail-call, because it returns 1 + length(rest), not length(rest).
_(context: javascriptallonge.pdf (source-range-83ecb080-01422, source-range-83ecb080-01424))_

> **const** length = ([first, ...rest]) => first === **undefined** ? 0 : 1 + length(rest);
_(source: javascriptallonge.pdf (source-range-83ecb080-01423))_

> Context: The obvious solution is push the 1 + work into the call to length. Here’s our first cut:
_(context: javascriptallonge.pdf (source-range-83ecb080-01430))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01431))_

> Context: This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:
_(context: javascriptallonge.pdf (source-range-83ecb080-01436))_

> **const** lengthDelaysWork = ([first, ...rest], numberToBeAdded) => first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01437))_

> Context: This lengthDelaysWork function calls itself in tail position. The 1 + work is done before calling itself, and by the time it reaches the terminal position, it has the answer. Now that we’ve seen how it works, we can clean up the 0 + numberToBeAdded business. But while we’re doing that, it’s annoying to remember to call it with a zero. Let’s fix that:
_(context: javascriptallonge.pdf (source-range-83ecb080-01436))_

> **const** length = (n) => lengthDelaysWork(n, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01439))_

> Context: Or we could use partial application:
_(context: javascriptallonge.pdf (source-range-83ecb080-01440))_

> **const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01441))_

> Context: Or we could use partial application:
_(context: javascriptallonge.pdf (source-range-83ecb080-01440))_

> **const** length = callLast(lengthDelaysWork, 0);
_(source: javascriptallonge.pdf (source-range-83ecb080-01442))_

> Context: Or we could use partial application:
_(context: javascriptallonge.pdf (source-range-83ecb080-01440))_

> length(["foo", "bar", "baz"]) _//=> 3_
_(source: javascriptallonge.pdf (source-range-83ecb080-01443))_

> Context: This version of length calls uses lengthDelaysWork, and JavaScript optimizes that not to take up memory proportional to the length of the string. We can use this technique with mapWith:
_(context: javascriptallonge.pdf (source-range-83ecb080-01444))_

> **const** mapWithDelaysWork = (fn, [first, ...rest], prepend) =>
_(source: javascriptallonge.pdf (source-range-83ecb080-01447))_

> first === **undefined**
_(source: javascriptallonge.pdf (source-range-83ecb080-01448))_

> **const** mapWith = callLast(mapWithDelaysWork, []);
_(source: javascriptallonge.pdf (source-range-83ecb080-01451))_

> mapWith((x) => x * x, [1, 2, 3, 4, 5]) _//=> [1,4,9,16,25]_
_(source: javascriptallonge.pdf (source-range-83ecb080-01452))_

> Context: We can use it with ridiculously large arrays:
_(context: javascriptallonge.pdf (source-range-83ecb080-01453))_

> mapWith((x) => x * x, [
_(source: javascriptallonge.pdf (source-range-83ecb080-01454))_

> Context: We can use it with ridiculously large arrays:
_(context: javascriptallonge.pdf (source-range-83ecb080-01453))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```
|0,|1,|2,|3,|4,|5,|6,|7,|8,|9,|
|---|---|---|---|---|---|---|---|---|---|
|10,|11,|12,|13,|14,|15,|16,|17,|18,|19,|
|20,|21,|22,|23,|24,|25,|26,|27,|28,|29,|
|30,|31,|32,|33,|34,|35,|36,|37,|38,|39,|
|40,|41,|42,|43,|44,|45,|46,|47,|48,|49,|
|50,|51,|52,|53,|54,|55,|56,|57,|58,|59,|
|60,|61,|62,|63,|64,|65,|66,|67,|68,|69,|
|70,|71,|72,|73,|74,|75,|76,|77,|78,|79,|
|80,|81,|82,|83,|84,|85,|86,|87,|88,|89,|
|90,|91,|92,|93,|94,|95,|96,|97,|98,|99,|
```

</details>
_(source: javascriptallonge.pdf (source-range-83ecb080-01455))_

> Context: In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example:
_(context: javascriptallonge.pdf (source-range-83ecb080-01462))_

| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |

<details>
<summary>Raw table text</summary>

```
| 0, | 1, | 2, | 3, | 4, | 5, | 6, | 7, | 8, | 9, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10, | 11, | 12, | 13, | 14, | 15, | 16, | 17, | 18, | 19, |
| 20, | 21, | 22, | 23, | 24, | 25, | 26, | 27, | 28, | 29, |
| 30, | 31, | 32, | 33, | 34, | 35, | 36, | 37, | 38, | 39, |
| 40, | 41, | 42, | 43, | 44, | 45, | 46, | 47, | 48, | 49, |
| 50, | 51, | 52, | 53, | 54, | 55, | 56, | 57, | 58, | 59, |
| 60, | 61, | 62, | 63, | 64, | 65, | 66, | 67, | 68, | 69, |
| 70, | 71, | 72, | 73, | 74, | 75, | 76, | 77, | 78, | 79, |
| 80, | 81, | 82, | 83, | 84, | 85, | 86, | 87, | 88, | 89, |
| 90, | 91, | 92, | 93, | 94, | 95, | 96, | 97, | 98, | 99, |
```

</details>
_(source: javascriptallonge.pdf (source-range-83ecb080-01463))_

> Context: The naïve function for calcuating the factorial of a positive integer follows directly from the definition: Once again, it is not tail-recursive, it needs to save the stack with each invocation so that it can take the result returned and compute n * factorial(n - 1). We can do the same conversion, pass in the work to be done:
_(context: javascriptallonge.pdf (source-range-83ecb080-01467, source-range-83ecb080-01470))_

> **const** factorial = (n) => n == 1 ? n : n * factorial(n - 1); factorial(1) _//=> 1_ factorial(5) _//=> 120_
_(source: javascriptallonge.pdf (source-range-83ecb080-01468))_

> **const** callLast = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args);
_(source: javascriptallonge.pdf (source-range-83ecb080-01476))_

> **const** factorial = callLast(factorialWithDelayedWork, 1);
_(source: javascriptallonge.pdf (source-range-83ecb080-01477))_

> factorial(1) _//=> 1_ factorial(5) _//=> 120_
_(source: javascriptallonge.pdf (source-range-83ecb080-01478))_

> Context: Our problem is that we can directly write:
_(context: javascriptallonge.pdf (source-range-83ecb080-01481))_

> But it is hideous to have to always add a 1 parameter, we’d be demanding that everyone using the factorial function know that we are using a tail-recursive implementation.
_(source: javascriptallonge.pdf (source-range-83ecb080-01483))_

> Context: We saw earlier that destructuring parameters works the same way as destructuring assignment. Now we learn that we can create a default parameter argument. Can we create a default destructuring assignment?
_(context: javascriptallonge.pdf (source-range-83ecb080-01493))_

> **const** [first, second = "two"] = ["one"];
_(source: javascriptallonge.pdf (source-range-83ecb080-01496))_

> ` ` **${** first **}** . **${** second **}** _//=> "one . two"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01497))_

> **const** [first, second = "two"] = ["primus", "secundus"];
_(source: javascriptallonge.pdf (source-range-83ecb080-01498))_

> ` ` **${** first **}** . **${** second **}** _//=> "primus . secundus"_
_(source: javascriptallonge.pdf (source-range-83ecb080-01499))_
