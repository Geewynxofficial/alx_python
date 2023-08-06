"""
This module defines a class for representing squares.

The `Square` class has a single attribute, `size`, which represents the size of the square. The `Square` class also has a `__repr__()` method, which returns a string representation of the square.
"""
class Square:
    """A class that defines a square."""

    # Private instance attribute
    __size = None

    def __init__(self, size=0):
        """Initializes the square with the given size.

        Args:
            size: The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size


