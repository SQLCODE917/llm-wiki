---
page_id: javascriptallonge-section-we-ll-keep-it-simple-1104ef0d
page_kind: source
page_family: section-reference
summary: We'll keep it simple:: 219 source-backed entries and 81 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-we-ll-keep-it-simple-1104ef0d@83bea6ce5c1562aa3da6f75cadbb4e57
---

# We'll keep it simple:

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-we-ll-keep-it-simple-generators-and-iterables-4c3f39e4]] - narrower source section: We'll keep it simple: / generators and iterables
- [[javascriptallonge-section-we-ll-keep-it-simple-generators-are-coroutines-a23babe6]] - narrower source section: We'll keep it simple: / generators are coroutines
- [[javascriptallonge-section-we-ll-keep-it-simple-interactive-generators-1f19e24c]] - narrower source section: We'll keep it simple: / Interactive Generators
- [[javascriptallonge-section-we-ll-keep-it-simple-interlude-the-carpenter-interviews-for-a-job-196a6679]] - narrower source section: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job
- [[javascriptallonge-section-we-ll-keep-it-simple-javascript-s-generators-a7436505]] - narrower source section: We'll keep it simple: / javascript's generators
- [[javascriptallonge-section-we-ll-keep-it-simple-lazy-and-eager-collections-b2c43c7f]] - narrower source section: We'll keep it simple: / Lazy and Eager Collections
- [[javascriptallonge-section-we-ll-keep-it-simple-more-generators-6ce23867]] - narrower source section: We'll keep it simple: / more generators
- [[javascriptallonge-section-we-ll-keep-it-simple-rewriting-iterable-operations-9606b732]] - narrower source section: We'll keep it simple: / rewriting iterable operations

## Statements

- Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-7239e085-01658))_
- So we see the same thing: The generation version has state, but it's implicit in JavaScript's linear control flow. Whereas the iteration version must make that state explicit. _(javascriptallonge.pdf (source-range-7239e085-01659))_
- In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on. _(javascriptallonge.pdf (source-range-7239e085-01658))_

## Statements by subsection

### We'll keep it simple: / javascript's generators

- It would be very nice if we could sometimes write iterators as a .next() method that gets called, and sometimes write out a generator. Given the title of this chapter, it is not a surprise that JavaScript makes this possible. _(javascriptallonge.pdf (source-range-7239e085-01661))_
- We can write an iterator, but use a generation style of programming. An iterator written in a generation style is called a generator . To write a generator, we write a function, but we make two changes: _(javascriptallonge.pdf (source-range-7239e085-01662))_
- When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately. _(javascriptallonge.pdf (source-range-7239e085-01667))_
- Generator functions can take an argument. Let's use that to illustrate yield : _(javascriptallonge.pdf (source-range-7239e085-01668))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-7239e085-01671))_
- An iterator written in a generation style is called a generator . _(javascriptallonge.pdf (source-range-7239e085-01662))_
- This makes sense, because empty never yields anything. _(javascriptallonge.pdf (source-range-7239e085-01667))_
- Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . _(javascriptallonge.pdf (source-range-7239e085-01671))_
- Invoking only more than once gives us fresh iterators each time: _(javascriptallonge.pdf (source-range-7239e085-01671))_

### We'll keep it simple: / generators are coroutines

- This is where generators behave very, very differently from ordinary functions. What happens semantically ? _(javascriptallonge.pdf (source-range-7239e085-01679))_
- The iterator is in a nascent or 'newborn' state. _(javascriptallonge.pdf (source-range-7239e085-01681))_
- When we call interator.next() , the body of our generator begins to be evaluated. _(javascriptallonge.pdf (source-range-7239e085-01682))_
- The rest of the program continues along its way until it makes another call to iterator.next() . _(javascriptallonge.pdf (source-range-7239e085-01686))_
- The iterator resumes execution from the point where it yielded the last value. _(javascriptallonge.pdf (source-range-7239e085-01687))_
- The body of our generator runs until it returns, ends, or encounters the next yield statement. There are no more lines of code, so it ends. _(javascriptallonge.pdf (source-range-7239e085-01698))_
- This behaviour is not unique to JavaScript, generators are called coroutines 92 in other languages: _(javascriptallonge.pdf (source-range-7239e085-01700))_
- Coroutines are computer program components that generalize subroutines for nonpreemptive multitasking, by allowing multiple entry points for suspending and resuming execution at certain locations. Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-7239e085-01701))_
- Instead of thinking of there being on execution context, we can imagine that there are two execution contexts. With an iterator, we can call them the producer and the consumer . The iterator is the producer, and the code that iterates over it is the consumer. When the consumer calls .next() , it 'suspends' and the producer starts running. When the producer yields a value, the producer suspends and the consumer starts running, taking the value from the result of calling .next() . _(javascriptallonge.pdf (source-range-7239e085-01702))_
- Of course, generators need not be implemented exactly as coroutines. For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later): _(javascriptallonge.pdf (source-range-7239e085-01704))_
- But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-7239e085-01706))_
- Coroutines are well-suited for implementing more familiar program components such as cooperative tasks, exceptions, event loop, iterators, infinite lists and pipes. _(javascriptallonge.pdf (source-range-7239e085-01701))_
- For example, a 'transpiler' might implement oneTwoThree as a state machine, a little like this (there is more to generators, but we'll see that later): _(javascriptallonge.pdf (source-range-7239e085-01704))_
- If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded. _(javascriptallonge.pdf (source-range-7239e085-01706))_

### We'll keep it simple: / generators and iterables

- Our generator function oneTwoThree is not an iterator. It's a function that returns an iterator when we invoke it. We write the function to yield values instead of return a single value, and JavaScript takes care of turning this into an object with a .next() function we can call. _(javascriptallonge.pdf (source-range-7239e085-01708))_
- If we call our generator function more than once, we get new iterators. As we saw above, we called oneTwoThree three times, and each time we got an iterator that begins at 1 and counts to 3 . Recalling the way we wrote ordered collections, we could make a collection that uses a generator function: _(javascriptallonge.pdf (source-range-7239e085-01709))_
- This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects: _(javascriptallonge.pdf (source-range-7239e085-01712))_
- This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-7239e085-01714))_
- So to summarize, ThreeNumbers is an object that we've made iterable, by way of writing a generator method for [Symbol.iterator] . _(javascriptallonge.pdf (source-range-7239e085-01715))_
- Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator. _(javascriptallonge.pdf (source-range-7239e085-01714))_

### We'll keep it simple: / more generators

- Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state: _(javascriptallonge.pdf (source-range-7239e085-01720))_
- We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own. _(javascriptallonge.pdf (source-range-7239e085-01725))_

### We'll keep it simple: / yielding iterables

