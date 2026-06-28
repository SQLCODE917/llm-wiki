---
page_id: javascriptallonge-truthiness
page_kind: concept
summary: Truthiness: 2 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-truthiness@e769782399e4908ab2991dc20009123e
---

# Truthiness

What [[javascriptallonge]] covers about truthiness:

## Statements

### truthiness and the ternary operator

- In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that semantically represent 'no value.' NaN is falsy, a value representing the result of a calculation that is not a number. 54 And there are more: 0 is falsy, a value representing 'none of something.' The empty string, '' is falsy, a value representing having no characters. _(javascriptallonge.pdf (source-range-31a4cf47-00765))_

- The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This affects the way the ! , && , and || operators work. We'll look at them in a moment, but first, we'll look at one more operator. _(javascriptallonge.pdf (source-range-31a4cf47-00767))_


## Related pages

- [[javascriptallonge-javascript]] - shared statements: Javascript shares source evidence from truthiness and the ternary operator: In JavaScript, there is a notion of 'truthiness.' Every value is either 'truthy' or 'falsy.' Obviously, false is falsy. So are null and undefined , values that seman ... [truncated] (1 shared statement(s))
- [[javascriptallonge-matter]] - shared statements: Matter shares source evidence from truthiness and the ternary operator: The reason why truthiness matters is that the various logical operators (as well as the if statement) actually operate on truthiness , not on boolean values. This af ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
