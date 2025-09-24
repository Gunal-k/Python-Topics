# Demonstrates polymorphism (same method name, different behavior)

class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Polymorphism in action
animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.speak()