- We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93 _(javascriptallonge.pdf (source-range-7239e085-01731))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. But if you can write it as a simple generator, write it as a simple generator. _(javascriptallonge.pdf (source-range-7239e085-01732))_
- Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e . _(javascriptallonge.pdf (source-range-7239e085-01734))_
- JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping. _(javascriptallonge.pdf (source-range-7239e085-01735))_
- 93 There are more complex cases where you want an iterable object, because you want to maintain state in properties or declare helper methods for the generator function, and so forth. _(javascriptallonge.pdf (source-range-7239e085-01732))_

### We'll keep it simple: / rewriting iterable operations

- Now that we know about iterables, we can rewrite our iterable operations as generators. Instead of: _(javascriptallonge.pdf (source-range-7239e085-01748))_
- No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done. _(javascriptallonge.pdf (source-range-7239e085-01752))_
- We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators: _(javascriptallonge.pdf (source-range-7239e085-01753))_

### We'll keep it simple: / Summary

- A generator is a function that is defined with function * and uses yield (or yield * ) to generate values. Using a generator instead of writing an iterator object that has a .next() method allows us to write code that can be much simpler for cases like recursive iterations or state patterns. And we don't need to worry about wrapping our values in an object with .done and .value properties. _(javascriptallonge.pdf (source-range-7239e085-01759))_
- This is especially useful for making iterables. _(javascriptallonge.pdf (source-range-7239e085-01760))_

### We'll keep it simple: / Lazy and Eager Collections

- in the older style of object-oriented programming, we built 'fat' objects. Each collection knew how to map itself ( .map ), how to fold itself ( .reduce ), how to filter itself ( .filter ) and how to find one element within itself ( .find ). If we wanted to flatten collections to arrays, we wrote a .toArray method for each type of collection. _(javascriptallonge.pdf (source-range-7239e085-01764))_
- Over time, this informal 'interface' for collections grows by accretion. Some methods are only added to a few collections, some are added to all. But our objects grow fatter and fatter. We tell ourselves that, well, a collection ought to know how to map itself. _(javascriptallonge.pdf (source-range-7239e085-01765))_
- But we end up recreating the same bits of code in each .map method we create, in each .reduce method we create, in each .filter method we create, and in each .find method. Each one has its own variation, but the overall form is identical. That's a sign that we should work at a higher level of abstraction, and working with iterables is that higher level of abstraction. _(javascriptallonge.pdf (source-range-7239e085-01766))_
- This 'fat object' style springs from a misunderstanding: When we say a collection should know how to perform a map over itself, we don't need for the collection to handle every single detail. That would be like saying that when we ask a bank teller for some cash, they personally print every bank note. _(javascriptallonge.pdf (source-range-7239e085-01767))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-7239e085-01765))_

### We'll keep it simple: / Lazy and Eager Collections / implementing methods with iteration

- Object-oriented collections should definitely have methods for mapping, reducing, filtering, and finding. And they should know how to accomplish the desired result, but they should do so by delegating as much of the work as possible to operations like mapWith . _(javascriptallonge.pdf (source-range-7239e085-01769))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-7239e085-01770))_
- To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs: _(javascriptallonge.pdf (source-range-7239e085-01776))_

### We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

- 'Laziness' is a very pejorative word when applied to people. But it can be an excellent strategy for efficiency in algorithms. Let's be precise: Laziness is the characteristic of not doing any work until you know you need the result of the work. _(javascriptallonge.pdf (source-range-7239e085-01783))_
- Both expressions evaluate to 220 . And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-7239e085-01786))_
- But it's still illustrative to dissect something important: Array's .map and .filter methods gather their results into new arrays. Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-7239e085-01787))_
- Whereas the .map and .filter methods on Pair work with iterators. They produce small iterable objects that refer back to the original iteration. This reduces the memory footprint. When working with very large collections and many operations, this can be important. _(javascriptallonge.pdf (source-range-7239e085-01788))_
- This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array. _(javascriptallonge.pdf (source-range-7239e085-01791))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. _(javascriptallonge.pdf (source-range-7239e085-01792))_
- Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections. _(javascriptallonge.pdf (source-range-7239e085-01800))_
- And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript. _(javascriptallonge.pdf (source-range-7239e085-01786))_
- Thus, calling .map.filter.reduce produces two temporary arrays that are discarded when .reduce performs its final computation. _(javascriptallonge.pdf (source-range-7239e085-01787))_
- Finally, we take the first element of that filtered, squared iterable and now JavaScript actually iterates over the stack's elements, and it only needs to square two of those elements, 29 and 28 , to return the answer. _(javascriptallonge.pdf (source-range-7239e085-01792))_
- If we mutate a collection after taking an iterable, we might get an unexpected result. _(javascriptallonge.pdf (source-range-7239e085-01800))_

### We'll keep it simple: / Lazy and Eager Collections / eager collections

- An eager collection, like an array, returns a collection of its own type from each of the methods. We can make an eager collection out of any collection that is gatherable , meaning it has a .from method: _(javascriptallonge.pdf (source-range-7239e085-01802))_
- Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs: _(javascriptallonge.pdf (source-range-7239e085-01806))_
- Pair is gatherable, because it implements .from() . _(javascriptallonge.pdf (source-range-7239e085-01806))_

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job

- Plissken lined up a technical interview with a well-funded startup in San Francisco. The Carpenter arrived early for his meeting with 'Thing Software,' and was shown to conference room 13. A few minutes later, he was joined by one of the company's developers, Christine. _(javascriptallonge.pdf (source-range-7239e085-01811))_

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. Despite his experience and industry longevity, the Carpenter did not mind being asked to demonstrate that he was, in fact, the person described on the resumé. _(javascriptallonge.pdf (source-range-7239e085-01813))_
- Many companies use white-boarding code as an excuse to have a technical conversation with a candidate, and The Carpenter felt that being asked to whiteboard code was an excuse to have a technical conversation with a future colleague. 'Win, win' he thought to himself. _(javascriptallonge.pdf (source-range-7239e085-01814))_
- Consider a finite checkerboard of unknown size. On each square, we randomly place an arrow pointing to one of its four sides. A chequer is placed randomly on the checkerboard. Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. If the arrow should cause the chequer to move off the edge of the board, the game halts. _(javascriptallonge.pdf (source-range-7239e085-01818))_
- The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. '↑, →, ↑, ↓, ↑, →…' Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space. _(javascriptallonge.pdf (source-range-7239e085-01819))_
- Christine interrupted. 'To save time, we have written a template of the solution for you in ECMASCript 2015 notation. Fill in the blanks. Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. You may use babeljs.io 95 , or ES6Fiddle 96 to check your work. ' _(javascriptallonge.pdf (source-range-7239e085-01821))_
- After some small talk, Christine explained that they liked to ask candidates to whiteboard some code. _(javascriptallonge.pdf (source-range-7239e085-01813))_
- Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. _(javascriptallonge.pdf (source-range-7239e085-01821))_

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

