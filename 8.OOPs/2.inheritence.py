# Demonstrates single and multilevel inheritance

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")

class Student(Person):  # Inherits from Person
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_course(self):
        print(f"{self.name} is studying {self.course}")

class GraduateStudent(Student):  # Multilevel inheritance
    def __init__(self, name, course, degree):
        super().__init__(name, course)
        self.degree = degree

    def show_degree(self):
        print(f"{self.name} has completed {self.degree}")

# Usage
g = GraduateStudent("Guna", "MCA", "Bachelor's")
g.greet()
g.show_course()
g.show_degree()