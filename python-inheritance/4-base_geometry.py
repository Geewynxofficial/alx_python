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
    def area(self):
        raise Exception("area() is not implemented")