- The Carpenter was not surprised at the problem. Bob Plissken was a crafty, almost reptilian recruiter that traded in information and secrets. Whenever Bob sent a candidate to a job interview, he debriefed them afterwards and got them to disclose what questions were asked in the interview. He then coached subsequent candidates to give polished answers to the company's pet technical questions. _(javascriptallonge.pdf (source-range-7239e085-01828))_
- Bob had, in fact, warned The Carpenter that 'Thing' liked to ask either or both of two questions: Determine how to detect a loop in a linked list, and determine whether the chequerboard game would halt. To save time, The Carpenter had prepared the same answer for both questions. _(javascriptallonge.pdf (source-range-7239e085-01830))_
- The Carpenter coughed softly, then began. 'To begin with, I'll transform a game into an iterable that generates arrows, using the 'Starman' notation for generators. I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' _(javascriptallonge.pdf (source-range-7239e085-01831))_
- 'Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.' The Carpenter sketched quickly. 'We want to take the arrows and convert them to positions. For that, we'll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That's what we need, because we need to know the current position to map each move to the next position.' _(javascriptallonge.pdf (source-range-7239e085-01834))_
- 'We could draw positions as nodes in a graph, connected by arcs representing the arrows. Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.' _(javascriptallonge.pdf (source-range-7239e085-01841))_
- 'There's an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. I approached this question in that spirit. Now that we have created an iterable of values that can be compared with === , I can show you this function:' _(javascriptallonge.pdf (source-range-7239e085-01844))_
- 'A long time ago,' The Carpenter explained, 'Someone asked me a question in an interview. I have never forgotten the question, or the general form of the solution. The question was, Given a linked list, detect whether it contains a cycle. Use constant space. ' _(javascriptallonge.pdf (source-range-7239e085-01846))_
- He then coached subsequent candidates to give polished answers to the company's pet technical questions. _(javascriptallonge.pdf (source-range-7239e085-01828))_
- The Carpenter coughed softly, then began. _(javascriptallonge.pdf (source-range-7239e085-01831))_
- I'll refactor a touch to make things clearer, for example I'll extract the board to make it easier to test:' _(javascriptallonge.pdf (source-range-7239e085-01831))_
- That's what we need, because we need to know the current position to map each move to the next position.' _(javascriptallonge.pdf (source-range-7239e085-01834))_

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the aftermath

- The Carpenter sat down and waited. This type of solution provided an excellent opportunity to explore lazy versus eager evaluation, the performance of iterators versus native iteration, single responsibility design, and many other rich topics. _(javascriptallonge.pdf (source-range-7239e085-01853))_
- The Carpenter was confident that although nobody would write this exact code in production, prospective employers would also recognize that nobody would try to detect whether a chequer game terminates in production, either. It's all just a pretext for kicking off an interesting conversation, right? _(javascriptallonge.pdf (source-range-7239e085-01854))_
- Christine looked at the solution on the board, frowned, and glanced at the clock on the wall. ' Well, where has the time gone? ' _(javascriptallonge.pdf (source-range-7239e085-01855))_

### We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink

- A few drinks later, The Carpenter was telling his Thing story and an engineer named Kidu introduced themself. _(javascriptallonge.pdf (source-range-7239e085-01863))_
- 'I worked at Thing, and Christine told us about your solution. I had a look at the code you left on the whiteboard. Of course, white-boarding in an interview situation is notoriously unreliable, so small defects are not important. But I couldn't help but notice that your solution doesn't actually meet the stated requirements for a different reason:' _(javascriptallonge.pdf (source-range-7239e085-01865))_
- 'The hasCycle function, a/k/a Tortoise and Hare, requires two separate iterators to do its job. Whereas the problem as stated involves a single stream of directions. You're essentially calling for the player to clone themselves and call out the directions in parallel.' _(javascriptallonge.pdf (source-range-7239e085-01866))_
- Kidu shrugged. 'You know, the requirement asked for a finite space algorithm, not a constant state algorithm. Doesn't it make sense to go with a faster finite space algorithm? There's no benefit to constant space if finite space is sufficient. ' _(javascriptallonge.pdf (source-range-7239e085-01869))_
- The Carpenter stared at Kidu's solution. 'I guess,' he allowed, 'It isn't always necessary to make a solution so awesome it would please the Ghosts of Mars.' _(javascriptallonge.pdf (source-range-7239e085-01871))_
- Whereas the problem as stated involves a single stream of directions. _(javascriptallonge.pdf (source-range-7239e085-01866))_

### We'll keep it simple: / Interactive Generators

- We used generators to build iterators that maintain implicit state. We saw how to use them for recursive unfolds and state machines. But there are other times we want to build functions that maintain implicit state. Let's start by looking at a very simple example of a function that can be written statefully. _(javascriptallonge.pdf (source-range-7239e085-01873))_
- Consider, for example, the moves in a game. The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made. _(javascriptallonge.pdf (source-range-7239e085-01876))_
- The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o : _(javascriptallonge.pdf (source-range-7239e085-01878))_

### We'll keep it simple: / Interactive Generators / representing naughts and crosses as a stateless function

- We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for: _(javascriptallonge.pdf (source-range-7239e085-01895))_

## Technical atoms

### Technical frame 1: We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01658))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01655))_

<a id="atom-technical-atom-0e2cb567c84a635d"></a>

```
// Iteration
let a, b, state = 0;
const fibonacci = () => {
switch (state) {
case 0:
state = 1;
return a = 0;
case 1:
state = 2;
return b = 1;
case 2:
[a, b] = [b, a + b];
return b
}
};
while (true) {
console.log(fibonacci());
}
//=>
0
1
1
2
3
5
8
13
```

### Technical frame 2: We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01658))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01657))_

<a id="atom-technical-atom-df1f6445054717c1"></a>

```
21
34
55
89
144
...
```

### Technical frame 3: We'll keep it simple:

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01658))_

> Again, this is not particularly horrendous, but like the recursive example, we're explicitly greenspunning the natural linear state. In a generator, we write 'do this, then this, then this.' In an iterator, we have to wrap that up and explicitly keep track of what step we're on.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01659))_

<a id="atom-technical-atom-eb63ca0b19d59058"></a>

> Whereas the iteration version must make that state explicit.

### Technical frame 4: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01667))_

> When we invoke empty , we get an iterator with no elements. This makes sense, because empty never yields anything. We call its .next() method, but it's done immediately.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01666))_

<a id="atom-technical-atom-1f3e69e493538b6d"></a>

```
function * empty () {};
empty().next()
//=>
{"done":true}
```

### Technical frame 5: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01668))_

> Generator functions can take an argument. Let's use that to illustrate yield :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01667))_

<a id="atom-technical-atom-b57e443f0d262b22"></a>

> When we invoke empty , we get an iterator with no elements.

### Technical frame 6: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01671))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01670))_

<a id="atom-technical-atom-f8e039c42865fbe9"></a>

```
function * only (something) {
yield something;
};
only("you").next()
//=>
{"done":false, value: "you"}
```

### Technical frame 7: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01671))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01672))_

<a id="atom-technical-atom-879df662b6da097f"></a>

```
only("you").next()
//=>
{"done":false, value: "you"}
only("the lonely").next()
//=>
{"done":false, value: "the lonely"}
```

