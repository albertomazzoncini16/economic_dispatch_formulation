from src.objects.abstract_object_class import AbstractObject
from typing import Optional, Type

def get_object_class_name(object_class: Optional[Type[AbstractObject] | str]) -> str:
    """
    Retrieve the class name of an object.

    - If `object_class` is a subclass of `AbstractObject`, return its `__name__`.
    - If `object_class` is a string, check if it matches any known subclass name of `AbstractObject`.

    Returns:
        str: The name of the class.

    Raises:
        ValueError: If the string does not match a valid subclass.
        TypeError: If the input is neither a subclass nor a valid string.
    """
    if isinstance(object_class, type) and issubclass(object_class, AbstractObject):
        return object_class.__name__
    elif isinstance(object_class, str):
        subclass_names = {subclass.__name__ for subclass in AbstractObject.__subclasses__()}
        if object_class in subclass_names:
            return object_class
        raise ValueError(f"'{object_class}' is not a valid AbstractObject subclass name.")
    else:
        raise TypeError("Input must be a subclass of AbstractObject or a valid subclass name as a string.")

def get_abstract_object_subclass (object_class_name: str) -> Type[AbstractObject]:
    """
    Retrieve the actual subclass of AbstractObject given its class name.

    Args:
        object_class_name (str): The name of the subclass.

    Returns:
        Type[AbstractObject]: The actual subclass.

    Raises:
        ValueError: If the class name does not correspond to a valid subclass.
    """
    subclass_lookup = {cls.__name__: cls for cls in AbstractObject.__subclasses__()}

    if object_class_name not in subclass_lookup:
        raise ValueError(f"'{object_class_name}' is not a recognized subclass of AbstractObject.")

    return subclass_lookup[object_class_name]

def assert_abstract_object_subclass(object_class: Type[AbstractObject] | str) -> None:
    """
    Ensures that the given class is a subclass of AbstractObject.

    Args:
        object_class (Type[AbstractObject]): The class to check.

    Raises:
        TypeError: If the provided class is not a subclass of AbstractObject.
    """
    if isinstance(object_class, str):
        object_class = get_abstract_object_subclass(object_class_name=object_class)
    if not issubclass(object_class, AbstractObject):
        raise ValueError(f"'{object_class.__name__}' must be a subclass of AbstractObject, "
                         f"but got {type(object_class).__name__} instead.")
