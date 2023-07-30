def add(a, b):
    return a + b
a = 1
b = 2
add_module = __import__("add_0")
add = add_module.add
result = add(a,b)
print (f"{a} + {b} = {result}")