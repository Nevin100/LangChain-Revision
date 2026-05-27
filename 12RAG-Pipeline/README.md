# 📖 Folder 12: RAG Pipeline

## 🎯 Objective

Build end-to-end Retrieval-Augmented Generation pipeline. Create a Q&A system from YouTube transcripts that uses LLM + retrieved context.

## 📚 Theory & Concepts

### **RAG (Retrieval-Augmented Generation) - What is it?**

```
Traditional LLM:
Input Query
    ↓
LLM (trained knowledge only)
    ↓
Output (may hallucinate if no training data)

RAG System:
Input Query
    ↓
Retrieve Relevant Context (Vector Store)
    ↓
LLM (with context + query)
    ↓
Output (grounded, factual)
```

### **Why RAG?**

```
Problem: LLM hallucination
├── Makes up facts
├── Outdated information
└── No source attribution

RAG Solution:
├── ✅ Grounds response in real documents
├── ✅ Can cite sources
├── ✅ Handles fresh data
├── ✅ Reduced hallucination
```

### **Complete RAG Pipeline Flow**

```
         ┌─ Indexing Phase (One-time) ─┐
         │                              │
    Load Documents                Vector Store
         │                              │
    Split Documents                   Created
         │
    Generate Embeddings
         │
    └──────────────────────────────────┘


         ┌─ Query Phase (Runtime) ─────┐
         │                              │
    User Query                          │
         │                              │
    Search Vector Store ────→ Retrieve Docs
         │                              │
    Prompt + Context                    │
         │                              │
    LLM Generation                      │
         │                              │
    Final Answer ──────────────────────┘
```

### **YouTube Transcript RAG**

```
YouTube Video URL
    ↓
Extract Transcript (YouTubeTranscriptApi)
    ↓
Split into Chunks (RecursiveCharacterTextSplitter)
    ↓
Create Embeddings
    ↓
Store in FAISS (Fast Similarity Search)
    ↓
Q&A: User Question → Retrieve → Generate Answer
```

## 📁 File Overview

### **code.py**
```
Purpose: Complete RAG pipeline implementation
Components:
├── YouTube transcript fetching
├── Document chunking
├── FAISS vector store
├── Similarity retrieval
├── Prompt construction
└── LLM-based answering
```

## 🔑 Key Learning Points

### **1. Complete RAG Architecture**

```python
from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Step 1: Load YouTube Transcript
youtube_loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
)
transcript = youtube_loader.load()

# Step 2: Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(transcript)

# Step 3: Create embeddings
embeddings = HuggingFaceEmbeddings()

# Step 4: Store in FAISS
vector_store = FAISS.from_documents(chunks, embeddings)

# Step 5: Create retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# Step 6: Define prompt
template = """Use the following context to answer the question.
Context: {context}

Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, 
                        input_variables=["context", "question"])

# Step 7: LLM
llm = ChatGroq(model="llama-3.1-8b-instant")

# Step 8: Q&A function
def rag_chain(question):
    # Retrieve
    docs = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    # Generate
    response = llm.invoke(
        prompt.format(context=context, question=question)
    )
    
    return response.content
```

### **2. Retrieve + Augment + Generate**

```python
# Complete RAG cycle
question = "What is the main topic of the video?"

# Retrieve: Get relevant chunks
relevant_docs = retriever.invoke(question)
print(f"Retrieved {len(relevant_docs)} documents")

# Augment: Build context
context = "\n\n".join([
    f"[{i+1}] {doc.page_content}" 
    for i, doc in enumerate(relevant_docs)
])

# Augment: Build prompt with context
prompt_text = f"""Using this context from the video:

{context}

Answer this question: {question}"""

# Generate: Get answer from LLM
answer = llm.invoke(prompt_text)

print(f"Answer: {answer.content}")
```

### **3. FAISS vs Chroma for RAG**

```
Chroma:
├── Lightweight
├── Good for learning
└── ~100K documents

FAISS:
├── Industrial strength
├── Fast similarity search
├── Million+ documents
└── Used in Folder 12
```

### **4. Chain-Based RAG (Clean Code)**

```python
from langchain.chains import RetrievalQA

# Simple chain-based approach
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",           # Stuff: Put all docs in prompt
    retriever=retriever,
    return_source_documents=True  # Include sources
)

# Usage
result = qa_chain.invoke({"query": "What is the main topic?"})
print(f"Answer: {result['result']}")
print(f"Sources: {result['source_documents']}")
```

## 💡 Practical Patterns

### **Pattern 1: Simple RAG Q&A**

