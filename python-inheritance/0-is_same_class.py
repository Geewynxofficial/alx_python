"""my obj class"""
def is_same_class(obj, a_class):
  """Returns True if the object is exactly an instance of the specified class ; otherwise False."""

  if not isinstance(obj, a_class):
    return False

  obj_class = type(obj)
  if obj_class == a_class:
    return True
  else:
    return False