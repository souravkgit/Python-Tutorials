# using 'in' and 'not in' for membership checking
tuple_ = (1, 3, 5)
string_ = "the cat in the hat"
list_ = [1, 2, 3, 4]

print(3 in tuple_)
print(0 in tuple_)
print(0 not in tuple_)
print("cat" in string_)
print([1, 2] in list_)
print(
    [1, 2] in [None, [1, 2], None]
)  # the list [1, 2] must be an element of the list to be seen as a member

# concatenating sequences with '+': (seq1 + seq2)
print([1, 2] + [3, 4])  # creates a new list
print("c" + "at")  # concatenates two strings

# Repeated concatenation of a sequence: (n*seq1 or seq1*n)
print("cat" * 3)  # equivalent to `cat + cat + cat`
print(4 * (1, 5))  # creates a new tuple

# Asking for the number of members in a sequence: len(seq)
print(len(list_))
print(len(string_))
print(len(tuple_))

# Getting the index of the first occurrence of x in a sequence: seq.index(x)
print(string_.index("t"))  # 't' first occurs at index-0
# `index` doesn't look within sequences contained by the outer sequence e.g. it sees 1, 2, and "moo", not 1, 2, "m", "o", "o"
print([1, 2, "moo"].index("m"))  # ValueError: 'm' is not in list

# Counting the number of occurrences of x in a sequence: seq.count(x)
print(string_.count("h"))
# `count` doesn't look within sequences contained by the outer sequence thus is doesn't "see" the 1 within `[1, 2]`.
print([1, [1, 2], "111", 1].count(1))


# Demonstrating indexing into sequences

# this is known as the "get-item" syntax
print(list_[0])  # indexing starts at 0
print(list_[-4])  # each entry has a positive index and negative index
print(list_[-1])  # negative indexing is relative to the end of the sequence
print("cat"[2])  # you can index directly into a sequence-object
print((True, False)[-1])

# demonstrating the basics of slicing a sequence
print(string_[0:4:1])  # start:0, stop:4, step:1
print(string_[1:4:1])  # start:1, stop:4, step:1
print(
    string_[0:5:2]
)  # start:0, stop:5, step:2 # get every other entry within [start, stop)
# starting and stopping at the same index produces an empty sequence start:0, stop:0, step:1
print(string_[0:0:1])


# using default start, stop, and step values
print(string_[:])  # start: 0, stop: 7, step: 1 # equivalent: `seq[None:None]`
print(string_[::2])  # start: 0, stop: 7, step: 2
print(string_[::-1])  # using a negative step size reverses the order of the sequence
print(string_[-2:])  # a slice returning the last two values of the sequence
print(string_[:-2])  # a slice returning all but the last two values of the sequence

# using the `slice` object explicitly
print(string_[slice(0, 3, 1)])
# using the `slice` object to slice several sequences
reverse = slice(None, None, -1)
print(string_[reverse])
print(list_[reverse])
print(tuple_[reverse])

# Handling out of bounds indices
print(
    list_[4]
)  # try to access the 5th item in `list_` # IndexError: list index out of range
print(list_[-5])  # IndexError: list index out of range
print(
    list_[:10000]
)  # no bounds checking is used for slicing (nearest valid start/stop value is used)
