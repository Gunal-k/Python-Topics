# Demonstrates closures in Python

def outer_function(msg):
    def inner_function():
        print("Message:", msg)
    return inner_function

my_func = outer_function("Hello from closure!")
my_func()  # prints the message