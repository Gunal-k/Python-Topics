# Demonstrates using 'with' statement for file handling (recommended)

# Writing to a file using 'with'
with open("with_file.txt", "w") as f:
    f.write("This file uses 'with' statement.\n")
    f.write("No need to close manually!")

# Reading from a file using 'with'
with open("with_file.txt", "r") as f:
    content = f.read()
    print("Reading with 'with':\n", content)