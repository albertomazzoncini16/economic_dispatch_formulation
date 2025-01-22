import importlib.util
import os
import inspect

def load_classes(module_path, module_name):
    """Dynamically load all classes from a module."""
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return {
        name: cls for name, cls in inspect.getmembers(module, inspect.isclass)
        if cls.__module__ == module_name
    }

def generate_object_class():
    """Generate `object_class.py` with all specific object classes."""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    module_path = os.path.join(base_dir, "objects", "specific_object_classes.py")
    module_name = "src.objects.specific_object_classes"

    class_dict = load_classes(module_path, module_name)
    output_file = os.path.join(os.path.dirname(module_path), "object_class.py")

    with open(output_file, "w") as f:
        f.write('class ObjectClass:\n    """Auto-generated class for specific object access."""\n\n')
        for class_name in class_dict:
            f.write(f"    from src.objects.specific_object_classes import {class_name}\n")
            f.write(f"    {class_name} = {class_name}\n\n")

    print(f"ObjectClass structure saved in {output_file}")

# Run automatically if executed directly
if __name__ == "__main__":
    generate_object_class()
