"""
Here are some useful built-in functions that accept iterables as arguments:

list, tuple, dict, set: construct a list, tuple, dictionary, or set, respectively, from the contents of an iterable
sum: sum the contents of an iterable.
sorted: return a list of the sorted contents of an interable
any: returns True and ends the iteration immediately if bool(item) was True for any item in the iterable.
all: returns True only if bool(item) was True for all items in the iterable.
max: return the largest value in an iterable.
min: return the smallest value in an iterable.
"""

# Examples of built-in functions that act on iterables
print(list("I am a cow"))
print(sum([1, 2, 3]))
print(sorted("gheliabciou"))
print(
    any((0, None, [], 0))
)  # `bool(item)` evaluates to `False` for each of these items
print(
    all([1, (0, 1), True, "hi"])
)  # `bool(item)` evaluates to  `True` for each of these items
print(max((5, 8, 9, 0)))
print(min("hello"))


# “Unpacking” iterables
grades = [("Ashley", 93), ("Brad", 95), ("Cassie", 84)]
for entry in grades:
    print(entry)
for name, grade in grades:
    print(name)
    print(grade)
    print("\n")


# Enumerating iterables
for entry in enumerate("abcd"):
    print(entry)
