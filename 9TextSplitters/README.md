# 📖 Folder 9: Text Splitters

## 🎯 Objective

Split large documents into smaller chunks that fit in LLM context window. Use intelligent chunking strategies while maintaining quality.

## 📚 Theory & Concepts

### **Problem: Context Window Limits**

```
LLM Context Window: 8,000 tokens (~6000 words)

Large Document: 50,000 words
                     ↓
Cannot fit directly (would lose information)
                     ↓
Solution: Split into 8-10 chunks of ~6000 words each
                     ↓
Process one by one or combine strategically
```

### **Token Counting**

```
Rough Estimation:
1 token ≈ 4 characters ≈ 0.75 words

Example:
"Hello world" = 2 words = ~2.7 tokens
Document = 1000 words = ~750 tokens

LLM with 8K context = ~6000 words max per request
```

### **Chunking Strategies**

```
1. CharacterTextSplitter
   └── Split by separator (e.g., "\n\n")
   └── Simple, fast

2. RecursiveCharacterTextSplitter
   └── Try multiple separators hierarchically
   └── Better structure preservation

3. SemanticTextSplitter
   └── Split based on meaning, not characters
   └── Experimental, slower

4. DocumentStructuredTextSplitter
   └── Preserve document structure (headers, etc.)
   └── Language-aware
```

### **Chunk Size vs Overlap**

```
chunk_size = 1000 characters
chunk_overlap = 200 characters

Document: "A" (1000) + "B" (1000) + "C" (1000)
                        ↓
Chunk 1: "A" + first 200 of "B"
Chunk 2: Last 200 of "A" + "B" + first 200 of "C"
Chunk 3: Last 200 of "B" + "C"

Advantage: No context lost at boundaries
```

### **Separator Hierarchy (Recursive)**

```
Try in order:
1. "\n\n" (paragraphs) - Best for meaning
2. "\n"   (lines) - Good for preserving structure
3. " "    (words) - Maintain word integrity
4. ""     (characters) - Last resort
```

## 📁 Files Overview

### **CharacterTextSplitting.py**
```
Method: Split by single separator
Splitter: CharacterTextSplitter
Best for: Simple, uniform content
```

### **DocumentStructuredtextSplitter.py**
```
Method: Recursive with document structure
Splitter: RecursiveCharacterTextSplitter
Best for: Complex documents with hierarchy
```

### **SemanticTextSplitting.py**
```
Method: Semantic meaning-based
Splitter: SemanticTextSplitter
Best for: Maintaining semantic coherence
```

### **TextStructuredSpliting.py**
```
Method: Language-aware recursive
Splitter: RecursiveCharacterTextSplitter with language
Best for: Code, markdown, etc.
```

## 🔑 Key Learning Points

### **1. CharacterTextSplitter - Simple**

```python
from langchain_text_splitters import CharacterTextSplitter

text = "Long document text here..."

splitter = CharacterTextSplitter(
    separator="\n\n",              # Split by paragraphs
    chunk_size=1000,               # Max 1000 characters per chunk
    chunk_overlap=200              # 200 char overlap
)

chunks = splitter.split_text(text)
print(f"Total chunks: {len(chunks)}")
print(f"First chunk: {chunks[0]}")
```

### **2. RecursiveCharacterTextSplitter - Smart**

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],  # Try in order
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(long_text)
# Tries "\n\n" first, then "\n", then " ", then ""
```

### **3. With Document Objects**

```python
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

# Load documents (Folder 8)
loader = TextLoader("document.txt")
documents = loader.load()

# Split documents
splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# split_documents preserves metadata!
chunks = splitter.split_documents(documents)

for chunk in chunks:
    print(f"Content: {chunk.page_content[:50]}")
    print(f"Source: {chunk.metadata['source']}")
```

### **4. Language-Specific Splitting**

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

# For Python code
splitter = RecursiveCharacterTextSplitter(
    language="python",
    chunk_size=500,
    chunk_overlap=100
)

code_chunks = splitter.split_text(python_code)

# For Markdown
splitter = RecursiveCharacterTextSplitter(
    language="markdown",
    chunk_size=1000,
    chunk_overlap=200
)

markdown_chunks = splitter.split_text(markdown_text)
```

### **5. Semantic Splitting (Advanced)**

