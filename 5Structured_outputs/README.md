# 📖 Folder 5: Structured Outputs

## 🎯 Objective

Get reliable, type-safe, validated outputs from LLMs (JSON, Pydantic models, TypedDict format). Ensure responses are in the expected format.

## 📚 Theory & Concepts

### **Problem: Unstructured LLM Outputs**

```
Unstructured (Raw Text):
User: "Extract name and age from: John is 25 years old"
LLM: "The person's name is John and he is 25 years old"
Issue: ❌ Need manual parsing, errors possible

Structured (Type-Safe):
{
    "name": "John",
    "age": 25
}
Issue: ✅ Direct use, type guaranteed
```

### **Output Formatting Methods**

```
1. JSON Schema
   └─ Give LLM a specific JSON structure

2. Pydantic Models
   └── Python objects with validation

3. TypedDict
   └── Type hints for dictionaries

4. Annotated Fields
   └── Detailed descriptions for fields
```

### **With Structured Output Method**

```
Normal LLM:
Input: "Extract info"
Output: "Free-form text with info scattered"

With with_structured_output():
Input: "Extract info"
LLM internally constrains: "Output MUST be valid JSON with these fields"
Output: Guaranteed valid structured response
Output: Valid, parseable structured data
```

### **Three Output Scenarios**

```
Scenario 1: Structured Outputs (Folder 5)
├── defined schema
└── LLM follows format strictly

Scenario 2: Unstructured (Old way)
├── Free-form text
└── Manual parsing required

Scenario 3: Semi-Structured (Folder 1-2)
├── Natural language
└── Partially predictable
```

## 📁 Subfolder Structure

### **📂 structured_outputs/ (Type-Safe)**

#### **json_schema.py**
```
Purpose: Raw JSON schema definition
Method: with_structured_output(json_schema=...)
Use: Direct JSON structure specification
```

#### **pydantic_ex.py**
```
Purpose: Python objects with validation
Method: with_structured_output(pydantic_model)
Use: Type hints, validators, relationships
Best for: Complex data models
```

#### **typed_Dict.py**
```
Purpose: Lightweight type hints
Method: with_structured_output(TypedDict)
Use: Simple structures, less overhead
Best for: Quick structured outputs
```

#### **ps.py (Probably "Pydantic Schema")**
```
Purpose: Enhanced Pydantic with Field descriptions
Method: Annotated fields with details
Use: Self-documenting models
```

### **📂 unstructured_outputs/ (Flexible)**

#### **output_parsers1.py**
```
Purpose: Basic output parsing
Method: StringOutputParser
Use: Simple string extraction
```

## 🔑 Key Learning Points

### **1. JSON Schema Method**

```python
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_groq import ChatGroq

# Define schema
json_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["name", "age"]
}

model = ChatGroq(model="llama-3.1-8b-instant")
structured_model = model.with_structured_output(json_schema)

# Usage
result = structured_model.invoke("John is 25 years old")
# result: {"name": "John", "age": 25}
```

### **2. Pydantic Model Method (BEST)**

```python
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(description="Person's full name")
    age: int = Field(description="Person's age in years", ge=0, le=150)
    email: str = Field(description="Email address")

model = ChatGroq(model="llama-3.1-8b-instant")
structured_model = model.with_structured_output(Person)

# Usage
result = structured_model.invoke("John is 25 and his email is john@example.com")
# result is Person instance with validation
print(result.name, result.age)  # "John", 25
```

### **3. TypedDict Method**

```python
from typing import TypedDict

class PersonDict(TypedDict):
    name: str
    age: int
    email: str

model = ChatGroq(model="llama-3.1-8b-instant")
structured_model = model.with_structured_output(PersonDict)

# Usage
result = structured_model.invoke("...")
# result: {"name": "John", "age": 25, "email": "..."}
```

### **4. Annotated Fields (Enhanced Pydantic)**

```python
from pydantic import BaseModel, Field
from typing import Annotated

class Person(BaseModel):
    name: Annotated[str, Field(description="Full name")]
    age: Annotated[int, Field(description="Age", ge=0)]
    score: Annotated[float, Field(description="Score 0-100")]
```

## 💡 Practical Patterns

### **Pattern 1: Information Extraction**

```python
from pydantic import BaseModel

class Contact(BaseModel):
    name: str
    phone: str
    email: str
    address: str

model = ChatGroq(...)
extractor = model.with_structured_output(Contact)

text = "Call John at 555-1234 or john@email.com, lives at 123 Main St"
contact = extractor.invoke(text)
# contact.name == "John"
# contact.phone == "555-1234"
```

### **Pattern 2: Entity Recognition**

