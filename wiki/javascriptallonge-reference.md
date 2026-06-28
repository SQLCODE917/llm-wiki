---
page_id: javascriptallonge-reference
page_kind: concept
summary: Reference: 5 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-reference@d86b3a0bae7db5c6aa8fe8c3945435a4
---

# Reference

What [[javascriptallonge]] covers about reference:

## Statements

### As Little As Possible About Functions, But No Less

- The first sip: Basic Functions

8

I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really counts is that it is somewhat useful for a human to read. But we must understand that whether we see [Function] or () => 0, internally JavaScript has a full and proper function.

## **functions and identities**

You recall that we have two types of values with respect to identity: Value types and reference types. Value types share the same identity if they have the same contents. Reference types do not.

Which kind are functions? Let’s try them out and see. For reasons of appeasing the JavaScript parser, we’ll enclose our functions in parentheses: (() => 0) === (() => 0) _//=> false_

Like arrays, every time you evaluate an expression to produce a function, you get a new function that is not identical to any other function, even if you use the same expression to generate it. “Function” is a reference type.

## **applying functions**

Let’s put functions to work. The way we use functions is to _apply_ them to zero or more values called _arguments_ . Just as 2 + 2 produces a value (in this case 4), applying a function to zero or more arguments produces a value as well.

Here’s how we apply a function to some values in JavaScript: Let’s say that _fn_expr_ is an expression that when evaluated, produces a function. Let’s call the arguments _args_ . Here’s how to apply a function to some arguments:

## _fn_expr_ ( _args_ )

Right now, we only know about one such expression: () => 0, so let’s use it. We’ll put it in parentheses[17] to keep the parser happy, like we did above: (() => 0). Since we aren’t giving it any arguments, we’ll simply write () after the expression. So we write: (() => 0)() _//=> 0_

> 17If you’re used to other programming languages, you’ve probably internalized the idea that sometimes parentheses are used to group operations in an expression like math, and sometimes to apply a function to arguments. If not… Welcome to the ALGOL family of programming languages! _(javascriptallonge.pdf (source-range-83ecb080-00045))_

- The first sip: Basic Functions

20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans as it wishes.

What about reference types? JavaScript does not place copies of reference values in any environment. JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original.

Because many references can share the same value, and because JavaScript passes references as arguments, JavaScript can be said to implement “call by sharing” semantics. Call by sharing is generally understood to be a specialization of call by value, and it explains why some values are known as value types and other values are known as reference types.

And with that, we’re ready to look at _closures_ . When we combine our knowledge of value types, reference types, arguments, and closures, we’ll understand why this function always evaluates to true no matter what argument[26] you apply it to: (value) =>

- ((ref1, ref2) => ref1 === ref2)(value, value) > 26 Unless the argument is NaN, which isn’t equal to anything, _including itself_ . NaN in JavaScript behaves a lot like NULL in SQL. _(javascriptallonge.pdf (source-range-83ecb080-00054))_

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

- Composing and Decomposing Data

108

## **so why arrays**

If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list?

Well, linked lists are fast for a few things, like taking the front element off a list, and taking the remainder of a list. But not for iterating over a list: Pointer chasing through memory is quite a bit slower than incrementing an index. In addition to the extra fetches to dereference pointers, pointer chasing suffers from cache misses. And if you want an arbitrary item from a list, you have to iterate through the list element by element, whereas with the indexed array you just fetch it.

We have avoided discussing rebinding and mutating values, but if we want to change elements of our lists, the naïve linked list implementation suffers as well: When we take the cdr of a linked list, we are sharing the elements. If we make any change other than cons-ing a new element to the front, we are changing both the new list and the old list.

Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We’ll see this explained later in Mutation).

For these and other reasons, almost all languages today make it possible to use a fast array or vector type that is optimized for iteration, and even Lisp now has a variety of data structures that are optimized for specific use cases.

## **summary**

Although we showed how to use tail calls to map and fold over arrays with [first, ...rest], in reality this is not how it ought to be done. But it is an extremely simple illustration of how recursion works when you have a self-similar means of constructing a data structure. _(javascriptallonge.pdf (source-range-83ecb080-00157))_


## Related pages

- [[javascriptallonge-type]] - shared statements: Type shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  8  I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really count ... [truncated] (2 shared statement(s))
- [[javascriptallonge-copy]] - shared statements: Copy shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-element]] - shared statements: Element shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (1 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-sequence]] - shared statements: Sequence shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))
- [[javascriptallonge-structure]] - shared statements: Structure shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  107 **const** node5 = [5, **null** ], node4 = [4, node5], node3 = [3, node4], node2 = [2, node3], node1 = [1, node2]; **const** oneTo ... [truncated] (1 shared statement(s))
- [[javascriptallonge-value]] - shared statements: Value shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (1 shared statement(s))
- [[javascriptallonge-whenever]] - shared statements: Whenever shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  108  ## **so why arrays**  If [first, ...rest] is so slow, why does JavaScript use arrays instead of making everything a linked list? ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
