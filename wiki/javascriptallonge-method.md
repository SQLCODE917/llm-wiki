---
page_id: javascriptallonge-method
page_kind: concept
summary: Method: 11 statement(s) and 4 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-27
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-method@13f48bf0a5056293101b89957d3aff0f
---

# Method

What [[javascriptallonge]] covers about method:

## Statements

- When we learn about context and methods, we’ll see that flip throws the current context away, so it can’t be used to flip methods. _(javascriptallonge.pdf (source-range-83ecb080-02270))_
- In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error. _(javascriptallonge.pdf (source-range-83ecb080-01411))_
- compact method syntax, but they are not relevant here. _(javascriptallonge.pdf (source-range-83ecb080-01623))_
- Now our .iterator() method is returning an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02410))_
- To ensure that the method would not conflict with any existing code, JavaScript provides a _symbol_ . _(javascriptallonge.pdf (source-range-83ecb080-02414))_
- The expression Symbol.iterator evaluates to a special symbol representing the name of the method that objects should use if they return an iterator object. _(javascriptallonge.pdf (source-range-83ecb080-02415))_
- Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done. _(javascriptallonge.pdf (source-range-83ecb080-02531))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack _(javascriptallonge.pdf (source-range-83ecb080-02738))_
- Some methods are only added to a few collections, some are added to all. _(javascriptallonge.pdf (source-range-83ecb080-02740))_
- And if we want to create convenience methods, we can reuse common pieces. _(javascriptallonge.pdf (source-range-83ecb080-02745))_
- Composing an iterable with a mapIterable method cleaves the responsibility for knowing how to map from the fiddly bits of how a linked list differs from a stack. _(javascriptallonge.pdf (source-range-83ecb080-02745))_

## Technical atoms

### Technical atom 1

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-01411))_

> In practice, using a method like this with more than about 50 items in an array may cause some implementations to run very slow, run out of memory and freeze, or cause an error.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-01412))_

> mapWith((x) => x * x, [

### Technical atom 2

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02531))_

> Let’s consider how they work. Whether it’s a simple functional iterator, or an iterable object with a .next() method, an iterator is something we call repeatedly until it tells us that it’s done.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02532))_

> Iterators have to arrange its own state such that when you call them, they compute and return the next item.

### Technical atom 3

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02658))_

> Now we can use it in a for...of loop, spread it into an array literal, or spread it into a function invocation, because we have written an iterable that uses a generator to return an iterator from its [Symbol.iterator] method.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02656))_

> **const** iterator = ThreeNumbers[Symbol.iterator]();

### Technical atom 4

**Context:** _(javascriptallonge.pdf (source-range-83ecb080-02662, source-range-83ecb080-02664))_

> generator methods for objects: This object declares a [Symbol.iterator] function that makes it iterable. Because it’s declared *[Symbol.iterator], it’s a generator instead of an iterator.

**Atom:** _(javascriptallonge.pdf (source-range-83ecb080-02663))_

> **const** ThreeNumbers = { *[Symbol.iterator] () { **yield** 1; **yield** 2; **yield** 3 } }


## Related pages

- [[javascriptallonge-iterator]] - shared statements and technical atoms (3 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-function]] - shared statements and technical atoms (1 shared statement(s), 3 shared atom(s))
- [[javascriptallonge-object]] - shared statements and technical atoms (2 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-iterable]] - shared technical atoms (2 shared atom(s))
- [[javascriptallonge-evaluate]] - shared statements (1 shared statement(s))
- [[javascriptallonge-expression]] - shared statements (1 shared statement(s))

## Source

- [[javascriptallonge]]