```python
class Entity(BaseModel):
    text: str
    type: str  # "PERSON", "ORG", "LOCATION"
    confidence: float

class Entities(BaseModel):
    items: list[Entity]

model = ChatGroq(...)
recognizer = model.with_structured_output(Entities)

text = "Apple CEO Tim Cook announced new products"
entities = recognizer.invoke(text)
# entities.items[0] -> Entity(text="Tim Cook", type="PERSON", confidence=0.95)
```

### **Pattern 3: Sentiment Analysis**

```python
class Sentiment(BaseModel):
    text: str
    label: str  # "positive", "negative", "neutral"
    score: float  # -1 to 1

model = ChatGroq(...)
analyzer = model.with_structured_output(Sentiment)

result = analyzer.invoke("This product is amazing!")
# result.label == "positive"
# result.score == 0.95
```

### **Pattern 4: Multi-Step Extraction**

```python
class Review(BaseModel):
    rating: int  # 1-5
    pros: list[str]
    cons: list[str]
    summary: str

model = ChatGroq(...)
reviewer = model.with_structured_output(Review)

result = reviewer.invoke("Great product but expensive")
# result.rating == 4
# result.pros == ["Great quality"]
# result.cons == ["Expensive"]
```

## 🔄 Output Formatting Comparison

| Method | Best For | Complexity | Validation |
|--------|----------|-----------|-----------|
| JSON Schema | Raw JSON | Simple | Basic |
| Pydantic | Complex models | Medium-High | Strict ✅ |
| TypedDict | Quick structs | Low-Medium | Type hints |
| Annotated | Self-docs | Medium | Enhanced |

## 🎓 Validation with Pydantic

### **Field Validators**

```python
from pydantic import BaseModel, field_validator

class Person(BaseModel):
    name: str
    age: int
    
    @field_validator('age')
    @classmethod
    def age_must_be_valid(cls, v):
        if not 0 <= v <= 150:
            raise ValueError('Age must be between 0 and 150')
        return v

# Usage: Automatic validation
person = Person(name="John", age=200)  # ❌ Raises ValidationError
person = Person(name="John", age=25)   # ✅ Valid
```

### **Constraints**

```python
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=150)  # >= 0, <= 150
    email: str = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    score: float = Field(ge=0.0, le=1.0)
```

## 📊 Use Cases

### **1. Structured Logging**

```python
class Log(BaseModel):
    timestamp: str
    level: str  # "INFO", "ERROR", "WARNING"
    message: str
    component: str

# LLM generates structured logs
```

### **2. API Response Generation**

```python
class APIResponse(BaseModel):
    status: str
    data: dict
    error: str | None

# LLM formats API-compliant responses
```

### **3. Data Processing Pipeline**

```python
class Document(BaseModel):
    title: str
    content: str
    tags: list[str]
    category: str

# LLM extracts structured documents
```

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Invalid JSON | Add error handling, use `try_parse_json` |
| Validation fails | Adjust constraints, use coerce |
| LLM ignores schema | Use `with_structured_output()` |
| Type mismatch | Ensure LLM prompt is clear |

## 💡 Pro Tips

1. **Pydantic First**: Use Pydantic for complex models (best validation)
2. **Field Descriptions**: Always add descriptions for LLM guidance
3. **Constraints**: Use Field limits (ge, le, min_length, etc.)
4. **Error Handling**: Wrap in try-except for robustness

## 📚 Pydantic Best Practices

```python
from pydantic import BaseModel, Field
from typing import Optional

class BestPractice(BaseModel):
    # 1. Always provide descriptions
    name: str = Field(description="Full name of person")
    
    # 2. Use Optional for nullable fields
    middle_name: Optional[str] = None
    
    # 3. Add constraints
    age: int = Field(ge=0, le=150, description="Age in years")
    
    # 4. Use enums for limited options
    status: str = Field(enum=["active", "inactive"])
    
    # 5. List for collections
    tags: list[str] = Field(description="Associated tags")
```

## 🚀 Next Steps

1. **Chains (Folder 6)**: Use structured outputs in pipelines
2. **Document Processing**: Extract structured data from documents
3. **Database Insertion**: Direct DB inserts from validated data

## 📝 Method Comparison

```
Method              | Setup Time | Validation | Flexibility | Use
────────────────────────────────────────────────────────────────
JSON Schema         | Fast       | Basic      | High        | APIs
Pydantic           | Medium     | Strong ✅   | Medium      | Apps
TypedDict          | Very Fast  | Weak       | Low         | Quick
String Parser      | Instant    | None       | High        | Simple
```

---

**Type-Safe Outputs Achieved! ✅**