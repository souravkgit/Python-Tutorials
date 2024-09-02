# Modules vs Packages vs Libraries


# --------------------------- Modules -------------------------------------- #
"""
Definition: A module is a single file that contains Python code. It can include functions, classes, variables, and runnable code.
Usage: Modules allow you to organize your code into manageable pieces. For example, you might have a module named math_utils.py that contains various utility functions for mathematical operations.
"""


# math_utils.py (Example)
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# To use this module in another file
import math_utils

result = math_utils.add(5, 3)
print(result)  # Output: 8


# --------------------------- Packages -------------------------------------- #
"""
Definition: A package is a collection of modules organized in a directory hierarchy. A directory becomes a package when it contains an __init__.py file (though this file is optional in Python 3.3+).
Usage: Packages help in organizing modules into a directory structure. For example, you might have a package named utilities with multiple modules like math_utils.py and string_utils.py.
"""
# Example
# utilities/
#     __init__.py
#     math_utils.py
#     string_utils.py

# To use this package in another file
from utilities import math_utils

result = math_utils.add(5, 3)
print(result)  # Output: 8


# --------------------------- Libraries -------------------------------------- #
"""
Definition: A library is a broader term that refers to a collection of modules and packages that are bundled together to provide a set of functionalities. It can be thought of as a package of packages.
Usage: Libraries are often distributed to provide reusable code for a wide range of tasks, like data manipulation, web development, etc. Examples of libraries include NumPy for numerical computations, requests for HTTP requests, and pandas for data analysis.
"""

# Example
import numpy as np

array = np.array([1, 2, 3, 4])
print(array)  # Output: [1 2 3 4]


"""
Summary
Module: A single file containing Python code.
Package: A directory containing modules and an __init__.py file (optional in Python 3.3+).
Library: A collection of modules and/or packages, often distributed as a single unit to provide a broad range of functionality.
"""
