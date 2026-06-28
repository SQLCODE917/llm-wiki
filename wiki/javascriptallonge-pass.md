---
page_id: javascriptallonge-pass
page_kind: concept
summary: Pass: 5 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-pass@74e2ac4abb0911f3501008c978aea760
---

# Pass

What [[javascriptallonge]] covers about pass:

## Statements

### truthiness and operators

- If we look at our examples above, we see that when we pass true and false to && and || , we do indeed get true or false as a result. But when we pass other values, we no longer get true or false : _(javascriptallonge.pdf (source-range-31a4cf47-00788))_

### destructuring is not pattern matching

- From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things. _(javascriptallonge.pdf (source-range-31a4cf47-00869))_

### caveat

- For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. _(javascriptallonge.pdf (source-range-31a4cf47-01324))_

### a return to backward thinking

- We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a way for list to call the code we pass in. _(javascriptallonge.pdf (source-range-31a4cf47-01416))_

- Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. _(javascriptallonge.pdf (source-range-31a4cf47-01422))_


## Technical atoms

### Technical frame 1: truthiness and operators

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00790))_

> In JavaScript, && and || aren't boolean logical operators in the logical sense. They don't operate strictly on logical values, and they don't commute: a || b is not always equal to b || a , and the same goes for && .

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00789))_

```
1 || 2 //=> 1 null && undefined //=> null undefined && null //=> undefined
```

### Technical frame 2: destructuring is not pattern matching

**Context:** _(javascriptallonge.pdf (source-range-31a4cf47-00869))_

> From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can to keep executing without failing. This often means that we must write our own code to detect failure conditions, as we cannot reply on the language to point out when we are doing semantically meaningless things.

**Atom:** _(javascriptallonge.pdf (source-range-31a4cf47-00867))_

```
const [...they] = []; they //=> [] const [which, what, they //=> []
```


## Related pages

- [[javascriptallonge-value]] - shared statements and technical atoms: Value shares source evidence from destructuring is not pattern matching: From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can ... [truncated]; Value shares technical record from truthiness and operators: 1 || 2 //=> 1 null && undefined //=> null undefined && null //=> undefined (1 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-result]] - shared statements and technical atoms: Result shares source evidence from destructuring is not pattern matching: From its very inception, JavaScript has striven to avoid catastrophic errors. As a result, it often coerces values, passes undefined around, or does whatever it can ... [truncated]; Result shares technical record from destructuring is not pattern matching: const [...they] = []; they //=> [] const [which, what, they //=> [] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-bind]] - shared technical atoms: Bind shares technical record from destructuring is not pattern matching: const [...they] = []; they //=> [] const [which, what, they //=> [] (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from destructuring is not pattern matching: const [...they] = []; they //=> [] const [which, what, they //=> [] (1 shared atom(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. (2 shared statement(s))
- [[javascriptallonge-directly]] - shared statements: Directly shares source evidence from a return to backward thinking: Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. (1 shared statement(s))
- [[javascriptallonge-instead]] - shared statements: Instead shares source evidence from a return to backward thinking: Instead of directly manipulating part of an entity, pass it a function and have it call our function with the part we want. (1 shared statement(s))
- [[javascriptallonge-iterator]] - shared statements: Iterator shares source evidence from caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. (1 shared statement(s))
- [[javascriptallonge-list]] - shared statements: List shares source evidence from a return to backward thinking: We're passing list what we want done with an empty list, and what we want done with a list that has at least one element. We then ask list to do it, and provide a wa ... [truncated] (1 shared statement(s))
- [[javascriptallonge-purpose]] - shared statements: Purpose shares source evidence from caveat: For all intents and purposes, once you pass an iterator to a function, you can expect that you no longer 'own' that iterator, and that its state either has changed or will change. (1 shared statement(s))

## Source

- [[javascriptallonge]]
