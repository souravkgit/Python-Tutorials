# Open a file in read mode (default)
file = open("example.txt")

# Open a file in write mode (creates the file if it doesn't exist)
file = open("example.txt", "w")

# Open a file in append mode (adds content to the end of the file)
file = open("example.txt", "a")

# Open a file in binary read mode
file = open("example.txt", "rb")

# close the file
file.close()


# Read the entire content of the file
content = file.read()  # file.read(n) read first n bytes

# Read one line at a time
line = file.readline()

# Read all lines into a list
lines = file.readlines()


# Write text to the file (overwrites existing content)
file.write("Hello, world!\n")

# Write multiple lines
file.writelines(["First line\n", "Second line\n"])

# Write binary data to a file
file.write(b"\x00\x01\x02")


# Open a file, work with it, and close it automatically
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 'r': Read (default mode)
# 'w': Write (creates a new file or truncates an existing file)
# 'a': Append (adds to the end of the file)
# 'b': Binary mode (e.g., 'rb' or 'wb')
# 'x': Exclusive creation (fails if the file already exists)

# File positioning
# Move the cursor to the beginning of the file
file.seek(0)

# Get the current position of the cursor
position = file.tell()

# Basic exception handling
try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An I/O error occurred.")
