---
page_id: javascriptallonge-section-mutation-4ba5b6e2
page_kind: source
summary: Mutation: 27 source-backed entries and 10 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-28
domain: javascriptallonge
category_path: sources/javascriptallonge/sections
source_id: javascriptallonge.pdf
projection_coverage: section-javascriptallonge-section-mutation-4ba5b6e2@b6934f782450dab32a19390d55af996b
---

# Mutation

From [[javascriptallonge]].

## Related pages

- [[javascriptallonge-mutation]] - topic hub: opens the topic page for Mutation

## Statements

- In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = : _(javascriptallonge.pdf (source-range-8eb13d6b-01120))_
- Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example: _(javascriptallonge.pdf (source-range-8eb13d6b-01126))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. And also: _(javascriptallonge.pdf (source-range-8eb13d6b-01128))_
- There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two aliases for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-8eb13d6b-01130))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we mutate the value in the inner environment? _(javascriptallonge.pdf (source-range-8eb13d6b-01133))_
- This is different. We haven't rebound the inner name to a different variable, we've mutated the value that both bindings share. Now that we've finished with mutation and aliases, let's have a look at it. _(javascriptallonge.pdf (source-range-8eb13d6b-01135))_
- JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value. _(javascriptallonge.pdf (source-range-8eb13d6b-01137))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction. _(javascriptallonge.pdf (source-range-8eb13d6b-01139))_
- Recall that you can access a value from within an array or an object using [] . _(javascriptallonge.pdf (source-range-8eb13d6b-01120))_
- Both halloween and allHallowsEve are bound to the same array value within the local environment. _(javascriptallonge.pdf (source-range-8eb13d6b-01128))_
- Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value. _(javascriptallonge.pdf (source-range-8eb13d6b-01130))_
- The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. _(javascriptallonge.pdf (source-range-8eb13d6b-01133))_
- Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. _(javascriptallonge.pdf (source-range-8eb13d6b-01139))_

## Technical atoms

### Technical frame 1: Mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01120))_

> In JavaScript, almost every type of value can mutate . Their identities stay the same, but not their structure. Specifically, arrays and objects can mutate. Recall that you can access a value from within an array or an object using [] . You can reassign a value using [] = :

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01118))_

> [Figure] (p.141)

### Technical frame 2: Mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01126))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01121))_

```
const oneTwoThree = [1, 2, 3]; oneTwoThree[0] = 'one'; oneTwoThree //=> [ 'one', 2, 3 ]
```

### Technical frame 3: Mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01126))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01123))_

```
const oneTwoThree = [1, 2, 3]; oneTwoThree[3] = 'four'; oneTwoThree //=> [ 1, 2, 3, 'four' ]
```

### Technical frame 4: Mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01126))_

> Wehave established that JavaScript's semantics allow for two different bindings to refer to the same value. For example:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01125))_

```
const name = {firstName: 'Leonard', lastName: 'Braithwaite'}; name.middleName = 'Austin' name //=> { firstName: 'Leonard', # lastName: 'Braithwaite', # middleName: 'Austin' }
```

### Technical frame 5: Mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01128))_

> Both halloween and allHallowsEve are bound to the same array value within the local environment. And also:

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01127))_

```
const allHallowsEve = [2012, 10, 31] const halloween = allHallowsEve;
```

### Technical frame 6: Mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01130))_

> There are two nested environments, and each one binds a name to the exact same array value. In each of these examples, we have created two aliases for the same value. Before we could reassign things, the most important point about this is that the identities were the same, because they were the same value.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01129))_

```
const allHallowsEve = [2012, 10, 31]; ( function (halloween) { // ... })(allHallowsEve);
```

### Technical frame 7: Mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01133))_

> The outer value of allHallowsEve was not changed because all we did was rebind the name halloween within the inner environment. However, what happens if we mutate the value in the inner environment?

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01132))_

```
const allHallowsEve = [2012, 10, 31]; ( function (halloween) { halloween = [2013, 10, 31]; })(allHallowsEve); allHallowsEve //=> [2012, 10, 31]
```

### Technical frame 8: Mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01135))_

> This is different. We haven't rebound the inner name to a different variable, we've mutated the value that both bindings share. Now that we've finished with mutation and aliases, let's have a look at it.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01134))_

```
const allHallowsEve = [2012, 10, 31]; ( function (halloween) { halloween[0] = 2013; })(allHallowsEve); allHallowsEve //=> [2013, 10, 31]
```

### Technical frame 9: Mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01137))_

> JavaScript permits the reassignment of new values to existing bindings, as well as the reassignment and assignment of new values to elements of containers such as arrays and objects. Mutating existing objects has special implications when two bindings are aliases of the same value.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01136))_

> [Figure] (p.143)

### Technical frame 10: Mutation

**Context:** _(javascriptallonge.pdf (source-range-8eb13d6b-01139))_

> Note well: Declaring a variable const does not prevent us from mutating its value, only from rebinding its name. This is an important distinction.

**Atom:** _(javascriptallonge.pdf (source-range-8eb13d6b-01138))_

> [Figure] (p.143)
