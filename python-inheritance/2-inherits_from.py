"""direct and indirect"""

def inherits_from(obj, a_class):
  """Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False."""
  
  if isinstance(obj, a_class):
    return False

  # Check if the object's class is a subclass of the specified class.

  obj_class = type(obj)
  while obj_class:
    if any(obj_class == sc for sc in obj_class.__bases__):
       return True
    obj_class = obj_class.__bases__[0]
    return False
    

