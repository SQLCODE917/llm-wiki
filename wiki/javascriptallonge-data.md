---
page_id: javascriptallonge-data
page_kind: concept
summary: Data: 5 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-data@1598649f9b4ff7b7132a20c9c05359f0
---

# Data

What [[javascriptallonge]] covers about data:

## Statements

### values and identity

- xvii

Prelude: Values and Expressions over Coffee

## **value types**

Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far.

- 2 + 2 === 4 _//=> true_

- (2 + 2 === 4) === (2 !== 5) _//=> true_

Note well what is happening with these examples: Even when we obtain a string, number, or boolean as the result of evaluating an expression, it is identical to another value of the same type with the same “content.” Strings, numbers, and booleans are examples of what JavaScript calls “value” or “primitive” types. We’ll use both terms interchangeably.

We haven’t encountered the fourth possibility yet. Stretching the metaphor somewhat, some types of cups have a serial number on the bottom. So even if you have two cups of the same type, and their contents are the same, you can still distinguish between them.

**==> picture [288 x 217] intentionally omitted <==**

**Cafe Macchiato is also a fine drink, especially when following up on the fortunes of the Azzurri or the standings in the Giro d’Italia**

## **reference types**

So what kinds of values might be the same type and have the same contents, but not be considered identical to JavaScript? Let’s meet a data structure that is very common in contemporary programming languages, the _Array_ (other languages sometimes call it a List or a Vector). _(javascriptallonge.pdf (source-range-83ecb080-00034))_

### Garbage, Garbage Everywhere

- Composing and Decomposing Data

106

In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.

Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp’s basic data type is often said to be the list, but in actuality it was the “cons cell,” the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells.

Lists were represented as linked lists of cons cells, with each cell’s head pointing to an element and the tail pointing to another cons cell.

Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today’s standards. Although the 704 used core memory, it still used vacuum tubes for its logic. Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance.

Here’s the scheme in JavaScript, using two-element arrays to represent cons cells: **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;

We can make a list by calling cons repeatedly, and terminating it with null: **const** oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, **null** )))));

## oneToFive

_//=> [1,[2,[3,[4,[5,null]]]]]_ Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like: _(javascriptallonge.pdf (source-range-83ecb080-00155))_

### Functional Iterators

- 145

Composing and Decomposing Data **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); **const** foldArray = (array) => callRight(foldArrayWith, array); **const** sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldArray([1, 4, 9, 16, 25])) _//=> 55_

What we’ve done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array);. The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable.

Here it is summing a tree of numbers: **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** foldTreeWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : Array.isArray(first) ? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\ e, rest)) : fn(first, foldTreeWith(fn, terminalValue, rest)); **const** foldTree = (tree) => callRight(foldTreeWith, tree); **const** sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldTree([1, [4, [9, 16]], 25])) _//=> 55_

We’ve found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we’ve completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-83ecb080-00200))_

### Making Data Out Of Functions

- Composing and Decomposing Data

158 **const** first = ([first, second]) => first, second = ([first, second]) => second; **const** latin = ["primus", "secundus"]; first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_ Or if we were using a POJO, we’d write them like this: **const** first = ({first, second}) => first, second = ({first, second}) => second; **const** latin = {first: "primus", second: "secundus"}; first(latin) _//=> "primus"_ second(latin) _//=> "secundus"_

In both cases, the functions first and second know how the data is represented, whether it be an array or an object. You pass the data to these functions, and they extract it.

But the first and second we built out of K and I don’t work that way. You call them and pass them the bits, and they choose what to return. So if we wanted to use them with a two-element array, we’d need to have a piece of code that calls some code.

