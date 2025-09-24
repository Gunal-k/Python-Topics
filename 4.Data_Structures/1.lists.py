# Demonstrates list operations

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Accessing elements
print("First fruit:", fruits[0])

# Adding elements
fruits.append("orange")
fruits.insert(1, "mango")
print("After adding:", fruits)

# Removing elements
fruits.remove("banana")
popped = fruits.pop()
print("After removing:", fruits)
print("Popped element:", popped)

# Slicing
print("Sliced list (1-3):", fruits[1:3])

# Looping through list
for fruit in fruits:
    print("Fruit:", fruit)