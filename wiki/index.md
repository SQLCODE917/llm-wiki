# Index

One entry per page: `- [[page-name]] — one-line summary`. Maintained
automatically by the harness on every page write. See `SCHEMA.md`.

## Sources
- [[antikythera-mechanism]] — The oldest known analog computer, an ancient Greek device for tracking astronomical events.
- [[javascriptallonge]] — Hub page for JavaScript Allongé, summarizing the entire book and linking to chapter-specific source pages.
- [[javascriptallonge-as-little-as-possible-about-functions-but-no-less]] — JavaScript functions as values, reference types, and function application mechanics (pages 30-43).
- [[javascriptallonge-chapter-5]] — Explains JavaScript's const keyword, lexical scoping, and function binding patterns like IIFEs.
- [[javascriptallonge-closures-and-scope]] — JavaScript closures, scope chains, pure functions, and environment hierarchy (pages 44-48).
- [[javascriptallonge-composing-and-decomposing-data]] — Chapter on composing and decomposing data in JavaScript.
- [[javascriptallonge-copy-on-write]] — Explains copy-on-write strategy for linked lists vs arrays, structure sharing, and trade-offs with copy-on-read. Includes code examples and the tortoise-and-hare loop detection algorithm.
- [[javascriptallonge-copyright-notice]] — Copyright information for *JavaScript Allonge*, including authorship, image credits, and licensing details (raw/javascriptallonge.pdf p.293-297).
- [[javascriptallonge-forewords-to-the-first-edition]] — Forewords to the first edition of JavaScript Allongé by Michael Fogus and Matthew Knox, discussing the Leanpub model and book content.
- [[javascriptallonge-frontend]] — Front matter of JavaScript Allongé, including prefaces, table of contents, and author information.
- [[javascriptallonge-garbage-garbage-everywhere]] — Analysis of JavaScript array recursion inefficiency, comparison to Lisp's linked lists, and object-based cons cell implementations. sources: raw/javascriptallonge.pdf p.126-140
- [[javascriptallonge-generating-iterables]] — Updated to include interactive generators and stateful function examples from the Naughts and Crosses game.
- [[javascriptallonge-interactive-generators]] — Explores interactive generators for stateful functions, using Naughts and Crosses as an example, and operations on iterables (map, filter, zip, etc.).
- [[javascriptallonge-interlude-the-carpenter-interviews-for-a-job]] — A chapter where The Carpenter solves a cycle detection problem using iterables and Floyd's algorithm during a job interview.
- [[javascriptallonge-iteration-and-iterables]] — Updated to include iterable operations from the chunk: mapWith, filterWith, zip, zipWith, memoize, and reduceWith.
- [[javascriptallonge-lazy-eager-collections]] — Discusses lazy and eager collections in JavaScript, their implementations via iterators, and efficiency tradeoffs between on-demand computation and immediate data processing.
- [[javascriptallonge-making-data-out-of-functions]] — Explores using combinators (K, I, V) and functions to create data structures like lists and pairs, avoiding arrays/objects. Introduces mapWith and flip functions.
- [[javascriptallonge-mutation]] — JavaScript mutation mechanics: array/object mutation, aliases, const/let reassignment, and var pitfalls (pages 141-157).
- [[javascriptallonge-naming-functions]] — JavaScript function naming conventions, declarations, and combinators (pages 62-78).
- [[javascriptallonge-object-assign]] — JavaScript Object.assign method for shallow cloning and merging objects (pages 198-205).
- [[javascriptallonge-picking-the-bean]] — Chapter on picking the bean pattern in JavaScript.
- [[javascriptallonge-picking-the-bean-choice-and-truthiness]] — JavaScript's truthiness, logical operators (!, &&, ||), ternary operator, and control-flow semantics explained with examples.
- [[javascriptallonge-recipes-with-basic-functions]] — JavaScript functional programming recipes: partial application, unary functions, tap, maybe, once, and left-variadic functions.
- [[javascriptallonge-self-similarity]] — Chapter on self-similar data structures in JavaScript.

## Entities
- [[archimedes]] — Ancient Greek mathematician and engineer, known for inventions like the Archimedean screw and principles of buoyancy.
- [[axel-rauschmayer]] — Author of "Exploring ES6" and foreword for JavaScript Allongé's Six Edition.
- [[corinth]] — Ancient Greek city-state in the Peloponnese, known for its strategic location and historical significance.
- [[generator]] — A function that produces values via yield, enabling coroutine-like behavior in JavaScript.
- [[javascript]] — JavaScript features including closures, scope chains, and global environment isolation.
- [[matthew-knox]] — Software developer and author who praised JavaScript Allongé's exploration of JavaScript's depth.
- [[michael-fogus]] — Software developer and author known for advocating functional programming.
- [[nan]] — JavaScript value representing an invalid or undefined numerical result.
- [[node-js]] — JavaScript runtime environment for server-side and CLI applications.
- [[reg-raganwald-braithwaite]] — Reginald Braithwaite, software developer and author of *JavaScript Allonge*, known for functional programming and JavaScript.
- [[syracuse]] — Ancient Greek city-state in Sicily, renowned as the birthplace of Archimedes and a center of engineering.
- [[undefined]] — JavaScript value representing the absence of a defined value; distinct from SQL NULL.

