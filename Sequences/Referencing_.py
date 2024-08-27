# Mutable and Immutable objects

# Some immutable objects
"""
numbers (integers, floating-point numbers, complex numbers)
strings
tuples
booleans
"""

# Some mutable objects
"""
lists
dictionaries
sets
NumPy arrays
"""

"""
The mutability of an object refers to its ability to have its state changed. A mutable object can have its state changed, whereas an immutable object cannot. For instance, a list is an example of a mutable object. Once formed, we are able to update the contents of a list - replacing, adding to, and removing its elements.
Basically what happens is, suppose we:
Create (initialize) a list with the state [1, 2, 3].
Assign this list to the variable x; x is now a reference to that list.
Using our referencing variable, x, update element-0 of the list to store the integer -4.
This does not create a new list object, rather it mutates our original list. This is why printing x in the console displays [-4, 2, 3] and not [1, 2, 3].
"""

# demonstrating the behavior of variables referencing the same object

# For lists
list1 = [1, 2, 3]  #  `list1` references [1, 2, 3]
list2 = list1  #  `list2` and `list1` now both reference [1, 2, 3]
print(list1)
print(list2)
list1.append(4)  # append 4 to the end of [1, 2, 3]
print(list1)
print(list2)

list1 = [1, 2, 3]  #  `list1` references [1, 2, 3]
list2 = [1, 2, 3]  #  `list2` references a *separate* list, whose value is [1, 2, 3]

list1.append(4)  # append 4 to the end of [1, 2, 3]
print(list1)
print(list2)  # `list2` still references its own list

x = [0, 1, 2, 3]
y = x[:2]
print(y)  # does `y` reference the same list as `x`?
x[0] = -1  # update one of the entries of the list that `x` references
print(x)
print(y)  # the list that `y` references was unaffected by the update


# For integers
x = 3
y = x
x *= 3
print(x)
print(y)
