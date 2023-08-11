import uuid

class Base:
    """Base class for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class."""
        if id is not None:
            self.id = id
        else:
            self.id = uuid.uuid4()
            Base.__nb_objects += 1

