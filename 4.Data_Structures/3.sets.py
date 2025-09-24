# Demonstrates set operations

# Creating a set
numbers = {1, 2, 3, 4}
print("Original set:", numbers)

# Adding elements
numbers.add(5)
print("After adding 5:", numbers)

# Removing elements
numbers.remove(2)  # raises KeyError if element not present
numbers.discard(10) # safe removal
print("After removing:", numbers)

# Set operations
A = {1, 2, 3}
B = {3, 4, 5}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A-B):", A - B)
print("Symmetric Difference:", A ^ B)

# Looping through set
for num in numbers:
    print("Number:", num)