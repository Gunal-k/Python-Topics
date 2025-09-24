# Demonstrates importing and using a custom module

# Import entire module
import my_module

print(my_module.greet("Guna"))
print("Sum:", my_module.add(5, 3))
print("Product:", my_module.multiply(5, 3))

# Import specific functions
from my_module import greet, add
print(greet("Student"))
print("Sum:", add(10, 20))

# Import with alias
import my_module as mm
print(mm.multiply(4, 5))
