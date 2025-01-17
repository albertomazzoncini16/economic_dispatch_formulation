
class AbstractObject:

    def __init__(self, object_name: str):
        self.object_name = object_name
        self.parent = {}
        self.children = {}

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

    def add_child(self, child_object_class: "AbstractObject", child_object_name: str):
        """Add a child object and store it as {class_name: [object_names]}."""
        child_class_name = child_object_class.__name__

        if child_class_name not in self.children:
            self.children[child_class_name] = []

        self.children[child_class_name].append(child_object_name)

    def add_parent(self, parent_object_class: "AbstractObject", parent_object_name: str):
        """Assign a parent to this object."""
        parent_class_name = parent_object_class.__name__

        if parent_class_name not in self.parent and not self.parent:
            self.parent[parent_class_name] = []

        self.parent[parent_class_name].append(parent_object_name)

    def get_parent(self) -> list:
        """Retrieve this object's parent."""
        all_parent = []
        for parent_list in self.parent.values():
            all_parent.extend(parent_list)  # Flatten all parent names
        return all_parent

    def get_all_children(self) -> list[str]:
        """Retrieve a flat list of all children across all class types."""
        all_children = []
        for child_list in self.children.values():
            all_children.extend(child_list)  # Flatten all child names
        return all_children

