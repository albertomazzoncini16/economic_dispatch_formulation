import importlib.util
import os
import inspect

def load_classes_from_module(module_path, module_name):
    """Dynamically import all classes from a given module file."""
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Extract classes defined in the module (avoid imported ones)
    classes = {
        name: cls for name, cls in inspect.getmembers(module, inspect.isclass)
        if cls.__module__ == module_name
    }
    return classes

def generate_object_class():
    """Dynamically generate object_class.py with all specific object classes."""
    module_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "objects", "specific_object_classes.py")
    module_name = "src.objects.specific_object_classes"

    class_dict = load_classes_from_module(module_path, module_name)

    # Path for the generated object_class.py file
    output_file = os.path.join(os.path.dirname(module_path), "object_class.py")

    with open(output_file, "w") as f:
        f.write("class ObjectClass:\n")
        f.write("    \"\"\"Auto-generated storage for object classes.\"\"\"\n\n")

        for class_name in class_dict.keys():
            f.write(f"    from src.objects.specific_object_classes import {class_name}\n")
            f.write(f"    {class_name} = {class_name}\n\n")

    print(f"Generated ObjectClass structure saved in {output_file}")

# Run this function to regenerate the file
if __name__ == "__main__":
    generate_object_class()
