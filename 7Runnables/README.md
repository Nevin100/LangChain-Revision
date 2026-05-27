# 📖 Folder 7: Runnables

## 🎯 Objective

Understand LangChain's fundamental composable primitives. Build complex workflows with Runnables - they are the foundation of Chains.

## 📚 Theory & Concepts

### **Runnable - Basic Unit**

```
Runnable = Anything that can execute a task

Examples:
├── LLM (ChatGroq) - Takes input, generates output
├── Prompt - Formats input
├── OutputParser - Parses output
├── Custom Function - Any Python function
└── Chain - Composition of above
```

### **Runnable Interface (Core Methods)**

```python
class Runnable:
    def invoke(input):        # Synchronous execution
        """Execute and wait for result"""
    
    def ainvoke(input):       # Asynchronous execution
        """Execute asynchronously"""
    
    def stream(input):        # Streaming output
        """Real-time output as it's generated"""
    
    def astream(input):       # Async streaming
        """Async real-time output"""
    
    def batch(inputs):        # Multiple inputs
        """Process multiple inputs efficiently"""
```

### **Composition Patterns**

```
1. RunnableSequence (A | B)
   └── Output of A becomes input to B

2. RunnableParallel (RunnableParallel({...}))
   └── Multiple runnables run together

3. RunnableLambda
   └── Wrap Python function as Runnable

4. RunnableBranch
   └── Conditional routing
```

### **Runnable State Flow**

```
Input → Type Checking → Execution → Output Validation → Output

Features:
├── Composable (| operator)
├── Reusable (same everywhere)
├── Testable (predictable behavior)
├── Async-first (both sync and async)
└── Typed (input/output types)
```

## 📁 Files Overview

### **part1/**
```
Purpose: Basic Runnable concepts
File: runnable1.py
Content: Square, Sum examples
```

### **part2/**
```
Purpose: Advanced patterns
Files:
- Runnable_Parallel.py - Parallel execution
- Runnable_Sequence.py - Sequential execution
```

## 🔑 Key Learning Points

### **1. Basic Runnable - Custom Class**

```python
from langchain_core.runnables import Runnable
from langchain_core.language_model import LanguageModel

class SquareRunnable(Runnable):
    def invoke(self, input: int) -> int:
        """Square a number"""
        return input ** 2
    
    def batch(self, inputs: list[int]) -> list[int]:
        """Square multiple numbers"""
        return [x ** 2 for x in inputs]

# Usage
square = SquareRunnable()
square.invoke(5)          # 25
square.batch([2, 3, 4])   # [4, 9, 16]
```

### **2. RunnableLambda - Function Wrapper**

```python
from langchain_core.runnables import RunnableLambda

# Wrap any function
def multiply_by_two(x):
    return x * 2

multiplier = RunnableLambda(multiply_by_two)
multiplier.invoke(5)      # 10

# In chains
chain = prompt | model | RunnableLambda(multiply_by_two)
```

### **3. RunnableSequence (A | B)**

```python
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StringOutputParser
from langchain_core.runnables import RunnableLambda

template = "What is {number} squared?"
prompt = PromptTemplate(template=template, input_variables=["number"])
model = ChatGroq(...)
parser = StringOutputParser()

# Sequence = prompt | model | parser
sequence = prompt | model | parser

# This is RunnableSequence internally
result = sequence.invoke({"number": 5})
```

### **4. RunnableParallel**

```python
from langchain_core.runnables import RunnableParallel, RunnableLambda

def joke(x):
    return f"Why did {x} cross the road?"

def explanation(x):
    return f"The {x} was trying to get somewhere else."

joke_runner = RunnableLambda(joke)
explain_runner = RunnableLambda(explanation)

parallel = RunnableParallel(
    joke=joke_runner,
    explanation=explain_runner
)

result = parallel.invoke("chicken")
# result = {
#     "joke": "Why did chicken cross the road?",
#     "explanation": "The chicken was trying to..."
# }
```

### **5. RunnableBranch (Conditional)**

```python
from langchain_core.runnables import RunnableBranch

def is_math_question(input):
    return "math" in input["question"].lower()

math_runner = RunnableLambda(lambda x: f"Solving: {x}")
general_runner = RunnableLambda(lambda x: f"Answering: {x}")

branch = RunnableBranch(
    (is_math_question, math_runner),  # If condition true, use math_runner
    (lambda x: True, general_runner)  # Else use general_runner (catch-all)
)

branch.invoke({"question": "What is 2+2?"})  # Math path
branch.invoke({"question": "What is Python?"})  # General path
```

