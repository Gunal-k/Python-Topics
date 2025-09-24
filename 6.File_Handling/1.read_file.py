# Demonstrates reading from a file

# Create a sample file first (for demonstration)
with open("sample.txt", "w") as f:
    f.write("Hello, Guna!\nWelcome to Python file handling.\nHave a great day!")

# Reading the file
file = open("sample.txt", "r")
content = file.read()
print("File content:\n", content)
file.close()

# Reading line by line
file = open("sample.txt", "r")
print("Reading line by line:")
for line in file:
    print(line.strip())
file.close()