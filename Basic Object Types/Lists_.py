# a list-type object stores a sequence of other objects
print([3.5, None, 3.5, True, "hello"])
print(type([1, 2, 3]))
print(isinstance([1, 2], list))
list_ = []  # constructing an empty list
list_ = ["hello"]  # constructing a list with only one member
x = "hello"  # the list constructor will simplify expressions and store their resulting objects
print([2 < 3, x.capitalize(), 5**2, [1, 2]])
print(list("apple"))  # `list` forms a list out of the contents of other sequences
print([1, "a", True] == [1, True, "a"])  # A list's ordering matters

x = [2, 4, 6, 8, 10]
y = [2, 4, 6, 8, 10]

# Accessing the contents of a list with indexing and slicing
print(len(x))  # give length of the iterable object
print(x[0])  # access the 0th item in the list via "indexing"
print(x[1:3])  # access a subsequence of the list via "slicing"

# changing a list after it has been constructed (i.e list allows mutation)
x[1] = "apple"  # "set" the string 'apple' into position 1 of `x`
print(x)
y[1:4] = [-3, -4, -5]  # replace a subsequence of `y`
print(y)

# Built in functions
x.append("moo")  # use `append` to add a single object to the end of a list
print(x)
x.extend(
    [True, False, None]
)  # use `extend` to add a sequence of items to the end of a list
print(x)
print(
    x.pop(1)
)  # pop the position-1 item out from a list `pop` will return the item that gets removed.
print(x)
x.remove(6)  # remove the object "d" from the list
print(x)
