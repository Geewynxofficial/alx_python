"""my kind of class"""
def is_kind_of_class(obj, a_class):
  """Returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False."""

  if not isinstance(obj, a_class):
    return False

  # Check if the object's class is a subclass of the specified class.

  obj_class = type(obj)
  while obj_class:
    if obj_class == a_class:
      return True
    obj_class = obj_class.__bases__[0]

  return False

