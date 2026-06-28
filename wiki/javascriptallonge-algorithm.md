---
page_id: javascriptallonge-algorithm
page_kind: concept
summary: Algorithm: 7 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-algorithm@08309305b56f22f6658a46982d0f5bd7
---

# Algorithm

What [[javascriptallonge]] covers about algorithm:

## Statements

### Tail Calls (and Default Arguments)

- Composing and Decomposing Data

95 depending on the implementation), plus some housekeeping information so it remembers what to do with that value, while it calls the equivalent of mapWith((x) => x * x, [3, 4, 5]).

This keeps on happening, so that JavaScript collects the values 1, 2, 3, 4, and 5 plus housekeeping information by the time it calls mapWith((x) => x * x, []). It can start assembling the resulting array and start discarding the information it is saving.

That information is saved on a _call stack_ , and it is quite expensive. Furthermore, doubling the length of an array will double the amount of space we need on the stack, plus double all the work required to set up and tear down the housekeeping data for each call (these are called _call frames_ , and they include the place where the function was called, an environment, and so on).

In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error.

mapWith((x) => x * x, [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99 ]) _//=> ???_

Is there a better way? Yes. In fact, there are several better ways. Making algorithms faster is a very highly studied field of computer science. The one we’re going to look at here is called _tail-call optimization_ , or “TCO.” _(javascriptallonge.pdf (source-range-83ecb080-00142))_

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

### Plain Old JavaScript Objects

- 117

Composing and Decomposing Data

Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away.

Mind you, this is still much, much faster than making partial copies of arrays. For a list of length _n_ , we created _n_ superfluous nodes and copied _n_ superfluous values. Whereas our naïve array algorithm created 2 _n_ superfluous arrays and copied _n_[2] superfluous values. _(javascriptallonge.pdf (source-range-83ecb080-00167))_

### Tortoises, Hares, and Teleporting Turtles

- Composing and Decomposing Data

142 } } **const** tortoiseAndHare = (aPair) => { **let** tortoisePair = aPair, harePair = aPair.rest; **while** ( **true** ) { **if** (isEmpty(tortoisePair) || isEmpty(harePair)) { **return false** ; } **if** (tortoisePair.first === harePair.first) { **return true** ; } harePair = harePair.rest; **if** (isEmpty(harePair)) { **return false** ; } **if** (tortoisePair.first === harePair.first) { **return true** ; } tortoisePair = tortoisePair.rest; harePair = harePair.rest; } }; **const** aList = list(1, 2, 3, 4, 5); tortoiseAndHare(aList) _//=> false_ forceAppend(aList, aList.rest.rest); tortoiseAndHare(aList);

_//=> true_

This algorithm is called “The Tortoise and the Hare,” and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you’ll detect the loop. _(javascriptallonge.pdf (source-range-83ecb080-00196))_

- Composing and Decomposing Data

143

At the time, I couldn’t think of any way to use hashing to solve the problem, so I gave up and tried to fit this into a powers-of-two algorithm. My first pass at it was clumsy, but it was roughly equivalent to this: **const** teleportingTurtle = (list) => { **let** speed = 1, rabbit = list, turtle = rabbit; **while** ( **true** ) { **for** ( **let** i = 0; i <= speed; i += 1) { rabbit = rabbit.rest; **if** (rabbit == **null** ) { **return false** ; } **if** (rabbit === turtle) { **return true** ; } } turtle = rabbit; speed *= 2; } **return false** ; }; **const** aList = list(1, 2, 3, 4, 5); teleportingTurtle(aList) _//=> false_ forceAppend(aList, aList.rest.rest); teleportingTurtle(aList); _//=> true_

Years later, I came across a discussion of this algorithm, The Tale of the Teleporting Turtle[75] . It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations.

What’s interesting about these two algorithms is that they both _tangle_ two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. In Functional Iterators, we’ll investigate one pattern for separating these concerns.

> 75http://www.penzba.co.uk/Writings/TheTeleportingTurtle.html _(javascriptallonge.pdf (source-range-83ecb080-00197))_

### Interlude: The Carpenter Interviews for a Job

- Served by the Pot: Collections

