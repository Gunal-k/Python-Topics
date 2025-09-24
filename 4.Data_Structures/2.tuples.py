# Demonstrates tuple operations

# Creating a tuple
colors = ("red", "green", "blue")
print("Tuple:", colors)

# Accessing elements
print("First color:", colors[0])

# Tuple is immutable
# colors[0] = "yellow"  # This will raise an error

# Tuple operations
new_colors = colors + ("yellow",)
print("Concatenated tuple:", new_colors)

# Looping through tuple
for color in colors:
    print("Color:", color)