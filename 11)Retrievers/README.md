# 📖 Folder 11: Retrievers

## 🎯 Objective

Implement intelligent document retrieval strategies from vector stores. Improve result quality using advanced search techniques.

## 📚 Theory & Concepts

### **Retriever vs Vector Store**

```
Vector Store:
└── Raw similarity search

Retriever:
├── Wraps vector store
├── Adds intelligence
├── Advanced search strategies
└── Integration point for RAG
```

### **Why Advanced Retrievers?**

```
Problem with Basic Similarity:
- Query: "machine"
- Returns docs about: washing machines (irrelevant!)
- Reason: Semantic overlap but different context

Advanced Retrievers:
├── CCR: Compress results to relevant snippets
├── MMR: Balance relevance + diversity
├── Multi-Query: Generate multiple queries
├── Self-query: Translate queries to filters
```

### **Four Retriever Types in This Folder**

```
1. VectorSearchRetriever
   └── Basic similarity (foundation)

2. CCR (Contextual Compression Retriever)
   └── Filter results to relevant parts
   └── Reduce noise

3. MMR (Maximal Marginal Relevance)
   └── Balance relevance + diversity
   └── Avoid repetitive results

4. MultiQueryRetriever
   └── Generate multiple interpretations
   └── Broader coverage
```

### **Retriever Architecture**

```
Query
    ↓
as_retriever() wrapper
    ↓
Apply Retrieval Strategy
    ├── Similarity Search
    ├── Compression
    ├── Diversity Filter
    └── Query Expansion
    ↓
Ranked Results
```

## 📁 Files Overview

### **VectorSearchRetriever/**
```
Purpose: Basic similarity search
Method: vector_store.as_retriever()
Output: Top-K documents by similarity
```

### **CCR/** (Contextual Compression Retriever)
```
Purpose: Filter results to relevant snippets
Methods: 
├── LLMChainExtractor - Use LLM to extract relevant parts
├── LLMChainFilter - Use LLM to filter documents
└── EmbeddingsFilter - Filter by embedding similarity
Output: Compressed, focused results
```

### **MMR/** (Maximal Marginal Relevance)
```
Purpose: Balance relevance with diversity
Method: search_type="mmr"
Parameter: lambda_mult (0-1, relevance vs diversity)
Output: Diverse relevant results
```

### **MultiQueryRetriever/**
```
Purpose: Generate multiple queries
Method: Automatic query expansion
Output: Union of results from multiple queries
Better: Broader document coverage
```

## 🔑 Key Learning Points

### **1. Basic Vector Search Retriever**

```python
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings()
vector_store = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

# Convert to retriever
retriever = vector_store.as_retriever(
    search_type="similarity",  # or "mmr"
    search_kwargs={"k": 5}     # Return top 5 results
)

# Usage
results = retriever.invoke("What is Python?")
for doc in results:
    print(f"Score: {doc.metadata.get('score', 'N/A')}")
    print(f"Content: {doc.page_content[:100]}\n")
```

### **2. Compression Retriever (LLMChainExtractor)**

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_groq import ChatGroq

base_retriever = vector_store.as_retriever(search_kwargs={"k": 10})

# LLM will extract only relevant parts
compressor = LLMChainExtractor.from_llm(
    llm=ChatGroq(model="llama-3.1-8b-instant"),
    prompt_template=None  # Uses default prompt
)

# Combine retriever + compressor
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

# Usage: Returns compressed results
results = compression_retriever.invoke("How does Python work?")
# Much shorter, more focused content
```

### **3. MMR (Maximal Marginal Relevance) Retriever**

```python
# MMR balances relevance + diversity
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "lambda_mult": 0.5  # 0.0 = diversity only, 1.0 = relevance only
    }
)

results = retriever.invoke("machine learning")

# Results will include:
# - Top result: Most relevant
# - Other results: Relevant but different topics
# - Avoids: Similar results to top result
```

### **4. Multi-Query Retriever**

```python
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant")

# Automatic query expansion
multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
    llm=llm,
    prompt=None  # Uses default prompt to generate variations
)

# Usage
results = multi_query_retriever.invoke("What is ML?")

# Internally:
# Generates: "What is machine learning?"
#            "Define machine learning"
#            "How does ML work?"
# Returns union of results from all queries
```

### **5. Compression with Embedding Filter**

```python
from langchain.retrievers.document_compressors import EmbeddingsFilter
from langchain.retrievers import ContextualCompressionRetriever

base_retriever = vector_store.as_retriever(search_kwargs={"k": 20})

# Filter by embedding similarity threshold
embeddings_filter = EmbeddingsFilter(
    embeddings=embeddings,
    similarity_threshold=0.76  # Only keep > 76% similar
)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=embeddings_filter,
    base_retriever=base_retriever
)