```python
def create_rag_qa(video_url):
    # Load
    loader = YoutubeLoader.from_youtube_url(video_url)
    docs = loader.load()
    
    # Split
    splitter = RecursiveCharacterTextSplitter(1000, 200)
    chunks = splitter.split_documents(docs)
    
    # Embed + Store
    embeddings = HuggingFaceEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    
    # Chain
    qa = RetrievalQA.from_chain_type(
        llm=ChatGroq(model="llama-3.1-8b-instant"),
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )
    
    return qa

# Usage
qa_system = create_rag_qa("https://youtube.com/watch?v=...")
answer = qa_system.invoke({"query": "What is about?"})
```

### **Pattern 2: RAG with Source Attribution**

```python
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    verbose=True  # See what's happening
)

result = qa_chain.invoke({"query": question})

# Print with sources
print(f"Question: {question}")
print(f"\nAnswer: {result['result']}")
print(f"\nSources:")
for doc in result['source_documents']:
    print(f"- {doc.metadata.get('source', 'Unknown')}")
```

### **Pattern 3: Advanced RAG with Compression**

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

# Base retriever
base_retriever = vector_store.as_retriever(search_kwargs={"k": 10})

# Add compression
compressor = LLMChainExtractor.from_llm(llm=llm)
retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)

# Use in RAG
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)
```

### **Pattern 4: Multi-Document RAG**

```python
# Load multiple YouTube videos
videos = [
    "https://youtube.com/watch?v=1",
    "https://youtube.com/watch?v=2",
    "https://youtube.com/watch?v=3",
]

all_docs = []
for url in videos:
    loader = YoutubeLoader.from_youtube_url(url)
    docs = loader.load()
    all_docs.extend(docs)

# Single RAG system for all
splitter = RecursiveCharacterTextSplitter(1000, 200)
chunks = splitter.split_documents(all_docs)

vector_store = FAISS.from_documents(chunks, HuggingFaceEmbeddings())
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", 
                                retriever=vector_store.as_retriever())
```

## 📊 Chain Types in RAG

```
"stuff":
├── Put all documents in prompt
├── Works for: Few documents, short documents
└── Fast

"map_reduce":
├── Summarize each document separately
├── Combine summaries
├── Works for: Many documents
└── Slower

"refine":
├── Start with first doc
├── Iteratively refine with more docs
├── Works for: Complex questions
└── Slowest
```

## 🎓 RAG Performance Optimization

### **Retrieval Quality Metrics**

```
1. Relevance: Retrieved docs answer question?
2. Precision: % of retrieved docs are relevant?
3. Recall: % of all relevant docs are retrieved?

Goal: High relevance, high precision, good recall
```

### **Performance Tuning**

```python
# Tune retrieval parameters
retriever = vector_store.as_retriever(
    search_type="mmr",           # Better diversity
    search_kwargs={
        "k": 5,                  # Top 5 docs
        "lambda_mult": 0.5       # Balance relevance-diversity
    }
)

# Tune chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,    # Larger = more context
    chunk_overlap=200   # More = better connections
)

# Tune prompt
template = """[System: You are expert]\n{context}\n\nQ: {question}\nA:"""
```

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| No relevant docs | Increase k, use multi-query retriever |
| Slow retrieval | Use basic similarity, reduce k |
| Poor quality answers | Improve prompt, use better retriever |
| Hallucination | Add source citation requirement |

## 💡 Pro Tips

1. **Retrieval Quality**: More important than LLM quality
2. **Chunk Size**: Experiment with 500-1500 characters
3. **Overlap**: Use 20-30% overlap
4. **k Value**: Start with 3-5, increase if needed
5. **Monitoring**: Track answer quality, source relevance

## 📚 Full RAG Pipeline Checklist

```
Indexing:
☐ Load documents
☐ Split into chunks (1000 chars, 200 overlap)
☐ Create embeddings (all-MiniLM-L6-v2)
☐ Store in vector store (FAISS)
☐ Test retrieval quality

Query:
☐ Retrieve relevant docs (k=3-5)
☐ Build context string
☐ Create prompt with context
☐ Call LLM
☐ Return answer with sources
```

## 🚀 Next Steps

1. **Folder 13**: Add tools/agents for more complex tasks
2. **Optimization**: Measure and improve retrieval metrics
3. **Scaling**: Deploy to production with caching

## 📖 Related Topics

- **Folder 8**: Document loading (YouTube transcripts)
- **Folder 9**: Text splitting (chunking strategy)
- **Folder 4**: Embeddings (vector generation)
- **Folder 10**: Vector stores (FAISS)
- **Folder 11**: Retrievers (advanced search)

---

**RAG Pipeline Complete! 🚀**