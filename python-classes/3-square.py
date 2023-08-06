"""
This module defines a class for representing squares.

The `Square` class has a single attribute, `size`, which represents the size of the square. The `Square` class also has a `__repr__()` method, which returns a string representation of the square.
"""
class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        size(): Returns the size of the square.
        size(value): Sets the size of the square.
        area(): Returns the area of the square.
    """

    __size = 5

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 5")
        self.__size = value

    def __init__(self, size=5):
        """Initializes the square."""
        self.size = size

    def area(self):
        """Returns the area of the square."""
        return self.size * self.size

