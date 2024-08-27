"""
General Syntax
while <condition>:
    block of code
"""

# demonstrating a basic while-loop
total = 0
while total < 2:
    total += 1  # equivalent to: `total = total + 1`

print(total)  # `total` has the value 2


"""
This code will perform the following steps:

Define the variable total, and assign it the value 0
Evaluate 0 < 2, which returns True: enter the enclosed code-block
Execute the code block: assign total the value 0 + 1
Evaluate 1 < 2, which returns True: enter the enclosed code-block
Execute the code block: assign total the value 1 + 1
Evaluate 2 < 2, which returns False: skip the enclosed code-block
Print the value of total (2)
"""
