# Assign values to variables a and b
a = 1
b = 2

# Import the add function from add_0.py
add_module = __import__("add_0")
add = add_module.add

# Print the result of the addition
result = add(a, b)
print(f"{a} + {b} = {result}")