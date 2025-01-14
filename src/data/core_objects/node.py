from src.data.core_objects import GenericCoreObject

class Node(GenericCoreObject):
    def __init__(self, object_name: str):
        super().__init__()  # Call CoreObject's __init__
        self.object_name = object_name  # Use the setter for validation