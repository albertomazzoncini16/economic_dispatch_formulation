from abc import ABC
from src.managers.relationship_manager import RelationshipManager
class AbstractObject(ABC):

    def __init__(self, object_name):
        self.object_name = object_name
        self.parent = None
        self.children = []

    def add_child(self, child):
        """
        Add a child object to this object if allowed by RelationshipManager.
        """
        if not RelationshipManager.is_valid_child(self, child):
            raise ValueError(f"{child.__class__.__name__} is not a valid child of {self.__class__.__name__}.")

        if child in self.get_ancestor_chain():
            raise ValueError(f"Circular reference detected: {child.object_name} is already an ancestor of {self.object_name}.")

        if child not in self.children:
            self.children.append(child)
            child.parent = self

    def validate_parent(self):
        """
        Validate that this object has a valid parent based on RelationshipManager.
        """
        if not RelationshipManager.is_valid_parent(self, self.parent):
            required_parents = RelationshipManager.rules.get(type(self), {}).get("parent", ())
            required_names = ", ".join([cls.__name__ for cls in required_parents])
            raise ValueError(f"{self.__class__.__name__} '{self.object_name}' must have a parent of type '{required_names}'.")

    def get_ancestor_chain(self):
        """
        Retrieve all ancestors of the current object.
        Returns:
            set: A set containing all ancestor objects.
        """
        ancestors = set()
        current = self
        while current.parent:
            ancestors.add(current.parent)
            current = current.parent
        return ancestors

    def get_all_descendants(self):
        """
        Retrieve all descendants of the current object.
        Returns:
            list: A list containing all descendant objects.
        """
        descendants = []
        stack = self.children[:]
        while stack:
            child = stack.pop()
            descendants.append(child)
            stack.extend(child.children)
        return descendants

    def remove_child(self, child):
        """
        Remove a child object from this object.
        Args:
            child (AbstractObject): The child object to remove.
        """
        if child in self.children:
            self.children.remove(child)
            child.parent = None

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
