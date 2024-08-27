# creating a tuple
x = (1, "a", 2)  # tuple with 3 entries
# (3) does not make a tuple with one entry you must provide a trailing comma in this instance
y = (3,)  # a tuple with 1 entry
print(type(x))
print(isinstance(y, tuple))


# the contents of a tuple cannot be changed: it is "immutable"
y = (1, "moo", None)  # (a, b, ...) creates a tuple
y[0] = 2  # TypeError: 'tuple' object does not support item assignment

# `tuple` can create a tuple out of other sequences
x = [2, 4, 8]
y = tuple(x)
print(x)
print(y)
