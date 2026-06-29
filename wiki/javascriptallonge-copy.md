---
page_id: javascriptallonge-copy
page_kind: concept
summary: Copy: 8 statement(s) and 13 atom(s) from raw/javascriptallonge.pdf.
sources: raw/javascriptallonge.pdf
updated: 2026-06-29
domain: javascriptallonge
category_path: concepts
projection_coverage: topic-javascriptallonge-copy@dc882a58123ae2f35c8d567243e9a809
---

# Copy

What [[javascriptallonge]] covers about copy:

## Statements

### ECMAScript 6 has three major groups of features: / Forewords to the First Edition / michael fogus

- As a life-long bibliophile and long-time follower of Reg's online work, I was excited when he started writing books. However, I'm very conservative about books - let's just say that if there was an aftershave scented to the essence of 'Used Book Store' then I would be first in line to buy. So as you might imagine I was 'skeptical' about the decision to release JavaScript Allongé as an ongoing ebook, with a pay-what-you-want model. However, Reg sent me a copy of his book and I was humbled. Not only was this a great book, but it was also a great way to write and distribute books. Having written books myself, I know the pain of soliciting and receiving feedback. _(javascriptallonge.pdf (source-range-7239e085-00084))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere

- The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it is using. Lather, rinse, repeat: Ever time we call mapWith , we're creating a new array, copying all the elements from prepend into the new array, and then we no longer use prepend . _(javascriptallonge.pdf (source-range-7239e085-01022))_

### Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays

- Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained later in Mutation). _(javascriptallonge.pdf (source-range-7239e085-01057))_

### Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

- The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return. _(javascriptallonge.pdf (source-range-7239e085-01111))_

### Composing and Decomposing Data / Mutation / building with mutation

- As noted, one pattern is to be more liberal about mutation when building a data structure. Consider our copy algorithm. Without mutation, a copy of a linked list can be made in constant space by reversing a reverse of the list: _(javascriptallonge.pdf (source-range-7239e085-01153))_

### Yes. Consider this variation: / Copy on Write / copy-on-write

- This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:' _(javascriptallonge.pdf (source-range-7239e085-01252))_

- Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) copy of that information to prevent its changes from becoming visible to all the other tasks.Wikipedia 73 _(javascriptallonge.pdf (source-range-7239e085-01253))_

- Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liberal with mutation. Once we're done with it and give it to someone else, we need to be conservative and use a strategy like copy-on-read or copy-on-write. _(javascriptallonge.pdf (source-range-7239e085-01255))_


## Technical atoms

### Technical frame 1: Composing and Decomposing Data / Garbage, Garbage Everywhere / some history

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01047))_

> Again, it's just extracting a reference from a cons cell, it's very fast. In Lisp, it's blazingly fast because it happens in hardware. There's no making copies of arrays, the time to cdr a list with five elements is the same as the time to cdr a list with 5,000 elements, and no temporary arrays are needed. In JavaScript, it's still much, much, much faster to get all the elements except the head from a linked list than from an array. Getting one reference to a structure that already exists is fas

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01046))_

```
cdr(oneToFive)
//=> [2,[3,[4,[5,null]]]]
```

### Technical frame 2: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01109))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01107))_

```
In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first:
2, rest: { first: 3, rest: EMPTY } } }.
We can then perform the equivalent of [first, ...rest] with direct property accessors:
```

### Technical frame 3: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01109))_

> What about mapping? Well, let's start with the simplest possible thing, making a copy of a list. As we saw above, and discussed in Garbage, Garbage Everywhere, it is fast to iterate forward through a linked list. What isn't fast is naïvely copying a list:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01108))_

```
const EMPTY = {};
const OneTwoThree = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY \
} } };
OneTwoThree.first
//=> 1
OneTwoThree.rest
//=> {"first":2,"rest":{"first":3,"rest":{}}}
OneTwoThree.rest.rest.first
//=> 3
Taking the length of a linked list is easy:
const length = (node, delayed = 0) =>
node === EMPTY
? delayed
: length(node.rest, delayed + 1);
length(OneTwoThree)
//=> 3
```

