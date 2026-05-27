# 🗺️ LangChain GenAI Learning Path - Quick Reference

## 📚 Complete Learning Roadmap

```
START HERE: Folder 1-4 (Foundation)
   ↓
INTERMEDIATE: Folder 5-7 (Composition)
   ↓
ADVANCED: Folder 8-11 (Data Processing)
   ↓
PRODUCTION: Folder 12-13 (Real Applications)
```

---

## 🚀 Quick Reference Guide

### **Folder 1: LLMs** 
**What**: Direct LLM API calls  
**Key Code**: `ChatGroq().invoke(message)`  
**Learn**: Basic model usage, parameters, prompting  
**Time**: 30 mins  

### **Folder 2: Chat Models**
**What**: Multi-turn conversations  
**Key Code**: `SystemMessage + HumanMessage`  
**Learn**: Structured conversations, message types  
**Time**: 30 mins  

### **Folder 3: Local Models**
**What**: Run open-source models locally  
**Key Code**: `HuggingFacePipeline.from_model_id()`  
**Learn**: Model loading, CPU/GPU, cost-free inference  
**Time**: 45 mins  

### **Folder 4: Embeddings**
**What**: Convert text to vectors  
**Key Code**: `HuggingFaceEmbeddings().embed_query()`  
**Learn**: Semantic similarity, vector math, dimensions  
**Time**: 45 mins  

### **Folder 5: Structured Outputs**
**What**: Type-safe, validated LLM outputs  
**Key Code**: `model.with_structured_output(Pydantic)`  
**Learn**: Pydantic models, validation, JSON schema  
**Time**: 1 hour  

### **Folder 6: Chains**
**What**: Compose prompt → model → parser  
**Key Code**: `prompt | model | parser`  
**Learn**: Workflow composition, pipe operator  
**Time**: 1 hour  

### **Folder 7: Runnables**
**What**: Composable execution primitives  
**Key Code**: `RunnableSequence, RunnableParallel`  
**Learn**: Parallel execution, branching, lambdas  
**Time**: 1 hour  

### **Folder 8: Document Loaders**
**What**: Load docs from multiple sources  
**Key Code**: `TextLoader, PyPdfLoader, DirectoryLoader`  
**Learn**: Source handling, metadata, batching  
**Time**: 45 mins  

### **Folder 9: Text Splitters**
**What**: Intelligent document chunking  
**Key Code**: `RecursiveCharacterTextSplitter`  
**Learn**: Chunk strategy, overlap, context windows  
**Time**: 1 hour  

### **Folder 10: Vector Stores**
**What**: Store embeddings for search  
**Key Code**: `Chroma.from_documents()`  
**Learn**: Indexing, similarity search, metadata filtering  
**Time**: 1.5 hours  

### **Folder 11: Retrievers**
**What**: Advanced search strategies  
**Key Code**: `MMR, CCR, MultiQueryRetriever`  
**Learn**: Ranking, diversity, compression  
**Time**: 1.5 hours  

### **Folder 12: RAG Pipeline**
**What**: End-to-end Q&A system  
**Key Code**: `YouTube → Index → Retrieve → Answer`  
**Learn**: Complete production pattern  
**Time**: 2 hours  

### **Folder 13: Tools & Agents**
**What**: Give LLM external capabilities  
**Key Code**: `initialize_agent(tools, llm)`  
**Learn**: Tool creation, agent loops, decision making  
**Time**: 1.5 hours  

---

## 🎯 Learning Paths Based on Goals

### **Path 1: Web Developer (LangChain Integration)**
Folders: 1 → 2 → 6 → 5 → 12
Time: 5 hours
Goal: Add AI features to web apps

### **Path 2: Data Scientist (Semantic Search)**
Folders: 4 → 8 → 9 → 10 → 11
Time: 5 hours
Goal: Build search systems over data

### **Path 3: AI Engineer (Full Stack)**
Folders: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13
Time: 12 hours
Goal: Master complete GenAI development

### **Path 4: Local-First Developer**
Folders: 3 → 4 → 8 → 9 → 10 → 11 → 12
Time: 7 hours
Goal: Build without APIs, fully local

---

## 💡 Key Concepts Map

```
Text Input
    ↓
LLM/Chat Model
    ↓
Structured Output
    ↓
Chains / Runnables
    ↓
Document Processing (Load → Split → Embed)
    ↓
Vector Store + Retriever
    ↓
RAG System
    ↓
Tools / Agents
    ↓
Production Application
```

