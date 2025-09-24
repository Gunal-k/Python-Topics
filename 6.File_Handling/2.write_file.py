# Demonstrates writing to a file

# Writing (overwriting) to a file
file = open("output.txt", "w")
file.write("This is the first line.\n")
file.write("This is the second line.\n")
file.close()

# Appending to a file
file = open("output.txt", "a")
file.write("This line is appended.\n")
file.close()

# Verify file content
file = open("output.txt", "r")
print("File content after write and append:")
print(file.read())
file.close()