## 💡 Practical Patterns

### **Pattern 1: Data Processing Pipeline**

```python
# Step 1: Extract
extract = RunnableLambda(lambda text: text.split())

# Step 2: Filter
filter_runner = RunnableLambda(lambda words: [w for w in words if len(w) > 3])

# Step 3: Uppercase
upper = RunnableLambda(lambda words: [w.upper() for w in words])

# Pipeline
pipeline = extract | filter_runner | upper

result = pipeline.invoke("hello world python programming")
# ["HELLO", "WORLD", "PYTHON", "PROGRAMMING"]
```

### **Pattern 2: Parallel Analysis**

```python
def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text)

def avg_word_length(text):
    words = text.split()
    return len(text) / len(words) if words else 0

analysis = RunnableParallel(
    word_count=RunnableLambda(count_words),
    char_count=RunnableLambda(count_chars),
    avg_length=RunnableLambda(avg_word_length)
)

result = analysis.invoke("Hello world python")
# {
#     "word_count": 3,
#     "char_count": 18,
#     "avg_length": 6.0
# }
```

### **Pattern 3: Conditional Processing**

```python
def is_long(text):
    return len(text) > 100

short_processor = RunnableLambda(lambda x: f"Short: {x[:50]}...")
long_processor = RunnableLambda(lambda x: f"Long: Summarizing {len(x)} chars")

text_router = RunnableBranch(
    (is_long, long_processor),
    (lambda x: True, short_processor)
)
```

## 📊 Runnable Execution Methods

```
invoke(input)          | Synchronous, waits for result
ainvoke(input)         | Async, use with await
stream(input)          | Real-time streaming output
astream(input)         | Async streaming
batch(inputs)          | Multiple at once
abatch(inputs)         | Async batch
```

## 🎓 Advanced Concepts

### **Type Hints in Runnables**

```python
from typing import Dict, Any

class TypedRunnable(Runnable):
    input_type = Dict[str, Any]
    output_type = Dict[str, str]
    
    def invoke(self, input: Dict[str, Any]) -> Dict[str, str]:
        return {"result": str(input)}

# Runtime type checking possible
```

### **Error Handling in Chains**

```python
from langchain_core.runnables import RunnableLambda

def safe_divide(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return "Error: Division by zero"

safe_runner = RunnableLambda(safe_divide)

# Won't crash
result = safe_runner.invoke(0)  # "Error: Division by zero"
```

### **Async Execution**

```python
import asyncio

async def async_example():
    result = await model.ainvoke(message)
    return result

# Run
asyncio.run(async_example())
```

## 📈 Performance Characteristics

```
Method       | Latency | Throughput | When to Use
─────────────────────────────────────────────────
invoke()     | ~1sec   | 1 req/sec  | Single request
batch()      | ~5sec   | 4 req/sec  | 4 requests
astream()    | ~1sec   | Streaming  | Real-time
parallel     | ~2sec   | 4x combo   | Multi-tasks
```

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Type error in chain | Check output type of previous matches input |
| Slow execution | Use parallel instead of sequential |
| Async error | Use ainvoke() not invoke() in async context |
| Memory exceeded | Use batch with smaller batch size |

## 💡 Pro Tips

1. **Use RunnableLambda**: Wrap simple functions easily
2. **Parallel**: Always parallelize independent operations
3. **Type Checking**: Enable at development time
4. **Streaming**: Use for real-time user feedback
5. **Caching**: Cache expensive operations

## 🔄 Runnable vs Function

```
Function:
├── Not composable
├── Manual chaining
└── Error prone

Runnable:
├── Composable (| operator)
├── Automatic typing
├── Error handling
└── Streaming support
```

## 📚 Runnable Hierarchy

```
Runnable (Base)
├── Prompt
├── LanguageModel
├── OutputParser
├── RunnableLambda
├── RunnableSequence (A | B)
├── RunnableParallel
├── RunnableBranch
└── Custom Runnables
```

## 🚀 Next Steps

1. **Folder 6**: Use Runnables in Chains (built on Runnables)
2. **Folder 12**: Runnables in RAG pipelines
3. **Create custom**: Build your own Runnable classes

## 📝 Summary

| Concept | Purpose | Example |
|---------|---------|---------|
| Runnable | Base primitive | ChatGroq, Prompt |
| RunnableSequence | A → B flow | chain1 \| chain2 |
| RunnableParallel | Simultaneous execution | Parallel({...}) |
| RunnableBranch | Conditional logic | If-else routing |
| RunnableLambda | Function wrapper | Lambda(func) |

---

**Runnables Mastered! 🏃**