---

## 🔗 Dependencies Chain

```
Folder 1,2,3: Standalone (Just API calls)
    ↓
Folder 4: Needs embeddings library
    ↓
Folder 5: Needs Pydantic
    ↓
Folder 6,7: Needs Folder 1,2,5
    ↓
Folder 8,9: Needs document libs
    ↓
Folder 10: Needs Folder 4,9 (embeddings + splitting)
    ↓
Folder 11: Needs Folder 10 (retriever wraps store)
    ↓
Folder 12: Needs Folder 8,9,10,11 (RAG pipeline)
    ↓
Folder 13: Needs Folder 12 (tools in agents)
```

---

## 🎓 Recommended Study Schedule

### **Week 1: Foundations**
- Day 1: Folder 1 (LLMs)
- Day 2: Folder 2 (Chat) + Folder 3 (Local)
- Day 3: Folder 4 (Embeddings)
- Day 4: Folder 5 (Structured)
- Day 5: Folder 6 (Chains)

### **Week 2: Data Processing**
- Day 1: Folder 7 (Runnables)
- Day 2: Folder 8 (Document Loaders)
- Day 3: Folder 9 (Text Splitters)
- Day 4: Folder 10 (Vector Stores)
- Day 5: Folder 11 (Retrievers)

### **Week 3: Production**
- Day 1: Folder 12 (RAG Pipeline)
- Day 2-3: Project - Combine everything
- Day 4: Folder 13 (Tools)
- Day 5: Projects - Advanced agents

---

## 🛠️ Quick Command Reference

```bash
# Setup
pip install -r requirements.txt
cp .env.example .env  # Add your API keys

# Run any example
python 1)LLMS/llm.py
python 2)Chat_Models/chat_model.py
# ... and so on

# Test specific folder
python -m pytest 6)Chains/
```

---

## 📊 Complexity vs Time Tradeoff

```
Easy & Fast          Hard & Slow
├─ Folder 1         ├─ Folder 11
├─ Folder 2         ├─ Folder 12
├─ Folder 3         └─ Folder 13
├─ Folder 4
├─ Folder 5
├─ Folder 6
├─ Folder 7
├─ Folder 8
├─ Folder 9
└─ Folder 10

Recommendation:
→ Learn in order (1-13)
→ Complexity increases naturally
→ Prerequisites are clear
```

---

## ✅ Success Checklist

After completing this course, you should be able to:

**Beginner (Folders 1-4):**
- ☐ Call LLM APIs
- ☐ Have multi-turn conversations
- ☐ Run models locally
- ☐ Generate embeddings

**Intermediate (Folders 5-7):**
- ☐ Get structured outputs
- ☐ Build chains
- ☐ Create parallel workflows
- ☐ Compose runnables

**Advanced (Folders 8-11):**
- ☐ Load documents
- ☐ Split intelligently
- ☐ Build vector stores
- ☐ Implement advanced retrieval

**Expert (Folders 12-13):**
- ☐ Build RAG systems
- ☐ Create AI agents
- ☐ Design tool systems
- ☐ Handle complex workflows

---

## 🔗 Cheat Sheet - Common Imports

```python
# Basics
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline

# Processing
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPdfLoader

# Storage & Retrieval
from langchain_community.vectorstores import Chroma, FAISS
from langchain.retrievers import ContextualCompressionRetriever

# Chains & Composition
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StringOutputParser
from langchain.chains import RetrievalQA

# Agents
from langchain.agents import initialize_agent, Tool
from langchain_community.tools import DuckDuckGoSearchRun
```

---

## 🚀 Next After This Course

1. **Specialization**: Choose domain (RAG, Agents, Automation)
2. **Production Deployment**: Docker, Kubernetes, Cloud
3. **Optimization**: Performance tuning, cost reduction
4. **Advanced Topics**: Fine-tuning, multi-agent systems
5. **Contributed**: Extend LangChain with custom components

---

## 📖 Resources

- [LangChain Docs](https://python.langchain.com/)
- [Groq API](https://groq.com/)
- [HuggingFace](https://huggingface.co/)
- [GitHub Discussions](https://github.com/langchain-ai/langchain)

---

**Happy Learning! Start with Folder 1 and progress sequentially. 🚀**