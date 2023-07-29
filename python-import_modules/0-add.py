import importlib

# Assign values to variables a and b
a = 1
b = 2

# Import the add function from add_0.py
add_module = importlib.import_module('add_0')
add = add_module.add

# Perform the addition and print the result
result = add(a, b)
print(f"{a} + {b} = {result}")
def add(a, b):
    return a + b