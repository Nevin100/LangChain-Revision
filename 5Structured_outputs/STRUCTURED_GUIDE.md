# 📖 Folder 5.1: Structured Outputs

## 🎯 Purpose

Type-safe, validated outputs from LLMs using Pydantic models, TypedDict, and JSON schemas.

## 📁 Files

### **json_schema.py**
```
Raw JSON schema definition
LLM specifies the exact structure
```

### **pydantic_ex.py**
```
Pydantic BaseModel with validation
Best for: Complex models with relationships
```

### **typed_Dict.py**
```
Lightweight type hints
Best for: Simple structures
```

### **ps.py**
```
Pydantic with detailed field annotations
Best for: Self-documenting code
```

## 🔑 Quick Start

```python
# Pydantic (RECOMMENDED)
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(description="Full name")
    age: int = Field(ge=0, le=150)

model = ChatGroq(...)
structured_model = model.with_structured_output(Person)
result = structured_model.invoke("John is 25")
# result.name == "John"
```

---

**Structured Outputs Quick Guide! 📋**