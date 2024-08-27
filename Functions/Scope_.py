"""
A valuable aspect of the “encapsulation” provided by functions is that the function’s input argument variables, and any variables defined within the function, cannot be “seen” nor accessed outside of the function. That is, these variables are said to have a restricted scope.
"""

x = 3  # `x` has file scope. It can be even be accessed
# within a function, even if it isn't passed to
# the function as an argument


# `my_func` has file scope (after it is defined)
def my_func(y):
    func_var = 9 + x  # `x` will have the value 3
    # the scope of `y` and `func_var` is restricted to this function
    return y


print(x)
# `func_var` and `y` do not exist here
print(func_var)  # raises NameError: name `func_var` not defined
print(y)  # raises NameError: name `y` not defined


# this demonstrates scope of variables in different contexts

from itertools import combinations  # `combinations` has file scope


# `my_func` has file scope
# `in_arg1` has restricted scope
# `in_arg2` has restricted scope
# `func_block` has restricted scope
def my_func(in_arg1, in_arg2="cat"):
    func_block = 1
    return None


# `file_var` has file scope
# `comp_var` has restricted scope
file_var = [comp_var**2 for comp_var in [-1, -2]]

# `if_block` has file scope
if True:
    if_block = 2
else:
    if_block = 3

# `it_var` has file scope
# `for_block` has file scope
for it_var in [1, 2, 3]:
    for_block = 1

# `while_block` has file scope
while True:
    while_block = None
    break
"""
In the preceding code, the following variables have file scope:
combinations
my_func
file_var
if_block
it_var
for_block
while_block

whereas the following variables have restricted scope:
in_arg1
in_arg2
func_block
comp_var
"""

# Variable Shadowing
"""
What happens when a file-scope variable and a function-scope variable share the same name? This type of circumstance is known as variable shadowing. Python resolves this by giving precedence to the variable with the most restricted scope, when inside that scope
"""
x = 2
y = 3


def func(x):
    # input-arg `x` overrides file-scope version of `x`
    y = 5  # overrides file-scope version of `y`
    return x + y


# `x` is 2 here, once again
# `y` is 3 here, once again
print(func(-5))  # prints 0
print(x, y)  # prints 2  3
