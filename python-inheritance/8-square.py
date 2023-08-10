"""basegeometry"""
class BaseGeometryMeta(type):
    """ type class """
    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [
            item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list
    
class BaseGeometry(metaclass=BaseGeometryMeta):

    """ description base """
    
    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list
class BaseGeometry(metaclass=BaseGeometryMeta):
    """ geo """
    def __dir__(self):
        attributes = super().__dir__()
        new_attribute_list = [item for item in attributes if item != "__init_subclass__"]
        return new_attribute_list
    
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        descript method
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value
class Rectangle(BaseGeometry):
    """rectangle"""
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    def area(self):
        return self.__width * self.__height
    
class Square(Rectangle):
    def __init__(self, size):
        self.__size = super().integer_validator("size", size)
        super().__init__(size, size)

