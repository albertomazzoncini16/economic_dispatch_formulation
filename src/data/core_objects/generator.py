from src.data.core_objects import GenericCoreObject

class Generator(GenericCoreObject):
    def __init__(self, object_name: str, max_capacity):
        super().__init__()  # Call CoreObject's __init__
        self.object_name = object_name  # Use the setter for validation
        self.max_capacity = max_capacity