239

**==> picture [476 x 314] intentionally omitted <==**

**----- Start of picture text -----**<br> 94<br>**----- End of picture text -----**<br>

Christine intoned the question, as if by rote:

Consider a finite checkerboard of unknown size. On each square, we randomly place an arrow pointing to one of its four sides. A chequer is placed randomly on the checkerboard. Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. If the arrow should cause the chequer to move off the edge of the board, the game halts.

The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. “↑, →, ↑, ↓, ↑, →…” Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space.

“So,” The Carpenter asked, “I am to write an algorithm that takes a possibly infinite stream of…” Christine interrupted. “To save time, we have written a template of the solution for you in ECMASCript 2015 notation. Fill in the blanks. Your code should not presume anything about the > 94https://www.flickr.com/photos/stigrudeholm/6710684795 _(javascriptallonge.pdf (source-range-83ecb080-00304))_

- 246

Served by the Pot: Collections **const** terminates = (game) => tortoiseAndHare(positionsOf(game)) **const** test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿","￿","￿","￿"] ]; terminates(Game({board: test, position: [0, 0]})) _//=> false_ terminates(Game({board: test, position: [3, 0]})) _//=> true_ terminates(Game({board: test, position: [0, 3]})) _//=> false_ terminates(Game({board: test, position: [3, 3]})) _//=> false_

“This solution makes use of iterables and a single utility function, statefulMapWith. It also cleanly separates the mechanics of the game from the algorithm for detecting cycles in a graph.”

## **the aftermath**

The Carpenter sat down and waited. This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics.

The Carpenter was confident that although nobody would write this exact code in production, prospective employers would also recognize that nobody would try to detect whether a chequer game terminates in production, either. It’s all just a pretext for kicking off an interesting conversation, right?

Christine looked at the solution on the board, frowned, and glanced at the clock on the wall. “ _Well, where has the time gone?_ ” “We at the Thing Software company are very grateful you made some time to visit with us, but alas, that is all the time we have today. If we wish to talk to you further, we’ll be in touch.” The Carpenter never did hear back from them, but the next day there was an email containing a generous contract from Friends of Ghosts (“FOG”), a codename for a stealth startup doing interesting work, and the Thing interview was forgotten.

Some time later, The Carpenter ran into Bob Plissken at a local technology meet-up. “John! What happened at Thing?” Bob wanted to know, “I asked them what they thought of you, and all they _(javascriptallonge.pdf (source-range-83ecb080-00311))_


## Related pages

- [[javascriptallonge-carpenter]] - shared statements: Carpenter shares source evidence from Interlude: The Carpenter Interviews for a Job: 246  Served by the Pot: Collections **const** terminates = (game) => tortoiseAndHare(positionsOf(game)) **const** test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-game]] - shared statements: Game shares source evidence from Interlude: The Carpenter Interviews for a Job: 246  Served by the Pot: Collections **const** terminates = (game) => tortoiseAndHare(positionsOf(game)) **const** test = [ ["￿","￿","￿","￿"], ["￿","￿","￿","￿"], ["￿" ... [truncated] (1 shared statement(s))
- [[javascriptallonge-language]] - shared statements: Language shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  106  In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and ret ... [truncated] (1 shared statement(s))
- [[javascriptallonge-programming]] - shared statements: Programming shares source evidence from Garbage, Garbage Everywhere: Composing and Decomposing Data  106  In broad terms, this means that a single 36-bit word could store two separate 15-bit values and it was very fast to save and ret ... [truncated] (1 shared statement(s))
- [[javascriptallonge-tortoise-hare]] - shared statements: Tortoise Hare shares source evidence from Tortoises, Hares, and Teleporting Turtles: Composing and Decomposing Data  142 } } **const** tortoiseAndHare = (aPair) => { **let** tortoisePair = aPair, harePair = aPair.rest; **while** ( **true** ) { **if** ... [truncated] (1 shared statement(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Interlude: The Carpenter Interviews for a Job: Served by the Pot: Collections  239  **==> picture [476 x 314] intentionally omitted <==**  **----- Start of picture text -----**<br> 94<br>**----- End of picture te ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
