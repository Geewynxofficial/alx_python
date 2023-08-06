"""
This module defines a class for representing squares.

The `Square` class has a single attribute, `size`, which represents the size of the square. The `Square` class also has a `__repr__()` method, which returns a string representation of the square.
"""
class Square:
    """A class representing squares."""

    def __init__(self, size):
        """Initialize a square with the given size."""
        self.size = size

    def __repr__(self):
        """Return a string representation of the square."""
        return f"Square(size={self.size})"


square = Square(9)
print(square)
