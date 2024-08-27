# Defining a function
'''
def <function name>(<function signature>):
    """ documentation string """
    <encapsulated code>
    return <object>
    
-> <function name> can be any valid variable name, and must be followed by parentheses and then a colon.
-> <function signature> specifies the input arguments to the function, and may be left blank if the function does not accept any arguments (the parentheses must still be included, but will not encapsulate anything).
-> The documentation string (commonly referred to as a “docstring”) may span multiple lines, and should indicate what the function’s purpose is. It is optional.
-> <encapsulated code> can consist of general Python code, and is demarcated by being indented relative to the def statement.
-> return if reached by the encapsulated code, triggers the function to return the specified object and end its own execution immediately.
'''


def count_vowels(in_string):
    """Returns the number of vowels contained in `in_string`"""  # doc string (can get using "__doc__" attribute)
    num_vowels = 0
    vowels = "aeiouAEIOU"
    for char in in_string:
        if char in vowels:
            num_vowels += 1  # equivalent to num_vowels = num_vowels + 1
    return num_vowels


print(count_vowels("Hi my name is Ryan"))


# Inline Functions
def add_2(x):
    return x + 2


# Arguments (sequence of comma-separated variable names can be specified in the function signature to indicated positional arguments)
def is_bounded(x, lower, upper):  # x, lower, upper are the arguments
    return lower <= x <= upper


# Specifying Arguments by Position
"""objects passed to is_bounded will be assigned to its input variables based on their positions"""
print(is_bounded(3, 2, 4))

# Specifying Arguments by Name
"""
can provide explicit names when specifying the inputs to a function, in which case ordering does not matter.
can mix-and-match positional and named input by using position-based inputs first
"""
print(is_bounded(lower=2, x=3, upper=4))
print(
    is_bounded(3, upper=4, lower=2)
)  # `x` is specified based on position `lower` and `upper` are specified by name


# Default-Valued Arguments
def count_vowels(in_string, include_y=False):
    """Returns the number of vowels contained in `in_string`"""
    vowels = "aeiouAEIOU"
    if include_y:
        vowels += "yY"  # add "y" to vowels
    return sum(1 for char in in_string if char in vowels)


print(count_vowels("Happy"))
print(count_vowels("Happy", True))
print(count_vowels(include_y=True, in_string="Happy"))
# -> Default-valued input arguments must come after all positional input arguments in the function signature


# Accommodating an Arbitrary Number of Positional Arguments


# The * symbol indicates that an arbitrary number of arguments can be passed to `args`, when calling `f`.
def f(*args):
    #  All arguments passed to `f` will be "packed" into a
    #  tuple that is assigned to the variable `args`.
    # `f()`  will assign `args = tuple()`
    # `f(x, y, ...)` will assign `args = (x, y, ...)`
    return args


print(f())  # pass zero arguments to `f`
print(f(1))  # pass one argument to `f`
print(f((0, 1), True, "Hey"))  # pass three arguments to `f`


# This syntax can be combined with positional arguments and default arguments.
# Any variables specified after a packed variable must be called by name
def f(x, *seq, y):
    print("x is: ", x)
    print("seq is: ", seq)
    print("y is: ", y)
    return None


print(f(1, 2, 3, 4, y=5))  # `y` must be specified by name


# Accommodating an Arbitrary Number of Keyword Arguments


# The ** symbol indicates that an arbitrary number of keyword arguments can be passed to `args`, when calling `f`.
def f(**args):
    #  All keyword arguments passed to `f` will be "packed" into a
    #  dictionary that is assigned to the variable `args`.
    # `f()`  will assign `args = {}` (an empty dictionary)
    # `f(x=1, y=2, ...)` will assign `args = {"x":1, "y":2, ...}`
    return args


print(f())  # pass zero arguments to `f`
print(f(x=1))  # pass one argument to `f`
print(f(x=(0, 1), val=True, moo="cow"))  # pass three arguments to `f`


# This syntax can be combined with positional arguments and default arguments.
# No additional arguments may come after a ** entry in a function-definition signature
def f(x, y=2, **kwargs):
    print("x is: ", x)
    print("y is: ", y)
    print("kwargs is: ", kwargs)
    return None


print(f(1, y=9, z=3, k="hi"))  # passing arbitrary keyword arguments to `f`


# accepting arbitrary positional and keyword arguments
def f(*x, **y):
    # all positional arguments get packed into the tuple `x`
    # all keyword arguments get packed into the dictionary `y`
    print(x)
    print(y)
    return None


print(f(1, 2, 3, hi=-1, bye=-2, sigh=-3))


# Functions are Objects
"""Once defined, a function behaves like any other Python object, like a list or string or integer. You can assign a variable to a function-object"""
var = count_vowels  # `var` now references the function `count_vowels`
print(var("Hello"))  # you can now "call" `var`

my_list = [count_vowels, print]
for func in my_list:
    func("hello")
# iteration 0: calls `count_vowels("hello")`
# iteration 1: calls `print("hello")`
