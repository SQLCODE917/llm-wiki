---
page_id: javascriptallonge-section-tortoises-hares-and-teleporting-turtles-5ba2545c
page_kind: source
summary: Tortoises, Hares, and Teleporting Turtles: 16 source-backed entries and 3 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-tortoises-hares-and-teleporting-turtles-5ba2545c@ff98273c4f71501332dad4d756f6a034
---

# Tortoises, Hares, and Teleporting Turtles

From [[javascriptallonge]].

## Statements

- It was, “Write an algorithm to detect a loop in a linked list, in constant space.” _(javascriptallonge.pdf (source-range-83ecb080-01906))_
- I’m not particularly surprised that I couldn’t think up an answer in a few minutes at the time. _(javascriptallonge.pdf (source-range-83ecb080-01907))_
- This is the “trick answer” to a question about finding a missing integer from a list, so I was trying the old, “Transform this into a problem you’ve already solved[74] ” meta-algorithm. _(javascriptallonge.pdf (source-range-83ecb080-01908))_
- Eventually, I came up with something and tried it (In Java!) on my home PC. _(javascriptallonge.pdf (source-range-83ecb080-01909))_
- I then forgot about it for a while. _(javascriptallonge.pdf (source-range-83ecb080-01909))_
- This algorithm is called “The Tortoise and the Hare,” and was discovered by Robert Floyd in the 1960s. _(javascriptallonge.pdf (source-range-83ecb080-01920))_
- You have two node references, and one traverses the list at twice the speed of the other. _(javascriptallonge.pdf (source-range-83ecb080-01920))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you’ll detect the loop. _(javascriptallonge.pdf (source-range-83ecb080-01920))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you’ll detect the loop. _(javascriptallonge.pdf (source-range-83ecb080-01920))_
- This algorithm is called “The Tortoise and the Hare,” and was discovered by Robert Floyd in the 1960s. _(javascriptallonge.pdf (source-range-83ecb080-01920))_
- At the time, I couldn’t think of any way to use hashing to solve the problem, so I gave up and tried to fit this into a powers-of-two algorithm. _(javascriptallonge.pdf (source-range-83ecb080-01923))_
- It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations. _(javascriptallonge.pdf (source-range-83ecb080-01926))_
- What’s interesting about these two algorithms is that they both _tangle_ two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. _(javascriptallonge.pdf (source-range-83ecb080-01927))_

## Technical atoms

> Context: I went home and pondered the problem. I wanted to solve it. Eventually, I came up with something and tried it (In Java!) on my home PC. I sent him an email sharing my result, to demonstrate my ability to follow through. I then forgot about it for a while. Some time later, I was told that the correct solution was:
_(context: javascriptallonge.pdf (source-range-83ecb080-01909))_

> **const** EMPTY = **null** ;
_(source: javascriptallonge.pdf (source-range-83ecb080-01910))_

> Context: I went home and pondered the problem. I wanted to solve it. Eventually, I came up with something and tried it (In Java!) on my home PC. I sent him an email sharing my result, to demonstrate my ability to follow through. I then forgot about it for a while. Some time later, I was told that the correct solution was:
_(context: javascriptallonge.pdf (source-range-83ecb080-01909))_

> **const** isEmpty = (node) => node === EMPTY;
_(source: javascriptallonge.pdf (source-range-83ecb080-01911))_

> Context: **const** teleportingTurtle = (list) => { **let** speed = 1, rabbit = list, turtle = rabbit; **while** ( **true** ) { **for** ( **let** i = 0; i <= speed; i += 1) { rabbit = rabbit.rest; **if** (rabbit == **null** ) { **return false** ; } **if** (rabbit === turtle) { **return true** ; } } turtle = rabbit; speed *= 2; } **return false** ; }; **const** aList = list(1, 2, 3, 4, 5); teleportingTurtle(aList) _//=> false_ forceAppend(aList, aList.rest.rest);
_(context: javascriptallonge.pdf (source-range-83ecb080-01924))_

> teleportingTurtle(aList); _//=> true_
_(source: javascriptallonge.pdf (source-range-83ecb080-01925))_
