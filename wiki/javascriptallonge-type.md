---
page_id: javascriptallonge-type
page_kind: concept
summary: Type: 9 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-type@472ad6e30cf121e64208bce89581a8ad
---

# Type

What [[javascriptallonge]] covers about type:

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

- xviii

Prelude: Values and Expressions over Coffee

An array looks like this: [1, 2, 3]. This is an expression, and you can combine [] with other expressions. Go wild with things like:

[2-1, 2, 2+1] [1, 1+1, 1+1+1] Notice that you are always generating arrays with the same contents. But are they identical the same way that every value of 42 is identical to every other value of 42? Try these for yourself:

[2-1, 2, 2+1] === [1,2,3] [1,2,3] === [1, 2, 3] [1, 2, 3] === [1, 2, 3] How about that! When you type [1, 2, 3] or any of its variations, you are typing an expression that generates its own _unique_ array that is not identical to any other array, even if that other array also looks like [1, 2, 3]. It’s as if JavaScript is generating new cups of coffee with serial numbers on the bottom.

They look the same, but if you examine them with ===, you see that they are different. Every time you evaluate an expression (including typing something in) to create an array, you’re creating a new, distinct value even if it _appears_ to be the same as some other array value. As we’ll see, this is true of many other kinds of values, including _functions_ , the main subject of this book. _(javascriptallonge.pdf (source-range-83ecb080-00035))_

### A Rich Aroma: Basic Numbers

- A Rich Aroma: Basic Numbers

2 all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actually 34 base 10.

Internally, both 042 and 34 have the same representation, as double-precision floating point[13] numbers. A computer’s internal representation for numbers is important to understand. The machine’s representation of a number almost never lines up perfectly with our understanding of how a number behaves, and thus there will be places where the computer’s behaviour surprises us if we don’t know a little about what it’s doing “under the hood.” For example, the largest integer JavaScript can safely[14] handle is 9007199254740991, or 2[‘53‘] - 1. Like most programming languages, JavaScript does not allow us to use commas to separate groups of digits.

## **floating**

Most programmers never encounter the limit on the magnitude of an integer. But we mentioned that numbers are represented internally as floating point, meaning that they need not be just integers. We can, for example, write 1.5 or 33.33, and JavaScript represents these literals as floating point numbers.

It’s tempting to think we now have everything we need to do things like handle amounts of money, but as the late John Belushi would say, “Nooooooooooooooooooooo.” A computer’s internal representation for a floating point number is binary, while our literal number was in base ten. This makes no meaningful difference for integers, but it does for fractions, because some fractions base 10 do not have exact representations base 2.

One of the most oft-repeated examples is this:

- 1.0 _//=> 1_

- 1.0 + 1.0 _//=> 2_

- 1.0 + 1.0 + 1.0 _//=> 3_ However:

> 13http://en.wikipedia.org/wiki/Double-precision_floating-point_format

> 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations. _(javascriptallonge.pdf (source-range-83ecb080-00038))_

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

106

In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and retrieve pairs of values. If you had two 15-bit values and wished to write them to the register, the CONS macro would take the values and write them to a 36-bit word.

Thus, CONS put two values together, CAR extracted one, and CDR extracted the other. Lisp’s basic data type is often said to be the list, but in actuality it was the “cons cell,” the term used to describe two 15-bit values stored in one word. The 15-bit values were used as pointers that could refer to a location in memory, so in effect, a cons cell was a little data structure with two pointers to other cons cells.

Lists were represented as linked lists of cons cells, with each cell’s head pointing to an element and the tail pointing to another cons cell.

Having these instructions be very fast was important to those early designers: They were working on one of the first high-level languages (COBOL and FORTRAN being the others), and computers in the late 1950s were extremely small and slow by today’s standards. Although the 704 used core memory, it still used vacuum tubes for its logic. Thus, the design of programming languages and algorithms was driven by what could be accomplished with limited memory and performance.

Here’s the scheme in JavaScript, using two-element arrays to represent cons cells: **const** cons = (a, d) => [a, d], car = ([a, d]) => a, cdr = ([a, d]) => d;

