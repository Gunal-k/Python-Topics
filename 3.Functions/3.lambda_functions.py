# Demonstrates anonymous (lambda) functions

# Lambda function to add two numbers
add = lambda x, y: x + y
print("Sum using lambda:", add(5, 3))

# Lambda function to check even or odd
is_even = lambda x: x % 2 == 0
print("Is 4 even?", is_even(4))

# Using lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)