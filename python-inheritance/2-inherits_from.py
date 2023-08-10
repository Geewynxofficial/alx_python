"""direct and indirect"""

def inherits_from(obj, a_class):
  """Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False."""
  
  obj_class = type(obj)
  if isinstance(obj, a_class) and obj_class is not a_class:
    return True
  else:
    return False
  
  a = True

