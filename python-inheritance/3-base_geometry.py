"""basegeometry"""

class BaseGeometry(metaclass= type):
    """ base """

def __dir__(self):
    attributes = super.__dir__()
    new_attribute_list = [item for item in attributes if item !=
    "__init_subclass__"]
    return new_attribute_list
    
a = BaseGeometry()
