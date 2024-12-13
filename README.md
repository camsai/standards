# CAMSAI Standards

The **CAMSAI Standards** repository defines and maintains a set of consistent schemas, validation tools, and data standards for materials science data and AI-driven research workflows. These standards ensure the interoperability, reproducibility, and scalability of materials-related datasets and applications across the CAMSAI ecosystem.

---

## **Purpose**

This repository provides:
- **Data Models**: Pydantic-based schemas for defining and validating data structures.
- **Validation Utilities**: Tools to ensure data compliance with established standards.
- **Interoperability Support**: Standards that facilitate seamless collaboration between different systems, tools, and workflows.

---

## **Key Features**

1. **Schema Definitions**
   - Comprehensive data models for common materials science objects.
   - Designed for compatibility with CAMSAI workflows and third-party applications.

2. **Validation Tools**
   - Python utilities to validate data against the defined standards.
   - Example workflows for integrating validation into your projects.

3. **Interoperability**
   - Supports data exchange and integration across various CAMSAI and external platforms.

---

## **Repository Structure**

- **`src/py/camsai/standards`**  
  Contains Python files defining the Pydantic schemas for various data models by source/provider (e.g., Mat3ra.com).
  
---

## **Installation**

### Using `pip`:
You can install the repository using `pip` (requires Python 3.8+):
```bash
pip install camsai-standards
```

or from GitHub:

```bash
pip install git+https://github.com/camsai/standards.git
```

### In JupyterLite:
Install the package in a Pyodide-based JupyterLite environment:
```python
await micropip.install("camsai-standards")
```

---

## **Usage**

### Example: Validating a Material Schema
```python
from camsai.standards.mat3ra import Mat3raMaterialSchema
from camsai.standards import is_valid

# Example material data
material_data = {...}

# Validate data
if is_valid(Mat3raMaterialSchema, material_data):
    print("Valid material data")
else:
    print("Invalid material data")
```

### Example: Using Predefined Examples
```python
from mat3ra.esse.data.examples import EXAMPLES

example_material = next((e for e in EXAMPLES if e["path"] == "material"), None)["data"]
print(example_material)
```

---

## **Contributing**

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a branch for your changes:
   ```bash
   git checkout -b feature/new-schema
   ```
3. Commit your changes and open a pull request.

Please ensure all contributions are consistent with existing standards and include tests where applicable.

---

## **License**

This repository is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For questions or feedback, contact us at:
- **Email**: [info@camsai.org](mailto:info@camsai.org)
- **Website**: [CAMSAI - Consortium for the Advancement of Materials Science with AI](https://camsai.org)