### Technical frame 4: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01111))_

> The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the call stack and then construct the list from back-to-front as all the recursive calls return.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01110))_

```
const slowcopy = (node) =>
node === EMPTY
? EMPTY
: { first: node.first, rest: slowcopy(node.rest)};
slowcopy(OneTwoThree)
//=> {"first":1,"rest":{"first":2,"rest":{"first":3,"rest":{}}}}
```

### Technical frame 5: Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01116))_

> Our mapWith function takes twice as long as a straight iteration, because it iterates over the entire list twice, once to map, and once to reverse the list. Likewise, it takes twice as much memory, because it constructs a reverse of the desired result before throwing it away.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01115))_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
And now, we can make a reversing map:
const reverseMapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverseMapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
reverseMapWith((x) => x * x, OneTwoThree)
//=> {"first":9,"rest":{"first":4,"rest":{"first":1,"rest":{}}}}
And a regular mapWith follows:
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const mapWith = (fn, node, delayed = EMPTY) =>
node === EMPTY
? reverse(delayed)
: mapWith(fn, node.rest, { first: fn(node.first), rest: delayed });
mapWith((x) => x * x, OneTwoThree)
//=> {"first":1,"rest":{"first":4,"rest":{"first":9,"rest":{}}}}
```

### Technical frame 6: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01155))_

> If we want to make a copy of a linked list without iterating over it twice and making a copy we discard later, we can use mutation:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01154))_

```
const reverse = (node, delayed = EMPTY) =>
node === EMPTY
? delayed
: reverse(node.rest, { first: node.first, rest: delayed });
const copy = (node) => reverse(reverse(node));
```

### Technical frame 7: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01157))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01156))_

```
const copy = (node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first, rest };
return copy(rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first, rest };
tail.rest = newNode;
return copy(node.rest, head, newNode);
}
}
```

### Technical frame 8: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01157))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01159))_

```
const mapWith = (fn, node, head = null, tail = null) => {
if (node === EMPTY) {
return head;
}
else if (tail === null) {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
return mapWith(fn, rest, newNode, newNode);
}
else {
const { first, rest } = node;
const newNode = { first: fn(first), rest };
tail.rest = newNode;
return mapWith(fn, node.rest, head, newNode);
}
}
mapWith((x) => 1.0 / x, OneToFive)
```

### Technical frame 9: Composing and Decomposing Data / Mutation / building with mutation

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01157))_

> This algorithm makes copies of nodes as it goes, and mutates the last node in the list so that it can splice the next one on. Adding a node to an existing list is risky, as we saw when considering the fact that OneToFive and ThreeToFive share the same nodes. But when we're in the midst of creating a brand new list, we aren't sharing any nodes with any other lists, and we can afford to be more liberal about using mutation to save space and/or time.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01160))_

```
//=> {"first":1,"rest":{"first":0.5,"rest":{"first":0.3333333333333333,"rest":\
{"first":0.25,"rest":{"first":0.2,"rest":{}}}}}}
```

### Technical frame 10: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01249))_

> But our new parent and child lists are copies that contain the desired modifications, without interfering with each other:

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01246))_

```
const rest = ({first, rest}) => rest;
const set = (index, value, list) =>
index === 0
? { first: value, rest: list.rest }
: { first: list.first, rest: set(index - 1, value, list.rest) };
const parentList = { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY }\
}};
const childList = rest(parentList);
const newParentList = set(2, "three", parentList);
const newChildList = set(0, "two", childList);
```

### Technical frame 11: Yes. Consider this variation: / Copy on Write / copy-on-write

**Context:** _(javascriptallonge.pdf (source-range-7239e085-01251))_

> And now functions like mapWith that make copies without modifying anything, work at full speed.

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-01250))_

```
newParentList
//=> {"first":1,"rest":{"first":2,"rest":{"first":"three","rest":{"first":{},"\
rest":{}}}}}
newChildList
//=> {"first":"two","rest":{"first":3,"rest":{"first":{},"rest":{}}}}
```

### Technical atom 12

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-02011))_

| entry | content |
| --- | --- |
| 106 | http://www.flickr.com/photos/trumpetca/ http://creativecommons.org/licenses/by/2.0/deed.en |
| 107 | http://www.flickr.com/photos/avlxyz/4907262046 |
| 108 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 109 | http://www.flickr.com/photos/digitalcolony/5054568279/ |
| 110 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 111 | http://www.flickr.com/photos/everydaylifemodern/1353570874/ |
| 112 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 113 | http://www.flickr.com/photos/everydaylifemodern/434299813/ |
| 114 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 115 | http://www.flickr.com/photos/the_rev/2295096211/ |
| 116 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 117 | http://www.flickr.com/photos/thedigitelmyr/6199419022/ |
| 118 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 119 | http://www.flickr.com/photos/sagamiono/4391542823/ |
| 120 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 121 | http://www.flickr.com/photos/digitalcolony/3924227011/ |
| 122 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 123 | http://www.flickr.com/photos/15481483@N06/6231443466/ |
| 124 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 125 | http://www.flickr.com/photos/tjgfernandes/2785677276/ |
| 126 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 127 | http://www.flickr.com/photos/kirstenloza/4805716699/ |
| 128 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 129 | http://www.flickr.com/photos/jenny-pics/5053954146/ 130 |

<details>
<summary>Raw table text</summary>

```
106 http://www.flickr.com/photos/trumpetca/
http://creativecommons.org/licenses/by/2.0/deed.en
107 http://www.flickr.com/photos/avlxyz/4907262046 108 http://creativecommons.org/licenses/by-sa/2.0/deed.en 109 http://www.flickr.com/photos/digitalcolony/5054568279/ 110 http://creativecommons.org/licenses/by-sa/2.0/deed.en 111 http://www.flickr.com/photos/everydaylifemodern/1353570874/ 112 http://creativecommons.org/licenses/by-nd/2.0/deed.en 113 http://www.flickr.com/photos/everydaylifemodern/434299813/ 114 http://creativecommons.org/licenses/by-nd/2.0/deed.en 115 http://www.flickr.com/photos/the_rev/2295096211/ 116 http://creativecommons.org/licenses/by/2.0/deed.en 117 http://www.flickr.com/photos/thedigitelmyr/6199419022/ 118 http://creativecommons.org/licenses/by-sa/2.0/deed.en 119 http://www.flickr.com/photos/sagamiono/4391542823/ 120 http://creativecommons.org/licenses/by-sa/2.0/deed.en 121 http://www.flickr.com/photos/digitalcolony/3924227011/ 122 http://creativecommons.org/licenses/by-sa/2.0/deed.en 123 http://www.flickr.com/photos/15481483@N06/6231443466/ 124 http://creativecommons.org/licenses/by-sa/2.0/deed.en 125 http://www.flickr.com/photos/tjgfernandes/2785677276/ 126 http://creativecommons.org/licenses/by/2.0/deed.en 127 http://www.flickr.com/photos/kirstenloza/4805716699/ 128 http://creativecommons.org/licenses/by/2.0/deed.en 129 http://www.flickr.com/photos/jenny-pics/5053954146/ 130
```

</details>

### Technical atom 13

**Atom:** _(javascriptallonge.pdf (source-range-7239e085-02045))_

| entry | content |
| --- | --- |
| 163 | http://www.flickr.com/photos/93425126@N00/313053257/ |
| 164 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 165 | http://www.flickr.com/photos/digitalcolony/2833809436/ |
| 166 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 167 | http://www.flickr.com/photos/citizenhelder/5006498068/ |
| 168 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 169 | http://www.flickr.com/photos/joncrel/237026246/ |
| 170 | http://creativecommons.org/licenses/by-nd/2.0/deed.en |
| 171 | http://www.flickr.com/photos/nalundgaard/3163852170/ |
| 172 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 173 | http://www.flickr.com/photos/47000103@N05/6525288841/ |
| 174 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 175 | http://www.flickr.com/photos/lotzman/978418891/ |
| 176 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 177 | http://www.flickr.com/photos/kk/sets/72157626168201654/with/5484839102/ |
| 178 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 179 | https://www.flickr.com/photos/kellan/434503323 |
| 180 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 181 | https://www.flickr.com/photos/whitneyinchicago/3835218626 |
| 182 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 183 | https://www.flickr.com/photos/sankarshan/5165312159 |
| 184 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 185 | https://www.flickr.com/photos/candy-s/7619358284 |
| 186 | https://www.flickr.com/photos/candy-s/ |
| 187 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 188 | https://www.flickr.com/photos/lorentey/22193876 |
| 189 | https://www.flickr.com/photos/lorentey/ |
| 190 | http://creativecommons.org/licenses/by/2.0/deed.en |
| 191 | https://www.flickr.com/photos/kk/5484876862 |
| 192 | http://creativecommons.org/licenses/by-sa/2.0/deed.en |
| 193 | https://www.flickr.com/photos/f_mafra/2956649121 194 http://creativecommons.org/licenses/by-sa/2.0/deed.en coffee pots 195 (c) 2009 Jonas Forth Some rights reserved 196 . |
| 5 | Barrel Roaster 197 (c) 2013 David Lytle Some rights reserved 198 . |

<details>
<summary>Raw table text</summary>

```
163 http://www.flickr.com/photos/93425126@N00/313053257/ 164 http://creativecommons.org/licenses/by-sa/2.0/deed.en 165 http://www.flickr.com/photos/digitalcolony/2833809436/ 166 http://creativecommons.org/licenses/by-sa/2.0/deed.en 167 http://www.flickr.com/photos/citizenhelder/5006498068/ 168 http://creativecommons.org/licenses/by/2.0/deed.en 169 http://www.flickr.com/photos/joncrel/237026246/ 170 http://creativecommons.org/licenses/by-nd/2.0/deed.en 171 http://www.flickr.com/photos/nalundgaard/3163852170/ 172 http://creativecommons.org/licenses/by-sa/2.0/deed.en 173 http://www.flickr.com/photos/47000103@N05/6525288841/ 174 http://creativecommons.org/licenses/by-sa/2.0/deed.en 175 http://www.flickr.com/photos/lotzman/978418891/ 176 http://creativecommons.org/licenses/by/2.0/deed.en 177 http://www.flickr.com/photos/kk/sets/72157626168201654/with/5484839102/ 178 http://creativecommons.org/licenses/by-sa/2.0/deed.en 179 https://www.flickr.com/photos/kellan/434503323 180 http://creativecommons.org/licenses/by/2.0/deed.en 181 https://www.flickr.com/photos/whitneyinchicago/3835218626 182 http://creativecommons.org/licenses/by/2.0/deed.en 183 https://www.flickr.com/photos/sankarshan/5165312159 184 http://creativecommons.org/licenses/by-sa/2.0/deed.en 185 https://www.flickr.com/photos/candy-s/7619358284 186 https://www.flickr.com/photos/candy-s/ 187 http://creativecommons.org/licenses/by/2.0/deed.en 188 https://www.flickr.com/photos/lorentey/22193876 189 https://www.flickr.com/photos/lorentey/ 190 http://creativecommons.org/licenses/by/2.0/deed.en 191 https://www.flickr.com/photos/kk/5484876862 192 http://creativecommons.org/licenses/by-sa/2.0/deed.en 193 https://www.flickr.com/photos/f_mafra/2956649121 194
http://creativecommons.org/licenses/by-sa/2.0/deed.en
coffee pots 195 (c) 2009 Jonas Forth Some rights reserved 196 .
5 Barrel Roaster 197 (c) 2013 David Lytle Some rights reserved 198 .
```

</details>


## Related pages

- [[javascriptallonge-copy-write]] - narrower topic: Copy on Write shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: This strategy of waiting to copy until you are writing is called copy-on-write, or 'COW:'; Copy on Write shares technical record from Yes. Consider this variation: / Copy on Write / copy-on-write: const rest = ({first, rest}) => rest; const set = (index, value, list) => index === 0 ? { first: value, rest: list.rest } : { first: list.first, rest: set(index - 1, ... [truncated] (3 shared statement(s), 2 shared atom(s))
- [[javascriptallonge-list]] - shared statements and technical atoms: List shares source evidence from Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists: The problem here is that linked lists are constructed back-to-front, but we iterate over them frontto-back. So to copy a list, we have to save all the bits on the ca ... [truncated]; List shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 9 shared atom(s))
- [[javascriptallonge-element]] - shared statements and technical atoms: Element shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated]; Element shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (2 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-reference]] - shared statements and technical atoms: Reference shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated]; Reference shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared statement(s), 1 shared atom(s))
- [[javascriptallonge-instead]] - shared technical atoms: Instead shares technical record from Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists: In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } }. We can then perform th ... [truncated] (2 shared atom(s))
- [[javascriptallonge-object]] - shared technical atoms: Object shares technical record from Composing and Decomposing Data / Plain Old JavaScript Objects / revisiting linked lists: In that case, a linked list of the numbers 1, 2, and 3 will look like this: { first: 1, rest: { first: 2, rest: { first: 3, rest: EMPTY } } }. We can then perform th ... [truncated] (2 shared atom(s))
- [[javascriptallonge-rest]] - shared technical atoms: Rest shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (2 shared atom(s))
- [[javascriptallonge-algorithm]] - shared technical atoms: Algorithm shares technical record from Composing and Decomposing Data / Mutation / building with mutation: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node)); (1 shared atom(s))
- [[javascriptallonge-coffee]] - shared technical atoms: Coffee shares technical table: 163 http://www.flickr.com/photos/93425126@N00/313053257/ 164 http://creativecommons.org/licenses/by-sa/2.0/deed.en 165 http://www.flickr.com/photos/digitalcolony/283 ... [truncated] (1 shared atom(s))
- [[javascriptallonge-javascript]] - shared technical atoms: Javascript shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-note]] - shared technical atoms: Note shares technical record from Composing and Decomposing Data / Mutation / building with mutation: const reverse = (node, delayed = EMPTY) => node === EMPTY ? delayed : reverse(node.rest, { first: node.first, rest: delayed }); const copy = (node) => reverse(reverse(node)); (1 shared atom(s))
- [[javascriptallonge-structure]] - shared technical atoms: Structure shares technical record from Composing and Decomposing Data / Garbage, Garbage Everywhere / some history: cdr(oneToFive) //=> [2,[3,[4,[5,null]]]] (1 shared atom(s))
- [[javascriptallonge-write]] - shared statements: Write shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Copy-on-write is the name given to the policy that whenever a task attempts to make a change to the shared information, it should first create a separate (private) c ... [truncated] (2 shared statement(s))
- [[javascriptallonge-code]] - shared statements: Code shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-follow]] - shared statements: Follow shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-function]] - shared statements: Function shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-mapwith]] - shared statements: Mapwith shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere: The array we had in prepend is no longer used. In GC environments, it is marked as no longer being used, and eventually the garbage collector recycles the memory it ... [truncated] (1 shared statement(s))
- [[javascriptallonge-pattern]] - shared statements: Pattern shares source evidence from Yes. Consider this variation: / Copy on Write / copy-on-write: Looking at the code again, you see that the copy function doesn't copy on write: It follows the pattern that while constructing something, we own it and can be liber ... [truncated] (1 shared statement(s))
- [[javascriptallonge-problem]] - shared statements: Problem shares source evidence from Composing and Decomposing Data / Garbage, Garbage Everywhere / so why arrays: Arrays avoid this problem by pessimistically copying all the references whenever we extract an element or sequence of elements from them (We'll see this explained la ... [truncated] (1 shared statement(s))

## Source

- [[javascriptallonge]]
