---
page_id: javascriptallonge-third
page_kind: concept
summary: Third: 5 statement(s) and 2 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-third@035ff7a58dde969d2e02c77f11a829f2
---

# Third

What [[javascriptallonge]] covers about third:

## Statements

### value types

- Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the difference between them. This is the case with the strings, numbers, and booleans we have seen so far. _(javascriptallonge.pdf (source-range-8eb13d6b-00128))_

### if functions without free variables are pure, are closures impure?

- The first function doesn't have any variables, therefore doesn't have any free variables. The second doesn't have any free variables, because its only variable is bound. The third one is actually two functions, one inside the other. (y) => ... has a free variable, but the entire expression refers to (x) => ... , and it doesn't have a free variable: The only variable anywhere in its body is x , which is certainly bound within (x) => ... . _(javascriptallonge.pdf (source-range-8eb13d6b-00351))_

### inside-out

- The third one is easiest for most people to read. It separates concerns nicely: The 'outer' function describes its parameters: _(javascriptallonge.pdf (source-range-8eb13d6b-00406))_

### truthiness and the ternary operator

- The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example: _(javascriptallonge.pdf (source-range-8eb13d6b-00773))_

### tail-call optimization

- There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away. _(javascriptallonge.pdf (source-range-8eb13d6b-00970))_


## Technical atoms

### Technical frame 1: truthiness and the ternary operator

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00775))_

> Wecertainly don't want JavaScript trying to evaluate deleteRecord(currentRecord) unless isAuthorized(currentUser) returns true .

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00774))_

```
const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den';
```

### Technical frame 2: tail-call optimization

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-00970))_

> There are three places it returns. The first two don't return anything, they don't matter. But the third is fn.apply(this, args) . This is a tail-call, because it invokes another function and returns its result. This is interesting, because after sorting out what to supply as arguments ( this , args ), JavaScript can throw away everything in its current stack frame. It isn't going to do any more work, so it can throw its existing stack frame away.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-00969))_

```
const maybe = (fn) => function (...args) { if (args.length === 0) { return ; } else { for ( let arg of args) { if (arg == null ) return ; } return fn.apply( this , args); } }
```


## Related pages

- [[javascriptallonge-expression]] - shared statements and technical atoms: Expression shares source evidence from truthiness and the ternary operator: The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:; Expression shares technical record from truthiness and the ternary operator: const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-second]] - shared statements and technical atoms: Second shares source evidence from truthiness and the ternary operator: The fact that either the second or the third (but not both) expressions are evaluated can have important repercussions. Consider this hypothetical example:; Second shares technical record from truthiness and the ternary operator: const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-evaluate]] - shared technical atoms: Evaluate shares technical record from truthiness and the ternary operator: const status = isAuthorized(currentUser) ? deleteRecord(currentRecord) : 'Forbid\ den'; (1 shared atom(s))
- [[javascriptallonge-function]] - shared technical atoms: Function shares technical record from tail-call optimization: const maybe = (fn) => function (...args) { if (args.length === 0) { return ; } else { for ( let arg of args) { if (arg == null ) return ; } return fn.apply( this , args); } } (1 shared atom(s))
- [[javascriptallonge-type]] - shared statements: Type shares source evidence from value types: Third, some types of cups have no distinguishing marks on them. If they are the same kind of cup, and they hold the same contents, we have no way to tell the differe ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
