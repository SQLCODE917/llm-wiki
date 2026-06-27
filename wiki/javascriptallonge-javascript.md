---
page_id: javascriptallonge-javascript
page_kind: concept
summary: Javascript: 84 statement(s) and 32 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-javascript@75df427b6db0daa3e86af9ed6c1e7dd7
---

# Javascript

What [[javascriptallonge]] covers about javascript:

## Statements

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

> Context: Prior to ECMAScript 2015, JavaScript did not support collecting a variable number of arguments into a parameter, so programmers would take advantage of an awkward work-around and write things like:
_(context: javascriptallonge.pdf (source-range-83ecb080-00051))_

> **function** foo () { **var** first = arguments[0], rest = [].slice.call(arguments, 1); _// ..._ }
_(source: javascriptallonge.pdf (source-range-83ecb080-00052))_

> Context: But now, JavaScript is gaining many important features, in part because the governing body behind JavaScript has observed that programmers are constantly working around the same set of limitations. With ECMASCript 2015, we can write:
_(context: javascriptallonge.pdf (source-range-83ecb080-00055))_

> **for** ( **let** i = 0; i < array.length; ++i) { _// ..._ }
_(source: javascriptallonge.pdf (source-range-83ecb080-00056))_

> Context: Second, sometimes, the cups are of the same type–perhaps two espresso cups–but they have different contents. One holds a single, one a double. This corresponds to comparing two JavaScript values that have the same type but different “content.” For example, the number 5 is not the same thing as the number 2.
_(context: javascriptallonge.pdf (source-range-83ecb080-00188))_

> **true** === **false** _//=> false_ 2 !== 5 _//=> true_ 'two' === 'five' _//=> false_
_(source: javascriptallonge.pdf (source-range-83ecb080-00189))_

> Context: > 14Implementations of JavaScript are free to handle larger numbers. For example, if you type 9007199254740991 + 9007199254740991 into node.js, it will happily report that the answer is 18014398509481982. But code that depends upon numbers larger than 9007199254740991 may not be reliable when moved to other implementations.
_(context: javascriptallonge.pdf (source-range-83ecb080-00232))_

> 0.1 _//=> 0.1_ 0.1 + 0.1 _//=> 0.2_ 0.1 + 0.1 + 0.1 _//=> 0.30000000000000004_
_(source: javascriptallonge.pdf (source-range-83ecb080-00235))_

> Context: This kind of “inexactitude” can be ignored when performing calculations that have an acceptable deviation. For example, when centering some text on a page, as long as the difference between what you might calculate longhand and JavaScript’s calculation is less than a pixel, there is no observable error.
_(context: javascriptallonge.pdf (source-range-83ecb080-00236))_

> Professional programmers almost never use floating point numbers to represent monetary amounts.
_(source: javascriptallonge.pdf (source-range-83ecb080-00237))_

> Context: In JavaScript, operators have an order of precedence designed to mimic the way humans typically parse written arithmetic. So: JavaScript treats the expressions as if we had written (2 * 5) + 1 and 1 + (5 * 2), because the * operator has a _higher precedence_ than the + operator. JavaScript has many more operators. In a sense, they behave like little functions. If we write 1 + 2, this is conceptually similar to writing plus(1, 2) (assuming we have a function that adds two numbers bound to the name plus, of course).
_(context: javascriptallonge.pdf (source-range-83ecb080-00240, source-range-83ecb080-00242))_

> 2 * 5 + 1 _//=> 11_ 1 + 5 * 2 _//=> 11_
_(source: javascriptallonge.pdf (source-range-83ecb080-00241))_


## Source

- [[javascriptallonge]]
