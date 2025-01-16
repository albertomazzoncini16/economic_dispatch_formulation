import pickle

class DataManager:
    def __init__(self):
        # Dictionary to store collections, keyed by object class name
        self.data_collections = {}

    def _get_or_create_collection(self, object_class):
        """
        Get or create a collection for the specified object class.
        """
        class_name = object_class.__name__
        if class_name not in self.data_collections:
            self.data_collections[class_name] = {}
        return self.data_collections[class_name]

    def add_object(self, object_class, object_name):
        """
        Add a new object to the collection. Ensures unique object names within the collection.
        """
        collection = self._get_or_create_collection(object_class)
        if object_name in collection:
            raise ValueError(f"Object with name '{object_name}' already exists in collection '{object_class.__name__}'.")
        collection[object_name] = object_class(object_name)

    def get_object(self, object_class, object_name):
        """
        Retrieve an object by its name from the collection.
        """
        collection = self._get_or_create_collection(object_class)
        return collection.get(object_name, None)

    def add_property(self, object_class, object_name, property_name, property_value):
        """
        Add or update a property for an object in the collection.
        """
        obj = self.get_object(object_class, object_name)
        if not obj:
            raise ValueError(f"Object with name '{object_name}' does not exist in collection '{object_class.__name__}'.")
        setattr(obj, property_name, property_value)

    def add_membership(self, child_class, child_name, parent_class, parent_name):
        """
        Establish a parent-child relationship between two objects.
        """
        child = self.get_object(child_class, child_name)
        parent = self.get_object(parent_class, parent_name)

        if not child:
            raise ValueError(f"Child object '{child_name}' does not exist in collection '{child_class.__name__}'.")
        if not parent:
            raise ValueError(f"Parent object '{parent_name}' does not exist in collection '{parent_class.__name__}'.")

        if child in parent.children:
            raise ValueError(f"Child '{child_name}' is already a member of parent '{parent_name}'.")
        parent.add_child(child)

    def list_objects(self, object_class):
        """
        List all objects in the collection for the specified class.
        """
        collection = self._get_or_create_collection(object_class)
        return list(collection.keys())

    def find_objects_by_property(self, object_class, property_name, property_value):
        """
        Find objects with a specific property value.
        """
        collection = self._get_or_create_collection(object_class)
        return [
            obj_name for obj_name, obj in collection.items()
            if hasattr(obj, property_name) and getattr(obj, property_name) == property_value
        ]

    def save_to_file(self, filename: str):
        """
        Save the current state of data collections to a file.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self.data_collections, file)

    def load_from_file(self, filename: str):
        """
        Load data collections from a file.
        """
        with open(filename, 'rb') as file:
            self.data_collections = pickle.load(file)