# Basics of string
print("Hello world")  # single quotes
print("Hello world")  # double quotes
print("""Hello world""")  # triple quotes
print("""Hello world""")  # triple quotes
print(type("hello"))
print(isinstance("83", str))
print(str(10.34))
print(str(True))

# String handling
greet = "Hello there!"
print(greet)
print(greet[0])
print(greet[0:5])
print(greet[::-1])
print("hi...\n...bye")  # using `\n` to create a newline

# using triple-quotes to write a multi-line string
x = """ I am a string.
I am part of the same string.
    me... too!"""
# Or
x = " I am a string.\nI am part of the same string.\n    me... too!"

# demonstrating a few of the built-in functions for strings
print("hello".capitalize())  # make first letter upper case
print("hello".upper())  # make whole string upper case
print("HELLO".lower())  # make whole string lower case
print("...".join(["item1", "item2", "item3"]))  # join a list of strings, using "..."
print("item1, item2, item3".split(", "))  # split a string wherever ", " occurs
print("script.py".endswith(".py"))  # does this string end with ".py"?
print("script.py".startswith("sc"))  # does this string start with "sc"?
print(f"x: {'Sourav'}, y: {greet}, z: {int("10")}")  # f-string
print(
    "x: {}, y: {}, z: {}".format(3.2, 8.4, -1.0)
)  # insert objects into a string, in its "formatting" fields {}
print("7".isdigit())  # Are the characters in the string numerical digits?
print(
    "{name} is {age} years old".format(name="Bruce", age=80)
)  # using `format` to replace placeholders with values
print(
    "{item:>8}".format(item="stew")
)  # padding a string with leading-spaces so that it has at least 8 characters
print(
    "My name is %s" % "Sourav"
)  # using `%`(cryptic operator) to  format strings (avoid this)
print("Hello".isupper()) # Return True if every character in the string is uppercase
print("hello".islower()) # Return True if every character in the string is lowercase