results = compression_retriever.invoke("query")
```

## 💡 Practical Patterns

### **Pattern 1: Production Retriever (Best)**

```python
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

llm = ChatGroq(model="llama-3.1-8b-instant")
base_retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 10, "lambda_mult": 0.5}
)

# Multi-query for broader coverage
multi_retriever = MultiQueryRetriever.from_llm(
    retriever=base_retriever,
    llm=llm
)

# Compression for quality
compressor = LLMChainExtractor.from_llm(llm=llm)
final_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=multi_retriever
)

# Usage
results = final_retriever.invoke("complex query")
```

### **Pattern 2: Speed-Optimized Retriever**

```python
# Simple, fast: Just similarity
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}  # Only top 3
)

# For real-time applications
results = retriever.invoke(query)
```

### **Pattern 3: Quality-Optimized Retriever**

```python
# Complex, slower: Multiple strategies
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 20, "lambda_mult": 0.25}  # More diversity
)

# Add compression
compressor = LLMChainExtractor.from_llm(llm=llm)
retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=retriever
)

# For high-quality results
results = retriever.invoke(query)
```

### **Pattern 4: Hybrid Retrieval (Metadata + Semantic)**

```python
# Combine metadata filtering with semantic search
def get_relevant_docs(query, category):
    # Base semantic search
    base_results = vector_store.similarity_search(query, k=10)
    
    # Filter by category metadata
    filtered = [
        doc for doc in base_results
        if doc.metadata.get("category") == category
    ]
    
    return filtered

results = get_relevant_docs("machine learning", "tutorial")
```

## 📊 Retriever Comparison

| Retriever | Speed | Quality | Best For |
|-----------|-------|---------|----------|
| Basic | ⚡⚡⚡ | ⭐⭐ | Fast responses |
| CCR | ⚡ | ⭐⭐⭐⭐ | Focused results |
| MMR | ⚡⚡ | ⭐⭐⭐ | Diverse results |
| Multi-Query | ⚡ | ⭐⭐⭐⭐ | Comprehensive |

## 🎓 Advanced Concepts

### **Lambda Mult in MMR**

```
lambda_mult = 0.0 (Pure Diversity)
└── All results different from each other
└── May miss best result

lambda_mult = 0.5 (Balanced)
└── Balanced relevance + diversity
└── Recommended for most use cases

lambda_mult = 1.0 (Pure Relevance)
└── Just like basic similarity search
└── May return very similar results
```

### **LLM Compression Cost-Benefit**

```
Cost: Calls LLM for every search
├── Slower (LLM latency added)
└── Higher token usage

Benefit:
├── More focused results
├── Reduced hallucination
└── Better for RAG systems
```

### **Multi-Query Strategy**

```
Input Query: "What is machine learning?"

Generated variations:
1. "Define machine learning"
2. "How does ML differ from AI?"
3. "Applications of machine learning"
4. "ML algorithms and models"

Final Result: Union of all results (deduplicated)
```

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Slow retrieval | Remove compression, use basic similarity |
| No relevant docs | Use multi-query retriever |
| Too many duplicates | Use MMR with lambda_mult < 1.0 |
| LLM rate limit | Batch retrievals, cache results |

## 💡 Pro Tips

1. **Start Simple**: Use basic retriever first, add complexity as needed
2. **MMR is Key**: Almost always better than pure similarity
3. **Compression Trade-off**: Worth the cost for RAG systems
4. **Query Generation**: Let LLM expand queries - it understands context
5. **Monitoring**: Track retrieval quality metrics

## 📚 Best Practices

### **RAG Pipeline Retriever**
```python
# Multiple strategies stacked
retriever = (
    vector_store
    .as_retriever(search_type="mmr", search_kwargs={"k": 20, "lambda_mult": 0.5})
    # ↓ Wrapped by Multi-Query
    # ↓ Wrapped by Compression
)
```

### **Metadata Filtering**
```python
# Before vector search
retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 5,
        "filter": {"category": "tutorial", "difficulty": "beginner"}
    }
)
```

## 🚀 Next Steps

1. **Folder 12**: Use retrievers in complete RAG pipeline
2. **Optimization**: Monitor and tune retrieval parameters
3. **Scaling**: Move to production retrieval systems

## 📖 Related Topics

- **Folder 10**: Vector Stores (foundation)
- **Folder 4**: Embeddings (similarity basis)
- **Folder 12**: RAG Pipeline (applies retrievers)
- **Multi-Query Retriever**: Query expansion

---

**Advanced Retrieval Mastered! 🔍**