### Technical frame 8: We'll keep it simple: / javascript's generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01671))_

> Invoking only("you") returns an iterator that we can call with .next() , and it yields "you" . Invoking only more than once gives us fresh iterators each time:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01674))_

<a id="atom-technical-atom-35869ebc98c52393"></a>

```
const sixteen = only("sixteen");
sixteen.next()
//=>
{"done":false, value: "sixteen"}
sixteen.next()
//=>
{"done":true}
```

### Technical frame 9: We'll keep it simple: / generators are coroutines

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01679))_

> This is where generators behave very, very differently from ordinary functions. What happens semantically ?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01678))_

<a id="atom-technical-atom-5f287b47dc681f91"></a>

```
const oneTwoThree = function * () {
yield 1;
yield 2;
yield 3;
};
oneTwoThree().next()
//=>
{"done":false, value: 1}
oneTwoThree().next()
//=>
{"done":false, value: 1}
oneTwoThree().next()
//=>
{"done":false, value: 1}
const iterator = oneTwoThree();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
```

### Technical frame 10: We'll keep it simple: / generators are coroutines

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01706))_

> But no matter how JavaScript implements it, our mental model is that a generator function returns an iterator, and that when we call .next() , it runs until it returns, ends, or yields. If it yields, it suspends its own execution and the consuming code resumes execution, until .next() is called again, at which point the iterator resumes its own execution from the point where it yielded.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01705))_

<a id="atom-technical-atom-e0bca2d9e767995c"></a>

```
const oneTwoThree = function () {
let state = 'newborn';
return {
next () {
switch (state) {
case 'newborn':
state = 1;
return {value: 1};
case 1:
state = 2;
return {value: 2}
case 2:
state = 3;
return {value: 3}
case 3:
return {done: true};
}
}
}
};
```

### Technical frame 11: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01712))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01709))_

<a id="atom-technical-atom-f851858a3f0a60d5"></a>

> If we call our generator function more than once, we get new iterators.

### Technical frame 12: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01712))_

> This pattern is encouraged, so much so that JavaScript provides a concise syntax for writing generator methods for objects:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01710))_

<a id="atom-technical-atom-df68b9aee54b4fac"></a>

```
const ThreeNumbers = {
[Symbol.iterator]: function * () {
yield 1;
yield 2;
yield 3
}
}
for (const i of ThreeNumbers) {
console.log(i);
}
//=>
1
2
3
[...ThreeNumbers]
//=>
[1,2,3]
const iterator = ThreeNumbers[Symbol.iterator]();
iterator.next()
//=>
{"done":false, value: 1}
iterator.next()
//=>
{"done":false, value: 2}
iterator.next()
//=>
{"done":false, value: 3}
iterator.next()
//=>
{"done":true}
```

### Technical frame 13: We'll keep it simple: / generators and iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01714))_

> This object declares a [Symbol.iterator] function that makes it iterable. Because it's declared *[Symbol.iterator] , it's a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01713))_

<a id="atom-technical-atom-08b3d4cd0486cddf"></a>

```
const ThreeNumbers = {
*[Symbol.iterator] () {
yield 1;
yield 2;
yield 3
}
}
```

### Technical frame 14: We'll keep it simple: / more generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01720))_

> Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01718))_

<a id="atom-technical-atom-2e01e3085500fe57"></a>

```
const Numbers = {
*[Symbol.iterator] () {
let i = 0;
while (true) {
yield i++;
}
}
};
for (const i of Numbers) {
console.log(i);
}
//=>
0
1
2
3
4
5
6
7
```

### Technical frame 15: We'll keep it simple: / more generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01720))_

> Our OneTwoThree example used implicit state to output the numbers in sequence. Recall that we wrote Fibonacci using explicit state:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01719))_

<a id="atom-technical-atom-5b9d980be748a7cb"></a>

```
8
9
10
...
```

### Technical frame 16: We'll keep it simple: / more generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01725))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01721))_

<a id="atom-technical-atom-ddfe8aff90ea154b"></a>

```
const Fibonacci = {
[Symbol.iterator]: () => {
let a = 0, b = 1, state = 0;
return {
next: () => {
switch (state) {
case 0:
state = 1;
return {value: a};
case 1:
state = 2;
return {value: b};
case 2:
[a, b] = [b, a + b];
return {value: b};
}
}
}
}
};
for (let n of Fibonacci) {
console.log(n)
}
//=>
0
1
1
2
3
5
8
13
```

### Technical frame 17: We'll keep it simple: / more generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01725))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01722))_

<a id="atom-technical-atom-888b3a037f1c0912"></a>

```
21
34
55
89
144
...
```

### Technical frame 18: We'll keep it simple: / more generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01725))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01724))_

<a id="atom-technical-atom-f4b0f57efe02590e"></a>

```
const Fibonacci = {
*[Symbol.iterator] () {
let a, b;
yield a = 0;
yield b = 1;
while (true) {
[a, b] = [b, a + b]
yield b;
}
}
}
for (const i of Fibonacci) {
console.log(i);
}
//=>
0
1
1
2
3
5
8
13
21
34
55
89
144
...
```

### Technical frame 19: We'll keep it simple: / more generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01725))_

> We've writing a function that returns an iterator, but we used a generator to do it. And the generator's syntax allows us to use JavaScript's natural management of state instead of constantly rolling our own.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01727))_

<a id="atom-technical-atom-10237a444786ad38"></a>

```
function * fibonacci () {
let a, b;
yield a = 0;
yield b = 1;
while (true) {
[a, b] = [b, a + b]
yield b;
}
}
for (const i of fibonacci()) {
console.log(i);
}
//=>
0
1
1
2
3
5
8
13
21
34
55
89
144
...
```

### Technical frame 20: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01731))_

> We've gone with the full iterable here, a TreeIterable(iterable) returns an iterable that treats iterable as a tree. It works, but as we've just seen, a function that returns an iterable can often be written much more simply as a generator, rather than a function that returns an iterable object: 93

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01730))_

<a id="atom-technical-atom-c3426fdb123a0599"></a>

```
const isIterable = (something) =>
!!something[Symbol.iterator];
const TreeIterable = (iterable) =>
({
[Symbol.iterator]: function * () {
for (const e of iterable) {
if (isIterable(e)) {
for (const ee of TreeIterable(e)) {
yield ee;
}
}
else {
yield e;
}
}
}
})
for (const i of TreeIterable([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
```

### Technical frame 21: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01734))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01732))_

<a id="atom-technical-atom-aa5a13c431df832a"></a>

> But if you can write it as a simple generator, write it as a simple generator.

### Technical frame 22: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01734))_

> Wetake advantage of the for...of loop in a plain and direct way: For each element e , if it is iterable, treat it as a tree and iterate over it, yielding each of its elements. If e is not an iterable, yield e .

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01733))_

<a id="atom-technical-atom-79c4ba4c0edddbb5"></a>

