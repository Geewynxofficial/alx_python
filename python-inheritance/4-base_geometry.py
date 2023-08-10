"""basegeometry"""
class BaseGeometry(metaclass=BaseGeometryMeta):
    """ geo """
    def area(self):
        raise Exception("area() is not implemented")
a = BaseGeometry()