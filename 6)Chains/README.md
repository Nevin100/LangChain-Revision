# 📖 Folder 6: Chains

## 🎯 Objective

Compose LLMs, Prompts, and Output Parsers to build reusable workflows. Use the pipe operator `|` to build complex applications.

## 📚 Theory & Concepts

### **Chain - Building Block Concept**

```
Chain = Prompt → Model → Output Parser

Example:
"What is Python?" 
    ↓
Prompt Template (format question)
    ↓
LLM (generate answer)
    ↓
Output Parser (parse response)
    ↓
Structured Output: {"answer": "..."}
```

### **Pipe Operator (|) - Composability**

```
Instead of:
result1 = prompt.invoke(input)
result2 = model.invoke(result1)
result3 = parser.parse(result2)

Use:
chain = prompt | model | parser
result = chain.invoke(input)

Cleaner, more readable, composable!
```

### **Chain Types in This Folder**

```
1. Simple Chain
   Prompt → Model → Parser
   └── One step linear flow

2. Sequential Chain
   Chain1 → Chain2 → Chain3
   └── Output of one is input to next

3. Parallel Chain
   ├── Chain1
   ├── Chain2  (Run simultaneously)
   └── Chain3
   └── Results combined

4. Conditional Chain
   If condition A: Use ChainX
   Else: Use ChainY
   └── Runtime decision making
```

### **PromptTemplate - Dynamic Prompts**

```python
from langchain_core.prompts import PromptTemplate

template = "You are an expert in {topic}. Answer: {question}"
prompt = PromptTemplate(
    template=template,
    input_variables=["topic", "question"]
)

# Usage
prompt.format(topic="Python", question="List libraries")
# Output: "You are an expert in Python. Answer: List libraries"
```

### **Output Parser - Result Extraction**

```
Raw LLM Output:
"The answer is [1, 2, 3, 4, 5]"

StringOutputParser:
"The answer is [1, 2, 3, 4, 5]"

ListOutputParser (if available):
[1, 2, 3, 4, 5]

CommaSeparatedListOutputParser:
["item1", "item2", "item3"]
```

### **Chain Architecture Diagram**

```
Input Variables: {topic: "AI", question: "How works?"}
         ↓
PromptTemplate
    - Substitutes {topic} and {question}
    - Creates formatted prompt string
         ↓
Model (ChatGroq)
    - Receives: "You are expert in AI. How works?"
    - Generates: Raw natural language response
         ↓
OutputParser
    - Extracts: Structured data from response
    - Returns: Parsed result
         ↓
Final Output: {"answer": "...", "confidence": 0.9}
```

## 📁 Files Overview

### **simple_chain/**
```
Purpose: PromptTemplate → Model → Parser
Pattern: Basic linear flow
Use: Single task, one-step processing
```

### **sequential_chain/**
```
Purpose: Chain1 output → Chain2 input
Pattern: Multi-step workflow
Use: When output of one is needed for next
```

### **parallel_chain/**
```
Purpose: Multiple chains run together
Pattern: RunnableParallel
Use: Independent tasks, combine results
Example: Generate notes + quiz simultaneously
```

### **condtional_chain/** (Note: folder name typo - "condtional")
```
Purpose: Conditional execution based on input
Pattern: RunnableLambda for routing
Use: Different processing paths based on input type
Example: Math question → calculator, General → Q&A
```

## 🔑 Key Learning Points

### **1. Simple Chain**

```python
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StringOutputParser

# Step 1: Create template
template = "Explain {concept} in simple terms for a {audience}"
prompt = PromptTemplate(template=template, 
                        input_variables=["concept", "audience"])

# Step 2: Initialize model
model = ChatGroq(model="llama-3.1-8b-instant")

# Step 3: Create parser
parser = StringOutputParser()

# Step 4: Compose chain
chain = prompt | model | parser

# Step 5: Use chain
result = chain.invoke({
    "concept": "Machine Learning",
    "audience": "beginner"
})
print(result)
```

### **2. Sequential Chain**

```python
from langchain_core.prompts import PromptTemplate

# Chain 1: Extract key points
template1 = "Summarize this in 3 points:\n{text}"
chain1 = PromptTemplate(...) | model | parser

# Chain 2: Expand on summary
template2 = "Elaborate on these points:\n{summary}"
chain2 = PromptTemplate(...) | model | parser

# Combine sequentially
sequential = chain1 | chain2  # Chain1 output → Chain2 input

# Usage
result = sequential.invoke({"text": "Long document..."})
```

### **3. Parallel Chain**