```
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
for (const ee of tree(e)) {
yield ee;
}
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4], 5]])) {
console.log(i);
}
//=>
1
2
3
4
5
```

### Technical frame 23: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01735))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01737))_

<a id="atom-technical-atom-0e0a00ee8196b6aa"></a>

```
for (const ee of tree(e)) {
yield ee;
}
```

### Technical frame 24: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01735))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01739))_

<a id="atom-technical-atom-06bb02d698b5a335"></a>

```
function * append (...iterables) {
for (const iterable of iterables) {
for (const element of iterable) {
yield element;
}
}
}
const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\
"]);
for (const word of lyrics) {
console.log(word);
}
//=>
a
b
c
one
two
three
do
re
me
```

### Technical frame 25: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01735))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01742))_

<a id="atom-technical-atom-3f887d1daf7a5385"></a>

```
function * append (...iterables) {
for (const iterable of iterables) {
yield * iterable;
}
}
const lyrics = append(["a", "b", "c"], ["one", "two", "three"], ["do", "re", "me\
"]);
for (const word of lyrics) {
console.log(word);
}
```

### Technical frame 26: We'll keep it simple: / yielding iterables

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01735))_

> JavaScript handles the recursion for us using its own execution stack. This is clearly simpler than trying to maintain our own stack and remembering whether we are shifting and unshifting, or pushing and popping.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01743))_

<a id="atom-technical-atom-a08bb83e790e552c"></a>

```
//=>
a
b
c
one
two
thre
do
re
```

### Technical frame 27: We'll keep it simple: / yielding iterables

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01744))_

<a id="atom-technical-atom-aba6cb6873b1bd9a"></a>

```
const isIterable = (something) =>
!!something[Symbol.iterator];
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
yield * tree(e);
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4
console.log(i);
}
//=>
1
2
3
4
5
```

### Technical frame 28: We'll keep it simple: / yielding iterables

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01745))_

<a id="atom-technical-atom-aa4f6a748680983d"></a>

```
three
do
re
me
yield * yields all of the elements of an iterable, in order. We can use it in tree, too:
const isIterable = (something) =>
!!something[Symbol.iterator];
function * tree (iterable) {
for (const e of iterable) {
if (isIterable(e)) {
yield * tree(e);
}
else {
yield e;
}
}
};
for (const i of tree([1, [2, [3, 4], 5]])) {
```

### Technical frame 29: We'll keep it simple: / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01752))_

> No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01749))_

<a id="atom-technical-atom-d3cb2e708d5fc1d6"></a>

```
const mapWith = (fn, iterable) =>
({
[Symbol.iterator]: () => {
const iterator = iterable[Symbol.iterator]();
return {
next: () => {
const {done, value} = iterator.next();
return ({done, value: done ? undefined : fn(value)});
}
}
}
});
```

### Technical frame 30: We'll keep it simple: / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01752))_

> No need to explicitly construct an object that has a [Symbol.iterator] method. No need to return an object with a .next() method. No need to fool around with {done} or {value} , just yield values until we're done.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01751))_

<a id="atom-technical-atom-ce5b6b7f5a1c9bc5"></a>

```
function * mapWith (fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
```

### Technical frame 31: We'll keep it simple: / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01753))_

> We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01754))_

<a id="atom-technical-atom-f9a92001c0ddb2e7"></a>

```
function * mapWith(fn, iterable) {
for (const element of iterable) {
yield fn(element);
}
}
function * filterWith (fn, iterable) {
for (const element of iterable) {
if (!!fn(element)) yield element;
}
}
```

### Technical frame 32: We'll keep it simple: / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01753))_

> We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01755))_

<a id="atom-technical-atom-2a19fa1bd258aa5f"></a>

```
function * untilWith (fn, iterable) {
for (const element of iterable) {
if (fn(element)) break;
yield fn(element);
}
}
```

### Technical frame 33: We'll keep it simple: / rewriting iterable operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01753))_

> We can do the same thing with our other operations like filterWith and untilWith . Here're our iterable methods rewritten as generators:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01757))_

<a id="atom-technical-atom-8476727d2baa72ac"></a>

```
const first = (iterable) =>
iterable[Symbol.iterator]().next().value;
function * rest (iterable) {
const iterator = iterable[Symbol.iterator]();
iterator.next();
yield * iterator;
}
```

### Technical frame 34: We'll keep it simple: / Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01776))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01772))_

<a id="atom-technical-atom-a76b12e0a5829382"></a>

```
const extend = function (consumer, ...providers) {
for (let i = 0; i < providers.length; ++i) {
const provider = providers[i];
for (let key in provider) {
if (provider.hasOwnProperty(key)) {
consumer[key] = provider[key]
}
}
}
return consumer
};
const LazyCollection = {
map(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
const {
done, value
} = iterator.next();
return ({
done, value: done ? undefined : fn(value)
});
}
}
}
}, LazyCollection);
},
reduce(fn, seed) {
const iterator = this[Symbol.iterator]();
let iterationResult,
accumulator = seed;
while ((iterationResult = iterator.next(), !iterationResult.done)) {
accumulator = fn(accumulator, iterationResult.value);
}
return accumulator;
```

### Technical frame 35: We'll keep it simple: / Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01776))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01773))_

<a id="atom-technical-atom-1dd93a5412bdd436"></a>

```
},
filter(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
do {
const {
done, value
} = iterator.next();
} while (!done && !fn(value));
return {
done, value
};
}
}
}
}, LazyCollection)
},
find(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
let {
done, value
} = iterator.next();
done = done || fn(value);
return ({
done, value: done ? undefined : value
});
}
}
}
```

### Technical frame 36: We'll keep it simple: / Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01776))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01774))_

<a id="atom-technical-atom-f8a7f12c9c5c68d8"></a>

```
}, LazyCollection)
},
until(fn) {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
return {
next: () => {
let {
done, value
} = iterator.next();
done = done || fn(value);
return ({
done, value: done ? undefined : value
});
}
}
}
}, LazyCollection)
},
first() {
return this[Symbol.iterator]().next().value;
},
rest() {
return Object.assign({
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
iterator.next();
return iterator;
}
}, LazyCollection);
},
take(numberToTake) {
return Object.assign({
```

### Technical frame 37: We'll keep it simple: / Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01776))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01775))_

<a id="atom-technical-atom-e5fc2652767abdb9"></a>

```
[Symbol.iterator]: () => {
const iterator = this[Symbol.iterator]();
let remainingElements = numberToTake;
return {
next: () => {
let {
done, value
} = iterator.next();
done = done || remainingElements-- <= 0;
return ({
done, value: done ? undefined : value
});
}
}
}
}, LazyCollection);
}
}
```

### Technical frame 38: We'll keep it simple: / Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01776))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01777))_

<a id="atom-technical-atom-f8b7820b12c59402"></a>

```
const Numbers = Object.assign({
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}, LazyCollection);
// Pair, a/k/a linked lists
const EMPTY = {
isEmpty: () => true
```

