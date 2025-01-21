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
│   ├── specific_object_classes.py       # Object classes
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
