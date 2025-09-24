# Demonstrates classes and objects

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create objects
s1 = Student("Guna", 21)
s2 = Student("Anu", 20)

s1.display_info()
s2.display_info()