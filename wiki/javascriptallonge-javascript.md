---
page_id: javascriptallonge-javascript
page_kind: concept
summary: Javascript: 84 statement(s) and 32 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-javascript@34cb2077fd3efe916d357980b3604387
---

# Javascript

What [[javascriptallonge]] covers about javascript:

## Statements

_Showing 14 of 84 statements selected for this topic._

- In JavaScript, the absence of a value is written undefined, and it means there is no value. _(javascriptallonge.pdf (source-range-83ecb080-00319))_
- We said that JavaScript binds names to values, but we didn’t say what it means to bind a name to a value. _(javascriptallonge.pdf (source-range-83ecb080-00455))_
- But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. _(javascriptallonge.pdf (source-range-83ecb080-00055))_
- JavaScript Allongé, The “Six” Edition packs all the goodness of JavaScript Allongé into a new, updated package that is relevant for programmers working with (or planning to work with) the latest version of JavaScript. _(javascriptallonge.pdf (source-range-83ecb080-00063))_
- The original JavaScript Allongé was not just written to teach JavaScript: It was written to describe certain ideas in programming: Working with small, independent entities that compose together to make bigger programs. _(javascriptallonge.pdf (source-range-83ecb080-00067))_
- JavaScript Allongé does not attempt to address the question of JavaScript best practices in the wider context of software development, because JavaScript Allongé isn’t a book about practicing, it’s a book about thinking. _(javascriptallonge.pdf (source-range-83ecb080-00092))_
- JavaScript places _references_ to reference types in environments, and when the value needs to be used, JavaScript uses the reference to obtain the original. _(javascriptallonge.pdf (source-range-83ecb080-00460))_
- JavaScript functions are values, so JavaScript functions can take functions as arguments, return functions, or both. _(javascriptallonge.pdf (source-range-83ecb080-00781))_
- When he’s not shipping JavaScript, Ruby, CoffeeScript and Java applications scaling out to millions of users, Reg “Raganwald” Braithwaite has authored libraries[221] for JavaScript, CoffeeScript, and Ruby programming such as Allong.es, Method Combinators, Katy, JQuery Combinators, YouAreDaChef, andand, and others. _(javascriptallonge.pdf (source-range-83ecb080-03267))_
- JavaScript Allongé is a first and foremost, a book about _programming with functions_ . _(javascriptallonge.pdf (source-range-83ecb080-00032))_
- It’s written in JavaScript, because JavaScript hits the perfect sweet spot of being both widely used, and of having proper first-class functions with lexical scope. _(javascriptallonge.pdf (source-range-83ecb080-00032))_
- JavaScript idioms like function combinators and decorators leverage JavaScript’s power to make code easier to read, modify, debug and refactor. _(javascriptallonge.pdf (source-range-83ecb080-00034))_
- Prior to ECMAScript 2015, JavaScript did not include many features that programmers have discovered are vital to writing great software. _(javascriptallonge.pdf (source-range-83ecb080-00038))_
- For example, JavaScript did not include block-structured variables. _(javascriptallonge.pdf (source-range-83ecb080-00038))_

## Technical atoms

_Showing 6 of 32 technical atoms selected for this topic._

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00051))_

> Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00052))_

> **function** foo () { **var** first = arguments[0], rest = [].slice.call(arguments, 1); _// ..._ }

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00055))_

> But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. With ECMASCript 2015, we can write:

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00056))_

> **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00188))_

> Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00189))_

> **true** === **false** _//=> false_ 2 !== 5 _//=> true_ 'two' === 'five' _//=> false_

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00232))_

> > 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00235))_

> 0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_

### Technical atom 5

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00236))_

> This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00237))_

> Professional programmers almost never use floating point numbers to represent monetary amounts.

### Technical atom 6

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-00240, source-range-83ecb080-00242))_

> In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2), because the * operator has a _higher precedence_ than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the nam

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-00241))_

> 2 * 5 + 1 _//=> 11_ 1 + 5 * 2 _//=> 11_


## Source

- [[javascriptallonge]]
