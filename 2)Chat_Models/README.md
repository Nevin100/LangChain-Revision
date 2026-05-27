# 📖 Folder 2: Chat Models

## 🎯 Objective

Implement multi-turn conversations in structured format using `SystemMessage` and `HumanMessage`. Understand the differences between LLM and ChatModel.

## 📚 Theory & Concepts

### **LLM vs Chat Model**

| Aspect | LLM | Chat Model |
|--------|-----|-----------|
| Input | Single text | Message objects (structured) |
| Use Case | General text generation | Conversations |
| History | Manual management | Built-in support |
| Formatting | Raw text | Structured format |
| Example | `text-davinci-003` | `gpt-4-turbo` |

### **Chat Architecture - Message Types**

```
Conversation Structure:
┌──────────────────────────────────────┐
│ SystemMessage: Role/Personality      │ (Optional, sets context)
├──────────────────────────────────────┤
│ HumanMessage: User question          │ (User input)
├──────────────────────────────────────┤
│ AIMessage: Model response            │ (Generated output)
├──────────────────────────────────────┤
│ [Repeat: HumanMessage → AIMessage]   │ (Multi-turn)
└──────────────────────────────────────┘
```

### **Core Components**

1. **SystemMessage**: Set the AI's personality and role
   - `"You are a helpful coding expert"`
   - Defines model behavior
   - Optional but recommended

2. **HumanMessage**: User's input and questions
   - Actual user queries
   - Can appear multiple times

3. **AIMessage**: Model's response
   - Automatically generated
   - Used for conversation history

### **ChatGroq vs HuggingFace Endpoints**

```
ChatGroq (API-Based)
├── Fast (LPU hardware)
├── High-quality models
├── Per-token billing
└── Internet required

HuggingFaceEndpoint (API-Based)
├── Various model options
├── Custom fine-tuned models
├── Variable performance
└── Hugging Face servers
```

### **Conversation Flow**

```
System: "You are Python expert"
User:   "How to read file?"
AI:     "Use open() function..."

User:   "What about error handling?"
AI:     "Use try-except block..."  ← Context aware!
```

## 📁 Files Overview

### **chat_model.py**

```
Purpose: ChatGroq with message history
Features: SystemMessage + HumanMessage + Invoke
```

### **huggingface_chat_model.py**

```
Purpose: HuggingFace endpoint integration
Features: Alternative to ChatGroq
```

## 🔑 Key Learning Points

### **1. Message Construction**

```python
from langchain_core.messages import SystemMessage, HumanMessage

system_msg = SystemMessage(content="You are helpful assistant")
human_msg = HumanMessage(content="What is Python?")

# Pass as list
messages = [system_msg, human_msg]
response = model.invoke(messages)
```

### **2. ChatGroq Initialization**

```python
from langchain_groq import ChatGroq

chat_model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)
```

### **3. Multi-Turn Conversation**

```python
messages = [
    SystemMessage(content="You are data scientist"),
    HumanMessage(content="What is ML?"),
    # ... AI response here ...
    HumanMessage(content="Explain algorithms"),  # Follow-up
    # Response will reference previous context
]
```

### **4. HuggingFace Endpoint**

```python
from langchain_huggingface import HuggingFaceEndpoint

hf_endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-2-7b-chat",
    api_key="your_hf_key"
)

response = hf_endpoint.invoke(messages)
```

## 💡 Practical Patterns

### **Pattern 1: Expert Role-Playing**

```python
messages = [
    SystemMessage("You are expert in quantum physics"),
    HumanMessage("Explain superposition")
]
```

### **Pattern 2: Step-by-Step Instructions**

```python
system = """You are a helpful tutor.
1. First explain the concept simply
2. Provide an example
3. Ask a follow-up question"""

messages = [
    SystemMessage(system),
    HumanMessage("What is recursion?")
]
```

### **Pattern 3: Multi-Turn Conversation History**

```python
def chat_with_memory(conversation_history, user_input):
    conversation_history.append(HumanMessage(content=user_input))
    response = model.invoke(conversation_history)
    conversation_history.append(response)
    return response.content, conversation_history

# Usage
history = [SystemMessage("You are helpful assistant")]
response1, history = chat_with_memory(history, "Hi there")
response2, history = chat_with_memory(history, "What's my first message?")
```

## 🔄 Message Flow Diagram

```
┌─────────────────┐
│  System Prompt  │ (Personality)
└────────┬────────┘
         │
┌────────▼────────┐
│ Human Input 1   │ (User question)
└────────┬────────┘
         │
┌────────▼────────┐
│ AI Response 1   │ (Generated answer)
└────────┬────────┘
         │
┌────────▼────────┐
│ Human Input 2   │ (Follow-up)
└────────┬────────┘
         │
┌────────▼────────┐
│ AI Response 2   │ (Context-aware)
└─────────────────┘
```

## 📊 Use Cases

### **1. Customer Support Bot**
```
System: "You are support representative"
User: "Order status?"
AI: "Please provide order ID"
```

### **2. Tutoring System**
```
System: "You are patient teacher"
User: "Explain recursion"
AI: "[Detailed explanation]"
User: "More examples?"
AI: "[Additional examples with context]"
```

### **3. Code Review Assistant**
```
System: "You are senior developer doing code review"
User: "[Code snippet]"
AI: "[Review with suggestions]"
```

## 🎓 Advanced Concepts

### **Context Window**
- Model kitna message history remember kar sakta hai
- Llama 3.1 8b: 8,192 tokens (~6000 words)
- Llama 3.1 70b: 8,192 tokens

### **Token Management**
```python
# Total tokens = Input tokens + Output tokens

# Estimate: 1 token ≈ 4 characters
# Conversation: 5 messages × 1000 chars = 1250 tokens (approx)
```

### **Temperature in Chat**
- **Support Bot**: 0.0-0.3 (consistent, factual)
- **Creative Writing**: 0.7-1.0 (varied responses)
- **Brainstorming**: 1.0-1.5 (highly creative)

## 📝 Comparison: ChatGroq vs HuggingFaceEndpoint

### **ChatGroq Advantages**
- ✅ Faster inference (LPU)
- ✅ Better quality models
- ✅ Easy setup
- ❌ Per-token costs

### **HuggingFaceEndpoint Advantages**
- ✅ More model options
- ✅ Can use custom fine-tuned models
- ❌ Slower inference
- ❌ Variable quality

## 🚀 Next Steps

1. **Chains (Folder 6)**: Messages ke saath output parsing add karo
2. **Runnables (Folder 7)**: Integrate into complex workflows
3. **Document Context**: Provide relevant docs for RAG

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Memory issues | Prune conversation history |
| Slow responses | Use ChatGroq, avoid HF endpoint |
| Inconsistent responses | Reduce temperature |
| Token limit exceeded | Summarize messages |

## 💡 Pro Tips

1. **Naming**: Use clear names for chains (e.g., `extraction_chain`)
2. **Modularity**: Create reusable chain components
3. **Error Handling**: Wrap chains in try-except
4. **Caching**: Cache chain results for identical inputs
5. **Testing**: Test each chain component separately

## 📚 Related Topics

- **Folder 1**: Single-turn LLM calls (foundation)
- **Folder 5**: Structured outputs from chat responses
- **Folder 6**: Chains with chat models
- **Folder 12**: Chat in RAG pipelines

---

**Happy Chatting! 💬**