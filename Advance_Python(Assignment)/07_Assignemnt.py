filename = "demo.txt"

# Create a file and write some content
file = open(filename, "w")
file.write("Welcome to Python file handling.\n")
file.write("This is the second line of the file.\n")
file.close()

print("File has been created successfully.")

# Read the file
file = open(filename, "r")
content = file.read()
file.close()

print("\nOriginal File Content:")
print(content)

# Add new content to the existing file
file = open(filename, "a")
file.write("This content was added afterwards.\n")
file.close()

print("Additional content has been added.")

# Read the updated file
file = open(filename, "r")
updated_content = file.read()
file.close()

print("\nUpdated File Content:")
print(updated_content)




# comment
# File has been created successfully.

# Original File Content:
# Welcome to Python file handling.
# This is the second line of the file.

# Additional content has been added.

# Updated File Content:
# Welcome to Python file handling.
# This is the second line of the file.
# This content was added afterwards.