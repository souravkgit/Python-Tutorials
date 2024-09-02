import os

file_path = "example.txt"

# Proper file handling with proper exceptions handling
try:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")

    with open(file_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError as e:
    print(e)
except IOError as e:
    print(f"An I/O error occurred: {e}")
