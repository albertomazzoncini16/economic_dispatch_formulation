# Economic Dispatch Formulation

## Overview

Economic Dispatch Formulation is a project aimed at developing robust and scalable optimization tools for day-ahead 
energy system economic dispatch. This system efficiently manages objects, their collections, and relationships 
using a centralized management approach.

---

## **Project Structure and Workflow**

This document outlines the **hierarchy**, **workflow**, and **efficiency advantages** of the system.

### **Hierarchy**
 
#### **1. Objects**
Objects represent fundamental entities such as `Node`, `Generator`, `Fuel`, and `Load`. These objects inherit 
from a base abstract class `AbstractObject` attributes such as `object_name` and relationships like `parent` 
and `children`.

#### **2. Objects Database**
The `objects_database` serves as a structured registry where objects are stored by class type. This provides:
- **O(1) lookup efficiency** for retrieving objects.
- Organized and easily accessible storage using a **nested dictionary**:
  ```python
  objects_database = { "ClassName": {"ObjectName": ObjectInstance}}
  objects_database = { "Node": {"node_16": Node(object_name='node_16')}}
  ```

#### **3. Relationship Validation**
The `RelationshipValidator` acts as a **rule enforcer** for object relationships. It:
- Defines **valid parent-child relationships**.
- Ensures that **only allowed relationships are set**.
- Does **not store relationships** but only validates them.

#### **4. DataManager**
The `DataManager` serves as the **central controller** and:
- Manages all objects inside `objects_database`.
- Uses `RelationshipValidator` to ensure valid relationships.
- Provides an interface to:
  - Add objects.
  - Add properties to objects.
  - Define relationships (`add_membership`).
  - Export data to CSV files.

---

### **Workflow**

#### **1. Initialization**
- The `DataManager` initializes the `objects_database`.
- Objects are stored under their class type within `objects_database`.

#### **2. Adding Objects**
1. Call `DataManager.add_object(object_instance)`.
2. The object is categorized inside `objects_database` under its class type.

#### **3. Adding Properties**
1. Call `DataManager.add_property(object_class, object_name, property_name, property_value)`.
2. The manager retrieves the object and updates its attributes.

#### **4. Creating Memberships**
1. Call `DataManager.add_membership(child_class, child_name, parent_class, parent_name)`.
2. The manager:
   - Uses `RelationshipValidator` to validate the relationship.
   - If valid, updates the parent-child attributes in `AbstractObject`.

#### **5.**

---

### **Example Usage**

#### Adding Objects
```python
# Add a node
manager.add_object(Node(object_name="node_16"))

# Add a generator
manager.add_object(Generator(object_name="gen_32"))
```

#### Adding Properties
```python
# Add properties to nodes
manager.add_property(Generator, "gen_32", "nominal_power", 100.0)
```

#### Creating Memberships
```python
# Link a generator to a node
manager.add_membership(Generator, "Gen1", Node, "Node1")
```

#### Exporting Data to CSV
```python
# Export all objects to CSV files (one per class)
manager.export_to_csv("exports/")
```

---

### **Project Structure**

```
src/
├── core_objects/
│   ├── abstract_object.py       # Base class for all objects
│   ├── node.py                  # Node class
│   ├── generator.py             # Generator class
│   ├── fuel.py                  # Fuel class
│
├── managers/
│   ├── data_manager.py          # Manages all objects and relationships
│   ├── relationship_validator.py # Validates relationships
│
├── utils/
│   ├── export_utils.py          # Handles CSV exporting
│
├── main.py                      # Entry point for execution
```

---

### **Advantages of This Design**

1. **O(1) Lookup Efficiency**:
   - Using a **nested dictionary (`objects_database`)** enables constant-time object retrieval.

2. **Centralized Object Management**:
   - `DataManager` provides a single interface for managing all objects and relationships.

3. **Strict Relationship Validation**:
   - `RelationshipValidator` ensures that only valid relationships are created.

4. **Scalability**:
   - Easily add new object types or extend validation rules without modifying the core logic.

5. **Data Export Capabilities**:
   - Each object class has its own CSV file, making reporting easier.

---

### **Next Steps**

- **Implement Relationship Queries**:
  - Add functions to retrieve all ancestors or descendants of an object.

- **Enhance Data Exporting**:
  - Support exporting relationships alongside objects.

- **Logging & Debugging**:
  - Add logging for object creations, modifications, and relationship changes.

---

This structure ensures a **robust, efficient, and scalable approach** for managing economic dispatch data. 🚀

