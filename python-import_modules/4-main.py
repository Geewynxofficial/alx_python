#!/usr/bin/python3
raise_exception = __import__('4-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te: result = safe_print_division(a, b)
print("Exception raised")