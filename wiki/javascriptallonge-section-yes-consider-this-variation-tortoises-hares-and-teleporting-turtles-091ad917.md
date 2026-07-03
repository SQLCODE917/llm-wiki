---
page_id: javascriptallonge-section-yes-consider-this-variation-tortoises-hares-and-teleporting-turtles-091ad917
page_kind: source
page_family: section-reference
summary: Yes. Consider this variation: / Tortoises, Hares, and Teleporting Turtles: 13 source-backed entries and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-07-02
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-yes-consider-this-variation-tortoises-hares-and-teleporting-turtles-091ad917@8f295611753a53412aee063e1c006e77
---

# Yes. Consider this variation: / Tortoises, Hares, and Teleporting Turtles

From [[javascriptallonge]].

## Related pages

### Source structure

- [[javascriptallonge-section-yes-consider-this-variation-b8b28d41]] - broader source section: Yes. Consider this variation:

## Statements

- A good long while ago (The First Age of Internet Startups), someone asked me one of those pet algorithm questions. It was, 'Write an algorithm to detect a loop in a linked list, in constant space.' _(javascriptallonge.pdf (source-range-7239e085-01258))_
- I think I told him that I was trying to figure out if I could adapt a hashing algorithm such as XORing everything together. This is the 'trick answer' to a question about finding a missing integer from a list, so I was trying the old, 'Transform this into a problem you've already solved 74 ' meta-algorithm. We moved on from there, and he didn't reveal the 'solution.' _(javascriptallonge.pdf (source-range-7239e085-01260))_
- I went home and pondered the problem. I wanted to solve it. Eventually, I came up with something and tried it (In Java!) on my home PC. I sent him an email sharing my result, to demonstrate my ability to follow through. I then forgot about it for a while. Some time later, I was told that the correct solution was: _(javascriptallonge.pdf (source-range-7239e085-01261))_
- This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-7239e085-01265))_
- Years later, I came across a discussion of this algorithm, The Tale of the Teleporting Turtle 75 . It seems to be faster under certain circumstances, depending on the size of the loop and the relative costs of certain operations. _(javascriptallonge.pdf (source-range-7239e085-01268))_
- What's interesting about these two algorithms is that they both tangle two separate concerns: How to traverse a data structure, and what to do with the elements that you encounter. In Functional Iterators, we'll investigate one pattern for separating these concerns. _(javascriptallonge.pdf (source-range-7239e085-01269))_
- This algorithm is called 'The Tortoise and the Hare,' and was discovered by Robert Floyd in the 1960s. _(javascriptallonge.pdf (source-range-7239e085-01265))_
- No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you'll detect the loop. _(javascriptallonge.pdf (source-range-7239e085-01265))_
