---
page_id: javascriptallonge-structure
page_kind: concept
summary: Structure: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-structure@b98c39682599fdb299aae0db48033d4b
---

# Structure

What [[javascriptallonge]] covers about structure:

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

107 **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; **const** oneToFive = node1;

This is a Linked List[68] , it’s just that those early Lispers used the names car and cdr after the hardware instructions, whereas today we use words like data and reference. But it works the same way: If we want the head of a list, we call car on it: car(oneToFive) _//=> 1_ car is very fast, it simply extracts the first element of the cons cell.

But what about the rest of the list? cdr does the trick: cdr(oneToFive) _//=> [2,[3,[4,[5,null]]]]_ Again, it’s just extracting a reference from a cons cell, it’s very fast. In Lisp, it’s blazingly fast because it happens in hardware. There’s no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it’s still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is faster than copying a bunch of elements.

So now we understand that in Lisp, a lot of things use linked lists, and they do that in part because it was what the hardware made possible.

Getting back to JavaScript now, when we write [first, ...rest] to gather or spread arrays, we’re emulating the semantics of car and cdr, but not the implementation. We’re doing something laborious and memory-inefficient compared to using a linked list as Lisp did and as we can still do if we choose.

That being said, it is easy to understand and helps us grasp how literals and destructuring works, and how recursive algorithms ought to mirror the self-similarity of the data structures they manipulate. And so it is today that languages like JavaScript have arrays that are slow to split into the equivalent of a car/cdr pair, but instructional examples of recursive programs still have echoes of their Lisp origins.

We’ll look at linked lists again when we look at Plain Old JavaScript Objects.

68https://en.wikipedia.org/wiki/Linked_list _(javascriptallonge.pdf (source-range-83ecb080-00156))_

### Mutation

- Composing and Decomposing Data

121 **const** EMPTY = {}; **const** OneToFive = { first: 1, rest: { first: 2, rest: { first: 3, rest: { first: 4, rest: { first: 5, rest: EMPTY } } } } };

OneToFive

_//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\_ r","rest":{"first":"five","rest":{}}}}}} const ThreeToFive = OneToFive.rest.rest;

ThreeToFive

//=> {"first":3,"rest":{"first":4,"rest":{"first":5,"rest":{}}}} ThreeToFive.first = "three"; ThreeToFive.rest.first = "four"; ThreeToFive.rest.rest.first = "five";

## ThreeToFive

//=> {"first":"three","rest":{"first":"four","rest":{"first":"five","rest":{}}\ }} OneToFive //=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":"fou\ r","rest":{"first":"five","rest":{}}}}}} Changes made to ThreeToFive affect OneToFive, because they share the same structure. When we wrote ThreeToFive = OneToFive.rest.rest;, we weren’t making a brand new copy of we were getting a reference to the same chain of nodes.

Structure sharing like this is what makes linked lists so fast for taking everything but the first item of a list: We aren’t making a new list, we’re using some of the old list. Whereas destructuring an array with [first, ...rest] does make a copy, so: _(javascriptallonge.pdf (source-range-83ecb080-00172))_

### Functional Iterators

- 145

Composing and Decomposing Data **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** foldArrayWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : fn(first, foldArrayWith(fn, terminalValue, rest)); **const** foldArray = (array) => callRight(foldArrayWith, array); **const** sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldArray([1, 4, 9, 16, 25])) _//=> 55_

What we’ve done is turn an array into a function that folds an array with const foldArray = (array) => callRight(foldArrayWith, array);. The sumFoldable function doesn’t care what kind of data structure we have, as long as it’s foldable.

Here it is summing a tree of numbers: **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** foldTreeWith = (fn, terminalValue, [first, ...rest]) => first === **undefined** ? terminalValue : Array.isArray(first) ? fn(foldTreeWith(fn, terminalValue, first), foldTreeWith(fn, terminalValu\ e, rest)) : fn(first, foldTreeWith(fn, terminalValue, rest)); **const** foldTree = (tree) => callRight(foldTreeWith, tree); **const** sumFoldable = (folder) => folder((a, b) => a + b, 0); sumFoldable(foldTree([1, [4, [9, 16]], 25])) _//=> 55_

We’ve found another way to express the principle of separating traversing a data structure from the operation we want to perform on that data structure, we’ve completely separated the knowledge of how to sum from the knowledge of how to fold an array or tree (or anything else, really). _(javascriptallonge.pdf (source-range-83ecb080-00200))_

### Making Data Out Of Functions

- Composing and Decomposing Data

159

Our latin data structure is no longer a dumb data structure, it’s a function. And instead of passing latin to first or second, we pass first or second to latin. It’s _exactly backwards_ of the way we write functions that operate on data.

## **the vireo**

Given that our latin data is represented as the function (selector) => selector("primus")("secundus"), our obvious next step is to make a function that makes data. For arrays, we’d write cons = (first, second) => [first, second]. For objects we’d write: cons = (first, second) => {first, second}. In both cases, we take two parameters, and return the form of the data.

For “data” we access with K and K(I), our “structure” is the function (selector) => selector("primus")("secundus"). Let’s extract those into parameters: (first, second) => (selector) => selector(first)(second) For consistency with the way combinators are written as functions taking just one parameter, we’ll curry[78] the function: (first) => (second) => (selector) => selector(first)(second) Let’s try it, we’ll use the word pair for the function that makes data (When we need to refer to a specific pair, we’ll use the name aPair by default): **const** first = K, second = K(I), pair = (first) => (second) => (selector) => selector(first)(second); **const** latin = pair("primus")("secundus"); latin(first) _//=> "primus"_ latin(second) _//=> "secundus"_

It works! Now what is this pair function? If we change the names to x, y, and z, we get: (x) => (y) => (z) => z(x)(y). That’s the V combinator, the Vireo! So we can write:

78https://en.wikipedia.org/wiki/Currying _(javascriptallonge.pdf (source-range-83ecb080-00215))_


## Related pages

- [[javascriptallonge-data]] - shared statements: Data shares source evidence from values and identity: xvii  Prelude: Values and Expressions over Coffee  ## **value types**  Third, some types of cups have no distinguishing marks on them. If they are the same kind of c ... [truncated] (3 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Functional Iterators: 145  Composing and Decomposing Data **const** callRight = (fn, ...args) => (...remainingArgs) => fn(...remainingArgs, ...args); **const** foldArrayWith = (fn, termin ... [truncated] (1 shared statement(s))
- [[javascriptallonge-reference]] - shared statements: Reference shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  107 **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; **const** oneTo ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
