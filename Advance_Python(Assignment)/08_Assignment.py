import os

current_folder = os.path.dirname(os.path.abspath(__file__))

source_path = os.path.join(current_folder, "input.txt")
destination_path = os.path.join(current_folder, "output.txt")

with open(source_path, "r") as f:
    content = f.readlines()

total_lines = len(content)
print("Total number of lines:", total_lines)

selected_lines = content[:2]

print("\nFirst two lines:")
for text in selected_lines:
    print(text.strip())

with open(destination_path, "w") as f:
    f.writelines(selected_lines)

print("\nFirst two lines copied to output.txt successfully.")


# Total number of lines: 5

# First two lines:
# Hello, this is the first line.
# This is the second line.

# First two lines copied to output.txt successfully.