### Technical frame 39: We'll keep it simple: / Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01776))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01778))_

<a id="atom-technical-atom-d0d3cda77a4b76f7"></a>

```
};
const isEmpty = (node) => node === EMPTY;
const Pair = (car, cdr = EMPTY) =>
Object.assign({
car,
cdr,
isEmpty: () => false,
[Symbol.iterator]: function () {
let currentPair = this;
return {
next: () => {
if (currentPair.isEmpty()) {
return {done: true}
}
else {
const value = currentPair.car;
currentPair = currentPair.cdr;
return {done: false, value}
}
}
}
}
}, LazyCollection);
Pair.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair(value, iterationToList(iteration));
})(iterable[Symbol.iterator]());
// Stack
const Stack = () =>
Object.assign({
array: [],
index: -1,
push: function (value) {
```

### Technical frame 40: We'll keep it simple: / Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01776))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01779))_

<a id="atom-technical-atom-692b026c4c1cf015"></a>

```
return this.array[this.index += 1] = value;
},
pop: function () {
const value = this.array[this.index];
this.array[this.index] = undefined;
if (this.index >= 0) {
this.index -= 1
}
return value
},
isEmpty: function () {
return this.index < 0
},
[Symbol.iterator]: function () {
let iterationIndex = this.index;
return {
next: () => {
if (iterationIndex > this.index) {
iterationIndex = this.index;
}
if (iterationIndex < 0) {
return {done: true};
}
else {
return {done: false, value: this.array[iterationIndex--]}
}
}
}
}
}, LazyCollection);
Stack.from = function (iterable) {
const stack = this();
for (let element of iterable) {
stack.push(element);
}
return stack;
}
```

### Technical frame 41: We'll keep it simple: / Lazy and Eager Collections / implementing methods with iteration

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01776))_

> To use LazyCollection , we mix it into an any iterable object. For simplicity, we'll show how to mix it into Numbers and Pair . But it can also be mixed into prototypes (a/k/a 'classes'), traits, or other OO constructs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01780))_

<a id="atom-technical-atom-81195c6e18dcad00"></a>

```
// Pair and Stack in action
Stack.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
//=> 100
Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
```

### Technical frame 42: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01786))_

> Both expressions evaluate to 220 . And the array is faster in practice, because it is a built-in data type that performs its work in the engine, while the linked list does its work in JavaScript.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01785))_

<a id="atom-technical-atom-8470d296d51b52a8"></a>

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
Pair.from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.reduce((seed, element) => seed + element, 0)
```

### Technical frame 43: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01791))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01788))_

<a id="atom-technical-atom-97184db350f67860"></a>

> When working with very large collections and many operations, this can be important.

### Technical frame 44: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01791))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01789))_

<a id="atom-technical-atom-5e62d943d738ba1c"></a>

> The effect is even more pronounced when we use methods like first , until , or take :

### Technical frame 45: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01791))_

> This expression begins with a stack containing 30 elements. The top two are 29 and 28 . It maps to the squares of all 30 numbers, but our code for mapping an iteration returns an iterable that can iterate over the squares of our numbers, not an array or stack of the squares. Same with .filter , we get an iterable that can iterate over the even squares, but not an actual stack or array.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01790))_

<a id="atom-technical-atom-e10108dd925b5dd3"></a>

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => x * x)
.filter((x) => x % 2 == 0)
.first()
```

### Technical frame 46: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01800))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01794))_

<a id="atom-technical-atom-f96696a48fc95366"></a>

```
Stack.from([ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
.map((x) => {
console.log(`squaring ${x}`);
return x * x
})
.filter((x) => {
console.log(`filtering ${x}`);
return x % 2 == 0
})
.first()
//=>
squaring 29
filtering 841
squaring 28
filtering 784
784
```

### Technical frame 47: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01800))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01795))_

<a id="atom-technical-atom-3773064a93e8ab4d"></a>

> If we write the almost identical thing with an array, we get a different behaviour:

### Technical frame 48: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01800))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01796))_

<a id="atom-technical-atom-08552cca31bbad29"></a>

```
[ 0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
.reverse()
.map((x) => {
console.log(`squaring ${x}`);
return x * x
})
.filter((x) => {
console.log(`filtering ${x}`);
return x % 2 == 0
})[0]
//=>
squaring 0
squaring 1
squaring 2
squaring 3
...
squaring 28
squaring 29
filtering 0
filtering 1
filtering 4
...
filtering 784
filtering 841
784
```

### Technical frame 49: We'll keep it simple: / Lazy and Eager Collections / lazy collection operations

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01800))_

> Balanced against their flexibility, our 'lazy collections' use structure sharing. If we mutate a collection after taking an iterable, we might get an unexpected result. This is why 'pure' functional languages like Haskell combine lazy semantics with immutable collections, and why even 'impure' languages like Clojure emphasize the use of immutable collections.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01799))_

<a id="atom-technical-atom-8672457350f9a8ff"></a>

```
const Numbers = Object.assign({
[Symbol.iterator]: () => {
let n = 0;
return {
next: () =>
({done: false, value: n++})
}
}
}, LazyCollection);
const firstCubeOver1234 =
Numbers
.map((x) => x * x * x)
.filter((x) => x > 1234)
.first()
//=> 1331
```

### Technical frame 50: We'll keep it simple: / Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01806))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01803))_

<a id="atom-technical-atom-260d903a41c4e031"></a>

```
const extend = function (consumer, ...providers) {
for (let i = 0; i < providers.length; ++i) {
const provider = providers[i];
for (let key in provider) {
if (provider.hasOwnProperty(key)) {
consumer[key] = provider[key]
}
}
}
return consumer
};
```

### Technical frame 51: We'll keep it simple: / Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01806))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01804))_

<a id="atom-technical-atom-a84a9a6634bcef5c"></a>

```
const EagerCollection = (gatherable) =>
({
map(fn) {
const
original = this;
return gatherable.from(
(function* () {
for (let element of original) {
yield fn(element);
}
})()
);
},
reduce(fn, seed) {
let accumulator = seed;
for(let element of this) {
accumulator = fn(accumulator, element);
}
return accumulator;
},
filter(fn) {
const original = this;
return gatherable.from(
(function* () {
for (let element of original) {
if (fn(element)) yield element;
}
})()
);
},
find(fn) {
for (let element of this) {
if (fn(element)) return element;
}
},
until(fn) {
```

### Technical frame 52: We'll keep it simple: / Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01806))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01805))_

<a id="atom-technical-atom-42f03cd992a4e79f"></a>

```
const original = this;
return gatherable.from(
(function* () {
for (let element of original) {
if (fn(element)) break;
yield element;
}
})()
);
},
first() {
return this[Symbol.iterator]().next().value;
},
rest() {
const iteration = this[Symbol.iterator]();
iteration.next();
return gatherable.from(
(function* () {
yield * iteration;
})()
);
return gatherable.from(iterable);
},
take(numberToTake) {
const original = this;
let numberRemaining = numberToTake;
return gatherable.from(
(function* () {
for (let element of original) {
if (numberRemaining-- <= 0) break;
yield element;
}
})()
);
}
});
```

