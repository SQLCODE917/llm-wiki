---
page_id: javascriptallonge-tortoise-hare
page_kind: concept
summary: Tortoise Hare: 1 statement(s) and 0 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-tortoise-hare@b0873d8791acc702510869397d13d708
---

# Tortoise Hare

What [[javascriptallonge]] covers about tortoise hare:

## Statements

### Tortoises, Hares, and Teleporting Turtles

- Composing and Decomposing Data

142 } } **const** tortoiseAndHare = (aPair) => { **let** tortoisePair = aPair, harePair = aPair.rest; **while** ( **true** ) { **if** (isEmpty(tortoisePair) || isEmpty(harePair)) { **return false** ; } **if** (tortoisePair.first === harePair.first) { **return true** ; } harePair = harePair.rest; **if** (isEmpty(harePair)) { **return false** ; } **if** (tortoisePair.first === harePair.first) { **return true** ; } tortoisePair = tortoisePair.rest; harePair = harePair.rest; } }; **const** aList = list(1, 2, 3, 4, 5); tortoiseAndHare(aList) _//=> false_ forceAppend(aList, aList.rest.rest); tortoiseAndHare(aList);

_//=> true_

This algorithm is called “The Tortoise and the Hare,” and was discovered by Robert Floyd in the 1960s. You have two node references, and one traverses the list at twice the speed of the other. No matter how large it is, you will eventually have the fast reference equal to the slow reference, and thus you’ll detect the loop. _(javascriptallonge.pdf (source-range-83ecb080-00196))_


## Related pages

- [[javascriptallonge-algorithm]] - shared statements: Algorithm shares source evidence from Tortoises, Hares, and Teleporting Turtles: Composing and Decomposing Data  142 } } **const** tortoiseAndHare = (aPair) => { **let** tortoisePair = aPair, harePair = aPair.rest; **while** ( **true** ) { **if** ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
