from abc import ABC

class GenericCoreObject(ABC):
    """
    Summary of the Abstract CoreObject Class
    Purpose:

    To define a base class for all core objects (e.g., Node, Generator).
    Enforces a consistent structure by requiring the implementation of object_name.
    Key Features:

    Uses a @property to encapsulate the object_name attribute.
    Validates that object_name is a non-empty string.
    Provides controlled access to the object_name attribute.
    Why Use @property:

    Ensures encapsulation and validation when getting or setting the object_name.
    Allows flexibility for future logic, such as dynamically computed names.
    """
    def __init__(self):
        self._object_name = None

    @property
    def object_name(self) -> str:
        """Getter for object_name."""
        return self._object_name

    @object_name.setter
    def object_name(self, object_name: str):
        """Setter for object_name with validation."""
        if not object_name or not isinstance(object_name, str):
            raise ValueError("Object name must be a non-empty string.")
        self._object_name = object_name
