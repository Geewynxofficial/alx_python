"""
This module defines a class for representing squares.

The `Square` class has a single attribute, `size`, which represents the size of the square. The `Square` class also has a `__repr__()` method, which returns a string representation of the square.
"""
class Square:
    """A square with a side length of `size`."""


    # Private instance attribute
    _size = 0

    # Property to retrieve the size
    @property
    def size(self):
        return self._size

    # Property setter to set the size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    # Instantiation with optional size
    def __init__(self, size=0):
        self.size = size

    # Public instance method to return the current square area
    def area(self):
        return self.size * self.size

    # Public instance method to print the square with the character "#"
    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print("#" * self.size)

