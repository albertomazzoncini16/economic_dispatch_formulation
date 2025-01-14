# Economic Dispatch Formulation

## Overview

Economic Dispatch Formulation is a project aimed at developing robust and scalable optimization tools for day-ahead energy system economic dispatch.

## **Project Structure and Workflow**

This document outlines the **hierarchy** and **workflow** of the system. The goal is to manage objects, their collections, and relationships efficiently using a centralized manager.

---

### **Hierarchy**

#### **1. Core Objects**
Core objects represent the fundamental entities in the system, such as `Node`, `Generator`, and `Fuel`. All core objects:
- Inherit from a base abstract class `CoreObject`.
- Contain attributes like `object_name` and relationships such as `parent` and `children`.

#### **2. Object Collections**
Object collections manage groups of core objects of the same type. Each collection:
- Inherits from a base class `ObjectCollection`.
- Provides methods to:
  - Add objects (`add_object`).
  - Add properties to objects (`add_property`).
  - Define relationships between objects (`add_membership`).
- Handles object-specific logic (e.g., `NodeCollection` manages parent-child relationships).

#### **3. DataCollectionsManager**
The `DataCollectionsManager` acts as the centralized authority. It:
- Dynamically initializes collections as needed.
- Stores all collections in a centralized storage.
- Provides a unified interface to:
  - Add objects across collections.
  - Add properties to objects.
  - Create memberships between objects.

#### **4. SystemManager**
The `SystemManager` initializes the `DataCollectionsManager` and serves as the primary entry point for user actions.

---

### **Workflow**

#### **1. Initialization**
- The `SystemManager` initializes the `DataCollectionsManager`, which lazily creates collections when needed.
- Collections are stored in a central `collections_storage` dictionary in the `DataCollectionsManager`.

#### **2. Adding Objects**
1. Call `DataCollectionsManager.add_object(object_class, object_name, **kwargs)`.
2. The manager:
   - Retrieves or initializes the appropriate collection.
   - Delegates the creation of the object to the collection.

#### **3. Adding Properties**
1. Call `DataCollectionsManager.add_property(object_class, object_name, property_name, property_value)`.
2. The manager:
   - Retrieves the appropriate collection.
   - Delegates the addition of the property to the collection.

#### **4. Creating Memberships**
1. Call `DataCollectionsManager.add_membership(child_object_class, child_object_name, parent_object_class, parent_object_name)`.
2. The manager:
   - Retrieves the appropriate collections for the child and parent objects.
   - Delegates the creation of the relationship to the relevant collection(s).

---

### **Example Usage**

#### Adding Objects

```python
# Add a node
manager.add_object("Node", "Node1")

# Add another node
manager.add_object("Node", "Node2")

# Add a generator
manager.add_object("Generator", "Gen1", capacity=100)
```

#### Adding Properties

```python
# Add properties to nodes
manager.add_property("Node", "Node1", "voltage", 110)
manager.add_property("Node", "Node2", "voltage", 220)
```

#### Creating Memberships

```python
# Create a parent-child relationship between nodes
manager.add_membership("Node", "Node2", "Node", "Node1")

# Link a generator to a node
manager.add_membership("Generator", "Gen1", "Node", "Node1")
```

---

### **Data Flow**

1. **Object Creation**:
   - When `add_object` is called, the `DataCollectionsManager` initializes the required collection (if it doesn’t already exist) and delegates object creation.

2. **Property Addition**:
   - The `DataCollectionsManager` ensures properties are added to the correct object within its respective collection.

3. **Membership Creation**:
   - Relationships are added via `add_membership`. The relevant collections validate and enforce relationship rules (e.g., parent-child constraints).

---

### **Project Structure**

```
src/
├── core_objects/
│   ├── core_object.py         # Abstract base class for all core objects
│   ├── node.py                # Node class
│   ├── generator.py           # Generator class
│   ├── fuel.py                # Fuel class
│
├── collections/
│   ├── object_collection.py   # Base class for all collections
│   ├── node_collection.py     # NodeCollection class
│   ├── generator_collection.py # GeneratorCollection class
│
├── managers/
│   ├── data_collections_manager.py  # Manages all collections and relationships
│   ├── system_manager.py            # Entry point for the system
```

---

### **Benefits of This Design**

1. **Centralized Management**:
   - The `DataCollectionsManager` simplifies interactions across collections, providing a single point of control.

2. **Lazy Initialization**:
   - Collections are created only when needed, optimizing resource usage.

3. **Extensibility**:
   - Adding new object types or collections (e.g., `TransformerCollection`) requires minimal changes.

4. **Scalability**:
   - The design handles complex relationships (e.g., hierarchical or many-to-many) while maintaining clarity.

5. **Encapsulation**:
   - Each collection enforces rules and logic specific to its object type.

---

### **Next Steps**

- **Test Relationships**:
  - Verify parent-child relationships and cross-object linking.
- **Extend Functionality**:
  - Add new object types or rules for membership and property management.
- **Optimize Queries**:
  - Add methods to retrieve and query relationships or objects based on conditions.
