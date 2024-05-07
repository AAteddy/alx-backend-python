# Python - Async Comprehension

This project tries to dig deep in to Python's Async Comprehension. At the end of this project, I am expected to fully understand and get hands on experience on:

<ul>
<li> How to write an asynchronous generator</li>
<li> How to use async comprehensions</li>
<li> How to type-annotate generators</li>
</ul>

## Definition:

## Asynchronous Comprehensions

PEP 492 and PEP 525 introduce support for native coroutines and asynchronous generators using async / await syntax. This PEP proposes to add asynchronous versions of list, set, dict comprehensions and generator expressions.

We propose to allow using async for inside list, set and dict comprehensions. Pending PEP 525 approval, we can also allow creation of asynchronous generator expressions.

### Examples:

<ul>
<li> set comprehension: {i async for i in agen()}; </li>
<li> list comprehension: [i async for i in agen()]; </li>
<li> dict comprehension: {i: i ** 2 async for i in agen()}; </li>
<li> generator expression: (i ** 2 async for i in agen()). </li>
</ul>
