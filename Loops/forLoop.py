"""
General Syntax
for <var> in <iterable>:
    block of code
"""

# demonstrating a basic for-loop
total = 0
for item in [1, 3, 5]:
    total = total + item

print(total)  # `total` has the value 1 + 3 + 5 = 9
# `item` is still defined here, and holds the value 5


"""
This code will perform the following steps:

Define the variable total, and assign it the value 0
Iterate on the list, producing value 1, define the variable item and assign it the value 1
Assign total the value 0 + 1
Iterate on the list, producing the value 3 and assigning it to item
Assign total the value 1 + 3
Iterate on the list, producing the value 5 and assigning it to item
Assign total the value 4 + 5
Iterate on the list. Having reached its end, a StopIteration signal it raised by the list, and the for-loop sequence is exited.
Print the value of total (9)
"""
