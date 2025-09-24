# Demonstrates basic function definition and usage

# Function without parameters
def greet():
    print("Hello, Guna!")

greet()

# Function with parameters
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# Function with default parameters
def greet_person(name="Guest"):
    print("Hello,", name)

greet_person()
greet_person("Guna")