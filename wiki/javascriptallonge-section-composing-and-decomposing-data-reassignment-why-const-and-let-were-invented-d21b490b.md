---
page_id: javascriptallonge-section-composing-and-decomposing-data-reassignment-why-const-and-let-were-invented-d21b490b
page_kind: source
summary: Composing and Decomposing Data / Reassignment / why const and let were invented: 12 source-backed entries and 1 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-composing-and-decomposing-data-reassignment-why-const-and-let-were-invented-d21b490b@458071908b20841d727162dd8c5435a9
---

# Composing and Decomposing Data / Reassignment / why const and let were invented

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-section-composing-and-decomposing-data-reassignment-5040fcae]] - broader source section: Composing and Decomposing Data / Reassignment

## Statements

- const and let are recent additions to JavaScript. For nearly twenty years, variables were declared with var (not counting parameters and function declarations, of course). However, its functional scope was a problem. _(javascriptallonge.pdf (source-range-7239e085-01202))_
- We haven't looked at it yet, but JavaScript provides a for loop for your iterating pleasure and convenience. It looks a lot like the for loop in C. Here it is with var : _(javascriptallonge.pdf (source-range-7239e085-01203))_
- Hopefully, you can think of a faster way to calculate this sum. 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem? _(javascriptallonge.pdf (source-range-7239e085-01205))_
- 72 There is a well known story about Karl Friedrich Gauss when he was in elementary school. His teacher got mad at the class and told them to add the numbers 1 to 100 and give him the answer by the end of the class. About 30 seconds later Gauss gave him the answer. The other kids were adding the numbers like this: 1 + 2 + 3 + . . . . + 99 + 100 = ? But Gauss rearranged the numbers to add them like this: (1 + 100) + (2 + 99) + (3 + 98) + . . . . + (50 + 51) = ? If you notice every pair of numbers adds up to 101. There are 50 pairs of numbers, so the answer is 50*101 = 5050. Of course Gauss came up with the answer about 20 times faster than the other kids. _(javascriptallonge.pdf (source-range-7239e085-01206))_

## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Reassignment / why const and let were invented

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01205))_

> Hopefully, you can think of a faster way to calculate this sum. 72 And perhaps you have noticed that var i = 1 is tucked away instead of being at the top as we prefer. But is this ever a problem?

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01204))_

```
var sum = 0;
for (var i = 1; i <= 100; i++) {
sum = sum + i
}
sum
#=> 5050
```