### Technical frame 53: We'll keep it simple: / Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01806))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01807))_

<a id="atom-technical-atom-6e8c82aa1db29bdf"></a>

```
const EMPTY = {
isEmpty: () => true
};
const isEmpty = (node) => node === EMPTY;
const Pair = (car, cdr = EMPTY) =>
Object.assign({
car,
cdr,
isEmpty: () => false,
[Symbol.iterator]: function () {
let currentPair = this;
return {
next: () => {
if (currentPair.isEmpty()) {
return {done: true}
}
else {
const value = currentPair.car;
currentPair = currentPair.cdr;
return {done: false, value}
}
}
}
}
}, EagerCollection(Pair));
Pair.from = (iterable) =>
(function iterationToList (iteration) {
const {done, value} = iteration.next();
return done ? EMPTY : Pair(value, iterationToList(iteration));
})(iterable[Symbol.iterator]());
Pair.from([1, 2, 3, 4, 5]).map(x => x * 2)
//=>
```

### Technical frame 54: We'll keep it simple: / Lazy and Eager Collections / eager collections

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01806))_

> Here is our Pair implementation. Pair is gatherable, because it implements .from() . We mix EagerCollection(Pair) into it, and this gives it all of our collection methods, which each method returning a new list of pairs:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01808))_

<a id="atom-technical-atom-2b2f858d8e7ab9b6"></a>

```
{"car": 2,
"cdr": {"car": 4,
"cdr": {"car": 6,
"cdr": {"car": 8,
"cdr": {"car": 10,
"cdr": {}
}
}
}
}
}
```

### Technical frame 55: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01818))_

> Consider a finite checkerboard of unknown size. On each square, we randomly place an arrow pointing to one of its four sides. A chequer is placed randomly on the checkerboard. Each move consists of moving the chequer one square in the direction of the arrow in the square it occupies. If the arrow should cause the chequer to move off the edge of the board, the game halts.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01816))_

<a id="atom-technical-atom-852b5f4ff7a52b7c"></a>

> [Figure] (p.262)

### Technical frame 56: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01819))_

> The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. '↑, →, ↑, ↓, ↑, →…' Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01818))_

<a id="atom-technical-atom-a590a5517057cd75"></a>

> If the arrow should cause the chequer to move off the edge of the board, the game halts.

### Technical frame 57: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01819))_

> The problem is this: The game board is hidden from us. A player moves the chequer, following the rules. As the player moves the chequer, they calls out the direction of movement, e.g. '↑, →, ↑, ↓, ↑, →…' Write an algorithm that will determine whether the game halts, strictly from the called out directions, in finite time and space.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01821))_

<a id="atom-technical-atom-da06962e386b539d"></a>

> You may use babeljs.io 95 , or ES6Fiddle 96 to check your work.

### Technical frame 58: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the problem

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01821))_

> Christine interrupted. 'To save time, we have written a template of the solution for you in ECMASCript 2015 notation. Fill in the blanks. Your code should not presume anything about the game-board's size or contents, only that it is given an arrow every time though the while loop. You may use babeljs.io 95 , or ES6Fiddle 96 to check your work. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01824))_

<a id="atom-technical-atom-0699eed645a4372c"></a>

```
const Game = (size = 8) => {
// initialize the board
const board = [];
for (let i = 0; i < size; ++i) {
board[i] = [];
for (let j = 0; j < size; ++j) {
board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)];
}
}
// initialize the position
let initialPosition = [
2 + Math.floor(Math.random() * (size - 4)),
2 + Math.floor(Math.random() * (size - 4))
];
// ???
let [x, y] = initialPosition;
const MOVE = {
"￿": ([x, y]) => [x - 1, y],
"￿": ([x, y]) => [x + 1, y],
"￿": ([x, y]) => [x, y - 1],
"￿": ([x, y]) => [x, y + 1]
};
while (x >= 0 && y >=0 && x < size && y < size) {
const arrow = board[x][y];
// ???
[x, y] = MOVE[arrow]([x, y]);
}
// ???
};
```

### Technical frame 59: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01834))_

> 'Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.' The Carpenter sketched quickly. 'We want to take the arrows and convert them to positions. For that, we'll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That's what we need, because we need to know the current position to map each move to the next position.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01832))_

<a id="atom-technical-atom-5e67bf82132459fa"></a>

```
const MOVE = {
"￿": ([x, y]) => [x - 1, y],
"￿": ([x, y]) => [x + 1, y],
"￿": ([x, y]) => [x, y + 1],
"￿": ([x, y]) => [x, y - 1]
};
const Board = (size = 8) => {
// initialize the board
const board = [];
for (let i = 0; i < size; ++i) {
board[i] = [];
for (let j = 0; j < size; ++j) {
board[i][j] = '￿￿￿￿'[Math.floor(Math.random() * 4)];
}
}
// initialize the position
const position = [
```

### Technical frame 60: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01834))_

> 'Now that we have an iterable, we can transform the iterable of arrows into an iterable of positions.' The Carpenter sketched quickly. 'We want to take the arrows and convert them to positions. For that, we'll map the Game iterable to positions. A statefulMap is a lazy map that preserves state from iteration to iteration. That's what we need, because we need to know the current position to map each move to the next position.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01833))_

<a id="atom-technical-atom-6081e6678c7d1d5f"></a>

```
Math.floor(Math.random() * size),
Math.floor(Math.random() * size)
];
return {board, position};
};
const Game = ({board, position}) => {
const size = board[0].length;
return ({
*[Symbol.iterator] () {
let [x, y] = position;
while (x >= 0 && y >=0 && x < size && y < size) {
const direction = board[y][x];
yield direction;
[x, y] = MOVE[direction]([x, y]);
}
}
});
};
```

### Technical frame 61: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01841))_

> 'We could draw positions as nodes in a graph, connected by arcs representing the arrows. Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01836))_

<a id="atom-technical-atom-f42f65b6b3c55d2b"></a>

```
const statefulMapWith = (fn, seed, iterable) =>
({
*[Symbol.iterator] () {
let value,
state = seed;
for (let element of iterable) {
[state, value] = fn(state, element);
yield value;
```

### Technical frame 62: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01841))_

> 'We could draw positions as nodes in a graph, connected by arcs representing the arrows. Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01837))_

<a id="atom-technical-atom-5cac2ca7f0313153"></a>

```
}
}
});
```

### Technical frame 63: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01841))_

> 'We could draw positions as nodes in a graph, connected by arcs representing the arrows. Detecting whether the game terminates is equivalent to detecting whether the graph contains a cycle.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01839))_

<a id="atom-technical-atom-65983b25668fd849"></a>

```
const positionsOf = (game) =>
statefulMapWith(
(position, direction) => {
const [x, y] =
MOVE[direction](position);
position = [x, y];
return [position, `x: ${x}, y: ${y}`];
},
[0, 0],
game);
```

