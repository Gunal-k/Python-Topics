# Demonstrates dictionary operations

# Creating a dictionary
student = {"name": "Guna", "age": 21, "course": "BCA"}
print("Original dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))

# Adding and updating entries
student["grade"] = "A"
student["age"] = 22
print("After update:", student)

# Removing entries
del student["grade"]
removed = student.pop("course")
print("After deletion:", student)
print("Removed course:", removed)

# Looping through dictionary
for key, value in student.items():
    print(f"{key}: {value}")