```python
from langchain_core.runnables import RunnableParallel

# Create multiple chains
notes_chain = prompt1 | model | parser
quiz_chain = prompt2 | model | parser
summary_chain = prompt3 | model | parser

# Run in parallel
parallel = RunnableParallel(
    notes=notes_chain,
    quiz=quiz_chain,
    summary=summary_chain
)

# Execute all at once
result = parallel.invoke({"content": "Study material"})
# result = {
#     "notes": "...",
#     "quiz": "...",
#     "summary": "..."
# }
```

### **4. Conditional Chain**

```python
from langchain_core.runnables import RunnableLambda

def route_by_type(inputs):
    if "math" in inputs["query"].lower():
        return "math_chain"
    else:
        return "general_chain"

math_chain = prompt1 | model
general_chain = prompt2 | model

conditional = RunnableLambda(route_by_type).input | {
    "math_chain": math_chain,
    "general_chain": general_chain
}
```

## 💡 Practical Patterns

### **Pattern 1: Content Generator**

```python
template = """Generate a {type} about {topic}.
Include at least {points} key points.

Output:"""

prompt = PromptTemplate(
    template=template,
    input_variables=["type", "topic", "points"]
)

chain = prompt | model | StringOutputParser()

result = chain.invoke({
    "type": "blog post",
    "topic": "Python",
    "points": 5
})
```

### **Pattern 2: Data Processing Pipeline**

```python
# Step 1: Validate input
validate_chain = PromptTemplate(...) | model

# Step 2: Extract info
extract_chain = PromptTemplate(...) | model

# Step 3: Format output
format_chain = PromptTemplate(...) | model

# Sequential: Validate → Extract → Format
pipeline = validate_chain | extract_chain | format_chain

result = pipeline.invoke({"data": "raw input"})
```

### **Pattern 3: Multi-Task Processing**

```python
from langchain_core.runnables import RunnableParallel

tasks = RunnableParallel(
    sentiment=sentiment_chain,
    entities=entity_chain,
    summary=summary_chain,
    keywords=keyword_chain
)

result = tasks.invoke({"text": "Document text..."})
# Returns dict with all results
```

## 📊 Chain Composition Patterns

```
Linear:        A → B → C
Sequential:    A output → B input → C input
Parallel:      A
               B  (run together)
               C
Branching:     If X: path1 else: path2
```

## 🎓 Advanced Concepts

### **RunnableParallel Performance**

```
Sequential execution:
Chain A: 2 sec
Chain B: 2 sec
Total:   4 sec

Parallel execution:
Chain A: 2 sec |
Chain B: 2 sec | → 2 sec (happens together)
Total:   2 sec (50% improvement!)
```

### **Chain Debugging**

```python
# Enable verbose mode
chain = prompt | model | parser

# Run with debug
result = chain.invoke({...}, config={"run_name": "my_chain", "callbacks": [...]})

# Check what's happening at each step
```

### **Chain Composition Rule**

```
Type compatibility:

Runnable A outputs Dict
Runnable B expects Dict
Result: A | B ✅ Works

Runnable A outputs String
Runnable B expects Dict
Result: A | B ❌ Error!

Solution: Add intermediate transformation
```

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Type mismatch in chain | Ensure output of A matches input of B |
| Chain too slow | Parallelize independent steps |
| Unexpected output | Check PromptTemplate formatting |
| Memory issues | Don't store huge results in parallel |

## 💡 Pro Tips

1. **Naming**: Use clear names for chains (e.g., `extraction_chain`)
2. **Modularity**: Create reusable chain components
3. **Error Handling**: Wrap chains in try-except
4. **Caching**: Cache chain results for same inputs
5. **Testing**: Test each chain component separately

## 📚 Comparison: Simple vs Sequential vs Parallel

```
Simple:
├── Fast setup
├── Single task
└── Limited complex workflows

Sequential:
├── Multi-step
├── Each step depends on previous
└── Good for pipelines

Parallel:
├── Independent tasks
├── Faster execution
└── Results aggregation
```

## 🚀 Common Chain Patterns

### **Q&A Chain**
```python
qa_template = """Answer the question:
{question}

Answer:"""
```

### **Translation Chain**
```python
translate_template = """Translate to {language}:
{text}

Translation:"""
```

### **Classification Chain**
```python
classify_template = """Classify as one of: {categories}

Text: {text}
Classification:"""
```

## 📝 Next Steps

1. **Folder 7**: Runnables - More advanced composition patterns
2. **Folder 12**: RAG Pipeline - Chains in real applications
3. **Combine with Document Processing**: Chains for document workflows

## 📖 Related Concepts

- **Prompt Engineering**: Crafting good templates
- **Output Parsing**: Extracting structured data
- **Runnables**: Lower-level composition primitives
- **Tools**: External functions in chains

---

**Chain Composition Mastered! ⛓️**