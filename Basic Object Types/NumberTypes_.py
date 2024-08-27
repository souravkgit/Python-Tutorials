# Integers
print(type(-3))  # return type of the variable or constant
print(isinstance(1.3, int))  # validate if the given instance is true for the variable
print(int("10"))  # convert string to integer
print(int(1.3))  # convert float to integer
print(int("10010", 2))  # convert binary to integer of base 2

# Floating point numbers
print(100**0.5)  # 100 raised to the power of 0.5
print(1 / 3)  # 1 divided by 3
print(type(-2.1))  # return type of the variable or constant
print(isinstance(10, float))  # validate if the given instance is true for the variable
print(
    isinstance(10.0, float)
)  # validate if the given instance is true for the variable
print(float("10.456"))  # convert string to float
print(float(-22))  # convert integer to float
print(2e-1)

# Complex numbers
print((2 + 3j))  # create a complex number
print(complex(2, 3))  # complex function used to create a complex number
print(complex(0, 1) ** 2)  # complex number raised to the power of 2
print(type(2 + 3j))  # return type of the variable or constant
print(
    isinstance(2 - 4j, complex)
)  # validate if the given instance is true for the variable

# Numbers Readability
print(1_000_000)  # this is nice!
print(2_3_4.5_6_7)
print(1_0 + 10_000j)
