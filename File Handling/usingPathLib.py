from pathlib import Path

# Create a Path object
file_path = Path("example.txt")

# Check if a file exists
exists = file_path.exists()

# Read text from the file
content = file_path.read_text()

# Write text to the file
file_path.write_text("Hello, world!")