We can make a list by calling cons repeatedly, and terminating it with null: **const** oneToFive = cons(1, cons(2, cons(3, cons(4, cons(5, **null** )))));

## oneToFive

_//=> [1,[2,[3,[4,[5,null]]]]]_ Notice that though JavaScript displays our list as if it is composed of arrays nested within each other like Russian Dolls, in reality the arrays refer to each other with references, so [1,[2,[3,[4,[5,null]]]]] is actually more like: _(javascriptallonge.pdf (source-range-83ecb080-00155))_

### Mutation

- Composing and Decomposing Data

118

## **Mutation**

**==> picture [240 x 321] intentionally omitted <==**

**Cupping Grinds**

In JavaScript, almost every type of value can _mutate_ . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using []. You can reassign a value using [] =: **const** oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree _//=> [ 'one', 2, 3 ]_ You can even add a value: _(javascriptallonge.pdf (source-range-83ecb080-00169))_

### Interlude: The Carpenter Interviews for a Job

- 246

Served by the Pot: Collections **const** terminates = (game) => tortoiseAndHare(positionsOf(game)) **const** test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"] ]; terminates(Game({board: test, position: [0, 0]})) _//=> false_ terminates(Game({board: test, position: [3, 0]})) _//=> true_ terminates(Game({board: test, position: [0, 3]})) _//=> false_ terminates(Game({board: test, position: [3, 3]})) _//=> false_

“This solution makes use of iterables and a single utility function, statefulMapWith. It also cleanly separates the mechanics of the game from the algorithm for detecting cycles in a graph.”

## **the aftermath**

The Carpenter sat down and waited. This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics.

The Carpenter was confident that although nobody would write this exact code in production, prospective employers would also recognize that nobody would try to detect whether a chequer game terminates in production, either. It’s all just a pretext for kicking off an interesting conversation, right?

Christine looked at the solution on the board, frowned, and glanced at the clock on the wall. “ _Well, where has the time gone?_ ” “We at the Thing Software company are very grateful you made some time to visit with us, but alas, that is all the time we have today. If we wish to talk to you further, we’ll be in touch.” The Carpenter never did hear back from them, but the next day there was an email containing a generous contract from Friends of Ghosts (“FOG”), a codename for a stealth startup doing interesting work, and the Thing interview was forgotten.

Some time later, The Carpenter ran into Bob Plissken at a local technology meet-up. “John! What happened at Thing?” Bob wanted to know, “I asked them what they thought of you, and all they _(javascriptallonge.pdf (source-range-83ecb080-00311))_


## Related pages

- [[javascriptallonge-value]] - shared statements: Value shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  8  I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really count ... [truncated] (3 shared statement(s))
- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (2 shared statement(s))
- [[javascriptallonge-reference]] - shared statements: Reference shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  8  I’d prefer something else, but I must accept that what gets typed back to us on the screen is arbitrary, and all that really count ... [truncated] (2 shared statement(s))
- [[javascriptallonge-data]] - shared statements: Data shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  106  In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and ret ... [truncated] (1 shared statement(s))
- [[javascriptallonge-environment]] - shared statements: Environment shares source evidence from As Little As Possible About Functions, But No Less: The first sip: Basic Functions  20 are identical to each other if they have the same content. So JavaScript can make as many copies of strings, numbers, or booleans ... [truncated] (1 shared statement(s))
- [[javascriptallonge-node]] - shared statements: Node shares source evidence from A Rich Aroma: Basic Numbers: A Rich Aroma: Basic Numbers  2 all numbers are base ten. If we start a literal with a zero, it is an octal literal. So the literal 042 is 42 base 8, which is actuall ... [truncated] (1 shared statement(s))
- [[javascriptallonge-third]] - shared statements: Third shares source evidence from values and identity: xvii  Prelude: Values and Expressions over Coffee  ## **value types**  Third, some types of cups have no distinguishing marks on them. If they are the same kind of c ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