```python
from langchain_text_splitters import SemanticTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings()

splitter = SemanticTextSplitter(
    embeddings=embeddings,
    chunk_size=500  # Approximate
)

# Splits based on semantic similarity
chunks = splitter.split_text(document_text)
```

## 💡 Practical Patterns

### **Pattern 1: Complete Pipeline**

```python
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Step 1: Load
loader = DirectoryLoader("./docs", glob="**/*.txt", loader_cls=TextLoader)
documents = loader.load()

# Step 2: Split
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(documents)

print(f"Loaded {len(documents)} docs → {len(chunks)} chunks")
```

### **Pattern 2: Optimized for Retrieval**

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

# For RAG systems - keep semantic coherence
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,        # ~600 words (safe for context)
    chunk_overlap=400,     # 50% overlap for better retrieval
    separators=["\n\n", "\n", ". ", " ", ""]
)

chunks = splitter.split_documents(documents)

# Each chunk is standalone searchable unit
```

### **Pattern 3: Size Analysis**

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(documents)

# Analyze chunks
sizes = [len(chunk.page_content) for chunk in chunks]
print(f"Min chunk: {min(sizes)} chars")
print(f"Max chunk: {max(sizes)} chars")
print(f"Avg chunk: {sum(sizes)/len(sizes):.0f} chars")
```

## 📊 Splitter Comparison

| Splitter | Speed | Quality | Best For |
|----------|-------|---------|----------|
| Character | ⚡⚡⚡ | ⭐⭐ | Simple content |
| Recursive | ⚡⚡ | ⭐⭐⭐ | Complex docs |
| Semantic | ⚡ | ⭐⭐⭐⭐ | Precise splitting |
| Language-Specific | ⚡⚡ | ⭐⭐⭐ | Code/Markdown |

## 🎓 Advanced Concepts

### **Optimal Chunk Size Calculation**

```
Context Window: 8000 tokens
Input overhead: 500 tokens (system prompt, query)
Available for context: 7500 tokens
Preserve for output: 2000 tokens

Chunk size: (7500 - 2000) / num_relevant_chunks

If using 3 chunks: (5500) / 3 ≈ 1800 tokens per chunk
In characters: 1800 * 4 ≈ 7200 characters per chunk
```

### **Overlap Benefits**

```
Without overlap:
Chunk1 ends:    "...the solution is important because..."
Chunk2 starts:  "...another topic..."
❌ Context lost at boundary

With overlap (200 chars):
Chunk1 ends:    "...the solution is important because..."
Chunk2:         "...important because...another topic..."
✅ Context preserved
```

### **Language-Specific Separators**

```python
# Python code
separators = ["\n\ndef ", "\nclass ", "\n    def ", "\n        def ", "\n"]

# Markdown
separators = ["\n# ", "\n## ", "\n### ", "\n\n", "\n", " "]

# Legal documents
separators = ["\n\n", "\n", ". ", " ", ""]
```

## 📈 Performance Impact

```
Chunk Size | # Chunks | Time to Process | Quality
─────────────────────────────────────────────────
500       | 100      | 10 sec         | ⭐
1000      | 50       | 5 sec          | ⭐⭐
2000      | 25       | 2.5 sec        | ⭐⭐
5000      | 10       | 1 sec          | ⭐⭐ (too large)
```

## ⚠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Chunks too small | Increase chunk_size |
| Chunks too large | Decrease chunk_size |
| Lost context | Increase chunk_overlap |
| Slow splitting | Use CharacterTextSplitter instead of Semantic |

## 💡 Pro Tips

1. **Conservative**: Start with 1000 chunk size, adjust based on results
2. **Overlap**: Use 20-30% overlap for better retrieval
3. **Metadata**: Preserve source metadata with `split_documents()`
4. **Testing**: Test different sizes on your specific data
5. **Caching**: Cache split chunks to avoid re-splitting

## 📚 Recommended Settings

### **For Q&A Systems (RAG)**
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ". ", " ", ""]
)
```

### **For Similarity Search**
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""]
)
```

### **For Code**
```python
splitter = RecursiveCharacterTextSplitter(
    language="python",
    chunk_size=800,
    chunk_overlap=200
)
```

## 🚀 Next Steps

1. **Folder 10**: Store chunks in vector store
2. **Folder 4**: Create embeddings for chunks
3. **Folder 11**: Retrieve chunks efficiently
4. **Folder 12**: Use in RAG pipeline

---

**Text Splitting Mastered! ✂️**