# Demonstrates nested loops

# Nested for loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# Simple pattern printing using nested loops
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
