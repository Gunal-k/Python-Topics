# Demonstrates creating and using custom exceptions

class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed for square root.")
    return num ** 0.5

try:
    value = int(input("Enter a number: "))
    print("Square root:", square_root(value))

except NegativeNumberError as e:
    print("Custom Exception Caught:", e)

except Exception as e:
    print("An unexpected error occurred:", e)