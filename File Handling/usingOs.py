import os

# Check if a file exists
exists = os.path.exists("example.txt")

# Get the file size
size = os.path.getsize("example.txt")

# Rename a file
os.rename("old_name.txt", "new_name.txt")

# Delete a file
os.remove("example.txt")
