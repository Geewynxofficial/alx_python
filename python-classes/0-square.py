class Square:
    def __init__(self, size):
        self.__size = size
    def __repr__(self):
        return "Square".format(self.__size)
