# Economic Dispatch Formulation

## Overview

Economic Dispatch Formulation is a project aimed at developing robust and scalable optimization tools for day-ahead energy system economic dispatch.

# Project Folder Structure

## `src/`
The main source directory containing all project modules.

- **`data/`**: Defines the main data structures and persistence logic
  - `__init__.py`: Data module initialization
  - **`core_objects/`**: Core system entities
    - `node.py`: Node class
    - `generator.py`: Generator class
    - `load.py`: Load class
    - `data.py`: Data class for metadata or additional attributes
  - **`collections/`**: Grouped object collections
    - `node_collection.py`: NodeCollection class
    - `generator_collection.py`: GeneratorCollection class
    - `load_collection.py`: LoadCollection class
    - `region_collection.py`: RegionCollection class
  - **`dataset/`**: Dataset management
    - `general_dataset.py`: GeneralSystemDataset class
    - `dataset_queries.py`: Query utilities for datasets
  - **`storage/`**: Data persistence logic
    - `parquet_handler.py`: Parquet format handler
    - `json_handler.py`: JSON format handler
    - `csv_handler.py`: CSV format handler
    - `pickle_handler.py`: Pickle format handler (added for saving/loading Python objects)

- **`managers/`**: High-level managers for system control
  - `__init__.py`: Managers module initialization
  - **`system_manager/`**: Manages the entire system
    - `general_manager.py`: Main manager for the system
    - `simulation_manager.py`: Manages simulations and subsets
    - `storage_manager.py`: Handles saving/loading datasets
  - **`metadata_manager/`**: Manages relationships and metadata
    - `memberships.py`: Node-Generator, Node-Load memberships
    - `relationships.py`: Additional relationships and validation

- **`simulations/`**: Subcollections and simulation logic
  - `model_simulation.py`: ModelSimulation class
  - `simulation_queries.py`: Query utilities for simulations

- **`utilities/`**: Reusable utility functions
  - `validation.py`: Validation utilities
  - `queries.py`: Query and filtering utilities
  - `serialization.py`: Save/load helpers

- **`__main__.py`**: Entry point for running the project

