# Economic Dispatch Formulation

## Overview

Economic Dispatch Formulation is a project aimed at developing robust and scalable optimization tools 
for day-ahead energy system economic dispatch.

## **Project Structure and Workflow**

This document outlines the **project structure**, **code content** and **user workflow** of the project, which revolves around object creation,
attribute assignment, and validation using a centralized manager.

---

### **Project Structure**

```
src/
├── managers/
│   ├── data_manager.py                  # Manages all objects and relationships
│   ├── object_attributes_manager.py     # Manages object attributes
│   ├── relationship_validator.py        # Enforces rules for objects relationships
├── objects/
│   ├── abstract_object_class.py         # Abstract base class for all objects
│   ├── registry_object_subclasses.py    # Registry of object classes
│   ├── object_classes.py                # ObjectClass class for easy access to AbstractObject subclasses
│   ├── specific_object_classes.py       # Object specificclasses
├── utils/
│   ├── abstract_object_subclasses.py    # AbstractObjects utils for str and class comparison
│   ├── object_classes_loader.py         # Load and build objects/object_class.py to store the AbstractObject subclasses

```

---
### **Code Content**

#### **1. Objects**
Objects represent the fundamental entities in the system, such as `Node`, `Generator`, and others.
All the Objects:
- Are subclasses of `AbstractObject`, that implement the mandatory `object_name`, and default `parent` and `children` attributes.
- Are pure data classes, hence they store attributes.
- Can be retrieved through `ObjectClass`.

#### **2. Object Attributes Manager**
The `ObjectAttributesManager` class is responsible for:
- Setting and getting object attributes.

#### **3. Data Manager**
The `DataManager` acts as the centralized authority. It:
- Dynamically instantiate subclasses of `AbstractObject`.
- Stores all created objects.
- Ensures each object is uniquely registered.
- Manages objects in a structured dictionary format, by storing objects in collections categorized by their class name.
- Uses ObjectManager for attribute handling.
- Uses RelationshipValidator to validate parent-child relationships.

#### **4. Relationship Validator**
The class `RelationshipValidator` enforces rules for object interactions:
- Ensures valid parent-child relationships.

#### **5. Utility Object Class Generator**

- Dynamically loads classes from `specific_object_classes.py`.
- Generates `object_class.py` to centralize access to these classes.
- `load_classes(module_path, module_name)` loads and returns all classes in a module.
- `generate_object_class()`: 
  - Finds `specific_object_classes.py`.
  - Loads its classes.
  - Generates `object_class.py` with structured class imports.
- Runs Automatically (`__main__` block).

```python
class ObjectClass:
    """Auto-generated class for specific object access."""

    from src.objects.specific_object_classes import Node
    Node = Node

#Utilisation
ObjectClass.Node
```

#### **6. Utility Abstract Object**
- Provides helper functions to retrieve and validate subclasses of `AbstractObject`.
- Ensures correct handling of class names as both string representations and actual class references.


