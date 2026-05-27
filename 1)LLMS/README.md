# 📖 Folder 1: LLMS (Language Learning Models)

## 🎯 Objective

Use LLM APIs directly to implement simple question-answering. Leverage Groq's high-speed LLM models through the ChatGroq API.

## 📚 Theory & Concepts

### **What is an LLM?**

- **Definition**: A generative AI model that produces text output from text input
- **Training**: Billions of parameters trained using transformer architecture
- **Capability**: Natural language understanding and generation
- **Strength**: Few-shot learning, reasoning, coding, translation

### **API-Based LLM vs Local Models**

| Aspect | API-Based (ChatGroq) | Local Models |
|--------|---------------------|-------------|
| Speed | Very Fast | Slow (GPU/CPU dependent) |
| Cost | Per-token billing | One-time setup |
| Privacy | Data in cloud | Local data |
| Accuracy | High (Llama 3.1) | Variable |
| Deployment | Instant | Complex |

### **ChatGroq - High-Speed Inference**

```
Request → Groq API → LPU (Language Processing Unit) → Response
         (Fast inference engine)
```

**Key Features:**
- **LPU Technology**: Dedicated AI acceleration hardware
- **Models Available**: Llama 3.1 (various sizes), Mixtral
- **Response Time**: Sub-second latency
- **Cost Efficient**: Affordable per-token pricing

### **Key Parameters**

1. **Model**
   - `llama-3.1-8b-instant` - 8 billion parameters, instant response
   - `llama-3.1-70b` - Larger model, better quality
   
2. **Temperature** (0.0 - 2.0)
   - `0.0` - Deterministic, consistent responses
   - `0.7` - Balanced creativity aur consistency
   - `1.5+` - Very creative, random

3. **max_tokens**
   - Response length limit
   - Prevents unexpected long outputs

### **LLM Response Pipeline**

```
Input Text
    ↓
Tokenization (words → tokens)
    ↓
Neural Network Processing
    ↓
Token Generation (iterative)
    ↓
Detokenization (tokens → words)
    ↓
Output Text
```

### **Prompt Engineering Basics**

```
Prompt = Context + Instructions + Examples + Query

Example:
"You are a helpful coding assistant.
Generate Python code for the following:
Task: Read a CSV file and print first 5 rows."
```

## 📁 Files Overview

### **llm.py**

```python
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

# Step 1: Initialize LLM
llm = ChatGroq(
    api_key="xxx",           # Groq API key (loaded from .env)
    model="llama-3.1-8b-instant",
    temperature=0.7          # Balances creativity vs consistency
)

# Step 2: Create message
message = HumanMessage(content="Your question here")

# Step 3: Get response
response = llm.invoke(message)  # Direct API call
print(response.content)
```

## 🔑 Key Learning Points

### **1. Environment Setup**
- Store `GROQ_API_KEY` in `.env` file
- Use `python-dotenv` library to load keys
- Never hardcode credentials in code!

### **2. ChatGroq Initialization**
```python
llm = ChatGroq(
    model="llama-3.1-8b-instant",  # Model selection
    temperature=0.7,                # Control randomness
    max_tokens=500                  # Output length limit
)
```

### **3. Invoke Method**
- **Purpose**: Send prompt to the LLM
- **Input**: Message object (HumanMessage, SystemMessage, etc.)
- **Output**: AIMessage with response
- **Blocking**: Synchronous call (waits for response)

### **4. Response Object Structure**
```python
response = llm.invoke(message)
# response.content - Actual text
# response.usage_metadata - Token usage statistics
# response.response_metadata - Model information
```

## 💡 Practical Tips

### **Cost Optimization**
1. **Smaller Models**: Start with `8b-instant`, upgrade to `70b` later
2. **Token Counting**: Understand prompt tokens for billing calculations
3. **Batch Processing**: Efficiently handle multiple queries together

### **Quality Improvement**
1. **Better Prompts**: Write clear, specific instructions
2. **Context**: Provide relevant background information
3. **Temperature**: Use 0.0-0.3 for deterministic results

### **Error Handling**
```python
try:
    response = llm.invoke(message)
except Exception as e:
    print(f"API Error: {e}")
```

## 🔄 LLM vs Other Models

```
LLM (General Purpose)
├── ChatGroq (API)
├── GPT-4 (OpenAI)
└── Gemini (Google)

Specialized Models
├── Embedding Models (text → vectors)
├── Vision Models (images)
└── Speech Models (audio)
```

## 📊 Use Cases

### **1. Q&A Systems**
```
User: "How to reverse a list in Python?"
LLM: "Use list[::-1] or reversed()"
```

### **2. Content Generation**
- Blog posts
- Code generation
- Translation

### **3. Summarization**
- Convert long documents into short summaries

### **4. Classification**
- Sentiment analysis
- Category detection

## 🎓 Next Steps

1. **Folder 2**: Chat Models - Multiple turns ke saath conversations
2. **Folder 3**: Local Models - Remove API dependency
3. **Folder 5**: Structured Outputs - Type-safe responses

## 🚀 Common Patterns

### **Simple Query-Response**
```python
result = llm.invoke(HumanMessage(content="question"))
print(result.content)
```

### **With Context (System Prompt)**
```python
messages = [
    SystemMessage(content="You are helpful assistant"),
    HumanMessage(content="Question here")
]
result = llm.invoke(messages)
```

### **Stream Response** (Real-time output)
```python
for chunk in llm.stream(message):
    print(chunk.content, end="", flush=True)
```

## 📝 Notes

- ChatGroq `invoke()` synchronous hai
- Async version: `ainvoke()` method
- Check rate limits in production
- Temperature tuning is crucial for task-specific results

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| API Key Error | Check .env, is GROQ_API_KEY set? |
| Rate Limit | Implement queue system |
| Timeout | Reduce max_tokens |
| Bad Responses | Adjust temperature |

---

**Happy Prompting! 🚀**