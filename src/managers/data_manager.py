import pickle
from src.objects.abstract_object_class import AbstractObject
from src.managers.relationship_validator import RelationshipValidator
from src.managers.objects_attributes_manager import ObjectAttributesManager  # Ensure ObjectManager is imported
from typing import Optional, Type, Dict


class DataManager:
    """
    Manages objects in a structured dictionary format.
    Stores objects in collections categorized by their class name.
    Uses ObjectManager for attribute handling.
    Uses RelationshipValidator to validate parent-child relationships.
    """
    def __init__(self, filename="data.pkl"):
        self.filename = filename
        self.objects_database: Dict[str, Dict[str, AbstractObject]] = {}  # Structure: {"ClassName": {"ObjectName": ObjectInstance}}

    @staticmethod
    def get_object_class_name(object_class: Optional[Type[AbstractObject] | str]) -> str:
        """
        Retrieve the class name of an object.

        - If `object_class` is a subclass of `AbstractObject`, return its `__name__`.
        - If `object_class` is a string, check if it matches any known subclass name of `AbstractObject`.
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

    def get_object_instance(self,
                            object_class: type[AbstractObject],
                            object_name: str
                            ) -> Optional[AbstractObject]:
        """Retrieve an object instance by class type and object name."""
        if not issubclass(object_class, AbstractObject):
            raise ValueError(f"{self.get_object_class_name(object_class)} must be a subclass of AbstractObject.")

        object_class_name = self.get_object_class_name(object_class)
        return self.objects_database.get(object_class_name, {}).get(object_name, None)

    def add_object(self, object_class: Type[AbstractObject], object_name: str):
        """Initialize and add a new object instance to the database under its class name."""
        if not issubclass(object_class, AbstractObject):
            raise TypeError(f"{object_class.__name__} must be a subclass of AbstractObject.")

        object_class_name = self.get_object_class_name(object_class)

        # Ensure the class category exists
        if object_class_name not in self.objects_database:
            self.objects_database[object_class_name] = {}

        # Prevent duplicates
        if object_name in self.objects_database[object_class_name]:
            raise ValueError(f"Object '{object_name}' already exists in '{object_class_name}'.")

        # Initialize and store the object
        object_class : AbstractObject
        obj: AbstractObject = object_class(object_name=object_name)
        self.objects_database[object_class_name][object_name] = obj

    def add_membership(self,
                       child_object_class: type[AbstractObject],
                       child_object_name: str,
                       parent_object_class: type[AbstractObject],
                       parent_object_name: str
                       ):
        """Validate and set a parent-child relationship using RelationshipValidator."""
        child_object_instance = self.get_object_instance(child_object_class, child_object_name)
        parent_object_instance = self.get_object_instance(parent_object_class, parent_object_name)

        if not parent_object_instance:
            raise ValueError(f"Parent {parent_object_name} must exist before setting a relationship.")

        if not child_object_instance:
            raise ValueError(f"Child {child_object_name} must exist before setting a relationship.")

        # Validate relationship before setting
        if not RelationshipValidator.is_valid_child(parent_object_instance.__class__, child_object_instance.__class__):
            raise ValueError(f"ObjectClass {child_object_instance.__class__.__name__} cannot be a child of ObjectClass {parent_object_instance.__class__.__name__}.")

        if not RelationshipValidator.is_valid_parent(child_object_instance.__class__, parent_object_instance.__class__):
            raise ValueError(f"ObjectClass {parent_object_instance.__class__.__name__} cannot be a parent of ObjectClass {child_object_instance.__class__.__name__}.")

        # Use ObjectManager to update attributes
        ObjectAttributesManager.set_child(obj=parent_object_instance, child_class=child_object_class, child_object_name=child_object_name)
        ObjectAttributesManager.set_parent(obj=child_object_instance, parent_class=parent_object_class, parent_object_name=parent_object_name)

    def add_attribute(self, object_class: type[AbstractObject], object_name: str, attr_name: str, attr_value):
        """Retrieve an object instance and add a property using ObjectManager."""
        object_class_instance = self.get_object_instance(object_class, object_name)

        if object_class_instance is None:
            raise ValueError(f"Object '{object_name}' of class '{object_class.__name__}' not found in DataManager.")

        ObjectAttributesManager.set_attribute(obj=object_class_instance, attr_name=attr_name, attr_value=attr_value)

    def get_object_attribute(self, object_class: type[AbstractObject], object_name: str, property_name: str):
        """Retrieve an object's attribute using ObjectManager."""
        obj = self.get_object_instance(object_class, object_name)
        if obj is None:
            raise ValueError(f"Object '{object_name}' of class '{object_class.__name__}' not found in DataManager.")
        return ObjectAttributesManager.get_attribute(obj, property_name)

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