### Technical frame 64: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01844))_

> 'There's an old joke that a mathematician is someone who will take a five-minute problem, then spend an hour proving it is equivalent to another problem they have already solved. I approached this question in that spirit. Now that we have created an iterable of values that can be compared with === , I can show you this function:'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01842))_

<a id="atom-technical-atom-6e3131abf4d34290"></a>

> [Figure] (p.267)

### Technical frame 65: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01846))_

> 'A long time ago,' The Carpenter explained, 'Someone asked me a question in an interview. I have never forgotten the question, or the general form of the solution. The question was, Given a linked list, detect whether it contains a cycle. Use constant space. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01845))_

<a id="atom-technical-atom-fbdc0186dc160d97"></a>

```
const tortoiseAndHare = (iterable) => {
const hare = iterable[Symbol.iterator]();
let hareResult = (hare.next(), hare.next());
for (let tortoiseValue of iterable) {
hareResult = hare.next();
if (hareResult.done) {
return false;
}
if (tortoiseValue === hareResult.value) {
return true;
}
hareResult = hare.next();
if (hareResult.done) {
return false;
}
if (tortoiseValue === hareResult.value) {
return true;
}
}
return false;
};
```

### Technical frame 66: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the carpenter's solution

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01846))_

> 'A long time ago,' The Carpenter explained, 'Someone asked me a question in an interview. I have never forgotten the question, or the general form of the solution. The question was, Given a linked list, detect whether it contains a cycle. Use constant space. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01850))_

<a id="atom-technical-atom-23f05dfe5a02c060"></a>

```
const terminates = (game) =>
tortoiseAndHare(positionsOf(game))
const test = [
["￿","￿","￿","￿"],
["￿","￿","￿","￿"],
["￿","￿","￿","￿"],
["￿","￿","￿","￿"]
];
terminates(Game({board: test, position: [0, 0]}))
//=> false
terminates(Game({board: test, position: [3, 0]}))
//=> true
terminates(Game({board: test, position: [0, 3]}))
//=> false
terminates(Game({board: test, position: [3, 3]}))
//=> false
```

### Technical frame 67: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / the aftermath

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01855))_

> Christine looked at the solution on the board, frowned, and glanced at the clock on the wall. ' Well, where has the time gone? '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01861))_

<a id="atom-technical-atom-e18d743db306f0a5"></a>

> [Figure] (p.270)

### Technical frame 68: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01869))_

> Kidu shrugged. 'You know, the requirement asked for a finite space algorithm, not a constant state algorithm. Doesn't it make sense to go with a faster finite space algorithm? There's no benefit to constant space if finite space is sufficient. '

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01868))_

<a id="atom-technical-atom-1f7039bb05bad07c"></a>

```
// implements Teleporting Tortoise
// cycle detection algorithm.
const hasCycle = (iterable) => {
let iterator = iterable[Symbol.iterator](),
teleportDistance = 1;
while (true) {
let {value, done} = iterator.next(),
tortoise = value;
if (done) return false;
for (let i = 0; i < teleportDistance; ++i) {
let {value, done} = iterator.next(),
hare = value;
if (done) return false;
if (tortoise === hare) return true;
}
teleportDistance *= 2;
}
return false;
};
```

### Technical frame 69: We'll keep it simple: / Interlude: The Carpenter Interviews for a Job / after another drink

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01871))_

> The Carpenter stared at Kidu's solution. 'I guess,' he allowed, 'It isn't always necessary to make a solution so awesome it would please the Ghosts of Mars.'

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01870))_

<a id="atom-technical-atom-6e1e8c30721fce75"></a>

```
const hasCycle = (orderedCollection) => {
const visited = new Set();
for (let element of orderedCollection) {
if (visited.has(element)) {
return true;
}
visited.add(element);
}
return false;
};
```

### Technical frame 70: We'll keep it simple: / Interactive Generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01876))_

> Consider, for example, the moves in a game. The moves a player makes are a stream of values, just like the contents of an array can be consider a stream of values. But of course, iterating over a stream of moves requires us to wait for the game to be over so we know what moves were made.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01874))_

<a id="atom-technical-atom-baf41efc12d55afa"></a>

> [Figure] (p.273)

### Technical frame 71: We'll keep it simple: / Interactive Generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01878))_

> The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01880))_

<a id="atom-technical-atom-7eee6429dcf3e259"></a>

> [Figure] (p.274)

### Technical frame 72: We'll keep it simple: / Interactive Generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01878))_

> The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01882))_

<a id="atom-technical-atom-477d1a02b417eb59"></a>

> [Figure] (p.274)

### Technical frame 73: We'll keep it simple: / Interactive Generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01878))_

> The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01884))_

<a id="atom-technical-atom-89edf54c56661718"></a>

> [Figure] (p.274)

### Technical frame 74: We'll keep it simple: / Interactive Generators

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01878))_

> The first player will always be o , and they will always place their chequer in the top-left corner, coincidentally numbered o :

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01886))_

<a id="atom-technical-atom-b28fbd22556115af"></a>

> [Figure] (p.274)

### Technical frame 75: We'll keep it simple: / Interactive Generators

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01888))_

<a id="atom-technical-atom-9edb61b96f5ecd84"></a>

> [Figure] (p.274)

### Technical frame 76: We'll keep it simple: / Interactive Generators

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01890))_

<a id="atom-technical-atom-0053b0b9f9573ac1"></a>

> [Figure] (p.275)

### Technical frame 77: We'll keep it simple: / Interactive Generators

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01892))_

<a id="atom-technical-atom-dbb0427d28303838"></a>

> [Figure] (p.275)

### Technical frame 78: We'll keep it simple: / Interactive Generators / representing naughts and crosses as a stateless function

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01895))_

> We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01896))_

<a id="atom-technical-atom-cb10e6f0eeb92ddf"></a>

> [Figure] (p.275)

### Technical frame 79: We'll keep it simple: / Interactive Generators / representing naughts and crosses as a stateless function

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01895))_

> We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01898))_

<a id="atom-technical-atom-ed96a88e635bb392"></a>

> [Figure] (p.275)

### Technical frame 80: We'll keep it simple: / Interactive Generators / representing naughts and crosses as a stateless function

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01895))_

> We could plays naughts and crosses as a stateless function. We encode each position of the board in some fashion, and then we build a dictionary from positions to moves. For example, the entry for:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01900))_

<a id="atom-technical-atom-c92f013bd6aab97d"></a>

> [Figure] (p.276)

### Technical atom 81

<a id="atom-technical-atom-e477122c10f17b08"></a>

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01823))_

> Christine quickly scribbled on the whiteboard:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01825))_

```text
95 http://babeljs.io
96 http://www.es6fiddle.net
```

<details>
<summary>Parsed table preview (needs review)</summary>

| entry | content |
| --- | --- |
| 95 | http://babeljs.io |
| 96 | http://www.es6fiddle.net |

</details>
