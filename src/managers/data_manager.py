import pickle
from src.objects.abstract_object_class import AbstractObject
from relationship_validator import RelationshipValidator
from typing import Optional, TYPE_CHECKING


class DataManager:
    """
    Manages objects in a structured dictionary format.
    Stores objects in collections categorized by their class name.
    """
    def __init__(self, filename="data.pkl"):
        self.filename = filename
        self.objects_database = {}  # Structure: {"ClassName": {"ObjectName": ObjectInstance}}


    def get_object_instance(self, object_class: type[AbstractObject], object_name: str) -> Optional[AbstractObject]:
        """Retrieve an object instance by class type and object name."""
        if not issubclass(object_class, AbstractObject):
            raise ValueError(f"{object_class.__name__} must be a subclass of AbstractObject.")

        object_class_name = object_class.__class__.__name__  # Extract class name dynamically
        return self.objects_database.get(object_class_name, {}).get(object_name, None)

    def get_class_object_names(self, object_class: type[AbstractObject]):
        """Return a list of all object names stored under a given class."""
        if not issubclass(object_class, AbstractObject):
            raise ValueError(f"{object_class.__class__.__name__} must be a subclass of AbstractObject.")

        object_class_name = object_class.__class__.__name__  # Get class name properly
        return list(self.objects_database.get(object_class_name, {}).keys())  # Returns a list of object names (str)

    def add_object(self, object_class: AbstractObject, object_name: str):
        """Add a new object to the database under its class name."""
        object_class_name = object_class.__class__.__name__

        # Ensure the class category exists
        if object_class_name not in self.objects_database:
            self.objects_database[object_class_name] = {}

        # Prevent duplicates
        if object_name in self.objects_database[object_class_name]:
            raise ValueError(f"Object '{object_name}' already exists in '{object_class_name}'.")

        # Store the object
        self.objects_database[object_class_name][object_name] = object_class

    def add_membership(self,
                       child_object_class: type[AbstractObject],
                       child_object_name: str,
                       parent_object_class: type[AbstractObject],
                       parent_object_name: str
                       ):
        """Validate and set a parent-child relationship."""
        child_object_class_instance = self.get_object_instance(child_object_class, child_object_name)
        parent_object_class_instance = self.get_object_instance(parent_object_class, parent_object_name)

        if not child_object_class_instance or not parent_object_class_instance:
            raise ValueError("Both parent and child must exist before setting a relationship.")

        # Validate relationship before setting
        if not RelationshipValidator.is_valid_child(parent_object_class, child_object_class):
            raise ValueError(f"{child_object_class} cannot be a child of {parent_object_class}.")

        if not RelationshipValidator.is_valid_parent(child_object_class, parent_object_class):
            raise ValueError(f"{parent_object_class} cannot be a parent of {child_object_class}.")

        # Set relationships using object methods
        parent_object_class_instance.add_child(child_object_class=child_object_class_instance,
                                               child_object_name=child_object_name)
        child_object_class_instance.add_parent(parent_object_class=parent_object_class_instance,
                                               parent_object_name=parent_object_name)

    def add_property(self, object_class: type[AbstractObject], object_name: str, property_name: str, property_value):
        """Retrieve an object instance and add a property if it exists as an attribute in the AbstractObject subclass.

        Args:
            object_class (type[AbstractObject]): The class type of the object.
            object_name (str): The name of the object.
            property_name (str): The attribute name to update.
            property_value: The value to set for the attribute.

        Raises:
            ValueError: If the object doesn't exist or the property is not a valid attribute.
        """
        obj = self.get_object_instance(object_class, object_name)

        if obj is None:
            raise ValueError(f"Object '{object_name}' of class '{object_class.__class__.__name__}' not found.")

        if not hasattr(obj, property_name):
            raise ValueError(f"'{property_name}' is not a valid attribute of {object_class.__class__.__name__}.")

        setattr(obj, property_name, property_value)

    def save_data(self):
        """Save objects to a file."""
        with open(self.filename, "wb") as f:
            pickle.dump(self.objects_database, f)

    def load_data(self):
        """Load objects from a file."""
        try:
            with open(self.filename, "rb") as f:
                self.objects_database = pickle.load(f)
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")
            self.objects_database = {}
