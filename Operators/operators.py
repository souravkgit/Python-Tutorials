# Assignment operator
a = 10
b = 20

# Arithmetic operators
a = a + 10
a += 10  # also valid for "-","*","**","/","//" etc..

# Comparison operators
print(a == b)  # Returns True if a is equal to b
print(a != b)  # Returns True if a is not equal to b
print(a < b)  # Returns True if a is less than b
print(a >= b)  # Returns True if a is greater than or equal to b
print(a is b)  # object identity
print(a is not b)  # negated object identity
print(2 < 3 < 1)  # performs (2 < 3) and (3 < 1)

# demonstrating `==` vs `is`
x = [1, 2, 3]
y = [1, 2, 3]
# `x` and `y` reference equivalent, but distinct lists
print(x == y)
print(x is y)

# Logic Operators
print(True or False)
print(True and False)
print(not False)
print(True | True)
print(True & False)

# condition statements (if, else, and elif)
if a > 80:
    status = "good"
elif a > 50:
    status = "okay"
elif a > 0:
    status = "danger"
else:
    status = "dead"
print(status)  # no need to define the status out of the statements

sign = "positive" if a >= 0 else "negative"  # Inline if else statements