## Concepts
- [[array-destructuring]] — Array destructuring creates a copy of elements, unlike linked list structure sharing which references the same nodes. See (raw/javascriptallonge.pdf p.158-176) for copy-on-write strategies.
- [[arrays]] — JavaScript arrays allow mutation via element reassignment even with `const`, and destructuring creates copies (unlike linked lists).
- [[call-by-value]] — JavaScript's evaluation strategy where arguments are evaluated before passing, with reference types sharing values (call-by-sharing).
- [[closure]] — A function or block that captures and retains references to variables from its lexical scope.
- [[combinator]] — Combinators like K (Kestrel), I (Idiot Bird), and V (Vireo) enable creating functions that manipulate data without arrays/objects. Used in functional programming for data structure creation.
- [[const]] — JavaScript's block-scoped variable declaration that prevents reassignment but allows shadowing in nested blocks.
- [[coroutine]] — A computational construct enabling suspension and resumption of execution, implemented via JavaScript generators.
- [[eager-evaluation]] — Describes eager evaluation in JavaScript, where operations on collections are processed immediately, creating new data structures at each step.
- [[ecmascript-2015]] — ECMAScript 2015 (ES6) language features and their impact on JavaScript.
- [[floating-point-numbers]] — JavaScript's representation of real numbers using IEEE 754 standard, with precision limitations.
- [[floyd-s-cycle-finding-algorithm]] — Algorithm for detecting cycles in a sequence using two pointers.
- [[function]] — JavaScript functions, pure functions, closures, and declaration hoisting.
- [[function-decorator]] — Higher-order functions that modify or wrap another function's behavior.
- [[functional-data-structures]] — Immutable data structures that persist previous states upon modification.
- [[functional-iterators]] — Iterators that process collections in a functional programming style.
- [[functional-programming]] — Functional programming concepts including closures and scope chains in JavaScript.
- [[iterable]] — Defines iterables in JavaScript via Symbol.iterator, with emphasis on generator-based implementations.
- [[lazy-evaluation]] — Evaluation strategy where expressions are evaluated only when needed.
- [[leanpub]] — A publishing platform enabling iterative book development with reader feedback.
- [[left-variadic-functions]] — Functions that accept a variable number of arguments on the left side of the call.
- [[lexical-scoping]] — JavaScript's mechanism for resolving variable names based on their position in the source code, rather than runtime context.
- [[linked-lists]] — JavaScript linked lists use structure sharing, where mutation of one alias affects all shared nodes. Contrast with array destructuring which creates copies. See (raw/javascriptallonge.pdf p.158-176) for copy-on-write strategies.
- [[logical-operators]] — JavaScript's logical operators (!, &&, ||) operate on truthiness, not strict booleans, with short-circuit evaluation.
- [[mapping]] — Applying a function to each element of a data structure.
- [[mapwith-and-flip]] — mapWith curries functions for data transformation, while flip reverses argument order. Both enable functional programming patterns in JavaScript.
- [[object-assign]] — JavaScript's Object.assign() method for shallow cloning and merging objects.
- [[object-destructuring]] — JavaScript object destructuring syntax and examples, including compact method syntax. sources: raw/javascriptallonge.pdf p.126-140
- [[ordered-collection]] — Describes ordered collections in JavaScript, which reset iteration on each access and support operations like mapWith.
- [[partial-application]] — Function technique to fix arguments in JavaScript
- [[quasi-literals]] — JavaScript template strings with backticks and interpolation using ${expression}.
- [[reference-types]] — Non-primitive data types in JavaScript compared by reference identity.
- [[saros-cycle]] — An 18-year astronomical period used to predict recurring solar and lunar eclipses.
- [[stateful-map]] — A lazy mapping technique that preserves state between iterations, used to track position in the chequer game problem.
- [[ternary-operator]] — JavaScript's ternary operator (?) is a control-flow expression that evaluates a condition and returns one of two values.
- [[tortoise-and-hare-algorithm]] — Algorithm to detect loops in linked lists using two pointers (tortoise and hare). See (raw/javascriptallonge.pdf p.158-176) for implementation details.
- [[truthiness]] — JavaScript's truthiness determines behavior of logical operators and conditionals, with falsy values including false, null, undefined, NaN, 0, and empty string.
- [[unary-functions]] — Decorator to enforce single-argument functions in JavaScript
- [[value-types]] — Primitive data types in JavaScript compared by value equality.
- [[void]] — A type of value representing the absence of any value or object.

## Syntheses
- [[wiki-health]] — Wiki health report from the latest lint pass (2026-06-12).
