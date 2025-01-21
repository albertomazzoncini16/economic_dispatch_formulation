from src.objects.abstract_object_class import AbstractObject

class SubClassesRegistry:
    """A registry that provides dot notation access to AbstractObject subclasses."""
    def __init__(self):
        self._classes = {cls.__name__: cls for cls in AbstractObject.__subclasses__()}

    def __getattr__(self, name):
        if name in self._classes:
            return self._classes[name]
        raise AttributeError(f"{name} is not a registered subclass of AbstractObject.")

    def __dir__(self):
        return list(self._classes.keys())

    def list_classes(self) -> list:
        """Returns a list of all registered subclass names."""
        return list(self._classes.keys())
