# The "range" generator

for i in range(2, 7):  # start: 2  (included) # stop: 7  (excluded) # step: 1  (default)
    print(i)

for i in range(1, 10, 2):  # start: 1  (included) # stop: 10  (excluded) # step: 2
    print(i)

for i in range(5):  # start: 0  (included) # stop: 5  (excluded) # step: 1 (default)
    print(i)

"""
the command range(5) will simply store the instructions needed to produce the sequence of numbers 0-4, whereas the list [0, 1, 2, 3, 4] stores all of these items in memory at once
"""


# Creating your own generator: generator comprehensions

"""
Syntax : (<expression> for <var> in <iterable> [if <condition>])

Written in a long form, the pseudo-code is:
for <var> in <iterable>:
    if bool(<condition>):
        yield <expression>
"""
# Example
even_gen = (
    i for i in range(100) if i % 2 == 0
)  # when iterated over, `even_gen` will generate 0.. 2.. 4.. ... 98


# The if <condition> clause in the generator expression is optional.
"""
(<expression> for <var> in <iterable>)

for <var> in <iterable>:
    yield <expression>
"""

# Example
# when iterated over, `example_gen` will generate 0/2.. 9/2.. 21/2.. 32/2
example_gen = (i / 2 for i in [0, 9, 21, 32])
for item in example_gen:
    print(item)


# <expression> can be any valid single-line of Python code that returns an object
# Example
gen = ((i, i**2, i**3) for i in range(10))
# will generate:
# (0, 0, 0)
# (1, 1, 1)
# (2, 4, 8)

gen = (("apple" if i < 3 else "pie") for i in range(6))  # Inline if-else expression
print(gen)
# will generate:
# 'apple'..
# 'apple'..
# 'apple'..
# 'pie'..
# 'pie'..
# 'pie'


# you **cannot** do the following...
gen = (i**2 for i in range(100))

# query the length of a generator
# print(len(gen))  # TypeError: object of type 'generator' has no len()

# index into a generator
# print(gen[2])  # TypeError: 'generator' object is not subscriptable


# Consuming generators
gen = (i**2 for i in range(100))
print(sum(gen))  # computes the sum 0 + 1 + 4 + 9 + 25 + ... + 9801
print(sum(gen))  # computes the sum of ... nothing! `gen` has already been consumed!


# checking for membership consumes a generator until
# it finds that item (consuming the entire generator
# if the item is not contained within it)
gen = (i for i in range(1, 11))
print(5 in gen)  # first 5 elements are consumed

# 1-5 are no longer contained in gen
# this check consumes the entire generator!
print(5 in gen)
print(sum(gen))


# chaining two generator comprehensions
gen_1 = (i**2 for i in [-20, -10, 0, 10, 20])  # generates 400.. 100.. 0.. 100.. 400
# iterates through gen_1, excluding any numbers whose absolute value is greater than 150
gen_2 = (j for j in gen_1 if abs(j) <= 150)
print(sum(gen_2))  # computing 100 + 0 + 100


# Iterating over generators using "next"
# consuming an iterator using `next`
short_gen = (i / 2 for i in [1, 2, 3])
print(next(short_gen))
print(next(short_gen))
print(next(short_gen))
print(next(short_gen))
"""StopIteration
Traceback (most recent call last)
<file> in <module>()
----> 1 next(short_gen)
StopIteration:"""


# Iterables vs. Iterators
# a list is an example of an iterable that is *not*
# an iterator - you cannot call `next` on it.
x = [1, 2, 3]
print(next(x))
"""---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-19-b9d20096048c> in <module>()
----> 1 next([1,2])

TypeError: 'list' object is not an iterator"""

# any iterable can be fed to `iter`
# to produce an iterator for that object
print(x=[1, 2, 3])
x_it = iter(x)  # `x_it` is an iterator
print(next(x_it))
print(next(x_it))
print(next(x_it))

# List Comprehensions ([<expression> for <var> in <iterable> {if <condition}])
print([i**2 for i in range(10)])  # a simple list comprehension
print([[0 for col in range(4)] for row in range(3)])  # Nested list comprehensions.
