class Square:
    """
    A class that defines a square by its size.

    Attributes:
    size (int): The size of the square."""
    def __init__(self, size):
        """
        Initialize a new square.

        Args:
        size (int): The size of the square.
        """
        self.__size = size
    def __repr__(self):
        """
        Return a string representation of the square.

        Returns:
        str: A string representation of the square.
        """
        return f"Square({self.__size})"
# return f"Square({self.__size})"