Here’s the first cut: **const** first = K, second = K(I); **const** latin = (selector) => selector("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_ _(javascriptallonge.pdf (source-range-83ecb080-00214))_

- Composing and Decomposing Data

159

Our latin data structure is no longer a dumb data structure, it’s a function. And instead of passing latin to first or second, we pass first or second to latin. It’s _exactly backwards_ of the way we write functions that operate on data.

## **the vireo**

Given that our latin data is represented as the function (selector) => selector("primus")("secundus"), our obvious next step is to make a function that makes data. For arrays, we’d write cons = (first, second) => [first, second]. For objects we’d write: cons = (first, second) => {first, second}. In both cases, we take two parameters, and return the form of the data.

For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters: (first, second) => (selector) => selector(first)(second) For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: (first) => (second) => (selector) => selector(first)(second) Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default): **const** first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second); **const** latin = pair("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_

It works! Now what is this pair function? If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y). That’s the V combinator, the Vireo! So we can write:

78https://en.wikipedia.org/wiki/Currying _(javascriptallonge.pdf (source-range-83ecb080-00215))_


## Technical atoms

### Technical frame 1: Table of Contents

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00007))_

> ## CONTENTS

|**Composing and Decomposing Data** . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|**77**|

|---|---|---|

|Arrays and Destructuring Arguments<br>. . . .|. . . . . . . . . . . . . . . . . . . . . . . .|78|

|Self-Similarity . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|86|

|Tail Calls (and Default Arguments) . . . . . .|. . . . . . . . . . . . . . . . . . . . . . . .|94|

|Garbage, Garbage Everywhere . . . . . . . .|. . . . . . . .

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00008))_

| Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| Recipes with Data . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 168 |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | . . . . . . . . . . . . . . . . . . . . . . . . | 179 |
| Served by the Pot: Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 182 |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| The Golden Crema: Appendices and Afterwords | . . . . . . . . . . . . . . . . . . . . . . . | 265 |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |

<details>
<summary>Raw table text</summary>

```
| Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 |
| --- | --- | --- |
| Arrays and Destructuring Arguments . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| Self-Similarity . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| Tail Calls (and Default Arguments) . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| Garbage, Garbage Everywhere . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 103 |
| Plain Old JavaScript Objects . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| Mutation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 118 |
| Reassignment . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 125 |
| Copy on Write . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 135 |
| Tortoises, Hares, and Teleporting Turtles . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 141 |
| Functional Iterators . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 144 |
| Making Data Out Of Functions . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 154 |
| Recipes with Data . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 168 |
| mapWith . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 170 |
| Flip . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 172 |
| Object.assign . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 175 |
| Why? . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 178 |
| A Warm Cup: Basic Strings and Quasi-Literals | . . . . . . . . . . . . . . . . . . . . . . . . | 179 |
| Served by the Pot: Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 182 |
| Iteration and Iterables . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 183 |
| Generating Iterables . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 201 |
| Lazy and Eager Collections . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 223 |
| Interlude: The Carpenter Interviews for a Job | . . . . . . . . . . . . . . . . . . . . . . . . | 238 |
| Interactive Generators . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 250 |
| Basic Operations on Iterables . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 261 |
| The Golden Crema: Appendices and Afterwords | . . . . . . . . . . . . . . . . . . . . . . . | 265 |
| How to run the examples . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 266 |
| Thanks! . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 268 |
| Copyright Notice . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 270 |
| About The Author . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 274 |
```

</details>

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00134))_

> Composing and Decomposing Data 88 its .length. But as an exercise, how would we write a length function using just what we have already? First, we pick what we call a _terminal case_ . What is the length of an empty array? 0. So let’s start our function with the observation that if an array is empty, the length is 0: **const** length = ([first, ...rest]) => first === **undefined** ? 0 : _// ???_ We need something for when the array isn’t empty. If an array is not empty, and we break it into two 

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00135))_

| entry | content |
| --- | --- |
| 1 | Divide the problem into smaller problems |
| 2 | If a smaller problem is solvable, solve the small problem |
| 3 | If a smaller problem is not solvable, divide and conquer that problem |
| 4 | When all small problems have been solved, compose the solutions into one big solution The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our solutions are a little simpler in that we don’t really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. This simpler form of “divide and conquer” is called _linear recursion_ . It’s very useful and simple to understand. Let’s take another example. Sometimes we want to _flatten_ an array, that is, an array of arrays needs to be turned into one array of elements that aren’t arrays.[62] We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us: The usual “terminal case” will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn’t an array, we don’t flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we’ll flatten it and put it together with the rest of our solution. > 62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array. Unfolds can be thought of a “path” through a data structure, and flattening a tree is equivalent to a depth-first traverse. |

