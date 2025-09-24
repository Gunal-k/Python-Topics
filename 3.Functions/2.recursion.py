# Demonstrates recursion (a function calling itself)

# Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"Factorial of {num} is {factorial(num)}")

# Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = 10
print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")