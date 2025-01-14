from src.data.core_objects import GenericCoreObject

class Load(GenericCoreObject):
    def __init__(self, object_name: str, load):
        super().__init__()  # Call CoreObject's __init__
        self.object_name = object_name  # Use the setter for validation
        self.load = load