<details>
<summary>Raw table text</summary>

```
Composing and Decomposing Data 

89 

Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the stand, then they turn the burner on and use the sparker to ignite the flame. After a bit the water boils, and they turn off the burner and are lead to a second bench. 

Once again, there is a card that reads, “boil water.” But this time, the beaker is on the stand over the burner, as left behind by the previous student. The engineers light the burner immediately. Whereas the mathematicians take the beaker off the stand and empty it, thus reducing the situation to a problem they have already solved. 

There is more to recursive solutions that simply functions that invoke themselves. Recursive algorithms follow the “divide and conquer” strategy for solving a problem: 

1. Divide the problem into smaller problems 

2. If a smaller problem is solvable, solve the small problem 

3. If a smaller problem is not solvable, divide and conquer that problem 

4. When all small problems have been solved, compose the solutions into one big solution 

The big elements of divide and conquer are a method for decomposing a problem into smaller problems, a test for the smallest possible problem, and a means of putting the pieces back together. Our solutions are a little simpler in that we don’t really break a problem down into multiple pieces, we break a piece off the problem that may or may not be solvable, and solve that before sticking it onto a solution for the rest of the problem. 

This simpler form of “divide and conquer” is called _linear recursion_ . It’s very useful and simple to understand. Let’s take another example. Sometimes we want to _flatten_ an array, that is, an array of arrays needs to be turned into one array of elements that aren’t arrays.[62] 

We already know how to divide arrays into smaller pieces. How do we decide whether a smaller problem is solvable? We need a test for the terminal case. Happily, there is something along these lines provided for us: 

Array.isArray("foo") 

- _//=> false_ 

Array.isArray(["foo"]) 

- _//=> true_ 

The usual “terminal case” will be that flattening an empty array will produce an empty array. The next terminal case is that if an element isn’t an array, we don’t flatten it, and can put it together with the rest of our solution directly. Whereas if an element is an array, we’ll flatten it and put it together with the rest of our solution. 

So our first cut at a flatten function will look like this: 

> 62 flatten is a very simple unfold, a function that takes a seed value and turns it into an array. Unfolds can be thought of a “path” through a data structure, and flattening a tree is equivalent to a depth-first traverse.
```

</details>


## Related pages

- [[javascriptallonge-argument]] - shared technical atoms: Argument shares technical record from Table of Contents: | Composing and Decomposing Data . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . | 77 | | --- | --- | --- | | Arrays and Destructuring Arguments . . ... [truncated] (2 shared atom(s))
- [[javascriptallonge-array]] - shared technical atoms: Array shares technical table: Composing and Decomposing Data  89  Of course, all the students know what to do: They fill the beaker with water, place the stand on the burner and the beaker on the ... [truncated] (1 shared atom(s))
- [[javascriptallonge-structure]] - shared statements: Structure shares source evidence from values and identity: xvii  Prelude: Values and Expressions over Coffee  ## **value types**  Third, some types of cups have no distinguishing marks on them. If they are the same kind of c ... [truncated] (3 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Functional Iterators: 145  Composing and Decomposing Data **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** foldArrayWith = (fn, termin ... [truncated] (2 shared statement(s))
- [[javascriptallonge-second]] - shared statements: Second shares source evidence from Making Data Out Of Functions: Composing and Decomposing Data  158 **const** first = ([first, second]) => first, second = ([first, second]) => second; **const** latin = ["primus", "secundus"]; fir ... [truncated] (1 shared statement(s))
- [[javascriptallonge-type]] - shared statements: Type shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  106  In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and ret ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
