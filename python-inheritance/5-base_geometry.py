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